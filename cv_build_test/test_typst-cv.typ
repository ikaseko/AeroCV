#import "/templates/typst-cv/source/template.typ": conf, date, show_skills

#let details = (
  name: "[FULL_NAME]",
  phonenumber: "[PHONE]",
  email: "[EMAIL]",
  address: "[ADDRESS]",
  links: (
    github: "https://[GITHUB]",
    linkedin: "https://[LINKEDIN]"
  )
)
#show: doc => conf(details, doc)

= Work Experience
== [JOB_TITLE] #date("[START] - [END]")
=== [COMPANY]
- [ACHIEVEMENT 1]

= Skills
#show_skills((
  "Languages": ("Skill 1", "Skill 2"),
))