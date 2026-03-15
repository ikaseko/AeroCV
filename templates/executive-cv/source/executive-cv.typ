#import "lib.typ": *

#show: executive-cv.with(
  author: (
    firstname: "Jonathan",
    lastname: "Crawford",
    email: "jcrawford@example.com",
    phone: "+1 (555) 123-4567",
    linkedin: "https://linkedin.com/in/jcrawford",
    address: "Chicago, IL"
  ),
  accent-color: rgb("#1B3A4B"),
)

= Professional Summary
Results-driven Executive Director with over 15 years of progressive experience in corporate finance, operational restructuring, and strategic planning. Recognized for leading multi-million dollar business transformations and delivering consistent revenue growth in highly competitive markets.

= Professional Experience

#resume-entry(
  title: "Executive Director of Finance",
  location: "Global Investments Partners, Chicago, IL",
  date: "2018 — Present"
)

#resume-item[
  - Spearheaded a global restructuring initiative that reduced operational redundancies by 22%
  - Managed an annual portfolio of \$450M, achieving year-over-year revenue growth of 14%
  - Led a cross-functional team of 45 analysts, directors, and compliance officers
]

#resume-entry(
  title: "Senior Financial Analyst",
  location: "Apex Strategy Consulting, New York, NY",
  date: "2010 — 2018"
)

#resume-item[
  - Directed M&A due diligence for 12 major acquisitions valued over \$50M each
  - Developed and implemented proprietary forecasting models adopted company-wide
  - Presented quarterly risk assessments directly to C-suite executives
]

= Education

#resume-entry(
  title: "Master of Business Administration (MBA)",
  location: "Harvard Business School, Boston, MA",
  date: "2008 — 2010"
)

#resume-entry(
  title: "Bachelor of Science in Economics",
  location: "University of Pennsylvania, Philadelphia, PA",
  date: "2004 — 2008",
  description: "Graduated Summa Cum Laude"
)

= Core Competencies

#resume-skill-item("Financial Management", ("P&L Management", "M&A Due Diligence", "Financial Forecasting"))
#resume-skill-item("Leadership & Strategy", ("Cross-functional Team Leadership", "Change Management", "Risk Mitigation"))
#resume-skill-item("Technical Skills", ("Bloomberg Terminal", "Advanced Excel/VBA", "SAP ERP", "Tableau"))
