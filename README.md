# 个人 Codex Skills

由 `qiuqiuqiu123` 维护的个人 Codex Skills。

## 可用 Skills

### `show-me`

使用最小且准确的可视化解释代码架构、运行流程、UI 结构、数据流、重构、状态变化和复杂概念，支持伪代码、树、Mermaid、diff 和聚焦的 HTML 产物。

使用 Skills CLI 安装：

```bash
npx skills add qiuqiuqiu123/codex-skills --skill show-me
```

手动安装到 Codex 时，将 `skills/show-me` 复制到 `~/.codex/skills/`，然后使用 `$show-me` 调用。

### IDD 套件

六个 Skill 实现了[意图驱动开发（Intent-Driven Development）](https://github.com/qiuqiuqiu123/intent-driven-development)工作流，并持续保持 steering、intent、contracts、代码、测试和锚点一致：

| Skill | 用途 |
|---|---|
| `idd-develop-feature` | 通过明确的意图与契约 Gate 澄清和开发特性 |
| `idd-debug` | 分析根因，或实施经过验证的最小修复 |
| `idd-deploy` | 按环境部署指定 revision，并完成线上验证 |
| `idd-init-project` | 初始化 Greenfield 项目，或渐进式接入 Brownfield 项目 |
| `idd-remove-feature` | 跨全部 IDD 层停用、弃用或删除特性 |
| `idd-reconcile` | 审计或修复漂移与锚点完整性 |

安装单个 Skill：

```bash
npx skills add qiuqiuqiu123/codex-skills --skill idd-develop-feature
```

需要展示特性设计或删除影响图时，同时安装可视化 Skill：

```bash
npx skills add qiuqiuqiu123/codex-skills --skill show-me
```

每个 IDD Skill 都包含固定版本的本地 `docs/idd-core.md` 副本。源仓库和精确 commit 记录在 [`idd-core.lock`](idd-core.lock) 中；运行时不依赖网络。

维护命令：

```bash
./scripts/sync-idd-core.sh /path/to/intent-driven-development/docs/idd-core.md <source-commit>
./scripts/validate-idd-suite.sh
```

## 许可证

采用 MIT 许可证，详见 [LICENSE](LICENSE)。
