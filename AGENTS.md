# AeroCV — Agent Usage Guide

This guide explains how to use AeroCV with local coding agents (Qwen Code, Claude Code, Cline, Continue, Roo Code, Kilo, and other VS Code extensions).

## Two System Prompts

AeroCV provides **two separate system prompts** optimized for different agent types:

| File | Target | Execution Environment |
|------|--------|----------------------|
| `SYSTEM_PROMPT_CODE_AGENTS.md` | **Local code agents** (Claude Code, Qwen Code, Codex, Cline, Roo Code) | Direct filesystem + shell access, `typst compile` in terminal |
| `SYSTEM_PROMPT_TYPST.md` | **Chat / cloud models** (GPT, Gemini, ChatGPT) | Sandboxed Python, ZIP extraction, `/mnt/data/` workspace |

**Local agents** should read `SYSTEM_PROMPT_CODE_AGENTS.md`. It has shell-based compilation commands, filesystem paths, and no Python ZIP extraction steps.

**Cloud agents** should read `SYSTEM_PROMPT_TYPST.md`. It has Python-based ZIP extraction and `subprocess.run` compilation for sandboxed environments.

## Prerequisites

1. **Typst** installed and available in PATH (or `typst.exe` / `typst` binary in project root)
   - Install: https://github.com/typst/typst/releases
   - Verify: `typst --version`

2. **Fonts** — each template has its own `fonts/` directory. When compiling, point typst to the correct font path.

## Project Structure (Agent-Relevant)

```
AeroCV/
├── templates/                       # 9 resume templates
│   └── <id>/
│       ├── source/                  # .typ source files
│       ├── fonts/                   # Template-specific fonts
│       └── packages/                # Typst packages (if needed)
├── cover_letters/                   # 4 cover letter templates
├── template_images/                 # Preview PNGs
├── schemas/                         # JSON schemas
├── scripts/                         # Build & test scripts
├── docs/                            # ATS guide, roadmap
├── output_pdfs/                     # ⬅️ Generated PDFs (gitignored)
├── packages/                        # Shared Typst packages (fontawesome, linguify)
├── SYSTEM_PROMPT_CODE_AGENTS.md     # ⬅️ Prompt for local code agents
├── SYSTEM_PROMPT_TYPST.md           # ⬅️ Prompt for chat/cloud models
├── templates_registry.json          # Machine-readable template catalog
├── quick_reference.json             # Abbreviated template info
└── AGENTS.md                        # This file
```

## Quick Workflow for Local Code Agents

### Step 1: Read Template Info

```
Read quick_reference.json → pick template ID
Read SYSTEM_PROMPT_CODE_AGENTS.md → get import syntax, compilation rules, code examples
```

### Step 2: Generate .typ File

Create a `.typ` file in the template's source directory or in `output_pdfs/`. Use the import syntax from `SYSTEM_PROMPT_CODE_AGENTS.md`.

### Step 3: Compile

```bash
typst compile --font-path templates/<id>/fonts <file>.typ output_pdfs/<output>.pdf
```

For templates with packages (modern-cv, brilliant-cv), set XDG_DATA_HOME:

```bash
# Linux/macOS
export XDG_DATA_HOME="$PWD/packages"
typst compile --font-path templates/<id>/fonts <file>.typ

# Windows (PowerShell)
$env:XDG_DATA_HOME = "$PWD\packages"
typst compile --font-path templates\<id>\fonts <file>.typ
```

### Step 4: Output

PDFs go to `output_pdfs/` (gitignored). Move or share from there.

## Quick Workflow for Cloud/Chat Agents

1. Read `quick_reference.json` → discover templates
2. Read `SYSTEM_PROMPT_TYPST.md` → get Python-based compilation steps
3. Extract template ZIP, generate Typst, compile via `subprocess.run`
4. Deliver PDF

## Template Quick Reference

| ID | Import | Best For | Photo | Cover Letter |
|----|--------|----------|-------|-------------|
| `brilliant-cv` | `#import "lib.typ": cv, cv-section, cv-entry` | Universal, ATS, multi-lang | Configurable | Yes |
| `modern-cv` | `#import "lib.typ": *` | Tech, corporate | Circular | Yes |
| `vantage` | `#import "vantage-typst.typ": *` | Tech, clean | No | No |
| `designer-cv` | `#import "designer-cv.typ": *` | Creative, design | Circular | Yes |
| `executive-cv` | `#import "executive-cv.typ": *` | Execs, conservative | Strict right | Yes |
| `portfolio-cv` | `#import "portfolio-cv.typ": *` | Devs, project-focused | Rounded | Yes |
| `typst-cv` | `#import "template.typ": conf, show_skills` | General, simple | Rectangular | No |
| `vercanard` | `#import "main.typ": *` | Minimal, single-page | No | No |
| `neat-cv` | (see source) | Bilingual EN/FR | Left side | Yes |

**Default recommendation**: `brilliant-cv` — most versatile, ATS-friendly, supports cover letters.

## Agent-Specific Configuration

### Claude Code (Anthropic CLI)

Create `CLAUDE.md` in project root (Claude Code reads this automatically):

```markdown
# AeroCV Project

Typst-based CV/resume generator with 9 templates.

## Commands
- Compile: `typst compile --font-path templates/<TEMPLATE_ID>/fonts <file>.typ output_pdfs/<output>.pdf`
- For modern-cv/brilliant-cv: set XDG_DATA_HOME to ./packages first
- Test all: `python scripts/test_all_templates.py`

## Key Files
- SYSTEM_PROMPT_CODE_AGENTS.md: template syntax & compilation rules for local agents
- SYSTEM_PROMPT_TYPST.md: template syntax & compilation rules for cloud/chat agents
- quick_reference.json: template catalog
- templates_registry.json: detailed template metadata

## Rules
- Always write generated .typ files to output_pdfs/ or the template's source/ dir
- Never commit PDFs or personal data
- Prefer brilliant-cv as default template
- Read SYSTEM_PROMPT_CODE_AGENTS.md before generating any .typ code
```

### Qwen Code (Qwen CLI)

Create `.qwen/agent.md` or add to project instructions:

```markdown
Same content as CLAUDE.md above. Qwen Code reads project-level instruction files.
```

### Cline / Roo Code (VS Code Extension)

Add to `.vscode/settings.json` (if not gitignored locally):

```json
{
  "cline.customInstructions": "This is AeroCV, a Typst CV generator. Read SYSTEM_PROMPT_CODE_AGENTS.md before creating .typ files. Compile with: typst compile --font-path templates/<id>/fonts. Output PDFs to output_pdfs/."
}
```

Or create `.clinerules` file in project root:

```
Read SYSTEM_PROMPT_CODE_AGENTS.md before generating Typst code.
Use brilliant-cv as default template.
Compile: typst compile --font-path templates/<TEMPLATE_ID>/fonts <file>.typ output_pdfs/<output>.pdf
For modern-cv/brilliant-cv, set XDG_DATA_HOME=./packages
Never commit PDFs or personal data to output_pdfs/.
```

### Continue (VS Code Extension)

Add to `.continue/config.yaml`:

```yaml
contextProviders:
  - name: file
    params:
      filePaths:
        - SYSTEM_PROMPT_CODE_AGENTS.md
        - quick_reference.json
```

### Kilo

Already configured via `.kilo/` directory. The `AGENTS.md` file is read automatically.

## Common Compilation Issues

| Issue | Fix |
|-------|-----|
| `font not found` | Add `--font-path templates/<id>/fonts` to compile command |
| `package not found` | Set `XDG_DATA_HOME` to `packages/` dir |
| `@` in email causes error | Use `@` only inside strings: `"user@example.com"` |
| `image(` without `#` | Always use `#image(...)` — never bare `image(...)` |
| `<` / `>` in text | Escape: `\<` and `\>` |
| Cover letter not rendering | Only `brilliant-cv` and `modern-cv` support cover letters natively |

## Testing

```bash
python scripts/test_all_templates.py
```

This compiles every template and reports success/failure. Output goes to `output/`.

## Rebuilding Agent Output (for GPT/Cloud agents)

```bash
python scripts/pack_per_template.py
```

This creates per-template ZIPs in `agent_output/` with all files needed for cloud-based GPT agents.

## Contributing

When adding a new template:
1. Add source files to `templates/<id>/source/`
2. Add fonts to `templates/<id>/fonts/`
3. Add preview to `template_images/resumes/<id>-preview.png`
4. Update `templates_registry.json` and `quick_reference.json`
5. Update `SYSTEM_PROMPT_CODE_AGENTS.md` and `SYSTEM_PROMPT_TYPST.md` with import syntax
6. Run `python scripts/test_all_templates.py` to verify
