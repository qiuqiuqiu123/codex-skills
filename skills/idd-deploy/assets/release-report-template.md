# IDD 发布包

## `plan.md`

```markdown
# 发布计划：<release-id>

- 环境：<environment>
- 策略：dry-run | standard | rolling | blue-green | canary | rollback
- 源 revision：<不可变 revision>
- 服务：<列表>
- 回滚目标：<revision 或 artifact>
- 已授权自动回滚：yes | no

## 相关 IDD 变更
## 预检命令
## 迁移兼容性
## 部署步骤
## 健康与 Smoke 信号
## Promotion 与失败阈值
## 回滚流程
## 批准
```

## `report.md`

```markdown
# 发布报告：<release-id>

- 环境：<environment>
- 源 revision：<revision>
- 线上 revision：<已验证 revision>
- 结果：verified | partial | failed | rolled-back

## 预检结果
## 部署事件
## 线上版本证据
## Readiness 与 Smoke 结果
## 指标与观察
## 回滚证据
## 已更新状态文档
## 残余风险
```
