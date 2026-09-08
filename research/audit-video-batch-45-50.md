---
type: research
status: draft
owner: adam
created: 2026-09-08
updated: 2026-09-08
sources: [raw/sources/2026-09-08-youtube/videos/zjrqh1bOm94/zjrqh1bOm94.md, raw/sources/2026-09-08-youtube/videos/M9Pw3qJdNYE/M9Pw3qJdNYE.md, raw/sources/2026-09-08-youtube/videos/1f19uvtzNds/1f19uvtzNds.md, raw/sources/2026-09-08-youtube/videos/p5fyQaRE7ao/p5fyQaRE7ao.md, raw/sources/2026-09-08-youtube/videos/_ZK7wgkHuG4/_ZK7wgkHuG4.md, raw/sources/2026-09-08-youtube/videos/HIuvLo23R2M/HIuvLo23R2M.md]
tags: [audit, youtube, guest-attribution, conditions]
---

# Video batch 45–50 audit

## Scope and result

Read all six complete structured research notes: **29,000 words**. Independently checked the consequential raw-caption ranges listed below: **3,801 unique segments, 26,687 caption words**, spanning approximately 2h12m of the six videos. This is full-note review plus targeted raw review, not an independent second reading of every raw transcript line. Counts exclude duplicate examination of overlapping ranges. Source metadata fields were also inspected for dates and attribution context.

The checked passages support the notes' principal lessons and their qualifications. No material reversal of a checked operating lesson or speaker attribution was found. One metadata interpretation needs refinement: ranks 48–50 have distinct live-release and upload fields, rather than an unexplained single-date conflict. Titles overstate the spoken evidence in the Taylor and Emir sessions. Eric and Jason's sessions explicitly lack Adam. None of these guest outcomes establishes Adam's proof, personal values or writing voice.

Only this audit was created. Raw sources, extraction notes/JSON/provenance, the live runner, guest hub, core wiki, index and log were not edited. Proposed additions below remain for the parent to evaluate; more recent Adam-authored LinkedIn evidence takes precedence for current direction.

## Examined documents and fingerprints

Each input hash matches the full raw Markdown file and the research note's recorded `Input SHA-256`. The note hash fingerprints the complete **research/youtube-video-notes/ID.md** text actually read. Navigation links lead to the promoted durable note, whose wrapper can produce a different hash.

| Rank / durable note | Source date used by note | Raw Markdown SHA-256 | Research note SHA-256 |
| --- | --- | --- | --- |
| 45 · [[strategy/video-notes/zjrqh1bOm94|Taylor Haren: cold email]] | July 29, 2025 | `2cbf0da50d1eef8ae3343fb75be2eecb8555331078b3ec0ceef84ac106d7b6ce` | `99c42677e8b9eef051964fcb399b464642d0aae3e04fd2c6fd25a0e06827277d` |
| 46 · [[strategy/video-notes/M9Pw3qJdNYE|Anthony Pierri: positioning]] | July 20, 2025 | `3770ee82b269d67554930a57c9d1baaea794d395bab868d56af69dc63e8333d7` | `ac4dc467af41b4ec9800845f8beeffc641bca344fd8a90a6c1d151d76d2ae13d` |
| 47 · [[strategy/video-notes/1f19uvtzNds|Maor: Base44]] | July 20, 2025 | `0da4214383d7cefe506f1660603e73a174a437a9eec2402044a843c6e299e050` | `cd67f90b0cfe153f3f05a8483130718224779ac3333f98a0eaa948c7f8f532ce` |
| 48 · [[strategy/video-notes/p5fyQaRE7ao|Emir Atli: HockeyStack]] | June 24, 2025 live release | `77079899be839c65834db6765dea16460989138fca4039ba8150e0b48138eb49` | `ce698e1d2caf795d7c34e624167d6bdba22c748ad264598f8b211b3e0e4f5717` |
| 49 · [[strategy/video-notes/_ZK7wgkHuG4|Eric Siu: content and acquisition]] | June 17, 2025 live release | `0f04276ad41d429e812e3da6a47ac919ad7e9fafbe74e4c25bd8d13f5ad7f0ba` | `668cf8dfc1436d051d6a3c63519a9f23190304a1cd356b7671f70c0533613026` |
| 50 · [[strategy/video-notes/HIuvLo23R2M|Jason Bay: outbound offers]] | June 10, 2025 live release | `4b0079474bd77008f2c214b67d9c8dca9b54875697ac68cbc63a2f16db4094a7` | `f5e044de5354055ee0a3dd9f9fe015d84693d0396062363a218f78b3acbc0a15` |

Targeted examination used each source folder's timestamped `ID.transcript.json`. These are the fingerprints of those exact inspected files:

| ID | Transcript JSON SHA-256 |
| --- | --- |
| zjrqh1bOm94 | `8c47144c5ee9bbfb1d9ad693b7d641ec706fbf01fc95fdc24f1829423ed27287` |
| M9Pw3qJdNYE | `41d9712c15834f5adee4c731e228e2fb15cad9f9bd3fd31a4383735aff697c87` |
| 1f19uvtzNds | `434d23ef3d32541a10426de02c42a99dc8b814d0db22d66fb444aaefe42f599a` |
| p5fyQaRE7ao | `0d0e8ccb84fc945ea53aeed7f60a53a2ffd059a798ac91959a1047da17ab1414` |
| _ZK7wgkHuG4 | `f91ecc4b4730bdaa1540602a3640e7615f537a437127819bc25452933f49fe92` |
| HIuvLo23R2M | `b021bef7ef7ee9646ad4d51a14ff2fd32091337e1a5d97e1b383d7aea6192efe` |

## Date-field refinement

The three notes correctly select their explicit UTC live-release timestamps. Their language about an unresolved header/metadata conflict is unnecessarily broad: each archived `.info.json` has `was_live: true`, a `release_date` on the earlier day, and an `upload_date` on the following day. The raw Markdown headers use the latter. Preserve both field meanings; do not silently rewrite exact raw headers. These metadata distinctions do not independently verify when every spoken event occurred.

| Video metadata | `release_date` | `release_timestamp` | `upload_date` | `timestamp` | `was_live` |
| --- | --- | --- | --- | --- | --- |
| [Emir metadata](../raw/sources/2026-09-08-youtube/videos/p5fyQaRE7ao/p5fyQaRE7ao.info.json) | `20250624` | `1750791887` | `20250625` | `1750839346` | `true` |
| [Eric metadata](../raw/sources/2026-09-08-youtube/videos/_ZK7wgkHuG4/_ZK7wgkHuG4.info.json) | `20250617` | `1750186956` | `20250618` | `1750234018` | `true` |
| [Jason metadata](../raw/sources/2026-09-08-youtube/videos/HIuvLo23R2M/HIuvLo23R2M.info.json) | `20250610` | `1749582056` | `20250611` | `1749629138` | `true` |

Exact affected extraction fields in `research/youtube-video-notes/ID.json` (zero-based array indices), with the corresponding rendered text under **Tensions and corrections** or **Coverage**:

- **p5fyQaRE7ao · `$.tensions_and_corrections[1]`:** “The canonical metadata gives release time 2025-06-24T19:04:47+00:00, while the transcript header says Published: 20250625. Preserve the metadata timestamp and flag the header discrepancy; neither establishes the precise recording date.” The release timestamp is correct; clarify that the raw header reflects the separate upload date.
- **_ZK7wgkHuG4 · `$.tensions_and_corrections[1]`:** “Publication metadata conflicts: SOURCE_METADATA gives 2025-06-17T19:02:36+00:00, while the transcript header says 20250618. The output preserves the explicit UTC metadata; neither date establishes the recording date.” Also **`$.coverage.limitations[4]`:** “Recording date is unspecified, and publication dates conflict between metadata fields. Relative dates remain relative rather than being converted into exact event dates.” Replace the conflict characterization in a reviewed derivative with the distinct live-release/upload explanation; retain caution about relative event dates.
- **HIuvLo23R2M · `$.tensions_and_corrections[1]`:** “Publication metadata specifies 2025-06-10T19:00:56+00:00, while the transcript header says Published: 20250611. The metadata timestamp is preserved; the discrepancy is unresolved and neither establishes the recording date.” The field distinction resolves why the displayed dates differ; it does not independently date every narrated event.

The three **`$.published`** values are respectively `2025-06-24T19:04:47+00:00`, `2025-06-17T19:02:36+00:00`, and `2025-06-10T19:00:56+00:00`. They match `release_timestamp` and need no numerical correction. Proposed derivative wording: “The archived metadata records a live release on [release date] and a later upload date of [upload date]. The note uses the live-release timestamp; the exact raw header preserves the upload field. Relative events remain tied to the conversation rather than inferred solely from either date.” Original model JSON and provenance remain unchanged.

## 45 · Taylor Haren — July 29, 2025

**Raw examined:** 10:00–14:55; 23:00–26:50; 27:27–30:10; 39:20–39:53; 44:10–46:30; 48:55–54:00. [Raw source][T]

- **Useful diagnostic sequence:** preserve a restart baseline, isolate a major change before raising volume, and inspect response collection before interpreting a rate drop. Taylor reverified the old list, held volume while testing copy, and attributed that day's lower displayed replies to disconnected inboxes. This supports checking instrumentation, copy and delivery as separate possible failures; his proposed bounce-log classifier was not yet shipped. 10:03–13:29, 27:27–30:08, 39:26–39:52.
- **Offer and sequence advice has an operating boundary.** His default of one strong email every one or two months serves a high-volume agency model. He still tests a second step for every new client and retains a cybersecurity exception whose analytical buyers respond better to email two. Do not extract a universal ban on follow-ups. 49:11–53:57.
- **Consequential evidence limits:** Taylor explicitly calls the AI-filter explanation an unproven theory at 13:42–14:25. Warm-up as complaint-pool dilution is likewise his theory, with secondhand evidence, a Gmail/Outlook distinction and shifting denominators; it is not a verified provider rule or safe-volume formula. 23:29–26:46.
- **Metric repair already handled correctly by the note:** Taylor corrects 8.5m monthly sends from RB2B to Fixer. Historical one-per-nine is a signup per sent email in an RB2B-triggered audience, while the current 38:1 ratio lacks an equally explicit outcome definition. Adam himself qualifies the relevance advantage of marketing RB2B to people already interested in RB2B. Do not compare these as a clean conversion decline or combine the early 21.5% positive figure with later send-to-positive rates. 13:30–13:41, 44:43–46:22.

## 46 · Anthony Pierri — July 20, 2025

**Raw examined:** 02:57–03:58; 16:33–21:20; 28:50–31:05; 31:25–35:30; 42:00–50:10. [Raw source][A]

- **Audience familiarity is part of positioning.** Anthony qualifies Adam's assumption that buyers already understand identification: it describes the LinkedIn audience he currently reaches. Adam accepts this correction. A primary message can connect to an activity the buyer already performs or is considering; Anthony explicitly allows earlier-funnel education about a new activity. This is more precise than a blanket prohibition on educating buyers. 31:30–35:30.
- **Distribution changes the strategic choice.** Adam prefers a narrow, easy, inexpensive workflow but weighs his strong B2B SaaS distribution against technically demanding competition. Anthony explains that opening an unfamiliar market requires a different operating path, not merely a different homepage headline. His objection to A/B testing concerns two multiyear business trajectories, not ordinary message experiments. No expansion decision is reached. 42:51–47:58.
- **Activation curiosity does not settle ongoing value.** Anthony's Fletch trial proved identification but churned because it did no outbound. He hypothesizes that such users can spread awareness; Adam still describes poor-fit adoption as a serious churn problem and admits he has not determined what the best RB2B users do. These statements cannot establish that churn is good or that most customers have no ROI. 16:46–21:10.
- **Historical direction, not current specification:** Adam's automated filtering/messages/outreach workflow is explicitly partly unbuilt. Current 2026 LinkedIn reversals of the broader outreach product must take precedence. The 70-versus-three team comparison does not establish FTEs or total labor; the malformed later price and historical plateau amount remain unresolved. His clarity-versus-lawyer anecdote is a historical choice, not legal guidance. 02:55–03:57, 29:16–31:01, 46:32–49:05.

## 47 · Maor / Base44 — July 20, 2025

**Raw examined:** 15:15–20:00; 22:55–25:05; 26:20–28:58; 39:55–47:38; 49:55–53:20; 54:05–57:00. [Raw source][B]

- **Recruit for real use, then observe the work.** Maor's first three, then ten users were acquaintances with actual reasons to use the unfinished product. He watched them, repaired failures and released again. For a narrow professional product he says he would need users from that profession. Ten becoming eleven over a month is his retention/referral heuristic, not an achieved viral coefficient. 15:40–19:56.
- **Faster activation had an explicit cost.** Removing the diagram-approval step shortened the path to a generated app, while accepting that initial output might mismatch intent and require later adjustment. Curated, improved app/code examples were injected into prompts; this was not evidence of training a proprietary foundation model. A narrated database-connected demo does not prove comprehensive production readiness. 23:02–25:03, 26:20–28:58.
- **Distinctive sharing iteration:** Maor first asked users to show their app and praise Base44. He reports a stronger approach after removing the praise requirement and helping users showcase what they accomplished. Building credits still incentivized that sharing. His later “share with three” claim does not mean three acquired or paying users. 43:03–44:59, 50:24–51:08.
- **Adam's directly stated content condition:** building in public fits when founder experience overlaps the intended buyer's interests; select the platform accordingly. He also distinguishes the compounding archive and improved craft from beginners matching his existing reach. Maor separately qualifies the same distribution fit for profession-specific buyers. This is a sharper audience condition, not an endorsement for every startup. 45:01–47:16.
- **Deal and team limits:** Maor describes approximately six people by acquisition, profit preceding expansion, and additional performance-based payments beyond the publicized initial consideration. No evidence establishes $80m personal net proceeds, a permanently solo team, or maximum deal value. Simple subscription visibility eased his diligence; Stripe access alone is not a complete diligence procedure. 51:34–53:20, 54:12–56:55. His report that Adam's content influenced him remains qualitative; it does not establish that Adam caused the exit.

## 48 · Emir Atli — June 24, 2025 live release

**Raw examined:** 02:55–05:02; 13:10–19:20; 21:25–25:30; 40:10–45:45; 45:55–53:50. [Raw source][E]

- **Validate the conversation before scaling it.** HockeyStack first followed up with interactive-demo users, then tested cold-call scripts while building infrastructure. One operator manually booked meetings before hiring and dialer expansion. Its shared multi-provider database was expressly for a company planning scale, not a required small-team starting stack. Daily human role-play and rep explanations of two good/two poor calls make the feedback loop concrete. 15:57–18:23, 24:31–25:15.
- **Diversification addressed volatility, not an inbound collapse.** Emir started outbound while inbound remained strong and continued fluctuating afterward. This is a condition-specific comparison with Eric's warning against scattering effort before a channel is developed; the two sources do not supply a universal diversification timetable. 13:38–15:57.
- **Adjacent markets need operational similarity and product authority.** Unexpected service-company inbound revealed familiar CRM, marketing and sales practices. Emir used those requirements to generate candidate industries, pursued one or two at a time, and allowed product changes. Adam's accountants/recruiting/staffing suggestions remain questions; similarity and AI-generated candidates do not validate willingness to pay. 40:15–45:45.
- **The attribution title reverses the useful nuance.** Emir defends incomplete, directional evidence for complex channel decisions. Adam asks what actually supplies evidence of a podcast exposure; the concrete answer relies on self-reporting and call transcripts, while webinar attendance can use a list. Neither establishes universal exposure tracking or causal attribution. The claimed 90% podcast self-report likelihood is unsupported. 46:11–53:42.
- **Historical Adam evidence is scoped correctly:** daily review with Rob of the early AI sales assistant is an experiment, not measured conversion impact. Alec Paul's quoted $12k/month service price and 20k-to-135k subscriber history do not independently establish Adam's expense or a causal return. HockeyStack's $74m is pipeline, not Adam's revenue or HockeyStack ARR. 03:00–04:56, 13:10–13:24.

## 49 · Eric Siu / Pete — June 17, 2025 live release

**Raw examined:** 00:38–01:05; 20:20–22:20; 26:30–32:10; 35:50–38:45; 46:30–48:10; 51:38–57:25. [Raw source][S]

- **Adam is absent**, explicitly stated in the opening. Eric's SEO and publishing rules are guest advice; Pete's company observations are host reports. Neither establishes a change to Adam's voice or personal strategy. 00:49–00:53.
- **The durable content workflow is conditional:** identify relevant high-intent questions, infer existing writing guidelines, inspect initial samples, edit, then expand useful production. The reported 21 drafts in 30 minutes excludes editing time and supplies no search or revenue result. Eric's later rejection of word-count obsession materially qualifies the earlier recommendation to increase Boon's output. 20:20–22:20, 28:46–29:46, 52:44–53:29.
- **A free product feature can serve acquisition.** Eric proposes giving away a distinctive useful feature while retaining other paid functionality. He explicitly warns that generic calculators are becoming easy to copy. This is a proposed Boon intervention, not measured link acquisition or conversion. 26:35–27:44, 29:49–30:44.
- **Channel and content quality boundaries:** start where buyers are, develop one channel, and consider repurposing from a shared long-form source; do not copy an experienced operator's entire stack at once. His demonstrated-channel focus coexists with search-concentration risk. Original data, useful tools and deeper analysis qualify volume advice; claimed algorithms, tool quality and ranking factors remain dated practitioner assertions. 36:00–38:38, 46:38–48:10, 54:44–57:03.

## 50 · Jason Bay / Pete — June 10, 2025 live release

**Raw examined:** 00:25–00:55; 11:40–17:40; 30:00–33:10; 34:30–37:00; 41:10–45:08; 45:50–48:05; 51:10–57:28. [Raw source][J]

- **Adam is absent**, with Pete identifying himself and explaining Adam is traveling. The account executive called Adam in Jason's welding example is a sample-pitch person, not Adam Robinson. 00:33–00:47, 12:45–13:59.
- **Useful value can precede a buying decision.** Jason distinguishes expertise access, reusable benchmarks and custom audits, evaluating value against the prospect's required effort. A tailored audit is more resource-intensive; Pete associates it with priority accounts. The conversation still seeks time, but promises a useful result even without a purchase. This is more accurate than “never ask for a meeting.” 11:56–17:23.
- **Diagnose authority and business outcomes without assuming every first contact is the executive.** Jason's Get Responding diagnosis is provisional; Lewis had already changed discovery/outbound and the website lagged. Jason later recommends examining first contacts in won deals: a director may be the enterprise entry point, while a small-business owner may be reachable directly. User convenience and executive priorities can require different messages. The £55,000/£4,200 annual-price caption discrepancy prevents a firm sales-motion classification. 30:07–33:10, 34:36–36:23, 45:54–47:49.
- **Coordinate channels, then test the total result.** Jason's three-week starting cadence is six calls, six emails and three social touches—not an equal split. Voicemail points to the email subject and is evaluated partly through replies. He later allows that some audiences may not need phone; enterprise parallel dialing requires research available at connection. All reported study lifts remain unverified comparisons, not conversion guarantees. 41:11–43:29, 51:52–53:42.
- **Medium should add meaning.** Jason now favors video when it can show the actual checkout/audit issue, while qualifying the declining novelty of generic introductions and his own poor voice-note results. His disclosed dialer sponsorship matters when reading recommendations. Pete's “virtually everything” manually written claim is third-party and qualified, and Jason's synthetic-content concern coexists with willingness to test AI tools; neither supplies Adam's permanent AI policy. 51:13–51:48, 53:44–57:26.

## Compact proposed core additions

Compared with the current learning map, ideal follower, building-in-public/GTM/SaaS pillars and guest hub. These are the few additions with a distinct condition or mechanism; they are proposals, not filed or approved context.

1. **Ideal follower / building in public:** Add Adam's explicit condition that founder storytelling needs overlap with buyer interests, plus his willingness to correct the assumption that current LinkedIn visitors represent the broader market. The existing audience page distinguishes followers from buyers but does not yet capture this direct historical qualification. [July 20 Base44, 45:01–47:16][B]; [July 20 Anthony, 32:42–34:37][A].
2. **GTM / creator participation:** Add Maor's attributed comparison: reward users for showing their own useful result, and test whether requiring platform praise suppresses participation. Keep the credits incentive visible and avoid implying measured causal uplift. This gives a specific iteration behind the existing broader “give creators a reason to succeed” principle. [July 20 Base44, 50:24–51:08][B].
3. **SaaS building / activation:** Add Base44's explicit tradeoff between an earlier functioning first result and an approval step that better specifies intent. Present it as Maor's case, requiring later correction of mismatched outputs; do not turn it into a general instruction to remove approvals. [July 20 Base44, 23:02–25:03][B].

The other lessons belong in their existing durable video notes or eventual guest synthesis. They reinforce already-filed offer quality, PMF before scaling, measurement separation, small-team qualifications and human review. This batch does not require new Adam proof numbers, a new taxonomy, or another personal-value declaration.

## Related Pages

- [[strategy/youtube-library]]
- [[strategy/learnings]]
- [[strategy/guest-playbooks]]
- [[audience/ideal-follower]]
- [[identity/source-conflicts]]
- [[strategy/source-policy]]

## Source Notes

Automatic captions are undiarized; context supports the attributions above but no audio or screen inspection was performed. Source claims, hypothetical advice, dated provider practices, title promises, commercial pitches and measured results remain distinct. This audit checks local evidence rather than current technical guidance or independent financial facts. New public copy remains unapproved. The already-resolved D-8umeDdYP0 opening review is outside this batch and was not repeated.

[T]: ../raw/sources/2026-09-08-youtube/videos/zjrqh1bOm94/zjrqh1bOm94.md
[A]: ../raw/sources/2026-09-08-youtube/videos/M9Pw3qJdNYE/M9Pw3qJdNYE.md
[B]: ../raw/sources/2026-09-08-youtube/videos/1f19uvtzNds/1f19uvtzNds.md
[E]: ../raw/sources/2026-09-08-youtube/videos/p5fyQaRE7ao/p5fyQaRE7ao.md
[S]: ../raw/sources/2026-09-08-youtube/videos/_ZK7wgkHuG4/_ZK7wgkHuG4.md
[J]: ../raw/sources/2026-09-08-youtube/videos/HIuvLo23R2M/HIuvLo23R2M.md
