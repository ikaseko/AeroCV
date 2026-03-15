# ATS (Applicant Tracking System) Guidelines for Typst CVs

## Overview

Applicant Tracking Systems (ATS) parse resumes automatically before human review. Typst generates clean PDFs by default, but following these guidelines ensures maximum compatibility.

---

## ✅ Best Practices

### 1. Text Flow (Left-to-Right, Top-to-Bottom)

ATS parsers read content in reading order. Ensure your template follows this pattern:

```typst
// GOOD - Natural reading order
= Experience

#resume-entry(
  title: "Job Title",
  date: "2020-2024",
)

// AVOID - Absolute positioning that breaks flow
#place(dx: 400pt, dy: 100pt)[Job Title]
```

### 2. Use Grids for Columns

Grids maintain logical reading order while creating visual columns:

```typst
// GOOD - ATS-friendly column layout
#grid(
  columns: 2,
  inset: 4pt,
  [Job Title],
  [2020-2024],
)

// AVOID - Absolute positioning
#box(width: 50%)[Job Title]
#box(width: 50%)[2020-2024]
```

### 3. Semantic Headings

Use standard heading levels for section structure:

```typst
// GOOD - Semantic headings
= Experience      // Level 1 (main sections)
== Job Title      // Level 2 (subsections)

// AVOID - Styled text as headings
#text(size: 16pt, weight: "bold")[Experience]
```

### 4. Standard Section Names

Use common section names that ATS recognizes:

| Recommended | Alternatives |
|-------------|--------------|
| `Experience` | Work History, Employment |
| `Education` | Academic Background |
| `Skills` | Technical Skills, Competencies |
| `Projects` | Portfolio, Key Projects |
| `Certifications` | Licenses, Credentials |

### 5. Font Embedding

Embed standard, readable fonts:

```typst
// GOOD - Common ATS-friendly fonts
#set text(font: "Source Sans Pro")
#set text(font: "Roboto")
#set text(font: "Inter")
#set text(font: "Arial")
#set text(font: "Helvetica")

// AVOID - Decorative fonts
#set text(font: "Comic Sans MS")
#set text(font: "Papyrus")
```

### 6. Ligature Handling

Some ATS struggle with ligatures. Disable if needed:

```typst
// GOOD - Disable ligatures for maximum compatibility
#set text(ligatures: false)
```

### 7. Bullet Points

Use standard bullet characters:

```typst
// GOOD - Standard bullets
#resume-item[
  - Achieved 40% improvement
  - Led team of 5 engineers
]

// AVOID - Special characters
#resume-item[
  ● Achieved 40% improvement
  → Led team of 5 engineers
]
```

### 8. Date Formats

Use clear, unambiguous date formats:

```typst
// GOOD - Clear formats
"2020-2024"
"Jan 2020 - Dec 2024"
"01/2020 - 12/2024"

// AVOID - Ambiguous formats
"20-24"
"Last 4 years"
```

### 9. Contact Information

Place contact info at the top in a clear format:

```typst
// GOOD - Standard format
#show: resume.with(
  author: (
    firstname: "John",
    lastname: "Doe",
    email: "john@example.com",
    phone: "+1-555-123-4567",
    linkedin: "johndoe",
  ),
)

// AVOID - Icons only (no text)
#fa-icon("envelope")  // ATS can't read this
```

### 10. Avoid These Elements

| Element | Problem | Alternative |
|---------|---------|-------------|
| `place()` | Breaks reading order | Use `grid()` |
| Images in content | Can't parse text | Use text only |
| Tables for layout | Confuses parsers | Use `grid()` |
| Headers/Footers | Often skipped | Put info in body |
| Columns > 2 | Hard to parse | Use single column |

---

## Template-Specific Guidelines

### Modern CV
- ✅ Uses `grid()` for layout
- ✅ Semantic headings
- ✅ Standard fonts
- ⚠️ Disable `place()` if used

### Brilliant CV
- ✅ Designed for ATS
- ✅ Grid-based layout
- ✅ Semantic structure

### Typst CV
- ✅ Simple structure
- ✅ No complex layouts

### VerCanard
- ✅ Minimal design
- ✅ Single column

### Vantage
- ✅ Clean layout
- ✅ Standard sections

### Neat CV
- ✅ Semantic sections
- ✅ Grid-based

---

## Testing Your Resume

### 1. Text Extraction Test

```bash
# Extract text from PDF
pdftotext resume.txt resume.pdf

# Verify reading order
cat resume.txt
```

### 2. Online ATS Simulators

- [Jobscan](https://www.jobscan.co/)
- [Resume Worded](https://resumeworded.com/)
- [SkillSyncer](https://skillsyncer.com/)

### 3. Manual Review

1. Open PDF in text editor
2. Verify text appears in correct order
3. Check for missing content
4. Ensure no garbled characters

---

## Quick Reference

```typst
// ATS-Friendly Template Structure

#show: resume.with(
  author: (
    firstname: "John",
    lastname: "Doe",
    email: "john@example.com",
    phone: "+1-555-123-4567",
  ),
  language: "en",
  paper-size: "a4",
)

= Experience

#resume-entry(
  title: "Software Engineer",
  location: "Company Name",
  date: "2020-2024",
)

#resume-item[
  - Led development of feature X
  - Improved performance by 40%
  - Managed team of 5 engineers
]

= Education

#resume-entry(
  title: "University Name",
  location: "B.S. Computer Science",
  date: "2016-2020",
)

= Skills

#resume-skill-item(
  "Programming",
  (strong("Python"), strong("JavaScript"), "Go"),
)
```

---

## Resources

- [Typst Documentation](https://typst.app/docs/)
- [ATS Resume Guidelines](https://www.jobscan.co/blog/ats-resume-examples/)
- [PDF Accessibility](https://www.adobe.com/accessibility/pdf/pdf-accessibility-checker.html)
