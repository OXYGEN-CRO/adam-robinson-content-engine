---
type: context
status: draft
owner: adam
created: 2026-09-08
updated: 2026-09-08
sources:
  - raw/sources/2026-09-08-motion-quality/manifest.md
  - https://buck.co/work/notion-ai
  - https://buck.co/work/apple-power-to-the-pro
  - https://github.com/Vincentwei1021/video-shotcraft
  - https://github.com/AbubakrChan/product-launch-motion
tags: [moltsets, launch-video, motion, research]
---

# MoltSets — motion direction after v02

## Decision

The user rejected the 20-second v02 on quality grounds and asked for substantially better craft, even at a shorter runtime. The next direction is a proposed **9-second film built around one continuous product action**. v02 is an archive of a rejected direction, not the foundation to polish scene by scene.

“Apple-level” is a desired standard of craft, not a quality verified by installing a skill. Research found useful tools and methods, but no evidence that a skill reliably produces that standard on demand.

## Why the previous cut failed

The draft used four separate compositions, repeated fades and vertical entrances, a generic reconstructed interface and a static mascot. Each scene restarted the viewer's attention. The product operation appeared late, and much of the runtime explained accessibility in words. There was no memorable action connecting the opening to the brand.

The technical checks were real, but they tested export integrity and layout. Treating those results as evidence of strong motion design was the wrong judgement. Adding more transitions to that structure would preserve its main weakness.

## Keep the rough character

MoltSets' hard pixels, terminal typography, restrained texture and coral/mint palette are useful distinctive material. My interpretation is that this roughness should be intentional and consistent: crisp geometry, purposeful character poses and exact timing. It should not mean arbitrary alignment, decorative clutter or unfinished movement.

[BUCK's Notion AI work](https://buck.co/work/notion-ai) is a relevant craft reference. The team retained Roman Muradov's drawing language, developed character performances with cel animation, and carried that feel into an interactive system. It is a character-animation case study, not an Apple launch-film template.

[BUCK's Apple “Power to the Pro”](https://buck.co/work/apple-power-to-the-pro) describes an idea developing through different visual treatments. It supports studying a coherent visual concept across varied materials. The full Apple film was not played in this research pass; its project text and a studio image were inspected. [BUCK's Comfy work](https://www.buck.co/work/comfy-brand-refresh) offers another useful principle: build motion from a product's existing shapes and relationships. These references inform technique; they do not establish MoltSets' approved identity.

## Skills and methods worth using

| Resource | What is useful | Judgement for MoltSets |
| --- | --- | --- |
| [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) · [preview gallery](https://vincentwei1021.github.io/video-shotcraft/) | A substantial shot library with actual previews and matching Remotion implementations. | Strongest practical library found. Select individual mechanisms; its paper/amber template is not our art direction. |
| [product-launch-motion](https://github.com/AbubakrChan/product-launch-motion) | Explicit creative direction, camera/motion guidance and a distinction between technical checks and design critique. | Strongest workflow reference for rescuing this draft. Its example film is not available for reuse. |
| [animation-techniques-kit](https://github.com/platan821/animation-techniques-kit) | Break down a real reference, prototype its central motion, compare, then extend. | Adopt this working method. Its basic headline component alone would not improve our film. |
| [Official Remotion skills](https://github.com/remotion-dev/skills) | Current implementation guidance for Remotion projects. | Useful engineering support if we use Remotion; it does not provide art direction. |
| [Every's product-launch-video](https://github.com/EveryInc/product-launch-video) | Brief/storyboard/render/review structure and product accuracy. | Helpful scaffold, but insufficient evidence of a higher visual standard by itself. |
| [Memex's product-launch-video-skill](https://github.com/memex-lab/product-launch-video-skill) | Some useful transition and continuity concepts. | Do not adopt its mandatory glow, ambient movement and effect-count rules; they conflict with this brand and confuse motion quantity with craft. |

Two Shotcraft mechanisms were examined in more detail: `terminal-typewriter` turns a completed input into a directional transition; `input-morph-assemble` carries a UI object into a brand reveal. I read their recipe cards and exact TSX implementations and inspected sampled frame sequences. The transferable idea is continuity. The fixtures, glow, rounded forms and exact numerical timing are not proposed MoltSets styling.

## Proposed nine-second film

Working concept: **a simple request becomes a useful lead list**. The ordinary language carries the accessibility message. The mark becomes part of the action rather than an overlay.

| Time | Visible action | Sound intention |
| --- | --- | --- |
| 0.0–2.3s | Tight composition on a readable prompt: “Find SaaS founders in Austin.” Clearly identify Claude Code with MoltSets. Begin with enough text already present to avoid spending the opening on slow typing. A coral cursor finishes the request. | A few dry key sounds, then a deliberate Enter. |
| 2.3–5.7s | Follow that same baseline into a focused lead-list result. One real result is legible; additional rows establish a useful list. One controlled scale change creates the reveal, followed by a stable reading beat. No unrelated panels or invented result counts. | A short accelerating sequence of restrained ticks resolves when the list settles. |
| 5.7–9.0s | The cursor becomes the coral underline in the original MoltSets mark. The mark and wordmark settle together. Working copy: “Unlimited leads. Just ask Claude.” Hold the completed composition. | A brief gap before a compact closing tone; a clean tail. |

This is proposed copy and choreography, not an approved offer or a finished animation. The user's “unlimited” direction retains the already-recorded core-data/plan-limit scope. The timing is an editorial target, not a promise about query speed. The result segment requires an authentic capture before it can serve as product proof. “Clockhole” remains interpreted as Claude Code from the preceding context.

Three approaches were considered: a continuous cursor-to-result graphic, a tightly edited live product demonstration, and a character-led pixel performance. The first best combines the user's message, existing assets and a short duration. A live capture supplies evidence within it. A mascot-led scene risks consuming the runtime without explaining lead sourcing and needs more performance work than the existing reveal frames provide.

## Production changes

1. Prototype the input-to-result transition at final quality for 2–3 seconds. Use the actual pixel geometry and font. Compare object paths, timing and readability with the selected reference mechanism.
2. Resolve that movement before extending to the opening and ending. Compose the film as a continuous action, with a clear change from anticipation to movement to rest.
3. Integrate a genuine product result and preserve a private unedited capture. A conceptual motion test may use explicitly identified placeholders, but they cannot become proof in the final film.
4. Design the audio as one short phrase. Audition the existing library and use a suitable musical fragment only if its ending works. The previous underscore is not automatically inherited.
5. Review motion at normal speed and frame by frame, then review the entire cut muted and with sound. Technical export checks follow the craft review. Recompose other aspect ratios after the main cut works.

The local launch-video skill now includes these checkpoints and no longer treats the kit's 360 ms entrance as a rule for film choreography. External skills have been researched and selectively used as methodological references; none has been globally installed, and no remote scripts were executed.

## Inspection record

Three complete example MP4 files were decoded and sampled into 16-frame contact sheets: Shotcraft's 38.06-second gallery introduction, its 36.18-second Ink Press template, and product-launch-motion's 44.30-second example. Two individual Shotcraft shots were also decoded and inspected as sampled sequences. This establishes visibility into layout and sequence, not a complete normal-speed motion or subjective sound review. No subjective listening claim is made. Apple/Notion studio imagery and source text were inspected; the full studio films were not played.

Research downloads remain in `research/launch-motion-quality-2026-09-08/`. Exact selected source documents, repository revisions and hashes are archived separately. Third-party films and imagery are references only, not assets for the MoltSets film or the Desktop delivery.

## Related Pages

- [[strategy/moltsets-launch-video]]
- [[brand/BRAND]]
- [[brand/audio]]
- [[index]]

## Source Notes

- User's latest critique, 2026-09-08: exact text retained in [[raw/sources/2026-09-08-motion-quality/manifest]]. The user prioritized shorter duration, senior motion-design quality and research into online skills.
- First-party GitHub source files and licences were downloaded and read to assess the six resources above. Repository revisions and file hashes are in the same archive. Marketing claims such as “cinematic” are not treated as verified quality.
- Studio project pages linked above were retrieved on 2026-09-08. Interpretations for MoltSets are proposed creative judgements, not claims made by those studios.
- v02 source and exported frames were the basis of the local critique. The original files are preserved under `output/moltsets-launch/v02/` and the existing Desktop delivery.
