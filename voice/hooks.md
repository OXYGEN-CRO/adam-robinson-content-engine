---
type: context
status: draft
owner: adam
created: 2026-09-08
updated: 2026-09-08
sources: [raw/sources/2026-09-08-linkedin/posts.normalized.json, research/linkedin-hook-ranking.md, raw/sources/2026-09-08-youtube/videos/eUzqVJpZPP4/eUzqVJpZPP4.md]
tags: [voice, hooks, linkedin, source-backed]
---

# Hooks

## Summary

Observed opening lines from the 200 selected LinkedIn posts (2025-10-20 to 2026-09-07), grouped by the shape that earned attention, with the capture-time like count as evidence. The archetype names match the method in [[skills/linkedin-copywriter/hook-framework|the hook framework]]. This is an observed record for one profile, not author approval and not a performance guarantee: Adam says on August 27 that after 70m impressions he still cannot predict what a post will do [P8]. Likes are the primary signal here because ten posts gate a resource behind a comment and inflate comment counts; those are marked G. Full ranking and feature statistics: [[research/linkedin-hook-ranking]].

## What the corpus shows

- **Stake beats scale.** First lines that expose Adam's own feeling or risk (embarrassed, tired, pisses me off, feel like shit) sit at a median of 256 likes against 196 for the rest. First lines that promote an event sit at 115. First lines built on a third party's result with no Adam stake cluster near the bottom.
- **A number is not a hook.** First lines with a digit have a median of 193 likes; without, 227. The strongest numbered hooks pair the figure with a constraint or a feeling. Adam's stated method says he uses numbers in almost every hook; the record shows they work as proof inside a tension, not on their own [YT 04:31–05:02].
- **Questions underperform.** Twenty-eight first lines contain a question mark, median 154 likes. The exceptions are questions with a stake already stated ("So why do I still do this? When it's so fucking hard and I don't have to anymore.") [P46].
- **The first sentence is short; the first paragraph often is not.** Median first sentence 62 characters, and 184 of 200 first sentences finish inside the roughly 140 characters a phone shows before "…more". Median first paragraph 154 characters: he routinely runs a second or third sentence past the mobile cut for desktop readers, with the stake already landed. Measure drafts with `scripts/hook_check.py`.
- **Short lines are fine.** Sixty-two first lines are 80 characters or fewer, median 214. A single flat sentence with nothing after it is one of his strongest shapes.
- **Synopsis openings lose.** The December 14 backstory opens on its summary ("From 2016-2020, my email marketing startup was stuck at $3M ARR") and lands at 107 likes; the January 4 version of a related story opens on a scene ("In 2017, a CEO friend told me I was 'wasting my life'") and lands at 589 [P161] [P152].

## Close reading of the last 100

Every pre-"see more" passage of the 100 newest posts (2026-03-09 to 2026-09-07) was read and hand-tagged by the moves it makes; the per-hook notes and full statistics are in [[research/linkedin-hook-close-reading]]. Median likes across the 100 is 217. The moves that separate the top from the bottom:

| Move | With | Without |
| --- | --- | --- |
| Adam is the subject of the first clause and a temperature word appears in the first hundred characters (tired, embarrassed, feel bad, hate, moron, delusional) | 376 (n=14) | 194 |
| Adam is the subject of the first clause and a contradiction is visible before see-more | 294 (n=28) | 186 |
| An explicit verdict (idiot, wrong, sucks, mistake, dead, not how) | 270 (n=28) | 182 |
| Announcement, invitation or pitch language in the first clause with no contradiction (thrilled to announce, going live, tomorrow, giving away, if you're X this is for you) | 106 (n=14) | 234 |
| A third party or company as the subject with no contradiction | 130 (n=18) | 234 |
| An open question (the question is the hook) | 119 (n=7) | 220 |
| A "Here's…" promise | 185 (n=19) | 227 |

What the strong hooks do, in order: Adam is in the first clause; his temperature or his money is on the line; two facts that should not both be true appear inside the first hundred characters; the specific is textured rather than round (17.3 million hits a week, 2.4 stars on Glassdoor, 74 bought and 94 cancelled, an 8-person breakfast); and he passes judgment rather than reporting. The five strongest hooks of the 100 have no "Here's…" promise at all. The promise is neutral at best; what precedes it decides the post.

What the weak hooks do: they put a guest, a company or the reader in the first clause; they open with announcement or invitation language; they ask a genuinely open question; they report a fact without judging it; and when a promo is coming, it shows before see-more. Announcement language survives only when the same sentence subverts it: "Thrilled to announce that after saying I would never hire people, I just hired two" (398) and "MoltSets has crossed $100k ARR … BEFORE even entering beta" (250) against "I'm thrilled to announce the MoltSets waitlist has crossed 5,000 members" with the twist arriving 150 characters later (131).

Two shapes need a second line to work. Dialogue earns the click when line two changes the meaning of line one ("Me: I think RB2B will stall out at around $12-13m. / Diana: Remember when that was the dream?", 372) and fails when line two is only a joke ("Marty Kausas: Why do you hate VCs so much? / Me: How much time do you have?", 119). A question earns the click after a concrete fact with the answer implied ("WTF is Apollo supposed to do here?" after two revenue lines, 255) and fails as the opener ("What actually IS an autonomous business?", 116).

Repetition is visible: "$10M ARR is the FU MONEY of SaaS" took 1550 likes in January and 256 when repeated in April as the opener of a longer breakdown.

## Archetypes with evidence

Quotations are exact first lines. Likes are capture-time snapshots. Source posts are research material; none is cleared for reuse as new copy.

| Archetype | Exact first line | Likes | Source |
| --- | --- | --- | --- |
| Law | "$10M ARR is the FU MONEY of SaaS." | 1550 | [P153] |
| Confession | "I quit drinking alcohol six years ago." | 1482 | [P79] |
| Correction | "Everybody thinks Clay raised at a $3.1B valuation because they grew 300% in 6 months. They're wrong. They raised at $3.1b because they built a culture of Customer Discovery and Product Iteration." | 1383 | [P190] |
| Big result, small resource | "I bootstrapped my first startup to $13m ARR in 26 months with only one sales rep doing OUTBOUND sales. The crazy part? Diana Ross did the same demo over 2,000 times using the same 10-slide deck." | 811 G | [P140] |
| Borrowed story with a twist | "After the founder of Twitch (Justin Kan) sold his company to Amazon for $1 billion, an interviewer asked him, 'Don't you think you won the lottery?' His answer was the best description of being a founder I've ever heard:" | 957 | [P106] |
| Anger at a norm | "It pisses me off when founders act like the fact that I am running my business to make money is some kind of low brow pursuit." | 861 | [P139] |
| Rage at a document | "FOUNDERS: WHAT KIND OF FUCKING MORON SIGNS UP FOR THIS?!?" | 782 | [P17] |
| Bare list | "Clay ($204m raised)" followed by four more funded competitors and RB2B's figure | 742 | [P58] |
| Scene | "Last week I was at an 8-person founder breakfast in Aspen. Guy goes around the table and asks everyone how they're using AI day-to-day. I was super embarrassed to answer the question, but I did." | 737 | [P97] |
| Exclusion | "I want to be crystal clear: the advice I give on LinkedIn is NOT for founders who think they're creating unicorns, decacorns, or the next Anthropic." | 575 | [P116] |
| Status list | "4 things that make me feel like shit about myself when I see them on LinkedIn:" | 532 | [P185] |
| Found object | "This is the only cold email I answered in the last 12 months." | 476 | [P117] |
| Found object | "I found a handwritten letter I wrote to myself in May 2016. 9 years later, it breaks my heart to read it." | 394 | [P172] |
| Dialogue | "Me: I think RB2B will stall out at around $12-13m." / "Diana: Remember when that was the dream?" | 372 | [P53] |
| Then versus now | "Me in 2019: I want a $25m ARR biz w/ under 35 employees." / "Retention.com today: $23m ARR, 27 FTE." | 368 | [P15] |
| Law, addressed | "MESSAGE TO FOUNDERS: You are not allowed to want to make money." | 357 | [P111] |
| Scene, dialogue body | "Last week somebody secretly bought MoltSets unlimited $997/mo plan - EVEN THOUGH THERE IS NO SIGNUP LINK YET." | 227 | [P47] |

Guest and event posts have a different job (registration), so a lower like count is not failure. The strongest of them still opens on the guest's most surprising fact and Adam's stake: "Taylor Haren was Clay's largest user at one point, hitting their platform 17.3 million times per week. Last month he replaced it with a $200/mo Claude Code subscription." (597 likes) [P80]. Compare the promo-first opening "We're going LIVE tomorrow with the OG of prospecting Jed Mahrle..." (53 likes) [P22].

## Openings that underperformed

| Shape | Exact first line | Likes | Source |
| --- | --- | --- | --- |
| Promo first | "You don't want to miss this! Tomorrow I'm going deep on ABM with Canberk Beker..." | 65 | [P96] |
| Data dump | "Here's a quarter-by-quarter MRR and churn rate comparison of Retention.com ($20m ARR) and RB2B ($6.6m ARR), from launch until 2 years in:" | 74 | [P176] |
| Hero without stake | "Will McTighe went from 3,000 to 400,000 LinkedIn followers in 20 months." | 81 | [P83] |
| Predictions list | "My predictions for Retention.com and RB2B for 2026:" | 65 | [P124] |
| Generic listicle | "These are the 7 best SaaS marketing strategies for 2026. 👇" | 101 | [P178] |
| "This is for you" | "If you're an early-stage SaaS trying to scale AI outbound and have no idea what intent signals actually matter, this is for you 👇" | 93 | [P175] |
| Synopsis | "From 2016-2020, my email marketing startup was stuck at $3M ARR. Literally *nothing* I did moved the needle. I was completely demoralized." | 107 | [P161] |
| Giveaway first | "I'm giving away a free Claude Skill that tells you which customers are about to churn AND hands you their cell phone number to stop it." | 89 | [P26] |

These are not banned shapes; they are shapes that need a stake or a tension added before they earn the click.

## Adam's stated hook rules

From the April 16, 2026 video and the March 7, 2026 post, kept distinct from the observed record above: the hook is everything before "see more" and its only job is the click; write every hook as if nobody has heard of you; build credibility with specific numbers; find the polarizing position that half the intended readers defend and half push back on; say the things you would only say to your spouse behind closed doors. He names Chris Walker for hooks and his own posts for closes [YT 00:29–02:42, 04:02–05:02] [P101]. The corpus supports the credibility and polarity rules and qualifies the numbers rule as above.

## Closes read with the hook

Strong observed closes compress the argument to a verdict ("Not quitting sooner." [P79]; "One discovery call at a time." [P190]; "They just kept buying tickets." [P106]), use a phrase he actually repeats ("Keep building." [P152] [P17]; "If you can bootstrap, bootstrap." [P2]), deflate with a joke ("Oh yea - can't wait for what the AI bots do with this one…" [P25]) or ask only after a list the reader can extend ("Did I miss anything in my analysis???" [P117]). He recommends against generic questions and in practice ends some posts with "Thoughts?" [P86]; preserve the variety rather than a rule.

## Related Pages

- [[voice/linkedin-voice]]
- [[voice/formats]]
- [[research/linkedin-hook-ranking]]
- [[identity/proof]]
- [[inspiration/creator-bank]]

## Source Notes

Exact first lines and capture-time like counts from `posts.normalized.json`; P numbers follow the recency rank used in [[voice/linkedin-voice]]. YT timestamps refer to the April 16, 2026 video transcript. Public-source research does not clear new first-person copy.

[P2]: ../raw/sources/2026-09-08-linkedin/posts/2026-09-04-7501664626724630528.md
[P8]: ../raw/sources/2026-09-08-linkedin/posts/2026-08-27-7498815008437460992.md
[P15]: ../raw/sources/2026-09-08-linkedin/posts/2026-08-18-7495491952788787200.md
[P17]: ../raw/sources/2026-09-08-linkedin/posts/2026-08-14-7494078350827794432.md
[P22]: ../raw/sources/2026-09-08-linkedin/posts/2026-08-03-7490075832640487424.md
[P25]: ../raw/sources/2026-09-08-linkedin/posts/2026-07-27-7487540559046209536.md
[P26]: ../raw/sources/2026-09-08-linkedin/posts/2026-07-26-7487206225135226880.md
[P46]: ../raw/sources/2026-09-08-linkedin/posts/2026-06-25-7475952078696259585.md
[P47]: ../raw/sources/2026-09-08-linkedin/posts/2026-06-23-7475236994441207810.md
[P53]: ../raw/sources/2026-09-08-linkedin/posts/2026-06-13-7471603042836971520.md
[P58]: ../raw/sources/2026-09-08-linkedin/posts/2026-06-02-7467608974775857153.md
[P79]: ../raw/sources/2026-09-08-linkedin/posts/2026-04-22-7452784741797294080.md
[P80]: ../raw/sources/2026-09-08-linkedin/posts/2026-04-19-7451678381395537920.md
[P83]: ../raw/sources/2026-09-08-linkedin/posts/2026-04-13-7449536001334501377.md
[P86]: ../raw/sources/2026-09-08-linkedin/posts/2026-04-02-7445528673232879618.md
[P96]: ../raw/sources/2026-09-08-linkedin/posts/2026-03-16-7439395242081996800.md
[P97]: ../raw/sources/2026-09-08-linkedin/posts/2026-03-14-7438643286480879616.md
[P101]: ../raw/sources/2026-09-08-linkedin/posts/2026-03-07-7436114197618245632.md
[P106]: ../raw/sources/2026-09-08-linkedin/posts/2026-02-28-7433601853990379520.md
[P111]: ../raw/sources/2026-09-08-linkedin/posts/2026-02-20-7430650697265635328.md
[P116]: ../raw/sources/2026-09-08-linkedin/posts/2026-02-13-7428154240784801793.md
[P117]: ../raw/sources/2026-09-08-linkedin/posts/2026-02-10-7427068419633586176.md
[P124]: ../raw/sources/2026-09-08-linkedin/posts/2026-02-04-7424877253005811712.md
[P139]: ../raw/sources/2026-09-08-linkedin/posts/2026-01-21-7419825711693217793.md
[P140]: ../raw/sources/2026-09-08-linkedin/posts/2026-01-20-7419429963537203202.md
[P152]: ../raw/sources/2026-09-08-linkedin/posts/2026-01-04-7413603368109051904.md
[P153]: ../raw/sources/2026-09-08-linkedin/posts/2026-01-03-7413231165542952960.md
[P161]: ../raw/sources/2026-09-08-linkedin/posts/2025-12-14-7405993222897868800.md
[P172]: ../raw/sources/2026-09-08-linkedin/posts/2025-11-29-7400611884409896960.md
[P175]: ../raw/sources/2026-09-08-linkedin/posts/2025-11-24-7398826829672988672.md
[P176]: ../raw/sources/2026-09-08-linkedin/posts/2025-11-22-7398097563540709378.md
[P178]: ../raw/sources/2026-09-08-linkedin/posts/2025-11-20-7397373460072554496.md
[P185]: ../raw/sources/2026-09-08-linkedin/posts/2025-11-11-7394074688689225729.md
[P190]: ../raw/sources/2026-09-08-linkedin/posts/2025-11-06-7392232550368374784.md
[YT]: ../raw/sources/2026-09-08-youtube/videos/eUzqVJpZPP4/eUzqVJpZPP4.md
