---
name: idd-develop-feature
description: 通过意图驱动开发规划或实现特性。使用场景（Use when）：用户要求在 IDD 项目中新增能力、保持意图和契约的权威性，或需要明确选择 lightweight 与 enterprise 方案。先起草意图并在 Gate 1 停止，再起草契约和可视化设计并在 Gate 2 停止，之后才能修改实现代码。
---

# IDD 特性开发

读取 [references/idd-core.md](references/idd-core.md) 和 [assets/change-bundle-template.md](assets/change-bundle-template.md)。使用唯一的 `.idd/changes/<slug>/` 变更包，不得覆盖无关的活跃变更。

## 确认范围

提问前，检查 `.steering/`、相关 intent、contracts、代码、测试和活跃变更。确认：

- 使用 `plan` 还是 `build` 模式；
- 使用 `lightweight` 还是 `enterprise`，先基于证据给出建议，再由用户明确确认；
- 目标结果、用户、实际与期望行为、验收场景、非目标和关键约束。

只询问仓库中无法获得且会改变设计的事实。

## 阶段 1：意图

编写 `request.md` 和 `intent-proposal.md`，明确权威 `intent/` 目标并展示精确的拟议 diff。获批前不得修改权威意图。

展示意图、假设、方案等级和开放问题。**在 Gate 1 停止。** 模糊的鼓励不算批准。获批前，不得创建或修改契约、技术设计、实现、生成代码、迁移或特性测试。

获批后，只应用已批准的意图 diff，并记录决策。

## 阶段 2：契约与设计

推导结构契约、EARS/GWT 行为契约、受影响代码和消费者、迁移、测试、锚点、运维事项和有序任务。Enterprise 工作还需覆盖安全、审计、兼容性、失败模式、容量、可观测性、回滚和 ADR 需求。

编写 `contract-impact.md`、`design.md` 和 `tasks.md`。可用时调用 `$show-me`，生成基于仓库事实的最小架构、状态、控制流或数据流图；否则使用紧凑且经过核对的 Mermaid。

展示契约 diff、设计图、影响、风险、迁移、验证和任务。**在 Gate 2 停止。** 获批前，不得修改实现、生成代码、迁移或测试。已批准的上游内容变化时，重新计算下游产物。

获批后，只应用已批准的契约变更。

## 阶段 3：实现

`plan` 模式以一套已批准、可直接实施的方案包结束。`build` 模式继续执行：

1. 按顺序实施任务，不进行无关重构。
2. 只根据已批准的 schema 生成代码，并添加独立的验收测试和失败路径测试。
3. 添加 `@intent:` 和 `@contract:` 锚点并刷新索引。
4. 运行聚焦检查和必需的更广范围检查。
5. 可用时以 `audit` 模式运行 `$idd-reconcile`。
6. 在 `verification.md` 中记录命令、证据、跳过的检查和残余风险。

只要仍有 Gate、验收场景、任务或必需验证未完成，就不得宣称工作完成。
