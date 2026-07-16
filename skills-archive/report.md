# 聚合报告（初始）

概述
- 本次抓取目标：深度抓取公开仓库中与 Agent / Skill / Prompt 相关的资源，包含 SKILL.md、prompt 模板、agent manifests、示例脚本和 SDK 示例。
- 输出：本仓库分支下的 skills-archive/ 目录包含聚合报告与来源清单；后续我可继续补抓并把每个文件原样包含在目录中。

关键发现（摘要）
- 主流实现与约定
  - Anthropic 提供了完整的 Skill API（create/list/versions/download），并在其 SDK 中放置了 skill 管理与下载工具（可直接 programmatic 下载 skill zip）。
  - ModelScope 定义了 ms-agent 的 SKILL.md 格式与 CLI（modelscope skills add），便于 skill 的集中管理与分发。
  - 多个组织（OpenAI、Google、ByteDance）在各自 repo 中以 SKILL.md / prompts.md / scripts/prompts_*.py 的形式维护 prompt 库与示例，适合直接搬运或转换为统一 Skill package。

可复用模板与建议
- 通用 SKILL.md frontmatter（建议 schema）
  ```yaml
  ---
  name: "summarizer.simple"
  version: "0.1.0"
  author: "your-name"
  description: "对文章/文档生成 TL;DR 摘要"
  entrypoint: "invoke"
  inputs:
    - name: "text"
      type: "string"
      required: true
  outputs:
    - name: "summary"
      type: "string"
  examples: []
  ---
  ```

- 推荐工程化步骤
  1. 将所有 prompt/skill 文件放入统一目录结构： skills/<org>/<repo>/<skill-id>/...
  2. 为每个 skill 提供 tests/inputs/*.json 与 expected_output.json，纳入 CI
  3. 提供 skill metadata（license、author、tags、version）并自动生成 catalog index（JSON/CSV）
  4. 对每个 skill 生成 schema 化的调用协议（JSON Schema）以便工具化校验
  5. 对外部调用（API/网络）添加权限与速率限制

高价值 prompt 示例（摘录）

- bytedance/AnewOmni/docs/ui/prompt-language-design.md — PromptProgram 抽象与分层设计（摘录）

```markdown
The purpose is not to replace the existing backend templates, but to provide a unified, composable, and interactive abstraction on top of them so users can control generation by writing prompt programs.

Target modalities:

- small molecules
- peptides
- antibodies

Core principles:

- users interact with a `PromptProgram`, not directly with backend template internals
- the model consumes a unified intermediate representation
- the surface API should feel like Python so it works in both REPL and browser demos

## Architecture

The design uses three layers.

### User Layer

Users construct a prompt through a Python-like API:

```python
graph = MoleculePrompt()
graph.add_fragment("c1ccccc1")
graph.add_filter(MolBeautyFilter(th=1))
graph.run_generation(save_dir="./outputs/mol_case")
```

### Compiler Layer

Prompt objects are compiled into an intermediate representation containing:

- nodes
- edges
- filters
- generation metadata
```

接下来的工作流
- 我将继续抓取更多文件并在此分支内补充完整的 skill 档案（每个 skill 的 SKILL.md、prompts、示例脚本）。
- 抓取完成并经你确认后，我可以在该分支创建 Pull Request 合并到默认分支，或按你要求导出 ZIP。

---
