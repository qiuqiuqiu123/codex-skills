# IDD 特性变更包

在 `.idd/changes/<slug>/` 下创建以下文件。它们是事务记录，不是权威业务源。

## `request.md`

```markdown
# 特性需求：<标题>

- Slug：<slug>
- 模式：plan | build
- 方案等级：lightweight | enterprise
- 状态：clarifying | awaiting-intent-approval | awaiting-contract-approval | ready-to-build | implementing | verified

## 目标结果
## 用户与角色
## 当前行为
## 期望行为
## 验收场景
## 非目标
## 约束
## 开放问题
## 批准记录
```

## `intent-proposal.md`

```markdown
# 意图提案：<标题>

## 受影响的权威文件
## 业务规则和工作流 Diff
## 权限或 Persona 影响
## 假设
## Gate 1 决策
```

## `contract-impact.md`

```markdown
# 契约影响：<标题>

## 结构契约
## 行为契约
## 兼容性与迁移
## 消费者与失败模式
## Gate 2 决策
```

## `design.md`

```markdown
# 技术设计：<标题>

## 背景
## 选定设计
## 已验证设计图
## 数据与状态流
## 安全与运维
## 替代方案与权衡
## 风险
```

## `tasks.md`

使用有序 checkbox，并为每项任务指定具体文件或产物。适用时包含实现、测试、锚点、迁移、可观测性、部署和一致性校验。

## `verification.md`

记录验收证据、命令和退出结果、一致性校验发现、跳过的检查及原因、残余风险，以及存在时的精确 revision。
