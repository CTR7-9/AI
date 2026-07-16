---
name: byted-viking-cli
description: 官方Viking CLI 命令行助手：本CLI覆盖火山引擎/BytePlus VikingDB(向量库)/Knowledge(知识库)/Memory(记忆库)的数据集管理和数据的读写及检索，
  可用于扩展Agent的知识检索边界 提升Agent的记忆能力；
  当用户对知识库/向量库提问时，使用本Skill;
  当用要操作向量库/知识库 或 从向量库/知识库检索信息时使用本Skill；
  当��户要记忆检索和记忆存储时，使用本Skill。
version: 1.3.0
license: Apache-2.0
---

## 目标
把用户的需求转换为可直接执行的`viking-cli`命令并执行，如果覆盖不了则提示用户。
`viking-cli` 在用户安装后位于系统 `PATH` 中，直接执行 `viking-cli`。

## 安装 CLI
用户可用一条命令完成安装（免下载脚本）：
```bash
curl -fsSL https://viking-skills.tos-cn-beijing.volces.com/viking-cli/install.sh | bash
```

安装完成后验证：
```bash
viking-cli version
```

## 工作原则
- 涉及复杂 JSON、中文、嵌套数组时，优先推荐文件输入方式；如果当前命令不支持文件输入，再给命令行 JSON 示例。
- 如果用户没有指定collection，则可省略 `--collection` 的参数，默认使用配置文件中的 collection 。
- 如果用户需求超出当前 CLI 能力边界，要明确说“当前 CLI 未实现该子命令”。

(Excerpted from bytedance/agentkit-samples/skills/byted-viking-cli/SKILL.md)
