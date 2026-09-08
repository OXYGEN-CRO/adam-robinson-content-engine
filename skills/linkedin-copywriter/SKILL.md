---
name: linkedin-copywriter
description: Draft or edit one LinkedIn post using the author's context, writing samples, factual sources and intended funnel job, with a scored hook shortlist and an anti-slop pass.
---

# Write a LinkedIn post

Read `AGENTS.md`, `index.md`, the relevant identity and audience pages, `identity/proof.md`, `voice/linkedin-voice.md`, `voice/hooks.md`, `voice/formats.md` and the selected pillar and funnel context. Read `hook-framework.md` and `anti-slop.md` in this folder. Read the full source behind the central claim. Search the raw post archive for one or two source posts in the archetype you intend to use; do not load the whole archive.

## Find the post

Identify one useful point, its source, the intended reader and the post's job. Work from the supplied brief and existing context; ask for missing information only when it would change the substance. Do not invent a milestone, anecdote, customer quote or feeling to make an idea interesting. A stub voice page does not block useful editing of a supplied draft; preserve the user's wording and say that the voice is uncalibrated.

Find the tension in the material before choosing a structure: the number that does not match the feeling, the result that should have been impossible, the expert who contradicts the crowd, the past self who was wrong. If there is no tension, say so and propose a different angle rather than manufacturing one.

Choose a structure the material supports: a sequence for a process, a story for a real change, evidence for a claim, dialogue for a real exchange, a comparison for a decision. Do not force every post into one house format.

## Write the hook

Follow the procedure in `hook-framework.md`: write ten hooks across at least four archetypes, score each on Stake, Specific, Tension and Stance, apply the kill rules, check the order of moves, run the stranger test, and pick the one the body can best substantiate. The first sentence must finish inside 140 characters with the stake and the contradiction already in it; run `python3 scripts/hook_check.py` on the final draft and put the mobile and desktop slices in the delivery note. Check every figure in the hook against `identity/proof.md`. Keep the two runners-up for the delivery note.

Prefer a specific observation over manufactured suspense. A number is a specific, not a hook by itself. Do not open on a summary of the story, an event promotion, a third party's result without the author's stake, or a question the reader can answer with no.

## Write the body and close

Use the author's actual rhythm and vocabulary from `voice/linkedin-voice.md`. Match paragraph length to the job: long and run-on when arguing, one-line beats when landing a story, one to three sentences per list item. Preserve the caveat beside the claim. Do not add slang, self-deprecation, profanity, ALL CAPS, deliberate mistakes or dramatic reversals to sound human; use them only where the material carries that emotion and the author's own posts show the habit.

The body sequence that the author describes and practices is: agitate a specific pain, offer a solution or reframe, land one takeaway. Say the lesson once. Close with something that makes the reader feel the argument: a verdict line, an earned signature phrase, a deflating joke, or a question only after a list the reader can genuinely add to. Use a CTA only when it fits the chosen funnel job and a real available offer. Do not gate a resource behind a comment unless the job is a resource offer.

## Edit for substance

Run every test in `anti-slop.md`: delete, swap, source, stranger, dinner, read-aloud, truncation and phrase scan. Cut generic praise, unsupported superlatives, repeated morals, empty transitions and slogan conclusions. Keep necessary explanations and qualifications. Read the hook, paragraph starts and close together; the argument should survive that reading alone.

Check every factual claim, quote, date and number against its source and public-use status. Keep reported results, targets and illustrative examples distinct. For repurposing, select one argument from the source rather than compressing the whole source. For revisions, address the requested changes first and preserve the user's facts and meaningful phrasing.

## Deliver or save

Return one paste-ready draft, then a short note with: the two runner-up hooks and their scores, the source behind each claim, any figure that needed a proof check, and any material uncertainty. Do not put process commentary, scores or source paths inside the copy. Offer the full hook list only when requested.

Always save the final draft into Oxygen Publishing as an unapproved draft, so the user can review it there. Read the `oxygen` block in `workspace.local.json` (see `workspace.example.json`) for the CLI binary and organization id; never infer an organization from the CLI's current selection. Write the copy to `output/<post-slug>/post.txt`, then run `<cli> publishing posts create --org <id> --draft --status draft --provider linkedin --publish-at <placeholder ISO date> --title "<author>: <topic>" --text-file <path> --json`. If a graphic was produced, upload it first with `publishing media upload-url`, PUT the file to the returned URL with the returned headers, confirm with `publishing media uploaded <media_id> --sha256 <hex>`, and pass `--content-json '{"media_asset_ids":["<media_id>"]}'`. Never pass `--approved`, never attach a sender the user did not name, and treat the publish-at value as a required queue field, not a schedule. Save the JSON response beside the text and return the `web_url` in the delivery note. If the Oxygen block is missing or the CLI fails, deliver in chat and say the draft was not saved.

When saving to Notion is also requested, follow `strategy/notion-schema.md`, fetch the configured destination and use `templates/notion-content.md`. Set Status to Creating, one Pillar and the selected Platform. Add a Publish date only if a date is agreed. Check for the existing card before creating another. If a reusable hook pattern emerged, offer to file it in the configured Hooks database; do not file it unasked.

If Notion is unconfigured, deliver in chat and state it was not saved. Never silently use another board. Saving a draft does not schedule or publish it.
