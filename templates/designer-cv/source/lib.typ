// Designer CV Template — Soft, Elegant, Refined "Figma 2026" Aesthetic
// Spacious, beautiful typographic hierarchy, subtle contrasts

#let designer-cv(
  author: (:),
  profile-picture: none,
  primary-color: rgb("#111111"),
  accent-color: rgb("#F72585"), // Used sparingly for high impact
  sidebar-color: rgb("#F8F9FA"), // Soft gray sidebar
  body-font: "Inter",
  paper-size: "a4",
  body
) = {
  set document(author: author.firstname + " " + author.lastname, title: "Resume - " + author.firstname + " " + author.lastname)
  set page(
    paper: paper-size,
    margin: (left: 9.5cm, right: 2cm, top: 2.5cm, bottom: 2cm),
    background: place(top + left, rect(width: 7.5cm, height: 100%, fill: sidebar-color))
  )
  set text(font: body-font, size: 9.5pt, fill: rgb("#333333"), weight: "regular", ligatures: false)

  place(top + left, dx: -8cm, dy: 0cm, block(
    width: 6cm,
    [
      #set text(fill: primary-color)
      
      #if profile-picture != none {
        align(left)[
          #box(width: 4cm, height: 4cm, clip: true, radius: 2cm, stroke: none, profile-picture)
        ]
        v(1cm)
      }

      #text(size: 24pt, weight: "black", tracking: 0.02em)[#upper(author.firstname)]\
      #text(size: 24pt, weight: "light", tracking: 0.02em, fill: accent-color)[#upper(author.lastname)]
      
      #v(0.5em)
      #if "role" in author [
        #text(size: 10pt, weight: "medium", fill: rgb("#666666"), tracking: 0.1em)[#upper(author.role)]
      ]

      #v(2cm)

      #let sidebar-heading(title) = {
        text(size: 10pt, weight: "bold", fill: primary-color, tracking: 0.15em)[#upper(title)]
        v(0.6em)
        line(length: 2cm, stroke: 1.5pt + primary-color)
        v(0.8em)
      }

      #sidebar-heading("Contact")
      #set text(size: 9.5pt, fill: rgb("#555555"))
      #set par(leading: 0.9em)
      #if "email" in author [ #author.email \ \ ]
      #if "phone" in author [ #author.phone \ \ ]
      #if "portfolio" in author [ #link(author.portfolio)[#text(fill: accent-color, weight: "semibold")[Portfolio ↗]] \ \ ]
      #if "linkedin" in author [ #link(author.linkedin)[#text(fill: primary-color, weight: "medium")[LinkedIn ↗]] \ \ ]
      #if "address" in author [ #author.address \ \ ]

      #v(1.5cm)

      #sidebar-heading("Expertise")
      #text(fill: primary-color, weight: "semibold")[UI/UX Design] \
      Interaction Design \
      Design Systems \
      User Research \
      Prototyping \
      Wireframing
      
      #v(1.5cm)
      
      #sidebar-heading("Tools")
      #text(fill: primary-color, weight: "semibold")[Figma, Sketch] \
      Framer, Principle \
      Adobe Creative Suite \
      Webflow
    ]
  ))

  set par(leading: 0.85em)
  
  show heading.where(level: 1): h => {
    v(1em)
    grid(
      columns: (auto, 1fr),
      align: (left, horizon),
      column-gutter: 1em,
      text(size: 12pt, weight: "black", fill: primary-color, tracking: 0.15em)[#upper(h.body)],
      line(length: 100%, stroke: 0.5pt + rgb("#EAEAEA"))
    )
    v(1em)
  }
  
  show heading.where(level: 2): h => {
    v(0.8em)
    text(size: 11pt, weight: "bold", fill: primary-color)[#h.body]
    v(0.3em)
  }

  body
}

// ─── RIGHT COLUMN MAIN ───
#let resume-entry(title: "", location: "", date: "", description: "") = {
  grid(
    columns: (1fr, auto),
    [
      #text(size: 11.5pt, weight: "bold", fill: rgb("#111111"))[#title] \
      #text(size: 10pt, fill: rgb("#777777"))[#location]
    ],
    align(right)[
      #text(size: 9.5pt, weight: "semibold", fill: rgb("#F72585"))[#date]
    ]
  )
  if description != "" {
    v(0.4em)
    [
      #set text(size: 9.5pt, fill: rgb("#444444"))
      #set par(leading: 0.9em)
      #description
    ]
  }
  v(0.8em)
}

#let resume-item(body) = {
  set list(marker: text(fill: rgb("#BBBBBB"), size: 8pt)[—], spacing: 0.6em)
  set text(size: 10pt, fill: rgb("#444444"))
  set par(leading: 0.9em)
  body
}

// Empty fallback to not break old tests
#let resume-skill-item(category, skills) = {}
