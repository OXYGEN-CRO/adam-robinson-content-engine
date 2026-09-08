---
type: research
status: draft
owner: adam
created: 2026-09-08
updated: 2026-09-08
sources: [raw/sources/2026-09-08-brief/brief.md, research/linkedin-collection-audit.json, research/youtube-collection-audit.json, research/youtube-synthesis-audit.json, research/youtube-manual-review-audit.json, research/qmd-coverage-audit.json]
tags: [completion, collection, synthesis, verification]
---

# Collection and integration audit

The requested collection, linked synthesis and QMD embeddings are complete. The reader reached terminal exit 0; all 100 selected video notes are linked into the wiki. The current-file embedding audit passed at 2026-09-08T10:36:25.655401+00:00. Context remains draft interpretation, subject to author review.

| Requirement | Evidence and current result |
| --- | --- |
| Latest 200 Adam-profile LinkedIn posts through Oxygen | Passed exact-body, author, source-ID and recency recomputation. September 7, 2026 to October 20, 2025. 250 unique feed objects retained, including 249 Adam posts and one excluded other-author repost; 200 selected. Fifteen Adam continuation comments also saved. |
| Latest 100 public YouTube uploads with complete transcripts | Passed exact channel, selection, caption normalization and source hashes. April 16, 2026 to August 14, 2024; 93 Videos and seven archived Live uploads. 138 discovery candidates retained. All 100 have English automatic captions, totaling 778,609 words and 69.20 hours; no ASR fallback required. |
| Raw material retained in repo, retrieved on demand | All 962 files in the four dated captures are present and not Git-ignored. Exact provider responses/metadata/captions coexist with full readable posts and timestamped transcripts. Root manifests are collapsed; raw content is not loaded routinely. |
| Full-transcript synthesis and traceable derivatives | Passed: 100/100 notes extracted, promoted and structurally valid, with zero structural errors. Three automatic coverage heuristics have exact source-bound reviews, independently reconciled with exit 0. Twenty correction records across eleven videos change only reviewed derivatives; original model outputs/provenance remain intact. |
| Linked wiki and recency-aware consolidation | Identity, proof, values, audience, voice, four proposed pillars and focused learning hubs are linked from [[index]]. Historical and guest detail remains in per-video notes. All tail reviews are complete; confirmed source defects are corrected. |
| QMD text and embeddings | Passed: 503/503 required documents have exact current text/FTS and complete, finite, nonzero embedding vectors: 200 posts, 100 transcripts, 136 wiki pages, two root pages and 65 supplemental raw Markdown files. Zero missing or stale required embeddings; isolated index content-engine-3b88f9e94f550ba1. Supplemental raw scope includes separately authorized captures. |

Exact phrase search found the September 4 original post; direct retrieval preserved its full wording and date. A structured lexical/vector query about the Robly-to-GetEmails transition returned the relevant March 31 video note. Direct retrieval also returned the newly indexed final support-session note. The final audit checks stored vectors and current disk content, beyond these retrieval examples.

## Verification scope

Capture checks recompute selection and text from raw objects, rather than trusting manifest counts. The YouTube check compares 109,692 nonempty caption events and 695 source hashes. These checks establish capture fidelity, not the accuracy of automatic speech recognition or independently audited business results.

The extraction checker binds the complete source and supplied prompt to successful terminal output, verifies structured content and the exact reviewed rendering, and reports coverage heuristics. Manual reviews retain those flags while recording source-bound findings; an independent reconciliation helper rejects stale or mismatched review evidence. Source-specific substantive audits distinguish full raw reads from full structured-note reads with targeted caption checks. Audio, slides and financial accounts were not independently verified.

The proof ledger prioritizes dated recent operating statements and separates targets, achieved self-reports, company scopes and historical snapshots. The four pillar names are the user's proposed organization; Adam's own stated taxonomy has three parts. Values and positioning remain interpretations subject to author review.

## Source Notes

- [[raw/sources/2026-09-08-linkedin/manifest]] and [collection audit](linkedin-collection-audit.json).
- [[raw/sources/2026-09-08-youtube/manifest]] and [collection audit](youtube-collection-audit.json).
- [[raw/sources/2026-09-08-web/manifest]] and [[raw/sources/2026-09-08-brief/manifest]].
- [[strategy/youtube-library]], [extraction audit](youtube-synthesis-audit.json), [reviewed corrections](youtube-note-corrections.json), and [[research/youtube-manual-review-audit]].
- [[research/qmd-retrieval-scope]] and [current-file/vector audit](qmd-coverage-audit.json).

No Git commit, remote push, Notion publication, scheduling or outreach is part of this task. Separate concurrent MoltSets graphics and copywriting-skill changes are preserved.
