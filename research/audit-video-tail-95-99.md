---
type: research
status: draft
owner: adam
created: 2026-09-08
updated: 2026-09-08
sources: [raw/sources/2026-09-08-youtube/selected-100.json]
tags: [audit, attribution, chronology, video-notes]
---

# Tail video-note fidelity audit: ranks 95, 96, 98 and 99

## Scope and completion status

**Complete:** all fields of the four original structured JSON notes have been read in full, including every learning, backstory item, metric, tension, caveat, reusable topic and coverage declaration. Independent source spot-checks cover the passages inventoried below. The selected ranks are 95, 96, 98 and 99; rank 97 belongs to another reviewer. No extraction has been duplicated.

One minor chronology overstatement was confirmed in rank 95 and has been corrected by the parent through the reviewed renderer. No other material extraction defect was found in the inspected passages. All four successful provenance records and source hashes were verified. This does not independently validate speaker claims, screen-only evidence or uninspected raw passages.

Only this report is being written. Raw sources, original notes/provenance, reviewed-renderer registry, durable context, live reader and QMD are outside this reviewer's write scope. Historical guest claims are not independently validated current advice. Publication timestamps do not automatically date the recording or a metric's measurement window.

## Source inventory and exact inspected ranges

Ranges are inclusive segment-start filters in seconds against the corresponding `.transcript.json`. Every returned caption was read. Keyword-navigation excerpts were used only to choose passages and are not counted as full-source reading. This audit does not claim a second full-transcript read.

| Rank / ID | Publication metadata | Full local archive | Exact raw ranges inspected, seconds |
| --- | --- | --- | --- |
| 95 / `KJbi0TPviRg` | September 18, 2024, 14:38:21 UTC | [[raw/sources/2026-09-08-youtube/videos/KJbi0TPviRg/KJbi0TPviRg.md]] | 0–250; 295–570; 985–1135; 1950–2445; 1992–2032; 2680–2735; 2730–2905; 3000–3190; 3323–3478 |
| 96 / `4SpQrjf1mwA` | September 11, 2024, 14:00:07 UTC | [[raw/sources/2026-09-08-youtube/videos/4SpQrjf1mwA/4SpQrjf1mwA.md]] | 0–250; 235–295; 475–655; 730–785; 860–1330; 1435–1570; 1590–1960; 2040–2280; 2275–2640; 2640–2705; 2765–2795; 2970–3240; 3207–3362 |
| 98 / `c5DvcHlt1c8` | August 28, 2024, 14:00:28 UTC | [[raw/sources/2026-09-08-youtube/videos/c5DvcHlt1c8/c5DvcHlt1c8.md]] | 0–250; 390–610; 595–672; 970–1250; 1265–1330; 1560–2170; 2450–2620; 2780–2830; 2885–3120; 3200–3290; 3279–3434 |
| 99 / `jUTHYPaWyeo` | August 21, 2024, 14:00:45 UTC | [[raw/sources/2026-09-08-youtube/videos/jUTHYPaWyeo/jUTHYPaWyeo.md]] | 0–250; 240–375; 366–488; 490–810; 803–980; 1200–1600; 1700–1990; 2610–2760; 2920–3010; 3000–3065; 3110–3310; 3352–3507 |

The selected metadata records and all four `.info.json` descriptions were read. Rank 95's description is empty. Rank 96's description frames Chili Piper as $30M ARR; rank 98 uses broad “outbound died” promotional language; rank 99 explicitly identifies Pete Crowley and Understory as the presenters. Each must be interpreted with the actual conversation.

## Confirmed defect and applied correction

**Rank 95, minor chronology overstatement — corrected by parent in the reviewed-renderer registry.** The original `/backstory_and_values/3/claim` says:

> Adam says he shared an office with the people who founded Jasper for two years before they started Jasper AI, giving him an early view of what the software could produce.

Within that original claim string, `for two years before` occupies zero-based half-open character indices **[65, 85)**. Original JSON SHA-256: `ebbf256e11a6fa574fa93453c0940a683a9ba9e11e50c82141056cc1f9c27715`.

Raw captions at **33:32.639–33:40.679** say he “was sharing an office” with the future founders “two years before they started Jasper Ai.” That establishes timing relative to Jasper, not a two-year duration. The proposed correction was to describe him sharing an office roughly two years before Jasper AI began and explicitly leave the duration unknown. The surrounding passage links seeing the software to his content decision, without securely dating that observation to the entire shared-office period.

The parent independently read **33:15–34:10** and reports applying a source-bound correction to this object, preserving timestamps, speaker and claim type, and adding an explicit duration caveat. Original JSON/provenance remain preserved; this is **not a pending durable correction**. The parent also reports that the core backstory already says only that they shared an office. No core chronology rewrite is needed.

## Consequential raw-source checks

### 95: Anthony Kennada — category creation and qualified attention

Adam explicitly says it is **September 17, 2024**, around 39:18–39:30, despite publication the following day. This is stronger recording-date evidence than inferring a date from a weekly schedule. Anthony's isolated reference to 2025 elsewhere does not override that explicit statement without further evidence. No time zone is given for the spoken 2:40 p.m.

“Don't create a category” is Anthony's qualified argument: only undertake it when the product's problem has no recognized alternative and education is unavoidable. At 5:02–9:30 and 18:04–18:55, Adam says this challenges how he has been thinking, describes the appeal of *Play Bigger*, and questions whether his own inbound-led-outbound work counts as category creation. His closing surprise is not evidence he announced a formal repositioning or ceased the activity. Gainsight's five-year lag between marketing buzz and revenue momentum is Anthony's history, not RB2B's growth period.

At 33:16–35:20 Adam describes sharing an office with Jasper's future founders and expecting AI to multiply generic content. His chosen response was to show his face and be highly transparent about his journey. His impression that AI-written comment replies had become less noticeable is personal observation, not a measured detection benchmark or proof all his own replies were manual. Anthony's audience-marketing product and roadmap remain Anthony's company claims.

At 37:20–39:30, Adam reports a video reaching 2.9M impressions, 119 comments with about 90 already present before wider distribution, and followers he considered poorly targeted. These are his own observations, not inspected analytics. His takeaway emphasizes relevant followers over broad impressions. He says he **may** stop short-form video after paternity leave; this is a contemplated decision, not an accomplished change or current September 2026 policy.

At 45:01–48:15 he describes poor on-camera performance in 2017, an approximately $3M ARR startup that had not grown for three years, basic camera coaching from Dustin Luke in Argentina, and later weekly one-minute GetEmails videos over six months with Helen. The displayed old Lead.com pitch promises four times as many abandoned-cart emails; replaying an advertisement does not validate that performance claim. Company chronology should not be resolved from the old pitch alone. The story supports practice and coaching, not an innate-camera-confidence claim or a universal six-month timetable.

Anthony's approximately $15K studio at 50:33–51:30 is his equipment example, not Adam's content budget. His advice to use no LinkedIn when the intended audience is elsewhere at 52:01 onward is guest advice. The following week's Amit appearance and Adam's expected return are plans at recording, not present show scheduling.

### 96: Alina Vandenberghe — guest financing, founder visibility and customer learning

The opening calls Chili Piper a $30M ARR company that bootstrapped and subsequently raised; Alina says three years of bootstrapping and approximately $3M ARR before funding. Do not label it then-unfunded or transfer its numbers to Adam. Alina sold a house and possessions; at 4:02–4:30 Adam explicitly distinguishes his own experience of renting and spending his savings before reaching cash-flow positivity. His general belief that startups consume available resources is an interpretation of that experience, not a survival guarantee.

The early product's claimed 40%-to-60% conversion improvement, $30-per-user charge and customer ROI belong to Alina. Her $3M seed, $15M 2020 Series A, approximately 11/12-to-30-person expansion and reported benefits/costs of outside funding are her account. The $100M exit story around 14:23–16:00 concerns an unnamed founder she admired and her aspiration, not a Chili Piper or Adam exit. Early investors' reported secondary gains are not her realized proceeds.

At 17:00–17:10 Adam wishes he had a product with net revenue expansion. That is a historical aside, not a precise current retention metric. Alina's discussion of competition, confidence, communication and work-life balance is her personal experience. Her answer about potentially reaching the same scale without funding explicitly depends on being a different person with different experience; it is not proof capital was unnecessary in the actual company.

At 28:28–30:00 Adam endorses building in public because a growing body of work can become more useful and encourage readers to explore the archive as the business develops. His Nick Shackelford example is a third-party illustration, not audited commercial attribution. At 34:00–37:59, attending events, identifying influential people, using drawings to solicit design input and asking why prospects preferred competitors are Alina/Nicolas's tactics, not a previously undocumented Adam acquisition playbook.

At 42:25–44:17, Adam expresses interest in the communication book/training Alina credits, then describes being outgoing around familiar people but inhibited among strangers. He says industry recognition made events feel more familiar, and recalls difficulty approaching strangers at early GetEmails events with a colleague captioned Diane. His experience is separate from Alina's 11-day retreat and personal transformation. His wish to read the book is not proof he did so or attended the retreat. The note preserves both speaker boundaries and his contextual self-description.

The year-in-advance customer payments at 49:50–50:48 are Chili Piper's early financing and demand evidence. Around 51:25–51:50 Alina dates channel hiring imprecisely and attributes about 20% of pipeline to it, with more influence beyond that; these are neither revenue percentages nor additive independent attribution. At 52:00–53:59 she describes direct feedback requests before or after churn. Adam says he needs to start doing that because churn is difficult. This is an acknowledged learning opportunity, not evidence that he implemented the process or that it solved churn. The later discovery-lapse admission already filed centrally is a related qualification, not something to overwrite.

### 98: Jason Bay — outbound remains conditional, and practice AI is not sales automation

The description's broad death-of-outbound framing is qualified immediately: Adam says Retention.com's 2023 BDR expansion failed, **but outbound still works** with appropriate strategies. Jason's customer roster and sales-performance claims are his own. At 6:31–9:59 Jason describes his prior done-for-you prospecting business; his mid-sentence address to “Adam, Santosh” does not mean they cofounded it or never used phones. At 10:07–10:21 Adam explicitly recalls using phones in 2023 and says they had not used the proposed voicemail-to-email approach.

Salesloft, Orum and Gong figures at 7–9 minutes are studies Jason cites, not inspected datasets or RB2B results. His 15-touch example, interest-based CTA comparisons and under-75-word framework are attributed 2024 guidance. His hypothetical email to an executive named Adam is not evidence of an actual deal. SMS, deliverability and platform comments are not validated current technical or legal guidance.

At 18:12–19:03 Adam directly credits Alex Hormozi's *$100M Offers* with transforming his thinking and shaping RB2B's core offer. He endorses making the offer compelling enough that the intended person would feel foolish declining it. The caption's isolated “isn't doing so well” conflicts with the surrounding praise; it is unsafe evidence of underperformance. The $100M is the book title, not company revenue or a quantified lift caused by the book.

Most of the 26–35-minute tactical framework is Jason's teaching, including executive-to-executive outreach, VC introductions, content supporting outbound and his own Square example. These are not proof Adam used an investor network or ghostwritten outbound emails. Around 41:40–43:30 Jason conditions his engagement on paying/renewing customers, known ICP, an inbound/content foundation and sales leadership. Adam asking how to serve a lean bootstrapper is not confirmation he bought the engagement.

At 53:27–54:47 Adam describes repeated relevant content making a new connection feel familiar enough to answer a casual message. His repeated 60-day period is rhetorical, not an observed average or guaranteed response time. The note preserves that qualification. Jason's preceding “team of one” account explicitly includes operations and agency support and does not describe Adam's staffing.

At 48:32–49:49 the Hyperbound “sell Adam 6sense” bot is an explicitly described simulation and contest using his voice. It is not an actual 6sense sales interaction, a statement that he bought the product, or evidence of unattended outbound calls made in his name. Jason's skepticism about autonomous selling and his comments about AI increasing inbox volume are his dated opinions. Next week's Mark debate remains a announced event in this recording; the separately archived debate establishes its own content.

### 99: Pete and Understory — signup-start attribution and planned spend

**Adam is absent.** Pete explicitly says Adam and Santos are away, introduces himself as RB2B's growth lead, and hosts Ali and Alex from Understory. Their accounts of the business and Adam are attributed team/agency reports. The dog and Colorado story at the end belong to Pete. The opening's joke about showing everything except a credit card is not general authorization for future disclosure.

Pete's Bullseye framework at 3–6 minutes puts community/content among working channels and ads/SEO in experiments. His two-channel limit, quarter-long test preference and agency-first approach are his operating explanation, not a newly confirmed permanent rule from Adam. Ali's approximately 100K follower count is a conversational historical estimate. Four campaign personas are sales, founders, marketing and outbound agencies, not four verified proportions of the entire audience.

At 9:10–9:59 the conversion event is **email submission starting RB2B signup**, not completed installation, activation, paid conversion or retained customer. Ali describes seven-day click and 30-day view attribution windows. They are distinct attribution lenses, not independent conversions to sum. He prefers click conversions as a tighter relationship to ads; that preference does not establish causal incrementality or audited ROI. A claim of more than one million ad impressions is a roughly month-long historical report.

At 13:02–13:42 the three-week wait before editing/boosting a post is a precaution based on an explicitly **unproved throttling hypothesis**. It is not confirmed platform behavior. At 21–24 minutes the poorer-converting sales audience and installation-authority explanation are observations and hypotheses; adding SDRs/BDRs and a possible September pivot are future tests. They specifically worry that those users' influence may not be attributable.

At 25:01–26:40, $25 is the signup-conversion **goal**, less than $50 is a broader desired ceiling, and approximately $33 is reported current performance. These are not customer acquisition cost figures. At 29–32 minutes July's near-$10K experiment leads to planned approximately $20K August pacing, while the later recollection says roughly $8K spent in the first month. Neither requires inventing a reconciled exact July total. Reported cost per conversion rises about $3; the speakers call the scaling profitable, but no paid-revenue, gross-margin or lifetime-value calculation is supplied. Spending above $100K per month is a hope, not achieved spend.

At 44–45 minutes Pete and Ali stress Adam's existing audience and content as a precondition. Ali's claim of at least twice the ad performance for regularly posting clients has no defined metric, sample or causal test. At 52–53 minutes the original cold-nurture/retarget-convert model changes because people start converting on cold thought-leader ads. Ungated material is the described current approach; gated-content testing is only on the roadmap. The $500 monthly-budget discussion and $25–$50-per-ad-per-day recommendation are guest heuristics, not demonstrated statistical significance or current ad prices. Academy publication and Pete's own future show are dated plans.

## Context comparison and possible central additions

Read [[strategy/learnings]] and [[audience/ideal-follower]] in full during this audit. They already contain audience/buyer separation, conditional outbound and offer/discovery principles. Most of these historical details therefore belong in their video leaves.

Two possible citation-level enrichments for parent judgment:

1. Adam's September 17, 2024 viral-video account can make the existing audience-fit boundary concrete: he valued relevant followers over a 2.9M-impression clip and treated its broad distribution as poor fit. Preserve that judgment and the date; do not claim he subsequently abandoned video.
2. Adam's direct Hormozi credit at rank 98, 18:12–19:03, can support the origin of his emphasis on a compelling core offer. It is inspiration and self-reported influence, not an endorsed book recommendation or independently measured growth cause.

No central addition or renderer correction has been applied by this reviewer. The parent's applied rank-95 correction is recorded separately above.

## Original-note review and hash inventory

Fully read [[research/youtube-video-notes/KJbi0TPviRg.json]], [[research/youtube-video-notes/4SpQrjf1mwA.json]], [[research/youtube-video-notes/c5DvcHlt1c8.json]] and [[research/youtube-video-notes/jUTHYPaWyeo.json]]. These are preserved originals. Any approved correction is applied to the durable [[strategy/video-notes/KJbi0TPviRg]] derivative through the parent's source-bound registry; an unchanged original research render does not mean the durable correction remains pending.

The inventory below identifies the reviewed originals, successful provenance records, full Markdown inputs, and normalized caption JSON used for the independent spot-check. Source counts and prompt hashes come from the central reader's provenance. Matching these hashes verifies the supplied input identity, not independent review of every raw word by this auditor.

### KJbi0TPviRg

```text
note_json_sha256: ebbf256e11a6fa574fa93453c0940a683a9ba9e11e50c82141056cc1f9c27715
provenance_json_sha256: 62bf73c3ab0428872bb9231922387af6a2e9b4a9b7966b10c358aa060df027a8
source_md_sha256: 4fbe030d978b0bddce423778dd52393d857fefdd450cf6235f51ed29772fd0d2
segments_json_sha256: 9cc5f5390d1cddbb1497dd97ff1a17bb977c41ded73d29f457df8e5b53c5e37e
prompt_sha256: 5999cf78a6f6739972b3a077ed13e6b3d4052463ade9d2139a916e9da041175a
source_words: 10596
source_characters: 71783
reader_exit_code: 0
source_hash_match: true
```

### 4SpQrjf1mwA

```text
note_json_sha256: 8b779f20d32753cbaa5d14928cdd2b55e0363d44edc3512f660eb575b60c29f2
provenance_json_sha256: b06ef1bfcf27fbe299f4b97c069b005459d516d40a410b92f591157db21e1ea9
source_md_sha256: 91a70a56bcdd309e7dee48196becb019843838e21a9740e5f553695c8b1893dd
segments_json_sha256: e072b10a2ed3fe287fbd23076c136147d9bb5a3f8f6e77d0b9549c6c2efe5473
prompt_sha256: bae2df54eee8a8fafa6b6082770136873aecd3ab70eb979540563a7e2921a66b
source_words: 10093
source_characters: 68984
reader_exit_code: 0
source_hash_match: true
```

### c5DvcHlt1c8

```text
note_json_sha256: 74d4cfc4271e7aa11ec816c7a8bc1d801d27d744c01881cb33ec42e41727bb2e
provenance_json_sha256: 2bdd7590bfa36be5aa80a9254f259b9f6d3f7cc5275565439c04652a91b47673
source_md_sha256: dba17b1f661cc2fe35b45e89f92da9f6eb8ffea8108ca65714d8346f9d51bd95
segments_json_sha256: bbf23eedb985c649780ba75d4f713367f463dc4583137cc97dc3c22dd80624b6
prompt_sha256: e32fc1a5e2afe5f494734ec53ac1eb484db412d35bd437dd5053c9fbc8d66003
source_words: 11099
source_characters: 75550
reader_exit_code: 0
source_hash_match: true
```

### jUTHYPaWyeo

```text
note_json_sha256: 9f453a8e7d179c54937c9a59b95eb9f9abe5d97635e0cc197258617c72047c47
provenance_json_sha256: 88cb03b0c3c579f23b032b151f800d8958e7d2ebb14074f603ad8fe92eefd1ea
source_md_sha256: 8cf40767f2406cad4224cca53f6261d74021366b5793c382637e30573f669998
segments_json_sha256: a8a65fd5925154715d7134fa0fefd09b7da2ccd568453dcf9016e44a5733e97c
prompt_sha256: 71350cb6526f79e2e598d453022c6d1648cc9f852eb7460201ea8181dae1ba63
source_words: 11023
source_characters: 75638
reader_exit_code: 0
source_hash_match: true
```
