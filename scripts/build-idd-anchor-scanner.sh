#!/usr/bin/env bash
set -euo pipefail

task_script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
task_repo_root=$(CDPATH= cd -- "$task_script_dir/.." && pwd)
task_source_dir="$task_repo_root/tools/idd-anchor-scan"
task_output="$task_repo_root/skills/idd-reconcile/scripts/scan_anchors.pyz"
task_build_dir=$(mktemp -d /tmp/idd-anchor-scan-build.XXXXXX)
trap 'rm -rf "$task_build_dir"' EXIT

PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s "$task_repo_root/tests" -v
cp "$task_source_dir/scan_anchors.py" "$task_build_dir/scan_anchors.py"
python3 -m zipapp "$task_build_dir" \
  --main "scan_anchors:main" \
  --python "/usr/bin/env python3" \
  --output "$task_output"
chmod +x "$task_output"
echo "Built $task_output"
