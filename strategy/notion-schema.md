---
type: configuration
status: active
owner: adam
created: 2026-09-07
updated: 2026-09-08
sources:
  - templates/origin.md
  - raw/sources/2026-09-08-notion-setup/brief.md
tags: [notion, template]
---

# Notion schema

[Adam Robinson Content Example](https://prospera-service.notion.site/3d4b3dd667a781dcac4aea561260a788) is the configured page in Tim's Digital Garden. It contains the Content Board, Pillars & Topics, and Hooks, using the same database-only home-page layout as Content Ecosystem. Verified on September 8, 2026: four pillars, 26 topics, 17 hook examples across 14 patterns, and zero content pieces. This page records configuration, not Adam's personal content.

Connection settings for your own duplicate belong in ignored `strategy/notion.local.json`.
Start from `strategy/notion.example.json`. The public release omits the old
bootstrap `strategy/notion.json` so a clone cannot inherit a live write target.
Creator Inspo was empty and removed from this template; the three databases below
are the complete setup.

## Content Board

| Property | Type / values |
| --- | --- |
| Name | Title |
| Status | Select: Idea, Creating, Published, Backlog |
| Pillar | Multi-select: Building in public, Bootstrapping versus VC, Go-to-market, SaaS building |
| Platform | Select: LinkedIn, X, YouTube, Instagram, Newsletter |
| Publish date | Date |

Use 1 pillar per piece. Pillar names and colors are synchronized with Pillars & Topics.

Views: Stages (by status), Calendar (by Publish date), All pieces, and By pillar. Draft bodies contain 1 paste-ready text code block. Record the reader, topic, one funnel job and sources in the page body. There is no Funnel stage or Format property. No draft rows or dates were created in this setup.

## Pillars & Topics

| Property | Type / values |
| --- | --- |
| Name | Title |
| Level | Select: Pillar, Topic |
| Pillar | Select: Building in public, Bootstrapping versus VC, Go-to-market, SaaS building |
| Status | Select: Active, Parked |
| One line | Text |

Views: Pillars (Level = Pillar), Topics (Level = Topic, grouped by Pillar), All (grouped by Pillar).

Four pillar rows and 26 topic rows are active. The existing reader questions were preserved: six topics each for Building in public and Bootstrapping versus VC; seven each for Go-to-market and SaaS building. Topic pages contain three or four subtopics, the source-listed funnel fit, and dated links to the original posts. Each pillar page has a promise, an opposing practice, a boundary, a filtered Topics view and a filtered Pieces view of the existing Content Board.

The setup follows `templates/notion-pillar.md` and `templates/notion-topic.md`, adapting their blank scaffold to the existing research. These remain copyable page bodies, not installed native database templates.

## Hooks

Hook (title), Type (select). Gallery and All hooks views. Seventeen examples from the existing archetype table in [[voice/hooks]] are populated. Every row contains the pattern and when to use it, the source opening in a text code block, an original-post link, publication date, capture-time likes and an adaptation note. Quotation punctuation comes from the preserved source post.

Types: Law, Confession, Correction, Big result — small resource, Anger at a norm, Scene, Dialogue, Then versus now, Found object, Borrowed story with a twist, Exclusion, Status list, Bare list, Rage at a document. The two Law variants and two Scene variants share their base type; the two Found object examples remain separate. Notion select names cannot contain commas, so its Big result label uses a dash.

The eight underperforming comparison examples and broader analysis remain in [[voice/hooks]]. The Notion gallery contains the 17 archetype examples, not every opening in the research archive.

## Public example references

These are public template references only. After duplication, fetch your copy
through Notion MCP and discover its new IDs. Never write to these example data
sources when setting up a clone. An incomplete local file means setup is unfinished.

| Database | Data source |
| --- | --- |
| [Content Board](https://app.notion.com/p/4949d7057e494bfebe655cafedc9a4cd) | `collection://d4a8daee-58d9-4aad-b7d9-69076b85a6be` |
| [Pillars & Topics](https://app.notion.com/p/3222516775b84661882ed07c76376b3d) | `collection://3b49ffe0-2277-453f-a3bd-40a7fd64406f` |
| [Hooks](https://app.notion.com/p/9485f6b45fd04daaa9adef9771b83492) | `collection://028cb465-79ab-40b3-83a8-9939f1f83cf3` |

Page ID: `3d4b3dd6-67a7-81dc-ac4a-ea561260a788`.

The three inline databases are ordered Content Board, Pillars & Topics, Hooks. The public template adds a compact duplication/setup callout above the databases, linking the repository and Oxygen. Use the existing Pillars view for the compact pillar overview and Topics for the topic board. View-tab order and empty-group display are Notion UI settings. If presenting the board, select Stages; select Gallery for hooks. Existing views were preserved, and By pillar was added to the same Content Board.

## Related Pages

- [[pillars]]
- [[funnel]]
- [[index]]

## Source Notes

- `templates/origin.md`: the structural reference and content excluded.
- New database schemas and views created through Notion MCP on 2026-09-07, under the page above. No original database was modified.
- [[raw/sources/2026-09-08-notion-setup/brief]]: user authorized populating the existing databases, adopting the existing pillar organization, deleting Creator Inspo and adding the content overview. Live queries verified row counts and each pillar's Topics filter. No posts were published or scheduled.
