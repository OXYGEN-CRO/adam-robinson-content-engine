---
type: reference
status: draft
owner: adam
created: 2026-09-08
updated: 2026-09-08
sources:
  - brand/BRAND.md
  - raw/sources/2026-09-08-moltsets-brand/manifest.md
tags: [brand, composition, motion]
---

# Composition patterns

Use [[brand/BRAND|Brand]] for identity and [[brand/architecture|Architecture]] for implementation. These are proposed production rules derived from the requested website, not author opinions.

## Choose the relationship first

| Message job | Starting composition | Preserve |
| --- | --- | --- |
| Introduce one thesis | `cover` | Large heading, supporting line, one framed illustration |
| Present a sourced statement | `quote` | Exact quotation, readable source, quiet space |
| Explain a short sequence | `carousel-detail` | Three distinct steps; add or remove steps as content requires |
| Connect input to outcome | `workflow` | Directional arrows, equal node hierarchy, one active operation |
| Attribute a speaker | `lower-third` | Name, true company/role, unobstructed video behind it |
| Open a vertical video | `story` | Large short title, meaningful mascot use, generous top/bottom allowance |
| Present measured evidence | `scorecard` | Value, unit, period, source and comparable basis |

Avoid making every idea into a terminal screenshot. Use the quote or open title when a frame adds no information. For real product demonstrations use a faithful screenshot rather than the illustrative code panel or conceptual map.

## Hierarchy and density

On 1080-wide artwork, prefer a headline of 4–9 words, body at 32 px or larger and at most one secondary paragraph. Keep critical sources at 24 px or larger when the source must be readable in-feed. Micro type is supporting metadata only. These are working limits, not rigid content rules; edit or split dense content instead of shrinking everything.

Read at native size and at 360 px wide. A widescreen diagram also needs a landscape preview; if it must be read in a portrait feed, adapt the diagram vertically. Preserve font proportions. Give punctuation and the key phrase a natural line break.

## Emphasis and frames

Coral selects the main idea. Mint can explain a result or connection. Use the warm surface on one meaningful panel, keeping most of the artwork dark. Yellow, red and purple are not a three-colour topic taxonomy. A full coral background is not the source website's default.

One terminal frame can organize a sequence. Inside it, separate simple steps with space or a dashed rule rather than nesting several terminal frames. Keep corners attached to their border. Use solid arrowheads with enough contrast; labels must not sit on the connector path. The shipped workflow has straight arrows and no ambiguous crossing.

## Motion patterns

For a richer implementation explainer, use [[brand/implementation-graphics]]: a dominant headline, a specific input, open annotations and a worked output with retained evidence. Each region can have a different visual weight. Show the operation with fields and states; a sequence of labelled rectangles alone may not explain enough.

The kit's default entry combines opacity with 24 px vertical travel over 360 ms. This is a component fallback; scene choreography can use masks, path-following, deliberate state changes and varied timing when they explain the action. Never scale text horizontally. Sequence reveals follow the causal order: input, link, operation, link, destination. Preserve the identity of the field or record as it changes. Leave enough hold time to read the complete composition. Use the pixel mascot's original frame sequence for a brief reveal and the thinking sprite only for an actual processing concept.

Static output and reduced-motion output must show all information. Do not add random timing, infinite blinking, auto-playing audio, or repeated whole-frame flashing. The renderer seeks exact times; `data-enter` is a start in milliseconds and `data-draw` is a connector start. A static frame is never dependent on playback finishing.

The CTA component has no default ask. Use it only when the current brief provides a useful next step. A footer may hold a source or page number without becoming a personal signature.

## Source Notes

- [[raw/sources/2026-09-08-graphics-skill/manifest]]: user requested stronger graphic craft and GIF capability; [[brand/implementation-graphics]] records the proposed extension and example.

- Source visual vocabulary: public MoltSets homepage and CSS captured 2026-09-08; see the dated manifest linked by [[brand/BRAND|Brand]].
- Scale, density, safe areas and motion refinements are proposed implementation choices under the user's graphics and motion brief.
