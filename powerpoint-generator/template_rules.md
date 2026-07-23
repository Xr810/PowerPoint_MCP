# User-Provided Template Rules

Use these rules whenever the user supplies a PowerPoint template or places one at `assets/company-template.pptx`.

## Template Authority

Follow this priority order:

1. Explicit user instructions
2. The supplied template's masters, layouts, theme, placeholders, and embedded brand assets
3. Content and layout guidance in `SKILL.md`
4. Generic PowerPoint design defaults

## Required Behaviour

- Verify that the template file exists and opens successfully before building.
- Start from a copy of the template instead of recreating its appearance from a blank presentation.
- Preserve slide size, masters, layouts, theme colours, fonts, logos, footers, page numbering, and recurring decorative elements.
- Replace editable placeholder content without altering locked brand elements.
- Choose the closest existing layout for each slide before creating a new layout.
- Do not redraw, recolour, stretch, crop, or replace logos unless the user explicitly requests it.
- When editing an existing deck, preserve its established visual system unless the user asks for a redesign.
- If an image placeholder is used, fill it with a relevant, verified visual; otherwise choose a layout without an image slot.

## Online Images

Online image discovery is allowed when it materially improves the presentation and the environment provides browsing or image-search tools.

- Prefer user-provided and source-derived visuals first.
- Prefer official, primary, institutional, Wikimedia Commons, or clearly licensed sources.
- Record the source URL and any attribution or license requirement.
- Reject watermarked, irrelevant, corrupted, or insufficient-resolution images.
- Crop images to the existing frame without distorting them.

## QA Checklist

- The output still uses the original template's masters and slide size.
- Theme colours, fonts, logos, footers, and page numbering are preserved.
- No placeholder text or empty image frames remain.
- Text fits without overflow and remains readable.
- Online visuals have recorded sources and required attribution.
- The final `.pptx` remains editable.
