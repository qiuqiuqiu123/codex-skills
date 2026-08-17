# IDD 问题包

## `analysis.md`

```markdown
# Bug 分析：<标题>

- Slug：<slug>
- 模式：analyze | fix
- 结论：confirmed | likely | unconfirmed | not-a-bug
- 严重性：critical | high | medium | low
- 根因置信度：high | medium | low
- IDD 层：intent | contract | implementation | environment | unknown

## 实际与期望行为
## 复现与环境
## 证据
## 受影响代码与锚点
## 根因
## 已排除假设
## 首选修复方向
## 测试与验证计划
## 风险与开放问题
```

## `fix.md`

```markdown
# Bug 修复：<标题>

- 分析：./analysis.md
- 状态：applied | partial | not-applied

## 根因修复
## 变更文件
## 回归测试
## 与分析结论的偏差
## 锚点或契约影响
```

## `verification.md`

记录修复后的原始复现、新增和已有测试命令及结果、更广范围的回归证据、跳过的检查及原因、残余风险和结论 `verified | partial | failed`。
