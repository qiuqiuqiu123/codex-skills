# IDD Core Protocol

> Version: 0.1.0-draft
>
> Status: normative draft for tool and Skill adapters

本文定义 IDD 工具、Agent 和 Skill 必须共同遵守的最小协议。面向人的完整说明见 [idd-methodology.md](./idd-methodology.md)。

## 1. Authority Model

权威顺序固定为：

```text
.steering > intent > contracts > generated implementation > ordinary implementation details
```

必须遵守：

- `.steering/` 与其他层冲突时，以 `.steering/` 为准。
- `intent/` 与契约或代码冲突时，以意图为准，除非存在显式 ADR override。
- `contracts/structure/` 的表格与嵌入 schema 冲突时，以 schema 为准并修正文档视图。
- `src/generated/` 由结构契约生成，不得手工修改。
- 普通实现可以独立演化，但派生自意图或契约的代码必须保持锚点和一致性。

## 2. Required Layers

```text
project-root/
├── .steering/
├── intent/
├── contracts/
├── src/
├── .anchors/
├── .validator/
└── .idd/
```

职责：

- `.steering/`：项目宪章、技术栈和工程约定。
- `intent/`：业务规则、领域概念、流程、角色和权限，不包含技术实现细节。
- `contracts/structure/`：实体、API 和事件的机器可读结构契约。
- `contracts/behavior/`：EARS 规则、Given/When/Then 场景和错误契约。
- `src/`：实现和测试；`src/generated/` 只由结构契约生成。
- `.anchors/`：文档和实现的双向索引。
- `.validator/`：漂移检查配置和最近报告。
- `.idd/`：变更、问题、发布和历史事务记录，不是业务权威源。

## 3. Human Gates

标准前向工作流：

```text
clarify request
  -> draft intent
  -> Gate 1: explicit human approval
  -> draft contracts and technical design
  -> Gate 2: explicit human approval
  -> modify implementation and tests
  -> refresh anchors
  -> reconcile
```

Gate 规则：

- Gate 必须由用户明确批准，Agent 不得自判通过。
- Gate 1 前不得修改契约和实现代码。
- Gate 2 前不得修改业务实现代码。
- 上游内容改变后，所有受影响的下游草案必须重新计算。
- 只修改现有实现、且不改变业务含义的 Bug 修复可以不创建新意图，但必须证明现有意图和契约已经明确覆盖预期行为。

## 4. Solution Profiles

### Lightweight

适用于影响范围小、不涉及敏感数据和公共兼容契约的单模块变更。仍必须保留可测试意图、必要契约、验证和锚点。

### Enterprise

适用于跨服务、公开 API、金额、权限、隐私、合规、高可用、数据迁移或长期运维场景。在基础产物之外必须考虑：

- 权限、审计和威胁模型
- API、事件和 schema 兼容
- 数据迁移与回滚
- 可观测性、容量和 SLO
- 灰度发布和失败恢复
- 必要的 ADR

Agent 可以推荐 profile，但必须让用户明确确认。

## 5. Change Propagation

| 变更源 | 必需动作 |
|---|---|
| 意图措辞或注释 | 只更新文档，确认不改变规则语义 |
| 意图规则 | 通过反向锚点计算契约和实现影响，等待 Gate |
| 结构 schema | 重新生成 generated code，并检查全部使用点 |
| 行为契约 | 定位关联实现和测试，生成增量 diff |
| 普通实现 | 检查是否偏离锚点；修实现、修上游或补 ADR |
| 删除或重命名 | 更新正反向锚点并检查死引用 |

传播只生成局部 diff，不重新生成整个系统。

## 6. Anchors

派生代码使用显式注释：

```text
@intent: intent/<path>.md#section
@contract: contracts/<path>.md#section
```

适配器必须：

- 验证锚点目标文件和章节存在。
- 在代码移动、删除和重命名后刷新 `.anchors/reverse.json`。
- 报告文档无实现、实现无文档和重复或冲突锚点。
- 不要求纯实现细节拥有业务锚点。

## 7. Transaction Records

推荐目录：

```text
.idd/
├── changes/<slug>/
├── issues/<slug>/
├── releases/<release-id>/
└── history/<slug>/
```

事务文件用于记录过程、审批、验证和审计。它们不得成为与 `intent/` 或 `contracts/` 并列的第二权威源。完成工作后，有效规则必须传播到对应权威层。

## 8. Reconciliation

完成实现、Bug 修复、特性删除或重要契约修改后，至少检查：

- intent 是否完整传播到 contracts。
- schema 与表格视图是否一致。
- contracts 与生成代码、普通实现和测试是否一致。
- 锚点目标和反向索引是否有效。
- `src/generated/` 是否被手工修改。
- `.steering/` 原则是否被违反。

报告使用：

- `critical`：明确违反 steering、意图或关键契约。
- `warning`：高概率漂移，需要人工判断。
- `suggestion`：覆盖或可维护性改进。

自动修复遇到业务语义歧义时必须停止，不能自行发明规则。

## 9. Language Convention

- `intent/`、`.steering/` 和契约说明使用中文。
- schema、OpenAPI 和代码标识符使用其原生英文形式。
- 行为契约保留 `WHEN`、`SHALL`、`IF`、`THEN`、`WHILE`、`Given`、`When`、`Then`、`And` 等英文关键字。
- 锚点指令固定使用 `@intent:`、`@contract:` 和 `@override`。

## 10. Adapter Invariants

任何 IDD Skill 或工具适配器都不得：

- 绕过人工 Gate。
- 用一次性 planning 取代持续的权威文档。
- 将 `.idd/` 事务文件提升为业务权威源。
- 默认对 Brownfield 做全量迁移。
- 在没有根因证据时自动修复 Bug。
- 把部署命令成功等同于线上 revision 已生效。
- 删除特性时只删代码而不处理文档、契约、测试、配置和锚点。
