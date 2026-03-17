#import "/templates/designer-cv/source/designer-cv.typ": *

#show: designer-cv.with(
  author: (
    firstname: "[FIRST_NAME]", lastname: "[LAST_NAME]",
    role: "[TARGET_ROLE]", email: "[EMAIL]",
    phone: "[PHONE]", portfolio: "https://[PORTFOLIO]",
    address: "[ADDRESS]"
  ),
  accent-color: rgb("#F72585"), profile-picture: none,
)

= Profile
[SUMMARY_PARAGRAPH]

= Experience
#resume-entry(title: "[JOB_TITLE]", location: "[COMPANY]", date: "[START] - [END]", description: "[DESC]")
#resume-item[
  - [ACHIEVEMENT 1]
  - [ACHIEVEMENT 2]
]

= Education
#resume-entry(title: "[DEGREE]", location: "[INSTITUTION]", date: "[START] - [END]")

= Skills
#resume-skill-item("Category", ("Skill 1", "Skill 2"))