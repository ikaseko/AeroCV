#import "/templates/modern-cv/source/lib.typ": *

#show: resume.with(
  author: (
    firstname: "[FIRST_NAME]", lastname: "[LAST_NAME]",
    email: "[EMAIL]", phone: "[PHONE]",
    github: "[GITHUB]", linkedin: "[LINKEDIN]",
    address: "[ADDRESS]", positions: ("[POSITION_1]",),
  ),
  profile-picture: none,
  date: datetime.today().display(),
  language: "en", colored-headers: true,
)

= Experience
#resume-entry(
  title: "[JOB_TITLE]",
  location: "[COMPANY], [LOCATION]",
  date: "[START] - [END]",
  description: "[DESC]"
)
#resume-item[
  - [ACHIEVEMENT 1]
  - [ACHIEVEMENT 2]
]

= Education
#resume-entry(
  title: "[INSTITUTION]",
  location: "[DEGREE]",
  date: "[START] - [END]"
)

= Skills
#resume-skill-item("Languages", (strong("Go"), "Python", "SQL"))
#resume-skill-item("Frameworks", (strong("React"), "Next.js"))