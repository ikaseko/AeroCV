#import "/templates/vercanard/source/template/main.typ": *
#show: resume.with(
  name: "[FULL_NAME]",
  title: "[TARGET_ROLE]",
  accent-color: rgb("f3bc54"),
  margin: 2.6cm,
  aside: [
    = Contact
    - [EMAIL]
    - [PHONE]
    
    = Skills
    - [SKILL 1]
    - [SKILL 2]
  ]
)

= Experience
#entry("[JOB_TITLE]", "[COMPANY]", "[START]-[END]")

= Education
#entry("[DEGREE]", "[INSTITUTION]", "[START]-[END]")