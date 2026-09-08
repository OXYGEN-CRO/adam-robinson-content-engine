# Source manifest — Adam Robinson LinkedIn archive from RB2B

- Captured: 2026-09-08; full export started at 12:32:38.976682 UTC and completed at 12:32:40.679635 UTC. Exact timing and command arguments are in `export-receipt.json`.
- Origin: [Adam Robinson LinkedIn Posts in Oxygen dev / RB2B](https://dev.oxygen-agent.com/workspaces/9ef2c28f-4021-4e21-881b-5af6a5213350/tables/6f0691cb-161b-41ec-8de7-afa083d9028c).
- Source author: 914 records attributed to Adam Robinson at `linkedin.com/in/retentionadam`; 65 other-author records retained in the export and excluded from Adam's corpus.
- Source dates: Adam's records span **2023-02-06T15:36:05.223Z through 2026-09-07T17:41:49.480Z**. Dates are the table's `posted_at` values; they do not establish when described events occurred.
- Selection: every row in the existing table, then exact profile-URL attribution and activity-ID deduplication. No recency cutoff or new provider scrape.
- Authorization: [[raw/sources/2026-09-08-linkedin-rb2b/brief]].
- Public-use boundaries: internal source research and retrieval. First-person public copy, scheduling, outreach and redistribution rights are not established by this capture. Other people's claims remain theirs.

## Export completeness and overlap

The read-only `oxygen-dev tables query` request used an explicit organization override, leaving the active CLI profile/workspace selection unchanged. The response reports an exact total of **979**, returns **979 unique activity IDs and row IDs**, and terminates with `hasMore: false`. No paid provider operation or remote data mutation ran.

All **200** previously selected posts are present with **identical text and publication dates**. Their original Markdown and raw provider captures are unchanged. The remaining **714** Adam-profile records now have their own exact readable source files. Forty-nine of those IDs were already inside the earlier raw 250-item provider capture but had not been promoted to individual post files; 665 Adam IDs are new even against that larger raw snapshot.

| Publication year | Adam-profile records |
| --- | ---: |
| 2023 | 368 |
| 2024 | 184 |
| 2025 | 209 |
| 2026 | 153 |
| Total | 914 |

The 65 excluded records are attributed to Santosh Sharan (58), Taylor Haren (4), and Diana Ross (3). Their complete exported rows remain available for source inspection in `responses/posts-page-001.json`; their text does not establish Adam's authorship or beliefs.

## Missing text and provenance limits

There are **911 nonempty Adam post bodies**. Three Adam records contain an empty `content` value in Oxygen:

- [[raw/sources/2026-09-08-linkedin-rb2b/posts/2023-06-13-7074415120633708545|2023-06-13 — 7074415120633708545]]
- [[raw/sources/2026-09-08-linkedin-rb2b/posts/2023-06-24-7078392579158904832|2023-06-24 — 7078392579158904832]]
- [[raw/sources/2026-09-08-linkedin-rb2b/posts/2025-01-01-7280289932038840321|2025-01-01 — 7280289932038840321]]

Those records preserve the empty source value and their URLs; no missing copy has been reconstructed from URL slugs or hooks. The table contains text, URLs, dates, author attribution, engagement, word count and first-line hooks. It does **not** include the original upstream scraper envelopes, attached media or scraping-run evidence. Export time is not the measurement time of engagement fields.

This is the complete available table, not proof of every post ever published, deleted, private or omitted by the earlier scraper. The additional posts are available for retrieval; this ingest does not claim a completed synthesis pass over them. Existing voice and strategy conclusions still reflect their documented original source sample.

## Files and verification

- `responses/table-description.json`: exact table/column metadata response.
- `responses/sample.json`: exact preliminary three-row inspection.
- `responses/posts-page-001.json`: exact complete CLI response with all 979 table rows, pagination state and table metadata.
- `export-receipt.json`: exact export command, dates, workspace/table identity and page counts.
- `posts.normalized.json`: combined 914-record Adam corpus, with full table text, source-row IDs, body hashes and readable paths. Identical original 200 bodies reuse their earlier paths.
- `posts/`: 714 additional readable source records, including the three empty-body records.
- `comparison.json`: attribution, overlap, dates, counts, exclusions and empty-body audit.
- [[raw/sources/2026-09-08-linkedin-rb2b/index]] and `by-year/`: unobtrusive archive navigation.
- `file-checksums.sha256`: SHA-256 inventory of this capture, excluding the inventory itself.

`python3 scripts/import_rb2b_linkedin.py --check` verifies the captured rows and all derived files without writes. The importer refuses to overwrite an existing artifact with different content. The original 200-post integrity check remains `python3 scripts/verify_linkedin_context.py`. The expanded manifest supplies the required LinkedIn scope to `scripts/verify_qmd_context.py`.
