---
type: research
status: draft
owner: adam
created: 2026-09-08
updated: 2026-09-08
sources: [raw/sources/2026-09-08-youtube/videos/atzcNzDIsgg/atzcNzDIsgg.md, raw/sources/2026-09-08-youtube/videos/gOvQngBqw80/gOvQngBqw80.md, raw/sources/2026-09-08-youtube/videos/d_rVwh521po/d_rVwh521po.md, raw/sources/2026-09-08-youtube/videos/EdDAHrvBDPM/EdDAHrvBDPM.md, raw/sources/2026-09-08-youtube/videos/D-8umeDdYP0/D-8umeDdYP0.md, raw/sources/2026-09-08-youtube/videos/g9mejr_-odc/g9mejr_-odc.md, raw/sources/2026-09-08-youtube/videos/ScY0k43N1u8/ScY0k43N1u8.md, raw/sources/2026-09-08-youtube/videos/CqlO3vkU_zo/CqlO3vkU_zo.md, raw/sources/2026-09-08-youtube/videos/jZ4o_B2g5bo/jZ4o_B2g5bo.md]
tags: [audit, guest-attribution, full-transcript-review]
---

# Guest-playbook audit

## Examined material

Read every nonempty caption segment in the three archived normalized transcripts, including opening teasers, audience/pitch segments, late discussion and closings: **33,110 words across 4,663 segments**, with combined metadata duration **2h 57m 14s**. Reading views joined consecutive caption fragments and inserted minute markers; the preserved sources were not edited. The initial long display of the Jesse transcript was truncated, so its missing 20:00–40:00 section was reread in a separate complete display before synthesis.

| Video | Published | Words / segments | First–last segment starts | Raw Markdown SHA-256 |
| --- | --- | --- | --- | --- |
| [[raw/sources/2026-09-08-youtube/videos/atzcNzDIsgg/atzcNzDIsgg|Jesse live build]] | 2025-09-11 | 11,616 / 1,573 | 00:00:00.080–00:59:41.599 | `4f355bf41b375f6ae0d99cb0fafb15d69813caec239792f118a600e3fd978491` |
| [[raw/sources/2026-09-08-youtube/videos/gOvQngBqw80/gOvQngBqw80|Josh interview]] | 2025-09-19 | 10,837 / 1,563 | 00:00:00.080–00:58:18.079 | `4ab614b6253031a3a25f7a7caf3a6c42cbe2e1e5d522675efb61d61b76c1985e` |
| [[raw/sources/2026-09-08-youtube/videos/d_rVwh521po/d_rVwh521po|Peep interview]] | 2025-09-08 | 10,657 / 1,527 | 00:00:00.880–00:59:06.480 | `6baaa8118a539e4dd60854156fa7d6908aeb2059cfeba1199014c46f0aa058a5` |

Also inspected each video's archived `.info.json` title, description, publication metadata and duration. The descriptions identify **Jesse Ouellette / LeadMagic**, **Peep Laja / Wynter**, and **Josh Abramson / TeePublic**. These spellings are metadata-backed, not silent corrections of the captions. See [Jesse metadata](../raw/sources/2026-09-08-youtube/videos/atzcNzDIsgg/atzcNzDIsgg.info.json), [Peep metadata](../raw/sources/2026-09-08-youtube/videos/d_rVwh521po/d_rVwh521po.info.json), and [Josh metadata](../raw/sources/2026-09-08-youtube/videos/gOvQngBqw80/gOvQngBqw80.info.json).

The generated notes became available during this review. Their **Summary**, **Speakers and attribution**, and **Tensions and corrections** sections were checked for all three; primary transcripts, rather than generated assertions, anchor the hub. No second CLI extraction was run. The generated notes appropriately preserve the central attribution and outcome limitations below.

## Jesse: attribution and demonstrated outcome

- **Host is Pete, not Adam.** Jesse addresses Pete at 01:47–01:49. At 46:50–47:40, the host describes his own part-time RB2B role and consultancy. Adam is discussed in the third person. The host's roughly 95%+ AI support/sales claim around 47:40–48:15 cannot be filed as Adam speaking.
- **Teaser and live build are different examples.** The one-day internal listening dashboard at 00:00–00:59 repeats material around 30:20–32:20. It is not the champion tracker built during the session.
- **Promotional launch language exceeds the caption evidence.** The description calls the app revenue-generating. The dialogue includes prebuilt prompting, live authentication/database failures, continued fixing around 53:00, and later hypothetical billing and launch discussion at 56:35–58:30. No captured purchase or completed paid launch is established.
- **The practical advice becomes more conditional.** The initial one-shot framing is qualified by staged sample-data UI work, integrations and developer assistance at 40:35–44:30. At 34:00, Jesse corrects the assumption that v0 is his primary tool: he uses Cursor most.
- **Repair claims are not test evidence.** Around 53:50–56:35 Jesse claims broad success against developers and says every discovered bug was fixed, while acknowledging he has not understood all the repairs. No exhaustive functional or security review is supplied. The hub retains the debugging process without certifying the application.
- **Commercial figures and licensing claims remain excluded from proof.** Historical approximately $30,000/month and later approximately 1,300 customers have different time contexts. Tool-cost examples, per-call API economics, free-tier possibilities and categorical IP-ownership assertions are not a validated operating budget or licensing assessment. They belong to Jesse/Pete, not Adam.

## Josh: capital, counterfactuals and mixed outcomes

- **Guest and Adam histories remain separate.** Josh owns the CollegeHumor/Vimeo/Busted Tees/TeePublic accounts. Adam's adjacent-business remarks and financial figures at 55:00–56:55 were read but are not promoted by this guest hub; the existing dated proof/conflict process owns such integration.
- **The acquisition anecdotes are anonymous, approximate and unverified.** At 06:00–09:15, Josh withholds identifying detail, guesses the capital raised and recalls rejected offers. The opening teaser repeats the same large-offer story, rather than providing independent corroboration.
- **A majority corporate acquisition is not a venture round.** Josh draws analogies around control and risk appetite. His IAC account should not be converted into a direct history of raising VC or a universal investor-behavior rule.
- **The sale account includes both costs and benefits.** Lost autonomy and reduced motivation at 14:30–19:10 coexist with appreciation for the later buyback and remaining-stake arrangement at 42:20–44:00. He says he does not regret the overall sale. Neither an uncomplicated success story nor “never sell” captures his account.
- **Separate financing is a considered alternative.** At 43:40–46:20, Josh describes the risk of funding Vimeo from the other business and a counterfactual separate raise constrained by the actual deal. This is not an executed restructuring playbook.
- **Do not resolve financial inconsistencies by guessing.** The dialogue variously gives Vimeo values around $1.4B and $1.8B; ownership percentages, retained equity and personal net-worth exposure have different denominators. The 30-times traffic-growth statement has an unclear company referent. Adam's inflation conversion and broad probability comparisons are not verified statistics.
- **Counterfactual growth and later company status remain bounded.** Josh cannot know what the original team would have built independently. His retrospective characterization of CollegeHumor going to zero is not a verified current entity-status statement. He explicitly credits later operators for Vimeo's success around 49:50–50:10.

## Peep: research method and rhetorical limits

- **More than two speakers appear.** Adam speaks about RB2B and Retention.com; Peep supplies the Wynter/CXL experience; Pete runs the show; Alexander/Alex pitches Skip around 09:00–16:15. Skip's campaign sizes, pricing, revenue and workload claims belong to that separate promotional segment. Chat requests for demos are not verified sales or completed meetings.
- **The market advice is conditional.** At 17:00–20:00 Peep discusses bootstrappers facing entrenched categories, while allowing disruption and competitive entry into successful niches. At 33:00–34:10 he accepts overlap with larger competitors when a distinctive initial offer creates entry. At 42:25–43:05 he allows capital-intensive models to need venture funding.
- **Small samples provide learning, not automatic certainty.** The five-person/80% and ten-person/95% claims at 45:00–46:05 are Peep's unverified extrapolation from cited UX research. They do not establish universal messaging-research coverage. His later 15-prospect suggestion and the host's five-person starting point are recommendations, not study results.
- **Preserve the correction of expert taste.** At 52:00–54:10 Pete admires a benefit-led homepage; Peep challenges that approach and says their opinions cannot replace feedback from the actual ICP. The hub does not present the host's favorite example as a validated template or adopt Peep's benefit-first objection as an absolute rule.
- **Message response is an intermediate signal.** At 45:00–47:10 Peep separates interest in a promise from the payment and retention needed for product-market fit. Wynter's roughly two-year path to breakeven at 31:45–32:45 also contradicts an implication of effortless profitability.
- **Guest support figures have a denominator ambiguity.** Peep says Fin solved 90% of “those inquiries” after describing routine questions making up about 80% of CXL's queue (06:00–06:45). Do not silently convert this into 90% of every support request or into RB2B performance.
- **The financing exchange contains unresolved assertions.** Around 40:00–41:35 Adam and Peep disagree about preferred stock and investor protection. Their categorical claims about flat growth, founder stakes, dilution and success probabilities were not verified. The hub uses decision conditions rather than presenting those claims as financing guidance.
- **Adam metrics are not silently reconciled here.** The 258 requests/59 escalations/approximately half later resolved arithmetic does not exactly support the stated 85%; sales-error categories may overlap; later RB2B $5M/$6M baselines are inconsistent; $12–15M remains an aspiration. Shared support and human follow-up qualify automation/headcount slogans. These remain detailed-note/proof-ledger concerns, not guest-playbook results.

## Extension: six additional full notes, selected raw checks

Reviewed **all six structured notes in full (29,295 words)** for selection ranks 28–33, including learnings, backstory, metrics, corrections, reusable topics and coverage. This is a different review depth from the independent full-transcript reading of the original three videos above. For these six, consequential distinctive lessons were checked directly against the raw ranges below; no claim is made to have independently reread every raw line. Truncated displays were completed with separate reads of the omitted sections. Notes 31–33 became available during source review and were all compared before filing. No extraction process was restarted or duplicated.

| Full structured note | Published | Note words | Direct raw passage checks |
| --- | --- | --- | --- |
| [[strategy/video-notes/EdDAHrvBDPM|Understory / EdDAHrvBDPM]] | 2025-08-29 | 4,814 | [[raw/sources/2026-09-08-youtube/videos/EdDAHrvBDPM/EdDAHrvBDPM|06:39–09:30; 14:14–15:14; 20:55–28:55; 46:35–53:05]] |
| [[strategy/video-notes/D-8umeDdYP0|Warmly / D-8umeDdYP0]] | 2025-08-22 | 5,303 | [[raw/sources/2026-09-08-youtube/videos/D-8umeDdYP0/D-8umeDdYP0|35:20–39:55; 52:30–56:00]] |
| [[strategy/video-notes/g9mejr_-odc|Kyle Coleman / g9mejr_-odc]] | 2025-08-15 | 4,467 | [[raw/sources/2026-09-08-youtube/videos/g9mejr_-odc/g9mejr_-odc|14:00–24:30; 27:50–28:45; 37:20–42:20; 46:45–52:20]] |
| [[strategy/video-notes/ScY0k43N1u8|SecurityPal / ScY0k43N1u8]] | 2025-08-08 | 5,679 | [[raw/sources/2026-09-08-youtube/videos/ScY0k43N1u8/ScY0k43N1u8|19:19–23:56; 25:32–27:10; 41:13–45:27]] |
| [[strategy/video-notes/CqlO3vkU_zo|Rivo / CqlO3vkU_zo]] | 2025-08-07 | 4,091 | [[raw/sources/2026-09-08-youtube/videos/CqlO3vkU_zo/CqlO3vkU_zo|02:40–03:50; 06:45–13:05; 17:15–20:16; 21:10–22:12; 32:55–34:45; 37:20–39:35]] |
| [[strategy/video-notes/jZ4o_B2g5bo|Irina Novoselsky / jZ4o_B2g5bo]] | 2025-08-02 | 4,941 | [[raw/sources/2026-09-08-youtube/videos/jZ4o_B2g5bo/jZ4o_B2g5bo|08:13–12:17; 24:14–28:50; 37:20–39:25; 45:48–46:50; 48:00–50:48]] |

Each note's recorded input SHA-256 matches its raw Markdown file. The table links the promoted durable copies in `strategy/video-notes/`. The following fingerprints identify the full research Markdown notes actually examined in `research/youtube-video-notes/`, in the table's order:

```text
EdDAHrvBDPM  9f38a76da0f14f72f463c0098eeda279dd76335dd775967cf2ae0c7ea55b7293
D-8umeDdYP0  365088535661e30d147ec4cf5920968474d8df2ab837625a80555aeab2245149
g9mejr_-odc  428b5e3e46cd34596885e7767dc17eccfa09e05d20c93d6abb0e0a1b1f99bc67
ScY0k43N1u8  17744283f1928d572d8de711e9835f606477ae8f0b737a42404533a029c51a48
CqlO3vkU_zo  f53abe2258a61d6566d8f7d51e5adb4e0cc662af81d22878185852b39cbab123
jZ4o_B2g5bo  4746a69f4bf1ab2e22fb893b162da0f61d94b38b24f721f957ccfd615bf4ffe8
```

### Understory: objectives and experiments

The agency/host episode explicitly excludes Adam as a speaker. The new hub avoids duplicating the historical persona-ranking interpretation already in [[audience/ideal-follower]]. Its distinctive additions are matching audience/creative/destination, distinguishing visibility from acquisition, and testing disputed copy with controlled variables. The raw record confirms that current Meta competitor creatives ran broadly while some more specific targeting and destination ideas were proposals. Customer inclusion in Meta and exclusion advice for acquisition remarketing are not reconciled in the panel. Early YouTube viewing depth supplies no acquisition-cost or revenue proof. Sam's technical-language counterexample changes Alex's recommendation into a test; the campaign was unlaunched. The 500–1,000-contact and four-variant advice lacks per-variant allocation or statistical assumptions.

### Warmly: a pending fork and a complementary product

Max explicitly describes a future choice between Series B growth and profitability, not an achieved reversal. His hiring and metric choices follow that prospective financing path. The source confirms that broader sales-led scope brings integration, services and stakeholder work, while RB2B can supply a component in Warmly's offering. Packaging with an opt-out does not prove adoption or incremental revenue. Metadata's exact ARR comparison should not replace the more ambiguous spoken figures; deal sizes are not explicitly annual contract values. This extension does not duplicate the limited-funding/ambition interpretation already in [[identity/values]], or transfer any guest financial claim into Adam's proof.

### Kyle Coleman: scope and permission within the method

The checked source explicitly separates labor-intensive cold executive outreach from PLG usage/paywall signals. Peer research remains a conversation and may include a small incentive; at 23:45–24:00 Kyle asks permission to use the contributor's name. This qualification is preserved in the hub. His efficiency claims, phone multipliers and quota examples lack comparable cost/outcome evidence. Training is about earning a conversation and questions, not a mandatory joke or script. The AI section distinguishes a defined process from accessible business context, with Pete's transcript archive remaining Pete's own workflow. Adam's coaching passage is already handled in [[identity/values]]. AI-calling and cold-texting legal assertions, voicemail product availability, and the healthcare pitch's tax/savings claims were not validated or promoted as instructions.

### SecurityPal: work completed, humans retained, round corrected

The customer forwards a blank questionnaire and receives a completed one; the value is completion rather than a new login. The raw source explicitly retains expert checks against invented policies and personnel, so this is not an all-AI operating model. Volume-based qualification and behavioral validation are guest advice, not measured universal thresholds. Pukar's strongest dismissal of certification objections is qualified by his acknowledgment of changed conditions and later certification; the hub does not recommend bypassing buyer requirements. At 42:04–42:21 he corrects the financing to **Series A**, while the title/intro supply differing $20M/$21M amounts and an uncorroborated “100 VCs” count. The cash-cycle examples are illustrative and each specific term pair yields 15 days; cash-flow timing cannot establish accounting profitability. Guest/company logos, questionnaire buyers and Adam's illustrative Samsung scenario are separate categories. The pro-VC → anti-VC → contextual-capital evolution in the structured note belongs to Pukar, not Adam.

### Rivo: target versus measured automation

At 02:43–03:49 Stuart says they are moving toward agent-written code and describes human specification, agent work, AI review and final human review. The **80% headline is a target/operating heuristic**, not a measured share of all engineering labor. Preparation includes repository cleanup, conventions, analogous files and checks. His strongest results explicitly concern recurring Shopify work; novel zero-to-one execution remains qualified. The help-article workflow uses code context and an instruction to omit internals; no confidentiality test was supplied. Auto-merging applies specifically to documentation after repeated review, not all production code. Ticket quality checks are being built and direct routing remains future work. Contribution counts, speed claims and hypothetical time saved are different, weakly specified metrics. The recording begins mid-conversation; principal guest Stuart is identified contextually, without a secure surname here. No staff-action claim or AI-employment mandate is imported into Adam's values.

### Irina: creator control, useful reactions and attribution

The raw record supports spontaneous executive-originated video plus production assistance, rather than total outsourcing. Irina differentiates help with comment wording from unattended relationship automation. Her 70/30 ratio has no defined unit, the seven-to-twelve exposure count is unsupported, and the nine-to-one value/ask ratio is a heuristic. Her corrected **37% social-touch** claim establishes reported overlap, not the host's stronger lead-origination interpretation. Employee personal brands are supported through development opportunities; this does not fully answer the host's separate question about acquisition dependence on a founder. Her mental replacement-CEO exercise is not an actual firing, and “cut my ELT in half” follows a discussion of meeting length, so it cannot establish layoffs. Product-content advice is qualified by customer explanations and demonstrations; no categorical ban on product updates is filed. Formatting/algorithm claims, DM/email comparisons, social-research statistics and claims about other AI tools' stale data remain unverified and time-sensitive. None becomes Adam's voice rules, cadence or public-content approval.

## Filing and limits

Created and later extended only [[strategy/guest-playbooks]] and this audit; no child pages were needed. No raw source, extraction provenance, identity/proof, voice, index or log was edited for these guest tasks. The parent integrator owns navigation and final index refresh. All sources are public automatic captions, with no audio/screen verification and no confirmed recording dates. Speaker assignment follows conversational context; uncertain brief interjections are not used to establish ownership of a lesson. The hub is a draft research aid, not approved first-person public copy or a current vendor implementation guide.

## Related Pages

- [[strategy/guest-playbooks]]
- [[strategy/source-policy]]
- [[strategy/video-notes/atzcNzDIsgg]]
- [[strategy/video-notes/gOvQngBqw80]]
- [[strategy/video-notes/d_rVwh521po]]

## Source Notes

Full local caption archives listed in the table above provide the primary evidence. Archived platform descriptions establish title/name spellings and their promotional framing. Generated notes were secondary cross-checks only. No external verification, outreach or publication was performed for this bounded task.
