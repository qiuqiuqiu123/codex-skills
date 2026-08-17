# IDD 特性删除包

## 活跃变更文件

```markdown
# 特性删除：<标题>

- Slug：<slug>
- 模式：disable | deprecate | delete
- 状态：inventory | awaiting-intent-approval | awaiting-contract-approval | executing | verified

## 原因与用户影响
## 权威 Intent 与 Contracts
## 依赖清单
## 外部消费者
## 数据保留与迁移
## 运维与基础设施
## 已验证依赖图
## 删除顺序
## Rollback 与不可逆步骤
## Gate 1 决策
## Gate 2 决策
```

## `.idd/history/<slug>/removal.md`

记录已批准的原因和模式、日期、受影响用户与消费者、精确删除的文件和资源、保留的兼容性、数据处置、负向验证、锚点刷新结果、部署或迁移 revision、批准人和残余义务。
