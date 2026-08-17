---
name: idd-reconcile
description: 审计或修复 IDD steering、intent、contracts、实现、生成代码、测试和锚点之间的漂移。使用场景（Use when）：检查文档是否仍然驱动代码、变更后验证锚点、生成按严重性排序的漂移报告，或按权威顺序实施修复，并在权威业务含义变化时停在人工 Gate。
---

# IDD 一致性校验

读取 [references/idd-core.md](references/idd-core.md) 和 [assets/drift-report-template.md](assets/drift-report-template.md)。确认范围和模式：

- `audit`：不得修改源码、权威文档、生成产物、测试或索引；只允许写入用户要求的报告。
- `repair`：先审计，再按权威顺序提出修复。修复模式不等于 Gate 已获批准。

语义检查前先运行确定性扫描器：

```bash
python3 <skill-root>/scripts/scan_anchors.pyz <project-root> --format markdown
```

## 审计

检查 `.steering/`、`intent/`、`contracts/`、实现、测试、`.anchors/`、`.validator/` 和范围内的 `.idd/` 记录。核对：

1. steering 违规和有效 ADR override；
2. intent 到 contracts 的传播是否缺失或矛盾；
3. schema、人工可读表格和生成产物是否一致；
4. 范围内每条 EARS/GWT 规则是否具有实现和独立测试证据；
5. 正向目标、标题、反向条目、已删除路径、重复项和过期事务引用。

不得要求纯实现细节拥有业务锚点。语义发现需标明置信度，并区分行为缺失与测试证据缺失。

将已证实的权威违规标为 `critical`，需要判断的高概率漂移标为 `warning`，非漂移改进标为 `suggestion`。每项发现都包含证据、权威来源、文件、置信度、后果、首选解决方向和 Gate 要求。

`audit` 模式返回或写入 `.validator/drift-report.md` 后停止。不得刷新索引，因为这会改变审计快照。

## 修复

1. 按以下顺序修复：steering 决策、intent、contracts、生成代码、普通实现、测试、锚点。
2. 业务含义、权限、工作流或权威 intent 变化时，在 Gate 1 停止。
3. 结构或行为 contracts 变化时，在 Gate 2 停止。
4. 只有实现漂移时，应用最小且经过验证的变更。
5. 只通过仓库自带的 generator 重新生成产物。
6. 权威内容和源码变更稳定后刷新索引。
7. 重新运行确定性和语义检查，保留变更前后证据。

如果证据无法确定正确的权威来源，停止并询问，不得自行发明规则。
