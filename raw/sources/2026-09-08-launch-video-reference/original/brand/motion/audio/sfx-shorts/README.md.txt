# Shorts SFX kit

ElevenLabs-generated, normalised in-pipeline (whoosh -20, impact -17, riser -19 dBFS).

## The prompt trap

The first kit was **unusable and it looked fine**. Prompts asking for a "deep impact thud"
produced literal sub-bass: 97-99% of the energy below 60Hz, and **0.1% audible on a phone
speaker** — which is where 75% of the viewing happens. They measured as clean audio and
were effectively silent.

Sound models read "deep", "thud", "impact", "boom" as *sub-bass*. For phone-first vertical
video the prompt must ask for the opposite:

> bright · airy · crisp · thin · high frequency · **no bass, no rumble**

That takes the same sounds from 0.1% to 99.8% phone-audible.

**`qa.py` now fails any kit with less than 60% of its energy above 200Hz.** A sound you
cannot hear is not a sound.
