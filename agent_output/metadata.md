# AeroCV Template Catalog

| ID | Style | Best For |
|---|---|---|
| `modern-cv` | Clean, professional | Tech, Corporate, ATS-friendly. Has photo & cover letter support. |
| `vantage` | Two-column, skill bars | Engineering, Support, ATS-optimized. |
| `designer-cv` | Creative, vibrant colors | Designers, Creatives, Marketing. |
| `executive-cv` | Formal, corporate | Executives, Senior Management, Finance. |
| `portfolio-cv` | Projects-focused | Developers, Artists, Portfolio showcase. |
| `typst-cv` | Academic, minimal | Academia, Research, Simple roles. |
| `vercanard` | Minimalist, sidebar | Minimalist style, any role. |

## Import Syntax Per Template

Each template zip is flat. After extraction, use these imports in your `.typ` file:

- **modern-cv**: `#import "lib.typ": *`
- **vantage**: `#import "vantage-typst.typ": *`
- **designer-cv**: `#import "designer-cv.typ": *`
- **executive-cv**: `#import "executive-cv.typ": *`
- **portfolio-cv**: `#import "portfolio-cv.typ": *`
- **typst-cv**: `#import "template.typ": conf, date, show_skills`
- **vercanard**: `#import "template/main.typ": *`
