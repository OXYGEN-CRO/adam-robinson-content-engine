#!/usr/bin/env python3
"""Audit completed YouTube extractions without modifying sources or worker state.

Exit 0: all 100 pass structural checks, with no heuristic review flags.
Exit 1: missing/invalid artifacts or provenance.
Exit 2: structural checks pass, but coverage/content needs manual review.
Heuristics expose questionable coverage; they do not prove semantic completeness.
Only the requested research audit report is written.
"""
from __future__ import annotations

import argparse
import ast
import collections
import datetime as dt
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = Path('raw/sources/2026-09-08-youtube')
NOTES = Path('research/youtube-video-notes')
RUN = Path('output/youtube-synthesis')
WIKI = Path('strategy/video-notes')
CLAIM_FIELDS = ('claim', 'start_timestamp', 'end_timestamp', 'speaker', 'claim_type', 'pillar', 'caveat')
CATEGORIES = ('key_learnings', 'backstory_and_values', 'metrics_and_dates')
CLAIM_TYPES = {'adam_self_report', 'adam_opinion', 'guest_statement', 'host_statement', 'interpretation', 'uncertain_speaker'}
TOP_FIELDS = {'video_id', 'title', 'published', 'speakers_and_attribution', 'summary', *CATEGORIES,
              'tensions_and_corrections', 'reusable_topics', 'coverage'}
KNOWN_DIAGNOSTICS = ('`--dangerously-bypass-hook-trust` is enabled.',
                     'Skill descriptions were shortened to fit the skills context budget.')


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def timestamp(value):
    if not isinstance(value, str) or not re.fullmatch(r'\d{1,3}:\d{2}(?::\d{2})?(?:\.\d{1,3})?', value):
        raise ValueError(f'Invalid timestamp {value!r}; expected MM:SS or HH:MM:SS')
    parts = value.split(':')
    if len(parts) == 2:
        minutes, seconds = int(parts[0]), float(parts[1])
        hours = 0
    else:
        hours, minutes, seconds = int(parts[0]), int(parts[1]), float(parts[2])
        if minutes >= 60:
            raise ValueError(f'Invalid minute field {value!r}')
    if seconds >= 60:
        raise ValueError(f'Invalid second field {value!r}')
    return hours * 3600 + minutes * 60 + seconds


def prompt_contract(root):
    """Read a literal; never import or execute the running pipeline."""
    code = (root / 'scripts/synthesize_youtube.py').read_text()
    tree = ast.parse(code)
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'INSTRUCTIONS' for t in node.targets):
            value = ast.literal_eval(node.value)
            if isinstance(value, str):
                return value, digest(code)
    raise ValueError('Cannot independently reconstruct prompt: literal INSTRUCTIONS missing')


def reviewed_wiki_data(root, vid, data, error):
    """Independently verify declared derivatives; terminal evidence stays original."""
    expected = json.loads(json.dumps(data))
    registry = root / 'research/youtube-note-corrections.json'
    if not registry.exists():
        return expected, []
    applied = []
    for correction in json.loads(registry.read_text())['corrections']:
        if correction['video_id'] != vid:
            continue
        try:
            note_bytes = (root / NOTES / f'{vid}.json').read_bytes()
            if hashlib.sha256(note_bytes).hexdigest() != correction['note_file_sha256']:
                raise ValueError('Original model-output hash changed')
            evidence = [{'path': correction['evidence_path'], 'sha256': correction['evidence_sha256']},
                        *correction.get('supporting_evidence', [])]
            for record in evidence:
                path = root / record['path']
                if hashlib.sha256(path.read_bytes()).hexdigest() != record['sha256']:
                    raise ValueError(f"Evidence hash changed: {record['path']}")
            if correction.get('source_fields'):
                metadata = json.loads((root / correction['evidence_path']).read_text())
                if any(metadata.get(k) != v for k,v in correction['source_fields'].items()):
                    raise ValueError('Declared metadata fields differ from archived evidence')
            field = correction['field']
            if field in ('tensions_and_corrections', 'coverage.limitations'):
                values = expected['coverage']['limitations'] if field == 'coverage.limitations' else expected[field]
                matches = [i for i,value in enumerate(values) if value == correction['original']]
                if len(matches) != 1:
                    raise ValueError('Expected one exact original list value')
                parent, key = values, matches[0]
            elif field in ('summary', 'speakers_and_attribution'):
                parent, key = expected, field
            elif re.fullmatch(r'(key_learnings|backstory_and_values|metrics_and_dates)\.\d+', field):
                category, index = field.split('.')
                parent, key = expected[category], int(index)
            else:
                raise ValueError(f'Unsupported derivative field {field}')
            if parent[key] != correction['original']:
                raise ValueError('Declared original differs from model field')
            replacement = correction['replacement']
            if isinstance(parent[key], dict):
                if not isinstance(replacement, dict) or set(replacement) != set(CLAIM_FIELDS):
                    raise ValueError('Replacement claim has invalid shape')
                if any(not isinstance(replacement[k], str) or not replacement[k] for k in CLAIM_FIELDS):
                    raise ValueError('Replacement claim fields must be nonempty text')
                if replacement['claim_type'] not in CLAIM_TYPES:
                    raise ValueError('Replacement claim has invalid attribution type')
                start, end = timestamp(replacement['start_timestamp']), timestamp(replacement['end_timestamp'])
                if start < 0 or end < start:
                    raise ValueError('Replacement claim has invalid time range')
                if any(replacement[k] != parent[key][k] for k in ('start_timestamp', 'end_timestamp')):
                    raise ValueError('Attribution corrections must preserve the original verified source anchors')
            elif not isinstance(replacement, str) or not replacement:
                raise ValueError('Replacement text is empty or invalid')
            parent[key] = json.loads(json.dumps(replacement))
            applied.append({'field': field, 'kind': correction['kind'], 'evidence_path': correction['evidence_path']})
        except (KeyError, IndexError, TypeError, ValueError, OSError) as exc:
            error('reviewed_derivative_invalid', f"{correction.get('field')}: {exc}")
    return expected, applied


def audit_note(root, item, instructions):
    vid = item['id']
    report = {'id': vid, 'errors': [], 'manual_review': [], 'diagnostics': [], 'checks': {}}
    errors, reviews = report['errors'], report['manual_review']

    def error(code, detail):
        errors.append({'code': code, 'detail': detail})

    def review(code, detail):
        reviews.append({'code': code, 'detail': detail})

    def read_json(path, label):
        try:
            return json.loads((root / path).read_text())
        except (OSError, ValueError) as exc:
            error(f'{label}_unavailable', f'{path}: {exc}')
            return None

    data = read_json(NOTES / f'{vid}.json', 'extraction')
    if data is None:
        return report
    if not isinstance(data, dict):
        error('extraction_shape', 'Top-level extraction must be an object')
        return report
    report['checks']['extraction_present'] = True
    if set(data) != TOP_FIELDS:
        error('schema_fields', f'Missing {sorted(TOP_FIELDS - set(data))}; extra {sorted(set(data) - TOP_FIELDS)}')
    for field, expected in [('video_id', vid), ('title', item['title']), ('published', item['public_release_utc'])]:
        if data.get(field) != expected:
            error('identity_mismatch', f'{field}: {data.get(field)!r} != {expected!r}')
    for field in ('speakers_and_attribution', 'summary'):
        if not isinstance(data.get(field), str) or not data[field].strip():
            error('empty_context', field)
    for field in ('tensions_and_corrections', 'reusable_topics'):
        value = data.get(field)
        if not isinstance(value, list) or any(not isinstance(s, str) or not s.strip() for s in value):
            error('invalid_string_list', field)

    source_path = Path(item['markdown_path'])
    try:
        source = (root / source_path).read_text()
    except OSError as exc:
        error('source_unavailable', str(exc))
        return report
    transcript = read_json(source_path.with_suffix('.transcript.json'), 'transcript')
    if not isinstance(transcript, dict) or not isinstance(transcript.get('segments'), list) or not transcript['segments']:
        error('transcript_empty', str(source_path))
        return report
    segments = transcript['segments']
    first = segments[0]['start_ms'] / 1000
    last_start = segments[-1]['start_ms'] / 1000
    last_end = (segments[-1]['start_ms'] + (segments[-1].get('duration_ms') or 0)) / 1000
    duration = item['duration']
    actual_words = sum(len(s['text'].split()) for s in segments)
    report['checks']['source_caption_bounds'] = {'first': first, 'last_start': last_start, 'last_end': last_end, 'video_duration': duration}
    if actual_words != item['word_count']:
        error('source_word_count', f'{actual_words} actual vs {item["word_count"]} selected metadata')

    provenance = read_json(NOTES / f'{vid}.provenance.json', 'provenance')
    if not isinstance(provenance, dict):
        error('provenance_shape_invalid', 'Provenance must be a nonempty object with source/prompt hashes and successful run metadata')
    else:
        expected = {'id': vid, 'source_path': item['markdown_path'], 'source_sha256': digest(source),
                    'source_characters': len(source), 'source_word_count': actual_words, 'exit_code': 0}
        for field, value in expected.items():
            if provenance.get(field) != value:
                error('provenance_mismatch', f'{field}: {provenance.get(field)!r} != {value!r}')
        meta = {k:item[k] for k in ('id', 'title', 'public_release_utc', 'duration', 'word_count', 'markdown_path')}
        reconstructed = (instructions + '\nSOURCE_METADATA\n' + json.dumps(meta, ensure_ascii=False)
                         + '\nBEGIN_UNTRUSTED_TRANSCRIPT\n' + source + '\nEND_UNTRUSTED_TRANSCRIPT\n')
        prompt_file = root / RUN / f'{vid}.prompt.txt'
        if prompt_file.exists():
            prompt = prompt_file.read_text()
            report['checks']['prompt_evidence'] = 'persisted prompt artifact'
            if source not in prompt:
                error('prompt_missing_full_source', 'Persisted prompt does not contain complete source text')
        else:
            prompt = reconstructed
            report['checks']['prompt_evidence'] = 'reconstructed from current literal instructions and original source/metadata'
        if provenance.get('prompt_sha256') != digest(prompt):
            error('prompt_hash_mismatch', 'Input prompt hash cannot be reproduced; preserve the exact historic prompt if the contract changed')
        try:
            started = dt.datetime.fromisoformat(provenance['started_at'])
            completed = dt.datetime.fromisoformat(provenance['completed_at'])
            if not started.tzinfo or not completed.tzinfo or completed < started:
                raise ValueError('missing timezone or completion before start')
        except (KeyError, TypeError, ValueError) as exc:
            error('run_dates_invalid', str(exc))
        if not isinstance(provenance.get('pid'), int) or not provenance.get('method'):
            error('run_identity_missing', 'Expected pid and nonempty method in provenance')
        report['checks']['source_sha256'] = digest(source)

    event_path = root / RUN / f'{vid}.events.jsonl'
    try:
        events = [json.loads(line) for line in event_path.read_text().splitlines() if line.strip()]
        terminals = [e for e in events if e.get('type') in ('turn.completed', 'turn.failed')]
        if not any(e.get('type') == 'thread.started' for e in events) or not any(e.get('type') == 'turn.started' for e in events):
            error('run_start_events_missing', 'Expected thread.started and turn.started events')
        if not terminals or terminals[-1].get('type') != 'turn.completed' or any(e.get('type') == 'turn.failed' for e in events):
            error('terminal_success_missing', 'Expected successful turn.completed and no turn.failed')
        else:
            usage = terminals[-1].get('usage', {})
            if not isinstance(usage.get('input_tokens'), int) or usage['input_tokens'] <= 0 or usage.get('output_tokens', 0) <= 0:
                error('terminal_usage_missing', 'Successful terminal event lacks positive input/output token accounting')
            report['checks']['terminal_usage'] = usage
        messages = [e['item']['text'] for e in events if e.get('type') == 'item.completed'
                    and e.get('item', {}).get('type') == 'agent_message' and isinstance(e['item'].get('text'), str)]
        if not messages or json.loads(messages[-1]) != data:
            error('terminal_output_mismatch', 'Final terminal agent message does not match extraction JSON')
        for event in events:
            event_item = event.get('item', {})
            if event.get('type') == 'error' or event_item.get('type') == 'error':
                message = str(event_item.get('message') or event.get('message') or event)
                if message.startswith(KNOWN_DIAGNOSTICS):
                    report['diagnostics'].append(message)
                else:
                    review('runtime_diagnostic', message)
            if event_item.get('type') in ('command_execution', 'file_change', 'mcp_tool_call', 'web_search'):
                review('unexpected_worker_action', f"Reader emitted {event_item.get('type')}; inspect log against bounded read-only task")
    except (OSError, ValueError, TypeError, KeyError) as exc:
        error('events_unavailable_or_invalid', f'{event_path.relative_to(root)}: {exc}')
    response = read_json(RUN / f'{vid}.response.json', 'terminal_response')
    if response is not None and response != data:
        error('response_mismatch', 'Persisted model response differs from extraction; any correction requires recorded provenance')

    coverage = data.get('coverage', {})
    if not isinstance(coverage, dict) or coverage.get('full_transcript_reviewed') is not True:
        error('full_review_not_claimed', 'coverage.full_transcript_reviewed must be true')
        coverage = coverage if isinstance(coverage, dict) else {}
    try:
        reviewed_first = timestamp(coverage.get('first_timestamp_reviewed'))
        reviewed_last = timestamp(coverage.get('last_timestamp_reviewed'))
        if reviewed_first > first + 1 or reviewed_last < last_start - 1:
            error('review_bounds_incomplete', f'Claimed {reviewed_first}–{reviewed_last}; actual captions {first}–{last_start}')
        if reviewed_first > reviewed_last or reviewed_last > max(duration, last_end) + 2:
            error('review_bounds_invalid', f'Claimed {reviewed_first}–{reviewed_last}; video duration {duration}')
    except ValueError as exc:
        error('review_timestamp_invalid', str(exc))
    limitations = coverage.get('limitations')
    if not isinstance(limitations, list) or not limitations or any(not isinstance(s, str) or not s.strip() for s in limitations):
        error('coverage_limitations_missing', 'Expected nonempty list of caveats')

    meaningful = []
    all_claims = []
    counts = {}
    for category in CATEGORIES:
        claims = data.get(category)
        if not isinstance(claims, list):
            error('claim_list_invalid', category)
            continue
        counts[category] = len(claims)
        for i, claim in enumerate(claims):
            label = f'{category}[{i}]'
            if not isinstance(claim, dict) or set(claim) != set(CLAIM_FIELDS):
                error('claim_shape_invalid', label)
                continue
            if any(not isinstance(claim[field], str) for field in CLAIM_FIELDS):
                error('claim_field_type', label)
                continue
            for field in ('claim', 'speaker', 'pillar'):
                if not claim[field].strip():
                    error('claim_field_empty', f'{label}.{field}')
            if claim['claim_type'] not in CLAIM_TYPES:
                error('claim_type_invalid', f'{label}: {claim["claim_type"]}')
            if category == 'metrics_and_dates' and not claim['caveat'].strip():
                error('metric_caveat_empty', label)
            try:
                start, end = timestamp(claim['start_timestamp']), timestamp(claim['end_timestamp'])
                if start > end or end > max(duration, last_end) + 2:
                    error('claim_timestamp_out_of_bounds', f'{label}: {start}–{end}, duration {duration}')
                else:
                    if category == 'key_learnings' and len(claim['claim'].split()) >= 10:
                        meaningful.append((start, end, claim['claim']))
                    if len(claim['claim'].split()) < 8:
                        review('thin_claim', f'{label}: {claim["claim"]}')
                all_claims.append(claim)
            except ValueError as exc:
                error('claim_timestamp_invalid', f'{label}: {exc}')
    report['checks']['claim_counts'] = counts
    if counts.get('key_learnings', 0) < 4:
        error('insufficient_learnings', 'Fewer than four lessons')
    if not counts.get('metrics_and_dates') and re.search(r'\b(ARR|million|billion|revenue|profit)\b|\$', source, re.I):
        review('potential_metrics_omitted', 'Source mentions business/financial quantities but metrics ledger is empty; inspect whether any material metric was omitted')

    long_video = duration >= 1200 or actual_words > 5000
    if long_video:
        if len(meaningful) < 15:
            review('long_video_lesson_count', f'{len(meaningful)} meaningful lessons; prompt requests 15–30+ for long videos')
        width = max(last_start - first, 1)
        max_span = max(180, .20 * width)
        anchors = [(start + end) / 2 for start, end, _ in meaningful if end - start <= max_span]
        third_counts = collections.Counter(min(2, max(0, int((point - first) / width * 3))) for point in anchors)
        report['checks']['meaningful_lesson_anchors_by_third'] = {name: third_counts[i] for i,name in enumerate(('early','middle','late'))}
        report['checks']['broad_lessons_not_counted_as_local_coverage'] = len(meaningful) - len(anchors)
        for i, name in enumerate(('early', 'middle', 'late')):
            if third_counts[i] < 2:
                review('thin_temporal_coverage', f'{name} third has {third_counts[i]} locally anchored substantive lessons; broad ranges do not count as full local coverage')
        points = [first, *sorted(anchors), last_start]
        gaps = [(a,b) for a,b in zip(points, points[1:]) if b - a > max(300, width * .20)]
        if gaps:
            review('large_lesson_anchor_gap', f'Long spans between meaningful lesson anchors: {gaps}; introductions/outros can explain some gaps, inspect the actual source')
    elif meaningful and not any(end >= first + (last_start - first) * .66 for _,end,_ in meaningful):
        review('short_video_late_content_missing', 'No learning reaches the final third; inspect whether substantive ending content was omitted')

    wiki_path = root / WIKI / f'{vid}.md'
    wiki_data, applied_reviews = reviewed_wiki_data(root, vid, data, error)
    report['checks']['reviewed_derivative_fields'] = applied_reviews
    try:
        wiki = wiki_path.read_text()
        report['checks']['wiki_present'] = True
        source_link = f'[[{item["markdown_path"][:-3]}]]'
        if source_link not in wiki or '\n## Source Notes\n' not in wiki:
            error('wiki_source_link_missing', str(wiki_path.relative_to(root)))
        if f'Video ID: {vid}' not in wiki or f'Input SHA-256: {digest(source)}' not in wiki:
            error('wiki_identity_or_hash_missing', str(wiki_path.relative_to(root)))
        if not re.search(r'^---\n.*?^status: draft\n.*?^---\n', wiki, re.S | re.M):
            error('wiki_draft_frontmatter_missing', str(wiki_path.relative_to(root)))
        for label, value in [('summary', wiki_data.get('summary')), ('speakers', wiki_data.get('speakers_and_attribution'))]:
            if isinstance(value, str) and value not in wiki:
                error('wiki_context_omitted', label)
        expected_claim_lines = []
        for category in CATEGORIES:
            for claim in wiki_data[category]:
                expected_line = (f"- **{claim['start_timestamp']}–{claim['end_timestamp']} · {claim['speaker']} · "
                                 f"{claim['claim_type']} · {claim['pillar']}:** {claim['claim']}"
                                 + (f" Caveat: {claim['caveat']}" if claim['caveat'] else ''))
                expected_claim_lines.append(expected_line)
                if expected_line not in wiki.splitlines():
                    error('wiki_claim_render_mismatch', f"{claim['start_timestamp']}: {claim['claim'][:100]}")
        actual_claim_lines = [line for line in wiki.splitlines() if line.startswith('- **')]
        if actual_claim_lines != expected_claim_lines:
            error('wiki_claim_sequence_mismatch', 'Rendered claims must contain exactly the verified sequence, with no stale, duplicate or extra claim lines')
        for text in wiki_data['tensions_and_corrections']:
            if f'- {text}' not in wiki.splitlines():
                error('wiki_tension_omitted', text[:100])
        if json.dumps(wiki_data['coverage'], ensure_ascii=False) not in wiki:
            error('wiki_coverage_render_mismatch', 'Coverage and its limitations differ from the verified derivative')
        if applied_reviews and '[[research/youtube-note-corrections.json]]' not in wiki:
            error('wiki_review_provenance_missing', 'Reviewed derivatives require a visible correction record link')
        for target in re.findall(r'\[\[([^\]|#]+)', wiki):
            path = root / target
            if not path.exists() and not path.with_suffix('.md').exists():
                error('wiki_broken_link', target)
    except OSError as exc:
        error('wiki_unavailable', str(exc))
    report['checks']['data_sha256'] = digest(json.dumps(data, sort_keys=True, ensure_ascii=False))
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default='research/youtube-synthesis-audit.json', help='Research audit report path relative to repo, or - for stdout only')
    args = parser.parse_args()
    errors = []
    selected = json.loads((ROOT / RAW / 'selected-100.json').read_text())
    selected_ids = {r['id'] for r in selected}
    if len(selected) != 100 or len(selected_ids) != 100:
        errors.append({'code': 'selection_count', 'detail': f'{len(selected)} records, {len(selected_ids)} distinct IDs; expected 100'})
    present = {p.stem for p in (ROOT / NOTES).glob('*.json') if not p.name.endswith('.provenance.json')}
    promoted = {p.stem for p in (ROOT / WIKI).glob('*.md')}
    for kind, ids in [('extraction', present), ('wiki', promoted)]:
        if ids - selected_ids:
            errors.append({'code': f'extra_{kind}_ids', 'detail': sorted(ids - selected_ids)})
        if selected_ids - ids:
            errors.append({'code': f'missing_{kind}_ids', 'detail': sorted(selected_ids - ids)})
    instructions, pipeline_hash = prompt_contract(ROOT)
    notes = []
    for item in selected:
        try:
            notes.append(audit_note(ROOT, item, instructions))
        except (KeyError, TypeError, ValueError, OSError) as exc:
            notes.append({'id': item.get('id'), 'errors': [{'code': 'malformed_artifact', 'detail': str(exc)}],
                          'manual_review': [], 'diagnostics': [], 'checks': {}})
    error_count = len(errors) + sum(len(n['errors']) for n in notes)
    review_count = sum(len(n['manual_review']) for n in notes)
    status = 'incomplete_or_invalid' if error_count else 'manual_review_required' if review_count else 'passed_with_stated_limits'
    report = {'audited_at': dt.datetime.now(dt.timezone.utc).isoformat(), 'status': status,
              'selected_count': len(selected), 'extraction_count': len(present & selected_ids),
              'promoted_count': len(promoted & selected_ids),
              'error_count': error_count, 'manual_review_count': review_count,
              'structurally_valid_note_count': sum(not n['errors'] for n in notes),
              'errors': errors, 'pipeline_code_sha256': pipeline_hash,
              'heuristics': {'long_video': 'duration >= 20 minutes OR transcript > 5,000 words',
                             'local_lesson': '>= 10 words; range <= max(180 sec,20% of caption extent)',
                             'third_coverage': 'at least 2 local lesson midpoints in each chronological third',
                             'long_video_lesson_count': '15 meaningful key learnings is a review threshold, not an invented completeness guarantee'},
              'limitations': ['Inputs and terminal outputs are checked, but a model assertion of reading the whole source does not prove exhaustive semantic understanding.',
                             'Temporal/count heuristics identify review candidates; they do not judge factual accuracy or attribution correctness.',
                             'The verifier does not silently clear review flags or manufacture metrics when a source has none.',
                             'When no prompt artifact exists, prompt hash is reconstructed from current literal instructions, supplied source and selected metadata. A changed historical prompt needs preserved evidence.',
                             'The pipeline may be running during this read-only audit. Missing artifacts are a snapshot, not proof that a live worker stopped.',
                             'Automatic captions may contain errors; source timestamp and hash checks do not verify against audio.'],
              'notes': notes}
    if args.output != '-':
        path = Path(args.output)
        path = path if path.is_absolute() else ROOT / path
        if not path.resolve().is_relative_to((ROOT / 'research').resolve()):
            raise SystemExit('Audit output must remain under research/; use --output - for stdout only')
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
        print(json.dumps({k:report[k] for k in ('status','selected_count','extraction_count','promoted_count','structurally_valid_note_count','error_count','manual_review_count')}, indent=2))
        print(f'Audit: {path.relative_to(ROOT)}')
    else:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if error_count else 2 if review_count else 0


if __name__ == '__main__':
    raise SystemExit(main())
