#import "/templates/portfolio-cv/source/portfolio-cv.typ": *

#show: portfolio-cv.with(
  author: (
    firstname: "[FIRST_NAME]", lastname: "[LAST_NAME]",
    role: "[TARGET_ROLE]", email: "[EMAIL]", phone: "[PHONE]",
    portfolio: "https://[PORTFOLIO]", github: "https://[GITHUB]"
  ),
  accent-color: rgb("#58A6FF"),
)

= Experience
#resume-entry(title: "[JOB_TITLE]", location: "[COMPANY]", date: "[START] - [END]")
#resume-item[
  - [ACHIEVEMENT 1]
]

= Selected Projects
#resume-project(
  title: "[PROJECT_NAME]", url: "https://[URL]", date: "[DATE]",
  tech: ("Tech 1", "Tech 2"), description: "[DESC]"
)