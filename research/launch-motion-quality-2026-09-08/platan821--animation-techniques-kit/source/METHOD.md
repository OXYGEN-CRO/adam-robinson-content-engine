# How to teach the model taste (the reference-match loop)

The single biggest lesson from building this: **"use these videos as inspiration" produces a poor-man's version of them.** Not because the model is bad — because there's no *measured target* and no scored loop. Nothing pins the reference's pacing down as a number the output must hit, so the model invents its own, and "invented pacing" is exactly what makes AI-made video feel cheap.

The fix is a loop with three moves. It's the same shape whether you're matching a screenshot or a video.

## Move 1 — Tear the references down into a *contract*, not prose

Pick 3–6 videos whose motion you actually admire (product launch films, motion-graphics ads, even a couple of good After Effects tutorials for specific techniques). Then decompose them two ways:

**Hard facts (measured, with ffmpeg):**
- shot count + per-shot duration distribution + **cut cadence** (cuts/sec) + how regular that rhythm is
- per-frame **motion magnitude** (is a shot static, a slow push, or a whip?)
- **cross-beat repetition** — how similar the motion bursts are to each other (the anti-repetition signal)
- resolution / fps / aspect / sharpness (production gloss)
- on-screen-text beats + their timing
- dead-air %, loudness arc, where the music hits

**Soft facts (intent), each chained to a hard fact:**
- the **beat map** (hook → … → CTA, with timecodes)
- the **energy curve** (rate each beat 1–5)
- the recurring **motion grammar** (the transition/motion vocabulary it reuses)
- the ONE hero move
- the **cross-beat arc** — how it builds, and how it avoids repeating itself

The key discipline: tie every soft read to the number that produces it. Not "the hook feels punchy" but "the hook lands *because* the first cut hits at 0.6s on the downbeat."

Across several references you get a **house style**: a contract of target *ranges* ("shots 0.6–1.4s, ~0.9 cuts/s synced to music hits, a text beat every ~1.2s, energy ramps to a CTA peak"). Split it into:

- **transferable structure** — pacing, cut cadence, motion grammar, text-beat rhythm, energy arc. Replicate this.
- **non-transferable skin** — their exact 3D look, their brand, their palette. Never clone this.

## Move 2 — Replicate the skeleton first, then re-skin

Build a proxy that hits the reference's **beat map and pacing** — shot durations, cut cadence, motion grammar, text-beat timing, energy arc — with *your* content and brand, **before** any creative divergence. This is the forcing function: with a beat map to hit, the model can't drift into its own invented pacing. Every deliberate deviation from the contract gets logged as a decision, not left as drift.

**Keep the mechanism, swap the palette.** A technique is colorless. If a reference recolors a hero word with a sweeping gradient, you keep the *sweep* and use *your* colors. Borrowed technique ≠ borrowed look.

## Move 3 — Score the output *against the reference*, in a loop

Don't judge the output against an abstract "is this good." Judge it against the reference's measured numbers:

- does the cut's cadence / shot-durations / motion match the reference's ranges?
- is the cross-beat variety as high as the reference's (or did you reuse one move 8 times)?
- played side by side, which feels cheaper, and at what second?

Then **loop** until the gap closes — not "one pass, ship."

## The technique library falls out of this

Do Move 1 across enough references and you accumulate a **library of named techniques** — "sequential word stagger," "match-cut," "draw-on underline," "count-up ticker" — each with the reference frames that taught it and a note on when to use it. That library is what you hand the model at build time so it composes from a real vocabulary instead of defaulting. A slice of mine is in [docs/technique-chooser.md](./docs/technique-chooser.md).

## Two determinism rules that make any of this render-safe

- **Never `Math.random()`** → seed a PRNG and drive it as a pure function of the frame.
- **Drive ALL motion from the frame** (`useCurrentFrame()`), never wall-clock. Re-render = byte-identical.
