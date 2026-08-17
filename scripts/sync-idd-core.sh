#!/usr/bin/env bash
set -euo pipefail

task_script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
task_repo_root=$(CDPATH= cd -- "$task_script_dir/.." && pwd)
task_source_file=${1:-}
task_source_commit=${2:-}

if [[ -z "$task_source_file" || -z "$task_source_commit" ]]; then
  echo "usage: $0 /path/to/idd-core.md <source-commit>" >&2
  exit 64
fi

if [[ ! -f "$task_source_file" ]]; then
  echo "IDD core source does not exist: $task_source_file" >&2
  exit 66
fi

task_source_sha=$(shasum -a 256 "$task_source_file" | awk '{print $1}')
task_skills=(
  idd-develop-feature
  idd-debug
  idd-deploy
  idd-init-project
  idd-remove-feature
  idd-reconcile
)

for task_skill in "${task_skills[@]}"; do
  task_target="$task_repo_root/skills/$task_skill/references/idd-core.md"
  mkdir -p "$(dirname -- "$task_target")"
  cp "$task_source_file" "$task_target"
done

cat > "$task_repo_root/idd-core.lock" <<EOF
repository=https://github.com/qiuqiuqiu123/intent-driven-development
commit=$task_source_commit
path=docs/idd-core.md
sha256=$task_source_sha
EOF

echo "Synced IDD core $task_source_commit ($task_source_sha) to ${#task_skills[@]} skills."
