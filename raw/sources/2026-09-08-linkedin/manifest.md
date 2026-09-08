# Source manifest — Adam Robinson LinkedIn

- Captured: 2026-09-08 UTC. Primary posts captured approximately 07:39–07:43; continuation supplement approximately 08:03–08:05.
- Origin: https://www.linkedin.com/in/retentionadam
- Source author: Adam Robinson, LinkedIn public identifier `retentionadam`, stable profile ID `ACoAAAn6cNQB-3DeWLieTXNmiuo8Bs-0VvHPgYA`.
- Source date: selected post bodies span **2025-10-20T20:23:22.916Z through 2026-09-07T17:41:49.480Z**.
- Selection: newest 200 unique posts attributed to Adam's profile, ordered by original `postedAt.date`. Publication under his profile does not verify the individual writing process.
- User authorization: [captured brief](../2026-09-08-brief/brief.md) explicitly requests 200 recent posts using the Oxygen-managed scraper and a local knowledge wiki.
- Public-use boundaries: publicly accessible material collected for private research and author context. Reuse in new first-person public copy, distribution of personal stories, scheduling and outreach are not approved. Guest metrics/statements retain their original subjects. Third-party comments are raw evidence only.

## Collection and native provider

Used **only Oxygen's managed cookieless `scraper.linkedin_profile_posts`** for post collection. The live descriptor and dry-run evidence are preserved in `responses/tool-descriptor.json` and `responses/page-01-dry-run.json`; each page cost 16 credits. No connected LinkedIn account quota was used.

1. One-page pilot returned 50 items and a pagination token; exact CLI/provider envelope in `responses/page-01-live.json`.
2. Hosted table-backed search followed the pilot cursor for three pages, returning 150 unique items. Run `38778251-2f4b-48a4-8294-3e666617c9aa` completed with no failures or duplicates. Source payloads are exact post objects in `responses/table-export-01.json`; the evolving cursor chain, attempts and charges are in `responses/ingestion-items.json`.
3. Those 200 timeline items contained 199 Adam-profile posts and one Taylor Haren repost. One additional hosted page, run `480cff7a-5611-4fb9-9858-8e5cc49309bc`, fetched 50 more items. This supports selecting exactly 200 Adam-profile posts while preserving the extra 49 and Taylor's repost separately in raw captures.
4. Pilot objects were imported into the same table without another provider call. Final table export contains 250 unique original timeline items in `responses/table-export-final.json`.

The generic `search plan` response suggested other providers despite the native-provider hint. It was **not executed**. `managed-search-plan.json` records the explicit native descriptor-based choice and observed payload/cursor paths. There was no provider fallback.

[Inspect the retained Oxygen source table](https://oxygen-agent.com/workspaces/4257983c-406e-4658-b899-d7ba3cc760a6/tables/c0c5e684-f06b-4e52-924c-cad5799495d8).

## Files and normalization

- `responses/`: exact CLI responses, live provider pilot envelope, table exports, descriptors, dry-run previews and hosted run/item records. `source_payload` in table exports retains each full raw post object, including original author/date, image links, embedded reposts and engagement.
- `posts/`: 200 individual Markdown files with unchanged post text, date, permalink, ID, source-object location and public-use boundary.
- `posts.normalized.json`: 200 selected posts with rank, source paths, original text and engagement snapshot.
- `selection-audit.json`: unique-count, author, recency, empty-text and exact-text SHA256 checks. Selection deduplicates post ID, filters exact author identifier, sorts by source timestamp, takes 200.
- `pilot-table-rows.json`: derived mapping used to append the already-captured pilot to the retained table, not a new scrape.
- `managed-search-plan.json`, `page-02-request.json`, `page-05-request.json`: authored native execution definition and cursor input artifacts.
- `continuations/`, `continuations.normalized.json`: separately preserved author comments described below; never counted as part of the 200 posts.
- `file-checksums.sha256`: immutable capture-file inventory/checksums, excluding itself.
- Normalization script: `scripts/normalize-linkedin.py`; it refuses to overwrite an existing source artifact with changed text.

## Author continuation supplement

Three selected posts explicitly continued in comments: July14,2026 (`7482856108223590400`), January28,2026 (`7422336968463765505`), December27,2025 (`7410750160303226880`). One relevance page per post using **`scraper.linkedin_post_comments`** recovered the continuations and nested replies. The descriptor has no author-only filter. Returned comments were filtered locally by Adam's stable profile ID.

- 15 Adam-authored root/nested comments preserved separately, including the complete substantive continuation threads visible in the returned pages.
- 232 root comments were returned across the three bounded pages; exact objects and nested replies remain in the pilot/hosted exports. No commenter enrichment or outreach occurred.
- The July14 endpoint reported another page, but the requested author conclusion was already recovered, so no extra commenter pagination was performed.
- Supplemental runs `5cccff4c-ea1e-438d-8546-0999ab22f880` and `fae117d5-7b9a-41ce-9cea-ac1165732cd3` completed, with 46 and 86 rows respectively. July14 used a 100-comment one-record pilot.
- Supplement table: [inspect continuation source objects](https://oxygen-agent.com/workspaces/4257983c-406e-4658-b899-d7ba3cc760a6/tables/22c7aa81-2c63-4d77-91a5-e780b9f07ab9).

## Cost and provenance

| Action | Calls/pages | Actual Oxygen credits | Evidence |
| --- | --- | --- | --- |
| Post pilot |1|16| `responses/page-01-live.json` |
| Hosted posts pages2–4 |3|48| `responses/ingestion-items.json` |
| Hosted posts page5 |1|16| `responses/extension-ingestion-items.json` |
| July14 comment pilot |1|16| `responses/comments-32-live.json` |
| January28 continuation page |1|16| `responses/comments-131-ingestion-items.json` |
| December27 continuation page |1|16| `responses/comments- 156-ingestion-items.json` |
| **Total** |**8**|**128**| Sum of actual receipts; posts 80, supplement 48. |

All calls were previewed and bounded at the live descriptor's 16-credit page price. Tables/imports/read-only exports incurred no provider credits. No subscription purchase, connected-account operation, enrichment or public write was performed.

## Completeness and interpretation limits

The200 selected posts are the latest 200 Adam-profile items returned by the native public profile feed at capture, with no duplicate IDs or empty body text. This proves the collected provider-visible feed slice; it cannot prove availability of deleted/private/unreturned posts. Original media URLs are preserved, but image/deck content is not automatically transcribed. The metadata/engagement is a snapshot and not audited financial evidence.

Some source copy is recycled, contains conflicting dates, or carries forecasts as provocative hooks. One post explicitly republishes Robb's wording; some quote guests and multiple metrics refer to third parties. The wiki retains those distinctions. See [LinkedIn synthesis](../../../research/linkedin-synthesis.md), [[voice/linkedin-voice]], [[identity/proof]] and [[strategy/pillars]].
