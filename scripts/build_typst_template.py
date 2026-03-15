import os
import shutil
import zipfile
import tarfile

base_dir = r"C:\Users\bbog2\Downloads\AWESOME_CV"
modern_cv_dir = os.path.join(base_dir, "modern-cv")
build_dir = os.path.join(base_dir, "build_typst")
fonts_dir = os.path.join(build_dir, "fonts")
packages_dir = os.path.join(build_dir, "packages")

# Clean build directory
if os.path.exists(build_dir):
    shutil.rmtree(build_dir)
os.makedirs(build_dir, exist_ok=True)
os.makedirs(fonts_dir, exist_ok=True)
os.makedirs(packages_dir, exist_ok=True)

print("=== Building Typst assets (FULL OFFLINE + Font Fix v2) ===\n")

# 1. Extract packages to separate directories
print("Extracting packages...")
os.makedirs(os.path.join(packages_dir, "linguify"), exist_ok=True)
os.makedirs(os.path.join(packages_dir, "fontawesome"), exist_ok=True)

with tarfile.open(os.path.join(base_dir, "linguify.tar.gz"), 'r:gz') as tar:
    tar.extractall(os.path.join(packages_dir, "linguify"))
print("  Extracted linguify")

with tarfile.open(os.path.join(base_dir, "fontawesome.tar.gz"), 'r:gz') as tar:
    tar.extractall(os.path.join(packages_dir, "fontawesome"))
print("  Extracted fontawesome")

# 2. Patch fontawesome lib-impl.typ to use correct font family names
lib_impl_path = os.path.join(packages_dir, "fontawesome", "lib-impl.typ")
with open(lib_impl_path, 'r', encoding='utf-8') as f:
    lib_impl_content = f.read()

# The fontawesome package already uses correct names "Font Awesome 7 Free" etc.
# We just need to ensure our OTF files have these internal names (they do)
# No patching needed - the original is correct
print("  Using original fontawesome lib-impl.typ")

# 3. Copy and patch lib.typ
with open(os.path.join(modern_cv_dir, "lib.typ"), 'r', encoding='utf-8') as f:
    lib_content = f.read()

# Change imports from @preview to local packages
lib_content = lib_content.replace(
    '#import "@preview/fontawesome:0.6.0": *',
    '#import "packages/fontawesome/lib.typ": *'
)
lib_content = lib_content.replace(
    '#import "@preview/linguify:0.5.0": *',
    '#import "packages/linguify/src/lib.typ": *'
)

# Fix: Remove description and keywords from set document() calls
lib_content = lib_content.replace(
    '''set document(
      author: author.firstname + " " + author.lastname,
      title: lflib._linguify("resume", lang: language, from: lang_data).ok,
      description: desc,
      keywords: keywords,
    )''',
    '''set document(
      author: author.firstname + " " + author.lastname,
      title: lflib._linguify("resume", lang: language, from: lang_data).ok,
    )'''
)

lib_content = lib_content.replace(
    '''set document(
      author: author.firstname + " " + author.lastname,
      title: lflib._linguify("cover-letter", lang: language, from: lang_data).ok,
      description: desc,
      keywords: keywords,
    )''',
    '''set document(
      author: author.firstname + " " + author.lastname,
      title: lflib._linguify("cover-letter", lang: language, from: lang_data).ok,
    )'''
)

# Keep original font family names - Typst will find them from font-path
# Source Sans 3 is the correct internal name (no need for Source Sans Pro fallback)
lib_content = lib_content.replace(
    '''font: ("Source Sans Pro", "Source Sans 3")''',
    '''font: ("Source Sans 3")'''
)

lib_content = lib_content.replace(
    '''header-font: "Roboto"''',
    '''header-font: "Roboto"'''
)

with open(os.path.join(build_dir, "lib.typ"), 'w', encoding='utf-8') as f:
    f.write(lib_content)
print("Copied and patched lib.typ")

# 4. Copy typst.toml
shutil.copy(os.path.join(modern_cv_dir, "typst.toml"), os.path.join(build_dir, "typst.toml"))
print("Copied typst.toml")

# 5. Copy lang.toml
shutil.copy(os.path.join(modern_cv_dir, "lang.toml"), os.path.join(build_dir, "lang.toml"))
print("Copied lang.toml")

# 6. Copy profile.png
shutil.copy(os.path.join(modern_cv_dir, "template", "profile.png"), os.path.join(build_dir, "profile.png"))
print("Copied profile.png")

# 7. Copy Source Sans 3 fonts
source_sans_dir = os.path.join(base_dir, "source-sans-release", "TTF")
font_mapping = {
    "SourceSans3-Regular.ttf": "SourceSans3-Regular.ttf",
    "SourceSans3-Bold.ttf": "SourceSans3-Bold.ttf",
    "SourceSans3-It.ttf": "SourceSans3-Italic.ttf",
    "SourceSans3-Light.ttf": "SourceSans3-Light.ttf",
}

for src_file, dest_file in font_mapping.items():
    src_path = os.path.join(source_sans_dir, src_file)
    dest_path = os.path.join(fonts_dir, dest_file)
    if os.path.exists(src_path):
        shutil.copy(src_path, dest_path)
        print(f"Copied {src_file} -> fonts/{dest_file}")
    else:
        print(f"WARNING: {src_file} not found")

# 8. Copy Roboto font
shutil.copy(
    os.path.join(base_dir, "Roboto[ital,wdth,wght].ttf"),
    os.path.join(fonts_dir, "Roboto-Regular.ttf")
)
print("Copied Roboto[ital,wdth,wght].ttf -> fonts/Roboto-Regular.ttf")

# 9. Copy FontAwesome OTF files with FA7 names (matching internal font metadata)
fa_otf_dir = os.path.join(base_dir, "fontawesome-main", "fontawesome7", "opentype")
fa_fonts = [
    ("FontAwesome7Free-Regular-400.otf", "FontAwesome7Free-Regular-400.otf"),
    ("FontAwesome7Free-Solid-900.otf", "FontAwesome7Free-Solid-900.otf"),
    ("FontAwesome7Brands-Regular-400.otf", "FontAwesome7Brands-Regular-400.otf"),
]
for src_file, dest_file in fa_fonts:
    src_path = os.path.join(fa_otf_dir, src_file)
    dest_path = os.path.join(fonts_dir, dest_file)
    if os.path.exists(src_path):
        shutil.copy(src_path, dest_path)
        print(f"Copied {src_file} -> fonts/{dest_file}")
    else:
        print(f"WARNING: {src_file} not found")

# 10. Copy Typst Linux binary
typst_linux_dir = os.path.join(base_dir, "typst-x86_64-unknown-linux-musl")
typst_binary = os.path.join(typst_linux_dir, "typst")
shutil.copy(typst_binary, os.path.join(build_dir, "typst"))
print("Copied typst binary (Linux x86_64)")

# 11. Create resume.typ template
resume_template = '''// Modern CV Resume Template for Typst
#import "lib.typ": *

#show: resume.with(
  author: (
    firstname: "John",
    lastname: "Doe",
    email: "john.doe@example.com",
    phone: "+1-555-123-4567",
    github: "johndoe",
    linkedin: "johndoe",
    address: "New York, USA",
    positions: ("Software Engineer",),
  ),
  profile-picture: none,
  date: datetime.today().display(),
  language: "en",
  colored-headers: true,
  paper-size: "a4",
)

= Experience

#resume-entry(
  title: "Senior Software Engineer",
  location: "Tech Corp, New York",
  date: "2020 - Present",
  description: "Leading development",
)

#resume-item[
  - Improved system performance by 40%
  - Mentored junior developers
]

= Education

#resume-entry(
  title: "University of Technology",
  location: "B.S. in Computer Science",
  date: "2013 - 2017",
)

#resume-item[
  - GPA: 3.8/4.0
]

= Skills

#resume-skill-item("Languages", (strong("Python"), strong("JavaScript"), "Go"))
#resume-skill-item("Tools", (strong("Docker"), "Kubernetes", "Git"))
'''

with open(os.path.join(build_dir, "resume.typ"), "w", encoding="utf-8") as f:
    f.write(resume_template)
print("Created resume.typ template")

# 12. Create assets_typst.zip WITH ALL FILES
zip_path = os.path.join(base_dir, "assets_typst.zip")
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
    # Add resume.typ (template)
    zipf.write(os.path.join(build_dir, "resume.typ"), "resume.typ")
    print(f"Added: resume.typ")
    
    # Add lib.typ
    zipf.write(os.path.join(build_dir, "lib.typ"), "lib.typ")
    print(f"Added: lib.typ")
    
    # Add typst.toml
    zipf.write(os.path.join(build_dir, "typst.toml"), "typst.toml")
    print(f"Added: typst.toml")
    
    # Add lang.toml
    zipf.write(os.path.join(build_dir, "lang.toml"), "lang.toml")
    print(f"Added: lang.toml")
    
    # Add profile.png
    zipf.write(os.path.join(build_dir, "profile.png"), "profile.png")
    print(f"Added: profile.png")
    
    # Add typst binary
    zipf.write(os.path.join(build_dir, "typst"), "typst")
    print(f"Added: typst (binary)")
    
    # Add fonts directory
    for root, dirs, files in os.walk(fonts_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.join("fonts", file)
            zipf.write(file_path, arcname)
            print(f"Added: {arcname}")
    
    # Add packages directory (linguify + fontawesome)
    for root, dirs, files in os.walk(packages_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, build_dir)
            zipf.write(file_path, arcname)
            print(f"Added: {arcname}")

print(f"\n✓ Created {zip_path}")

# List the final structure
print("\n=== Final assets_typst.zip structure ===")
total_size = 0
with zipfile.ZipFile(zip_path, 'r') as zipf:
    for name in sorted(zipf.namelist()):
        info = zipf.getinfo(name)
        total_size += info.file_size
        print(f"  {name} ({info.file_size:,} bytes)")

print(f"\nTotal uncompressed size: {total_size:,} bytes")
print(f"Compressed size: {os.path.getsize(zip_path):,} bytes")
print("\n=== Build complete! ===")
