#!/usr/bin/env bash
set -euo pipefail
TASK_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
if [[ "${1:-}" != "" && "${1:-}" != "--embed" ]] || [[ $# -gt 1 ]]; then
  echo 'Usage: scripts/qmd-refresh.sh [--embed]' >&2
  exit 2
fi
"$TASK_ROOT/scripts/qmd.sh" update
if [[ "${1:-}" == "--embed" ]]; then
  "$TASK_ROOT/scripts/qmd.sh" embed -c context --max-docs-per-batch 16 --max-batch-mb 8
fi
