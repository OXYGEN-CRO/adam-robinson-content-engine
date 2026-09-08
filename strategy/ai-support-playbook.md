---
type: context
status: draft
owner: adam
created: 2026-09-08
updated: 2026-09-08
sources: [raw/sources/2026-09-08-youtube/selected-100.json, raw/sources/2026-09-08-youtube/videos/C7n2q31PPh4/C7n2q31PPh4.md, raw/sources/2026-09-08-youtube/videos/jkBFQ85hV30/jkBFQ85hV30.md, raw/sources/2026-09-08-linkedin/posts/2026-05-22-7463630759023529985.md, research/audit-ai-support-clips.md, research/audit-documentary-and-early-support.md]
tags: [ai-support, documentation, human-escalation, operating-principles]
---

# AI support playbook

## Scope and ownership

This is a practical synthesis of the **August 14, 2024** support webinar and the **July 30, 2025** discussion with Adam, Pete and Robb and its ten accompanying clips, all read in full. The July clips repeat the longer conversation; they are one case study, not eleven independent demonstrations. Robb describes most documentation and support operations. Adam describes his sales clone, daily answer review and founder-level business claims. Captions do not identify speakers, so uncertain interjections remain attributed to the discussion rather than Adam. The separate May 22, 2026 LinkedIn update supplies a later, explicitly dated self-report.

The central idea: repetitive customer interaction can become a maintained knowledge system. Human work continues in documentation, product fixes, answer review and escalations. This page expands [[strategy/learnings]] and preserves historical tool choices; it is not a current vendor comparison. The workflow order below is an editorial synthesis, not a numbered process stated verbatim by the speakers.

## The early baseline: three ways to self-serve

In August 2024, Robb explicitly separates **knowledge-base articles, rule-based self-service workflows and an AI support agent**, with human help available as a fallback. The workflows are reusable topic branches, such as installation or billing, and operate independently of AI. This matters when interpreting the remarkably low human-involvement percentage: it includes successful self-service that never involved Fin. [[raw/sources/2026-09-08-youtube/videos/jkBFQ85hV30/jkBFQ85hV30|05:11–05:24; 13:19–14:35; 17:14–17:47]]

He describes investing substantial initial attention in the system: five hours a week is not a realistic promise of quick completion. Turning repeated inbox questions into articles frees time to improve the next part. Even the “one support agent” headline has a time boundary: during this webinar he announces that another support hire has accepted and will start the following Monday. This is a support-operation story, not the headcount of the whole business. [[raw/sources/2026-09-08-youtube/videos/jkBFQ85hV30/jkBFQ85hV30|03:49–04:19; 21:53–22:56; 23:50–26:03]]

## Build and maintain the knowledge

1. **Start with recurring questions that consume support time.** Robb starts with the questions that provoke “not again.” Turn the answer already being written for a customer into a reusable article, then send the article on subsequent occasions. The discussion suggests one article a day as an achievable starting habit; the six-month article totals are illustrative arithmetic, not a reported production result. [[raw/sources/2026-09-08-youtube/videos/_3zVR0AQLhc/_3zVR0AQLhc|Support docs, 00:05–02:10]]

2. **Write complete instructions that both people and AI can read.** Robb recommends clear headings, defined sections, lists and precise text. Explain what to click and where; a screenshot with an arrow should not contain the only instruction. His observation that Fin was only beginning to handle images belongs to July 2025. His custom GPT reformats articles he has written, adds structure and fixes grammar; it does not establish the product facts. A sensible implementation rule is to check the revised article against the actual product before publishing—this review rule is our interpretation, not a measured result from the demonstration. [[raw/sources/2026-09-08-youtube/videos/ZtJaI-5_sVk/ZtJaI-5_sVk|Writing for AI and humans, 00:25–02:22]]; [[raw/sources/2026-09-08-youtube/videos/fZrJqB1xG4w/fZrJqB1xG4w|Robb's editing GPT, 00:04–01:46]]

3. **Use FAQs to retain the customer's language and edge cases.** Put the question as customers actually ask it, then restate enough context for its answer to stand alone. Group FAQs with the relevant topic or integration. The discussion describes question analytics as one way to discover repeated wording and weak answers. Robb's “80%” core-use-case example and talk of AI confidence are explanatory heuristics, not measured coverage or calibrated confidence scores. [[raw/sources/2026-09-08-youtube/videos/4vJt-djbbNw/4vJt-djbbNw|FAQ design, 00:04–02:39]]

4. **Create troubleshooting branches, not a list of generic fixes.** Map the observed symptom or exact error message to likely causes and explicit next steps. Robb's “no profiles collected” example distinguishes never collecting, an account running out of credits, a trial ending, and a removed script. Order likely causes first. For a vague login complaint, ask whether the email is unrecognized, the login email never arrived, or a 403 appeared after login before giving the relevant instructions. Available account state can narrow the branch further. [[raw/sources/2026-09-08-youtube/videos/Wr1-CoTwg8s/Wr1-CoTwg8s|Troubleshooting, 00:28–03:51]]; [[raw/sources/2026-09-08-youtube/videos/nhQKi4F3GzA/nhQKi4F3GzA|Clarifying the symptom, 00:30–03:00]]; [[raw/sources/2026-09-08-youtube/videos/C7n2q31PPh4/C7n2q31PPh4|Account context, 33:43–34:44]]

5. **Record changes with a date and explanation.** Robb uses changelogs to explain what changed, when and why, so support can distinguish old behavior from a fixed bug. The discussion recommends a short entry for code changes or fixes. Its July 7 Apollo-integration scenario illustrates this use; it is not a separately verified release record. [[raw/sources/2026-09-08-youtube/videos/dBmCgPPA2iA/dBmCgPPA2iA|Changelogs, 00:04–02:00]]

**Keep canonical instructions synchronized with releases.** The earlier webinar supplies a concrete maintenance practice: Robb pre-edits pricing articles and workflows, then publishes them when the product change goes live. He recalls doing this twice on June 6, 2024 after the first pricing revision proved wrong. He tests likely customer questions about pricing and credit usage, repairs the article if the answer fails, and continues checking live conversations. A changelog therefore complements maintained instructions; it does not replace them. His statement that Fin immediately ingested revisions describes that historical system, not a universal refresh guarantee. [[raw/sources/2026-09-08-youtube/videos/jkBFQ85hV30/jkBFQ85hV30|26:25–29:48]]

## Guide the interaction and keep a human route

**Documentation describes the product; guidance describes how to conduct the conversation.** Robb treats guidance like a prompt: ask for missing context, choose sources, decide when to link an article, handle edge cases and specify when to escalate. The source does not supply a complete escalation policy. The earlier webinar does describe a direct route: if the user asks for a human, connect them without extra hoops and give a timing note. It also asks users to handle one question at a time and permits switching back to self-service. [[raw/sources/2026-09-08-youtube/videos/nhQKi4F3GzA/nhQKi4F3GzA|Guidance, 00:30–03:01]]; [[raw/sources/2026-09-08-youtube/videos/jkBFQ85hV30/jkBFQ85hV30|11:56–13:19]]

**Give the agent only the operational authority intended for it.** In August 2024 Robb says it cannot act in the billing platform; trial restarts go to a person. This limits what a manipulated answer can execute. He also avoids adding discount information, but absence from documentation does not prove a model cannot invent a discount. The same webinar says live account data is still a planned integration; July 2025 describes it in use. Access to contextual data and permission to change an account are separate decisions, and the later integration does not prove billing authority was added. [[raw/sources/2026-09-08-youtube/videos/jkBFQ85hV30/jkBFQ85hV30|07:49–08:32; 30:34–33:02]]; [[raw/sources/2026-09-08-youtube/videos/C7n2q31PPh4/C7n2q31PPh4|33:43–34:44]]

**Test the route for loops.** Their human-facing articles sometimes said to email support. Fin repeated that instruction while already providing support; the email then reached Fin again. Robb added guidance not to refer the person back to the same support channel. He reports that this removed that frustration. This is a specific repaired loop, not proof that all escalations or customer frustrations disappeared. [[raw/sources/2026-09-08-youtube/videos/nhQKi4F3GzA/nhQKi4F3GzA|Support-to-support loop, 03:34–05:53]]

**Make unresolved questions visible while building the knowledge base.** Adam reports keeping Delphi's creativity setting on “strict” for a month to expose questions without documented answers. He distinguishes a missing article from an existing article that the bot interprets badly. His later move to a more adaptive setting and off-topic TV-show example are historical choices, not evidence that broad improvisation improves support accuracy. The durable principle is to surface a knowledge gap so a human can close it. [[raw/sources/2026-09-08-youtube/videos/S3fI3M3ckVE/S3fI3M3ckVE|Finding documentation gaps, 03:53–05:30]]

## Review conversations and choose the repair

Robb describes reviewing AI conversations, including already resolved cases, while especially inspecting escalations. Adam describes spending about half an hour a day improving his clone's answers and applying the standard he would expect of a human employee. Their proposed job change is from repeatedly answering tickets to improving future answers, with Robb still handling exceptions. [[raw/sources/2026-09-08-youtube/videos/I0OCKRPDQPY/I0OCKRPDQPY|Review habit and human work, 00:03–04:09]]

| What the conversation reveals | Repair supported by the discussion | Case or boundary |
| --- | --- | --- |
| Users repeatedly cannot find something | Improve the interface so the question need not arise | Robb moved plan, credits used and subscription controls into the sidebar; he reports those questions disappeared. No before/after counts are supplied. |
| A release creates confusing behavior | Fix the product presentation | A combined list buried person-level visitors among company-level results. Separating the views reportedly removed confusion; the example is about presentation, not proof that identification accuracy changed. |
| No source answers the question | Write the missing article or FAQ | Adam used unanswered questions to locate documentation gaps. |
| The answer is documented but the bot gets it wrong | Revise the answer or conversational guidance | Correct the failure instead of assuming that adding more documents will solve it. |

The first two examples come from Robb's account at [[raw/sources/2026-09-08-youtube/videos/S3fI3M3ckVE/S3fI3M3ckVE|00:31–03:30]]; the repair distinction follows at [[raw/sources/2026-09-08-youtube/videos/S3fI3M3ckVE/S3fI3M3ckVE|03:31–05:30]]. Although this upload's title says **four pillars**, the discussion names **three**: interface improvement, support documentation and answer revision. This table separates two product examples without inventing a fourth pillar.

## Historical division between sales and support tools

| July 2025 role | Reason given in the conversation | Limits stated then |
| --- | --- | --- |
| Delphi before account creation | Adam wanted visitors arriving from his thought leadership to question a clone of him and resolve the few barriers to a free signup. | Adam said reporting and workflows were limited, and email capture required a Delphi account. He suspected this stopped conversations but explicitly lacked hard data. |
| Intercom Fin after signup | Robb valued app integration and customer-specific information such as plan, credits and account status for support diagnosis. | Adam said it did not supply his desired personal clone. Robb's preference for Fin if restricted to one tool was specific to his support work. |

These statements describe their setup and perceptions on **July 30, 2025**. They do not establish present capabilities, comparative accuracy, or a recommendation to buy either product. [[raw/sources/2026-09-08-youtube/videos/QqNhenP7jao/QqNhenP7jao|Full comparison, 00:04–05:42]]

The choice evolved: in August 2024 Robb prioritized support and preferred avoiding two separate bots. By July 2025 the team accepted two tools because the founder-clone sales experience served a distinct need. Preserve the stage-specific tradeoff rather than treating either setup as an unchanging rule. [[raw/sources/2026-09-08-youtube/videos/jkBFQ85hV30/jkBFQ85hV30|41:03–42:42]]

## What was claimed, and what remains unmeasured

| Date and source | Attributed statement | Evidential limit |
| --- | --- | --- |
| August 1–11, 2024, reported in the August 14 upload | Robb reports 4,600 support instances, 97 handled by a human (2.1%). For July 1–August 11: about 17,000 instances, 472 human-handled (2.8%). | Includes articles and non-AI workflows. The complements are not AI resolution rates. Rounded denominators and reported percentages are retained. [[raw/sources/2026-09-08-youtube/videos/jkBFQ85hV30/jkBFQ85hV30|05:34–06:06]] |
| August 2024 webinar | Fin joins about 74% of support conversations and resolves 60% of those; the longer July 1–August 11 comparison is 75% involvement and 56% resolution. | Conversation subset, unlike total support instances. Robb later says an unanswered follow-up can count as assumed resolution when the user disappears; these are not all explicit confirmations of success. [[raw/sources/2026-09-08-youtube/videos/jkBFQ85hV30/jkBFQ85hV30|06:40–07:19; 35:32–36:08]] |
| August 2024 webinar; saved-time estimate explicitly concerns July | Approximately $180 for the AI component and an estimated 136 hours saved. | The $180 billing period is not clearly stated. It is the AI component, not an all-in support cost including platform fees and human work. Saved time is modeled at 15 minutes per resolved conversation, not time-tracked. Historical pricing is not a current offer. [[raw/sources/2026-09-08-youtube/videos/jkBFQ85hV30/jkBFQ85hV30|35:09–37:45]] |
| July 30, 2025 discussion | Adam says roughly 60,000 free users, $5.5m ARR and three people; he describes Robb improving support answers and handling escalations. | Historical founder self-report. Free users are not paying customers; three people is not evidence of zero human work or a complete accounting of shared resources. [[raw/sources/2026-09-08-youtube/videos/I0OCKRPDQPY/I0OCKRPDQPY|03:19–03:55]] |
| July 30, 2025 discussion | Adam estimates about 60 people asking roughly three questions each per day, or approximately 180 questions to his clone. | He corrects himself from “60 questions” to people; this is conversational arithmetic, not a logged support-ticket count. [[raw/sources/2026-09-08-youtube/videos/C7n2q31PPh4/C7n2q31PPh4|19:12–19:31]] |
| July 30, 2025 publisher description | “95%” of B2B sales, marketing and customer support is described as being done over AI. | Broad promotional wording in the description, without a supplied denominator or measurement window. Do not relabel it as ticket resolution. [[raw/sources/2026-09-08-youtube/videos/C7n2q31PPh4/C7n2q31PPh4.info.json|Captured metadata, description]] |
| May 22, 2026 LinkedIn post | Adam says Fin began at 25% resolution and now handles 98.9% of all tickets, escalating 1.1%; Robb handles escalations in 15 minutes a day or less. The post also reports RB2B crossing $9m ARR. | Later self-report with no dashboard, denominator, period or independent quality audit supplied. “Handles” is his wording; it should not silently become independently verified successful resolution. [[raw/sources/2026-09-08-linkedin/posts/2026-05-22-7463630759023529985|May 22 update]] |

The later post credits a deliberately simple product and Robb Clarke's documentation, alongside unusually favorable existing distribution and data economics. Adam explicitly warns that his situation cannot simply be copied. It supports continuity of the operating idea, not a controlled causal claim that documentation alone produced the reported rate.

For another team's implementation, a useful **proposed measurement plan** is to record the time window, eligible ticket count, AI-handled count, human escalation count and reviewed answer-quality failures separately. Inspect resolved conversations as well as exceptions, and track recurrent product problems before and after changes. This plan is our interpretation of the review discipline; these particular measurements were not supplied in the sources. Keep [[identity/proof]] and [[identity/source-conflicts]] as the authority for dated business claims.

## Related Pages

- [[strategy/learnings]]
- [[strategy/youtube-library]]
- [[strategy/source-policy]]
- [[identity/proof]]
- [[identity/source-conflicts]]

## Source Notes

[[research/audit-ai-support-clips]] inventories all eleven fully read transcripts, their caption bounds, attribution limits and overlap. Their exact captions and metadata remain under [[raw/sources/2026-09-08-youtube/index]]. The source set is ranks 34–44 of the captured selection, all published July 30, 2025; the selection itself was captured September 8, 2026. Sources are automatic captions, not audio-verified transcripts. Editorial spelling normalizations such as Fin, Delphi and RB2B follow the surrounding discussion and metadata; raw text is unchanged.

[[research/audit-documentary-and-early-support]] adds the full read of rank 100, `jkBFQ85hV30`, published August 14, 2024. The early webinar is a baseline with different denominators and capabilities, not a contradiction automatically resolved by later rates. Its ambiguous framing of the bot as “our team” is documented in the audit, not adopted as a recommended disclosure practice. The discussion's third-party legal anecdotes and forecasts about future voice/image capabilities are not validated guidance.

All results are attributed claims or qualitative anecdotes. No current product documentation, account dashboards, underlying support corpus or custom GPT configuration was inspected for this page. Public availability supports the requested context research; approval for new first-person publication remains unresolved.
