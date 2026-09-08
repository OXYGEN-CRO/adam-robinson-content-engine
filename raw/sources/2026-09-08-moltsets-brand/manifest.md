# MoltSets brand capture — 2026-09-08

- Source: https://moltsets.com/ and its public linked CSS/assets.
- Purpose: user requested branding extraction and an improved reusable graphics/motion foundation.
- Exact source: `homepage.html`, `moltsets-base.css`, original assets under `assets/`, and six SF Mono WOFF2 files under `fonts/`.
- Rendered evidence: `homepage-desktop.png` is a real full-page browser capture including the site's overlays. `moltsets-lockup-source.png` is the first header capture; `moltsets-lockup-transparent.png` is a second capture with only ancestor backgrounds cleared. Preserve both.
- `source-tokens.json` extracts the first CSS root token block without changing values.
- `assets-manifest.json` records source URLs, destination files, bytes, hashes and rights notes. `capture-manifest.json` records the transparent lockup capture and its production derivative.
- Live browser inspection confirmed SF Mono 400 and 700 loaded; CSS declares 300, 400, 500, 600, 700 and 800. The original logo is live lowercase text and an inline pixel mark; no full outlined wordmark was linked in the inspected header.
- Original mascot reveal: seven frames, cumulative starts 0, 150, 240, 320, 410, 490 and 550 ms. Original thinking sprite uses seven frames with random hold ranges. The production kit uses fixed holds within those ranges for reproducible video frames.
- Source/public-use boundary: public website material saved for the user's company-brand task. Source visibility is not a stock-art or font redistribution licence. SF Mono files are reference-only; production uses bundled OFL Roboto Mono. Company logo/sprites remain MoltSets assets. Homepage claims are not independently verified by this ingest.
- Structural reference: `~/personal-brand/brand/BRAND.md`, `tokens.json`, `components.css`, `package.json` and folder inventory, read only. No personal content or identity assets copied.
- Human versus interpretation: the user identifies the supplied website as Adam Robinson's company. Larger graphic type, safe margins, compositions and deterministic motion are proposed implementation choices, not observed website tokens or author beliefs.

Durable synthesis: [Brand guide](../../../brand/BRAND.md), [patterns](../../../brand/patterns.md), [architecture](../../../brand/architecture.md).
