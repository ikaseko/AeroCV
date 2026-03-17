#import "/templates/executive-cv/source/executive-cv.typ": *

#show: executive-cv.with(
  author: (
    firstname: "[FIRST_NAME]", lastname: "[LAST_NAME]",
    email: "[EMAIL]", phone: "[PHONE]",
    linkedin: "https://[LINKEDIN]", address: "[ADDRESS]"
  ),
  accent-color: rgb("#1B3A4B"),
)

= Summary
[SUMMARY_PARAGRAPH]

= Professional Experience
#resume-entry(title: "[JOB_TITLE]", location: "[COMPANY]", date: "[START] - [END]")
#resume-item[
  - [ACHIEVEMENT 1]
]

= Education
#resume-entry(title: "[DEGREE]", location: "[INSTITUTION]", date: "[START] - [END]", description: "[DESC]")