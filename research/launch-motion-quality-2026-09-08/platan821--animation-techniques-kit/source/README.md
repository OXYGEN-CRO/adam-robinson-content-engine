# animation-techniques-kit

Reusable [Remotion](https://www.remotion.dev/) techniques for building **product / launch videos in code** — no After Effects, no template tool, no agency.

_I built this to make the launch video for my own app — 100% code, no editor. A few people asked how it worked, so I cleaned up and open-sourced the techniques._

**This is a hand-picked, sanitized starter set** — ~33 technique recipes with real Remotion code, plus the method behind them. It's a deliberately *curated* subset (see [Why a "starter"](#why-a-starter)); if it's useful, I'll keep expanding it.

## Demo

The launch video this kit was built to make — 100% code, no editor:

[![Watch the launch video](docs/assets/demo-thumb.jpg)](https://www.getreps.io/watch)

---

## Why this exists

"Use these videos as inspiration" gives you a poor-man's version of what you're copying — the model has no *measured* target, so it invents its own pacing and taste. The fix isn't a better prompt; it's a **method**: tear the references down into a technique library + a measured beat map, then build against that. The full method is in **[METHOD.md](./METHOD.md)** — it's the most useful thing here.

Two things make a code-authored video not look like a template:

1. **A real technique library** — **[docs/techniques/](./docs/techniques/)** has ~33 recipes (the actual Remotion "how", with code), and **[docs/technique-chooser.md](./docs/technique-chooser.md)** lets you pick a move by intent.
2. **Motion synced to the actual beat grid**, not lyric syllables — see **[scripts/beatgrid.cjs](./scripts/beatgrid.cjs)**.

## What's inside

```
docs/
  techniques/            # ~33 recipes: the "how" in Remotion, with code  <- START HERE
  technique-chooser.md   # "I want to do X" -> which technique
src/
  theme.ts               # placeholder brand tokens — swap for yours
  components/text.tsx    # GradientText, KineticHeadline, DrawOnUnderline
scripts/
  beatgrid.cjs           # detect a song's tempo + beat grid, in VIDEO FRAMES
METHOD.md                # how to teach the model taste (the reference-match loop)
```

### The shipped components

- **`GradientText`** — gradient-filled live text (a cheap, high-leverage premium cue).
- **`KineticHeadline`** — word-by-word spring-up + fade, staggered. The calm, legible spine of most value-prop beats.
- **`DrawOnUnderline`** — a hand-drawn underline that draws itself on to emphasize one word.

All motion is driven by `useCurrentFrame()` (never wall-clock, never `Math.random()`), so renders are deterministic and don't flicker across threads. Two rules keep everything render-safe:

- **Never `Math.random()`** → seed a PRNG. (Biggest footgun — multi-thread flicker.)
- **Drive all motion from `useCurrentFrame()`**, including inside a Three.js canvas.

### The beat-grid script

Getting music to *feel* synced is the thing that surprised me most. Timing changes to the sung lyric looks wrong (syllables are unevenly spaced); timing them to the **even beat grid** looks right. `beatgrid.cjs` prints the beat positions as frame numbers you drop straight into your sequence timings:

```bash
node scripts/beatgrid.cjs path/to/music.wav 30
# Estimated tempo: 115.0 BPM
# Beat period: 0.522s = 15.65 video-frames @30fps
# Beat grid (video frames @30fps):
#   33, 48, 64, 80, 95, 111, 127, 142
```

(Requires `ffmpeg` on your PATH.)

## Using the components

```tsx
import {KineticHeadline, GradientText} from './src/components/text';
import {GRADIENTS} from './src/theme';

// inside a <Sequence>:
<KineticHeadline text="Ship it in a weekend." startFrame={0} />
<GradientText gradient={GRADIENTS.accent}>one hero word</GradientText>
```

Drop them into your own Remotion project (`npm i remotion @remotion/google-fonts`), then swap `src/theme.ts` for your brand tokens. The look is yours; the motion is reusable.

## Why a "starter"

Turning internal build notes into something publishable takes real work — I had to strip the **reference-frame images from other people's videos** (not mine to republish), remove my own brand, and neutralize the example code. So this is a deliberately curated batch that covers the techniques behind a full launch video, not a raw dump. **There's a lot more — if people find this useful, I'll expand it. [Open an issue](../../issues) with what you'd want next.**

## Credits

- Built with **[Remotion](https://www.remotion.dev/)** — the "React for videos" library that makes all of this possible. (Remotion has its own license — check it for commercial use.)
- The techniques here were learned by studying great motion-graphics and product-launch videos frame by frame, then rebuilding the *mechanics* from scratch in my own code. Standing on a lot of shoulders.
- The **3D iPhone** in the demo is an iPhone 17 Pro model I **purchased on [CGTrader](https://www.cgtrader.com/items/6420976)**. It's a paid, non-redistributable asset, so it is **not** included in this repo — buy your own from that link.

## License

MIT — see [LICENSE](./LICENSE). It's a sharing project: use it, remix it, ship your own videos with it. No attribution required (but always welcome).
