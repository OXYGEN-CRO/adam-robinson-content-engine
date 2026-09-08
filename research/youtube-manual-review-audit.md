---
type: research
status: draft
owner: adam
created: 2026-09-08
updated: 2026-09-08
sources: [scripts/verify_youtube_manual_reviews.py, research/youtube-manual-review-audit.json, research/youtube-manual-review-audit.tests.json, research/youtube-synthesis-audit.json, research/youtube-coverage-reviews.json]
tags: [audit, youtube, manual-review, provenance]
---

# Manual review reconciliation

The [new checker](../scripts/verify_youtube_manual_reviews.py) confirms that **all three current automatic flags have matching, valid review records**. It preserves the automatic flags and structural errors instead of deleting or overwriting them.

The final all-100 reconciliation at 2026-09-08T10:35:18.817813+00:00 returned **exit 0**: all **100 extracted, promoted and structurally valid notes**, **zero structural errors**, and **three reviewed coverage flags**. The primary checker keeps those three heuristics visible and returns exit 2; the reconciliation confirms their source-bound reviews without suppressing them.

The earlier September 8, 09:58 UTC validation run returned exit 2 against an 80-note snapshot with 22 missing-artifact/aggregate error records. That historical result tested the distinction between reviewed flags and overall completion; the linked machine reports now describe the final all-100 run.

| Flag | Matched evidence |
| --- | --- |
| `D-8umeDdYP0` — `large_lesson_anchor_gap` | Exact automatic gap 0.719–739.5 seconds lies wholly inside the recorded full-read interval 0–800 seconds; timestamped evidence treatments are present. |
| `wYFjORZCtug` — `thin_claim` | Exact detail matches `metrics_and_dates.1`, its original text and 02:41–02:54 anchor; read interval is 0–190 seconds. |
| `Y63QI4BKEcg` — `thin_claim` | Exact detail matches `metrics_and_dates.11`, its original text and 36:13–36:20 anchor; read interval is 2143–2210 seconds. |

The checker validates canonical selected source/note paths, complete file-byte SHA-256 hashes, automatic-snapshot source and normalized-note hashes, unique current-flag matches, claim paths/text, reviewed interval coverage, timestamped evidence, and nonempty reviewer/finding/reason/limits. It recognizes the explicitly recorded `reviewed_no_material_gap` finding; an unsupported or unresolved disposition fails. It also rejects inputs that change during the run.

Run after refreshing the automatic audit:

```sh
python3 scripts/verify_youtube_manual_reviews.py
```

Exit **0** means valid current reviews and an automatic snapshot reporting all 100 complete without structural errors. Exit **1** means missing, stale, mismatched or invalid manual-review/input evidence. Exit **2** means current reviews are valid but automatic completion or structural checks remain outstanding. Neither zero exit nor valid metadata certifies semantic truth, complete understanding or audio accuracy.

The [machine audit](youtube-manual-review-audit.json) preserves complete top-level automatic errors, per-note structural errors and original flags. The [disposable-test evidence](youtube-manual-review-audit.tests.json) records ten detected failure cases: stale source bytes, stale note bytes, new unreviewed flag, missing review, mismatched claim path, mismatched exact claim detail, altered flagged gap, incomplete read interval, empty evidence and incorrect canonical note path. Every negative case returned exit 1. The baseline retained the original structural errors exactly. Disposable fixtures were removed and all live inputs remained unchanged during testing.

Checked helper SHA-256: `099503d068ba9f0a9398b8d74c3867b86490849baa49c16f7361a3c650d5ca50`. Input hashes are retained in each machine report, allowing later refreshed automatic snapshots to be distinguished. Final wiki lint passed with 136 context pages.

## Source Notes

The human findings remain in `research/youtube-coverage-reviews.json`; this helper verifies their recorded scope and binding to current artifacts, not their substantive correctness. No original automatic audit, manual-review registry, raw source, model output, existing script, index, log or running extraction process was modified by this task. The result complements the primary all-100 verifier and never overrides its errors or terminal-output checks.

## Related Pages

- [[research/README]]
- [[index]]
