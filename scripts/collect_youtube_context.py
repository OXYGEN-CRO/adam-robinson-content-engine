#!/usr/bin/env python3
"""Collect dated YouTube source evidence; never overwrite an existing source file."""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import pathlib
import subprocess
import time

ROOT = pathlib.Path(__file__).resolve().parents[1]
CAPTURE = ROOT / "raw/sources/2026-09-08-youtube"
WORK = ROOT / "output/youtube-collection"
CHANNEL = "UCSHn0Px37BjzMqnZBmVWwcQ"


def save_new(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        with path.open("x") as f:
            f.write(text)


def normalize(video_dir):
    info_paths = list(video_dir.glob("*.info.json"))
    if not info_paths:
        return None
    info = json.loads(info_paths[0].read_text())
    video_id = info["id"]
    if info.get("channel_id") != CHANNEL:
        raise ValueError(f"Unexpected channel for {video_id}")
    options = list(video_dir.glob("*.en-orig.json3")) or list(video_dir.glob("*.en.json3"))
    if not options:
        return None
    caption = options[0]
    data = json.loads(caption.read_text())
    segments = []
    for event in data.get("events", []):
        text = "".join(s.get("utf8", "") for s in event.get("segs", [])).strip()
        if text:
            segments.append({"start_ms": event.get("tStartMs", 0),
                             "duration_ms": event.get("dDurationMs"), "text": text})
    lang = caption.name[len(video_id) + 1 : -6]
    origin = "youtube_publisher_captions" if lang in info.get("subtitles", {}) else "youtube_automatic_captions"
    transcript = {"video_id": video_id, "title": info.get("title"),
                  "url": f"https://www.youtube.com/watch?v={video_id}",
                  "upload_date": info.get("upload_date"), "channel_id": info.get("channel_id"),
                  "captured_at": dt.datetime.fromtimestamp(caption.stat().st_mtime, dt.timezone.utc).isoformat(),
                  "transcript_origin": origin, "language": lang,
                  "raw_caption_file": str(caption.relative_to(ROOT)),
                  "normalization": "Concatenate utf8 segments per caption event; retain event start and duration; whitespace trim only.",
                  "segments": segments}
    save_new(video_dir / f"{video_id}.transcript.json", json.dumps(transcript, ensure_ascii=False, indent=2) + "\n")
    lines = [f"# {info.get('title')}", "", f"- Video: https://www.youtube.com/watch?v={video_id}",
             f"- Channel: {info.get('channel')} ({info.get('channel_id')})",
             f"- Published: {info.get('upload_date')}", f"- Captured: {transcript['captured_at']}",
             f"- Transcript: {origin}; {lang}",
             f"- Exact captions: {caption.name}",
             "- Public-use boundary: Publicly accessible source, collected for private research/context; reuse in new public copy is not approved.",
             "- Speaker caution: Captions are not diarized. Guest statements must not be attributed to Adam without contextual verification.",
             "", "## Transcript", ""]
    for s in segments:
        seconds = s["start_ms"] // 1000
        stamp = f"{seconds // 3600:02d}:{seconds % 3600 // 60:02d}:{seconds % 60:02d}"
        lines.append(f"[{stamp}] {s['text']}")
    save_new(video_dir / f"{video_id}.md", "\n".join(lines) + "\n")
    return {"id": video_id, "title": info.get("title"), "upload_date": info.get("upload_date"),
            "timestamp": info.get("timestamp"), "release_timestamp": info.get("release_timestamp"),
            "duration": info.get("duration"), "channel_id": info.get("channel_id"),
            "transcript_origin": origin, "segment_count": len(segments),
            "word_count": sum(len(s["text"].split()) for s in segments),
            "markdown_path": str((video_dir / f"{video_id}.md").relative_to(ROOT))}


def collect(entry):
    video_id = entry["id"]
    video_dir = CAPTURE / "videos" / video_id
    existing = normalize(video_dir)
    if existing:
        return existing
    log_path = WORK / f"{video_id}.{int(time.time())}.log"
    cmd = ["yt-dlp", "--no-update", "--no-overwrites", "--skip-download", "--write-info-json",
           "--write-subs", "--write-auto-subs", "--sub-langs", "en-orig,en", "--sub-format", "json3",
           "--js-runtimes", "node", "--sleep-requests", "0.5", "--no-playlist",
           "-o", str(video_dir / "%(id)s.%(ext)s"), f"https://www.youtube.com/watch?v={video_id}"]
    with log_path.open("x") as log:
        result = subprocess.run(cmd, stdout=log, stderr=subprocess.STDOUT, timeout=180)
    normalized = normalize(video_dir)
    return normalized or {"id": video_id, "error": f"No transcript; yt-dlp exit {result.returncode}", "log": str(log_path.relative_to(ROOT))}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--normalize-only", action="store_true")
    args = parser.parse_args()
    WORK.mkdir(parents=True, exist_ok=True)
    if args.normalize_only:
        for path in (CAPTURE / "videos").iterdir():
            if path.name != CHANNEL:
                result = normalize(path)
                if result:
                    print(json.dumps(result), flush=True)
        return
    discovery = json.loads((CAPTURE / "discovery/channel-flat.json").read_text())
    candidates = {}
    for tab in discovery["entries"]:
        for rank, entry in enumerate(tab.get("entries", [])[:100], 1):
            candidates.setdefault(entry["id"], {**entry, "tab_title": tab["title"], "tab_rank": rank})
    save_new(CAPTURE / "discovery/candidates.json", json.dumps(list(candidates.values()), ensure_ascii=False, indent=2) + "\n")
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(collect, entry): entry["id"] for entry in candidates.values()}
        for n, future in enumerate(concurrent.futures.as_completed(futures), 1):
            try:
                result = future.result()
            except Exception as e:
                result = {"id": futures[future], "error": str(e)}
            print(json.dumps({"completed": n, "total": len(futures), **result}), flush=True)


if __name__ == "__main__":
    main()
