# PowerPoint Generator for Hermes

这是一个可迁移的 Hermes PowerPoint 生成 Skill。它包含：

- 大纲确认后的整套文字内容一次生成
- 批量构建可编辑 PowerPoint
- 同级节点、人物、Requirements 和环形布局的孤儿项检查
- 在线图片搜索、来源记录与图片质量检查
- 公司 PowerPoint 模板和品牌规则
- 文本溢出、重叠和密度检查脚本

## 仓库可见性

建议将这个仓库设为 **Private**。

`powerpoint-generator/assets/company-template.pptx` 包含公司模板样式、`Confidential` 标记以及原始 PowerPoint 文档元数据。除非你确认拥有公开分发模板的权利，否则不要把该文件上传到公开仓库。

Skill 的代码和 Markdown 文档沿用目录中的 MIT License；公司模板的使用和分发权需要单独确认。

## 安装到另一台电脑

确保另一台电脑已经安装 Hermes，然后把整个 `powerpoint-generator` 文件夹复制到：

```text
~/.hermes/skills/productivity/powerpoint-generator/
```

最终应当存在：

```text
~/.hermes/skills/productivity/powerpoint-generator/SKILL.md
```

在 `~/.hermes/config.yaml` 中启用 PowerPoint MCP：

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

另一台电脑还需要：

- 可以运行 `uvx`
- 可以下载或运行 `office-powerpoint-mcp-server`
- Hermes 提供浏览器或图片搜索工具，在线配图功能才会生效
- 网络访问允许搜索和下载图片

安装完成后新开一个 Hermes 对话，让 Skill 重新加载。

## 上传到 GitHub

长期使用时，GitHub 私有仓库比反复通过邮件发送 ZIP 更合适：

- 可以保留每次 Skill 修改记录
- 多台电脑可以通过 `git pull` 同步
- 出现问题时可以回滚到旧版本
- ZIP 可以作为第一次迁移或离线备份

可以将解压后的整个目录上传到一个新的 Private GitHub repository。后续在其他电脑上通过 `git clone` 获取，然后复制或软链接其中的 `powerpoint-generator` 文件夹到 Hermes Skills 目录。

## 包含的文件

```text
powerpoint-generator-hermes/
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
