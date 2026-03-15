// Executive / Conservative CV Template — Elegant, high-contrast header band
// Classic serif font, strong visual hierarchy without being flashy

#let executive-cv(
  author: (:),
  profile-picture: none,
  accent-color: rgb("#1B3A4B"),
  header-bg: rgb("#1B3A4B"),
  body-font: "Source Sans 3",
  paper-size: "a4",
  body
) = {
  set document(author: author.firstname + " " + author.lastname, title: "Resume - " + author.firstname + " " + author.lastname)
  set page(
    paper: paper-size,
    margin: (left: 0cm, right: 0cm, top: 0cm, bottom: 0cm),
  )
  set text(font: body-font, size: 10.5pt, fill: rgb("#222222"), weight: "regular", ligatures: false)

  // === HEADER BANNER ===
  block(
    width: 100%,
    fill: header-bg,
    inset: (x: 2cm, y: 1.5cm),
    [
      #grid(
        columns: (1fr, auto),
        align: (left, right + horizon),
        [
          #text(size: 30pt, weight: "bold", fill: white, tracking: 0.1em)[#upper(author.firstname + " " + author.lastname)]
          #v(0.5em)
          #text(size: 10pt, fill: rgb("#B0C4D8"), weight: "medium")[
            #if "address" in author [ #author.address #h(1em) ]
            #author.phone #h(1em) #author.email
            #if "linkedin" in author [ #h(1em) #link(author.linkedin)[LinkedIn] ]
          ]
        ],
        [
          #if profile-picture != none {
            box(
              width: 3.5cm,
              height: 4.2cm,
              clip: true,
              stroke: 2pt + rgb("#B0C4D8"),
              profile-picture
            )
          }
        ]
      )
    ]
  )

  // Gold accent line under header
  block(width: 100%, height: 4pt, fill: rgb("#C9A96E"))

  // === BODY ===
  block(
    width: 100%,
    inset: (x: 2cm, top: 1cm, bottom: 1cm),
    {
      show heading.where(level: 1): h => {
        v(0.7em)
        text(size: 12pt, weight: "bold", fill: accent-color, tracking: 0.1em)[
          #upper(h.body)
        ]
        v(0.2em)
        line(length: 100%, stroke: 1pt + rgb("#C9A96E"))
        v(0.4em)
      }

      show heading.where(level: 2): h => {
        v(0.5em)
        text(size: 11pt, weight: "bold", fill: rgb("#000000"))[#h.body]
        v(0.2em)
      }

      body
    }
  )
}

// ─── HELPER FUNCTIONS ───

#let resume-entry(title: "", location: "", date: "", description: "") = {
  grid(
    columns: (1fr, auto),
    [
      #text(size: 11pt, weight: "bold", fill: rgb("#111111"))[#title] \
      #text(size: 10pt, style: "italic", fill: rgb("#555555"))[#location]
    ],
    align(right)[
      #text(size: 10pt, weight: "medium", fill: rgb("#1B3A4B"))[#date]
    ]
  )
  if description != "" {
    v(0.2em)
    text(size: 10pt, fill: rgb("#444444"))[#description]
  }
  v(0.5em)
}

#let resume-item(body) = {
  set list(marker: text(fill: rgb("#C9A96E"), size: 7pt)[◆], spacing: 0.4em)
  body
}

#let resume-skill-item(category, skills) = {
  grid(
    columns: (auto, 1fr),
    column-gutter: 1em,
    [#text(weight: "bold", size: 10pt, fill: rgb("#1B3A4B"))[#category:]],
    [#text(size: 10pt)[#skills.join(",  ")]]
  )
  v(0.4em)
}
