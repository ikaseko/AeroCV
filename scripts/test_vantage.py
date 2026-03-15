import subprocess
import os

base = "c:/Users/bbog2/Downloads/AWESOME_CV"
work = f"{base}/cv_build_test"
os.makedirs(work, exist_ok=True)

typst_code = f"""
#import "../templates/vantage/source/vantage-typst.typ": *

#vantage(
  name: "Ivan Kaseko",
  position: "Software Engineer",
  links: (
    (name: "email", link: "mailto:test@test.com", display: "test@test.com"),
  ),
  tagline: [A short summary here.],
  [
    == Experience
    === Job 1
    #term("2020 - Present", "Remote")
    - Bullet 1
    - Bullet 2
  ],
  [
    == Skills
    #skill("Go", 5)
    #skill("Python", 4)
  ]
)
"""

with open(f"{work}/test_vantage.typ", "w", encoding="utf-8") as f:
    f.write(typst_code)

print("Compiling...")
proc = subprocess.run([
    f"{base}/typst.exe", "compile",
    "--root", base,
    f"{work}/test_vantage.typ",
    f"{work}/test_vantage.pdf"
], capture_output=True, text=True)

if proc.returncode == 0:
    print(f"Success! PDF generated at {work}/test_vantage.pdf")
else:
    print("Failed:")
    print(proc.stderr)

