# Animated graphics and GIF delivery

Use a short animation when change, sequence or causality improves understanding. Static headlines, source labels and the essential takeaway should remain readable. A dense poster does not become readable by revealing every tiny label one after another.

## Choreography

Storyboard an opening, action, resolved hold and reset. For a short social explainer, 6–10 seconds with a 2–3 second completed hold is a useful starting point, not a platform requirement. Make one central action legible before extending the sequence.

- Preserve object continuity: a selected field becomes a filter; a record passes a check and becomes a row. Use masks, travel, state changes or path reveals for the actual relationship.
- Give anticipation, movement and rest different timing. The kit's generic 360 ms entrance is a component default, not mandatory choreography.
- Keep the title and useful navigation visible early. Animate the focal operation; avoid several competing loops, restless backgrounds or a compulsory breathing CTA.
- Show missing evidence as missing, rather than animating it into a successful result. Timing is illustrative unless it comes from a measured recording.
- Hold the result long enough to read. Return through a deliberate short reset, or use a bounded replay. Never call a hard cut seamless. Match the endpoint states when claiming a seamless loop.
- The HTML preview should offer play/pause/replay and respect reduced motion with a complete still. GIF players cannot be relied on to respect that preference, so supply a static companion.

Use deterministic time: every visual state must be computed from the supplied timestamp, including counters, sprites, masks, classes and moving objects. Avoid randomness, wall-clock dependencies and unpaused CSS animations. Repeated and backward seeks must produce the same frame.

## Local exporter

This repository has pinned Playwright and FFmpeg in `brand/package.json`. Reuse them:

```sh
npm ci --prefix brand
npm exec --prefix brand -- playwright install chromium
node brand/render-animation.mjs brand/applications/lead-list-recipe/animation.json output/lead-list-recipe
```

`animation.json` supplies the local HTML entry, selector, native width/height, duration in milliseconds, MP4 fps, GIF width/fps, poster time, font families, review timestamps and explicit source files for the editable bundle. Copy the example and adapt its timings and file list to the actual artwork. Entries and dependencies must live inside this repository's `brand/`; the output must be a separate directory outside `brand/`. Working one-offs can use a new application folder without altering shared templates. Declare intentional intermediate masks in `motionClipClasses`; the report retains those observations for visual review, and the completed poster still receives the full clipping check.

The page exposes `window.GraphicMotion = {duration, posterMs, ready, seek, pause, play}`. `seek(ms, {respectReducedMotion:false})` selects an exact export frame. Browser playback respects the media preference; without JavaScript the composition shows its completed static state. This contract is independent of the older `MoltsetsMotion` kit API; use a thin adapter if reusing an existing scene.

The exporter captures a native PNG sequence, creates H.264 MP4 and a palette-optimised looping GIF, and saves a complete PNG, a 360-wide preview, review frames, a contact sheet, an offline review player and an allowlisted editable bundle. It checks fonts, missing assets, text bounds, repeat/backward seek and reduced-motion output. It decodes both encodings to check dimensions, frames and runtime and writes an export report with source/output hashes. It refuses incomplete source bundles and removes only its own temporary frames after success; use `--keep-frames` if useful for editing.

For another environment, implement the same outcome with available tools; do not assume these repo-specific paths exist. Actual illustration generation/editing uses the environment's image-generation tool, while typography and deterministic diagram animation belong in HTML/SVG or a motion renderer.

## Size, encoding and inspection

The example uses 1080 × 1350 MP4 at 30 fps and 720 × 900 GIF at 20 fps. These are production choices. Verify current destination requirements when exact upload compliance matters. Provide MP4 as a companion; do not claim every social destination accepts animated GIFs.

GIF timing uses centiseconds; the exporter accepts 10, 20 or 25 fps to keep exact frame delays. Use a palette generated from the actual sequence. For flat terminal graphics, ordered dithering often keeps grain more stable than diffusion; inspect gradients and small text after encoding. See FFmpeg's official [palettegen](https://ffmpeg.org/ffmpeg-filters.html#palettegen), [paletteuse](https://ffmpeg.org/ffmpeg-filters.html#paletteuse) and [GIF muxer](https://ffmpeg.org/ffmpeg-formats.html#gif-2) documentation, checked 2026-09-08.

If the GIF exceeds the chosen budget, first remove noisy texture and unnecessary changing pixels, then consider runtime, palette size, dimensions or fps. Recheck readability after any reduction. Report actual file size, not an assumed platform limit.

Open the encoded GIF/MP4 and static PNG at intended and phone sizes. Inspect the first frame, central transformation, result hold and reset. A contact sheet supports review of poses and composition; it does not prove smooth playback or pleasant sound. State which checks were actually performed. Deliver the editable bundle as well as the output files, with the concept's factual/illustrative status.
