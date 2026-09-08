---
type: research
status: draft
owner: adam
created: 2026-09-08
updated: 2026-09-08
sources: [raw/sources/2026-09-08-youtube/videos/7p-QD-3MtBw/7p-QD-3MtBw.md, raw/sources/2026-09-08-youtube/videos/JaN_78GB638/JaN_78GB638.md, research/youtube-video-notes/7p-QD-3MtBw.json]
tags: [audit, youtube, history, attribution, bootstrapping]
---

# Aye Moah conversations: source and history audit

## Finding

**The March 2025 upload is a different conversation, not a repeat of the November 2024 episode.** November covers Moah's founding story and operating practices with Adam and Santos. March introduces her as a returning guest, adds Boomerang co-founder Alex and the acquired product's founder Cameron, and discusses an acquisition announced in December 2024 and results from the first two months of 2025. The acquisition's name is inconsistently captioned as “gqs,” “GQ” and “Jus”; this audit does not treat automatic spelling as verified branding.

The March title's **$10m sale and $1m banker fee belong to Adam's Robly account**, not Moah's exit. Adam reports signing a contract, paying the fee and later regretting it. The title's “SCAMMED” framing is not an established fraud finding. Moah describes a separate earlier near-sale that she abandoned; neither its buyer nor its date is established. [[raw/sources/2026-09-08-youtube/videos/7p-QD-3MtBw/7p-QD-3MtBw|00:28–01:43; 38:41–39:40]]

## Reading and exact evidence

Read **all 2,654 normalized caption segments, containing 19,422 words**, without title-only or keyword-only substitution. March was read in contiguous windows before and from 28:00; November before and from 29:00. Together those windows include every segment, including the March montage and separate closing teaser. Both captured metadata descriptions and publication fields were inspected. Captions are automatic and lack speaker labels; no audio, video or external transaction records were reviewed.

| Rank / ID | Public release UTC | Listed duration | Segments / words | First start / last start / maximum end, seconds |
| --- | --- | --- | --- | --- |
| 68 — [[raw/sources/2026-09-08-youtube/videos/7p-QD-3MtBw/7p-QD-3MtBw|7p-QD-3MtBw]] | 2025-03-18 22:35:29 | 55:46 | 1,338 / 9,984 | 0.120 / 3343.559 / 3348.359 |
| 87 — [[raw/sources/2026-09-08-youtube/videos/JaN_78GB638/JaN_78GB638|JaN_78GB638]] | 2024-11-13 15:00:05 | 57:12 | 1,316 / 9,438 | 0.520 / 3426.559 / 3431.720 |

Both captured records identify Adam's channel `UCSHn0Px37BjzMqnZBmVWwcQ` and have `was_live: false`. November has equal upload and release timestamps; March has an upload timestamp and no separate release timestamp. The conversational live-audience format does not override those metadata fields. Small differences between caption extent and listed duration do not prove additional speech.

| Artifact | SHA-256 |
| --- | --- |
| March Markdown | `4389e0a0bb902fb52612a814d042a9c2cd16cb93d7836eede886ea79007e4bcd` |
| March normalized transcript JSON | `faaaf170eb3ab280b19dab1822e9bd6cf70cc5e42b84d718ee3a9115a13d32ee` |
| March metadata JSON | `b2cabab8f13f2230d924b31e52e667decc7e4f6bcc1d5d8228392345653f512a` |
| November Markdown | `f190c591fa1a306b1918ff940f673a0490056a88579e1da55109392a90e4778c` |
| November normalized transcript JSON | `9011a6246cd0b1b81f275577e9424fba201868e20cd303904c129c00fd3ce49d` |
| November metadata JSON | `c42338675151f00b0d50f2f128379dc0bf7a88fc748f08303119dfdee674455d` |
| March original structured note | `7dfc4c325f8532d001a6cb287a56e16932e516583e30364c2827d3f6819a5269` |
| March original provenance | `463eeaade9dc8953840156ed6d2733a223ae0046f2c3d81009def4b1ebcf6354` |

The March note's recorded source hash matches the Markdown above, provenance has `exit_code: 0`, and its retained event stream ends in `turn.completed`. The complete original JSON matches the final terminal agent message. Every field of that note was read. At **2026-09-08 09:35:33 UTC**, the November structured note was not present; this audit makes no claim about its eventual extraction fidelity and did not launch another reader.

## Why these are distinct episodes

- March explicitly says Moah has appeared before at 01:46–02:00. It introduces Alex and Cameron, who are absent from the November interview, and later refers back to the prior discussion about repeatable processes. [March 01:46](https://www.youtube.com/watch?v=7p-QD-3MtBw&t=106); [24:17](https://www.youtube.com/watch?v=7p-QD-3MtBw&t=1457)
- March's sourcing story begins with 2022 outreach, but the answer at 12:49–12:56 specifically dates the **announcement** to December 2024. A host later calls the interview roughly three months after signing; that is approximate retrospective timing, not an independently documented closing date. The 2025 goal update at 51:14–51:34 places the discussion after the first two months of that year. [12:49](https://www.youtube.com/watch?v=7p-QD-3MtBw&t=769); [46:41](https://www.youtube.com/watch?v=7p-QD-3MtBw&t=2801); [51:14](https://www.youtube.com/watch?v=7p-QD-3MtBw&t=3074)
- November closes by advertising a replay at 9 a.m. “tomorrow” and next week's Eric Siu discussion about B2B SEO in 2024. The recording therefore preceded the intended replay; the precise recording date/time and timezone are not independently supplied. Do not automatically turn November 13's upload into the recording date. [November 56:24–57:06](https://www.youtube.com/watch?v=JaN_78GB638&t=3384)
- As a mechanical cross-check, tokenizing all text with case-folded `[a-z0-9']+` and comparing exact 12-token windows found **zero shared windows** among 9,923 unique March and 9,457 unique November windows. This supports the full-read finding; caption variation means textual overlap alone cannot establish or exclude a re-edit.

## Full-read coverage and speaker boundaries

| November range | Material read and interpretation retained |
| --- | --- |
| 00:00–09:00 | Moah's MIT/immigration context, UX work, supporting the startup through salary and lower rent, first $100k check, $400k total financing, early product and voluntary subscriptions, 40% lifetime discount, roughly 18 months to covering founder salaries. These are Moah/Boomerang history, not Adam's. |
| 09:00–19:08 | Hiring against large Silicon Valley employers, platform competition, 2019 retrenchment, power-user retention, Google overture, collaborative values and documentation, team/ARR milestones. Google motive is expressly speculative; an overture is not an exit. |
| 19:08–28:41 | Adam's discussion of headcount pressure, hiring overshoot and reduced focus; Moah's support-trained company; Adam's praise and his different Robb/Intercom support model. He wishes for her support culture rather than claiming he already has it. |
| 28:41–37:00 | Moah's conditional financing preference, funnel experiments and early Australian outbound targeting; first two meetings were scheduled, not closed sales. Adam describes a first Retention.com enterprise proof of concept and its unexpected complexity. |
| 37:00–42:36 | Separate offshore/team examples from Moah, Santos and Adam. Adam describes manual outbound, customer-account audits, an earlier Argentina team and the subsequent Canadian engineering-manager approach. |
| 42:36–51:51 | Moah's customer-led roadmap, technical differentiation, work boundaries, SEO/AI concerns, unsent product features, response data and the original enterprise idea that gave way to snooze/send-later. Adam identifies RB2B's then-current “what now?” problem after identifying a visitor. |
| 51:51–57:06 | Moah's contribution-based staffing judgment and charitable activity; Adam's admission that he has lost operating discipline before and his explicit wish to use his audience to tell stories about this alternative founder path. |

| March range | Material read and interpretation retained |
| --- | --- |
| 00:00–09:55 | Montage, Adam's Robly fee regret, returning guests, Lucid Club pitch and audience-fit limits. Pitch-poll reactions do not validate demand from the actual regulated-industry buyers. |
| 09:55–19:53 | Founder-to-founder sourcing, delayed LinkedIn connection, December announcement, deal-structure research, counsel and valuation advice, major terms and bank-account handover. “No banker-led transaction” does not mean no professional advice. |
| 19:53–27:00 | Product/customer/values alignment, Cameron's continuity goal, roadmap acceleration, Adam's profitable-freedom interpretation and Robly buyer relationship. Guest philanthropy and acquisition criteria remain theirs. |
| 27:00–35:49 | Alonzo's early WhatsApp CRM, unqualified inbound meetings, discovery and messaging coaching. Three sales, below-5% closing and 15% no-shows have incomplete cohort definitions. Five discovery questions are mentioned but not spoken. |
| 35:49–46:40 | Current closed-comparable valuation reasoning, downside affordability, Moah's earlier near-sale, Cameron's plateau, cash/equity/compensation levers and a misused legal term corrected during drafting. No actual acquisition price or multiple is disclosed. |
| 46:40–55:26 | Early integration, strategic importance revealed to Cameron after closing, flexible role-setting, progress toward the 2025 revenue-increase goal, internal product use, Adam's changed banker preference and closing. Early satisfaction is not long-term acquisition proof. |
| 55:26–55:43 | Separate, context-poor promotional teaser about audience/product fit; its speaker is unidentified. It is not safely Moah's or Adam's final answer. |

## Important historical distinctions

**Financing and exit ownership.** In November, Moah explicitly reports **$400,000 total outside funding**, including an initial $100,000 check around 2010, before the business reached ramen profitability. Adam treats this as compatible with the bootstrapping label; neither source supports “never raised.” Her 2015-era Google overture is described as about one times ARR when revenue was around $3–4m, and she says they did not accept it. March's earlier near-sale is undated and unnamed; the two stories must not be silently identified as the same attempted transaction. The later acquisition involved cash/equity and retention/compensation components, but their amounts and financing arrangements are undisclosed. [November 03:01–05:03](https://www.youtube.com/watch?v=JaN_78GB638&t=181); [08:04–09:02](https://www.youtube.com/watch?v=JaN_78GB638&t=484); [14:20–15:39](https://www.youtube.com/watch?v=JaN_78GB638&t=860); [March 38:41–39:40](https://www.youtube.com/watch?v=7p-QD-3MtBw&t=2321)

**Adam's sale and chronology.** March supplies a $10m Robly sale, $1m banker payment and approximately $70k legal fees. Those amounts are historical self-reports, not net personal proceeds or the Boomerang purchase price. At 26:18–26:34 Adam says the buyer was a customer he met at Affiliate Summit around 2015, with the sale five years later. Approximately 2020 is an inference from two approximate statements, not a resolved sale date. Preserve newer 2026 testimony and the chronology uncertainty already tracked in [[identity/backstory]] and [[identity/proof]]. [March 00:28–01:17](https://www.youtube.com/watch?v=7p-QD-3MtBw&t=28); [26:18–26:34](https://www.youtube.com/watch?v=7p-QD-3MtBw&t=1578)

**Small teams and status pressure.** Adam connects unnecessary scale to social pressure around employee counts, recalls a dismissive reaction to GetEmails' six-person team, and says expansion took roughly two years to beat its earlier earnings. His nearby “10 or 12 million” scale shorthand does not restate the metric. Earlier he says the business was “making $8 million” while reducing the team by 40%; that passage alone does not specify the financial metric or period. These figures should not silently become a clean ARR/profit time series. Moah's separate milestone series—$2.2m ARR/eight people in 2014, roughly $8m/23 at the 2018 peak, $10m with a reduction to ten in 2019, then nineteen people at recording—belongs to Boomerang. [November 18:13–24:30](https://www.youtube.com/watch?v=JaN_78GB638&t=1093)

**Support and operating roles.** Moah describes three U.S. support staff and training everyone to cover customer support. Adam admires this and says he wishes he had that culture. His own account instead credits Robb's engineering/documentation background and Intercom AI plus workflows. The captioned “93 seat” apparently refers to CSAT, but the exact score format, denominator and period are not established here; it is not an AI-resolution rate. The “couple thousand interactions a week” estimate is also undefined and should not become a ticket total. This November baseline does not override later support metrics or the 2026 shared-team correction. [November 25:22–28:41](https://www.youtube.com/watch?v=JaN_78GB638&t=1522)

**Values versus guest achievements.** Boomerang's documentation, protected off-hours, school funding and climate grants are Moah's operating values and reported activities. November specifies roughly 10–12 schools, nine research projects over about seven years and a $50k grant model; none is Adam's philanthropy. Adam does explicitly say that a purpose of his founder audience is to tell stories showing that another path is possible. That is a dated statement of intent, not an approved permanent brand mission. [November 17:15–18:12](https://www.youtube.com/watch?v=JaN_78GB638&t=1035); [44:01–44:29](https://www.youtube.com/watch?v=JaN_78GB638&t=2641); [54:39–56:33](https://www.youtube.com/watch?v=JaN_78GB638&t=3279)

**Historical technology and policy claims.** Moah's Australian-law figures, deliverability practices and 11–12% email click rate are historical attributed statements, not current compliance advice or evidence of downstream conversion. The first two meetings were due later that day after roughly two-and-a-half to three weeks of work. Adam's November “late adopter” remark concerns his own recent LLM use; it does not negate his description of Robb's earlier AI implementation. His 2024 wish for a next-step button in RB2B is an unresolved product idea then, not a feature launch or his final 2026 product strategy. [November 31:14–36:28](https://www.youtube.com/watch?v=JaN_78GB638&t=1874); [45:46–48:06](https://www.youtube.com/watch?v=JaN_78GB638&t=2746)

## Structured-note fidelity

No substantive defect was identified in the fully read March note at the hash recorded above. In particular:

- `metrics_and_dates[0]` correctly assigns Robly's sale and fees to Adam, and the associated backstory and `tensions_and_corrections[0]` distinguish regret from fraud.
- `metrics_and_dates[1]` and `backstory_and_values[1]` explicitly label the inferred approximately-2020 sale date. They should remain qualified when linked into the wider history.
- `metrics_and_dates[5]` and `[14]` distinguish the December announcement from the host's approximate post-signing interval. The note does not manufacture an exact closing date.
- `metrics_and_dates[6]` and the seed-investor tension preserve the limit of “bootstrapped.” November supplies the stronger $400k financing baseline, but its absence from a March-only extraction is not an omission defect.
- `key_learnings[26]` and `metrics_and_dates[16]` correctly interpret the 30% figure as progress toward an undisclosed **revenue-increase target**, not 30% revenue growth.
- `key_learnings[29]` and the attribution section identify the separate closing teaser and its unknown speaker. They do not assign it to Moah or Adam.
- The note retains counsel, Quiet Light valuation advice, the undisclosed actual acquisition terms, the lawyers' correction of an incorrectly used term and Cameron's post-close discovery of the full strategic plan. It does not turn the case into proof that trust makes diligence unnecessary.

The March description's claim that the acquisition avoided legal headaches is promotional compression: the discussion explicitly includes legal work, negotiation and a corrected drafting misunderstanding. The November description's specific 2001 arrival and lack-of-English claims are metadata assertions, not facts explicitly established in the spoken transcript. No proposed metadata or raw correction is applied. November note fidelity remains unreviewed until that original extraction exists.

## Proposed enduring core additions — two only

1. **Robly's buyer relationship and fee regret — proposed for [[identity/backstory]], with metric handling in [[identity/proof]].** Adam's March 2025 account joins two parts of one sale: knowing the buyer as a customer for years, and regretting a $1m banker contract after already finding that buyer. The useful lesson is scrutinizing the role and cost of intermediaries against the actual deal circumstances. Preserve the historical self-report, unresolved date and guest case's retained professional advice; do not repeat the title's scam allegation as fact or turn Adam's preference into universal transaction advice. [00:28–01:43](https://www.youtube.com/watch?v=7p-QD-3MtBw&t=28); [26:18–26:59](https://www.youtube.com/watch?v=7p-QD-3MtBw&t=1578); [52:55–54:31](https://www.youtube.com/watch?v=7p-QD-3MtBw&t=3175)

2. **Build engineering management before expanding the team — proposed for [[identity/backstory]] and [[strategy/learnings]].** In November, Adam recalls moving to Argentina for Robly, struggling with the team and local employment arrangements, and finding better results after a local manager led it. For Retention.com, he describes hiring a Canadian engineering manager who worked alongside Tate for roughly four months before six engineers were hired. His stated lesson distinguishes exceptional individual contribution from managing a growing team. Dates remain unspecified; the employment dispute is his account, not verified legal history, and the example does not prove that location alone determined performance. [39:55–42:14](https://www.youtube.com/watch?v=JaN_78GB638&t=2395)

## Source Notes

Use [[strategy/youtube-library]] for original leaf-note coverage. This audit fully reviews both available raw transcripts but only one original structured note. It preserves the differences among human statements, title/description claims and editorial interpretation. Publicly accessible material is not automatic clearance for new first-person copy. No raw source, model note, provenance, correction registry, script, core page, index, log or running extraction process was modified.
