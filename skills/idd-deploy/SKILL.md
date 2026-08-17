---
name: idd-deploy
description: 将 IDD 项目部署或回滚到指定的本地、开发、staging、production 或自定义环境。使用场景（Use when）：revision 需要以 dry-run、standard、rolling、blue-green、canary 或 rollback 模式执行，并要求使用仓库定义的预检、明确的生产授权、线上 revision 验证和可审计发布报告。
---

# IDD 部署

读取 [references/idd-core.md](references/idd-core.md) 和 [assets/release-report-template.md](assets/release-report-template.md)。优先使用仓库自带的发布自动化；项目已有部署命令时不得自行编造。

## 确认范围

检查发布说明、CI/CD、manifest、环境、迁移、健康检查、可观测性和当前状态。确认并复述：

- 环境：`local`、`dev`、`staging`、`production` 或具名自定义目标；
- 策略：`dry-run`、`standard`、`rolling`、`blue-green`、`canary` 或 `rollback`；
- 不可变的源 revision、受影响服务和相关 IDD 变更；
- 回滚目标，以及是否授权自动回滚；
- 线上版本、健康、smoke、promotion 和失败信号。

外部目标或回滚行为仍不明确时询问用户。

## 预检

1. 确认工作树和 revision，不得静默部署未提交状态。
2. 拒绝存在未解决 critical IDD 漂移的部署。
3. 运行必需的测试、lint、类型检查和构建。失败时停止，不得弱化检查门槛。
4. 验证配置，但不得打印 secret 值。
5. 验证迁移与新旧应用 revision 均保持兼容。
6. 定义 promotion、观察、失败和回滚标准。
7. 编写 `.idd/releases/<release-id>/plan.md`。

`dry-run` 在非修改性验证后停止。执行 production 部署、破坏性迁移、公开流量变更或回滚前，展示精确目标、revision、服务、操作、停机影响、回滚方案和风险。除非当前请求已经明确授权该操作，否则必须获得针对该操作的授权；不得将 staging 授权扩大到 production，也不得将部署授权扩大为回滚授权。

## 部署并验证

1. 执行已批准路径并记录平台 revision。
2. 观察渐进发布的每一步，超过失败阈值时停止。
3. 证明新 revision 正在承载流量。
4. 运行深度 readiness 和业务 smoke 检查，再观察预先定义的日志和指标，不得暴露敏感数据。
5. 失败时只遵循已批准的回滚策略；未授权回滚时保留证据并停止。
6. 线上验证成功后，编写 `report.md`；仓库存在部署状态文档时同步更新。

退出码为 0 不等于线上验证成功。目标环境确认精确 revision 和必需行为之前，不得宣称已部署、健康、已发布或已回滚。
