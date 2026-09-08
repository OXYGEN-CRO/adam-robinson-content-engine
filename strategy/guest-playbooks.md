---
type: context
status: draft
owner: adam
created: 2026-09-08
updated: 2026-09-08
sources: [raw/sources/2026-09-08-youtube/videos/atzcNzDIsgg/atzcNzDIsgg.md, raw/sources/2026-09-08-youtube/videos/gOvQngBqw80/gOvQngBqw80.md, raw/sources/2026-09-08-youtube/videos/d_rVwh521po/d_rVwh521po.md, raw/sources/2026-09-08-youtube/videos/EdDAHrvBDPM/EdDAHrvBDPM.md, raw/sources/2026-09-08-youtube/videos/D-8umeDdYP0/D-8umeDdYP0.md, raw/sources/2026-09-08-youtube/videos/g9mejr_-odc/g9mejr_-odc.md, raw/sources/2026-09-08-youtube/videos/ScY0k43N1u8/ScY0k43N1u8.md, raw/sources/2026-09-08-youtube/videos/CqlO3vkU_zo/CqlO3vkU_zo.md, raw/sources/2026-09-08-youtube/videos/jZ4o_B2g5bo/jZ4o_B2g5bo.md, research/audit-guest-playbooks.md]
tags: [guest-playbooks, attribution, messaging, prototyping, founder-decisions]
---

# Guest playbooks

## Scope and starting points

Practical lessons from nine guest sessions published August 2–September 19, 2025. Three transcripts were independently read in full; six additional full structured notes were reviewed with direct checks of consequential raw passages. The [[research/audit-guest-playbooks|audit]] records that distinction. These workflows are editorial summaries of named speakers' advice. Guest experiences, results and host commentary establish no Adam personal proof or writing voice. For his more recent direction, use [[strategy/learnings]], [[strategy/pillars]] and [[identity/proof]], where recent relevant LinkedIn statements take precedence.

| Need | Guest and source date | Detailed source note |
| --- | --- | --- |
| Find a defensible niche and test its message | Peep Laja, Wynter — 2025-09-08 | [[strategy/video-notes/d_rVwh521po]] |
| Turn a familiar workflow into an API-backed prototype | Jesse Ouellette, LeadMagic — 2025-09-11; hosted by Pete | [[strategy/video-notes/atzcNzDIsgg]] |
| Evaluate capital, an exit or an adjacent business | Josh Abramson — 2025-09-19; with Adam and a co-host | [[strategy/video-notes/gOvQngBqw80]] |
| Design paid campaigns and interpretable copy tests | Understory / Pete — 2025-08-29; Adam absent | [[strategy/video-notes/EdDAHrvBDPM|Full note]] |
| Connect capital, product scope and partnerships | Max Greenwald, Warmly — 2025-08-22 | [[strategy/video-notes/D-8umeDdYP0|Full note]] |
| Research executive buyers and define AI work | Kyle Coleman, ClickUp — 2025-08-15 | [[strategy/video-notes/g9mejr_-odc|Full note]] |
| Deliver completed work and improve cash discipline | Pukar Hamal, SecurityPal — 2025-08-08 | [[strategy/video-notes/ScY0k43N1u8|Full note]] |
| Prepare an existing codebase for agent work | Stuart, Rivo — 2025-08-07 | [[strategy/video-notes/CqlO3vkU_zo|Full note]] |
| Build executive and employee social participation | Irina Novoselsky, Hootsuite — 2025-08-02 | [[strategy/video-notes/jZ4o_B2g5bo|Full note]] |

## Peep Laja: niche selection and message testing

1. **Identify why this particular business can win.** Peep favors an underserved part of a real market where a smaller business can prosper without requiring an incumbent's growth rate. Feature parity alone is a weak reason to switch from an established leader. His caveat matters: disruption can change market positions, and successful niches can attract larger competitors. This is a market-selection hypothesis, not protection from competition. [September 8, 17:00–20:00][P]

2. **Turn domain experience into a testable customer hypothesis.** Peep started with uncertainty about whether CXL's sales copy resonated, found others with the problem, interviewed them, and tested who would pay. His initial hypotheses were wrong; Wynter took approximately two years of experiments and small pivots to break even, funded by other business profits. Existing pain starts discovery; it does not complete it. [September 8, 29:00–34:10][P]

3. **Test the promise before committing substantial development work.** Put a concrete value proposition in front of intended buyers. Separate whether they understand it, whether they want it, and what remains unclear. Interest and follow-up questions justify another validation step. Peep explicitly distinguishes this message response from product-market fit, which requires payment and retention. [September 8, 45:00–47:10 and 48:40–49:15][P]

4. **Recruit candid prospects and shorten the feedback cycle.** His manual alternative to Wynter is to recruit around 15 relevant prospects who are neither customers nor familiar with the brand, use an independent interviewer or survey to reduce courtesy bias, and compensate participants for their time. Repeat feedback and revision quickly. The co-host later suggests starting with five; neither count is a universal statistical requirement. [September 8, 54:20–57:58][P]

5. **Establish both clarity and a reason to choose you.** Peep asks whether the buyer can explain the difference from the familiar category leader. Co-host Pete adds that a non-specialist buying-committee member must understand the homepage too. When Pete praises another company's benefit-led hero, Peep challenges the example: the target buyer's response should decide, rather than either expert's taste. Treat benefit-first copy as something to test, not an approved formula. [September 8, 50:00–54:10][P]

**Separate operational example:** Peep describes classifying CXL's support questions, automating repetitive requests with Fin, and retaining one human for exceptions. The transferable workflow is to inspect the actual queue and preserve an escalation route. His staffing and resolution numbers belong to CXL and remain guest self-reports. [September 8, 06:00–06:45][P]

## Jesse Ouellette: prototype a narrow operational tool

1. **Choose one useful function for one known user.** Jesse recommends starting inside an agency or business whose workflow the builder understands. LeadMagic began with an agency portal and email validation, then favored data services over another experiment in campaign analytics. That sequence offers a bounded first project, rather than a requirement to recreate a complete incumbent product. [September 11, 20:30–21:10, 35:35–36:15 and 42:35–45:35][J]

2. **Specify the data and behavior before generating the interface.** His champion tracker uses a documented API, a watch list and distinct outcomes such as changed jobs, no change, or never worked at the submitted employer. He gives a model the API information and design intent to expand into a build specification; a sample API response makes the intended data concrete. [September 11, 03:05–08:18, 09:55–11:15 and 25:15–27:00][J]

3. **Separate the visual prototype from working integrations.** After live failures, Jesse recommends first settling the interface with sample data, then integrating authentication, storage and APIs. He identifies these as points where an experienced developer may be needed. Pete stresses architecture knowledge and suggests beginners start with a simple interactive document. [September 11, 13:45–17:05 and 40:35–44:30][J]

4. **Change the debugging process when repeated prompts stop helping.** Jesse exports to GitHub, opens the repository in Cursor and initially uses Ask mode to diagnose without changing code. He then applies repairs to the broken behavior. The demo encounters database, authentication and interaction defects; the claim that the tool fixed everything is not a demonstrated exhaustive test. [September 11, 36:15–40:15 and 52:25–56:35][J]

5. **Use internal tools to answer a narrow operating question.** His separate LinkedIn listening dashboard tracks company mentions, distinguishes partners and competitors, and connects the findings with existing internal data. The potential use is to inspect discussion and respond to relevant mentions. He speculates about selling it; neither sales nor measured lift is established. Likewise, recurring champion monitoring still requires scheduled API checks. [September 11, 30:20–32:20 and 50:25–53:40][J]

**Release boundary:** the session demonstrates a prototype and repairs. Later billing, launch and an immediate subscription are discussed hypothetically. The promotional title/description does not prove a revenue-generating commercial launch. Tool choices and cost claims describe September 2025, not current implementation instructions. [September 11, 56:35–58:30][J]

## Josh Abramson: decisions about capital and the next business

- **Compare the founder's acceptable outcomes with the capital provider's.** Josh contrasts an individual's concentrated risk with an investor's portfolio. A profitable business that stops growing may still satisfy its owner while missing a fund's goals. His anonymous rejected-acquisition stories illustrate the concern but do not establish probabilities or a general rule that venture funding ends badly. [September 19, 06:00–10:15 and 33:00–35:15][A]

- **Include control and daily work in the sale decision.** Josh describes a majority sale that created personal liquidity while leaving a large retained stake and reduced autonomy. He recommends considering what meaningful work and collaboration would remain afterward. His later account is mixed: he values opportunities the transaction created and says he does not regret the overall sale. This is a decision prompt, not advice that every founder should keep a business. [September 19, 14:30–19:10, 24:00–29:30 and 42:20–44:00][A]

- **Examine whether one venture can consume another's cash.** In Josh's account, Vimeo's uncertain monetization and funding needs competed with the cash-generating business inside the same ownership structure. He considers separate outside financing a possible way to reduce that exposure, but says the actual deal constrained it. This qualifies a simple anti-VC reading of the episode; the alternative was a counterfactual, not an executed solution. [September 19, 43:40–46:20][A]

- **Inventory existing advantages before starting an adjacent company.** Josh traces the t-shirt business to CollegeHumor's audience, Vimeo to an existing team, and TeePublic to Busted Tees. Distribution, collaborators and operating infrastructure can support experiments. He also acknowledges that starting from a standstill and buying a good business are both difficult, and his old sectors have become harder. An adjacent launch is not automatically easy or attractive. [September 19, 50:55–54:50][A]

## Understory: paid distribution and disciplined tests

- **Carry the buyer's question through the whole campaign.** The agency repurposed strong organic posts into persona groups. Chris Chambers recommends aligning the audience, specific comparison or feature creative, and destination page. The described YouTube activity was remarketing; cold prospecting and some competitor-specific refinements were still proposals. Organic performance and video views do not prove profitable acquisition. [August 29, 06:39–08:30 and 21:26–28:30][U]
- **Resolve audience exclusions through the campaign's purpose.** Ali reports including customers in Meta ads to maintain visibility; Chris recommends excluding them from acquisition remarketing. The panel leaves the difference unresolved. Do not extract a universal customer-inclusion rule or assume the recommendation describes the deployed configuration. [August 29, 14:14–15:14 and 27:29–27:55][U]
- **Test a disputed message, with the variable chosen first.** Alex Fine initially favors buyer consequences over deliverability jargon; Super Send's Sam counters that operational terminology can identify a real pain. Alex then recommends testing both. Separate hook, CTA and body experiments so the result remains interpretable. His sample-size and short-email rules are agency heuristics; the reviewed campaign had not launched. [August 29, 46:39–53:00][U]

## Max Greenwald: connect financing to operating choices

- **Make the next capital decision an explicit fork.** Max contrasts pursuing another round with tightening spending toward profitability. He connects the choice to required future scale, dilution, hiring and metrics. This was a pending Warmly decision, not a completed transition; his payout arithmetic is illustrative. His hypothetical preference for a limited initial raise is already qualified in [[identity/values]]. [August 22, 35:24–39:52 and 52:38–53:25][W]
- **Reconsider competition when customer needs diverge.** Warmly's larger contracts require integrations, services and sales involvement; Max describes packaging RB2B's narrower data service into that broader offer. The lesson is to inspect complementary buyer needs before treating overlap as a winner-takes-all contest. Default packaging, optional removal and an agency discount do not establish universal adoption or partnership revenue. [August 22, 38:12–39:52 and 54:19–55:51][W]

## Kyle Coleman: earn executive conversations

- **Research the person, persona and account before connecting the offer.** Kyle's executive-outbound method learns internal priorities through practitioner conversations, then approaches the decision-maker with relevant findings and customer proof. He explicitly asks permission to name a contributor. Start with a few accounts and evaluate against the deals needed; his examples supply no comparative acquisition-cost result. This is distinct from ClickUp's usage/paywall-triggered PLG outreach, which he also supports. [August 15, 14:00–16:28, 18:50–24:26 and 27:55–28:39][K]
- **Standardize the purpose of a call while allowing natural delivery.** Kyle wants a short explanation that earns permission to ask useful questions. Representatives can adapt words and tone they cannot say with conviction; his playful opener is not suitable for everyone. Pete connects that flexibility to a shared understanding of buyer, value and pain. [August 15, 37:11–42:15][K]
- **Define the outcome, process and context before delegating to AI.** Kyle starts with examples of good work, reverse-engineers the steps, and supplies organizational messaging and prior artifacts. Pete separately preserves client-call context for later questions. These are their workflows; neither establishes autonomous strategy or Adam's use of the same tools. [August 15, 46:47–48:05 and 49:57–52:18][K]

## Pukar Hamal: sell completed work and test real value

- **Remove the customer's work, not merely relocate it.** SecurityPal initially accepted an empty questionnaire and returned a completed document without a customer login. Pukar combines AI with expert verification because invented policies and follow-up questions still require accountability. Occasional requests may suit free tools; repeated questionnaire volume can justify paid fulfillment. The example does not establish a general exemption from security requirements. [August 8, 19:19–23:56][S]
- **Prefer behavior to polite buying promises.** Pukar looks for payment, expansion and actual introductions. He warns that “add one feature and I'll buy” can delay an honest rejection. Certification may matter in procurement, but cannot by itself repair weak customer demand; his own company later obtained it. [August 8, 25:32–27:06 and 41:13–42:04][S]
- **Adapt operating economics when capital conditions change.** Pukar describes responding to the 2022 downturn through larger upfront contracts and attention to collections. His examples show why payment timing deserves attention, not that cash-flow positivity equals profit. He explicitly corrects the introduction: his round was Series A, not seed; the title's profitability framing is not an audited result. [August 8, 42:04–42:21 and 44:17–45:27][S]

## Stuart at Rivo: prepare agents for repeatable engineering

- **Prepare the repository and constrain the assignment.** Stuart removes unused code, uses descriptive names, documents established patterns and supplies analogous files in a standard prompt. Completion requires tests, linting and integration checks. Humans specify and review; the spoken 10/80/10 allocation is an intended model, not measured automation of all engineering. Strongest results concern familiar Shopify patterns and integrations, with substantial preparation behind them. [August 7, 02:43–03:49, 06:48–13:06 and 32:56–34:41][R]
- **Use code context to maintain customer help, with an explicit publication boundary.** Rivo keeps help articles in the repository, assigns article-specific updates, and transfers changes through pull requests and an Intercom API. Stuart instructs the agent to omit implementation details. He later allows automatic merging for these documentation changes after reviewing many outputs; that exception is neither a rule for production code nor a confidentiality guarantee. [August 7, 17:15–21:58][R]
- **Improve incoming tickets before automating their execution.** Stuart is building checks that request missing context before engineering starts. Direct ticket-to-agent routing remains a later step. The useful distinction is between improving the input and claiming the entire downstream workflow already works. [August 7, 37:22–39:29][R]

## Irina Novoselsky: social participation that fits the person

- **Keep the substance personal while delegating packaging.** Irina moved from overedited writing to spontaneous videos between meetings, then added assistance with visuals and accompanying text. This fits her verbal strengths; it is not a video-first rule for every executive. [August 2, 08:13–12:17][I]
- **Choose relevant conversations and useful reactions.** She listens to a defined set of prospective customers, conferences and panels, contributes substantive comments, and favors reader learning or action over congratulations. AI can assist wording; she opposes unattended relationship-building. Her 70/30 activity split and repeated-exposure numbers are heuristics, while lead contact with social is not proven lead origination. [August 2, 24:14–28:47 and 45:48–46:45][I]
- **Make product content useful and let employees build their own presence.** Irina suggests customer explanations and problem-solving demonstrations, qualifying her earlier rejection of generic launch posts. Her nine-to-one value/ask rule is advice, not an optimized ratio. She also supports employees' portable brands and seeks retention through growth opportunities, rather than preventing public participation. These are her editorial and leadership choices. [August 2, 37:20–39:23 and 48:40–50:45][I]

## Related Pages

- [[strategy/youtube-library]]
- [[strategy/pillars/go-to-market]]
- [[strategy/pillars/saas-building]]
- [[strategy/pillars/bootstrapping-versus-vc]]
- [[strategy/source-policy]]
- [[research/audit-guest-playbooks]]

## Source Notes

Source dates above are publication dates; recording dates are not confirmed. All nine are public automatic-caption archives captured on 2026-09-08, with no audio verification or diarization. Archived video descriptions supply names where captions vary; Stuart's surname remains unestablished here. Public research access does not approve new public copy. No guest revenue, sale, staffing or customer claim has been transferred to Adam's proof or voice pages. Vendor, platform-algorithm and financing assertions remain dated source claims, not current implementation instructions.

[P]: ../raw/sources/2026-09-08-youtube/videos/d_rVwh521po/d_rVwh521po.md
[J]: ../raw/sources/2026-09-08-youtube/videos/atzcNzDIsgg/atzcNzDIsgg.md
[A]: ../raw/sources/2026-09-08-youtube/videos/gOvQngBqw80/gOvQngBqw80.md
[U]: ../raw/sources/2026-09-08-youtube/videos/EdDAHrvBDPM/EdDAHrvBDPM.md
[W]: ../raw/sources/2026-09-08-youtube/videos/D-8umeDdYP0/D-8umeDdYP0.md
[K]: ../raw/sources/2026-09-08-youtube/videos/g9mejr_-odc/g9mejr_-odc.md
[S]: ../raw/sources/2026-09-08-youtube/videos/ScY0k43N1u8/ScY0k43N1u8.md
[R]: ../raw/sources/2026-09-08-youtube/videos/CqlO3vkU_zo/CqlO3vkU_zo.md
[I]: ../raw/sources/2026-09-08-youtube/videos/jZ4o_B2g5bo/jZ4o_B2g5bo.md
