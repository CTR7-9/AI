---
name: ms-agent
version: 1.0.0
description: >-
  Access ms-agent's advanced AI capabilities via MCP tools: deep research,
  document research, financial research, code generation, video generation,
  web search (arxiv/exa/serpapi), LSP code validation (TypeScript/Python/Java),
  concurrent-safe file editing, and agent delegation. All project-level
  capabilities support async submit/check/get patterns. Use when the user
  asks to research a topic, analyze documents, generate code or videos,
  validate code, edit files, or delegate tasks. Requires ms-agent (pip install ms-agent).
metadata:
  nanobot:
    emoji: "🤖"
    requires:
      bins: ["python3"]
      env: []
  hermes:
    tags: [research, codegen, tools, mcp]
    category: ai-tools
---

# ms-agent Skills

This skill connects you to the **ms-agent Capability Gateway** — a unified
interface to ms-agent's projects, components, and atomic tools, exposed as
MCP tools.

## Setup

Verify ms-agent is installed:

```bash
python scripts/check_ms_agent.py
```

The MCP server must be configured in your agent's config. Pick the section
that matches your agent host.

### nanobot config.json

```json
{
  "tools": {
    "mcpServers": {
      "ms-agent": {
        "command": "python3",
        "args": ["-m", "ms_agent.capabilities.mcp_server"],
        "env": {"PYTHONPATH": "/path/to/ms-agent"},
        "toolTimeout": 300,
        "enabledTools": ["*"]
      }
    }
  }
}
```

(Excerpted from modelscope/ms-agent/ms-agent-skills/SKILL.md)
