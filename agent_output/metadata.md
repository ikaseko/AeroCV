# AeroCV Template Catalog

| ID | Style | Best For |
|---|---|---|
| `modern-cv` | Classic & Header-centric | Traditional corporate, Academic, Legal. Basic lists with a large top header. |
| `vantage` | High-Impact Tech & Skills | Backend/Frontend Engineers, SRE, DevOps, Data Science. High IT/Tech focus with side-by-side layout and skill bars. |
| `designer-cv` | Creative & Vibrant color | UI/UX Designers, Frontend Devs, Marketers. Visually striking with an accent sidebar. |
| `executive-cv` | Formal Leadership | C-Level, Management, Consulting, Finance. Very clean, conservative, structured. |
| `portfolio-cv` | Developer Portfolio | Fullstack Engineers, Open-Source Contributors. Prominently highlights GitHub projects and tech stacks. |
| `typst-cv` | Academic & Minimalist | Researchers, PhDs, Scientists. Extremely sparse styling focused purely on content and publications. |
| `vercanard` | Modern Asymmetric Sidebar | Product Managers, Startup Roles. Stylish left-aligned contact/skills sidebar with rich main content area. |
| `brilliant-cv` | Modern & Multilingual | Universal, clean design with excellent typography. Highly adaptable for Software Engineers, Managers, and general professional use. |

## Import Syntax Per Template

Each template zip is flat. After extraction, use these imports in your `.typ` file:

- **modern-cv**: `#import "lib.typ": *`
- **vantage**: `#import "vantage-typst.typ": *`
- **designer-cv**: `#import "designer-cv.typ": *`
- **executive-cv**: `#import "executive-cv.typ": *`
- **portfolio-cv**: `#import "portfolio-cv.typ": *`
- **typst-cv**: `#import "template.typ": conf, date, show_skills`
- **vercanard**: `#import "template/main.typ": *`
