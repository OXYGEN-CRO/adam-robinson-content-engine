#!/usr/bin/env python3
"""Read-only completion audit for this dated latest-100 YouTube capture."""
import collections
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'raw/sources/2026-09-08-youtube'
CHANNEL = 'UCSHn0Px37BjzMqnZBmVWwcQ'
selected = json.loads((BASE / 'selected-100.json').read_text())
candidates = json.loads((BASE / 'discovery/candidates.json').read_text())
discovery = json.loads((BASE / 'discovery/channel-flat.json').read_text())
assert discovery['channel_id'] == CHANNEL
assert discovery['uploader_id'] == '@retentionadam'
assert len(selected) == len({r['id'] for r in selected}) == 100
assert len(candidates) == len({r['id'] for r in candidates}) == 138
assert {r['id'] for r in candidates} == {e['id'] for tab in discovery['entries'] for e in tab['entries'][:100]}

resolved = []
for candidate in candidates:
    vid = candidate['id']
    info = json.loads((BASE / 'videos' / vid / f'{vid}.info.json').read_text())
    assert info['channel_id'] == CHANNEL
    timestamp = info.get('release_timestamp') or info['timestamp']
    resolved.append({'id': vid, 'timestamp': timestamp,
                     'surface': candidate['tab_title'].rsplit(' - ', 1)[-1],
                     'surface_rank': candidate['tab_rank']})
resolved.sort(key=lambda row: (row['timestamp'], row['id']), reverse=True)
assert [r['id'] for r in selected] == [r['id'] for r in resolved[:100]]
for surface in ['Videos', 'Live', 'Shorts']:
    tab = sorted([r for r in resolved if r['surface'] == surface], key=lambda r: r['surface_rank'])
    assert all(a['timestamp'] >= b['timestamp'] for a, b in zip(tab, tab[1:])), surface

event_count = word_count = seconds = 0
coverage = []
for row in selected:
    vid = row['id']
    folder = BASE / 'videos' / vid
    raw = json.loads((folder / f'{vid}.en-orig.json3').read_text())
    normalized = json.loads((folder / f'{vid}.transcript.json').read_text())
    info = json.loads((folder / f'{vid}.info.json').read_text())
    markdown = (folder / f'{vid}.md').read_text()
    assert normalized['video_id'] == info['id'] == row['id']
    assert normalized['transcript_origin'] == 'youtube_automatic_captions'
    assert 'en-orig' in info['automatic_captions']
    exact = [''.join(s.get('utf8', '') for s in e.get('segs', [])).strip() for e in raw['events']]
    exact = [s for s in exact if s]
    segments = normalized['segments']
    assert exact == [s['text'] for s in segments], vid
    assert all(a['start_ms'] <= b['start_ms'] for a,b in zip(segments, segments[1:])), vid
    assert all(s['text'] in markdown for s in segments), vid
    assert len(segments) == row['segment_count']
    event_count += len(segments)
    counted_words = sum(len(s['text'].split()) for s in segments)
    assert counted_words == row['word_count']
    word_count += counted_words
    seconds += info['duration']
    last = segments[-1]
    end = (last['start_ms'] + (last.get('duration_ms') or 0)) / 1000
    coverage.append(end / info['duration'])
    assert end / info['duration'] > .97, vid
    assert segments[0]['start_ms'] / 1000 < 6, vid

hash_lines = (BASE / 'SHA256SUMS').read_text().splitlines()
for line in hash_lines:
    digest, name = line.split('  ', 1)
    assert hashlib.sha256((BASE / name).read_bytes()).hexdigest() == digest, name

print(json.dumps({'status': 'passed', 'channel_id': CHANNEL, 'selected_count': len(selected),
                  'candidate_count': len(candidates), 'selected_surfaces': dict(collections.Counter(r['surface'] for r in selected)),
                  'newest_public_release': selected[0]['public_release_utc'],
                  'oldest_public_release': selected[-1]['public_release_utc'],
                  'first_excluded_id': resolved[100]['id'], 'nonempty_caption_events': event_count,
                  'transcript_words': word_count, 'duration_hours': round(seconds / 3600, 4),
                  'minimum_caption_end_to_video_duration': round(min(coverage), 4),
                  'verified_source_hashes': len(hash_lines),
                  'limitations': ['Auto captions not human/audio-verified', 'No diarization',
                                  'Public visible channel uploads only', 'Publication date may differ from recording date']}, indent=2))
