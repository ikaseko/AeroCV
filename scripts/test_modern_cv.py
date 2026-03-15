import os, zipfile, subprocess, tempfile

z = zipfile.ZipFile("agent_output/modern-cv.zip")
t = tempfile.mkdtemp()
z.extractall(t)

code = """#import "lib.typ": *
#show: resume.with(
  author: (firstname: "Test", lastname: "User", email: "test@e.com", phone: "+1", github: "g", address: "A", positions: ("E",)),
  date: datetime.today().display(), language: "en", colored-headers: true,
)
= Skills
#resume-skill-item("Cat", ("Go",))
"""

with open(os.path.join(t, "resume.typ"), "w") as f:
    f.write(code)

r = subprocess.run(
    ["typst.exe", "compile", "--font-path", os.path.join(t, "fonts"), os.path.join(t, "resume.typ")],
    capture_output=True, text=True
)
print("Return code:", r.returncode)
print("STDERR:", r.stderr)
print("PDF exists:", os.path.exists(os.path.join(t, "resume.pdf")))
