# PowerPoint Generator for Hermes

A portable Hermes skill for planning, generating, and quality-checking PowerPoint presentations.

## Features

- Generates the complete slide-by-slide content specification after outline approval
- Batch-builds an editable PowerPoint presentation instead of repeatedly generating and checking one slide at a time
- Detects orphaned peer items in rows, circular diagrams, people layouts, and requirement groups
- Supports online image search with source, attribution, relevance, and image-quality checks
- Includes a company PowerPoint template and template-specific brand rules
- Includes a script for detecting text overflow, overlap, and excessive content density

## Repository Visibility

This repository should remain **private**.

`powerpoint-generator/assets/company-template.pptx` contains company template styling, `Confidential` markings, and original PowerPoint document metadata. Do not publish this file in a public repository unless you have confirmed that you are authorized to distribute the template publicly.

The skill code and Markdown documentation use the included MIT License. Rights to use or redistribute the bundled company template must be confirmed separately.

## Installation

Install Hermes on the destination computer, then copy the complete `powerpoint-generator` directory to:

```text
~/.hermes/skills/productivity/powerpoint-generator/
```

Confirm that this file exists:

```text
~/.hermes/skills/productivity/powerpoint-generator/SKILL.md
```

Enable the PowerPoint MCP server in `~/.hermes/config.yaml`:

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

The destination computer also needs:

- A working `uvx` installation
- Access to download or run `office-powerpoint-mcp-server`
- Hermes browser or image-search tools for online image sourcing
- Network access for searching and downloading images

Start a new Hermes conversation after installation so that Hermes loads the skill again.

## Using GitHub for Synchronization

A private GitHub repository is preferable to repeatedly sending ZIP archives:

- It preserves the history of every skill update
- Multiple computers can synchronize changes with `git pull`
- Previous versions can be restored when necessary
- ZIP archives can still be used for initial transfer or offline backup

Upload this complete repository directory to a private GitHub repository. On another computer, clone the repository and copy or symlink its `powerpoint-generator` directory into the Hermes skills directory.

Example:

```bash
git clone https://github.com/Xr810/PowerPoint_MCP.git
mkdir -p ~/.hermes/skills/productivity
cp -R PowerPoint_MCP/powerpoint-generator \
  ~/.hermes/skills/productivity/powerpoint-generator
```

## Repository Structure

```text
PowerPoint_MCP/
├── README.md
├── LICENSE
├── .gitignore
└── powerpoint-generator/
    ├── SKILL.md
    ├── LICENSE
    ├── company_template_rules.md
    ├── content_guidelines.md
    ├── slide_patterns.md
    ├── assets/
    │   └── company-template.pptx
    └── scripts/
        └── check_text_layout.py
```

## Validation

Before distributing an updated version:

1. Validate the skill directory with the skill validation tool.
2. Confirm that the PowerPoint template opens without archive errors.
3. Run `scripts/check_text_layout.py` against a generated presentation.
4. Open a new Hermes conversation and test a complete outline-to-PowerPoint workflow.
