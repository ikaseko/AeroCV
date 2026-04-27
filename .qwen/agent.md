# AeroCV Project

Typst-based CV/resume generator with 9 templates.

## Commands
- Compile: `typst compile --font-path templates/<TEMPLATE_ID>/fonts <file>.typ output_pdfs/<output>.pdf`
- For modern-cv/brilliant-cv: set XDG_DATA_HOME to ./packages first (Windows: `$env:XDG_DATA_HOME = "$PWD\packages"`)
- Test all: `python scripts/test_all_templates.py`

## Key Files
- SYSTEM_PROMPT_CODE_AGENTS.md: template syntax & compilation rules for local agents
- quick_reference.json: template catalog
- templates_registry.json: detailed template metadata
- AGENTS.md: full agent integration guide

## Rules
- Always write generated .typ files to output_pdfs/ or the template's source/ dir
- Never commit PDFs or personal data
- Prefer brilliant-cv as default template
- Read SYSTEM_PROMPT_CODE_AGENTS.md before generating any .typ code
- Escape `<` and `>` in text as `\<` and `\>`
- Use `@` only inside strings: `"user@example.com"`
- Always use `#image(...)` — never bare `image(...)`
