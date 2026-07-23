# Office PowerPoint MCP Server — Vendored Snapshot

This directory contains the exact source files installed locally from:

```text
office-powerpoint-mcp-server==2.0.7
```

The upstream files contain an internal version mismatch: the package metadata is `2.0.7`, while `get_server_info()` reports `2.1.0`. This vendored directory preserves the installed source unchanged and uses the package version `2.0.7` as the snapshot identifier.

Hermes currently launches the package with:

```bash
uvx --from office-powerpoint-mcp-server ppt_mcp_server
```

## Upstream

- Repository: [GongRzhe/Office-PowerPoint-MCP-Server](https://github.com/GongRzhe/Office-PowerPoint-MCP-Server)
- PyPI package: `office-powerpoint-mcp-server`
- Upstream author: GongRzhe
- License: MIT

This is a vendored installed snapshot for reproducibility and local deployment. It is not original MCP source code authored in this repository. The upstream MIT license is preserved in `LICENSE`.

## Local Installation

With `uv`:

```bash
uv sync
```

With standard Python tooling:

```bash
python -m pip install .
```

## Run

Start the stdio MCP server:

```bash
uv run ppt_mcp_server
```

Start the streamable HTTP server on port 8000:

```bash
uv run ppt_mcp_server --transport http --port 8000
```

## Hermes Configuration

```yaml
mcp_servers:
  ppt:
    command: uv
    args:
      - run
      - --project
      - /absolute/path/to/PowerPoint_MCP/mcp-server
      - ppt_mcp_server
    connect_timeout: 120.0
    enabled: true
```

Replace the example path with the real checkout path.

## Runtime Dependencies

- `fonttools>=4.0.0`
- `mcp[cli]>=1.8.0`
- `pillow>=8.0.0`
- `python-pptx>=0.6.21`

## Snapshot Contents

- `ppt_mcp_server.py` — console entry point and server registration
- `tools/` — presentation, content, template, chart, connector, master, transition, and design tools
- `utils/` — content, design, presentation, template, validation, and core helpers
- `slide_layout_templates.json` — built-in slide layout definitions
