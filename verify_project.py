"""
Verify project structure and assets
"""
import os
import json

base_dir = r"C:\Users\bbog2\Downloads\AWESOME_CV"

print("=" * 70)
print("=== AeroCV Project Verification ===")
print("=" * 70)

# Check required directories
required_dirs = [
    "templates",
    "templates/modern-cv",
    "templates/modern-cv/assets",
    "templates/modern-cv/fonts",
    "templates/modern-cv/packages",
    "template_images",
    "template_images/resumes",
    "template_images/cover_letters",
    "cover_letters",
    "cover_letters/modern-cv",
    "output",
    "scripts",
    "docs",
    "schemas",
]

print("\n📁 Directory Structure:")
print("-" * 70)
all_dirs_exist = True
for dir_path in required_dirs:
    full_path = os.path.join(base_dir, dir_path)
    exists = os.path.exists(full_path)
    status = "✓" if exists else "✗"
    print(f"  {status} {dir_path}")
    if not exists:
        all_dirs_exist = False

# Check required files
required_files = [
    "templates_registry.json",
    "quick_reference.json",
    "SYSTEM_PROMPT_TYPST.md",
    "templates/modern-cv/assets/typst_assets.zip",
    "schemas/templates_registry.schema.json",
    "schemas/quick_reference.schema.json",
]

print("\n📄 Required Files:")
print("-" * 70)
all_files_exist = True
for file_path in required_files:
    full_path = os.path.join(base_dir, file_path)
    exists = os.path.exists(full_path)
    status = "✓" if exists else "✗"
    size = ""
    if exists:
        size = f"({os.path.getsize(full_path):,} bytes)"
    print(f"  {status} {file_path} {size}")
    if not exists:
        all_files_exist = False

# Validate JSON files
print("\n🔍 JSON Validation:")
print("-" * 70)
json_files = [
    "templates_registry.json",
    "quick_reference.json",
]
for json_file in json_files:
    full_path = os.path.join(base_dir, json_file)
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"  ✓ {json_file} - Valid JSON")
        if "version" in data:
            print(f"    Version: {data['version']}")
    except json.JSONDecodeError as e:
        print(f"  ✗ {json_file} - Invalid JSON: {e}")

# Summary
print("\n" + "=" * 70)
print("=== Summary ===")
print("=" * 70)
if all_dirs_exist and all_files_exist:
    print("✅ Project structure is complete and ready!")
else:
    print("⚠️  Some files or directories are missing!")
    if not all_dirs_exist:
        print("  - Missing directories")
    if not all_files_exist:
        print("  - Missing files")

# Template info
print("\n📋 Available Templates:")
print("-" * 70)
try:
    with open(os.path.join(base_dir, "quick_reference.json"), 'r', encoding='utf-8') as f:
        ref = json.load(f)
    
    print("  Resume Templates:")
    for t in ref["availableTemplates"]["resumes"]:
        print(f"    • {t['name']} ({t['id']})")
        print(f"      Assets: {t['assetsPath']}")
        print(f"      Features: {', '.join(t['keyFeatures'])}")
    
    print("\n  Cover Letter Templates:")
    for t in ref["availableTemplates"]["coverLetters"]:
        print(f"    • {t['name']} ({t['id']})")
        print(f"      Matches: {t.get('matchesResume', 'N/A')}")
        print(f"      Assets: {t['assetsPath']}")
except Exception as e:
    print(f"  ⚠️  Could not load template info: {e}")

print("\n" + "=" * 70)
