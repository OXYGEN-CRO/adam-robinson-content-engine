---
name: brand-system
description: Establish or update a client's visual identity, reusable tokens and graphic conventions from their preferences and supplied assets.
---

# Maintain the brand system

Read `AGENTS.md`, `brand/BRAND.md`, relevant positioning and audience pages, supplied references and any existing implementation files. Resolve paths within this repository. No brand is preinstalled.

For a new identity, capture the client's desired impression, constraints, existing assets and usage contexts. Propose a direction only when design work is requested. Label proposed rules as draft until the client adopts them. A missing brand guide does not authorize copying a reference creator's identity.

## Central ownership

Use `brand/BRAND.md` for intent, status, usage rules and navigation. When implementation is needed, place exact reusable values in a central token file and licensed assets in `brand/assets/`. Create only the layers the actual deliverables need. Do not assume scripts or templates from another repository are present.

Separate source tokens, generated files, reusable templates, explorations and delivered assets. Link to audience and voice context instead of duplicating it. Keep compositions flexible while sharing meaningful typography and color roles.

When strengthening an existing identity, identify what feels generic in the rendered work before changing tokens. Proportion, artifact detail, annotation style and information-specific composition may need improvement more than the palette. For motion work, define how brand shapes select, travel, transform and resolve, with a readable static state. Keep scene-specific choreography local until it proves reusable; one GIF's duration or silhouette is not a universal brand rule.

## Changes

For an existing system, inspect affected consumers before editing. A request for one graphic does not authorize a global palette change. Shared CSS can alter historical work: preserve delivered assets or pin their dependencies when necessary.

Update the guide, relevant tokens and consumers together within the requested scope. Never install branded example assets as defaults in the blank template. Keep product screenshots faithful to the real product.

## Verify and hand off

Use the project's actual checks and renderer if available. Otherwise validate new artifacts with the tools used to build them. Inspect representative layouts for font loading, contrast, clipping and asset portability. Do not claim a build or visual check that was not run.

Update Source Notes, `index.md` and `log.md` for durable decisions. Return the authoritative files, adoption status and any unfinished migration.
