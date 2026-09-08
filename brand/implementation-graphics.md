---
type: reference
status: draft
owner: adam
created: 2026-09-08
updated: 2026-09-08
sources:
  - raw/sources/2026-09-08-graphics-skill/manifest.md
  - brand/BRAND.md
tags: [brand, graphics, gif, implementation, motion]
---

# Implementation graphics with motion

## Direction

The user asked for stronger graphic craft and GIF support, taking inspiration from `~/personal-brand`. Extend the existing MoltSets foundation through composition and movement: a strong typographic focal point, open annotations, an identifiable working artifact and selective state changes. The palette, font family and original logo remain the identity anchors. These are proposed production extensions under this brief, not a newly approved personal identity.

Use the updated [graphics-designer skill](../skills/graphics-designer/SKILL.md). Its composition reference supplies choices beyond equal cards; its motion reference covers choreography, deterministic rendering and inspected GIF/MP4/static delivery.

## Proposed shareable graphic

**Build a lead list you can explain.** A practical recipe for GTM operators: start with a specific request, turn it into filters, check the evidence, and preserve the reason and source with each output row. Proposed pillar: go-to-market. Proposed funnel job: middle, teaching an implementation method. The user asked for an idea; this is a rendered concept that makes the idea reviewable.

The original MoltSets wordmark anchors a large two-line headline. An example request sits in one warm terminal surface. Open numbered operations connect through a travelling coral pixel; the route changes to mint as the illustration resolves into a layered output sheet. The completed composition can stand alone as a useful static graphic.

The example domain `saas.example`, schema fields and review states are illustrative. This is a proposed recipe, not Adam's claimed personal method, a runnable integration, measured processing time or a live product screenshot. The graphic carries “WORKFLOW ILLUSTRATION · EXAMPLE FIELDS.” No lead identities, outcome metrics, pricing claims or invented commands are used.

| Time | Visual job |
| --- | --- |
| 0–1.1s | Headline and request are readable; relevant words are selected. |
| 1.1–2.2s | The input resolves into SaaS, Founder and Austin filters. |
| 2.2–4.1s | The pixel follows the route to the evidence check; sources and missing fields retain distinct treatment. |
| 4.1–4.9s | A row enters the output sheet and its reason stays visible. |
| 4.9–7.2s | The complete graphic holds for reading. |
| 7.2–8.0s | A short reverse reset returns to the opening; the final 120 ms is stable. |

The eight-second animation is illustrative timing. Read the caption and supporting post before sharing; no publication or scheduling was performed by this design task.

## Source and rendering

- Editable [artwork](applications/lead-list-recipe/art.html), [CSS](applications/lead-list-recipe/art.css), [timeline](applications/lead-list-recipe/animation.js) and [export configuration](applications/lead-list-recipe/animation.json).
- Reusable [renderer](render-animation.mjs), using the existing pinned local dependencies.
- Working exports: `output/lead-list-recipe/` — GIF, MP4, static poster, phone preview, review frames, contact sheet, offline review player, export report and a frozen editable dependency bundle.

```sh
node brand/render-animation.mjs brand/applications/lead-list-recipe/animation.json output/lead-list-recipe
```

The example uses 1080 × 1350 at 30 fps for MP4 and 720 × 900 at 20 fps for GIF. Those are chosen production sizes, not verified platform upload limits. The HTML preview defaults to the complete graphic, has play/pause/scrubbing and honours reduced motion. A GIF cannot be assumed to honour the viewer's motion preference; the PNG is the static alternative.

## Inspection record

Rendered and inspected on 2026-09-08: native poster, 360-wide poster, eight source keyframes and sixteen decoded GIF samples. The encoded GIF is 720 × 900, 160 frames, eight seconds and 332,265 bytes. The MP4 is 1080 × 1350, 240 frames and eight seconds; browser playback reached the end with zero dropped frames. The review player's GIF start/stop and the source preview's play/pause/scrub/poster controls passed functional checks.

The renderer verified the actual bundled font, complete-poster text bounds, recorded intermediate masks, repeated/backward seek, matching loop endpoints, reduced-motion poster and exact poster reproduction from the frozen dependency bundle. All three updated skills passed their validator, the existing brand suite passed ten check groups, and wiki lint passed. These checks establish the recorded technical behaviour and sampled visual inspection; no audience-response test or live workflow execution is claimed.

## Related Pages

- [[brand/BRAND]]
- [[brand/patterns]]
- [[brand/architecture]]
- [[strategy/editorial-direction]]
- [[inspiration/launch-motion-quality]]

## Source Notes

- User brief dated 2026-09-08: [[raw/sources/2026-09-08-graphics-skill/manifest]]. “Too simplistic” is the user's critique, not a numerical quality measurement.
- `~/personal-brand` reference inspected read-only: the graphics skill and content-engineering-101 implementation informed static/motion pairing, concrete detail and reusable production. Tim's identity, personal imagery, metrics and CTA conventions were not imported.
- Existing [[brand/BRAND]] establishes company assets, font substitution and current identity scope. The example recipe and choreography are assistant proposals under this brief.
