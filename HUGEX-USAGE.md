# HUGEX Usage Guide

Simple Docker container with AI coding agents.

## Quick Start

```bash
# AI code analysis with Codex CLI
docker run -e OPENAI_API_KEY="sk-proj-..." \
  -e REPO_URL=https://github.com/user/repo \
  -e PROMPT="analyze this codebase" \
  codex-universal-explore:dev /opt/agents/codex
```

## Available Agents

- **`/opt/agents/codex`** - OpenAI Codex CLI (recommended)
- **`/opt/agents/mcp`** - Python MCP client (legacy)

## Codex Agent Examples

### Code Analysis
```bash
docker run -e OPENAI_API_KEY="sk-proj-..." \
  -e REPO_URL=https://github.com/drbh/simu \
  -e PROMPT="explain what this code does" \
  codex-universal-explore:dev /opt/agents/codex
```

### Fix Bugs
```bash
docker run -e OPENAI_API_KEY="sk-proj-..." \
  -e REPO_URL=https://github.com/user/repo \
  -e PROMPT="fix the authentication bug" \
  codex-universal-explore:dev /opt/agents/codex
```

### Add Features
```bash
docker run -e OPENAI_API_KEY="sk-proj-..." \
  -e REPO_URL=https://github.com/user/repo \
  -e PROMPT="add error handling to the API" \
  codex-universal-explore:dev /opt/agents/codex
```

### Generate Tests
```bash
docker run -e OPENAI_API_KEY="sk-proj-..." \
  -e REPO_URL=https://github.com/user/repo \
  -e PROMPT="write unit tests for the main functions" \
  codex-universal-explore:dev /opt/agents/codex
```

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `OPENAI_API_KEY` | ✅ | - | Your OpenAI API key |
| `REPO_URL` | ✅ | - | Git repository URL |
| `PROMPT` | ❌ | "Fix the typos in the README" | What you want the AI to do |
| `LLM_MODEL` | ❌ | `o4-mini` | Model: `o4-mini`, `gpt-4o`, `o3` |

## Interactive Mode

```bash
# Drop into shell, then run agents manually
docker run -it codex-universal-explore:dev

# Inside container:
export OPENAI_API_KEY="sk-proj-..."
export REPO_URL=https://github.com/user/repo
/opt/agents/codex
```

## Help

```bash
# Get help for any agent
docker run codex-universal-explore:dev /opt/agents/codex --help
```

That's it! Simple AI-powered code automation in a container.
