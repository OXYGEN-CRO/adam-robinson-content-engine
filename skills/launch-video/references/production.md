# Production recipe

Read after the concept and requested production scope are clear. This recipe adapts the useful mechanics of the source Remotion workflow; it is not a bundled, installed Remotion project.

## Project layout

```text
output/moltsets-launch/
  SCRIPT.md                 # exact copy, scene action and source mapping
  storyboard.json           # one ordered list of beat IDs and events
  package.json              # pinned production dependencies
  package-lock.json
  public/                   # versioned/pinned assets and genuine captures
  generated/audio/          # project-owned generation outputs only
  audio-manifest.json       # hashes, duration, source and use status
  src/
    Root.tsx
    Video.tsx
    theme.ts                # derived from brand/tokens.json
    script.ts               # data only, no renderer imports
    timings.ts
    SoundDesign.tsx
    scenes/
  out/
  review/
```

Keep paths relative to this actual layout. The original repo was moved and some source scripts still resolve the former `brand/motion` location; do not copy those path assumptions. Do not copy its old scenes as MoltSets product screens.

## Timing contract

Start with an ordered beat list: `id`, `onScreen`, optional `spokenText`, `plannedSeconds`, `sourceIds`, `status`. Give events `beatId` and `offsetFrames`; compute absolute frame values centrally at the composition's FPS.

For a music-and-type film, time the animatic around readable text and the product action, then align transitions to the selected music. For narration, first record or generate the authorized voice, measure the duration of each clip and allow reading holds and pauses explicitly. Do not squeeze a voiceover into outdated estimated windows.

Preserve the source workflow's content-hash cache. Include text/prompt, provider, model, voice, settings, requested duration and processing version in cache keys. Also verify the file hash, not merely file existence. An unchanged hash skips regeneration. Record measured sample duration after trimming, rather than retaining the requested duration as if exact.

The final timeline must reject duplicate IDs, unknown anchors, missing audio, negative offsets that precede the film, overlap that cuts speech, and events extending beyond composition duration. Explicit silence and intentional overlaps are allowed. Planning estimates may render an animatic if clearly marked provisional.

## Visual implementation

Use React/Remotion sequences for editable scenes when appropriate. Load local fonts before the first captured frame. Every frame must derive from the current frame/time; avoid wall-clock animation, randomness without a seed and network-dependent assets.

Reserve row heights before reveals. Hold complete headline states long enough to read. Avoid layout shifts while typing, abrupt scroll discontinuities, and long stretches showing microscopic console text. Crop the actual demo to the relevant prompt/tool result; preserve its meaning and keep edit points honest.

Recompose for each aspect ratio. A landscape terminal capture usually needs a different crop and fewer visible columns in a 4:5 feed version. Start with 30 fps and 1920×1080 / 1080×1350 as creative targets, not claims about platform upload requirements.

## Product proof capture

Record the actual configured client, input, tool invocation, returned data and saved output. Use a small authorized demonstration dataset. Preserve an unedited private review capture alongside the edit. Hide credentials before capture. Mask contact fields that are not intended for public display.

If the recording is condensed or sped up, disclose it visibly and do not attach an unmeasured runtime claim. If actual results include missing data, show it honestly or choose a narrower supported promise. An animation cannot establish success rate, data coverage, speed or price savings.

## Output and inspection

1. Render stills for opening, reveal, demo, result and CTA at the final composition sizes. Inspect full and phone-sized views.
2. Render the full video with audio. Use a widely playable H.264/AAC MP4 and verify the actual media metadata. For SDR, explicitly manage BT.709 and the encoder's colour range; compare decoded frames to the source rather than assuming metadata alone guarantees accuracy. The original implementation encountered washed-out blacks from full-range source media.
3. Watch end to end with sound and muted. Listen for clipped transients, weak phone-speaker cues, masking, hard music joins and abrupt endings. Check captions against spoken words when present.
4. Record review results tied to hashes of the current source and exports. A changed script, asset or timeline invalidates the corresponding review.
5. Return the requested MP4s, poster frame, editable project and concise review notes. Do not upload to an inherited Drive folder or create another repo's content records.
