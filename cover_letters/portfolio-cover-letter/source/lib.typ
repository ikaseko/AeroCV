// Portfolio Cover Letter Template — Modern header matching portfolio-cv

#let portfolio-cover-letter(
  author: (:),
  recipient: (:),
  accent-color: rgb("#0077B6"),
  dark-color: rgb("#023E73"),
  body-font: "Source Sans 3",
  paper-size: "a4",
  body
) = {
  set document(author: author.firstname + " " + author.lastname, title: "Cover Letter - " + author.firstname + " " + author.lastname)
  set page(
    paper: paper-size,
    margin: (left: 0cm, right: 0cm, top: 0cm, bottom: 0cm),
  )
  set text(font: body-font, size: 10pt, fill: rgb("#333333"), weight: "regular", ligatures: false)

  // === HEADER ===
  block(
    width: 100%,
    fill: dark-color,
    inset: (x: 1.8cm, top: 1.3cm, bottom: 1cm),
    [
      #text(size: 26pt, weight: "bold", fill: white, tracking: 0.05em)[#author.firstname #author.lastname]
      #v(0.3em)
      #if "role" in author [
        #text(size: 12pt, weight: "medium", fill: rgb("#90CAF9"))[#author.role]
        #v(0.4em)
      ]
      #text(size: 9.5pt, fill: rgb("#B0C4D8"))[
        #author.email
        #h(1em) | #h(1em)
        #author.phone
        #if "portfolio" in author [ #h(1em) | #h(1em) *#link(author.portfolio)[Portfolio]* ]
        #if "github" in author [ #h(1em) | #h(1em) #link(author.github)[GitHub] ]
      ]
    ]
  )

  block(width: 100%, height: 3pt, fill: accent-color)

  // === BODY ===
  block(
    width: 100%,
    inset: (x: 1.8cm, top: 1.5cm, bottom: 1cm),
    {
      [
        #if "date" in author [ #text(size: 10pt, fill: rgb("#888888"))[#author.date] \ \ ]
        #text(weight: "bold", size: 11pt, fill: dark-color)[#recipient.name] \
        #if "title" in recipient [ #text(size: 10pt)[#recipient.title] \ ]
        #if "company" in recipient [ #text(size: 10pt)[#recipient.company] \ ]
        #if "address" in recipient [ #text(size: 10pt, fill: rgb("#666666"))[#recipient.address] ]
      ]
      
      v(2em)
      
      body
    }
  )
}

#let cover-letter-body(body) = {
  set par(justify: true, linebreaks: "optimized", leading: 1em)
  set text(size: 10.5pt)
  body
  v(2em)
}

#let cover-letter-closing(closing-text) = {
  text(size: 10.5pt)[#closing-text]
  v(3em)
}
