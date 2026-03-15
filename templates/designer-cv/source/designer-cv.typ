#import "lib.typ": *

#show: designer-cv.with(
  author: (
    firstname: "Alex",
    lastname: "Morgan",
    role: "Senior Product Designer",
    email: "alex@example.com",
    phone: "+1 234 567 890",
    portfolio: "https://dribbble.com/alexmorgan",
    address: "New York, NY"
  ),
  accent-color: rgb("#F72585"),
  profile-picture: none,
)

= Profile
Award-winning Product Designer with 8+ years of experience creating intuitive, visually striking digital experiences for cross-platform products. Proven ability to bridge the gap between creative vision and business objectives, specializing in zero-to-one product launches and comprehensive design systems.

= Experience

#resume-entry(
  title: "Lead Product Designer",
  location: "Creative Agency Inc, New York",
  date: "2020 — Present",
  description: "Led end-to-end design process for enterprise software solutions."
)

#resume-item[
  - Spearheaded design system overhaul, reducing design-to-development time by 40%
  - Mentored a team of 5 junior and mid-level designers, fostering a culture of critique
  - Increased user engagement by 25% through meticulous UX/UI optimizations
]

#v(1em)

#resume-entry(
  title: "UX/UI Designer",
  location: "Tech Startup Corp, Boston",
  date: "2016 — 2020",
  description: "Designed core experiences for a flagship fintech mobile application."
)

#resume-item[
  - Conducted extensive user research and usability testing with over 200 participants
  - Prototyped high-fidelity mockups and micro-interactions using Figma and Framer
  - Collaborated closely with engineering to ensure pixel-perfect implementation
]
