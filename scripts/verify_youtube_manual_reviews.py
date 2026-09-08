#!/usr/bin/env python3
"""Reconcile automatic coverage flags with hash-bound manual review records.

Exit 0: current flags have valid reviews and the automatic snapshot is complete/error-free.
Exit 1: missing, stale, mismatched or invalid review/input evidence.
Exit 2: current flags have valid reviews, but the automatic snapshot remains incomplete/invalid.
Never edits or clears the automatic audit or review registry. Metadata validates recorded
review scope, not the truth of a finding or exhaustive semantic understanding.
"""
from __future__ import annotations

import argparse
import ast
import datetime as dt
import hashlib
import json
import math
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
AUTO = Path('research/youtube-synthesis-audit.json')
REVIEWS = Path('research/youtube-coverage-reviews.json')
SELECTED = Path('raw/sources/2026-09-08-youtube/selected-100.json')


def digest(content):
    return hashlib.sha256(content).hexdigest()


def seconds(value):
    if not isinstance(value, str) or not re.fullmatch(r'\d{1,3}:\d{2}(?::\d{2})?(?:\.\d{1,3})?', value):
        raise ValueError(f'Invalid timestamp: {value!r}')
    parts = value.split(':')
    if len(parts) == 2:
        hour, minute, second = 0, int(parts[0]), float(parts[1])
    else:
        hour, minute, second = int(parts[0]), int(parts[1]), float(parts[2])
        if minute >= 60:
            raise ValueError(f'Invalid minute: {value!r}')
    if second >= 60:
        raise ValueError(f'Invalid second: {value!r}')
    return hour * 3600 + minute * 60 + second


def interval(value):
    if not isinstance(value, (list, tuple)) or len(value) != 2:
        raise ValueError('Expected a two-number interval')
    if any(isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x) for x in value):
        raise ValueError('Interval must contain finite numbers')
    start, end = value
    if start < 0 or end < start:
        raise ValueError('Invalid interval ordering')
    return [start, end]


def audit(root, automatic_path=AUTO, reviews_path=REVIEWS):
    root = Path(root).resolve()
    inputs = {}

    def read(rel):
        path = root / rel
        content = path.read_bytes()
        inputs[str(rel)] = digest(content)
        return json.loads(content)

    automatic, registry, selected = read(automatic_path), read(reviews_path), read(SELECTED)
    items = {row['id']: row for row in selected}
    notes = {row['id']: row for row in automatic['notes']}
    report = {
        'audited_at': dt.datetime.now(dt.timezone.utc).isoformat(),
        'helper_sha256': digest(Path(__file__).read_bytes()),
        'input_sha256': inputs,
        'errors': [], 'review_records': [], 'flags': [],
        'automatic_snapshot': {k: v for k, v in automatic.items() if k != 'notes'},
        'automatic_note_errors': [{'id': row['id'], 'errors': row.get('errors', [])} for row in automatic['notes'] if row.get('errors')],
        'automatic_flags': [{'id': row['id'], 'manual_review': row.get('manual_review', [])} for row in automatic['notes'] if row.get('manual_review')],
        'limitations': [
            'Original automatic flags and errors are preserved; this helper never suppresses them.',
            'Valid hashes, paths and intervals identify recorded review evidence, not factual truth or proof of exhaustive semantic reading.',
            'Completion refers only to the supplied automatic-audit snapshot, not a live inventory or independent rerun of extraction checks.',
            'A manual finding resolves only its matched heuristic and does not override structural errors, terminal-output checks or source uncertainty.',
        ],
    }

    def error(code, detail):
        report['errors'].append({'code': code, 'detail': detail})

    if len(items) != 100 or len(selected) != 100 or automatic.get('selected_count') != 100:
        error('selection_mismatch', 'Expected the exact 100 selected videos')
    if len(notes) != len(automatic['notes']) or set(notes) != set(items):
        error('automatic_note_identity_mismatch', 'Automatic audit must contain one row for every selected ID')
    actual_error_count = len(automatic.get('errors', [])) + sum(len(row.get('errors', [])) for row in automatic['notes'])
    flag_count = sum(len(row.get('manual_review', [])) for row in automatic['notes'])
    if actual_error_count != automatic.get('error_count') or flag_count != automatic.get('manual_review_count'):
        error('automatic_summary_mismatch', 'Automatic error/flag counts do not match the preserved detail records')

    units = []
    for row in automatic['notes']:
        for index, flag in enumerate(row.get('manual_review', [])):
            base = {'video_id': row['id'], 'automatic_flag_index': index, 'code': flag['code'], 'detail': flag['detail']}
            if flag['code'] == 'large_lesson_anchor_gap':
                match = re.fullmatch(r'Long spans between meaningful lesson anchors: (\[.*\]); introductions/outros can explain some gaps, inspect the actual source', flag['detail'])
                try:
                    gaps = ast.literal_eval(match.group(1)) if match else None
                    if not isinstance(gaps, list) or not gaps:
                        raise ValueError('Gap list missing')
                    for gap in gaps:
                        units.append({**base, 'flagged_interval_seconds': interval(gap)})
                except (SyntaxError, ValueError, TypeError) as exc:
                    error('automatic_gap_unparseable', f"{row['id']}: {exc}")
                    units.append(base)
            else:
                units.append(base)

    matches = {}
    for index, review in enumerate(registry['reviews']):
        issues = []
        record = {'review_index': index, 'video_id': review.get('video_id'), 'flag_code': review.get('flag_code'), 'errors': issues}
        report['review_records'].append(record)

        def problem(code, detail):
            issues.append({'code': code, 'detail': detail})
            error(code, f'review[{index}]: {detail}')

        try:
            vid = review['video_id']
            if vid not in items or not re.fullmatch(r'[A-Za-z0-9_-]{11}', vid):
                raise ValueError('Video is not in the selected corpus')
            expected_paths = {'source_path': items[vid]['markdown_path'], 'note_path': f'research/youtube-video-notes/{vid}.json'}
            content = {}
            for field, expected in expected_paths.items():
                path = root / expected
                if review.get(field) != expected or not path.resolve().is_relative_to(root):
                    raise ValueError(f'{field} must exactly equal selected canonical path {expected}')
                content[field] = path.read_bytes()
                actual = digest(content[field])
                inputs[expected] = actual
                record[field], record[field.replace('_path', '_sha256')] = expected, actual
                if actual != review.get(field.replace('_path', '_sha256')):
                    problem('review_hash_mismatch', f'{field} bytes changed or declared hash is stale')
            note = json.loads(content['note_path'])
            if note.get('video_id') != vid:
                problem('note_identity_mismatch', vid)
            automatic_checks = notes[vid].get('checks', {})
            canonical = json.dumps(note, sort_keys=True, ensure_ascii=False).encode()
            if automatic_checks.get('data_sha256') != digest(canonical):
                problem('automatic_note_snapshot_stale', vid)
            if automatic_checks.get('source_sha256') != digest(content['source_path']):
                problem('automatic_source_snapshot_stale', vid)
            for field in ('reviewed_at', 'reviewer', 'finding', 'reason', 'limits'):
                if not isinstance(review.get(field), str) or not review[field].strip():
                    problem('review_context_missing', field)
            reviewed_at = dt.datetime.fromisoformat(review['reviewed_at'])
            if not reviewed_at.tzinfo:
                problem('review_date_invalid', 'Timezone required')
            if review.get('finding') != 'reviewed_no_material_gap':
                problem('review_finding_unresolved', 'This helper only recognizes the explicitly recorded no-material-gap disposition')
            read_interval = interval(review['raw_interval_read_seconds'])
            source_end = max(items[vid]['duration'], automatic_checks['source_caption_bounds']['last_end'])
            if read_interval[1] > source_end + 2:
                problem('review_interval_out_of_source_bounds', str(read_interval))
            evidence = review.get('evidence')
            if not isinstance(evidence, list) or not evidence:
                raise ValueError('Nonempty evidence list required')
            evidence_intervals = []
            for evidence_record in evidence:
                if not isinstance(evidence_record, dict) or not isinstance(evidence_record.get('treatment'), str) or not evidence_record['treatment'].strip():
                    raise ValueError('Each evidence record needs a nonempty treatment')
                parts = re.split(r'\s*[–—-]\s*', evidence_record.get('range', ''))
                if len(parts) != 2:
                    raise ValueError('Evidence needs a timestamp range')
                evidence_interval = interval([seconds(x) for x in parts])
                if evidence_interval[0] < read_interval[0] or evidence_interval[1] > read_interval[1]:
                    problem('evidence_outside_read_interval', str(evidence_interval))
                evidence_intervals.append(evidence_interval)
            record.update({'raw_interval_read_seconds': read_interval, 'finding': review.get('finding'), 'reason': review.get('reason'), 'evidence': evidence})
            code = review['flag_code']
            candidates = [(i, unit) for i, unit in enumerate(units) if unit['video_id'] == vid and unit['code'] == code]
            if code == 'thin_claim':
                match = re.fullmatch(r'(key_learnings|backstory_and_values|metrics_and_dates)\.(\d+)', review.get('claim_path', ''))
                if not match:
                    raise ValueError('Invalid claim_path')
                category, number = match.group(1), int(match.group(2))
                claim = note[category][number]
                expected_detail = f'{category}[{number}]: {claim["claim"]}'
                if review.get('flag_detail') != expected_detail:
                    problem('review_claim_detail_mismatch', 'Claim path/text does not match exact recorded thin_claim detail')
                candidates = [(i, unit) for i, unit in candidates if unit['detail'] == review.get('flag_detail')]
                claim_interval = interval([seconds(claim['start_timestamp']), seconds(claim['end_timestamp'])])
                if claim_interval[0] < read_interval[0] or claim_interval[1] > read_interval[1]:
                    problem('review_interval_incomplete', f'Read interval does not cover entire flagged claim {claim_interval}')
                if not any(a <= claim_interval[0] and b >= claim_interval[1] for a, b in evidence_intervals):
                    problem('claim_evidence_range_missing', 'No cited evidence range covers the complete claim anchor')
                record.update({'claim_path': review['claim_path'], 'exact_flag_detail': expected_detail, 'claim_interval_seconds': claim_interval})
            elif code == 'large_lesson_anchor_gap':
                flagged = interval(review['flagged_interval_seconds'])
                candidates = [(i, unit) for i, unit in candidates if unit.get('flagged_interval_seconds') == flagged]
                if not candidates:
                    problem('review_flag_interval_mismatch', 'Recorded flagged interval does not exactly match the automatic gap')
                if read_interval[0] > flagged[0] or read_interval[1] < flagged[1]:
                    problem('review_interval_incomplete', 'Read interval does not cover the entire automatic flagged gap')
                record['flagged_interval_seconds'] = flagged
            else:
                raise ValueError(f'Unsupported review flag code {code}')
            if len(candidates) != 1:
                problem('review_flag_match_not_unique', f'Expected one matching current flag unit, found {len(candidates)}')
            else:
                unit_index, unit = candidates[0]
                if unit_index in matches:
                    problem('duplicate_review_for_flag', str(unit_index))
                else:
                    matches[unit_index] = index
        except (KeyError, IndexError, TypeError, ValueError, OSError) as exc:
            problem('review_invalid', str(exc))

    for index, unit in enumerate(units):
        review_index = matches.get(index)
        state = 'unreviewed' if review_index is None else 'invalid_review' if report['review_records'][review_index]['errors'] else 'reviewed'
        report['flags'].append({**unit, 'review_index': review_index, 'review_status': state})
        if state == 'unreviewed':
            error('unreviewed_automatic_flag', f"{unit['video_id']} {unit['code']}: {unit['detail']}")
    for rel, expected_hash in inputs.items():
        if digest((root / rel).read_bytes()) != expected_hash:
            error('input_changed_during_audit', rel)
    report['current_flags_reviewed'] = not report['errors'] and all(x['review_status'] == 'reviewed' for x in report['flags'])
    report['automatic_error_count_preserved'] = actual_error_count
    report['automatic_flag_count_preserved'] = flag_count
    report['flag_unit_count'] = len(units)
    report['reviewed_flag_unit_count'] = sum(x['review_status'] == 'reviewed' for x in report['flags'])
    report['all_100_complete_in_automatic_snapshot'] = actual_error_count == 0 and all(automatic.get(k) == 100 for k in ('selected_count', 'extraction_count', 'promoted_count', 'structurally_valid_note_count'))
    if not report['current_flags_reviewed']:
        report['status'], report['exit_code'] = 'manual_reviews_invalid_or_incomplete', 1
    elif not report['all_100_complete_in_automatic_snapshot']:
        report['status'], report['exit_code'] = 'current_flags_reviewed_automatic_snapshot_incomplete_or_invalid', 2
    else:
        report['status'], report['exit_code'] = 'current_flags_reviewed_automatic_snapshot_complete_with_stated_limits', 0
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--automatic-audit', default=str(AUTO))
    parser.add_argument('--reviews', default=str(REVIEWS))
    parser.add_argument('--output', default='research/youtube-manual-review-audit.json')
    args = parser.parse_args()
    output = (ROOT / args.output).resolve()
    protected = {(ROOT / p).resolve() for p in (args.automatic_audit, args.reviews, SELECTED)}
    if not output.is_relative_to((ROOT / 'research').resolve()) or output in protected:
        raise SystemExit('Output must be a separate research report; input files cannot be overwritten')
    try:
        report = audit(ROOT, Path(args.automatic_audit), Path(args.reviews))
    except (KeyError, TypeError, ValueError, OSError) as exc:
        report = {'status': 'manual_review_inputs_invalid', 'current_flags_reviewed': False, 'exit_code': 1,
                  'errors': [{'code': 'input_invalid', 'detail': str(exc)}],
                  'limitations': ['No original audit, review registry or source file was changed.']}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ('status', 'current_flags_reviewed', 'exit_code')}, indent=2))
    print(f'Audit: {output.relative_to(ROOT)}')
    return report['exit_code']


if __name__ == '__main__':
    raise SystemExit(main())
