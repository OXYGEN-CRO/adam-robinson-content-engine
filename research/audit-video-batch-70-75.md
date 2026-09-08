---
type: research
status: draft
owner: adam
created: 2026-09-08
updated: 2026-09-08
sources: [raw/sources/2026-09-08-youtube/selected-100.json, raw/sources/2026-09-08-linkedin/posts.normalized.json]
tags: [audit, attribution, chronology, video-notes]
---

# Video-note fidelity audit: selected ranks 70–75

## Result and scope

Fully read all fields of the six original structured JSON notes listed below, including every learning, metric, caveat, tension and coverage declaration. Independently inspected the exact caption ranges recorded below. This is a semantic spot-check of consequential source claims, not a second full-transcript read of all six videos. The central reader received each whole archived Markdown transcript; its six successful provenance records and source hashes were checked. No extraction was restarted or duplicated.

**One confirmed material defect:** the Sam McKenna note assigns a repeated Eric Siu outro and its post-engagement figures to Sam. Exact fields and a proposed correction appear below. The other five notes preserve the material boundaries in the inspected passages. “No defect found” does not mean their guest claims were independently verified, nor that uninspected raw passages received this additional audit.

Only this report was written. Raw captions, original note JSON/provenance/research renders, durable wiki pages, index/log and the live reader were not modified by this reviewer. All recommendations are internal synthesis proposals. Current claims continue to prefer the latest captured LinkedIn evidence; historical financial, platform or other advice is not validated current guidance.

## Sources and exact inspected ranges

Ranges below are **inclusive segment-start filters in seconds** against each `.transcript.json`, grouped only for readability. Every caption returned within these ranges was read. They need not coincide exactly with sentence boundaries. All listed original `.json` notes were read in full; raw Markdown/provenance and caption JSON hashes are recorded at the end.

| Rank / ID | Publication from selected metadata | Full raw archive | Independently read raw ranges, seconds |
| --- | --- | --- | --- |
| 70 `MUQ4f6DkmsA` | 2025-03-12 16:52:55 UTC | [[raw/sources/2026-09-08-youtube/videos/MUQ4f6DkmsA/MUQ4f6DkmsA|Brenden Short]] | 24–140; 406–640; 761–865; 1560–1670; 1790–1840; 2400–2725; 3100–3200; 3439–3459 |
| 71 `WLounenLFDg` | 2025-03-10 14:00:38 UTC | [[raw/sources/2026-09-08-youtube/videos/WLounenLFDg/WLounenLFDg|Lolita / JetSmarter]] | 0–600; 785–958; 1428–1450; 1855–1895; 2007–2090; 2280–2700; 2708–2900; 2984–3180; 3250–3320; 3300–3591 |
| 72 `b2L2rX26a6A` | 2025-03-07 15:01:00 UTC | [[raw/sources/2026-09-08-youtube/videos/b2L2rX26a6A/b2L2rX26a6A|Jessica Zweig]] | 470–525; 688–854; 1378–1448; 1636–1757; 2580–2667; 2795–2892; 3336–3540; 3583–3633 |
| 73 `pcG_402qsp0` | 2025-03-05 16:00:53 UTC | [[raw/sources/2026-09-08-youtube/videos/pcG_402qsp0/pcG_402qsp0|Wes Bush]] | 25–105; 806–927; 1250–1360; 1660–1998; 2070–2249; 2249–2542; 2558–2690; 2825–2960 |
| 74 `89Jl-njDguM` | 2025-02-28 17:00:19 UTC | [[raw/sources/2026-09-08-youtube/videos/89Jl-njDguM/89Jl-njDguM|Eric Siu]] | 0–365; 365–507; 1041–1148; 1365–1640; 2040–2240; 2491–2619; 2670–2790; 2888–2942; 3040–3213 |
| 75 `Y63QI4BKEcg` | 2025-02-26 15:48:26 UTC | [[raw/sources/2026-09-08-youtube/videos/Y63QI4BKEcg/Y63QI4BKEcg|Sam McKenna]] | 0–440; 432–568; 552–777; 1170–1330; 1410–1500; 1515–1699; 1830–2080; 2140–2448; 2448–2540; 2730–2940; 3060–3152; 3140–3302; 3300–3432; 3368–3432 |

Metadata descriptions were also inspected for JetSmarter, Eric and Sam. Titles/descriptions remain promotional source text, not proof. A truncated preliminary attempt to inspect Wes's ranges was discarded; only the successful reads above count.

Read current [[identity/backstory]], [[identity/values]] and [[strategy/learnings]] in full to avoid redundant proposals. Also read the complete normalized bodies of these four LinkedIn posts:

- [[raw/sources/2026-09-08-linkedin/posts/2026-08-20-7496214966937530368|August 20, 2026 schedule]]: current Monday meetings, Tuesday content and flexible remaining days. This supersedes historical content calendars; spacious time is not no work.
- [[raw/sources/2026-09-08-linkedin/posts/2026-03-19-7440454271109836800|March 19, 2026 product-direction reversal]]: explicitly contrasts the prior outreach-platform ambition with keeping RB2B simple. Its $18m scenario and $10m ceiling remain hypothetical, and its 90-day spam prediction is not a verified outcome.
- [[raw/sources/2026-09-08-linkedin/posts/2025-12-01-7401332695840272384|December 1, 2025 ghostwriter status]]: says he does not use a ghostwriter, credits Alec Paul as coach/strategist/producer. The post's ARR attribution is not re-audited here.
- [[raw/sources/2026-09-08-linkedin/posts/2025-11-03-7391161075544711168|November 3, 2025 Tommy Clark credit]]: credits his original ghostwriter's frameworks and first 20,000 followers. Historical ghostwriter help and later no-ghostwriter status can both be true.

## Confirmed defect: Sam note's Eric outro

Original source JSON: [Y63QI4BKEcg.json](youtube-video-notes/Y63QI4BKEcg.json), SHA-256 `78b4259883303c8f7763a259c5e1cfa548262f583222eabf4c176724e67ad257`.

The show signs off and announces Wes as the next guest before an appended clip begins. [Sam archive, 56:53–57:10](https://www.youtube.com/watch?v=Y63QI4BKEcg&t=3413) repeats the speaker saying he felt like Adam on LinkedIn, then reporting 841 comments/about 500 likes and joking “call me Eric Robinson.” The same passage appears in Eric's own interview's substantive ABM segment at [34:22–34:46](https://www.youtube.com/watch?v=89Jl-njDguM&t=2062), immediately before Eric explains his tool and agency connection. It repeats again in Eric's outro at 53:14–53:31. This is positive contextual attribution to Eric, not merely uncertainty caused by a speaker change.

Exact zero-based JSON paths and proposed replacements:

| Path | Original | Proposed reviewed wording |
| --- | --- | --- |
| `/speakers_and_attribution` | Sentence: “The opening is a teaser montage, and the final passage returns to Sam discussing a LinkedIn post.” This occupies string characters **[628,725)**, zero-based, end-exclusive. | “The opening is a teaser montage. The final passage is a separate appended Eric Siu clip, matched to his full interview at 34:22–34:46 in 89Jl-njDguM; it does not return to Sam.” |
| `/metrics_and_dates/25/claim` | “Sam reports 841 comments and approximately 500 likes on a LinkedIn post she says she published the prior week.” | “An appended clip repeats Eric Siu's report of 841 comments and approximately 500 likes on a LinkedIn post he says he published the prior week.” |
| `/metrics_and_dates/25/speaker` | “Sam McKenna” | “Eric Siu, in a separate appended promotional clip” |
| `/metrics_and_dates/25/caveat` | “Guest post-engagement self-report at recording time. The exact post date and whether this is the earlier displayed playbook post are not established. Her comparison to Adam supplies no numerical Adam engagement benchmark.” | “Matched to Eric's full-context ABM discussion in 89Jl-njDguM at 34:22–34:46 and repeated there at 53:14–53:31. This is not Sam's post or her displayed playbook post, not a second campaign, and not an Adam engagement metric. The relative post date belongs to Eric's underlying recording, whose exact date remains unknown.” |

Keep this item's supplied timestamps, `claim_type: guest_statement` and pillar. There is no need to manufacture a new outcome or change the other Sam metrics. The opening helpfulness/revenue-first teaser does come from Sam: compare 00:00–00:21 with 24:02–24:20 and 51:34–51:59. That separate match does not make the Eric closing clip Sam's speech.

**Applied status:** parent independently checked Sam 56:44–57:10 and Eric 34:10–34:55, then reported applying the speakers and metric-25 corrections through the reviewed registry, bound to both source JSON hashes. Original JSON/provenance remain preserved. This reviewer did not modify any original or derivative. The original research Markdown is intentionally distinct from the corrected durable `strategy/video-notes/Y63QI4BKEcg.md` rendition; an unchanged original research render is not evidence of a pending durable correction. Parent also directly checked Eric 26:30–27:10 and accepted the discovery-lapse qualifier for integration; the report itself does not claim that core edit is already applied.

## Findings and qualifications by source

### 70 — Brenden Short: no Adam testimony

Pete states at 08:46–09:05 that Adam is away at an executive offsite. Brenden's microcampaign system, Clay recommendations and examples remain guest material; Pete's views remain host material. This episode supplies no direct Adam identity claim.

The historical agency comparison has conflicting eight-versus-eighty emails per day; twentyfold replies/results and fivefold demos are different outcomes with undefined baselines. The note preserves those limits. “70% founders under $3m” describes a host-reported audience, with the revenue period unspecified. Filtering a sample 20,000 contacts to 30 or 50 is an illustration, not a measured campaign. “Zero” direct-API cost is promptly qualified as cheap, without total labor/platform cost. VanHack's $2,000/month unlimited-hire AI recruiter is a proposed pivot. The show-production plans and corrected one-week publication delay do not establish the exact recording date. No central addition proposed.

### 71 — JetSmarter: funding, valuation and older circumstances

At 09:11–09:24 Adam asks whether a billion was raised; Lolita corrects him: billion-dollar **valuation**, close to $200m **raised**. The title does not establish a $200m-to-$1bn valuation series, annual revenue or Adam-company performance. Her founding/exit durations and 2018 acquisition descriptions are retained without inventing a reconciled transaction timeline. Her defenses of the company and characterizations of media coverage remain her contested account.

The underlying recording is clearly historical relative to the March 2025 publication: first-child-at-six-months and Jasper-relative-history references are not a March 2025 household/business snapshot. No exact recording year is established here. Adam's five Aspen winter seasons/~300 ski days are cumulative, not days per year. At 31:01–31:10 he reports two M&A **processes**, not two closed exits. At 23:48–24:07 he admits not calculating CAC; enthusiasm about efficiency is not a measured CAC figure.

At 33:27–34:49 Adam changes his interpretation as a former JetSmarter customer: lost membership benefits and status helped make the disaster narrative persuasive to him. This is his personal reaction, not independent adjudication of the acquisition. At 45:10–48:19 he describes talented colleagues and recruiting around an ambitious dream; at 56:36–57:27 he emphasizes satisfaction from transformative customer outcomes. These support dated motivations, not an approved mission or proof of the customer's asserted results. His described 3–4 founder-hours/week and roughly 35 pieces exclude others' production work and do not supersede August 2026's calendar. No current metric or goal should be backdated to this upload.

### 72 — Jessica: an explicitly 2024 conversation

The host asks about the present in 2024 at 11:33 and Jessica repeats “today in 2024” around 14:01. March 7, 2025 is publication. “March,” “last Labor Day,” eighteen months of posting, twelve months to understand his message, and his Monday-meetings/content job all belong to that earlier conversation; no precise recording day is established.

Adam attributes his results partly to unusual founder–buyer–LinkedIn alignment. At 27:19–28:34 he studies roughly 100 Chris Walker podcast episodes, identifies recurring themes, and builds his own equivalents. At 43:19–44:03 his original ghostwriter helped him learn even though strategy was missing; Jessica's stronger “fell flat” characterization must not replace his mixed assessment. At 55:41–56:19 his use of a Justin Welsh worksheet lacked clarity about the personal message, not merely business categories. This is not evidence the worksheet was defective, nor that Jessica's four pillars are Adam's approved taxonomy.

At 47:02–47:23 Adam says he answers every comment to help readers feel they know him like a friend. Treat this as a dated self-report, not a verified 100% response rate or today's policy. Jessica's agency acquisition, seven-figure business, book sales, hiring target and client promotion remain hers. No Adam revenue or funding metrics are supplied.

### 73 — Wes: first excitement, incomplete outcomes and an unbuilt proposal

The billion-dollar claim is the host's promotional credit to Wes's playbook across companies, not one company reaching $1bn without salespeople. The conversation endorses founder-led selling and previews sales-assisted PLG. Adam's “almost $5 million in 12 months” has no explicitly stated ARR unit; his separate over-$20m “AR” Shopify-company report is not an RB2B metric.

Adam directly says the initial Slack contact supplied the exciting moment, but the team did not advance much beyond it (27:47–28:24). Nine out of ten users staying free was his original **design hypothesis**, not achieved conversion or market penetration. At 30:09–32:50 he rethinks delivery through an inbox, account signals and suggested messages; “hypothesis, don't have the product yet” is explicit around 31:27. The later March 19, 2026 reversal governs current product direction.

At 34:36–36:00 he distinguishes visitor traffic from a lead and then a booked demo, and says the pushed Clay integration was too hard for most of these users despite fitting some companies. At 36:56–37:24 he says users corrected his assumption that drafting outreach was a minor obstacle: they were busy, not incapable. The numerical severity scale is reversed in his answer; the qualitative change of mind is clear. Wes's signal/noise complaint expressly might already have been fixed. Approximate first-version 1,000 signups/12 paid customers, future courses and community design must not become today's KPIs or shipped offers.

### 74 — Eric: discovery lapse is Adam's; SEO prescriptions are Eric's

The title's SEO-death claim is contradicted by the actual discussion. Eric retains content/links/Google, recommends focus before diversification, and conditions SEO investment on runway, product-market fit and an already-working channel. Adam says he has not built an SEO acquisition play in his SaaS businesses; this is not proof those companies had zero organic traffic or his adoption of Eric's strategy.

At 17:23–18:25 Adam describes the audience he helps most as founders around $1m ARR and warns against acquisition spending before a solid value proposition. His community is around day 20 (24:17–24:38), its captioned pricing is unreliable, and channel consolidation is a proposal. At 26:38–27:04 he says Adam/Santos did extensive prelaunch discovery then stopped for about nine months; he associates plateau and customers turning off the product with competition and unmet needs. This is his causal diagnosis, without a churn percentage or proof a new process had shipped.

At 42:30–43:11 he credits Dave Gerhardt's idea of community formed through recurring LinkedIn conversations. Eric's 841 comments/500 likes, 20–25 calls, lower CPC and higher account engagement belong to Eric's tool. Conversion evidence was not yet available. Personalized company-level ads are not verified individual-level personalization. Diana's “$1m to $10m” and “zero to $10m ARR” twice are differing claims about her sales history, not Adam's. Her joining to build a still-absent sales model is an announcement relative to recording.

### 75 — Sam: selective automation, measured scopes and separate voices

Adam explicitly intends brand as a 2025 content pillar, questions whether automation leaves reps understanding an important account, and praises unusually thorough discovery/craftsmanship. Those are his statements; Show Me You Know Me, the gifting records, specific referrals and reputation-review policy are Sam's. Her support for AI-assisted research and prioritization qualifies a blanket anti-automation reading.

Sam's 239 requests in approximately a day and Adam's 8,196 **pending backlog** are different metrics. Her 43% open/~20% response versus 6%/<1% comparison lacks cohort/date/methodology and is not a meeting rate; the 43 opens/20 replies illustration fits 100 emails, not 50. The nearly $100,000 Equifax deal and thirteen prospecting minutes are her selected case, excluding unknown downstream sales/delivery time and contract term. She explicitly says at 49:03 onward that it is not generally so easy.

Dave's nine ventures are not nine exits; his 96 closed-beta customers and warm-outreach product are not Adam's. His ten-draft/fifteen-minute workflow is a stated goal. Sam's 19-person team is distinct from Adam's six executives/50% women; Adam is uncertain about the company-wide proportion. His referenced 120 hours of email observation and nineteen book edits are third-party examples. The title establishes no quantified multimillion-dollar loss. The sole confirmed note defect is the separate Eric outro documented above.

## Three proposed core additions, maximum

1. **Continuous discovery, with a real lapse attached** — add one dated example under SaaS learning/customer-led values: “In the conversation published February 28, 2025, Adam says prelaunch RB2B discovery lapsed for about nine months. He links the subsequent plateau to changing competition and needs, and says customer conversations cannot stop.” Cite Eric 26:38–27:04. Do not claim uninterrupted practice, measured causation or an implemented fix.
2. **A useful outcome beyond first excitement** — enrich the existing Slack-learning paragraph: “In the March 5, 2025 publication, Adam distinguishes the excitement of seeing a visitor from the work of producing a lead or demo. User feedback also changed his estimate of outreach drafting: busy users needed help taking the next action.” Cite Wes 27:47–28:24 and 34:36–37:24. The inbox/AI workflow was unbuilt and later product direction changed; do not promote it as current RB2B behavior.
3. **The content-learning path was mixed and gradual** — optional short backstory enrichment, without duplicating the existing topic-learning point: “In footage explicitly set in 2024, Adam describes learning from an initial ghostwriter and studying Chris Walker, while finding his personal message only through sustained publishing. His early pillar worksheet lacked that personal clarity.” Cite Jessica 27:19–28:34, 43:19–44:03, 46:40–48:08 and 55:41–56:19; retain November/December 2025 Tommy/Alec distinctions. This does not make him currently ghostwritten, approve a voice, or import Walker's beliefs.

Other guest frameworks and historical minor numbers belong in attributed video notes, not the central identity/proof pages. No additional core proposal is made from JetSmarter or Sam.

## Source Notes

Original structured notes and provenance are in `research/youtube-video-notes/`; reviewed durable derivatives belong in `strategy/video-notes/`. Full local transcript links are in the source table. Latest selected metadata governs publication order; publication is not a blanket event date. All claims remain self-reports, guest reports or clearly labeled interpretation.

The hash inventory below records what this review examined. `source_word_count` counts the central reader's full Markdown input, including its archival formatting; it is not the number of raw words independently reread here. Each provenance `exit_code` was zero and `source_sha256` matched the actual raw Markdown bytes.

### MUQ4f6DkmsA

Full input: 11,016 words / 72,542 characters. [Original JSON](youtube-video-notes/MUQ4f6DkmsA.json); [provenance](youtube-video-notes/MUQ4f6DkmsA.provenance.json).

```text
note_json: 691def0153bddb8dfb0eecbff58146ad0159c312853024ad4b747838204f6701
provenance_json: 7af94b22c3d819d497c0b26c4ab71016df3673186b6cd40659b58fc89d5535aa
source_md: 72f5f12a7b565494a7b449435f4470c68e336dc4be4035fa2b1fa896f35f3cb9
segments_json: 618bd107b590e450fd76bd9de75cee2b4f1bd36c7bf9553c076d58ca60ba164d
full_prompt: 837b657b2daf1824f18959ba41288167c6c6c86407aabf4f08f555810178ff36
```

### WLounenLFDg

Full input: 11,596 words / 75,313 characters. [Original JSON](youtube-video-notes/WLounenLFDg.json); [provenance](youtube-video-notes/WLounenLFDg.provenance.json).

```text
note_json: c7f7e9c462c558373751e1bd5b7a0e172ba5466e4838b07c16e0fa00fb59e8f2
provenance_json: 28f735c3a8d2d8c3bc2c06c5dbbbfd66534c57e9c695909f685721a5658ff53e
source_md: 5affae9dbb6482007eb49b37d69929b417847268cb354d6cf3c93da4984b8357
segments_json: 9cb4a6827983d30be568166b4305cdbf00eee2986293af21ae043db18f633359
full_prompt: 52dff8455db2d7c058b0b31a53c8480f36e1f00390f88d8c7c9347efee05ef36
```

### b2L2rX26a6A

Full input: 10,935 words / 73,159 characters. [Original JSON](youtube-video-notes/b2L2rX26a6A.json); [provenance](youtube-video-notes/b2L2rX26a6A.provenance.json).

```text
note_json: e93e4e0871cdeb83091f018b18e739a66768e973b5e57df5c5aa9f4e5cb8358e
provenance_json: 237ffa3c4b12e70796c76bbc1ce01511384875166c8cf4168dc4716694b5260d
source_md: b69bf1d13592166025ced71957c8ae3256ea2496e7ac8b58b9eece866461e5f6
segments_json: fe54243a9ed2162eb03c2318875cae6d8020c06e503c327886a960b0347664ed
full_prompt: a36621d47fda95741e11762f9acbcb87f4528b5af1f1976a2d90447b72858f4a
```

### pcG_402qsp0

Full input: 9,118 words / 60,310 characters. [Original JSON](youtube-video-notes/pcG_402qsp0.json); [provenance](youtube-video-notes/pcG_402qsp0.provenance.json).

```text
note_json: d527b8cad4ef4a6a8aabf1271b8c9fec9072b4581cdf22edb07936c055be1059
provenance_json: de4d18f0b9e4ca2bfdc47f1092a3cd7a18b9a927f40b5f2d32bbf15f093ab71c
source_md: bb3bd703b8679425bd08eb0ec597acdb269b37badaa393384114ca5f0bf0b292
segments_json: 8e8ee224cccec6acebf69defc99b6247a65511d5ff86cd72982b2af99fa2c390
full_prompt: d21aaf5f722bfd50c6dfa1bff4026f9fec64ad853fe5fb1c8fbdeefb15549555
```

### 89Jl-njDguM

Full input: 11,104 words / 72,852 characters. [Original JSON](youtube-video-notes/89Jl-njDguM.json); [provenance](youtube-video-notes/89Jl-njDguM.provenance.json).

```text
note_json: 58be7e57e96c9044e705c4f40dda04cc22a77781d4a3aadedf223e56d511ead2
provenance_json: 0d6d03e15225c0c29af7978255ab1de658ee6498ae1f83ea26cf8b70f1985787
source_md: 041bb835573113605eb494468e321186eaa1fa7f6a8aa5105f2f41cb22df200c
segments_json: 4dd34b81d8aaf75139f12891e60719cfbdc3d740bdd6700e68b41ce6a7f4ce19
full_prompt: 6a1fdcd9abdee636665bffe8005223f40887c2e8bce51b41c597c4734b50e286
```

### Y63QI4BKEcg

Full input: 12,060 words / 78,660 characters. [Original JSON](youtube-video-notes/Y63QI4BKEcg.json); [provenance](youtube-video-notes/Y63QI4BKEcg.provenance.json).

```text
note_json: 78b4259883303c8f7763a259c5e1cfa548262f583222eabf4c176724e67ad257
provenance_json: bf24c5dd1c07623986939fe46062180d2fb7f59351972066b12f739a7f655beb
source_md: 0572732915c88e723e4dfa7fe6f442bbe50971679cba080da7ab832dd7110073
segments_json: cebad02357627cae05486c74b1c1cbe0df66ff54109d88f966c155f20ecf7cd5
full_prompt: 90922031297157b26d24acabfa28c08fe38b837d5bc717bb63655eae19ef6207
```

