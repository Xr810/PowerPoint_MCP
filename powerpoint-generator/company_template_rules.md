# Company Template Rules

This file records the company-specific presentation rules inferred from the user-provided PowerPoint template. These rules override the generic academic presentation defaults whenever a company-branded deck is requested.

## Source Template

Installed display name:
`Company Template (Installed, Default)`

Stable skill-relative copy:
`assets/company-template.pptx`

Resolved runtime path:
`${HERMES_SKILL_DIR}/assets/company-template.pptx`

Original user-provided template source:
Local source path intentionally omitted from this distribution package.

## Authority Order

For company-branded presentations, follow this order strictly:

1. User instructions
2. Official blank company template master/layout/logo/color/font/footer rules in this file and the `.pptx` template itself
3. Academic argument-structure guidance from `SKILL.md` and `content_guidelines.md`
4. Finished company decks only as secondary reference material when the official blank template does not specify enough
5. Generic PowerPoint skill design suggestions

If there is any conflict, preserve the official blank company template.

## Locked Brand Rules

### 1) Always build from the template

- Do not create a branded company deck from a blank presentation if the template is available.
- Start from the template and preserve the existing master, layouts, footer treatment, page numbering, and embedded brand assets.
- Replace placeholder content only; do not redesign the master unless the user explicitly asks for a template redesign.

### 2) Do not modify company symbols or logos

- Never redraw, recolor, stretch, crop, swap, simplify, or replace company logos/symbol marks embedded in the template.
- Reuse the existing embedded assets and layout placeholders from the template.
- If a slide needs a company symbol, copy it from the template instead of generating a new one.

### 3) Locked visual system inferred primarily from the official blank template

The official blank template is the primary visual authority. The following should be treated as locked unless the user explicitly asks otherwise:

- Aspect ratio: 16:9 widescreen
- Official template slide size: 10 x 5.625 inches
- Primary emphasis color in the template: `#F58220`
- Supporting warm neutral used in the template: `#E7E2D9`
- Content backgrounds are predominantly white / very light
- Dark text is used through the theme rather than decorative color-heavy text

Do not substitute a different palette unless the user explicitly asks.

### 4) Typography

- Theme major/minor Latin font in the original template: `helvetica`
- East Asian font in theme: `黑体`
- Use Helvetica first when creating a new company-branded deck from the official template.
- If editing an existing deck that already diverges from the template, preserve that deck's existing font system unless the user explicitly asks you to normalize it back to the official template.
- Template note on content layouts: `Title (Helvetica) 18pt or 20pt max.`
- Therefore, for company-branded content slides, do not freely enlarge titles. Standard content-slide titles should generally stay in the 18–20 pt range unless the chosen layout clearly supports something larger.
- Blank-template text styles provide enough baseline guidance to build responsibly even when the template contains only placeholder content:
  - cover title about 48 pt
  - cover subtitle about 24 pt
  - date about 18 pt
  - body hierarchy around 20 pt / 16 pt / 12 pt
  - footer around 8 pt

### 5) Footer / internal-marking treatment

Primary official-template footer / closing elements:
- `Confidential`
- `Page` with slide number
- official end-slide treatments built into the template

Rule:
- If starting from the official template, preserve its `Confidential` + `Page` treatment
- If editing or continuing an existing company deck that already diverges, preserve that deck's footer system unless the user explicitly asks to revert to the official template style
- Do not mix footer systems within the same deck unless the user explicitly asks for a redesign

### 6) Preferred layout families and what is probably editable

Available named layouts in the original template include:
- cover slide 1
- cover slide 2
- title slide
- directory slide
- chapter image slide
- chapter title slide
- content slide 1
- content slide 2
- content slide 3
- content slide 4
- content slide 5
- content slide 6
- content slide 7
- content slide 8
- content slide 9
- contact slide
- end slide 1
- end slide 2

From comparing the two finished decks, the following are likely editable content zones:
- Main slide title text
- Section / chapter heading text
- Body bullets and paragraph text
- Comparison tables and matrix content
- Architecture diagrams and screenshots
- Recommendation / verdict statements

The following are likely not editable unless the user explicitly asks:
- Overall page chrome and slide framing
- Brand color system
- Persistent footer / confidentiality markers of the source style you are working from
- Closing-slide treatment
- Repeated decorative brand accents that appear consistently across slides

For image-bearing layouts, the placeholder frame/layout is part of the template and should be preserved, but the image content inside it should be replaced with a real relevant visual rather than being left blank.

Online image discovery/download is enabled. Prefer user-provided or source-derived visuals, then template assets, then relevant online visuals from official, primary, institutional, Wikimedia Commons, or clearly licensed sources. Record the source URL and attribution/license requirement, validate the downloaded file and resolution, and preserve the template's image frame. If no suitable visual is available, change to the closest company-template layout without an image slot; never leave the original frame empty.

Use existing layout families instead of inventing new visual structures when possible.

## Recommended Workflow

1. Apply the blocking requirements gate in `SKILL.md`; do not build until every required input and the outline are explicitly approved.
2. If template choice is missing, call `clarify` with the clickable choices defined in `SKILL.md`. Offer `Company Template (Installed, Default)` first, but do not silently select it.
3. When the user selects `Company Template (Installed, Default)`, resolve it to `${HERMES_SKILL_DIR}/assets/company-template.pptx`; do not ask for a path or upload.
4. Open/copy the installed `.pptx` as the base presentation. Do not substitute PPT MCP generic themes or template IDs.
5. Choose the nearest existing company layout by name.
6. Replace placeholders with user content. Fill image layouts with verified provided, derived, embedded, or responsibly sourced online visuals; otherwise choose a no-image layout.
7. Keep brand assets, page numbering, and confidential markers intact.
8. Apply academic content rules inside the existing branded structure.
9. QA both for argument quality and template fidelity.

## Inference From The Two Finished Comparison Decks

By comparing both completed decks, these practical rules seem reliable:

- The company style in real use is more informative and denser than the blank template alone suggests
- Comparison tables with repeated left/right product columns are an accepted slide pattern
- A strong orange accent (`#F58220`) is consistently reused for emphasis and therefore should be preserved
- The actual delivered decks may use a footer system closer to `Internal Use Only` + date + numeric page number than to the older `Confidential` template footer
- A `Thank You` ending slide is an observed production option

These finished decks should be treated as secondary reference only. Use them to infer content density, comparison-slide patterns, and practical page composition when the official blank template is silent. Do not let them override the official template's font, footer, or master rules unless the user explicitly asks for that finished-deck style.

## Academic-Specific Adaptation Rule

The academic skill normally prefers ending on a conclusions slide rather than a generic thank-you slide. For company-branded academic decks:

- Keep the final substantive slide as Conclusions / Recommendations when possible
- If the user also wants the corporate end/contact/thank-you slide, place it after conclusions as a branded closing slide
- Do not delete the company end slide format if the user specifically wants the corporate template fully preserved
- The finished comparison decks show that a dedicated `Thank You` closing slide is a valid company usage pattern, but it does not override the official blank template by default

## QA Checklist Addendum: Brand Fidelity

Before finalizing a company-branded deck, verify:

- The deck still matches the official blank template unless the user explicitly requested a different existing-deck style
- Company logos/symbols are unchanged
- Brand colors were preserved (`#F58220`, `#E7E2D9`, white/light backgrounds)
- Fonts remain consistent with the official template unless the user explicitly requested preservation of an existing divergent deck
- Footer elements such as `Confidential` and `Page` numbering still match the official template unless the user explicitly requested another source style
- No new decorative motifs were introduced that conflict with the template
- If using comparison-slide patterns, column structure and verdict/callout treatment remain visually consistent across slides
- No image-bearing template slot is left empty in the final deck
- Image-bearing layouts contain verified inserted image objects, not empty frames, placeholder text, or decorative rectangles
- Every online visual has a recorded source URL and any required attribution/license note
- Content titles remain within the template's 18–20 pt cap and normally occupy no more than two rendered lines
- Body text is normally 16–20 pt and is never reduced below 16 pt merely to force-fit content
- Dense content is shortened, moved, re-laid out, or split across slides before any font-size reduction
- Every slide passes rendered visual inspection for text overlap, clipping, and overflow
