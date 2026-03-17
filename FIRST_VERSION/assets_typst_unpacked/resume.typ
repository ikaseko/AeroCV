// Modern CV Resume Template for Typst
#import "lib.typ": *

#show: resume.with(
  author: (
    firstname: "John",
    lastname: "Doe",
    email: "john.doe@example.com",
    phone: "+1-555-123-4567",
    github: "johndoe",
    linkedin: "johndoe",
    address: "New York, USA",
    positions: ("Software Engineer",),
  ),
  profile-picture: none,
  date: datetime.today().display(),
  language: "en",
  colored-headers: true,
  paper-size: "a4",
)

= Experience

#resume-entry(
  title: "Senior Software Engineer",
  location: "Tech Corp, New York",
  date: "2020 - Present",
  description: "Leading development",
)

#resume-item[
  - Improved system performance by 40%
  - Mentored junior developers
]

= Education

#resume-entry(
  title: "University of Technology",
  location: "B.S. in Computer Science",
  date: "2013 - 2017",
)

#resume-item[
  - GPA: 3.8/4.0
]

= Skills

#resume-skill-item("Languages", (strong("Python"), strong("JavaScript"), "Go"))
#resume-skill-item("Tools", (strong("Docker"), "Kubernetes", "Git"))
