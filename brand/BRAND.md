---
type: context
status: active
owner: adam
created: 2026-09-07
updated: 2026-09-08
sources:
  - https://moltsets.com/
  - raw/sources/2026-09-08-moltsets-brand/manifest.md
tags: [brand, design-system, graphics, motion]
---

# MoltSets: terminal graphics and motion

The working system follows **MoltSets**, the company website supplied by the user. The name is styled `moltsets` in the logo. This is a company-derived graphics foundation for Adam's content, not evidence of an independently approved personal identity.

Start with the [visual kit](kit/index.html), [component catalogue](kit/index.html#components), [motion preview](kit/motion.html) and [production instructions](architecture.md). Source colours and assets are observed facts. Graphic scale, spacing, component adaptations and motion rules are proposed production extensions implemented under the user's brief; they are not an official company manual.

## Source of truth

- [tokens.json](tokens.json) owns exact colours, font roles, graphic typography, layout and motion timing. [build.mjs](build.mjs) generates `tokens.css`, `tokens.js`, template HTML and the catalogue.
- [base.css](base.css) owns canvas and type primitives. [components.css](components.css) and [components.mjs](components.mjs) own the shared components and escaped HTML factories.
- [templates/scenes.mjs](templates/scenes.mjs) owns the seven editable example compositions. [templates/manifest.json](templates/manifest.json) registers sizes and generated files.
- `assets/` contains the original mark, source lockup capture, mascot and thinking frames, texture, and a bundled production font with its licence.
- [patterns.md](patterns.md) explains layout choices; [architecture.md](architecture.md) explains extension, export and validation.

## Colours

These values were extracted from the live `moltsets-base.css` on 2026-09-08, not sampled approximately from screenshots. All 22 source colour variables, including tints, chips, dividers and semantic utilities, are preserved in the token file.

| Role | Value | Usage |
| --- | --- | --- |
| Base | `#0A0B0E` | Default canvas |
| Elevated | `#1E1E1E` | Secondary panels |
| Coral / brand | `#F4805D` | Identity, headline emphasis, frames, actions |
| Mint / success | `#34D399` | Results, positive states, meaningful connectors |
| Primary text | `#F1F5F9` | Headlines and reading text |
| Secondary text | `#CBD5E1` | Supporting content |
| Muted text | `#94A3B8` | Sources, labels and metadata |
| Warm panel | `rgba(244,128,93,0.10)` | Source terminal wash over Base |
| Brand background | `#39291D` | Selected operation or warm emphasis |
| Hint | `#FDE047` | Actual cautions or hints |
| Danger | `#F87171` | Actual error states |
| Purple | `#9747FF` | Archived source utility; avoid as a general brand accent |

Use dark text on a coral-filled CTA; white on coral does not provide enough reading contrast. Normal reading text uses Primary, Secondary or Muted on Base, Elevated or the warm panel. Mint is not a substitute for every body paragraph. Semantic colour always has a written label. Faint dividers are decorative; use a stronger source colour or solid wire when a boundary communicates a relationship.

## Fonts

The website declares **SF Mono** at weights 300, 400, 500, 600, 700 and 800. Live inspection confirmed Regular and Bold loaded. Its logo is lowercase SF Mono Bold plus a pixel underscore/chevron. Exact WOFF2 files and original CSS are saved in the dated source archive for reference.

The portable graphics kit uses **Roboto Mono Variable**, weights 100–700, with its SIL OFL licence in `assets/fonts/`. This is an explicit production substitution, not a claim that the website uses Roboto Mono. Apple's published San Francisco terms do not provide general artwork or font redistribution permission; no separate company font licence was supplied. The source fonts therefore stay out of production CSS and packaging. The captured original wordmark preserves the site's actual lettering.

The working scale is 88 px Display, 64 px Headline, 44 px Title, 32 px Body, 24 px Label and 20 px Micro on a 1080-wide graphic. These are production extensions; the website's 12–22 px interface text should not be copied directly onto a social canvas. Use 400 for reading, 500 for labels, 600–700 for emphasis. Keep the font's natural width and use deliberate line breaks. Do not fabricate italics or introduce an unrelated serif accent.

## Style and geometry

Preserve the near-black terminal, coral signal, mint response, pixel mascot, short prompts, square geometry, dashed frames and small corner marks. The source sets glow to `none` and signal intensity to `0`. Avoid adding scanline animation, neon bloom, glass or heavy CRT effects.

Use one main thought, a clear focal point and consistent roles, with enough concrete detail to teach the idea. Richer implementation graphics can combine open numbered annotations, a selected input, a travelling pixel and a layered output artifact. Vary scale, proportion and grouping instead of putting every item in an equal terminal card. These composition and motion extensions are proposed in [[brand/implementation-graphics|Implementation graphics with motion]], following the user's critique of overly simplistic output.

Use an 8 px spacing unit and 72 px default safe margin. Vertical scenes reserve 120 px at top and 220 px at bottom as a working video allowance, not a guarantee about every platform overlay. Corners belong to terminal frames; they are not mandatory decoration on every card.

## Logo and asset use

- [Original mark](assets/logos/moltsets-mark.svg): exact source SVG. Preserve its two colours, aspect ratio and geometry.
- [Original lockup](assets/logos/moltsets-lockup-source.png): transparent 920 × 224 capture of the real header at 8× device scale after font loading and typing completed. [SVG container](assets/logos/moltsets-lockup.svg) embeds that PNG for convenient placement; it is **not an outlined vector wordmark**. Use the PNG at or below native resolution; use the true vector mark for very large or compact placements.
- Keep at least half the mark height clear around the lockup; use 160 px or more for the lockup on a 1080-wide graphic and inspect the destination preview. Avoid recolouring, stretching, tracing or replacing its type.
- `assets/mascot/` contains all seven original reveal frames, at the source 125 × 160 aspect ratio. `assets/thinking/` contains seven original thinking frames. Preserve crisp pixel shapes; do not treat the mascot as a newly commissioned portrait.
- `assets/textures/site-background.png` is the original texture. The graphic template reduces its opacity to keep it behind the message.

The company assets remain MoltSets assets, saved for the company graphics requested by the user. They have not been relicensed as stock art. Do not reuse them for another client. No supplied photograph or personal signature is assumed.

## Components, templates and motion

The catalogue includes 18 working components: logo, mark, eyebrow, terminal frame, status, callout, quote, metric, numbered step, diagram node, connector, code panel, prompt, CTA, footer, mascot, thinking sprite and lower third. They are rendered examples backed by shared HTML factories and CSS, not names in a schema.

Seven prebuilt compositions cover an editorial cover, source quote, carousel detail, widescreen workflow, transparent lower third, vertical scene and square evidence card. Names and company relationship in the lower third come from the user; no job title is invented. Examples are design studies, not approved posts. Metric slots deliberately remain empty. Read [[identity/proof|Proof]] before inserting a number, and [[voice/linkedin-voice|Voice]] before drafting new public copy.

Motion reuses the same DOM and components. `MoltsetsMotion.seek(milliseconds)` gives deterministic frames; defaults show the finished frame. The 4-second, 30 fps example reveals nodes in order, draws their connectors and holds the final idea. Sprite timing, 360 ms entry, 24 px travel and easing live centrally. Reduced-motion users see a stable final composition. The lower third has a true transparent PNG export. See the [motion preview](kit/motion.html).

For a short animated explainer, develop the object's action, readable result and loop reset rather than applying the generic entrance to every layer. The [implementation example](applications/lead-list-recipe/art.html) and [GIF exporter](render-animation.mjs) add an eight-second illustrated recipe with GIF, MP4 and static companions. Its independent `GraphicMotion` timeline keeps scene-specific choreography local; it does not change earlier templates or the shared runtime. See [[brand/implementation-graphics]] for the proposed concept and [[brand/architecture]] for rendering.

## Production and review

Run the commands in [[brand/architecture|Architecture]]. Inspect full-size and small previews. Check the message, original logo, loaded fonts, contrast, safe margins, clipping, source attribution and connector logic. Generated reports establish technical checks, not public approval or factual validation. Pin or copy the complete dependency set when delivering a finished artwork so future shared changes do not alter it.

## Related Pages

- [[formats]]
- [[brand/patterns|Composition patterns]]
- [[brand/architecture|Architecture and usage]]
- [[identity/positioning|Positioning]]
- [[audience/ideal-follower|Audience]]

## Source Notes

- User brief, 2026-09-08: improve the graphics skill and branding, add dynamic GIFs, and propose a shareable implementation graphic using `~/personal-brand` as inspiration. Recorded in [[raw/sources/2026-09-08-graphics-skill/manifest]].

- User brief, 2026-09-08: extract `https://moltsets.com/`, save logo, colours and fonts, build improved prebuilt components for graphics and later motion; use `~/personal-brand` as structural inspiration.
- [Dated capture](../raw/sources/2026-09-08-moltsets-brand/manifest.md): exact HTML/CSS, source token extraction, asset hashes, source fonts, screenshot and lockup capture. Homepage is public; copied branding is for the scoped company work.
- [MoltSets](https://moltsets.com/) and [source CSS](https://moltsets.com/moltsets-base.css), observed 2026-09-08: identity, typography, palette, frame styling and sprite timing. This guide does not independently validate homepage marketing claims.
- [Apple font terms](https://developer.apple.com/fonts/), read 2026-09-08: production licensing decision; [Roboto Mono licence](https://github.com/google/fonts/blob/main/ofl/robotomono/OFL.txt) is bundled verbatim.
- `~/personal-brand/brand/BRAND.md`, `tokens.json`, `components.css`, `package.json` and file structure, read 2026-09-08: architectural inspiration only. Tim's colours, fonts, signature, CTA policy and personal claims were not adopted.
