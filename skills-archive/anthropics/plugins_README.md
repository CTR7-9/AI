# Claude Code Plugins — README (excerpt)

This directory contains some official Claude Code plugins that extend functionality through custom commands, agents, and MCP servers. These are examples of what's possible with the Claude Code plugin system—many more plugins are available through community marketplaces.

## Plugins in This Directory

| Name | Description | Contents |
|------|-------------|----------|
| [agent-sdk-dev](./agent-sdk-dev/) | Development kit for working with the Claude Agent SDK | **Command:** `/new-sdk-app` - Interactive setup for new Agent SDK projects<br>**Agents:** `agent-sdk-verifier-py`, `agent-sdk-verifier-ts` - Validate SDK applications against best practices |
| [claude-opus-4-5-migration](./claude-opus-4-5-migration/) | Migrate code and prompts from Sonnet 4.x and Opus 4.1 to Opus 4.5 | **Skill:** `claude-opus-4-5-migration` - Automated migration of model strings, beta headers, and prompt adjustments |
| [code-review](./code-review/) | Automated PR code review using multiple specialized agents with confidence-based scoring to filter false positives | **Command:** `/code-review` - Automated PR review workflow<br>**Agents:** 5 parallel Sonnet agents for CLAUDE.md compliance, bug detection, historical context, PR history, and code comments |

(Excerpted from anthropics/claude-code/plugins/README.md)
