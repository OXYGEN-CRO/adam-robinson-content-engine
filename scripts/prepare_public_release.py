#!/usr/bin/env python3
"""Create a new, sanitized snapshot without editing raw sources or Git history.

The destination must not exist. Review and scan the export before publishing.
This is a repository-specific release policy, not a general secret detector.
"""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_REPO = 'https://github.com/OXYGEN-CRO/adam-robinson-content-engine'
ALLOWED_ROOTS = {'identity', 'audience', 'strategy', 'voice', 'brand', 'inspiration',
                 'raw', 'research', 'templates', 'scripts', 'skills', '.github'}
ALLOWED_FILES = {'README.md', 'AGENTS.md', 'CLAUDE.md', 'index.md', 'log.md',
                 '.gitignore', '.gitleaks.toml', 'LICENSE', 'THIRD_PARTY_NOTICES.md',
                 'SECURITY.md', 'CONTRIBUTING.md', 'workspace.example.json'}
SECRET_KEY = re.compile(r'^(?:pagination_?token|access_?token|refresh_?token|'
                        r'api_?key|authorization|cookie|cookies|password|'
                        r'client_?secret|private_?key)$', re.I)
SIGNED_QUERY = re.compile(r'(?:^|&)(?:signature|sig|lsig|token|expire|expires|'
                          r'x-amz-signature|x-goog-signature|policy|key-pair-id)=', re.I)

def exclusion(rel):
    p = Path(rel)
    if rel not in ALLOWED_FILES and p.parts[0] not in ALLOWED_ROOTS:
        return 'local workspace or incidental artifact'
    if any(x in p.parts for x in ('node_modules', '__pycache__', '.git', '.obsidian')):
        return 'local runtime or application state'
    if rel in {'strategy/notion.json', 'strategy/notion.local.json', 'workspace.local.json'}:
        return 'workspace-specific connection configuration'
    if p.name.startswith('.env') or p.suffix in {'.pem', '.key', '.pyc', '.log'}:
        return 'credentials or local runtime file'
    if p.name.startswith('SF-Mono-'):
        return 'proprietary reference font'
    if p.suffix.lower() in {'.mp3', '.wav', '.mp4', '.mov', '.webm'}:
        return 'research media or undocumented audio redistribution entitlement'
    if p.parts[0] == 'research' and p.suffix.lower() in {'.png', '.jpg', '.jpeg', '.webp', '.gif'}:
        return 'research-only imagery'
    if p.parts[0] in {'raw', 'research'} and p.suffix.lower() in {'.html', '.htm'}:
        return 'saved third-party website markup'
    return None

def sanitize(value):
    if isinstance(value, dict):
        return {k: '[REDACTED FOR PUBLIC RELEASE]' if SECRET_KEY.fullmatch(k) and v
                else sanitize(v) for k, v in value.items()}
    if isinstance(value, list):
        return [sanitize(v) for v in value]
    if isinstance(value, str) and value.startswith(('https://', 'http://')):
        try:
            u = urlsplit(value)
            if SIGNED_QUERY.search(u.query):
                return urlunsplit((u.scheme, u.netloc, u.path, '', ''))
        except ValueError:
            pass
    return value

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination', type=Path)
    args = parser.parse_args()
    dest = args.destination.resolve()
    if dest.exists():
        parser.error('destination exists; choose a new directory')
    candidates = set(subprocess.check_output(
        ['git', 'ls-files', '-z', '--cached', '--others', '--exclude-standard'],
        cwd=ROOT).decode().split('\0')) - {''}
    dest.mkdir(parents=True)
    omitted, modified, included = [], [], []
    for rel in sorted(candidates):
        source = ROOT / rel
        if not source.exists() or source.is_dir():
            continue
        reason = exclusion(rel)
        if reason:
            omitted.append({'path': rel, 'reason': reason})
            continue
        if source.is_symlink():
            raise ValueError(f'Unexpected symlink in export: {rel}')
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        original = source.read_bytes()
        data = original
        if source.suffix == '.json':
            try:
                parsed = json.loads(original)
                cleaned = sanitize(parsed)
                if parsed != cleaned:
                    data = (json.dumps(cleaned, ensure_ascii=False, indent=2) + '\n').encode()
            except (ValueError, UnicodeDecodeError):
                pass
        target.write_bytes(data)
        shutil.copymode(source, target)
        if data != original:
            modified.append({'path': rel, 'reason': 'removed continuation tokens or signed URL queries',
                             'original_sha256': hashlib.sha256(original).hexdigest(),
                             'public_sha256': hashlib.sha256(data).hexdigest()})
        included.append(rel)
    # Recreate portable discovery links; never copy local absolute symlinks.
    for dirname in ('.agents', '.claude'):
        (dest / dirname).mkdir(exist_ok=True)
        (dest / dirname / 'skills').symlink_to('../skills', target_is_directory=True)
    # Preserve historical capture hashes and generate checks for sanitized bytes.
    sums = dest / 'raw/sources/2026-09-08-youtube/SHA256SUMS'
    if sums.exists():
        original_sums = sums.read_text()
        lines = []
        for line in original_sums.splitlines():
            _, name = line.split('  ', 1)
            lines.append(hashlib.sha256((sums.parent / name).read_bytes()).hexdigest() + '  ' + name)
        rewritten = '\n'.join(lines) + '\n'
        if rewritten != original_sums:
            (sums.parent / 'SHA256SUMS.capture').write_text(original_sums)
            sums.write_text(rewritten)
    manifest = {'date': '2026-09-08', 'public_repository': PUBLIC_REPO,
                'source_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT).decode().strip(),
                'source': 'working-tree snapshot; existing uncommitted content included',
                'history': 'not included; private source history preserved separately',
                'included_files': len(included), 'omitted': omitted, 'sanitized': modified,
                'integrity': 'Source text is retained. SHA256SUMS verifies public bytes; SHA256SUMS.capture preserves original capture hashes when changed.'}
    (dest / 'PUBLIC_RELEASE_MANIFEST.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps({'destination': str(dest), 'included': len(included),
                      'omitted': len(omitted), 'sanitized': len(modified)}, indent=2))

if __name__ == '__main__':
    main()
