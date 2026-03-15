// Executive Cover Letter Template — Navy header band with gold accent

#let executive-cover-letter(
  author: (:),
  recipient: (:),
  accent-color: rgb("#1B3A4B"),
  header-bg: rgb("#1B3A4B"),
  body-font: "Source Sans 3",
  paper-size: "a4",
  body
) = {
  set document(author: author.firstname + " " + author.lastname, title: "Cover Letter - " + author.firstname + " " + author.lastname)
  set page(
    paper: paper-size,
    margin: (left: 0cm, right: 0cm, top: 0cm, bottom: 0cm),
  )
  set text(font: body-font, size: 10.5pt, fill: rgb("#222222"), weight: "regular", ligatures: false)

  // === HEADER BANNER ===
  block(
    width: 100%,
    fill: header-bg,
    inset: (x: 2cm, y: 1.2cm),
    [
      #text(size: 26pt, weight: "bold", fill: white, tracking: 0.1em)[#upper(author.firstname + " " + author.lastname)]
      #v(0.4em)
      #text(size: 10pt, fill: rgb("#B0C4D8"), weight: "medium")[
        #if "address" in author [ #author.address #h(1em) ]
        #author.phone #h(1em) #author.email
        #if "linkedin" in author [ #h(1em) #link(author.linkedin)[LinkedIn] ]
      ]
    ]
  )

  block(width: 100%, height: 4pt, fill: rgb("#C9A96E"))

  // === BODY ===
  block(
    width: 100%,
    inset: (x: 2cm, top: 1.5cm, bottom: 1cm),
    {
      // Recipient info
      [
        #if "date" in author [ #text(size: 10pt)[#author.date] \ \ ]
        #text(weight: "bold", size: 11pt, fill: accent-color)[#recipient.name] \
        #if "title" in recipient [ #text(size: 10.5pt)[#recipient.title] \ ]
        #if "company" in recipient [ #text(size: 10.5pt)[#recipient.company] \ ]
        #if "address" in recipient [ #text(size: 10.5pt, fill: rgb("#555555"))[#recipient.address] ]
      ]
      
      v(2em)
      
      body
    }
  )
}

#let cover-letter-body(body) = {
  set par(justify: true, linebreaks: "optimized", leading: 1em)
  set text(size: 11pt)
  body
  v(2em)
}

#let cover-letter-closing(closing-text) = {
  text(size: 11pt)[#closing-text]
  v(3em)
}
