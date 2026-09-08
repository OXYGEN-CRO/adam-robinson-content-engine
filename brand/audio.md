---
type: context
status: draft
owner: adam
created: 2026-09-08
updated: 2026-09-08
sources: [raw/sources/2026-09-08-launch-video-reference/manifest.md, brand/motion/audio/library/manifest.json]
tags: [brand, audio, launch-video, reference]
---

# Audio for the MoltSets launch

## Summary

Two music tracks and eight effects were copied from the owner's Oxygen knowledge repository for launch-video planning. These are reusable candidates, not a newly established MoltSets sonic identity. No OXYGEN narration was imported.

Open the [local audition page](kit/audio.html). The [audio manifest](motion/audio/library/manifest.json) records original paths, byte hashes, measured durations, source generation metadata and the current audition/use status. Files were successfully decoded; subjective listening remains a production step.

## Library

| File | Duration | Proposed function |
| --- | --- | --- |
| electronic-underscore.mp3 | 39.78s | Main reveal-to-CTA music candidate |
| ambient-underscore.mp3 | 28.06s | Calmer alternate direction |
| typing.mp3 | 1.52s | Visible typing |
| send-click.mp3 | 0.52s | Submit prompt |
| success-chime.mp3 | 1.23s | Actual returned output |
| selection-tick.mp3 | 0.52s | Discrete selection / opening motif |
| landing-tone.mp3 | 1.65s | Optional end-card resolution |
| short-whoosh.mp3 | 0.63s | Scene transition |
| short-riser.mp3 | 1.65s | Pre-reveal anticipation |
| short-impact.mp3 | 0.52s | Reveal accent |

Durations are the imported MP3 container durations reported by the local FFmpeg decode pass, rounded to hundredths. They differ slightly from the source generator's measurements, which are preserved separately. Final timeline construction should measure decoded audio and planned trims.

## Use and provenance

The source workflow and shorts-kit notes identify ElevenLabs generation. They do not record the generating account or its commercial-use entitlement. The user authorized importing assets from their repo; the local copy does not independently establish that missing entitlement. Preserve this status when selecting the public master rather than claiming a verified licence.

The launch skill's `references/audio.md` documents timing, generation, mixing and review. Keep any derived edits in the production project's own folder and preserve these source copies. Never clear this shared library to reset a new film.

## Related Pages

- [[brand/BRAND]]
- [[strategy/moltsets-launch-video]]
- [[brand/architecture]]

## Source Notes

Imported on 2026-09-08 from `oxygen-knowledge/gtm-production/brand/motion/audio/`. Exact reference scripts and timing manifests are archived under [[raw/sources/2026-09-08-launch-video-reference/manifest]]. Music descriptions are based on the original generation prompts, not a claim that this planning pass listened to the tracks.
