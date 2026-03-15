// Designer Cover Letter Template — Soft, Elegant, Refined "Figma 2026" Aesthetic
// Matches the new designer CV with a subtle gray left sidebar

#let designer-cover-letter(
  author: (),
  profile-picture: none,
  primary-color: rgb("#111111"),
  accent-color: rgb("#F72585"),
  sidebar-color: rgb("#F8F9FA"),
  body-font: "Inter",
  paper-size: "a4",
  body
) = {
  set document(author: author.firstname + " " + author.lastname, title: "Cover Letter - " + author.firstname + " " + author.lastname)
  set page(
    paper: paper-size,
    margin: 0cm,
  )
  set text(font: body-font, size: 9.5pt, fill: rgb("#333333"), weight: "regular", ligatures: false)

  grid(
    columns: (7.5cm, 1fr),
    
    // ─── LEFT COLUMN (Soft gray sidebar) ───
    block(
      width: 100%,
      height: 100%,
      fill: sidebar-color,
      inset: (x: 1.5cm, top: 2.5cm, bottom: 2cm),
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
        #author.email \ \
        #author.phone \ \
        #if "portfolio" in author [ #link(author.portfolio)[#text(fill: accent-color, weight: "semibold")[Portfolio ↗]] \ \ ]
        #if "linkedin" in author [ #link(author.linkedin)[#text(fill: primary-color, weight: "medium")[LinkedIn ↗]] \ \ ]
        #if "address" in author [ #author.address \ \ ]
      ]
    ),
    
    // ─── RIGHT COLUMN (Clean White Body) ───
    block(
      width: 100%,
      height: 100%,
      fill: rgb("#FFFFFF"),
      inset: (x: 2cm, top: 2.5cm, bottom: 2cm),
      [
        #set par(leading: 0.85em)
        #body
      ]
    )
  )
}
