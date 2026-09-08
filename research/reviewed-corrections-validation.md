---
type: research
status: draft
owner: adam
created: 2026-09-08
updated: 2026-09-08
sources: [scripts/synthesize_youtube.py, scripts/verify_youtube_synthesis.py, research/youtube-note-corrections.json, research/reviewed-corrections-validation.json, research/reviewed-corrections-validation.retest.json]
tags: [audit, youtube, corrections, provenance, validation]
---

# Reviewed correction validation

## Result

**Latest result: both identified gaps are fixed and the bounded retest passes.** The initial nine corrections were valid and all six affected promoted notes matched the declared derivative exactly. The initial disposable tests exposed two verifier weaknesses; the preserved findings below concern that earlier code, and the follow-up section records the corrected versions and results.

Machine evidence: [reviewed-corrections-validation.json](reviewed-corrections-validation.json). Reproducible local fixture runner: [run_validation.py](../output/reviewed-corrections-validation/run_validation.py). The runner imports copied scripts without invoking `main()` or `work()`, applies mutations only to disposable copies, and removes its fixture directory. No model jobs were started.

The examined versions are bound by these SHA-256 hashes:

| File | SHA-256 |
| --- | --- |
| `scripts/synthesize_youtube.py` | `58ed45e6bade37e355906e078cb43dac7c7f4e5f2560909b5a6c58a86f6ac2e9` |
| `scripts/verify_youtube_synthesis.py` | `ddbd05510120ab994ad1ec104833ba85c1686b3a35e22179e2639ad87fe90389` |
| `research/youtube-note-corrections.json` | `3e91ee3eb033978150f48653bc6aee56450be7c26e6024b91a56a8c2be975c66` |

## Initial confirmed gaps

1. **Replacement timestamps can exceed the source duration.** In the copied Mailchimp correction, setting `replacement.end_timestamp` to `99:00:00` produces a rendered note and **zero verifier errors or manual-review flags**. `reviewed_wiki_data()` checks timestamp syntax and ordering at verifier lines 115–117, but the source-duration check at lines 294–296 runs on original claims before derivatives are applied. The renderer also accepts malformed timestamp text; the verifier catches malformed syntax, but both accept the ordered 99-hour range. Apply source-bound timestamp validation to replacement claims while retaining original-output validation. Test: `out_of_bounds_replacement_timestamp`.

2. **The verifier accepts stale claims retained alongside their corrections.** Appending the original Mailchimp `adam_self_report` claim line after the correctly rendered `host_statement` line yields **zero verifier errors or manual-review flags**. Lines 347–353 check that every expected line is present, without rejecting an extra contradictory original claim. Replacing the corrected line with the stale line is detected, so the missing protection concerns coexistence. Compare the complete parsed claim blocks, including their count and category, with the expected derivative, or explicitly reject superseded original blocks. Test: `wiki_retains_stale_claim_alongside_correction`.

Neither defect requires changing immutable sources, model JSON or provenance. The parent owns implementation fixes.

## Checks that passed

All nine records match their whole original-note hashes, their exact original fields, and all primary/supporting evidence hashes. Declared metadata fields also match the captured JSON. The machine report records canonical JSON hashes for original/replacement field values; these document exact reviewed values rather than substituting for source hashes.

| Affected video | Records | Independent derivative and exact promoted render | Original provenance and terminal checks |
| --- | ---: | --- | --- |
| `-GDzNq_R0b8` | 1 | Pass | Pass |
| `HIuvLo23R2M` | 1 | Pass | Pass |
| `RK1Kk1h783c` | 3 | Pass | Pass |
| `_ZK7wgkHuG4` | 2 | Pass | Pass |
| `meZrgsAZWos` | 1 | Pass | Pass |
| `p5fyQaRE7ao` | 1 | Pass | Pass |

The independent application of registry replacements matched both implementations, and neither function modified its input object. The six baseline `audit_note()` results have zero errors and zero manual-review flags; this is not an all-100 audit or a claim of complete semantic accuracy.

Disposable tests confirmed rejection of stale original-note bytes, stale primary evidence, stale supporting evidence, unsupported correction fields, a mismatched original field and an invalid replacement claim type. The verifier also rejects malformed replacement timestamps, although the renderer itself accepts them.

Original terminal-output protections remain effective: changing original note content and rebinding the registry's note hash still triggers both `terminal_output_mismatch` and `response_mismatch`. Tampering with the provenance source hash triggers `provenance_mismatch`. Reverting a promoted claim to its original attribution triggers `wiki_claim_render_mismatch`. These tests preserve the distinction between original model output and reviewed derivatives.

All **59 live files** read into the initial fixture snapshot remained byte-for-byte unchanged during that review, including affected original JSON, provenance, captions, registry and scripts. The file hashes and terminal/response comparisons establish the observed state; they do not reconstruct any unrecorded historical edit. Temporary fixture removal succeeded. The reusable test runner and research validation reports are the only files created by this task.

## Source Notes

This review checks implementation behavior and faithful application of declared corrections. The underlying semantic source reviews remain [[research/audit-video-batch-51-55]] and the registry's cited evidence. It does not authorize new public copy or replace the independent final corpus audit. Original scripts, raw sources, registry, model outputs, promoted notes, index, log and the running extraction process were not modified by this task.

## Follow-up: both fixes verified at 09:29 UTC

After the parent updated both scripts and rebuilt the catalog, the fixture runner's `--retest` mode ran the **clean six-note baseline and only the two previously missed cases**. Before/after evidence is retained separately: [initial results](reviewed-corrections-validation.json) and [retest results](reviewed-corrections-validation.retest.json). The registry hash is unchanged.

| Updated script | SHA-256 |
| --- | --- |
| `scripts/synthesize_youtube.py` | `0e5e3c489e546fb78aa9b07edf8508df13573dc55b6b2f23eae9cd9d9365e67b` |
| `scripts/verify_youtube_synthesis.py` | `2e136efe63487a29332c6231616ac8844677c85431fd32f4033aff585589e862` |

| Scenario | Before | After |
| --- | --- | --- |
| Clean six-note baseline | All exact derivatives/renders and original provenance checks pass | All six still pass, with zero errors or manual-review flags |
| Replacement timestamp changed to `99:00:00` | Renderer accepts; verifier emits zero errors | Renderer rejects; verifier emits `reviewed_derivative_invalid` because a correction must retain its original verified timestamp anchors |
| Original attribution line appended alongside correction | Verifier emits zero errors | Verifier emits `wiki_claim_sequence_mismatch` |

The inspected fixes require claim corrections to preserve original start/end timestamp strings and compare all rendered claim lines against the complete expected sequence. This prevents the two reproduced failure modes while keeping original source, prompt, provenance, terminal-message and response checks active in the clean baseline. No further mutation scenarios were run in this follow-up.

The retest again left all 59 live snapshot files unchanged and removed its disposable fixture directory. These results apply to the identified code hashes and nine-record registry; they do not claim an exhaustive security review or final all-100 completion.
