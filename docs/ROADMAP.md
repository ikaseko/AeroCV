# Roadmap: Custom CV Template Generation in Typst

## Overview

This roadmap outlines the process for creating, importing, and managing custom CV templates in the AeroCV system.

---

## Phase 1: Template Discovery (Week 1)

### 1.1 Find Templates

**Sources:**
- [Typst Templates](https://typst.app/templates)
- [GitHub Typst CV](https://github.com/search?q=typst+cv)
- [Typst Universe](https://typst.app/universe)

**Criteria:**
- [ ] MIT/Apache/BSD license
- [ ] Active maintenance (updated in last 6 months)
- [ ] Clear documentation
- [ ] Example output (PDF/PNG)
- [ ] No complex dependencies

### 1.2 Evaluate Templates

**Checklist:**
```markdown
- [ ] Structure analysis complete
- [ ] Dependencies identified
- [ ] Font requirements documented
- [ ] Preview image available
- [ ] ATS compatibility verified
- [ ] Cover letter support (optional)
```

### 1.3 Import Template

**Steps:**
1. Clone repository to `_temp_import/`
2. Run `python analyze_templates.py`
3. Run `python organize_templates.py`
4. Verify structure in `templates/<id>/`

---

## Phase 2: Template Integration (Week 2)

### 2.1 Build Assets

**Required Files:**
- Typst Linux binary (39.7 MB)
- Fonts (if custom)
- Packages (from @preview)

**Command:**
```bash
python build_template_assets.py --template <template-id>
```

### 2.2 Update Registry

**Edit `templates_registry.json`:**
```json
{
  "templates": [
    {
      "id": "new-template",
      "name": "New Template Name",
      "type": "resume",
      "paths": {
        "assets": "templates/new-template/assets/typst_assets.zip",
        "source": "templates/new-template/source",
        "templateFile": "templates/new-template/source/main.typ"
      },
      "preview": {
        "image": "template_images/resumes/new-template-preview.png"
      }
    }
  ]
}
```

### 2.3 Add Preview Image

**Requirements:**
- Format: PNG or JPG
- Size: 800x1100px recommended
- File: `template_images/resumes/<id>-preview.png`

**Generate from PDF:**
```bash
# Using ImageMagick
convert -density 150 output.pdf -quality 90 preview.png
```

---

## Phase 3: Template Testing (Week 3)

### 3.1 Compile Test

```bash
cd templates/<id>/
unzip assets/typst_assets.zip
./typst compile --font-path fonts source/main.typ
```

### 3.2 Verify Output

**Checklist:**
- [ ] PDF generates without errors
- [ ] All fonts render correctly
- [ ] Layout matches preview
- [ ] Text extracts properly (ATS test)
- [ ] All sections work

### 3.3 Cross-Platform Test

**Environments:**
- [ ] Linux (GPT Code Interpreter)
- [ ] Windows (local)
- [ ] macOS (if available)

---

## Phase 4: Template Documentation (Week 4)

### 4.1 Create Template Guide

**File: `docs/templates/<id>.md`**

**Contents:**
- Overview
- Features
- Customization options
- Example code
- Known issues

### 4.2 Update Quick Reference

**Edit `quick_reference.json`:**
```json
{
  "availableTemplates": {
    "resumes": [
      {
        "id": "new-template",
        "name": "New Template",
        "bestFor": ["tech", "creative"],
        "assetsPath": "templates/new-template/assets/typst_assets.zip"
      }
    ]
  }
}
```

### 4.3 Update System Prompt

**Edit `SYSTEM_PROMPT_TYPST.md`:**
- Add template to available templates list
- Add specific commands/sections
- Add customization options

---

## Phase 5: Custom Template Creation

### 5.1 Design Template

**Tools:**
- [Typst Web App](https://typst.app/)
- Local Typst installation
- Text editor (VS Code with Typst extension)

**Structure:**
```
my-template/
├── typst.toml          # Package config
├── lib.typ             # Main library
├── template.typ        # Entry point
├── fonts/              # Custom fonts
└── images/             # Assets
```

### 5.2 Implement Components

**Required Components:**
```typst
// Header with contact info
#let resume-header(author) = { ... }

// Section heading
#let section-heading(title) = { ... }

// Entry component
#let resume-entry(title, location, date, description) = { ... }

// Bullet items
#let resume-item(content) = { ... }

// Skills
#let resume-skill-item(category, skills) = { ... }
```

### 5.3 Test Locally

```bash
typst compile template.typ
```

### 5.4 Package for Distribution

**Create `typst.toml`:**
```toml
[package]
name = "my-template"
version = "1.0.0"
entrypoint = "template.typ"
authors = ["Your Name"]
license = "MIT"
```

**Build:**
```bash
# Create source directory
mkdir -p templates/my-template/source

# Copy files
cp -r my-template/* templates/my-template/source/

# Build assets
python build_template_assets.py --template my-template
```

---

## Template Standards

### Code Style

```typst
// Use clear function names
#let resume-entry(...) = { ... }  // Good
#let re(...) = { ... }            // Bad

// Document parameters
/// Entry for work experience
///
/// Parameters:
/// - title: Job title
/// - location: Company/location
/// - date: Date range
/// - description: Company description
#let resume-entry(title, location, date, description) = { ... }

// Use consistent formatting
#set text(font: "Source Sans Pro", size: 11pt)
```

### File Organization

```
templates/<id>/
├── assets/
│   └── typst_assets.zip    # Binary + fonts + packages
├── source/
│   ├── main.typ           # Main template file
│   ├── lib.typ            # Library (if any)
│   ├── typst.toml         # Package config
│   └── ...                # Other source files
├── fonts/
│   └── *.ttf, *.otf       # Font files
└── packages/
    └── ...                # Local packages
```

### Documentation

Every template must have:
- [ ] README.md in source directory
- [ ] Entry in templates_registry.json
- [ ] Preview image
- [ ] ATS compatibility notes
- [ ] Customization options documented

---

## Quick Reference Commands

### Import Template
```bash
python import_templates.py
python analyze_templates.py
python organize_templates.py
```

### Build Assets
```bash
python build_template_assets.py --template <id>
```

### Update Registry
```bash
python update_registry.py
```

### Verify
```bash
python verify_project.py
```

---

## Resources

- [Typst Documentation](https://typst.app/docs/)
- [Typst Packages](https://typst.app/universe)
- [Font Squirrel](https://www.fontsquirrel.com/) - Free commercial fonts
- [Google Fonts](https://fonts.google.com/) - Open source fonts
- [Typst Discord](https://discord.gg/2uDybryKPe) - Community support

---

## Timeline Summary

| Phase | Duration | Deliverables |
|-------|----------|--------------|
| 1. Discovery | Week 1 | 3-5 candidate templates |
| 2. Integration | Week 2 | Assets built, registry updated |
| 3. Testing | Week 3 | All templates compile successfully |
| 4. Documentation | Week 4 | Complete docs for all templates |
| 5. Creation | Ongoing | Custom templates as needed |

---

## Future Enhancements

- [ ] Template preview generator (PDF to PNG)
- [ ] Automated ATS testing
- [ ] Multi-language support expansion
- [ ] Cover letter template library
- [ ] Theme/color customization UI
- [ ] Export to LaTeX format
- [ ] Integration with job boards
