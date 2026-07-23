---
name: powerpoint-generator
description: "PPT tasks: MUST load first. Missing inputs: stop and ask. Use for creating, revising, updating, improving, planning, or structuring any presentation, PowerPoint, deck, or slides in any language. Enforce the blocking requirements gate and explicit outline approval. After approval, generate the complete deck specification in one pass, batch-build editable slides, and run one whole-deck QA pass before making targeted fixes."
license: MIT for skill code and documentation; user-added templates may have separate rights. See LICENSE.
metadata:
  hermes:
    tags: [ppt, powerpoint, presentation, deck, slides, slide-deck, planning, comparison, academic, chinese, english, 幻灯片, 演示文稿, 汇报]
---

# PowerPoint Generator Skill

## How This Skill Works

This skill has two required layers:

1. **This file** — governs content, argument structure, and design standards for academic presentations. Read it fully before planning any slides.
2. **The enabled `ppt` MCP** — governs technical implementation such as creating, editing, and inspecting the `.pptx` file. Use it only after the requirements gate and outline-approval gate are open.

The built-in `powerpoint` skill is optional supplementary guidance. If it is disabled, continue with this skill and the enabled `ppt` MCP; never skip this skill's gates because the built-in skill is unavailable.

If the user provides an existing `.pptx` template, company template, institution template, or branded deck to imitate, also read:

3. **Template-specific rules** — preserve the template's master, layouts, colours, fonts, logos, and footer conventions. When a template is supplied or added to this skill, read [template_rules.md](template_rules.md).

**Always read all applicable files before writing any code or creating any files.**

## Output Language Default

- If the user explicitly specifies the presentation language, use that language.
- If the user does not specify the presentation language, create the deck in **English**.
- Do not infer the deck language from the language of the user's prompt. A Chinese request still produces an English deck unless the user explicitly requests Chinese or another language.
- Do not ask a language question when the user omitted it; English is the installed default.

## Non-Negotiable Execution State

Every presentation task starts in `BLOCKED_REQUIREMENTS` state. Enabling this skill, recognizing the topic, finding a template, or being able to infer plausible content does not open the gate.

Allowed while blocked:

- Identify which required inputs the user explicitly supplied.
- Read user-provided source material only when needed to determine what the user already supplied.
- Ask the user for missing required inputs.

Forbidden while blocked:

- Do not plan slides, draft an outline, allocate pages, generate content, call the `ppt` MCP, run presentation-building commands, or create/edit output files.
- Do not guess, infer, silently default, or retrieve missing planning decisions from prior unrelated sessions.
- Do not treat a topic-only prompt, an available company template, or existing source files as permission to proceed.

When inputs are missing, use the `clarify` tool if available; otherwise ask in a normal assistant response. If template choice is missing, ask the dedicated clickable template question defined in Gate A before asking open-ended questions. Ask only for missing items, then end the turn and wait for the user's answer.

After all required inputs are explicitly resolved, move to `BLOCKED_OUTLINE_APPROVAL`: propose the page allocation and slide-by-slide outline, then ask for approval. Do not call PPT generation/editing tools or create files until the user explicitly approves that outline. Only explicit approval starts the build pipeline: `GENERATE_DECK_SPEC` → `BATCH_BUILD` → `WHOLE_DECK_QA` → `TARGETED_FIXES` when needed.

## Universal PPT Routing Rule

This skill is no longer limited to academic triggering.

### Semantic routing rule (language-independent)

- Trigger this skill from the user's underlying task intent, not from any fixed keyword list.
- Do not rely on literal tokens such as `PPT`, `PowerPoint`, `.pptx`, `slides`, or any specific Chinese/English phrase as the deciding factor.
- Any language is valid. The same task should route to this skill whether the user asks in English, Chinese, or another language.
- The deciding question is: "Is the user asking the agent to create, modify, plan, structure, revise, or improve a presentation artifact?"
- If yes, load this skill.

### Examples are illustrative, not exhaustive

The following requests are only examples. They are not the routing rule and should not be treated as an exhaustive trigger list:

- "make a PPT"
- "create a PowerPoint"
- "build a deck"
- "generate slides"
- "prepare a presentation"
- "make an 8-slide deck comparing A and B"
- "revise this presentation for leadership"
- "revise this .pptx"
- "做PPT"
- "生成PPT"
- "做幻灯片"
- "做个演示文稿"
- "帮我做一份PPT"
- "帮我生成一个汇报"
- "帮我做一个对比演示"

Routing rule:

- If the request is functionally about producing or improving a presentation artifact, use this skill first for planning and requirements control even if the user never says the exact words "PPT" or "PowerPoint".
- Then use the `powerpoint` skill for the technical file operations.
- If the deck is academic, research, conference, seminar, thesis, grant, or evidence-heavy, apply the academic-specific standards in this file in full.
- If the deck is non-academic (business, product, strategy, comparison, internal review, sales, marketing, etc.), still apply the mandatory grill, outline approval, and structure discipline from this skill, but adapt style/tone to the user and do not force academic-only elements like citations or references unless the context requires them.

Anti-pattern:

- Do not decide whether to load this skill by checking whether the user used one of a few memorized phrases.
- Do not assume that a request in another language should bypass this skill just because it does not match a known keyword example.

---

## Quick Reference

| Task | Guide |
|------|-------|
| Content planning, argument structure, slide-by-slide rules | [content_guidelines.md](content_guidelines.md) |
| Per-slide-type patterns (title, methods, results, etc.) | [slide_patterns.md](slide_patterns.md) |
| Branded deck using a user-provided template | [template_rules.md](template_rules.md) |
| Technical creation or editing | Enabled `ppt` MCP after both gates are open |
| Optional supplementary implementation guidance | Built-in `powerpoint` skill, only when enabled |

---

## Step 1: Identify Presentation Type

Before planning a single slide, determine which mode applies.

### Company-branded academic mode

Use this whenever the user supplies a company template, asks to preserve an existing corporate style, or says colours / symbols / brand elements must not be changed.

**Priority order: template fidelity → argument structure → data clarity → layout refinement.**

Follow [template_rules.md](template_rules.md) in full, then apply the academic argument rules in this skill inside the locked template structure.

### Structured Argument (default for academic work)

Use for: conference papers, seminar talks, thesis defenses, dissertation chapters, grant briefings, internal lab presentations, policy briefings, consulting-style research deliverables.

**Priority order: argument structure → data → layout → aesthetics.**

Follow [content_guidelines.md](content_guidelines.md) in full.

### Visual / Narrative

Use for: public engagement talks, science communication to non-specialist audiences, funding pitches to lay panels, event keynotes.

Follow the PPTX skill's design-forward guidelines. Argument structure still matters, but visual storytelling and emotional engagement take priority.

### General business / product / comparison mode

Use for: product comparisons, internal reviews, strategy updates, vendor evaluations, sales decks, business cases, feature overviews, pros/cons presentations, and other non-academic presentation work.

Rules:

- Still run the mandatory grill and outline-approval workflow in this skill.
- Keep the structure explicit and decision-oriented.
- Use the `powerpoint` skill's design guidance unless the user provides a template or asks for a more analytical / academic style.
- Do not force citations, references, or academic deck architecture unless the user asks for them or the content clearly requires them.

### When in doubt

Default to **Structured Argument** for analytical or evidence-heavy work; default to **General business / product / comparison mode** for ordinary PPT requests that do not carry explicit academic signals. If the user mentions a paper, a study, a dataset, a thesis, a grant, or a conference, they almost certainly want structured argument mode.

---

## Step 2: Plan the Deck Before Creating Any Slides

Apply the following two gates to every presentation task, regardless of deck length, apparent simplicity, or available templates.

### Gate A: Required inputs

Do not proceed until the user has explicitly supplied or explicitly decided every item below:

1. **Audience** — who will read or see the deck.
2. **Objective** — inform, compare, persuade, request approval, defend research, sell, or another explicit purpose.
3. **Length** — target slide count or presentation duration.
4. **Template choice** — obtain an explicit selection through the clickable template chooser below. Do not silently choose a template.
5. **Source-material status** — identify the required files/data, or obtain explicit confirmation that no source material is required.
6. **Structure ownership** — obtain the user's required sections, or explicit permission for the agent to propose the structure and page allocation.
7. **Required/forbidden slides** — record requirements for agenda, appendix, references, closing, contact, pricing, comparison table, and similar slide types; obtain explicit confirmation when there are none.
8. **Consumption mode** — live presentation or asynchronous reading.

Do not substitute agent judgment for an answer. Words such as "reasonable," "confidently infer," "when relevant," and "materially affect" are not exemptions. If any item is unresolved, remain in `BLOCKED_REQUIREMENTS`, ask only for the missing items, and end the turn.

### Template chooser

An optional company template can be installed at:

- Skill-relative file: `assets/company-template.pptx`
- Resolved file: `${HERMES_SKILL_DIR}/assets/company-template.pptx`

Check whether that file exists before presenting the template choices.

If the file exists and the user did not explicitly choose a template, the first clarification must be a dedicated `clarify` call with exactly this structure:

```json
{
  "question": "Which template should I use for this presentation?",
  "choices": [
    "Company Template (Installed)",
    "I will provide another template",
    "Match an existing finished deck",
    "No template — use a custom style"
  ]
}
```

If the file does not exist, omit the installed-template choice:

```json
{
  "question": "Which template should I use for this presentation?",
  "choices": [
    "I will provide a template",
    "Match an existing finished deck",
    "No template — use a custom style"
  ]
}
```

Rules:

- Put each option in `choices`; never embed the options as numbered prose in `question`.
- Present `Company Template (Installed)` as the first choice only when the file exists.
- When the user selects it, record the template decision immediately and map it to `${HERMES_SKILL_DIR}/assets/company-template.pptx`.
- Before building, verify that the resolved installed-template file exists. Open/copy that `.pptx` as the base presentation and preserve its masters/layouts. Do not replace it with the PPT MCP's generic `modern_blue` scheme or built-in template IDs.
- If another choice requires a file or deck identifier, ask for that missing item in the next turn.
- After the template choice is resolved, ask one compact open-ended `clarify` question covering the remaining unresolved Gate A items. If only one or two items remain, ask only those items. Do not repeat or ask the user to reconfirm information already stated explicitly, including a requested slide count.

### Multi-item clarification formatting

When a `clarify` prompt asks for more than one missing requirement, format it as a vertical answer form:

- Put every numbered question on its own physical line.
- Keep each line short enough to avoid normal terminal wrapping.
- Insert a newline between items; never join questions with commas or place multiple numbered items in one paragraph.
- Use the user's interaction language for the questions. The deck's default output language does not control the clarification language.
- End with a request to reply using the same numbered lines.

Use this shape, omitting items that are already resolved:

```text
Please answer each item on its own line:

1. Audience?
2. Objective?
3. Sources? (files or none)
4. Structure? (provide it or ask me to propose)
5. Required/forbidden slides? (or none)
6. Mode? (live or asynchronous)

Reply using the same numbered lines.
```

For a Chinese interaction, use the equivalent compact form:

```text
请每项单独回答一行：

1. 受众？
2. 目标？
3. 资料来源？（文件或“无”）
4. 结构？（你提供，或由我建议）
5. 必须包含或禁止的页面？（或“无”）
6. 使用方式？（现场演示或异步阅读）

请按相同编号逐行回复。
```

### Gate B: Outline approval

After Gate A is complete:

1. Propose an explicit section-by-section page allocation.
2. Produce a slide-by-slide outline containing each slide's title, action title/takeaway, and intended exhibit or content type.
3. Run the ghost deck test and repair the outline if the action titles do not tell a coherent argument.
4. Ask the user to approve or adjust the proposed outline.
5. End the turn and wait.

This approval is mandatory for every deck, including decks of 10 slides or fewer and apparently simple requests. Do not start building, call the `ppt` MCP, run presentation-generation commands, or create/edit files until the user explicitly approves the outline.

Use the ghost deck test during planning: read only the proposed action titles in sequence. They must tell the complete argument. If they don't, fix the outline before building.

### Fast build pipeline after approval

After the user explicitly approves the outline, continue without adding another approval gate:

1. **`GENERATE_DECK_SPEC` — write the complete text version once.** Generate a structured specification for the entire deck before calling the `ppt` MCP. For every slide, include the slide number, selected layout, title, action title/takeaway, final body copy, exhibit or visual instructions, source/citation text when required, and speaker notes when requested. Compose all slide copy to the container budgets in this skill. Do not alternate between drafting one slide and building that slide.
2. **Validate the specification in memory.** Run the ghost deck test across all action titles, check page allocation, remove repetition, and shorten content that already exceeds the known layout budgets. This is a single content pass, not a slide-by-slide tool loop.
3. **`BATCH_BUILD` — populate the editable presentation.** Open or copy the selected template once. Create and populate all slides from the approved specification using the largest safe batch operations exposed by the `ppt` MCP. When a true batch operation is unavailable, perform the required write operations consecutively without reopening, rendering, optimizing, or inspecting each completed slide. Keep text, tables, charts, diagrams, and shapes as native editable PowerPoint objects. Save once after the complete population pass.
4. **`WHOLE_DECK_QA` — inspect once after the build.** Reopen or inspect the completed deck once, extract its text once, run the text-layout checker once, and render all slides in one batch. Review every rendered slide, but do not introduce a separate render/check round trip after each slide during construction.
5. **`TARGETED_FIXES` — repair only failures.** Fix only slides flagged by text extraction, layout checks, or visual review. Re-render affected slides during iteration. After targeted fixes, perform one final whole-deck verification pass.

Do not rasterize complete text slides into images as an intermediate or final presentation format. Whole-slide images make text uneditable and unsearchable, reduce accessibility, can blur when scaled, and often increase file size. Raster or SVG assets are appropriate only for genuine visual exhibits that cannot remain native PowerPoint objects.

---

## Step 3: Apply Design Standards

Academic presentations use **communication-first design**. These rules override the PPTX skill's design-forward defaults.

For non-academic decks, treat the academic design rules below as optional defaults rather than mandatory constraints. In non-academic contexts, preserve the user's template/style requirements first; otherwise prefer the `powerpoint` skill's design guidance while keeping this skill's planning discipline.

If the user has supplied a branded company template, these generic design defaults are secondary. In that case, preserve the template's visual system exactly and use these rules only for content density, argument structure, readability, and annotation discipline.

### Color

- White background for all content slides.
- One sans-serif font throughout (Arial, Calibri, or Helvetica — confirm with user or match their institution's template if provided).
- Maximum three colors: one primary, one accent, one for emphasis or alerts. Default: dark navy primary (`1F4E79`), mid-blue accent (`2E75B6`), white or off-white background.
- No decorative color gradients, no themed color palettes unless the user explicitly requests them.
- Use color to **direct attention** — highlight the key finding on a chart, mark a callout box — not for decoration.

If a company template is provided, treat its palette as locked. Do not substitute your own "better" academic colors.

### Typography

| Element | Size | Weight |
|---------|------|--------|
| Action title | 24–28 pt | Bold |
| Section header | 20–22 pt | Bold |
| Body bullets | 20 pt | Regular |
| Chart labels / annotations | 16–18 pt | Regular |
| Source citations on slides | 12–14 pt | Regular, muted color |

Single font face. Use size and weight for hierarchy — never multiple typefaces.

If the template specifies a corporate font and title-size cap, follow the template rather than these generic defaults.

### Layout

- Left-align all body text. Center only slide titles and axis labels.
- Consistent grid: all text boxes and figures align to the same margins (minimum 0.5" from slide edges).
- For result slides: figure on the left, interpretive bullets on the right. This matches natural left-to-right reading.
- White space is a signal of analytical clarity — do not fill every inch.
- 16:9 widescreen is the default. Confirm with the user if they know the venue's aspect ratio.

#### Peer-group, row, and circular-layout integrity

- Treat people, roles, requirements, stages, and other peer items as independent shapes; do not place a whole peer group in one auto-wrapping text box.
- Before placing a horizontal group, verify that `item_count × item_width + gaps` fits inside the safe content width. Before placing a circular group, verify every node and label against the slide bounds and reserved title/footer regions.
- Keep peer shapes equal in size and aligned to the same baseline or orbit. Prefer one-line labels; if one label must use two lines, apply a consistent two-line treatment or shorten it rather than letting one item wrap awkwardly.
- Never allow the final peer item to drop alone onto a new row. If one row does not fit, use balanced rows such as 3+2, 4+3, or 4+4; avoid 4+1, 6+1, or 7+1 orphan layouts.
- For radial diagrams, distribute nodes by calculated angles around one center. If labels collide or leave the safe area, shorten labels, enlarge the radius within bounds, or switch to a balanced grid/timeline; do not fake a circle with an overflow row beneath it.
- During whole-deck QA, flag any row with a single unintended trailing item, inconsistent peer wrapping, uneven gaps, or a node outside its intended group. Repair the group as one layout unit.

### Image completion rule

Treat every image-bearing layout as an asset-delivery obligation, not a suggestion. A slide is incomplete until each image slot contains a verified relevant visual or the slide has been changed to a layout that does not require an image.

#### Online image retrieval is enabled

After the outline is approved and before populating image-bearing slides:

1. Create a visual asset plan listing each slide that needs an image, the image's communication purpose, preferred subject, and target aspect ratio.
2. Use assets in this priority order:
   1. user-provided images, screenshots, charts, or figures
   2. visuals extracted or rebuilt from user-provided source material
   3. visuals already embedded in the installed template or an explicitly selected finished deck
   4. online visuals found with `web_search`, `browser_navigate`, `browser_get_images`, or an equivalent image-search/browser tool
3. Use online visuals when they materially improve explanation or visual balance. For an ordinary 8–10 slide deck, aim for meaningful visuals on roughly one-third to one-half of content slides; do not force an image onto every slide.
4. Prefer official product pages, primary sources, institutional media libraries, Wikimedia Commons, or clearly licensed sources. Avoid watermarked images, unclear-rights assets, and generic stock imagery that adds no information.
5. Record the source page URL and creator/license or attribution requirement for every downloaded visual. Put concise attribution on the slide or in speaker notes/references as appropriate.
6. Validate every candidate file before insertion:
   - it opens as a real PNG, JPEG, WebP, or SVG rather than HTML or an error page
   - it is not a tracking pixel, favicon, blank image, thumbnail placeholder, or broken file
   - its resolution is at least twice the intended displayed dimensions when practical, and its aspect ratio suits the slot
   - it is directly relevant to the slide's action title
7. Insert the verified image into the real template placeholder using the `ppt` MCP image operation. Crop proportionally; do not stretch or distort it.
8. Reopen or inspect the slide after insertion and confirm that the image object exists, occupies the intended frame, and does not cover titles, text, logos, page numbers, or footer elements.
9. When no suitable visual exists, choose the nearest no-image layout. Do not create an image slot that cannot be filled.

#### Hard failure behavior

- Do not leave an image placeholder empty.
- Do not leave placeholder instruction text such as "insert image," "image here," or a filename in the final deck.
- Do not draw a colored rectangle or decorative frame and treat it as a completed image.
- Do not use an irrelevant stock image merely to fill space.
- Do not use low-resolution, watermarked, distorted, misleading, or unattributed online visuals.
- If no suitable visual is available, switch to a text, chart, table, or diagram layout that does not contain an image slot. Preserve the template's brand system while changing layout.

If a template is provided, reuse its layouts instead of inventing new slide structures unless the user explicitly asks for a redesign.

### Text fit and overlap prevention

Treat non-overlapping, readable text as a build constraint, not a cosmetic QA preference.

#### Compose to the container budget

- Inspect the chosen layout and placeholder geometry with the PPT MCP before writing slide copy.
- For company-template content slides, keep the title to at most 2 rendered lines and normally at most 80 English characters or 32 CJK characters.
- Use no more than 5 body bullets on a single-column slide and no more than 4 bullets per column on a two-column slide.
- Keep each English bullet to about 12–14 words and each CJK bullet to about 22–26 characters. Use at most one indentation level.
- A comparison table should normally contain no more than 6 body rows and 4 columns. Split a larger table across slides instead of squeezing it.
- Draft concise slide copy first. Do not paste paragraph prose into placeholders and rely on font shrinking to make it fit.

#### Fixed readability floors

- Follow the selected template's intended title size and text hierarchy.
- Company-template body text should normally be 16–20 pt and must not be reduced below 16 pt merely to force content into a box.
- Citations, metadata, and footer text may use the template's smaller built-in styles, but must stay inside their dedicated regions.
- Never call `mcp__ppt__optimize_slide_text` with its default `min_font_size=8`. For company-template content slides, pass `min_font_size=16`; set `max_font_size` to the layout's intended maximum. Optimization is a finishing pass, not permission to exceed the content budget.

#### Mandatory fix order

If text does not fit or any unintentional overlap appears, repair it in this order:

1. Shorten copy and remove repetition.
2. Move secondary detail to speaker notes or an appendix.
3. Select a roomier existing layout.
4. Split the content across two slides and update the approved page allocation if necessary.
5. Adjust font size only within the allowed range; never cross the readability floor.

Do not reduce margins, stack text boxes, move content into the footer/logo/page-number safe zones, or hide overflow behind another shape.

#### Required overlap QA

- Maintain at least 0.12 inch between independent text boxes and at least 0.20 inch between content text and the footer/logo/page-number regions.
- After the complete deck is populated, inspect shape geometry in one whole-deck pass. Run `mcp__ppt__optimize_slide_text` with the explicit safe font range only on slides flagged by overflow, density, or visual review; do not optimize every slide by default.
- Render all slides in one batch, or generate one Quick Look preview for the completed deck, and visually inspect every slide at normal viewing scale. Geometry checks alone cannot detect glyph overflow, bad wrapping, or text clipped inside its own box.
- Run `scripts/check_text_layout.py OUTPUT.pptx` before delivery. Treat every reported text-overlap, out-of-bounds, or density warning as requiring visual inspection and correction; the script is a warning system, not a substitute for rendering.
- During repair, re-render only affected slides. Then run one final whole-deck verification pass and confirm there is no visible text overlap, clipping, or unreadably dense text.

### Avoid (Academic-Specific)

- **No decorative icons** — icons in colored circles, stock images, clip art are inappropriate for analytical academic presentations.
- **No accent lines under titles** — use whitespace instead.
- **No color palettes chosen for aesthetic interest** — use institution colors or the minimal defaults above.
- **No full-bleed background images on content slides** — reserve for title/section dividers only if desired.
- **No text-heavy slides** — if the audience is reading, they are not listening. Maximum ~40 words of body text per content slide.
- **No brand drift** — do not replace locked corporate colours, logos, footer text, or symbols with generic academic styling.
- **No empty image boxes** — never leave image placeholders blank in a final generated deck.

---

## Step 4: Build and QA

Follow the fast build pipeline above. Keep the expensive operations deck-wide and batched:

- Generate the complete deck specification before the first presentation write.
- Open the selected template once, populate the complete deck, and save once before QA.
- Run content extraction once on the completed deck, using `markitdown` when available.
- Render all slide images in one batch and inspect every slide.
- Fix only affected slides, then run one final whole-deck verification pass.

Fallback when the local environment blocks full render QA:
- If LibreOffice / `soffice` conversion is killed or unavailable, do not pretend the visual QA passed.
- Run an ad-hoc verification instead: reopen the generated `.pptx`, extract presentation text with the `ppt` MCP, and generate at least a Quick Look thumbnail on macOS (for example via `qlmanage`) if available.
- Report this explicitly as partial/ad-hoc verification, not as a full visual QA pass.
- If possible, also add a small temporary verification script under an OS-safe temp path to assert slide count and key expected text markers, then delete it after running.

**Additionally, run the formate-specific checks:**

Only run the full academic-specific checklist below when the deck is academic, research-facing, citation-bearing, or the user explicitly asks for academic style. For general business/product decks, keep the planning/outline/QA workflow but skip academic-only requirements such as references unless requested.

```
Academic QA checklist:
□ Every content slide has an action title (complete sentence stating the takeaway)
□ Ghost deck test passes (action titles alone tell the full argument)
□ One exhibit per results slide; each exhibit has a "so what" annotation
□ Every borrowed figure or data point has an in-slide citation
□ A References slide exists at the end
□ Conclusions slide is the last non-appendix substantive slide; if company style requires it, a branded closing / thank-you slide may follow
□ Contact information and/or QR code/link on the final slide
□ Font sizes are readable from the back of a room (≥ 20 pt body text)
□ No decorative elements that don't carry content
□ Section dividers or breadcrumb bar present for decks > 15 slides
□ If using a company template, brand colours / symbols / footer conventions remain unchanged
□ No required image placeholder is left empty; image layouts contain real visual content or were replaced with a better non-image layout
□ Every inserted visual was rechecked on the rendered/inspected slide for crop, overlap, distortion, and relevance
□ Every online visual has a recorded source URL and any required attribution/license note
□ Template-based text respects the selected layout's hierarchy and remains readable
□ The text-layout checker was run and every warning was visually reviewed and corrected
□ Every slide was rendered/previewed and checked for text overlap, clipping, and overflow
```

---

## Key Principles (Summary)

**Action titles, not topic labels.** Every slide title is a complete sentence stating the takeaway. Reading titles alone should tell the whole argument (ghost deck test).

**One argument, made well.** Don't present your whole paper. Pick the claim that can be made convincingly in the allotted time. Everything else goes in the appendix.

**One insight per slide.** One exhibit per results slide. Highlight the key finding directly on the chart — don't make the audience hunt for it.

**Slides support speech; they don't replace it.** Body text is for orientation, not information transfer. The presenter carries the argument; the slide carries the evidence.

**Cite everything borrowed.** Academic integrity applies to slides. In-text citations on the slide, full references on the References slide.

**End on conclusions by default.** The conclusions slide should be the last substantive slide and stay on screen during Q&A. If the company's real-world template style requires a branded thank-you / closing slide, that slide may follow as a separate corporate closer.

---

## Dependencies

Same as PPTX skill:
- `pip install "markitdown[pptx]"` — text extraction
- `npm install -g pptxgenjs` — creating from scratch
- LibreOffice (`soffice`) — PDF conversion
- Poppler (`pdftoppm`) — PDF to images
