#import "lib.typ": *

#show: executive-cover-letter.with(
  author: (
    firstname: "Jonathan",
    lastname: "Crawford",
    email: "jcrawford@example.com",
    phone: "+1 (555) 123-4567",
    linkedin: "https://linkedin.com/in/jcrawford",
    address: "Chicago, IL",
    date: "September 15, 2024"
  ),
  recipient: (
    name: "Board of Directors",
    title: "Executive Search Committee",
    company: "Apex Global Financial",
    address: "400 Wall Street, New York, NY"
  ),
  accent-color: rgb("#1B3A4B"),
)

#cover-letter-body[
  Dear Members of the Executive Search Committee,

  I am writing to express my strong interest in the Chief Financial Officer position at Apex Global Financial, as recently discussed with your recruitment partners. With over 15 years of progressive executive experience navigating complex corporate restructurings and leading multi-million dollar portfolios, I am well-positioned to drive sustainable fiscal strategies at Apex.
  
  During my tenure at Global Investments Partners as Executive Director of Finance, I spearheaded a global operational overhaul that reduced redundancies by 22% while concurrently managing a \$450M portfolio that achieved consistent double-digit growth. My expertise lies in aligning financial discipline with broader strategic objectives to secure robust market positioning. 
  
  I welcome the opportunity to outline how my background in risk mitigation and M&A due diligence aligns with your strategic vision for the upcoming fiscal decade. I look forward to speaking with the committee soon.
]

#cover-letter-closing("Respectfully yours,")
#text(weight: "bold")[Jonathan Crawford]
