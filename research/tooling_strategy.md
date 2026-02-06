# Project Chimera — Tooling Strategy

**Last Updated**: 2026-02-06

---

## 1. MCP Server Overview

Project Chimera uses Model Context Protocol (MCP) servers to extend AI agent capabilities. All MCP servers are configured in `.cursor/mcp.json` (project-level) or `~/.cursor/mcp.json` (global).

| Server | Purpose | Transport |
|--------|---------|-----------|
| **tenxfeedbackanalytics** | AI fluency tracking, passage time & performance triggers | SSE (remote) |
| **filesystem** | File read/write, directory operations, search | stdio (local) |
| **git** | Version control: status, diff, commit, branch | stdio (local) |

---

## 2. Configured Servers

### 2.1 tenxfeedbackanalytics (Existing)

- **Purpose**: AI fluency analytics and trigger logging
- **Tools**: `list_managed_servers`, `log_passage_time_trigger`, `log_performance_outlier_trigger`
- **Config**: Remote SSE; runs on Tenx infrastructure
- **Headers**: `X-Device`, `X-Coding-Tool` for client identification

### 2.2 filesystem

- **Purpose**: Secure file operations for development
- **Source**: [@modelcontextprotocol/server-filesystem](https://www.npmjs.com/package/@modelcontextprotocol/server-filesystem) (official Anthropic/MCP)
- **Tools**: `read_text_file`, `read_multiple_files`, `write_file`, `edit_file`, `create_directory`, `list_directory`, `move_file`, `search_files`, `get_file_info`, `list_allowed_directories`, `directory_tree`
- **Access**: Scoped to `${workspaceFolder}` (project root only)
- **Install**: `npx -y @modelcontextprotocol/server-filesystem` (no pre-install)

**Config**:
```json
{
  "filesystem": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-filesystem", "${workspaceFolder}"]
  }
}
```

### 2.3 git

- **Purpose**: Version control operations for Spec-Driven Development
- **Source**: [mcp-server-git](https://pypi.org/project/mcp-server-git/) (official MCP)
- **Tools**: `git_status`, `git_diff`, `git_diff_staged`, `git_diff_unstaged`, `git_add`, `git_reset`, `git_commit`, `git_log`, `git_show`, `git_branch`, `git_checkout`, `git_create_branch`, `git_init`
- **Install**: `uvx mcp-server-git` (requires [uv](https://docs.astral.sh/uv/))

**Config**:
```json
{
  "git": {
    "command": "uvx",
    "args": ["mcp-server-git"]
  }
}
```

**Alternative** (if `uv` not installed):
```json
{
  "git": {
    "command": "python",
    "args": ["-m", "mcp_server_git"]
  }
}
```
Requires: `pip install mcp-server-git`

---

## 3. Prerequisites

| Dependency | Required For | Install |
|------------|--------------|---------|
| **Node.js** | filesystem | [nodejs.org](https://nodejs.org) |
| **uv** | git (recommended) | `pip install uv` or [astral.sh/uv](https://docs.astral.sh/uv/) |
| **Python 3.10+** | git (alternative) | — |
| **Git** | git server operations | [git-scm.com](https://git-scm.com) |

---

## 4. SDD Alignment

Per Constitution and `specs/_meta.md`:

- **Traceability**: Git MCP supports commit messages with `Spec:` and `Test:` references
- **Skills vs Tools**: MCP servers are Tools (external, side-effectful); Skills are internal
- **Tool calls**: Must include `spec_id`, `call_purpose`, `call_authorization` when invoking MCP tools from agents

---

## 5. Adding New MCP Servers

1. Add entry to `.cursor/mcp.json` under `mcpServers`
2. Document in this file: purpose, tools, config, prerequisites
3. Update `.cursor/rules/project-chimera.mdc` if new tools affect Prime Directive or traceability

---

## 6. Troubleshooting

| Issue | Resolution |
|-------|------------|
| filesystem: "No allowed directories" | Ensure `${workspaceFolder}` resolves; Cursor uses project root |
| git: "uvx not found" | Install uv or switch to `python -m mcp_server_git` |
| Tools not visible in Cursor | Restart Cursor; check Settings → Tools & MCP; refresh server |
| tenx: Connection failed | Verify network; check headers match Tenx requirements |
