#!/usr/bin/env python3
"""Build an append-only selection manifest after all candidate source files exist."""
import collections
import datetime as dt
import hashlib
import json

from collect_youtube_context import CAPTURE, CHANNEL, ROOT, normalize, save_new

candidates = json.loads((CAPTURE / "discovery/candidates.json").read_text())
records = []
for entry in candidates:
    row = normalize(CAPTURE / "videos" / entry["id"])
    assert row and row["word_count"] > 0, f"Missing transcript: {entry['id']}"
    row.update({"surface": entry["tab_title"].rsplit(" - ", 1)[-1], "surface_rank": entry["tab_rank"],
                "url": f"https://www.youtube.com/watch?v={entry['id']}"})
    row["sort_timestamp"] = row.get("release_timestamp") or row["timestamp"]
    row["public_release_utc"] = dt.datetime.fromtimestamp(row["sort_timestamp"], dt.timezone.utc).isoformat()
    records.append(row)
records.sort(key=lambda row: (row["sort_timestamp"], row["id"]), reverse=True)
assert len(records) == len(set(row["id"] for row in records)) == 138
selected = records[:100]
assert len(selected) == 100 and all(row["channel_id"] == CHANNEL for row in selected)
for rank, row in enumerate(records, 1):
    row["recency_rank"] = rank
    row["selected_latest_100"] = rank <= 100
save_new(CAPTURE / "all-candidates.json", json.dumps(records, ensure_ascii=False, indent=2) + "\n")
save_new(CAPTURE / "selected-100.json", json.dumps(selected, ensure_ascii=False, indent=2) + "\n")

lines = ["# Adam Robinson — latest 100 YouTube sources", "",
         "Exactly 100 public uploads selected from the supplied channel, across Videos, Live and Shorts, captured 2026-09-08. See [[raw/sources/2026-09-08-youtube/manifest|collection manifest]] for provenance and limitations.", "",
         "| Rank | Public release (UTC) | Surface | Video / timestamped transcript | Words |", "| --- | --- | --- | --- | ---: |"]
for row in selected:
    path = row["markdown_path"][:-3]
    title = row["title"].replace("|", "—")
    lines.append(f"| {row['recency_rank']} | {row['public_release_utc'][:10]} | {row['surface']} | [[{path}|{title}]] | {row['word_count']:,} |")
save_new(CAPTURE / "index.md", "\n".join(lines) + "\n")

report = {"verified_at": dt.datetime.now(dt.timezone.utc).isoformat(), "channel_id": CHANNEL,
          "candidate_count": len(records), "selected_count": len(selected), "unique_selected_ids": len({row['id'] for row in selected}),
          "channel_ids": sorted({row['channel_id'] for row in selected}), "selected_surfaces": dict(collections.Counter(row['surface'] for row in selected)),
          "transcript_origins": dict(collections.Counter(row['transcript_origin'] for row in selected)),
          "selected_word_count": sum(row['word_count'] for row in selected), "selected_duration_seconds": sum(row['duration'] for row in selected),
          "newest": selected[0], "oldest": selected[-1], "first_excluded": records[100],
          "missing_transcripts": [], "missing_metadata": [],
          "caption_coverage": []}
for row in selected:
    transcript = json.loads((ROOT / row['markdown_path']).with_suffix('.transcript.json').read_text())
    segments = transcript['segments']
    last = segments[-1]
    end_seconds = (last['start_ms'] + (last.get('duration_ms') or 0)) / 1000
    report['caption_coverage'].append({'id': row['id'], 'duration_seconds': row['duration'],
                                       'first_segment_seconds': segments[0]['start_ms'] / 1000,
                                       'last_segment_end_seconds': end_seconds,
                                       'ratio_end_to_duration': round(end_seconds / row['duration'], 4)})
save_new(CAPTURE / "verification.json", json.dumps(report, ensure_ascii=False, indent=2) + "\n")

manifest = f"""# Source manifest — Adam Robinson YouTube

- Captured: 2026-09-08; exact per-file UTC timestamps in normalized transcript JSON. Verification: {report['verified_at']}.
- Origin: https://www.youtube.com/channel/{CHANNEL} (channel handle `@retentionadam`, displayed author `Adam Robinson`). Channel metadata links the exact LinkedIn profile supplied by the user.
- Source author: Adam Robinson's official supplied channel; guest conversations also contain guest speech.
- Source dates: latest selected upload {selected[0]['public_release_utc'][:10]} through {selected[-1]['public_release_utc'][:10]}. These are publication/release dates, not necessarily recording dates. Historical references and reposted episodes retain their original event-time context.
- Selection: latest 100 publicly accessible channel uploads across Videos, archived Live and Shorts at capture time. Read the latest 100 entries of Videos and all 14 Live + all 24 Shorts. The discovery response additionally preserves 10 older Videos entries. Resolve individual metadata, deduplicate by video ID, sort descending by `release_timestamp` where supplied (public premiere/live start), otherwise `timestamp` (upload/publication), and select the first 100. There are {report['selected_surfaces'].get('Videos', 0)} Videos and {report['selected_surfaces'].get('Live', 0)} Live entries in the final selection; all Shorts predate its cutoff.
- Boundary evidence: selected rank 100 is `{selected[-1]['id']}` ({selected[-1]['public_release_utc'][:10]}); first excluded is `{records[100]['id']}` ({records[100]['public_release_utc'][:10]}). Unavailable, deleted, private or unlisted uploads are outside the visible public channel listing and cannot be inventoried from it.
- Files: `discovery/channel-flat.json` exact yt-dlp channel/playlist extraction; `discovery/candidates.json` candidate membership; `selected-100.json` exact task selection; `all-candidates.json` 138 resolved sources including boundary evidence; `index.md` linked source catalog; `verification.json` counts and caption end coverage; `videos/VIDEO_ID/VIDEO_ID.info.json` exact yt-dlp metadata; `*.en-orig.json3`/`*.en.json3` exact downloaded captions; `*.transcript.json` normalized timestamped events; `*.md` searchable timestamped rendition. All 138 candidate transcripts are preserved, including 38 outside the latest-100 scope; synthesis of the requested corpus should use `selected-100.json`.
- Method/tool: installed yt-dlp `2026.06.09`, public YouTube access; collection script `scripts/collect_youtube_context.py`, selection/verification script `scripts/finalize_youtube_context.py`. No account cookies, paid transcript service or user credentials used. Three duplicate `en` fetches returned HTTP 429 after successful `en-orig`; metadata-only retries resolved their otherwise absent metadata. Original successful caption files were preserved.
- Transcript completeness: 100/100 selected videos have nonempty English YouTube automatic captions, totaling {report['selected_word_count']:,} words across {report['selected_duration_seconds']/3600:.2f} hours. No open-source ASR fallback was necessary because captions were available for every selected video. These are YouTube's existing machine captions, not human-verified transcripts. Text is preserved without correcting proper names, numbers, dates or transcription errors. Read source context and cross-check contradictory claims.
- Transcript normalization: concatenate the `utf8` values within each JSON3 event, trim surrounding whitespace, omit empty/newline-only events, preserve event start/duration. Source JSON3 remains the authoritative exact response. No diarization; a host or guest speaking in a multi-person conversation cannot be inferred solely from channel ownership.
- Public-use boundaries: public source material gathered at the user's request for private research and author-context synthesis. Public availability does not establish approval to reuse personal stories or exact wording in newly published author copy. No publication, outreach or scheduling authorized by this capture.
- Metric boundaries: self-reported claims are source-dated, not independently verified financial results. Page/channel view, like and subscriber counts are snapshots at capture and must not be presented as company performance. Episode titles may be promotional and can disagree with spoken claims; retain distinctions.

## Related

- [[raw/sources/2026-09-08-youtube/index|Latest 100 transcript catalog]]
- [[identity/proof|Proof and dated metrics]]
- [[identity/backstory|Backstory]]
- [[strategy/pillars|Content pillars]]
"""
save_new(CAPTURE / "manifest.md", manifest)
hashes = []
for path in sorted(CAPTURE.rglob('*')):
    if path.is_file() and path.name != 'SHA256SUMS':
        hashes.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(CAPTURE)}")
save_new(CAPTURE / 'SHA256SUMS', '\n'.join(hashes) + '\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['caption_coverage','newest','oldest','first_excluded']}, indent=2))
