---
name: idd-remove-feature
description: 停用、弃用或永久删除由 IDD 管理的特性。使用场景（Use when）：下线能力、endpoint、工作流、flag、schema 或 UI，并要求基于证据生成反向影响图、经过意图和契约 Gate、保证迁移安全、同步删除文档和代码、完成负向验证、清理锚点并保留审计记录。
---

# IDD 特性删除

读取 [references/idd-core.md](references/idd-core.md) 和 [assets/removal-record-template.md](assets/removal-record-template.md)。使用唯一的 `.idd/changes/<slug>/` 变更包。

## 确认范围并建立影响图

从权威 intent 和 contracts 开始，沿锚点和仓库引用追踪。确认：

- `disable`：关闭入口，但保留可恢复的实现；
- `deprecate`：在约定迁移窗口内保持兼容；
- `delete`：物理删除实现和已失效的权威内容。

盘点 intent、contracts、代码、路由、UI、API、事件、job、消费者、flag、配置、schema、存量数据、迁移、测试、文档、SDK、遥测、dashboard、runbook、基础设施和锚点。确认保留、兼容、rollout 和 rollback 义务。

可用时调用 `$show-me`，生成基于证据的最小依赖树和删除顺序；否则使用紧凑的树或 Mermaid。标记不确定的依赖边。

## Gate 1：意图

起草精确的权威 intent diff，包括原因、模式、用户可见的剩余行为、日期、替代方案、数据处理和非目标。展示后**在 Gate 1 停止**。获批前不得修改 contracts 或实现，只应用已批准的 diff。

## Gate 2：契约

起草 API、事件、schema、行为、错误、消费者、迁移、兼容和 rollout 变更。旧 revision 或消费者仍依赖该 schema 时，破坏性数据变更必须采用经过验证的分阶段迁移。

展示精确的 contract diff、依赖图、有序实施步骤、rollback 限制和不可逆影响。**在 Gate 2 停止。** 只应用已批准的契约变更。

## 执行

1. Gate 2 未逐项列出破坏性目标时，再次确认精确目标。
2. 必要时先关闭入口和新增写入，再删除依赖项。
3. 按批准方案迁移、导出、匿名化或保留数据。
4. 按依赖顺序删除实现、生成产物、配置、基础设施和运维资产。
5. 删除失效测试，并添加负向测试证明该能力已不可访问。
6. 删除失效的活跃规则，同时保留兼容记录。
7. 刷新锚点，并在可用时运行 `$idd-reconcile`。
8. 编写 `.idd/history/<slug>/removal.md`，记录批准、精确删除项、数据处置、验证、revision 和残余义务。

只要消费者、数据、flag、路由、contracts、锚点或运维资产仍未得到说明，就不得宣称已完全删除。保留审计历史。
