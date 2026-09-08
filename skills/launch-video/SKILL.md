---
name: launch-video
description: Plan or produce a product launch video with a sourced storyboard, the repo's visual identity, a real product demonstration, beat-synchronized music and sound effects, and editable local deliverables. Use for launch films, product announcement videos, or refinements to their script, motion and sound.
---

# Launch video

This is the MoltSets adaptation of the launch-video workflow in the owner's `oxygen-knowledge` repository. It supports planning and production as separate scopes. A request to plan is complete with a reviewable plan; it does not require rendering, paid audio generation, uploading or publishing.

## Context and scope

1. Read `index.md`, `AGENTS.md`, `brand/BRAND.md` and the current brief. Retrieve relevant identity, audience, strategy and voice pages. Check `identity/proof.md` before using metrics.
2. Determine the requested stage: concept, script, storyboard, animatic, production or revision. Carry that stage to completion. Infer reversible creative choices; ask only about missing information that materially changes the promise, demonstration or destination.
3. Read the full source behind product claims. Verify current pricing, availability, integration capabilities and competitor comparisons from first-party sources. Record date and URL. Separate source facts, user launch instructions and proposed copy. Do not promote historical beta pricing to a current offer.
4. For a MoltSets credit-pricing story, distinguish core-data plan access, usage limits, mobile-phone tokens and the separate Claude subscription/API bill. Resolve contradictory billing documentation before using absolute claims such as “no credits,” “unlimited” or “one price for everything.”

## Build the story

Define one audience, one frustration, one product promise, one demonstrable result and one CTA. Explain the creative reasoning rather than treating a reference film's style as evidence of performance.

Read `references/art-direction.md` before storyboarding or revising a rejected film. Establish the visual idea and study actual references before choosing transitions or writing scene code.

Choose a structure that fits the runtime. A short film can show one request becoming one useful result, followed by the brand. Do not force recognition, tension, reveal, workflow, offer and CTA into separate slides. Reveal the product early enough to leave time for proof. Competitor logos establish recognition; they do not establish feature parity, inferior quality or customer savings.

For planning, deliver:

- Positioning, audience and desired viewer action.
- A timed storyboard with beat IDs, exact draft on-screen copy, visual action, audio cue and evidence status.
- The hero demo input, prompt, actual tool action and output to capture.
- Visual and sound direction, selected existing assets and any missing assets.
- A claim ledger, unresolved launch details and the next production steps.

Use `references/production.md` when implementing the timeline and `references/audio.md` when selecting or mixing audio. The current campaign plan is `strategy/moltsets-launch-video.md`; it is a discussion draft, not an evergreen offer.

## Apply the local brand

- Read `brand/tokens.json`; derive scene tokens from it rather than copying a second palette.
- Use the production font recorded there. The archived SF Mono files are reference-only; the current licensed production font is Roboto Mono.
- Use the actual MoltSets mark, lockup, mascot and thinking frames in `brand/assets/`. The existing lockup SVG contains a raster image; do not describe it as outlined vector artwork or enlarge it beyond useful resolution.
- Use dark terminal surfaces, coral emphasis and mint for successful results. Typography, spacing and purposeful motion should do most of the work. Brand documentation governs exact values.
- Treat kit easing, entrance distance and sprite timing as component-preview defaults. Choreograph film timing for the action: preparation, acceleration, contact, settling and a readable hold. Repeating the same entrance across scenes does not establish a film's motion language. The kit's four-second preview is not a prescribed launch-film length.
- Genuine product capture stays accurate. An illustrated or reconstructed interface must be identified as such during review. Use real product footage for claims about actual operation.

## Assets and implementation

Existing audio lives in `brand/motion/audio/library/`; consult its manifest and `brand/audio.md`. An audition page is at `brand/kit/audio.html`. Third-party reference logos and provenance live in `brand/motion/logos/third-party/`.

For production, use a project directory such as `output/moltsets-launch/` with editable scene source, a pinned dependency lockfile, `public/` assets and separate generated caches. Remotion is the reference implementation approach; the existing deterministic browser renderer is also available for simpler compositions. Check current official documentation when adopting or updating APIs.

Keep beats, measured audio durations, visual events and SFX in one coordinated timeline. Anchor events to a beat ID plus an offset. Missing beat IDs and missing duration data must fail production validation rather than silently placing events at zero or the end.

Reuse authorized local assets before generating replacements. Never import another project's credentials, voice identity, brand scenes or upload destination. Do not delete shared audio folders to reset a project. Paid generation and external distribution follow the actual user-authorized scope.

## Review and delivery

For a new direction or a quality rescue, build the hardest 2–3 seconds first. Compare the rendered motion with the selected reference mechanism at normal speed and frame by frame. Revise the prototype until it communicates the intended action and preserves the brand; then extend the timeline. This is an internal production checkpoint, not a request for new user permission.

Keep craft review separate from technical validation. A valid MP4, aligned type and unclipped layout cannot establish compelling motion. Review the visual idea, continuity between shots, changing pace, restraint, product credibility and the relationship between action and sound. Do not describe a film as premium, polished or Apple-level merely because it passed automated checks.

Inspect the entire exported video with audio and mute it for a second pass. Inspect key frames at full size and phone size. Verify copy, authentic tool output, font loading, contrast, timing, cropping, end-card hold and sound audibility. The product promise must survive muted playback. Use `brand-review` for a full visual review when appropriate.

Verify duration, dimensions, frame rate, codecs, audio peaks and colour range. Compare representative decoded video frames with source renders. Run `scripts/wiki-lint.sh` after filing context and the project's relevant render checks. Never report listening or playback checks that were not performed.

Deliver editable source and requested renders to the user's destination, with a brief account of what was checked and what remains provisional. Local delivery satisfies a local draft request. Publication, scheduling, outreach, external uploads and unrelated content-system updates are separate actions.

## Provenance

Adapted on 2026-09-08 from `oxygen-knowledge/gtm-production/.claude/skills/launch-video/SKILL.md` and its implementation at `gtm-production/content/motion/launch-video/`. Exact selected reference files and hashes are retained in `raw/sources/2026-09-08-launch-video-reference/`. OXYGEN's branding, fixed voice, shared-cache deletion and mandatory Drive/content-post workflow were not carried into this skill.

Art-direction revision on 2026-09-08 follows the user's rejection of v02 and research recorded in `inspiration/launch-motion-quality.md`. External skills were examined as references, not installed or adopted wholesale. Pinned source snapshots and licences are in `raw/sources/2026-09-08-motion-quality/`.
