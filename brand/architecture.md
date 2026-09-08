---
type: reference
status: active
owner: adam
created: 2026-09-08
updated: 2026-09-08
sources:
  - brand/BRAND.md
  - brand/package.json
tags: [brand, implementation, graphics, motion]
---

# Use and extend the graphics kit

Open [kit/index.html](kit/index.html) directly in a browser. Fonts, logos, CSS and scripts are local; no renderer, account or network is required to browse it. The source is independent of `~/personal-brand`.

## File ownership

| Layer | Authoritative files | Consumers |
| --- | --- | --- |
| Identity and judgement | `BRAND.md`, `patterns.md` | Graphic briefs and review |
| Values | `tokens.json` | Generated `tokens.css`, `tokens.js` |
| Structure and components | `base.css`, `components.css`, `components.mjs` | Templates, catalogue, motion |
| Compositions | `templates/scenes.mjs`, `templates/compositions.css` | Generated template HTML and manifest |
| Catalogue | `build.mjs`, `kit/kit.css`, `kit/kit.js`, `kit/preview.js` | Generated catalogue, sample pages and manifest |
| Motion | `motion/runtime.js`, `motion/motion.css`, central motion tokens | All scene HTML, seek renderer, preview |
| Source evidence | `../raw/sources/2026-09-08-moltsets-brand/` | Provenance only; source fonts are excluded from production |
| Exports | `../output/moltsets-brand/` | PNGs, phone previews, video, reports and archive; ignored by Git |

Do not edit generated files to make a durable change. For a one-off graphic, copy a template into `output/<job>/`, adjust its relative dependencies to `brand/`, and edit freely. Before a final handoff, copy or package its dependency set to freeze the appearance. Shared kit updates should not silently rerender historical deliveries.

## Setup and commands

Run from the repository root with Node 22 or newer and npm available:

```sh
npm ci --prefix brand
npm exec --prefix brand -- playwright install chromium
node brand/build.mjs
node brand/render.mjs
node brand/render.mjs motion
node brand/check.mjs
python3 scripts/package_moltsets_brand.py
bash scripts/wiki-lint.sh
```

`npm --prefix brand run release` runs build, static render, motion render and checks. Packaging is separate. The package lock pins the renderer and FFmpeg. No globally installed browser skill or personal-brand runtime is required. The renderer serves `brand/` temporarily on a loopback-only ephemeral port and closes it when finished.

Static rendering exports seven native PNGs, seven 360 px previews, all 18 component PNGs and kit screenshots. The lower-third PNG preserves alpha. The motion command exports a 4-second 1920 × 1080 H.264 MP4 at 30 fps, plus 120 deterministic PNG frames. The MP4 is opaque; composite the transparent lower-third PNG over footage, or render its HTML frame sequence with `omitBackground:true` when authoring a future animated overlay. Do not mistake the MP4 for an alpha video format.

## Reuse a component

Copy the markup from the catalogue's “Reusable markup” panels. Load `base.css` then `components.css`; `base.css` imports generated tokens and the local font. Resolve all relative asset paths from the new HTML location. For scripted generation, import an HTML factory:

```js
import {terminal, step} from './brand/components.mjs';
const html = terminal('sequence', step('01', 'A real step', 'Its explanation'));
```

Content arguments are escaped. The `terminal` factory intentionally accepts trusted assembled HTML as its second argument. Do not pass untrusted source HTML to that slot. Classes use the `ms-` prefix; no Tailwind dependency is required. `--component-size` adjusts body-sized components without changing the full graphic type scale.

To add a scene, register its ID, title, width, height, classes and markup in `templates/scenes.mjs`, then build. The renderer and checker consume the generated manifest, so new scenes participate automatically. Keep proposed copy and placeholders visibly distinct from evidence.

## Motion contract

Load `tokens.js` then `motion/runtime.js` after the artwork. Put `data-enter="520"` on a layer to begin a reveal at 520 ms. Add `data-draw="860"` to an SVG path for a stroke reveal. `data-mascot` and `data-thinking` enable source sprite sequences. Keep each independently animated wrapper separate; nested reveals multiply opacity, so make sure an outer frame finishes before the inner content starts.

```js
await document.fonts.ready;
await MoltsetsMotion.ready;
MoltsetsMotion.pause();
MoltsetsMotion.seek(1400); // milliseconds; no accumulated playback state
```

`seek` clamps to the scene duration. Backward and repeated seeks reproduce the same frame. `play` runs once; `pause` stops it. Reduced-motion preferences resolve to the final frame. Export tools can explicitly request a timeline frame with `seek(ms, {respectReducedMotion:false})`; the interactive preview respects the preference. `tokens.js` is a plain browser global for offline use; other animation frameworks can import `tokens.json` and reproduce the same values.

## Custom GIF and MP4 explainers

The [animation renderer](render-animation.mjs) handles a locally authored `GraphicMotion` scene independently of the seven generated kit templates:

```sh
node brand/render-animation.mjs brand/applications/lead-list-recipe/animation.json output/lead-list-recipe
```

Read [[brand/implementation-graphics]] for the concept and editable source. The configuration declares native dimensions, GIF dimensions/fps, poster time, review times, expected fonts and the explicit dependency allowlist. Scene HTML and dependencies live inside `brand/`; exports go to a separate directory outside it. The exporter reproduces the poster from a frozen bundle, checks deterministic and backward seeks, checks reduced motion, captures a PNG sequence, encodes GIF/MP4, decodes both to verify dimensions and duration, and writes an offline review page and report. Intermediate masks may declare `motionClipClasses`; their intentional clipping is recorded for visual review, while the complete poster receives the full bounds check. Captures are removed only after success; `--keep-frames` retains them.

The example's eight-second duration, 30 fps native MP4 and 20 fps GIF are deliberate asset choices, not changes to central motion tokens. GIF endpoint equality is checked when `seamless` is declared; inspect the actual reset for pacing as well. GIF playback does not reliably inherit reduced-motion preferences; include the static PNG. There are no new dependencies or runtime links to `~/personal-brand`.

## Kit checks and limits

The checker verifies source colour fidelity, generated-token drift, bundled assets and licence, native dimensions, original logo alpha, template content bounds and safe margins, actual rendered glyph fonts, missing requests, colour contrast for designated reading pairs, deterministic seek, reduced motion, preview controls, local-file operation and responsive catalogue width. It validates the delivered video by decoding it with FFmpeg and matching frame metadata.

Inspect the images as well. Programmatic bounds cannot establish visual taste or factual truth. Check sources and [[identity/proof|Proof]] before filling evidence slots. Read [[brand/patterns|Patterns]] when adapting a dense diagram to a smaller destination.

## Source Notes

- Architecture inspired by the separation of guide, central values, CSS, templates, assets and exports in `~/personal-brand/brand`, inspected 2026-09-08.
- This implementation, factory API and renderer were created for the user-provided MoltSets brief. See [[brand/BRAND|Brand]] for extraction evidence, adoption status and font substitution.
