#import "/templates/vantage/source/vantage-typst.typ": *

#vantage(
  name: "[FULL_NAME]",
  position: "[TARGET_POSITION]",
  links: (
    (name: "email", link: "mailto:[EMAIL]", display: "[EMAIL]"),
    (name: "github", link: "https://[GITHUB]", display: "[GITHUB]"),
    (name: "linkedin", link: "https://[LINKEDIN]", display: "[LINKEDIN]"),
  ),
  tagline: [[SUMMARY_PARAGRAPH]],
  [
    == Experience
    === [JOB_TITLE] | [COMPANY]
    #term("[START] - [END]", "[LOCATION]")
    - [ACHIEVEMENT_1]
    - [ACHIEVEMENT_2]
    
    == Projects
    === [PROJECT_NAME] | [TECH_STACK]
    #term("[DATE]", "")
    - [ACHIEVEMENT_1]

    == Education
    === [DEGREE] 
    #term("[DATES]", "[LOCATION]")
  ],
  [
    == Skills
    #skill("[SKILL_1]", 5)
    #skill("[SKILL_2]", 4)
  ]
)