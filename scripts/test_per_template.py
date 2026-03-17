"""Test that each per-template zip compiles standalone."""
import os, zipfile, subprocess, shutil, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "agent_output"
TYPST_BIN = ROOT / "typst.exe"  # local Windows binary

# Minimal test code for each template
TEST_CODE = {
    "modern-cv": '''#import "lib.typ": *
#show: resume.with(
  author: (firstname: "Test", lastname: "User", email: "test@example.com", phone: "+1234567890", github: "testuser", address: "City", positions: ("Engineer",)),
  date: datetime.today().display(), language: "en", colored-headers: true,
  show-footer: false,
)
= Experience
#resume-entry(title: "Job", location: "Company", date: "2020-2024")
#resume-item[- Built things]
= Skills
#resume-skill-item("Languages", (strong("Go"), "Python"))
''',
    "vantage": '''#import "vantage-typst.typ": *
#vantage(
  name: "Test User", position: "Engineer",
  links: ((name: "email", link: "mailto:test@test.com", display: "test@test.com"),),
  tagline: [Summary text here],
  [
    == Experience
    === Engineer | Company
    #term("2020-2024", "City")
    - Built things
  ],
  [
    == Skills
    #skill("Go", 5)
  ]
)
''',
    "designer-cv": '''#import "designer-cv.typ": *
#show: designer-cv.with(
  author: (firstname: "Test", lastname: "User", role: "Engineer", email: "test@test.com", phone: "+1234567890"),
  accent-color: rgb("#F72585"),
)
= Experience
#resume-entry(title: "Job", location: "Co", date: "2020-2024", description: "D")
#resume-item[- Built things]
= Skills
#resume-skill-item("Cat", ("Go", "Python"))
''',
    "executive-cv": '''#import "executive-cv.typ": *
#show: executive-cv.with(
  author: (firstname: "Test", lastname: "User", email: "test@test.com", phone: "+1234567890"),
  accent-color: rgb("#1B3A4B")
)
= Experience
#resume-entry(title: "Job", location: "Co", date: "2020-2024")
#resume-item[- Built things]
''',
    "portfolio-cv": '''#import "portfolio-cv.typ": *
#show: portfolio-cv.with(
  author: (firstname: "Test", lastname: "User", role: "Engineer", email: "test@test.com", phone: "+1234567890", github: "https://github.com/test"),
  accent-color: rgb("#58A6FF")
)
= Experience
#resume-entry(title: "Job", location: "Co", date: "2020-2024")
#resume-item[- Built things]
= Projects
#resume-project(title: "Proj", url: "https://example.com", date: "2023", tech: ("Go",), description: "D")
''',
    "typst-cv": '''#import "template.typ": conf, date, show_skills
#let details = (name: "Test User", phonenumber: "+1234567890", email: "test@test.com", links: (github: "https://github.com/test",))
#show: doc => conf(details, doc)
= Experience
== Engineer #date("2020-2024")
=== Company
- Built things
= Skills
#show_skills(("Languages": ("Go", "Python"),))
''',
    "vercanard": '''#import "main.typ": *
#show: resume.with(
  name: "Test User", title: "Engineer", accent-color: rgb("f3bc54"), margin: 2.6cm,
  aside: [= Contact
- #("test@test.com")
= Skills
- Go]
)
= Experience
#entry("Engineer", "Company", "2020-2024")
''',
    "brilliant-cv": '''#import "lib.typ": cv, cv-section, cv-entry
#let metadata = toml("metadata_clean.toml")
#metadata.language = "en"
#(metadata.personal.first_name = "Test")
#(metadata.personal.last_name = "User")
#(metadata.personal.info.email = "test@test.com")
#show: cv.with(metadata, profile-photo: none)
#cv-section("Experience")
#cv-entry(title: "Job", society: "Company", date: "2020-2024", location: "City", description: list([Built things]))
''',
}

def test_template(template_id: str):
    zip_path = OUTPUT_DIR / f"{template_id}.zip"
    if not zip_path.exists():
        print(f"  [MISSING] {template_id}: zip not found")
        return False

    with tempfile.TemporaryDirectory() as tmpdir:
        # Extract template zip
        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extractall(tmpdir)

        # Write test code
        test_file = os.path.join(tmpdir, "resume.typ")
        with open(test_file, "w", encoding="utf-8") as f:
            f.write(TEST_CODE[template_id])

        # Compile
        result = subprocess.run(
            [str(TYPST_BIN), "compile", "--font-path", os.path.join(tmpdir, "fonts"), test_file],
            capture_output=True, text=True, cwd=tmpdir
        )

        pdf_path = os.path.join(tmpdir, "resume.pdf")
        if result.returncode == 0 and os.path.exists(pdf_path):
            size_kb = os.path.getsize(pdf_path) / 1024
            print(f"  [OK] {template_id}: compiled ({size_kb:.0f} KB)")
            return True
        else:
            print(f"  [FAIL] {template_id}: FAILED")
            print(f"     stderr: {result.stderr[:2000]}")
            return False

def main():
    print("=== Testing per-template zip compilation ===\n")
    results = {}
    for tid in TEST_CODE:
        results[tid] = test_template(tid)

    passed = sum(1 for v in results.values() if v)
    total = len(results)
    print(f"\n{'='*40}")
    print(f"Results: {passed}/{total} passed")

if __name__ == "__main__":
    main()
