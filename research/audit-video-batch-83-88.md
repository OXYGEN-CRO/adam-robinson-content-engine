---
type: research
status: draft
owner: adam
created: 2026-09-08
updated: 2026-09-08
sources: [raw/sources/2026-09-08-youtube/selected-100.json, research/youtube-note-corrections.json, research/audit-aye-moah-history.md]
tags: [audit, youtube, attribution, metrics, source-fidelity]
---

# Video-note fidelity audit: selected ranks 83–88

## Finding and scope

**All six original structured notes were read completely. Three claim-type defects were found and the parent applied all three to reviewed derivatives.** Their original claims and caveats already distinguish Diana's achievements from Adam's; the incorrect `adam_self_report` classifications were changed to `host_statement`. No other substantive defect was established in the consequential passages checked. One exact speaker transition in the Aye Moah episode remains uncertain from text alone and is recorded below, rather than converted into a confident correction.

This is a full read of six structured extractions, with targeted raw-passage verification for ranks 83–86 and 88. Rank 87's entire raw transcript was read earlier, as documented in [[research/audit-aye-moah-history]], and its now-available original note was read in full here. The first rank-83 print truncated a few tokens in `backstory_and_values[1]`; the complete object was separately reread. No original note was treated as fully read on the strength of its title, summary or a keyword search.

The six sources contain **62,020 caption words**. This audit does not claim a fresh full raw read of all those words, does not independently verify business outcomes, and does not establish that the complete 100-video extraction has finished. [[strategy/youtube-library]] and the separate automatic synthesis audit carry overall completion. Automatic captions lack diarization. No audio, video, private analytics, contract or financial statement was inspected. The supplied publication timestamps do not establish exact recording or event dates.

## Identity, extent and provenance

All six metadata records identify channel `UCSHn0Px37BjzMqnZBmVWwcQ`. Claim counts are key learnings / backstory and values / metrics and dates. Caption bounds below are first start / last start / maximum cue end in seconds; small cue overruns beyond listed video duration are retained rather than rounded into new speech. Each note's last reviewed anchor matches the floored last caption start.

| Rank / ID | Captured title | Selected public release UTC | Words / segments | Claim counts | Caption bounds, seconds |
| --- | --- | --- | --- | --- | --- |
| 83 — `Y3xKljQlMzA` | Signal Stacking for Startups - How you can create a $100m ARR signal stack with a $1m ARR budget | 2024-12-18T15:00:06+00:00 | 10,242 / 1,736 | 30/9/19 | 0.000/3435.480/3438.120 |
| 84 — `TBgRHplsJhY` | How to engage anonymous site visitors. - with Florian Tatulia | 2024-12-11T15:00:21+00:00 | 9,200 / 1,287 | 31/6/16 | 0.240/3067.680/3072.880 |
| 85 — `xwidBsviGII` | Spray and pray outbound doesn't work anymore ... What now? - With Diana Ross | 2024-12-04T19:41:32+00:00 | 10,026 / 1,618 | 32/9/25 | 0.000/3475.520/3478.000 |
| 86 — `fg4kNYt38FM` | SEO for B2B with Eric Siu | 2024-11-20T17:53:05+00:00 | 11,183 / 1,499 | 33/9/29 | 0.040/3242.640/3248.760 |
| 87 — `JaN_78GB638` | Boomerang  Bootstrapper Aye Moah | 2024-11-13T15:00:05+00:00 | 9,438 / 1,316 | 33/12/31 | 0.520/3426.559/3431.720 |
| 88 — `H4LpPMR6v1E` | Founder Brand Creation with Dave Gerhardt | 2024-11-06T15:00:06+00:00 | 11,931 / 1,689 | 30/10/32 | 0.800/3362.319/3365.200 |

File naming is exact: source Markdown is `raw/sources/2026-09-08-youtube/videos/{id}/{id}.md`; normalized captions use `{id}.transcript.json` in that same directory. Original notes and provenance are `research/youtube-video-notes/{id}.json` and `{id}.provenance.json`. SHA-256 values are hashes of complete file bytes, not a canonicalized JSON representation.

| Artifact | SHA-256 |
| --- | --- |
| `Y3xKljQlMzA` — Source Markdown | `b19b4abb4678dd07f09ba50cc6e7bafc5e2b4d49607cc38be28d72603e6f4ac3` |
| `Y3xKljQlMzA` — Normalized captions | `7e10a6a883af0483dbab0e884a543af686144250e8f7a56606cc794982a06c0a` |
| `Y3xKljQlMzA` — Original note | `b5bf829011d0f432c247fcd18862fefeef1fe0373fa815f0f2485ad6116aa802` |
| `Y3xKljQlMzA` — Original provenance | `696201cdff100ed3eba72345695b2838b2ca51153615e4b9dfd845aa85c40d95` |
| `TBgRHplsJhY` — Source Markdown | `6f0f8d9230404f72b2c1d6ca67f3097755b2cc3782ae7dd123f4368f3edf520d` |
| `TBgRHplsJhY` — Normalized captions | `bc70e4661d13e60c0e994101624269f0a5c7fedbfca57d88b3afdaad3f289a7a` |
| `TBgRHplsJhY` — Original note | `43545db22fd86ee760b64e15bcae1cb79bdd9687393f83ce12eba11e1bea3271` |
| `TBgRHplsJhY` — Original provenance | `6b05c7b011187704adf1e4569d062ebefe8691c80350cab1ea6bf811f423848c` |
| `xwidBsviGII` — Source Markdown | `c9874ed6247b05f545615555e3d29573c88ad39c14c25bf8a311b079629725ad` |
| `xwidBsviGII` — Normalized captions | `9cf80e7d7859da37401bfe5cb42be0684058ff295a1a6f622164c3b6099d4bb0` |
| `xwidBsviGII` — Original note | `747241822c68a7b7c88ec80babc6be14e0822c73ed7b7a8965dadf2fa3434b77` |
| `xwidBsviGII` — Original provenance | `7f05074b7c6264d6d55522b68b8248db22e218c4cc352110d67ae8d46c71a4eb` |
| `fg4kNYt38FM` — Source Markdown | `816948522f41f848ddbbc5dd1043173b1c5aaf1b231c3db89d6444b83703cee7` |
| `fg4kNYt38FM` — Normalized captions | `6cf176bdde9c459e9d3171900789b32a5288da59bb33197791dd421aa361e35f` |
| `fg4kNYt38FM` — Original note | `697715a5f8aab3972b169b17deab9b068d4228ce2b768e8df0cc2eb31fc79610` |
| `fg4kNYt38FM` — Original provenance | `91b8a2dda7855e25b146d9334dfcc4f504b49db34cc0e1663e1ce536687e80f6` |
| `JaN_78GB638` — Source Markdown | `f190c591fa1a306b1918ff940f673a0490056a88579e1da55109392a90e4778c` |
| `JaN_78GB638` — Normalized captions | `9011a6246cd0b1b81f275577e9424fba201868e20cd303904c129c00fd3ce49d` |
| `JaN_78GB638` — Original note | `912ba422ce095c61eed1b51b66d371fd73e0725cefed4e5ed6eec14dd186db77` |
| `JaN_78GB638` — Original provenance | `ce41385429c3170e298ec5b18e9b6fcd9e16fed87bde926e1f9750e19344fe56` |
| `H4LpPMR6v1E` — Source Markdown | `408a880c08b48abdb54b8e793056c717a53fc86874662d8836ab03a7349298db` |
| `H4LpPMR6v1E` — Normalized captions | `e4e578618cda14c706e23777e52f3f807590bed5591586713db6b181729ab035` |
| `H4LpPMR6v1E` — Original note | `d29011877bbf9d16b315c979cb8e87bcfafb4b7b45017fc876b0dc5454b34f85` |
| `H4LpPMR6v1E` — Original provenance | `12a647c9c611708898845747393e1bd457711204215fc563332752da71145d12` |

At **2026-09-08T10:19:36.379817+00:00**, all six provenance records had the exact source path and Markdown byte hash shown above, `exit_code: 0`, and retained event streams ending in `turn.completed`. Parsing each final terminal `agent_message` as JSON yielded exact object equality with its original note. Those checks establish source/output linkage and successful terminal completion; they do not prove semantic truth or independent human reading. Prompt reconstruction and whole-library structural validation remain the responsibility of the separate independent verifier.

## Directly examined raw passages

Intervals specify the caption-start windows inspected in this audit, including surrounding context. End boundaries are exclusive when used by the reading script. The prior complete rank-87 read covers every normalized segment and its final closing remarks.

| ID | Examined ranges | Why these passages mattered |
| --- | --- | --- |
| `Y3xKljQlMzA` | 02:28–02:55; 09:31–14:26; 16:47–19:20; 22:57–23:12; 26:55–27:25; 29:39–29:50; 55:11–55:36 | Revised 2025 positioning; ICP/TAM teaching mistake; still-hypothetical CRM workflow; early free/paid mismatch; discovery versus scaling; Mixmax deal/date claims; financing scope. |
| `TBgRHplsJhY` | 01:05–01:26; 12:46–13:24; 21:40–23:03; 39:40–42:35; 47:30–48:33 | Pete's identity and Adam's absence; guest reply/meeting rates; timing suggestion versus implemented process; identification denominators and explicit request not to publish an analytics anecdote; digital-footprint qualification. |
| `xwidBsviGII` | 00:00–01:15; 05:52–06:05; 20:21–21:12; 22:46–23:01; 27:29–28:07; 30:45–32:08; 35:36–35:55; 46:15–48:40; 55:24–56:10 | Relationship chronology, narrowed Diana achievement, manual sales operations, Diana's post engagement, PLG expectation change, stage-specific sales hiring, separate Retention.com/RB2B ARR shorthand, changing publisher ICP, untested turnaround expectation. |
| `fg4kNYt38FM` | 05:11–06:10; 24:00–25:24; 27:23–27:50; 37:29–37:50; 48:49–49:44; 53:21–53:44 | Adam's lack of SEO practice versus Eric's expertise; Diana's differing milestone descriptions; nine-month discovery lapse; early CPC/engagement results with conversions pending; PMF and runway conditions; future staffing. The relevant first Diana claim begins 24:32, after the initial 24:00 reading window. |
| `JaN_78GB638` | Prior full read: all 1,316 segments, 00:00.520 through last start 57:06.559 / maximum end 57:11.720. Additional reread 19:47–21:07. | Complete Adam/Moah/host separation, seed financing, staffing and earnings shorthand, support responsibilities, unclosed outbound meetings, engineering-management history, guest philanthropy and Adam's stated desire to tell alternative founder stories; uncertain small-team speaker transition. |
| `H4LpPMR6v1E` | 00:00–05:26; 13:09–14:56; 22:24–24:54; 26:53–27:21; 30:12–31:51; 34:58–37:46; 44:47–48:27; 49:15–49:39; 53:17–56:04 | Offer/price revisions, publication versus historical start period, founder dependence, sales-cycle limits, writing help and BDR history, differentiation/pillars, guest versus Adam acquisition spending, content research, impressions versus followers, guest membership and event audience. |

## Confirmed defects and applied status

The parent directly reread the corresponding source windows and added these three corrections to `research/youtube-note-corrections.json` at approximately 10:13:49 UTC on September 8, 2026. The registry was independently inspected here: all three original note hashes and normalized-caption hashes match the files above, each recorded original object equals its exact original field, and each replacement differs only in `claim_type`. All three promoted claim lines were also directly inspected and display `host_statement`. Original model outputs and provenance still match their terminal outputs. The parent reported rebuilding 88 promoted notes and obtaining 88 structurally valid notes; this scoped audit did not rerun the whole-library verifier.

| Original field | Defect and evidence | Applied derivative |
| --- | --- | --- |
| `fg4kNYt38FM.metrics_and_dates[12]` | Adam reports **Diana's** two sales journeys. At 24:32–24:46 he says $1m to $10m as the only rep twice; at 53:21–53:39 he uses $0 to $10m ARR. The original caveat correctly says this is a colleague's achievement and preserves differing starting amounts. [24:32](https://www.youtube.com/watch?v=fg4kNYt38FM&t=1472); [53:21](https://www.youtube.com/watch?v=fg4kNYt38FM&t=3201). | `adam_self_report` → `host_statement`; speaker remains Adam Robinson. Claim, caveat, pillar and 24:32–53:39 anchors retained. |
| `xwidBsviGII.metrics_and_dates[3]` | Adam initially credits Diana with two zero-to-$10m journeys, then immediately narrows this to two $1m-to-$10m journeys; Diana agrees. They span incompletely specified businesses and do not make Adam the sole subject of both results. ARR is not explicitly restated in this passage. [05:52–06:03](https://www.youtube.com/watch?v=xwidBsviGII&t=352). | `adam_self_report` → `host_statement`; speaker remains Adam Robinson. Claim, caveat, pillar and 05:52–06:03 anchors retained. |
| `xwidBsviGII.metrics_and_dates[8]` | Adam estimates about 2,500 likes and hundreds of requests on **Diana's** sales-sheet post, addressing her directly. The original caveat already rules out treating these as Adam's own engagement. [22:46–23:01](https://www.youtube.com/watch?v=xwidBsviGII&t=1366). | `adam_self_report` → `host_statement`; speaker remains Adam Robinson. Claim, caveat, pillar and 22:46–23:01 anchors retained. |

No associated summary or tension field was found to transfer Diana's results to Adam; no broader prose correction was proposed for those fields. The original classification defects remain inspectable in the raw model JSON. This review did not rewrite them.

## Important qualifications retained by the notes

**83 — Signal stacking.** The title's $100m ARR stack on a $1m ARR budget is a framing promise, not demonstrated economics. Adam calls the proposed TAM/CRM/account-owner flow a hypothesis. His early RB2B example separates roughly 3,000 free signups and 13 paying customers around eight weeks from his proposed $495/month CRM-integration price; the integration was not yet built. Those numbers must not be multiplied into ARR. His caution against scaling marketing before clear demand is qualified by his later allowance that free users can help discover the ICP. Heath's first holiday-campaign deal and the separate $100k Mixmax deal are guest reports, without independently measured incremental causality. A reference to recording-day 17 and a Friday-13 campaign launch precedes the December-18 publication; publication is not the deal's measurement date. Mixmax's earlier Series B does not support “bootstrapped from inception.”

**84 — Pete and Florian, not an Adam interview.** Pete explicitly hosts while Adam and Santos are at an offsite. The note appropriately contains no Adam self-report or opinion claim. Common Room's reported reply rates, trial-booking rates and growth belong to Florian's case; different channel populations and undefined denominators prevent clean ROI comparisons. Pete's suggestion that the documentation should be updated after hearing a faster follow-up practice is a reconsideration, not proof the workflow changed. His comparison involving 20,000 apparent U.S. visitors, 17 identifications and another analytics view near 90 is unresolved, and he expressly asks not to post it. The note preserves that public-use boundary; the example is not an approved customer story or a diagnosis of a vendor.

**85 — Diana and changing conditions.** Her prior manual outbound and Retention.com sales process do not demonstrate the new RB2B playbook: the conversation describes her first official RB2B day as the prior day and anticipates testing for four to six weeks. Past main-domain/manual email tactics remain historical. The founder's first-sales-hire lesson distinguishes inventing a sales process from executing an established one. The roughly $20m-plus Retention.com and $4m RB2B ARR references stay separate. The publisher agreement is described as $50,000 per month for two years, not collected cash, recognized revenue, or proof all publishers became a good ICP. The closing prediction that RB2B will become unstuck in weeks or months is not an achieved turnaround.

**86 — Eric's channel and AI advice, Adam's operating admissions.** Eric's search-everywhere perspective, content production practices, AI-agent forecasts and agency examples remain guest statements. He discloses his Skool investment. Advice to establish a working channel/PMF before a 12–24-month SEO investment is stage-conditional; later diversification does not erase that boundary. Adam's own lack of SEO practice is not evidence his companies received zero organic traffic. Eric's roughly 50% CPC reduction and doubled engagement were early results with conversions still pending, not revenue improvement. Adam's admission of roughly nine months without customer discovery is retrospective self-explanation of a plateau, not a causal experiment. His November discussion of Diana joining RB2B is a plan at that moment; December's episode supplies a later status.

**87 — November Moah note now available.** The earlier full-source audit explicitly left this note unreviewed because it had not arrived. This audit closes that narrower gap by reading the complete original November extraction. It correctly keeps Moah's $400,000 total seed financing, initial $100,000 check, roughly 18-month ramen-profitability period and rejected Google overture separate from Adam's history. “Bootstrapped” does not become “never raised.” Boomerang's milestones, nineteen-person team and charitable projects stay attributed to Moah; her hypothetical $20m-revenue/30-person company is not a reported result. Adam's “making $8m” and “10 or 12 million” do not receive an invented financial metric or period. Moah's support-trained company is something Adam admires and wishes for, not his existing policy. His captioned “93 seat” is not converted into a 93% AI-resolution rate, and a couple thousand interactions per week is not silently a precisely defined ticket denominator. Her early outbound meetings were scheduled, not attended or closed; legal/deliverability assertions are historical guest claims, not current guidance. His Argentina/Canada management history is kept separate from Moah's remote-team case. The March upload is a later, distinct conversation, as already established in [[research/audit-aye-moah-history]].

One local attribution limit remains: `JaN_78GB638.key_learnings[9]` assigns the “smallest team appropriate to the phase” principle to Adam and the fulfillment/efficiency rationale to Moah. At 19:47–20:38 the automatic text flows from Adam's own restructuring example into both rationales without an explicit speaker marker. The next clear direct-address turn says “the hard part, Adam” at approximately 20:42. The note's division is plausible, but the exact turn cannot be verified from this text alone. **No confirmed correction is proposed.** Keep the joint, interpretive nature and contextual-attribution limitation; do not use this narrow transition to assert either an exclusive Moah rationale or that every sentence was Adam's. No audio check was performed. [19:47–21:07](https://www.youtube.com/watch?v=JaN_78GB638&t=1187).

**88 — Dave Gerhardt.** Drift/Privy/Exit 5 history and current-at-recording 170,000 followers / 5,000 members belong to Dave. The note does not multiply members by his $300/year offer or interpret impressions as unique audience reach. Adam's prediction of 75% founders is distinguished from the reported live poll's 58%; the poll's categories total 96% and lack a denominator. The RB2B community offer revises one-time to annual and contains inconsistent captioned figures ($29.97, 297 monthly, roughly $3,000/year, an included plan captioned 3.49). The note does not reconstruct a precise price. Adam's $12,000/month outside LinkedIn help excludes writing; Kyle's additional captioned “50” has no safe scale/period. Dave's $10k/month Drift program and $10k video are different guest examples, not Adam's spending or proven ROI. Adam explicitly accepts founder dependence while not contemplating a sale; Dave proposes several visible company experts as a possible mitigation. Dave limits immediate webinar selling by product price and sales-cycle length. Adam's Shopify-content difficulty is not a claim the audience is unreachable: Dave challenges the approach and Adam allows that more iteration might have worked. The education/community bundle and founder-brand moat are experiments/opinions, not validated results.

## Two concise core additions — applied by parent

The parent applied both proposals to [[strategy/learnings]] after directly reading 09:20–14:35 of the signal-stacking source and 46:00–48:50 of the Diana source. This task did not edit a core page. The account-fit addition retains the CRM hypothesis caveat, and the publisher addition omits the contract number from the compact core. Current [[strategy/learnings]], [[identity/backstory]], [[identity/proof]], [[identity/source-conflicts]], [[strategy/financing-decisions]] and [[strategy/guest-playbooks]] were checked for relevant existing coverage. The customer-discovery lapse, content-pillar development, engineering-manager story and public layoffs narrative are already represented and are not proposed again. Latest 2026 direction retains precedence over these 2024 operating snapshots. The submitted wording and boundaries follow for auditability.

1. **Qualify the account before acting on the signal.** Proposed short addition to the go-to-market learning map: “In December 2024 Adam called failing to teach TAM qualification a mistake in RB2B's early customer education. He proposed mapping named accounts and owners before triggering outreach; that workflow was still a hypothesis. The durable principle is to establish who should buy before treating identified activity as a reason to contact them.” Adam supplies the admitted mistake and proposed workflow; Heath's separate guest examples illustrate why relevant buying signals differ by company. Do not promote historical HubSpot/Salesforce details into current tool recommendations. [[raw/sources/2026-09-08-youtube/videos/Y3xKljQlMzA/Y3xKljQlMzA|09:31–12:30]]; [09:31](https://www.youtube.com/watch?v=Y3xKljQlMzA&t=571).

2. **Revisit an old segment when its buying conditions change.** Proposed short addition beside changing GTM tactics: “Adam's December 2024 publisher example shows that an unattractive segment can become viable after the offer and company credibility change. Diana adds that the buyers' urgency had changed. Treat an ICP as a dated hypothesis, while testing actual demand rather than assuming past rejection is permanent.” Adam supplies the prior slow-payment/long-cycle problem, later signed publisher agreement and brand-credibility comparison; Diana supplies the market-pain interpretation. The contract amount stays a historical self-report in the leaf note unless separately needed in [[identity/proof]]; it is not required to express the lesson. [[raw/sources/2026-09-08-youtube/videos/xwidBsviGII/xwidBsviGII|46:15–48:40]]; [46:15](https://www.youtube.com/watch?v=xwidBsviGII&t=2775).

## Source Notes

The exact source and note hashes above identify the reviewed versions. Use [[strategy/youtube-library]] for all selected videos and [[research/audit-aye-moah-history]] for the prior complete November/March raw reading and event chronology. Public accessibility supported the authorized research; it does not remove the expressly stated analytics boundary or authorize new first-person publication. Human testimony, guest accounts, title promises and editorial interpretations remain distinct.

Only this new audit file was written by this task. Raw sources, original notes, provenance, correction registry, scripts, promoted notes, core pages, index, log and the active extraction runner were preserved. No model job or QMD process was launched.
