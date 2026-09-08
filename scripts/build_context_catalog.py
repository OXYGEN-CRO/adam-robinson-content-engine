#!/usr/bin/env python3
"""Promote available transcript research notes and rebuild the linked wiki catalogs.
No model calls or raw-source mutations. Run after extraction batches complete.
"""
from pathlib import Path
import importlib.util,json
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('synthesis',ROOT/'scripts/synthesize_youtube.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
items=json.loads((mod.RAW/'selected-100.json').read_text())
linkedin=json.loads((ROOT/'raw/sources/2026-09-08-linkedin-rb2b/posts.normalized.json').read_text())
linkedin_count=len(linkedin)
linkedin_bodies=sum(bool(p['content'].strip()) for p in linkedin)
mod.WIKI.mkdir(parents=True,exist_ok=True)
completed=[]
for item in items:
 p=mod.DEST/f"{item['id']}.json"
 if not p.exists():continue
 data=json.loads(p.read_text());mod.valid(item,data)
 provenance=json.loads((mod.DEST/f"{item['id']}.provenance.json").read_text())
 (mod.WIKI/f"{item['id']}.md").write_text(mod.render(item,data,provenance))
 completed.append(item['id'])
front='---\ntype: context\nstatus: draft\nowner: adam\ncreated: 2026-09-08\nupdated: 2026-09-08\nsources: [raw/sources/2026-09-08-youtube/selected-100.json, raw/sources/2026-09-08-youtube/manifest.md]\ntags: [youtube, source-library, learning-index]\n---\n\n'
lines=[front+'# YouTube learning library','',f'The latest 100 public channel uploads are captured with transcripts. {len(completed)}/100 currently have full-transcript research extractions promoted below. All are draft interpretations; the timestamped source remains the evidence.','', 'The selection spans 2026-04-16 to 2024-08-14: 93 Videos and 7 archived Live uploads. All Shorts precede the cutoff. Thirty-eight extra discovery candidates remain preserved as boundary evidence and are not counted in this learning library.','', '## Read by purpose','','- [[identity/backstory]] and [[identity/proof]] — consolidated chronology and dated social proof.','- [[identity/values]] and [[identity/life-goals]] — motivations and decisions.','- [[strategy/learnings]] — consolidated lessons with their conditions and current direction.','- [[strategy/pillars]] — cross-source topic organization.','- [[voice/linkedin-voice]] — stated process versus observed writing.','', '## Video notes, newest first','','| Rank | Published | Video and research note | Transcript |','| --- | --- | --- | --- |']
for page, label in [('strategy/guest-playbooks', 'Guest and host playbooks, kept separate from Adam’s own proof'), ('strategy/ai-support-playbook', 'AI support: documentation, repair and escalation'), ('strategy/financing-decisions', 'Historical financing decisions and disagreements')]:
 if (ROOT/(page+'.md')).exists():
  lines.insert(lines.index('## Video notes, newest first')-1, f'- [[{page}]] — {label}.')
for x in items:
 title=x['title'].replace('|','/').replace('[','(').replace(']',')')
 note=f"[[strategy/video-notes/{x['id']}|{title}]]" if x['id'] in completed else f'{title} — synthesis pending'
 lines.append(f"| {x['recency_rank']} | {x['public_release_utc'][:10]} | {note} | [[{x['markdown_path'][:-3]}|Source]] |")
lines+=['','## Related Pages','','- [[strategy/source-policy]]','- [[raw/sources/2026-09-08-youtube/index]]','- [[index]]','','## Source Notes','','- [[raw/sources/2026-09-08-youtube/manifest]] — provenance, selection definition, transcription method and public-use boundaries.','- Individual video-note claims are timestamped, identify speakers, distinguish self-report/opinion/guest material, and retain metric ambiguity. They were extracted from the complete supplied transcript, with input hashes saved under `research/youtube-video-notes/`.','- Automatic captions can mishear proper names and figures. Important claims must be checked against the original passage and newer sources before use. A source date does not establish recording date.']
(ROOT/'strategy/youtube-library.md').write_text('\n'.join(lines)+'\n')
lines=['# Adam Robinson — context index','',f'A source-backed working wiki of Adam Robinson’s public writing and speech, captured on 2026-09-08. The archive contains **{linkedin_count} Adam-profile LinkedIn records ({linkedin_bodies} nonempty bodies)** and **100 recent YouTube videos with transcripts**. Context combines the original 200-post LinkedIn sample with a focused review of older posts; the full archive is available for retrieval. Context pages are draft synthesis, not author-approved public copy.','',f'Full-transcript research notes are available for **{len(completed)}/100** selected videos. Read [[strategy/source-policy]] for recency, attribution and metric rules.','', '## Start here','','- [[audience/ideal-follower|Ideal follower and reader decisions]]','- [[strategy/editorial-direction|Practical editorial direction]]','- [[identity/backstory|Backstory and chronology]]','- [[identity/proof|Dated proof ledger and conflicting claims]]','- [[identity/values|Values and decisions]]','- [[identity/positioning|Proposed positioning]]','- [[strategy/pillars|Four proposed content pillars and Adam’s own taxonomy]]','- [[strategy/learnings|Learning map and operating lessons]]','- [[strategy/youtube-library|YouTube learning library]]','- [[voice/linkedin-voice|Observed LinkedIn voice and stated process]]','', '## Context map','']
for folder in ['identity','audience','strategy','voice','brand','inspiration']:
 paths=[p for p in (ROOT/folder).rglob('*.md') if 'video-notes' not in p.parts and 'node_modules' not in p.parts and not any(part.startswith('.') for part in p.relative_to(ROOT).parts)]
 lines+=[f'### {folder}','']
 for p in sorted(paths):
  content=p.read_text();title=next((l[2:] for l in content.splitlines() if l.startswith('# ')),p.stem)
  lines.append(f'- [[{p.relative_to(ROOT).with_suffix("").as_posix()}|{title}]]')
 lines+=['']
lines+=['## Source archive','','Raw material is retained for search and on-demand retrieval; it does not need to be loaded into every context. See the detailed video notes in [[strategy/youtube-library]].','','<details>','<summary>Dated source manifests</summary>','','- [[raw/sources/2026-09-08-brief/manifest|User brief and proposed pillar provenance]]','- [[raw/sources/2026-09-08-linkedin/manifest|Oxygen LinkedIn capture and pagination provenance]]',f'- [[raw/sources/2026-09-08-linkedin-rb2b/manifest|Expanded RB2B LinkedIn archive — {linkedin_count} Adam records]]','- [[raw/sources/2026-09-08-context-expansion/manifest|Context expansion instruction and scope]]','- [[raw/sources/2026-09-08-youtube/manifest|YouTube capture and selection boundary]]','- [[raw/sources/2026-09-08-web/manifest|Supplementary public web sources]]','','</details>','','## Retrieval and boundaries','','Use `./scripts/qmd.sh search "terms" -c context` for exact wording, or structured `query`/`vsearch` for conceptual retrieval. Read the full source behind a hit. After updates, run `python3 scripts/build_context_catalog.py`, then `./scripts/qmd-refresh.sh --embed`. The isolated index belongs to this checkout.','','See [[brand/BRAND]] for the separately developed MoltSets company graphics system and its stated scope. This source-research task does not add personal-brand or public-copy approval. Publishing cadence and current offers require a current brief. See [[log]] for the ingest record.']
(ROOT/'index.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'promoted_notes':len(completed),'selected_videos':100,'index':'index.md'}))
