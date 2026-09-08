#!/usr/bin/env python3
"""Independently verify exact LinkedIn text and newest-200 selection from raw data."""
from pathlib import Path
import datetime,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'raw/sources/2026-09-08-linkedin'
posts=json.loads((BASE/'posts.normalized.json').read_text())
assert len(posts)==200
assert len({p['id'] for p in posts})==200
assert {p['author_identifier'] for p in posts}=={'retentionadam'}
raw={}
for rel in sorted({p['source_file'] for p in posts}):
 data=json.loads((ROOT/rel).read_text())
 objects=[r['source_payload'] for r in data] if isinstance(data,list) else data['data']['result']['response']['raw']['elements']
 for p in objects:raw.setdefault(str(p['id']),p)
authored=[p for p in raw.values() if p.get('author',{}).get('publicIdentifier')=='retentionadam']
selected=sorted(authored,key=lambda p:datetime.datetime.fromisoformat(p['postedAt']['date'].replace('Z','+00:00')),reverse=True)[:200]
assert [str(p['id']) for p in selected]==[p['id'] for p in posts]
for p in posts:
 source=raw[p['id']]
 assert source['content']==p['content'] and p['content'].strip()
 assert source['linkedinUrl']==p['source_url']
 assert source['postedAt']['date']==p['source_date']
 md=(ROOT/p['markdown_path']).read_text()
 body=md.split('## Exact post text\n\n',1)[1].split('\n\n## Source Notes\n',1)[0]
 assert body==source['content'],p['id']
audit=json.loads((BASE/'selection-audit.json').read_text())
assert audit['post_text_sha256']=={p['id']:hashlib.sha256(p['content'].encode()).hexdigest() for p in posts}
print(json.dumps({'status':'passed','selected_posts':len(posts),'captured_unique_items':len(raw),'captured_adam_posts':len(authored),'source_text_matches':200,'newest':posts[0]['source_date'],'oldest':posts[-1]['source_date'],'method':'Recomputed from exact source objects; byte-equivalent normalized body; raw IDs/date/author sort; no reliance on manifest count alone.'},indent=2))
