#import "lib.typ": *

#show: portfolio-cover-letter.with(
  author: (
    firstname: "ELENA",
    lastname: "RODRIGUEZ",
    role: "Full Stack Developer",
    email: "elena@example.com",
    phone: "+1 (555) 987-6543",
    portfolio: "https://elenadev.com",
    github: "https://github.com/elenarodriguez",
    date: "May 20, 2025"
  ),
  recipient: (
    name: "Engineering Hiring Manager",
    company: "FutureTech Software Labs",
    address: "Austin, TX - Remote"
  ),
  accent-color: rgb("#0077B6"),
)

#cover-letter-body[
  Dear Engineering Hiring Manager,

  I am writing to apply for the Senior Frontend Engineer position at FutureTech Software Labs. Having followed your recent open-source contributions to the React ecosystem, I am incredibly excited about the prospect of joining a team that prioritizes developer experience and cutting-edge web performance.
  
  In my current role as a Senior Backend Engineer at TechNova Solutions, I architected a microservices environment that reduced API latency by 40%. However, my true passion lies in building seamless user interfaces and robust full-stack applications. You can view one of my proudest architectural achievements on my portfolio (DevStream), a WebRTC-based platform capable of handling 10k+ concurrent connections, built entirely from scratch. 
  
  I am particularly drawn to FutureTech because of your commitment to accessible, high-performance web applications. I believe my open-source experience and deep knowledge of both Next.js and Go would allow me to make an immediate impact on your upcoming core platform rewrite.

  I have included a link to my GitHub where you can review my public repositories and code quality. Thank you for your time and consideration — I hope to discuss my qualifications with you soon.
]

#cover-letter-closing("Best regards,")
#text(weight: "bold")[Elena Rodriguez]
