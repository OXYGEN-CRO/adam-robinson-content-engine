---
type: source
status: captured
owner: adam
created: 2026-09-08
updated: 2026-09-08
sources: []
tags: [source, launch-video, local-import]
---

# Launch-video workflow and assets — source manifest

## Scope

The user requested importing the launch-video skill and reusable sound assets from their Oxygen knowledge repo, applying MoltSets branding, and planning a public launch around credit-pricing frustration and Claude Code. The exact brief is in `brief.txt`.

The requested `~/oxyen-knowledge` resolved to `/Users/timscheuer/oxygen-knowledge`. Source skill: `gtm-production/.claude/skills/launch-video/SKILL.md`. Actual implementation: `gtm-production/content/motion/launch-video/` (some source-relative paths predate a move).

## Preserved material

- `files.json`: source paths and SHA-256 hashes for 13 exact reference files.
- `original/`: exact source skill, selected generator/timing/mixing files, music prompts and shorts-kit notes, saved with `.txt` suffixes as archival reference rather than active instructions.
- `claim-sources.json`: current public first-party URLs, checked date and bounded findings for campaign claims.
- `brief.txt`: supplied human brief.
- Reusable audio copies and their per-file manifest: `brand/motion/audio/library/`.
- Three third-party reference logos and their manifest: `brand/motion/logos/third-party/`.

Observed source-repository HEAD: `9edc7ae5e4ffab76d725e568de19c7fd04cffd99`. This records the checkout, not a claim that all source files were committed. Per-file hashes identify the exact working-tree bytes copied. No source-repository files were edited. No credentials or narration were copied, no new audio was generated and no publication was performed.

## Interpretation and boundaries

The active destination skill adapts the workflow to the local brand and allows planning-only delivery. OXYGEN's fixed voice, visual scenes, deletion of shared audio directories and mandatory Drive/content-post instructions are retained only in the archived original, not applied here.

Existing audio was identified by generation prompts, decoded and measured. It was not subjectively auditioned in this pass. Original files do not establish the generating account's commercial-use entitlement. Logo originals were found in the source repository; their original download URLs were not recorded in the inspected files. Check selected artwork before final public render.

## Source Notes

Human intent is authoritative for the planned public launch; the current website still advertises closed beta. The proposed storyboard is filed at [[strategy/moltsets-launch-video]], with current billing ambiguities recorded rather than silently resolved. The raw source snapshot remains append-only.
