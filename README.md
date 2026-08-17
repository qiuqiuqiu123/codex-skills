# Personal Codex Skills

Personal Codex skills maintained by `qiuqiuqiu123`.

## Available skills

### `show-me`

Explains code architecture, runtime flow, UI structure, data flow, refactors, state changes, and dense concepts with the smallest accurate visual: pseudocode, trees, Mermaid, diffs, or focused HTML artifacts.

Install with the Skills CLI:

```bash
npx skills add qiuqiuqiu123/codex-skills --skill show-me
```

For a manual Codex install, copy `skills/show-me` into `~/.codex/skills/` and invoke it with `$show-me`.

### IDD suite

Six skills implement the [Intent-Driven Development](https://github.com/qiuqiuqiu123/intent-driven-development) workflow while keeping steering, intent, contracts, code, tests, and anchors coherent:

| Skill | Purpose |
|---|---|
| `idd-develop-feature` | Clarify and develop features through explicit intent and contract Gates |
| `idd-debug` | Analyze root causes or apply a verified minimal fix |
| `idd-deploy` | Deploy a named revision with environment-aware live verification |
| `idd-init-project` | Initialize Greenfield or incrementally adopt Brownfield projects |
| `idd-remove-feature` | Disable, deprecate, or delete features across every IDD layer |
| `idd-reconcile` | Audit or repair drift and anchor integrity |

Install one skill:

```bash
npx skills add qiuqiuqiu123/codex-skills --skill idd-develop-feature
```

Install the visual companion as well when using feature design or removal maps:

```bash
npx skills add qiuqiuqiu123/codex-skills --skill show-me
```

Each IDD skill contains a pinned local copy of `docs/idd-core.md`. The source repository and exact commit are recorded in [`idd-core.lock`](idd-core.lock); runtime use does not depend on network access.

For maintainers:

```bash
./scripts/sync-idd-core.sh /path/to/intent-driven-development/docs/idd-core.md <source-commit>
./scripts/validate-idd-suite.sh
```

## License

MIT. See [LICENSE](LICENSE).
