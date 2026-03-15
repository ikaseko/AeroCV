#import "lib.typ": *

#show: portfolio-cv.with(
  author: (
    firstname: "ELENA",
    lastname: "RODRIGUEZ",
    role: "Full Stack Developer",
    email: "elena@example.com",
    phone: "+1 (555) 987-6543",
    portfolio: "https://elenadev.com",
    github: "https://github.com/elenarodriguez"
  ),
  accent-color: rgb("#58A6FF"), // GitHub Blue
)

= Selected Projects

#resume-project(
  title: "DevStream Video Platform",
  url: "https://devstream.io",
  date: "2023",
  tech: ("React", "Node.js", "WebRTC", "PostgreSQL", "Redis"),
  description: "Built a high-performance video streaming platform for developers. Handled 10k+ concurrent connections utilizing custom WebRTC signaling servers."
)

#resume-project(
  title: "AI Code Reviewer CLI",
  url: "https://github.com/elenarodriguez/ai-review",
  date: "2022",
  tech: ("Rust", "OpenAI API", "Git hooks"),
  description: "An open-source CLI tool that automatically reviews local git commits using LLMs before pushing. Achieved 5k+ stars on GitHub within 2 months."
)

#resume-project(
  title: "E-Commerce GraphQL API",
  url: "https://github.com/elenarodriguez/shop-api",
  date: "2021",
  tech: ("Go", "GraphQL", "MongoDB", "Docker"),
  description: "A highly scalable e-commerce backend with modular inventory, payment processing, and real-time shipping webhooks."
)

= Experience

#resume-entry(
  title: "Senior Backend Engineer",
  location: "TechNova Solutions, San Francisco, CA",
  date: "2021 — Present",
)

#resume-item[
  - Architected microservices yielding 40% reduction in API latency
  - Mentored 4 junior developers and established CI/CD best practices
]

#resume-entry(
  title: "Web Developer",
  location: "Creative Web Agency, Austin, TX",
  date: "2018 — 2021",
)

#resume-item[
  - Delivered 15+ full stack web applications for Fortune 500 clients
  - Integrated complex third-party APIs including Stripe, Twilio, and SendGrid
]

= Education & Skills

#resume-entry(
  title: "B.S. Computer Science",
  location: "University of Texas at Austin",
  date: "2014 — 2018"
)

#resume-skill-item("Languages", ("JavaScript/TypeScript", "Go", "Rust", "Python", "SQL"))
#resume-skill-item("Frameworks", ("React", "Next.js", "Express", "Tailwind CSS"))
#resume-skill-item("DevOps", ("Docker", "Kubernetes", "AWS (EC2, S3, RDS)", "GitHub Actions"))
