#!/usr/bin/env bash
set -euo pipefail

task_script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
task_repo_root=$(CDPATH= cd -- "$task_script_dir/.." && pwd)
task_expected_sha=$(awk -F= '$1 == "sha256" {print $2}' "$task_repo_root/idd-core.lock")
task_skills=(
  idd-develop-feature
  idd-debug
  idd-deploy
  idd-init-project
  idd-remove-feature
  idd-reconcile
)

if [[ -z "$task_expected_sha" ]]; then
  echo "idd-core.lock has no sha256" >&2
  exit 1
fi

for task_skill in "${task_skills[@]}"; do
  task_dir="$task_repo_root/skills/$task_skill"
  task_skill_file="$task_dir/SKILL.md"
  task_agent_file="$task_dir/agents/openai.yaml"
  task_core_file="$task_dir/references/idd-core.md"

  [[ -f "$task_skill_file" ]] || { echo "missing $task_skill_file" >&2; exit 1; }
  [[ -f "$task_agent_file" ]] || { echo "missing $task_agent_file" >&2; exit 1; }
  [[ -f "$task_core_file" ]] || { echo "missing $task_core_file" >&2; exit 1; }

  grep -Fxq "name: $task_skill" "$task_skill_file" || { echo "wrong skill name: $task_skill" >&2; exit 1; }
  grep -Fq "\$$task_skill" "$task_agent_file" || { echo "default prompt does not mention \$$task_skill" >&2; exit 1; }
  if rg -n '\[TODO(:|\])' "$task_skill_file" "$task_agent_file" >/dev/null; then
    echo "TODO placeholder remains in $task_skill" >&2
    exit 1
  fi

  task_actual_sha=$(shasum -a 256 "$task_core_file" | awk '{print $1}')
  if [[ "$task_actual_sha" != "$task_expected_sha" ]]; then
    echo "IDD core hash mismatch in $task_skill" >&2
    exit 1
  fi
done

python3 -c 'import pathlib, sys; compile(pathlib.Path(sys.argv[1]).read_text(), sys.argv[1], "exec")' \
  "$task_repo_root/tools/idd-anchor-scan/scan_anchors.py"
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s "$task_repo_root/tests" >/dev/null
python3 "$task_repo_root/skills/idd-reconcile/scripts/scan_anchors.pyz" --help >/dev/null
echo "IDD suite validation passed for ${#task_skills[@]} skills."
