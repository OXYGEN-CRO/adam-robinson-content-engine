# Sound design

## Reuse the library

Open `brand/kit/audio.html` to audition the imported cues. File roles and prompts are in `brand/motion/audio/library/manifest.json`. These are source-repo assets, not a newly approved MoltSets sonic identity. Generation provenance is not proof of an account's commercial-use entitlement; retain the manifest's status when assembling a public master.

The electronic underscore is approximately 40 seconds. The ambient alternative is shorter. Do not silently stretch either across a longer film: start music after the cold open, edit a musical loop, or obtain a suitable longer version when production scope permits. Audition any join in the full mix.

Useful functions:

- Typing: connect the viewer to a visible input; stop when typing stops.
- Selection tick: mark a discrete choice or the credit-counting motif.
- Send click: synchronize exactly with the actual submission frame.
- Confirmation: reward a real returned result or saved output.
- Short whoosh/riser/impact: support a structural transition sparingly.
- Music: carry momentum through the film without fighting readable text or speech.

Do not put a sound on every moving object. A short intentional pause before the reveal can create more contrast than another impact. Keep logo comparisons tonally factual, without fake error alarms or implied product failures.

## New generation, when requested

ElevenLabs was used in the reference project. Verify the current official API, account permissions and output formats before implementing generation. Use environment-based credentials and project-owned output paths. Never copy `.env` or call a paid API merely to finish a planning request.

For narration, use a user-supplied recording or an authorized selected voice. Do not reuse the reference project's voice as Adam, clone his voice without explicit permission, or present generated narration as a recording of him.

Prompts should describe musical function, energy, instrumentation and duration. For short UI cues, specify a crisp audible midrange transient, restrained low end, and no speech. The source shorts kit documented a failure where sub-bass effects barely survived phone speakers; check the actual mix on the target playback device rather than importing its percentage claims as universal rules.

Hash inputs and measure outputs as described in `production.md`. Trim unwanted leading silence with care: a musical pickup may be intentional. Preserve the original asset and record any processing in a derived manifest.

## Mixing targets for the first cut

These are proposed mix targets, not platform specifications:

- Start around -16 to -14 LUFS integrated for the complete mix, then adjust by listening; cap true peak at -1 dBTP.
- If narration is present, lower music enough to keep every word intelligible and use smooth gain changes. Do not copy a fixed `volume: 0.12` from the reference as if it normalizes every track.
- Keep typing and repeated ticks quieter than the reveal and output confirmation. Avoid harsh bursts at frame zero.
- Verify stereo and mono playback, a phone-speaker pass and the final music tail. Silence detection and loudness measurements supplement listening; they do not replace it.
- Record measured loudness, peak, duration and any incomplete listening checks in the review report.
