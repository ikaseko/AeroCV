# AeroCV - Multi-Template Typst System

A professional CV/Resume and Cover Letter generator using **Typst** with support for **6 templates**. Designed for use with GPT Code Interpreter (Advanced Data Analysis) in fully offline mode.

## 🚀 Quick Start

### For GPT Agent

1. **Read `quick_reference.json`** - Discover available templates
2. **Read `templates_registry.json`** - Get detailed template info  
3. **Follow `SYSTEM_PROMPT_TYPST.md`** - Compilation instructions

### 🤖 Quickest way — GPT Agent
No setup. Just describe your target role and paste the job description.

👉 **[Try AeroCV on ChatGPT](https://chatgpt.com/g/g-69b6fdb57ef081918831daa7673cb131-aerocv-ats-resume-cover-letter-pdf-maker)**
### Python Code for Code Interpreter

```python
import os, zipfile, subprocess, json

# Load template info
with open("/mnt/data/quick_reference.json") as f:
    ref = json.load(f)

# Get assets path (user selects template)
assets_path = ref["availableTemplates"]["resumes"][0]["assetsPath"]

# Setup work directory
work_dir = "/mnt/data/cv_build"
os.makedirs(work_dir, exist_ok=True)
os.chdir(work_dir)

# Extract assets (includes typst binary)
with zipfile.ZipFile(f"/mnt/data/{assets_path}", "r") as zip_ref:
    zip_ref.extractall(work_dir)

os.chmod("typst", 0o755)

# Create and compile
with open("resume.typ", "w") as f:
    f.write(resume_content)

subprocess.run(["./typst", "compile", "--font-path", "fonts", "resume.typ"])
```

## 📋 Available Templates

### Resume Templates

| ID | Name | Style | Best For | Cover Letter | Photo | Preview |
|----|------|-------|----------|--------------|-------|---------|
| `modern-cv` | Modern CV | Professional | Tech, Corporate | ✅ | ✅ Circular | [Preview](template_images/resumes/modern-cv-preview.png) |
| `typst-cv` | Typst CV | Simple | General | ❌ | ✅ Rectangular | [Preview](template_images/resumes/typst-cv-preview.png) |
| `brilliant-cv` | Brilliant CV | Modern | Multi-language | ✅ | ✅ Configurable | [Preview](template_images/resumes/brilliant-cv-preview.png) |
| `vercanard` | VerCanard | Minimal | Single-page | ❌ | ❌ | [Preview](template_images/resumes/vercanard-preview.png) |
| `vantage` | Vantage | Clean | Tech | ❌ | ❌ | [Preview](template_images/resumes/vantage-preview.png) |
| `neat-cv` | Neat CV | Bilingual | EN/FR | ✅ | ✅ Left side | [Preview](template_images/resumes/neat-cv-preview.pdf) |
| `designer-cv` | Designer CV | Creative | High-end Design | ✅ | ✅ Circular | [Preview](template_images/resumes/designer-cv-preview.png) |
| `executive-cv` | Executive CV | Formal | Execs, Academics | ✅ | ✅ Strict right | [Preview](template_images/resumes/executive-cv-preview.png) |
| `portfolio-cv` | Portfolio CV | Technical | Devs, Artists | ✅ | ✅ Rounded | [Preview](template_images/resumes/portfolio-cv-preview.png) |

### Template Details

#### Modern CV (`modern-cv`)
- **Source**: [ptsouchlos/modern-cv](https://github.com/ptsouchlos/modern-cv)
- **Features**: Clean design, FontAwesome icons, 35+ languages
- **Fonts**: Source Sans 3, Roboto
- **Packages**: fontawesome, linguify

#### Typst CV (`typst-cv`)
- **Source**: [JCGoran/typst-cv-template](https://github.com/JCGoran/typst-cv-template)
- **Features**: Simple, customizable via TOML
- **Fonts**: System fonts
- **Packages**: None

#### Brilliant CV (`brilliant-cv`)
- **Source**: [yunanwg/brilliant-CV](https://github.com/yunanwg/brilliant-CV)
- **Features**: ATS-friendly, modular, multi-language
- **Fonts**: Roboto, Inter, Source Sans
- **Packages**: fontawesome, tidy

#### VerCanard (`vercanard`)
- **Source**: [elegaanz/vercanard](https://github.com/elegaanz/vercanard)
- **Features**: Minimalist, single-page
- **Fonts**: System fonts
- **Packages**: vercanard (self-contained)

#### Vantage (`vantage`)
- **Source**: [sardorml/vantage-typst](https://github.com/sardorml/vantage-typst)
- **Features**: Clean layout, SVG icons
- **Fonts**: System fonts
- **Packages**: None

#### Neat CV (`neat-cv`)
- **Source**: [UntimelyCreation/typst-neat-cv](https://github.com/UntimelyCreation/typst-neat-cv)
- **Features**: Bilingual (EN/FR), content separation
- **Fonts**: Source Sans Pro (included)
- **Packages**: None

#### Designer CV (`designer-cv`)
- **Source**: Custom Built
- **Features**: Visually striking, creative 2-column layout, stylized typography
- **Fonts**: Inter, Outfit
- **Packages**: None

#### Executive CV (`executive-cv`)
- **Source**: Custom Built
- **Features**: Restrained, highly structured, minimal colors, strict ATS layout
- **Fonts**: Times New Roman
- **Packages**: None

#### Portfolio CV (`portfolio-cv`)
- **Source**: Custom Built
- **Features**: Dedicated project sections, prominent portfolio links, modern header
- **Fonts**: Roboto, Montserrat
- **Packages**: None

## 📁 Project Structure

```
AeroCV/
├── templates/                    # Template storage
│   ├── modern-cv/               # Modern CV template
│   ├── typst-cv/                # Typst CV template
│   ├── brilliant-cv/            # Brilliant CV
│   ├── vercanard/               # VerCanard
│   ├── vantage/                 # Vantage
│   ├── neat-cv/                 # Neat CV
│   ├── designer-cv/             # High-end Designer CV
│   ├── executive-cv/            # Structured Executive CV
│   └── portfolio-cv/            # Project-focused CV
│       ├── assets/              # Compiled assets (ZIP)
│       ├── source/              # Template source files
│       ├── fonts/               # Font files
│       └── packages/            # Typst packages
│
├── cover_letters/               # Cover letter templates
│   └── modern-cv/
│
├── template_images/             # Preview images
│   ├── resumes/                # Resume previews
│   └── cover_letters/          # Cover letter previews
│
├── output/                      # Generated PDFs
├── scripts/                     # Build scripts
├── schemas/                     # JSON schemas
├── docs/                        # Documentation
│   ├── ATS_GUIDELINES.md       # ATS compatibility guide
│   ├── ROADMAP.md              # Template creation roadmap
│   └── TEMPLATE_IMPORT_STATUS.md
│
├── templates_registry.json      # 📋 Template registry
├── quick_reference.json         # ⚡ Quick reference guide
├── SYSTEM_PROMPT_TYPST.md       # 🤖 GPT agent instructions
└── README.md                    # This file
```

## 📄 Key Files

| File | Purpose | Size |
|------|---------|------|
| `quick_reference.json` | Quick template discovery | 2.3 KB |
| `templates_registry.json` | Full template registry with paths | 6+ KB |
| `SYSTEM_PROMPT_TYPST.md` | GPT agent instructions | 7.2 KB |
| `schemas/*.schema.json` | JSON schema validation | 11 KB |
| `docs/ATS_GUIDELINES.md` | ATS compatibility guide | - |
| `docs/ROADMAP.md` | Template creation roadmap | - |
| `docs/PHOTO_QUICK_REF.md` | 📸 Profile Photo Quick Ref | - |

## 📸 Profile Photo Support

Several templates support including a professional profile photo. When using a compatible template, the AI agent will ask if you'd like to include one.

### Supported Templates
- **Modern CV**: Circular photo in the header.
- **Typst CV**: Rectangular photo.
- **Brilliant CV**: Configurable placement.
- **Neat CV**: Left-side sidebar photo.

### How to Use
1. **Upload**: Provide a PNG or JPG file (min 200x200px recommended).
2. **Confirm**: The agent will detect the photo and ask for confirmation.
3. **Generate**: The photo will be integrated into the final PDF.

For technical implementation details, see [docs/PHOTO_QUICK_REF.md](docs/PHOTO_QUICK_REF.md).


1. Clone template: `python import_templates.py`
2. Analyze: `python analyze_templates.py`
3. Organize: `python organize_templates.py`
4. Build assets: `python build_template_assets.py`
5. Update registry: `python update_registry.py`
6. Verify: `python verify_project.py`

## 🌐 Supported Languages

35+ languages including: English, Russian, German, French, Spanish, Italian, Portuguese, Dutch, Polish, Chinese, Japanese, Korean, Arabic, Hindi, Turkish, and more.

## ✅ ATS Compatibility

All templates follow ATS best practices:
- ✅ Semantic headings
- ✅ Grid-based layouts (no absolute positioning)
- ✅ Standard section names
- ✅ Embedded fonts
- ✅ Clean text extraction

See [docs/ATS_GUIDELINES.md](docs/ATS_GUIDELINES.md) for details.

## 🔧 Scripts

| Script | Purpose |
|--------|---------|
| `import_templates.py` | Clone template repositories |
| `analyze_templates.py` | Analyze template structure |
| `organize_templates.py` | Organize into project structure |
| `build_template_assets.py` | Build assets.zip for templates |
| `update_registry.py` | Update templates_registry.json |
| `verify_project.py` | Verify project structure |

## 📝 License

- **Modern CV**: MIT License (Paul Tsouchlos)
- **Brilliant CV**: MIT License
- **Typst CV**: MIT License
- **VerCanard**: MIT License
- **Vantage**: MIT License
- **Neat CV**: MIT License
- **Project Structure & Custom Templates (`designer-cv`, `executive-cv`, `portfolio-cv`)**: Functional Source License (Non-Compete) - See LICENSE file.

## 🙌 Credits & Original Templates

This project builds upon the fantastic work of the open-source Typst community. Credit to the original template creators:
1. **Typst CV**: [JCGoran/typst-cv-template](https://github.com/JCGoran/typst-cv-template)
2. **Brilliant CV**: [yunanwg/brilliant-CV](https://github.com/yunanwg/brilliant-CV)
3. **VerCanard**: [elegaanz/vercanard](https://github.com/elegaanz/vercanard)
4. **Vantage**: [sardorml/vantage-typst](https://github.com/sardorml/vantage-typst)
5. **Neat CV**: [UntimelyCreation/typst-neat-cv](https://github.com/UntimelyCreation/typst-neat-cv)

## 🔗 Links

- [Typst Documentation](https://typst.app/docs/)
- [Typst Templates](https://typst.app/templates)
- [Typst Universe](https://typst.app/universe)
