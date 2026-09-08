#!/usr/bin/env python3
"""Check the context structure without interpreting blank prompts as content."""
from pathlib import Path
import re, sys

root = Path(__file__).resolve().parents[1]
errors = []
required = ['AGENTS.md', 'CLAUDE.md', 'README.md', 'index.md', 'log.md', 'strategy/notion-schema.md']
for name in required:
    if not (root / name).is_file():
        errors.append(f'missing file: {name}')
if (root / 'AGENTS.md').read_text() != (root / 'CLAUDE.md').read_text():
    errors.append('AGENTS.md and CLAUDE.md differ')
folders = ['identity', 'audience', 'strategy', 'voice', 'brand', 'inspiration']
def wiki_document(path):
    """Dependencies and local tool artifacts are not author context pages."""
    parts = path.relative_to(root).parts
    return not any(part in {'node_modules', 'output', '__pycache__', 'venv'}
                   or part.startswith('.') for part in parts)

pages = [p for folder in folders for p in (root / folder).rglob('*.md') if wiki_document(p)]
all_pages = [p for p in root.rglob('*.md') if wiki_document(p)]
names = {p.stem for p in all_pages}
for path in pages:
    content = path.read_text()
    frontmatter = re.match(r'^---\n(.*?)\n---\n', content, re.S)
    if not frontmatter:
        errors.append(f'missing frontmatter: {path.relative_to(root)}')
        continue
    for key in ['type','status','owner','created','updated','sources','tags']:
        if not re.search(rf'^{key}:', frontmatter[1], re.M):
            errors.append(f'missing {key}: {path.relative_to(root)}')
    if '\n## Source Notes\n' not in content:
        errors.append(f'missing Source Notes: {path.relative_to(root)}')
    if not re.search(r'\[\[.+?\]\]', content):
        errors.append(f'missing related link: {path.relative_to(root)}')
for path in [root/'index.md', *pages]:
    for link in re.findall(r'\[\[(.+?)\]\]', path.read_text()):
        target = link.split('|')[0].split('#')[0]
        if not (root/target).exists() and not (root/(target+'.md')).exists() and target not in names:
            errors.append(f'broken link: {target}')
# A library hub can index detailed notes without listing every note on the home page.
# Require every context page to be reachable through wiki links from index.md.
context_paths = {p.relative_to(root).with_suffix('').as_posix(): p for p in pages}
context_stems = {}
for target, path in context_paths.items():
    context_stems.setdefault(path.stem, []).append(target)
reachable, queue = set(), [root/'index.md']
while queue:
    current = queue.pop()
    for link in re.findall(r'\[\[(.+?)\]\]', current.read_text()):
        target = link.split('|')[0].split('#')[0].removesuffix('.md')
        if target not in context_paths:
            matches = context_stems.get(target, [])
            target = matches[0] if len(matches) == 1 else target
        if target in context_paths and target not in reachable:
            reachable.add(target)
            queue.append(context_paths[target])
for target in context_paths:
    if target not in reachable:
        errors.append(f'not reachable from index: {target}')
for error in errors:
    print(error)
if errors:
    sys.exit(1)
print(f'wiki lint passed: {len(pages)} context pages; agent rules match')
