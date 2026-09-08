---
title: Cross-source repeated outro attribution audit
status: draft
updated: 2026-09-08
---

# Cross-source repeated outro attribution audit

The bounded scan found **117 directed matching pairs across 45 video endings**. One additional consequential boundary error was confirmed in the original `EqXag_z2OpQ` extraction: it treated an appended PLG montage as the continuation of Adam's financing answer. **The parent applied the reviewed clarification while this audit ran.** The previously confirmed Jesse and Sam misattributions were already handled; no further consequential attribution errors were found in the ending claims examined.

Most other guest inserts were already marked separate or uncertain by their original notes. Repeated text is evidence of reuse, not independent corroboration, an additional metric observation, or proof that the preceding guest said it.

## Method and coverage

All **100 selected transcript JSON files** were scanned. For each video, the candidate window begins 60 seconds before its final caption start. Text was lowercased, curly apostrophes normalized, and tokenized as alphanumeric words with internal apostrophes. Twelve-word shingles from those windows were matched against every other selected full transcript; consecutive matches at the same token offset were merged into exact runs. Same-video matches were excluded. The longest match was 187 words in a known support clip.

The supporting [JSON audit](audit-repeated-outros.json) records all 100 source paths, dates, transcript/Markdown/info hashes, candidate runs, exact token and segment indices, timestamp ranges, and normalized matched text. It also records hashes of the **44 available original candidate notes** and their provenance files, plus the directly examined raw passage ranges. The original structured note for rank 86, `fg4kNYt38FM`, was unavailable at this review snapshot; its raw ending was inspected. No extraction was rerun.

Direct review concentrated on the final 90 seconds of ranks 54, 56, and 57–76, the relevant original interview passages, and the older Eric interview. The known July 2025 support clips and short repeated Adam promotional wording were screened separately. Ending claims in the available original notes were checked; this was not a second full reading of 100 transcripts or of every note.

Exact matching can miss paraphrases, caption differences that interrupt every 12-word sequence, inserts before the final minute, and material outside the selected archive. Contextual speaker attribution is based on captions and conversational handoffs; audio and video were not inspected. Unknown turns remain unknown.

## Confirmed additional defect — clarification applied

In [[raw/sources/2026-09-08-youtube/videos/EqXag_z2OpQ/EqXag_z2OpQ|the keynote/Q&A, published 2025-03-21]], Adam's financing answer finishes around **56:14**. The **56:14.48–56:33.32** tail repeats the opening montage of [[raw/sources/2026-09-08-youtube/videos/pcG_402qsp0/pcG_402qsp0|the Wes Bush interview, published 2025-03-05]], **00:00.12–00:21.04**. A caption event straddles the edit, so 56:14 is an approximate boundary rather than an audiovisual cut measurement.

The reference interview supplies the separate contexts: host newsletter remarks at **01:59.52–02:17.88**; Pete's PLG suitability question at **07:48.84–08:06.08**; Adam's qualification that an existing relevant organic audience makes freemium PLG more attractive at **13:36.68–14:20.36**; and Wes's scaling argument at **06:48.16–07:13.20**. Thus the appended material is an edited, mixed-speaker PLG teaser, not the conclusion of one financing argument. The valid financing lesson remains intact.

Exact affected original fields:

| Original JSON field | Original problematic statement | Reviewed disposition |
| --- | --- | --- |
| `$.key_learnings[31].caveat` | “The final comparison about existing organic distribution and a self-selling product ends mid-discussion.” | Parent clarified that financing ends around 56:14 and the appended montage is not evidence for that lesson. |
| `$.tensions_and_corrections[20]` | “The supplied transcript ends at 00:56:33 during an unfinished comparison about startup models, existing organic audiences and products that sell themselves.” | Parent identified the separate reused PLG montage. |
| `$.coverage.limitations[0]` | Describes the reviewed ending as the “final financing discussion.” | Parent clarified that the final material also includes a separate montage. |
| `$.coverage.limitations[2]` | Says the final supplied text “ends mid-discussion.” | Parent clarified that the last caption belongs to the truncated promotional montage. |

The original broad `$.key_learnings[31].end_timestamp` of **00:56:33** was deliberately retained in the reviewed note; the corrected caveat bounds its evidentiary use. Original model JSON and provenance remain unchanged. Parent reported this correction applied to the reviewed registry/durable note; it is not an outstanding action.

Evidence hashes:

- SHA-256 `27a4f0a08ae5a880ba66ba941a7a3fef50ef362d9eb213770fd01b363d84da68`: transcript of the keynote.
- Wes interview transcript: `8e8ee224cccec6acebf69defc99b6247a65511d5ff86cd72982b2af99fa2c390`.
- SHA-256 `15744457fd79995e2b07f8b8db6140df6d345484668653458b0cf93869e5f1be`: original extraction JSON for the keynote.

## Reused guest-teaser families

| Family and comparison reference | Appended appearances examined | Attribution finding and original-note outcome |
| --- | --- | --- |
| **Inbox before subject lines.** [[raw/sources/2026-09-08-youtube/videos/3wjL3IATsyg/3wjL3IATsyg|Andy Mewborn, 2025-03-31]]: edited opening **00:00–00:26**; main passages **04:12–05:02** and **22:51–23:22**. | Jesse `RK1Kk1h783c` **52:53–53:18** (May 5); Andy excerpt `-4-S3d65UB8` **18:00–18:24** (Apr 30); Ryan `ZaR-0Iqp7vY` **53:11–53:35** (Apr 27); Tom `M0VvUsyJQ-M` **53:01–53:26** (Apr 23); Adam presentation `wYFjORZCtug` **48:02–48:26** (Apr 11); Alec `yMNyVxr4IAo` **52:24–52:50** (Apr 9). | Material comes from the Andy interview, assembled from separate passages. Andy supplies the substantive email-priority framework; brief host interjections require turn-level care. Jesse's original assignment was already corrected by the parent. The Andy excerpt says likely Andy; the other four originals keep the speaker uncertain/separate. No additional correction needed. |
| **Quickest awareness / public figures' travel / why companies fail.** [[raw/sources/2026-09-08-youtube/videos/JZiUalL7h-8/JZiUalL7h-8|Documentary compilation, 2025-03-14]]: opening **00:01–00:21**, separate main scenes **01:20:28–01:20:50** and **02:01:13–02:01:29**. | Patrick `lF2axpN3mic` **54:22–54:39** (Apr 7); Sam Parr `OGLC5ceoQ5w` **56:19–56:37** (Apr 4); Andy `3wjL3IATsyg` **53:25–53:42** (Mar 31). | These are documentary fragments, not conclusions from Patrick, Sam, or Andy. The public-figure and company-failure lines come from different scenes; the short opening awareness question was not independently diarized. All three notes safely withhold a complete attributed lesson. |
| **PLG / existing organic audience.** [[raw/sources/2026-09-08-youtube/videos/pcG_402qsp0/pcG_402qsp0|Wes Bush, 2025-03-05]], opening **00:00–00:21** and separate passages detailed above. | Santos/Amit `yJ6C1urpnws` **57:14–57:34** (Mar 25); keynote `EqXag_z2OpQ` **56:14–56:33** (Mar 21); Aye Moah `7p-QD-3MtBw` **55:26–55:43** (Mar 18). | Mixed-speaker montage. The keynote boundary error was corrected. The other two originals already flag the ending as separate/uncertain. Adam's absence from the main Santos/Amit interview remains true; reused footage is a separate context. |
| **Show up to solve / prioritize reachable revenue opportunities.** [[raw/sources/2026-09-08-youtube/videos/Y63QI4BKEcg/Y63QI4BKEcg|Sam McKenna, 2025-02-26]]: opening **00:00–00:29**, main passages **24:04–24:33** and **51:31–52:00**. | Documentary `JZiUalL7h-8` **02:29:15–02:29:35** (Mar 14); Brenden `MUQ4f6DkmsA` **57:19–57:37** (Mar 12); Jessica `b2L2rX26a6A` **01:00:13–01:00:32** (Mar 7); Wes `pcG_402qsp0` **48:57–49:19** (Mar 5). | The main passages establish Sam's sales advice: choose relevant advocates/referrals within limited sales capacity, and teach to build trust. This does not establish that Adam prioritizes revenue above other values, or that Sam makes such a universal life claim. All four originals already mark an uncertain/separate montage; no consequential misattribution to correct. |
| **841 comments / roughly 500 likes.** [[raw/sources/2026-09-08-youtube/videos/89Jl-njDguM/89Jl-njDguM|Eric Siu re-edit, 2025-02-28]] **34:23–34:44**, also [[raw/sources/2026-09-08-youtube/videos/fg4kNYt38FM/fg4kNYt38FM|Eric interview, 2024-11-20]] **35:09–35:29**. | Lolita `WLounenLFDg` **59:33–59:49** (Mar 10); Sam `Y63QI4BKEcg` **56:53–57:10** (Feb 26); Adam workshop `23rVr8tozS8` **58:26–58:43** (Feb 22). Eric's Feb 28 re-edit also repeats its own anecdote at **53:14–53:31**. | Eric addresses Adam and jokes about calling himself Eric Robinson; surrounding context ties the post to his ABM discussion. The Sam assignment was already corrected. Lolita/workshop notes correctly keep the metric separate from Adam and their preceding speaker. Eric's own recap is not an attribution error. The November release demonstrates why a later re-edit date must not become a new post-performance date. |

All table dates are publication dates of the archived versions, not verified recording dates. The supporting JSON maps every ID to its exact source path, publication timestamp, matching ranges, and hashes.

## Controls and remaining uncertainty

- July 30 support clips, ranks 34–43, match the same underlying `C7n2q31PPh4` discussion. This known repurposing does not make an original guest/unknown-speaker label erroneous by itself.
- Vaibhav's two versions (`o-ulfe0ZzVE`, May 16, and `p2dDw0Dy1VM`, May 13) repeat the same sign-off and Nathan Barry preview. Their notes keep Nathan's $45 million ARR characterization as a third-party host claim.
- The November Eric video's matching tail is the ordinary interview sign-off, not another guest inserted after it. Its original structured note was still pending, so no note-level conclusion is asserted for that source.
- Short matches among Adam's own videos, mostly promotional phrasing and reused instruction, did not reveal a different-guest attribution error in the ending claims examined. They should still not be treated as independent corroboration of figures.
- Whole-montage speaker identity should not be inferred from one matched sentence. The documentary's initial awareness question and brief interjections remain uncertain. Exact cut locations can straddle caption events.

## Source Notes

This audit follows [[strategy/source-policy]] and preserves the distinction between raw evidence, original extraction output, and reviewed durable notes. Only this Markdown audit and its supporting JSON were created or changed. Raw sources, model outputs, notes, provenance, scripts, registry, index/log, QMD, and the central reader were not modified by this audit task.

Final verification passed: **432 source/note/provenance hashes**, all **9 local wiki links**, candidate counts, and `git diff --check` for the two audit artifacts.
