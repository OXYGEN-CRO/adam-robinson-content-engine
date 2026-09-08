---
title: Repository QMD retrieval scope audit
status: draft
updated: 2026-09-08
---

# Repository QMD retrieval scope audit

This local maintenance pass removes working exports and superseded research-note copies from retrieval. It preserves every source file on disk and keeps the raw archive searchable on demand. The central transcript reader and source files are outside this task's write scope.

## Configuration and isolation

- Installed package: `@tobilu/qmd` **2.5.3**, under `/Users/timscheuer/.nvm/versions/node/v22.22.2/lib/node_modules/@tobilu/qmd`; use its matching Node 22.22.2.
- Wrapper: `scripts/qmd.sh`; index: `content-engine-3b88f9e94f550ba1`, derived from this checkout's canonical absolute path.
- Sole collection: `context`, rooted at `/Users/timscheuer/adam-robinson-webinar`, matching `**/*.md`.
- Local configuration: `/Users/timscheuer/.config/qmd/content-engine-3b88f9e94f550ba1.yml`.
- Local database: `/Users/timscheuer/.cache/qmd/content-engine-3b88f9e94f550ba1.sqlite`.
- Exactly two additional file exclusions: `output/**` and `research/youtube-video-notes/**`. The reviewed notes in `strategy/video-notes/**`, all other research, and all eligible raw Markdown remain in scope.
- Preserve the existing root, `raw/sources`, and `strategy/video-notes` context summaries, model selections, and other collection settings.

`scripts/qmd-setup.sh` now writes this configuration reproducibly through the installed QMD collections API. It selects the wrapper's explicit index, checks that the collection belongs to this repository, preserves existing context text, and adds missing context defaults. It refuses a conflicting collection root, pattern, extra collection, unreviewed existing file exclusion, or `INDEX_PATH` override. Configuration is idempotent; setup explicitly leaves indexing to `scripts/qmd-refresh.sh --embed`, so callers control the timing of the update and embedding pass.

## Version-matched evidence

The installed `dist/collections.js` exports `setConfigIndexName`, `setConfigSource`, `loadConfig`, `saveConfig`, and `getConfigPath`; its YAML serializer preserves the loaded configuration fields. The CLI's explicit `--index` branch in `dist/cli/qmd.js:2499` selects the same named configuration and bypasses project-local config discovery.

The CLI update function passes `yamlCol.ignore` to `reindexCollection` (`dist/cli/qmd.js:552`). The native implementation in `dist/store.js:944` passes those patterns to `fast-glob` together with its built-in exclusions for `node_modules`, `.git`, `.cache`, `vendor`, `dist`, and `build`; it disables symlink following and filters hidden path segments. It deactivates formerly indexed document paths absent from the new candidate set and cleans orphaned index content. It does not remove source files. `collection exclude` concerns whole-collection default query inclusion and is not the file-exclusion mechanism used here.

## Preflight evidence

At **2026-09-08 09:32:05 UTC**, the actual installed `fast-glob` implementation with the native update options found **578** eligible Markdown files before these two exclusions and **502** afterward: **6** working exports and **70** original research-note copies were excluded. More research notes may be generated later; the prefix rule applies to them automatically. The previous index snapshot had **475** active entries, including 6 working exports and 27 research-note copies.

All **364** eligible raw Markdown files remained candidates. The selected-source manifests were checked per document, using each exact `markdown_path`; **200/200 LinkedIn posts** and **100/100 YouTube transcripts** were included, with zero missing or excluded paths. JSON captions, provider responses, and metadata remain on disk; the existing Markdown collection indexes their Markdown representations, not JSON files.

| Manifest | Count | SHA-256 |
| --- | ---: | --- |
| `raw/sources/2026-09-08-linkedin/posts.normalized.json` | 200 | `5fbc54092f7b501fe82f9762af36e859b94eafbaa18169c925ef57970b76d776` |
| `raw/sources/2026-09-08-youtube/selected-100.json` | 100 | `6ac44cc9a19e0ec99b4f81b556c5dc3525d277a37f40df7ef8cc95bc1c3e20ac` |

## Update and embedding pass

Exactly one native `./scripts/qmd.sh update` completed with exit **0**: **61 new, 44 updated, 398 unchanged, 33 removed**; QMD cleaned 44 orphaned content hashes. The 33 removed active index entries were the 6 working exports and 27 original research-note copies present in the older index. They remain files on disk.

Exactly one native `./scripts/qmd.sh embed -c context --max-docs-per-batch 16 --max-batch-mb 8` ran in exec session **49094**, was followed to terminal exit **0**, and reported **1,391 chunks from 147 documents in 1 minute 41 seconds**. No additional update or embedding pass ran in this task.

The resulting SQLite snapshot has **503 active documents**, **364 active raw Markdown documents**, **zero active paths** under either new exclusion, and **33 inactive paths** under those exclusions. `store_collections` contains only the expected repo-rooted `context` collection, with the exact two exclusion patterns synchronized from YAML.

## Read-only verification and preservation

At **2026-09-08 09:36:48 UTC**, the existing auditor's installed-runtime `NODE_AUDIT` routine was reused in memory with SQLite opened read-only, `query_only=1`, and a read transaction. Its command-line/report-writing entry point was not run; this task did not replace `research/qmd-coverage-audit.json`. Checks compare each current disk body/hash/title against the active document and FTS row, then inspect every stored vector chunk for the configured model, fingerprint, contiguous sequence, coherent total, and actual finite nonzero vector data.

| Required raw category | Exact text/FTS and current-vector checks | Actual vector chunks |
| --- | ---: | ---: |
| Selected LinkedIn posts | **200/200 passed** | 314 |
| Selected YouTube transcripts | **100/100 passed** | 4,661 |
| Other raw Markdown | **64/64 passed** | 922 |

The configured embedding model remains `hf:ggml-org/embeddinggemma-300M-GGUF/embeddinggemma-300M-Q8_0.gguf`; runtime fingerprint **`c37385`**, vector dimensions **768**. SQLite contained **7,332** vector metadata rows and **7,332** actual vector rows. The installed pending predicate found **zero pending active indexed documents**. The canonical JSON digest of the 300 selected per-document results, including disk/index hashes and actual chunk proofs, was `aa39a523afdb3738be7c512f3eeeb79a43d36e7cf6ce6e03303e3c64059b04ca`.

This is snapshot completeness, not a claim that ongoing wiki authoring has stopped. The same read-only check found 98/106 current wiki pages and 1/2 root pages fully current. Nine pages had changed or appeared after indexing: `identity/backstory.md`, `identity/proof.md`, `index.md`, `strategy/learnings.md`, `strategy/video-notes/EqXag_z2OpQ.md`, `strategy/video-notes/JZiUalL7h-8.md`, `strategy/video-notes/MUQ4f6DkmsA.md`, `strategy/video-notes/meZrgsAZWos.md`, and `strategy/youtube-library.md`. Their newest disk bodies or newly created paths need the parent's final refresh, as does this audit's completion revision. No required raw document was stale, absent, or excluded.

Additional checks:

- `bash -n scripts/qmd-setup.sh` passed. A second setup invocation left both the configuration bytes and modification time unchanged.
- An `INDEX_PATH` override was rejected before database creation or mutation.
- The original configuration's existing fields, model values, and all three context texts remained equal after removing only the newly added `ignore` field from the comparison.
- All **76** originally excluded files retained identical SHA-256 values after update/embedding; one more research note appeared concurrently and is covered by the same prefix exclusion. No source file was removed or rewritten by this task.
- The other three QMD configuration files (`index.yml`, `adam-robinson-webinar.yml`, and `content-engine-a03b7efaf73057c2.yml`) retained identical hashes. All indexing commands explicitly used this repository's wrapper/index.
- Isolated configuration SHA-256 changed from `2cefce744e620b67634ed23c8843a22f5bbfcf8925930248632cfaa735b06c28` to `d7197649e861409062d3288a9b0679c0cfa1ecbfa62203cca1264bf7081b5fbd`.

Installed implementation hashes used for the verification:

| Runtime file | SHA-256 |
| --- | --- |
| `dist/store.js` | `bbf1ff75d57b2c652b7cb89e1e0c76c454ea5bff05cffdb8aa41a6cc14e59221` |
| `dist/collections.js` | `d6c6005c75407ca44e01175a21690ce23d8daabd459c06df39c857344f436d56` |
| `dist/cli/qmd.js` | `2fb0da8887e4cac6fca35a11895b3b9ce8f2ecd677ab7590c069bd564003939d` |
| `dist/llm.js` | `0de8e18a6a3b39000b51e7b75daf8295ab4ee978be0632ffe3e58ac231eac36a` |
| `dist/db.js` | `5d3b7e0c06d5cd8749464bbd36de26c433f62f269f3a69bea68c6fe23e1cc3ca` |

## Source Notes

This is a local retrieval configuration audit, not source interpretation or publication approval. Evidence comprises the installed runtime files identified above, the isolated YAML/SQLite state, exact source manifests, and direct filesystem candidate enumeration. The original research-note Markdown remains available through `rg` or direct file reads; use durable `strategy/video-notes` pages for ordinary note retrieval.

## Related Pages

- [[research/README]]
- [[index]]
