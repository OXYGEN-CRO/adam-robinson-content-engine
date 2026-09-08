# Hook framework

The hook is everything the reader sees before "…more". Its only job is to make a stranger click. It does not summarize the post, announce a list or introduce the author. Write it last or rewrite it last; the best post idea is wasted without one.

## Length, defined

LinkedIn does not publish the cut. Third-party measurements agree on about **140 characters on the mobile app** and about **210 on desktop**, counted with spaces and line breaks, and both clients also cap visible lines (about two on mobile, three on desktop), so a hard return spends the rest of that line. Treat these as working budgets and check a real feed when it matters.

The author's own practice in the 200-post corpus: median first sentence 62 characters; 184 of 200 first sentences finish inside 140; median first paragraph 154 characters, so he often runs a second or third sentence past the mobile cut and lets desktop see it.

Rules that follow:

- **The first sentence finishes inside 140 characters** and already contains the stake and the contradiction. Whatever is cut after it is bonus, never the payoff.
- **Nothing essential sits between 140 and 210.** Desktop readers get a second beat; mobile readers must not need it.
- **A hard return before 140 is a choice, not an accident.** One short line then a return gives mobile one more line; two returns show almost nothing. The author's one-line hooks ("I quit drinking alcohol six years ago.") work because the line is the whole thought.
- **One sentence per line in the hook, blank line between.** The author's strongest openings are laid out that way ("I quit drinking alcohol six years ago." / blank / "Here's what my life looked liked then vs. now:"). Do not run two hook sentences together in one paragraph unless the second is a half-sentence continuation of the first. A blank line costs a visible line on mobile, so the first line must already carry the stake.
- **The cut should land on a boundary.** If character 140 falls mid-word inside the payoff, move the payoff earlier or shorten.

Run `python3 scripts/hook_check.py draft.txt` (or pipe the draft in) before delivery. It prints the mobile and desktop slices, the first-sentence length, and warnings for a first sentence over budget, a mid-word cut, or a wasted early return. Include the two slices in the delivery note.

Author-specific evidence lives in `voice/hooks.md`. This file is the method.

## The four ingredients

A hook that earns the click usually carries three of these four. A hook with one is a caption.

| Ingredient | Question it answers | Weak version | Strong version |
| --- | --- | --- | --- |
| Stake | What does the author have on the line? | A third party's result, a general observation | The author's money, fear, embarrassment, decision or reputation |
| Specific | Can the reader picture it? | "a lot of founders", "recently", "a big number" | A dated event, a named person, an exact figure, a physical object, a quoted line |
| Tension | What contradiction must the body resolve? | A claim that needs no resolution | Big result versus small resource; success versus bad feeling; consensus versus "they're wrong"; then versus now |
| Stance | Can the reader agree or fight? | Balanced, hedged, "it depends" | A position half the intended readers will push back on and the other half will defend |

Numbers are a form of Specific, not a substitute for the other three. In the author's own corpus, first lines containing a number do not outperform first lines without one. A number earns its place when it creates Tension or proves Stake.

## Archetypes

Each archetype is a shape, not a template to fill. Choose by what the material actually contains. Names match `voice/hooks.md`, where each is tied to source posts and their engagement.

| Archetype | Shape | Use when the material has |
| --- | --- | --- |
| Law | One belief stated as fact, no hedge, then the case for it | A conviction the author has already argued in several places |
| Confession | A private fact stated flat, with life or business stakes | Something true and unflattering that the author is willing to publish |
| Correction | "Everybody thinks X. They're wrong. It's Y." | A consensus explanation and a better one the author can support |
| Big result, small resource | A milestone paired with the constraint that makes it surprising | A verified metric and an unusual input (team size, cost, time, one rep) |
| Anger at a norm | The author is annoyed by a behavior and says why | A recurring irritation with a principle underneath it |
| Scene | Time, place, people, and the awkward moment | A real event the author was present for |
| Dialogue | "Me: ... / Customer: ..." | A real exchange, or one clearly marked as reconstructed |
| Then versus now | Two dated states side by side | A past goal or state and a current state that comments on it |
| Found object | A letter, deck, spreadsheet or screenshot that surfaced | A real artifact the author can show or quote |
| Borrowed story with a twist | A well-known name plus the line nobody knows | A source quote the author can attribute and a lesson of their own |
| Exclusion | Who this is NOT for | A clear audience boundary that makes the intended reader feel chosen |
| Status list | "N things that make me feel ___ when I see them" | A list where every item carries the author's reaction |
| Bare list | Data with the argument withheld | Comparable facts that make the point without a sentence |
| Rage at a document | An artifact plus an unfiltered reaction | A real document worth reacting to |

## Order of moves inside the hook

A close reading of the author's 100 most recent hooks (`research/linkedin-hook-close-reading.md`) shows the strong ones make the same moves in roughly the same order. Use this as the sentence-level check after the ingredients are present.

1. **The author is the subject of the first clause.** "I", "Me:", "We", or the author's name reacting. Hooks that put a guest, a company or "if you're a founder" first sit at half the median. If the post is about someone else, the first clause still needs the author's stake in them.
2. **Temperature or money is on the line inside the first hundred characters.** Tired, embarrassed, feel bad, hate, could retire, don't want to do this anymore; or a figure the author can lose. Hooks that combine an author-first clause with a temperature word run at roughly double the median.
3. **Two facts that should not both be true, both visible before "see more".** Profitable but envious. Never hiring, just hired two. No signup link, somebody bought the $997 plan. Largest user, replaced it for $200. If the contradiction arrives after the fold, the fold has already lost the reader.
4. **The specific is textured, not round.** 17.3 million hits a week, 2.4 stars, 74 bought and 94 cancelled, an 8-person breakfast, $997. Round vanity numbers (150k followers, $100m pipeline, 3,000 to 400,000) mark the weak set.
5. **A judgment, not a report.** Moron, idiot, delusional, sucks, dead, wrong, the biggest mistake. The author decides; the reader argues.
6. **The promise comes last, if at all.** "Here's how" after a contradiction is fine. "Here's how" after an announcement is a caption. The five strongest hooks in the sample have no promise.

Words that cap a hook unless the same sentence overturns them: thrilled to announce, going live, tomorrow on the show, join us, giving away, don't miss this, if you're X this is for you, what if you could. If an event must be sold, the guest's most surprising fact and the author's stake go first; the invitation goes after the fold.

## Procedure

1. **Name the point.** One sentence: what the reader should think differently after reading. One sentence: who the reader is and what situation they are in. If either sentence is fuzzy, go back to the material.
2. **Find the tension.** List what contradicts what in the source: a number that does not match a feeling, a result that should have been impossible, an expert who says the opposite of the crowd, a past self who was wrong. No tension, no hook. Consider whether the post should exist.
3. **Write ten.** Draft ten hooks across at least four archetypes. Write each as the literal first one to three lines, not a description of a hook. Vary length: some one short line, some a dense two-sentence run.
4. **Score.** For each hook give 0 to 2 for Stake, Specific, Tension and Stance. Then apply the kill rules: an unsupported number, an invented person or exchange, a promise the body cannot pay off, or any pattern in `anti-slop.md` scores zero regardless.
5. **Truncate.** Cut each surviving hook at 140 characters. Does what remains still create the itch? If the first sentence is setup, move the payoff forward.
6. **Stranger test.** Read the top three as someone who has never heard of the author. What makes them click is not who is writing but what is at stake and what they are promised. If credibility is needed, it must be inside the hook as a specific, not assumed.
7. **Pick one, keep two.** Choose the hook the body can substantiate best, not the loudest. Keep the two runners-up for the delivery note. Check every figure against `identity/proof.md` before it goes out.

## Scorecard

| Criterion | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Stake | About someone else or no one | Author involved but nothing at risk | Author's money, reputation, fear or decision is exposed |
| Specific | Abstract nouns and vague quantities | One concrete detail | A detail the reader can picture, dated or named, verified in source |
| Tension | Statement needs no resolution | Mild curiosity | A contradiction the reader wants resolved |
| Stance | Hedged or neutral | A position, softly held | A position the reader will argue with |

Seven or eight of eight is a hook. Five or six may work if the body is exceptional. Four or below is a caption; rewrite.

## Common failures

- **Synopsis hook.** The first line summarizes the story instead of entering it. The author's own retellings that open on the summary underperform his retellings that open on the scene or the twist.
- **Promo hook.** "Tomorrow we're going live with..." earns registrations from people already interested and little else. If an event post is required, open on the guest's most surprising fact and the author's stake in it, then invite.
- **Hero hook.** A third party's impressive number with no author stake. Add the author's reaction or comparison, or reconsider the post.
- **Question hook.** A question the reader can answer with "no" and scroll on. Questions in first lines underperform in the corpus.
- **Listicle promise without a stake.** "7 best strategies for 2026" competes with every other list. "4 things that make me feel like shit when I see them on LinkedIn" is the same shape with a stake.
- **Credibility as biography.** "As the founder of three companies" is a label. "I bootstrapped $0 to $1m ARR three times" is a specific. Use the second form and verify it.
- **Manufactured tension.** A cliffhanger the body does not pay off. The click is bought, the reader leaves annoyed, and the next hook is trusted less.

## Endings, because the hook and the close are read together

The close should make the reader feel something rather than ask them to do something. Observed strong closes in the author's corpus: the verdict line (the post's argument compressed to a few words), the earned signature (a phrase the author actually repeats), the deflating joke, and the question only after a list the reader can genuinely add to. Generic prompts such as "What's your take?" and "Let's continue in the comments" kill the momentum the hook bought.

Read hook and close together before delivery. They should feel like one argument's first and last word.
