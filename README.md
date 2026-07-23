# PowerPoint MCP and Hermes Skill

This repository contains the two components used by the local Hermes PowerPoint workflow:

1. `powerpoint-generator/` — the Hermes skill that controls requirements gathering, outline approval, content generation, layout rules, online image sourcing, batch construction, and presentation QA.
2. `mcp-server/` — a vendored source snapshot of `office-powerpoint-mcp-server==2.0.7`, the MCP server currently launched by Hermes through `uvx`.

## Current Local Runtime

The verified Hermes configuration uses:

```yaml
mcp_servers:
  ppt:
    command: uvx
    args:
      - --from
      - office-powerpoint-mcp-server
      - ppt_mcp_server
    connect_timeout: 120.0
    enabled: true
```

The locally cached package was verified as:

```text
Name: office-powerpoint-mcp-server
Version: 2.0.7
Entry point: ppt_mcp_server = ppt_mcp_server:main
```

The upstream snapshot contains an internal version mismatch: its installed package metadata is `2.0.7`, while `get_server_info()` reports `2.1.0`. This repository preserves the installed files unchanged and identifies the snapshot by its package version, `2.0.7`.

All cached copies of the installed server entry module had the same SHA-256 digest before this snapshot was created.

## Add Your Own PowerPoint Template

No company PowerPoint template is included in this repository.

To enable the optional company-template workflow, copy a template that you are authorized to use to:

```text
powerpoint-generator/assets/company-template.pptx
```

See `powerpoint-generator/assets/README.md` for the expected location. Do not commit a proprietary or confidential template to a public repository.

## Install the Hermes Skill

Copy the complete skill directory to:

```text
~/.hermes/skills/productivity/powerpoint-generator/
```

The final entry point must be:

```text
~/.hermes/skills/productivity/powerpoint-generator/SKILL.md
```

Start a new Hermes conversation after installation so that Hermes reloads the skill.

## Run the MCP Server

### Option A: Reproduce the current `uvx` setup

This is the simplest option and matches the currently verified Hermes configuration:

```bash
uvx --from office-powerpoint-mcp-server==2.0.7 ppt_mcp_server
```

Use the YAML configuration shown in **Current Local Runtime**. Add `==2.0.7` after the package name if you want to pin the exact uploaded version.

### Option B: Run the vendored local snapshot

Install or verify `uv`, then run:

```bash
cd mcp-server
uv sync
uv run ppt_mcp_server
```

To make Hermes use this local checkout:

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

Replace `/absolute/path/to/PowerPoint_MCP` with the real checkout path on that computer.

## Online Image Sourcing

The Hermes skill permits online image discovery when images materially improve a presentation. The destination Hermes installation must expose browser or image-search tools and allow network access. Downloaded visuals must be relevant, sufficiently large, free of watermarks, and accompanied by source and attribution information when required.

## Repository Structure

```text
PowerPoint_MCP/
├── README.md
├── LICENSE
├── .gitignore
├── powerpoint-generator/
│   ├── SKILL.md
│   ├── LICENSE
│   ├── template_rules.md
│   ├── content_guidelines.md
│   ├── slide_patterns.md
│   ├── assets/
│   │   └── README.md
│   └── scripts/
│       └── check_text_layout.py
└── mcp-server/
    ├── README.md
    ├── LICENSE
    ├── pyproject.toml
    ├── ppt_mcp_server.py
    ├── slide_layout_templates.json
    ├── tools/
    └── utils/
```

## Validation

Before publishing an update:

1. Validate `powerpoint-generator/` with the Hermes skill validator.
2. Parse every Python source file and the MCP `pyproject.toml`.
3. If you add a PowerPoint template, confirm that it opens without archive errors.
4. Start the MCP server and verify that it initializes successfully over stdio.
5. Open a new Hermes conversation and test the complete outline-to-PowerPoint workflow.

## Upstream Attribution

`mcp-server/` is a vendored snapshot of:

- Project: [GongRzhe/Office-PowerPoint-MCP-Server](https://github.com/GongRzhe/Office-PowerPoint-MCP-Server)
- PyPI package: `office-powerpoint-mcp-server`
- Installed snapshot version: `2.0.7`
- Upstream author: GongRzhe
- License: MIT

The upstream license is preserved in `mcp-server/LICENSE`. The vendored MCP source is not original code authored in this repository.

The Hermes skill code and Markdown documentation use their included license. Any template added by a user remains subject to its own usage and redistribution rights.
