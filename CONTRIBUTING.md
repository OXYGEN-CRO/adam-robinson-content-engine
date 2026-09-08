# Contributing

Start at [index.md](index.md) and read [AGENTS.md](AGENTS.md). Keep source text
and synthesis separate, retain dates and attribution, and check
[the proof ledger](identity/proof.md) before changing a metric. Draft synthesis
is not an author-approved statement.

Add new source material to a dated folder with a manifest. Preserve existing
raw source files. In a sanitized public export, document changes to transport
metadata and omitted assets in the release manifest. Do not submit private
workspace settings, prospect lists or authentication details.

Run `./scripts/wiki-lint.sh` and the checks relevant to your change. For source
archive changes, run the LinkedIn and YouTube integrity commands in the README.
For credential checks, follow [SECURITY.md](SECURITY.md). Keep `AGENTS.md` and
`CLAUDE.md` identical. Open a pull request describing the resulting behavior,
source evidence and verification.
