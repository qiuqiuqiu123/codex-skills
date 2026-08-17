---
name: idd-init-project
description: 在新项目或已有项目中初始化意图驱动开发。使用场景（Use when）：建立 Greenfield 基础或第一个垂直切片，或通过发现真实项目规则、保护已有指令、蒸馏一个高价值模块，并建立 steering、intent、contracts、锚点、验证和事务记录来渐进式接入 Brownfield 项目。
---

# IDD 项目初始化

读取 [references/idd-core.md](references/idd-core.md)。离线模板位于 `assets/idd-template.tar.gz`；解压前先检查内容，合并而不是覆盖目标文件。

## 确认范围

检查目标项目，然后确认 `lightweight` 或 `enterprise`，并选择一种模式：

- `greenfield/foundation-only`：只建立 IDD 和应用基础，不创建业务切片；
- `greenfield/starter-slice`：建立基础后，实现一个经过 Gate 的垂直特性；
- `brownfield`：围绕一个选定模块渐进式接入。

Greenfield 模式需确认产品边界、技术栈、包管理器、存储、环境和验证方式。Brownfield 模式应先从可追踪证据中推导，再进行询问。

## Greenfield

1. 澄清目标结果、用户、非目标、质量约束、环境和方案等级。
2. 起草 `.steering/constitution.md`、`tech-stack.md` 和 `conventions.md`。尚未实现的命令保留明确 TODO，不得猜测。
3. 展示完整 steering 草案，等待批准后再写入。
4. 将模板解压到临时目录并检查内容，把已确认的结构合并到目标，不得替换已有文件。
5. 初始化术语表、权限、空索引、validator 配置和 `.idd/` 目录。
6. 只搭建已确认的应用基础设施，并运行真实验证命令。

`foundation-only` 以项目结构、已验证命令和开放决策结束。`starter-slice` 将一个最小垂直切片移交 `$idd-develop-feature`，并继续执行 Gate 1 和 Gate 2。

## Brownfield

不得默认蒸馏整个仓库。

1. 读取指令、manifest、CI、脚本、源码边界、测试、文档、schema、部署配置和目标相关历史。
2. 为已有指令建立台账，分类为 `retain`、`rewrite`、`relocate`、`automate` 或 `delete`，并记录证据和风险。
3. 从证据推导候选 steering 规则。只询问仓库无法揭示的治理要求、领域含义、冻结区域或反复出现的问题。
4. 写入前展示 steering 提案和台账。删除或弱化规则必须获得批准。
5. 选择用户提供或批准的一个高价值模块。
6. 起草推导出的 intent 和 contracts，明确标记不确定的业务含义，并执行正常 Gate。
7. 获批后添加锚点并建立一致性校验基线。
8. 其他模块保持未蒸馏状态，只记录下一个候选模块。

只有必需文件已存在、已有内容得到保留、JSON 索引可解析、命令有证据支撑、验证已运行或已记录 blocker，并且 Brownfield 范围明确时，才能结束。
