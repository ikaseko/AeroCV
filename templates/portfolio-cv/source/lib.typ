// Portfolio CV — Immersive Dark Mode
// Inspired by: Linear.app, Vercel dashboard, Raycast
// Tight, dense, information-rich — no wasted pixels

#let portfolio-cv(
  author: (:),
  profile-picture: none,
  accent-color: rgb("#4493F8"), // GitHub blue
  bg-color: rgb("#0D1117"),
  surface-color: rgb("#161B22"),
  border-color: rgb("#30363D"),
  text-color: rgb("#E6EDF3"),
  muted-color: rgb("#7D8590"),
  body-font: "Inter",
  paper-size: "a4",
  body
) = {
  set document(author: author.firstname + " " + author.lastname, title: "Portfolio — " + author.firstname + " " + author.lastname)
  set page(paper: paper-size, fill: bg-color, margin: 0cm)
  set text(font: body-font, size: 9pt, fill: text-color, weight: "regular", ligatures: false)

  // === HEADER BLOCK ===
  block(
    width: 100%,
    fill: surface-color,
    stroke: (bottom: 1pt + border-color),
    inset: (x: 2cm, y: 1.5cm),
    [
      #grid(
        columns: (auto, 1fr, auto),
        align: (left, left, right + horizon),
        column-gutter: 1.2em,
        // Accent circle
        box(
          width: 0.4cm,
          height: 2.5cm,
          fill: accent-color,
          radius: 2pt,
        ),
        [
          #text(size: 28pt, weight: "black", fill: text-color, tracking: -0.02em)[#upper(author.firstname) #upper(author.lastname)]
          #v(0.3em)
          #if "role" in author [
            #text(size: 11pt, weight: "light", fill: muted-color)[#author.role]
            #v(0.4em)
          ]
          #text(size: 8.5pt, fill: muted-color, tracking: 0.02em)[
            #author.email
            #h(1.2em) #sym.dot #h(1.2em)
            #author.phone
            #if "portfolio" in author [ #h(1.2em) #sym.dot #h(1.2em) #text(fill: accent-color)[#link(author.portfolio)] ]
            #if "github" in author [ #h(1.2em) #sym.dot #h(1.2em) #link(author.github)[GitHub] ]
          ]
        ],
        [
          #if profile-picture != none {
            box(width: 3cm, height: 3cm, clip: true, radius: 6pt, stroke: 1pt + border-color, profile-picture)
          }
        ]
      )
    ]
  )

  // === BODY ===
  block(
    width: 100%,
    inset: (x: 2cm, top: 1.5cm, bottom: 1.5cm),
    [
      #set par(leading: 0.8em)

      #show heading.where(level: 1): h => {
        v(1.2em)
        text(size: 8pt, weight: "bold", fill: muted-color, tracking: 0.18em)[#upper(h.body)]
        v(0.6em)
        line(length: 100%, stroke: 0.5pt + border-color)
        v(0.8em)
      }

      #body
    ]
  )
}

// ─── PROJECT ENTRY — Dense, editorial ───
#let resume-project(title: "", url: "", date: "", tech: (), description: "") = {
  block(
    width: 100%,
    stroke: (left: 2pt + rgb("#4493F8")),
    inset: (left: 1em, top: 0.2em, bottom: 0.5em, right: 0em),
    [
      #grid(
        columns: (1fr, auto),
        [
          #text(size: 11pt, weight: "semibold", fill: rgb("#E6EDF3"))[#title]
          #if url != "" [ #h(0.6em) #text(size: 8pt, fill: rgb("#4493F8"))[#link(url)] ]
        ],
        [
          #text(size: 8.5pt, fill: rgb("#7D8590"), font: "Consolas")[#date]
        ]
      )
      #if tech.len() > 0 {
        v(0.4em)
        for t in tech {
          box(
            inset: (x: 0.55em, y: 0.2em),
            radius: 3pt,
            fill: rgb("#1C2128"),
            stroke: 0.5pt + rgb("#30363D"),
            text(size: 7.5pt, fill: rgb("#CDD9E5"), font: "Consolas")[#t]
          )
          h(0.35em)
        }
      }
      #if description != "" {
        v(0.5em)
        [
          #set text(size: 9pt, fill: rgb("#7D8590"))
          #description
        ]
      }
    ]
  )
  v(0.7em)
}

#let resume-entry(title: "", location: "", date: "", description: "") = {
  grid(
    columns: (1fr, auto),
    [
      #text(size: 10.5pt, weight: "semibold", fill: rgb("#CDD9E5"))[#title] \
      #v(0.1em)
      #text(size: 9pt, fill: rgb("#7D8590"))[#location]
    ],
    align(right)[
      #text(size: 8.5pt, fill: rgb("#7D8590"), font: "Consolas")[#date]
    ]
  )
  if description != "" {
    v(0.4em)
    [
      #set text(size: 9pt, fill: rgb("#7D8590"))
      #description
    ]
  }
  v(0.9em)
}

#let resume-item(body) = {
  set list(marker: text(fill: rgb("#4493F8"), size: 8pt)[›], spacing: 0.55em)
  set text(size: 9pt, fill: rgb("#9198A1"))
  set par(leading: 0.75em)
  body
}

#let resume-skill-item(category, skills) = {
  grid(
    columns: (auto, 1fr),
    column-gutter: 1.5em,
    [
      #text(size: 8.5pt, weight: "semibold", fill: rgb("#7D8590"), tracking: 0.08em, font: "Consolas")[#upper(category)]
    ],
    [
      #text(size: 9pt, fill: rgb("#CDD9E5"))[#skills.join("  ·  ")]
    ]
  )
  v(0.5em)
}
