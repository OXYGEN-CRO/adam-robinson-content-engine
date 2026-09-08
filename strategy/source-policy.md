---
type: context
status: draft
owner: adam
created: 2026-09-08
updated: 2026-09-08
sources: [raw/sources/2026-09-08-brief/brief.md, raw/sources/2026-09-08-brief/retrieval-preference.md, raw/sources/2026-09-08-linkedin-rb2b/manifest.md, AGENTS.md]
tags: [sources, provenance, recency, retrieval]
---

# Source policy and recency

## Summary

This wiki is a research synthesis of Adam Robinson's public material, prepared for the repository owner's brief. It is not an approved biography, campaign or voice guide. The brief requests 200 recent LinkedIn posts, the newest 100 YouTube videos with transcripts, supporting online context and a repository-specific QMD embedding index.

A later request expanded the LinkedIn archive using the existing Oxygen dev / RB2B table. The combined corpus has 914 Adam-profile records from February 2023 through September 2026, including 911 nonempty bodies and three explicitly empty source records. All 979 table rows remain preserved; 65 other-author records are excluded from Adam's corpus. The full available table is captured, but completeness of Adam's lifetime LinkedIn history is unknown. The original 200-post synthesis has been extended through a focused review of 21 older posts. Each addition cites its evidence; this is not a completed semantic review of all 914 records. See [[research/context-expansion-review]].

## Reading claims

- **Author statement:** something Adam says, including revenue and performance claims. Treat it as self-reported unless separate verification is cited.
- **Source-backed fact:** directly supported by a dated, identifiable source. A company's own page supports what it publicly claims, not an independent audit.
- **Interpretation:** a proposed lesson, value, audience, pillar, positioning or content use synthesized from the sources. Such interpretations remain drafts.
- **Unknown:** not established in the collected sources. A template prompt is never evidence.

## Recency rules

Use the latest relevant statement for a present-tense description, while retaining earlier statements as dated history. The publication date, period described and capture date are different fields. A recent retelling of an old event does not make the event recent.

Read [[identity/proof]] before using numbers. Preserve company scope, metric definition, currency or unit, timeframe and claim strength. Do not combine one company's ARR with another company's profit, turn a run rate into realized annual profit, turn a forecast into a result, or describe an aspiration as a milestone. A newer mention only supersedes an older one when they describe the same thing.

## Source use and attribution

Raw captures are append only. Exact machine responses, platform captions and normalized readable source pages serve different purposes; the manifests identify them. Auto captions can mishear company names and numbers. Read the timestamped passage and surrounding context; do not silently correct the preserved raw caption. Separate Adam's speech from hosts, guests and reposted material.

Distinct uploads can reuse footage. Some interviews append another guest's teaser after the goodbye; other uploads are clips of a longer conversation. The archive counts selected uploads, not independent observations. Check the speaker and recording context before assigning an ending's claim to the headline guest, and do not count repeated engagement or revenue figures as additional results. Reviewed corrections belong in the wiki derivative with source evidence; original captions and model outputs remain intact.

Public availability establishes research access, not approval for reuse in new public copy. This task authorizes the local second brain and retrieval setup. It does not authorize publication, scheduling, outreach or new claims in Adam's name.

## Retrieval

Start at [[index]], then search through `./scripts/qmd.sh`. This wrapper uses an index derived from this checkout's absolute path. Search results point to evidence; retrieve and read the full relevant passage before answering. After changes, `./scripts/qmd-refresh.sh --embed` updates both text search and embeddings. Plain `./scripts/qmd-refresh.sh` only updates text search.

The raw archive is retained for on-demand retrieval. Do not load all post bodies or transcripts into every writing/research context. Read the relevant synthesized pages first, search for the needed evidence, then open only the source passages needed for the claim. The user explicitly requested this separation on 2026-09-08. The home page emphasizes synthesized context; the library and dated manifests provide access to detailed notes and original material.

## Related Pages

- [[identity/proof]]
- [[strategy/pillars]]
- [[voice/linkedin-voice]]
- [[index]]

## Source Notes

- [[raw/sources/2026-09-08-brief/brief]] — user collection brief captured 2026-09-08; the four suggested pillars are the user's proposal, not Adam's approval.
- [[raw/sources/2026-09-08-brief/retrieval-preference]] — preserve raw posts/transcripts and retrieve them on demand, without making the archive prominent in every context.
- [[raw/sources/2026-09-08-linkedin-rb2b/manifest]] — expanded archive, attribution, unchanged overlaps and three missing bodies; includes the later collection instruction.
- Repository `AGENTS.md` — rules for source preservation, unknowns, public-use boundaries and linked context.
