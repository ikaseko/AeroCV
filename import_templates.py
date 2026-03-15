"""
Import multiple Typst CV templates into the project structure.
Clones repositories and organizes them into templates/ directory.
"""
import os
import subprocess
import shutil
import json

base_dir = r"C:\Users\bbog2\Downloads\AWESOME_CV"
templates_dir = os.path.join(base_dir, "templates")
temp_dir = os.path.join(base_dir, "_temp_import")

# Templates to import
# Format: (repo_url, template_id, template_name, type)
templates_to_import = [
    # Already exists: modern-cv
    # New templates:
    ("https://github.com/JCGoran/typst-cv-template", "typst-cv", "Typst CV Template", "resume"),
    ("https://github.com/yunanwg/brilliant-CV", "brilliant-cv", "Brilliant CV", "resume"),
    ("https://github.com/elegaanz/vercanard", "vercanard", "VerCanard", "resume"),
    ("https://github.com/sardorml/vantage-typst", "vantage", "Vantage", "resume"),
    ("https://github.com/UntimelyCreation/typst-neat-cv", "neat-cv", "Neat CV", "resume"),
]

print("=" * 70)
print("=== Typst CV Template Importer ===")
print("=" * 70)

# Create temp directory
os.makedirs(temp_dir, exist_ok=True)
print(f"\n📁 Temp directory: {temp_dir}")

# Clone repositories
print("\n=== Cloning Repositories ===\n")
cloned_templates = []

for repo_url, template_id, name, doc_type in templates_to_import:
    print(f"\n🔄 Cloning: {name}")
    print(f"   URL: {repo_url}")
    
    clone_dir = os.path.join(temp_dir, template_id)
    
    # Skip if already exists
    if os.path.exists(clone_dir) and os.path.exists(os.path.join(clone_dir, ".git")):
        print(f"   ⚠️  Already exists, pulling latest...")
        try:
            subprocess.run(["git", "-C", clone_dir, "pull"], check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            print(f"   ⚠️  Pull failed: {e}")
    else:
        try:
            subprocess.run(["git", "clone", "--depth", "1", repo_url, clone_dir], 
                         check=True, capture_output=True, timeout=60)
            print(f"   ✓ Cloned successfully")
        except subprocess.CalledProcessError as e:
            print(f"   ✗ Clone failed: {e}")
            continue
        except subprocess.TimeoutExpired:
            print(f"   ✗ Clone timed out")
            continue
    
    cloned_templates.append({
        "id": template_id,
        "name": name,
        "type": doc_type,
        "repo": repo_url,
        "source_dir": clone_dir
    })

print(f"\n=== Cloned {len(cloned_templates)} templates ===")

# Show summary
print("\n📋 Imported Templates:")
for t in cloned_templates:
    print(f"  • {t['name']} ({t['id']})")
    print(f"    Source: {t['source_dir']}")

print("\n" + "=" * 70)
print("=== Next Steps ===")
print("=" * 70)
print("""
1. Review cloned templates in _temp_import/
2. Run: python organize_templates.py
3. Run: python build_all_assets.py
4. Run: python generate_previews.py
5. Run: python update_registry.py
""")

# Save import manifest
manifest = {
    "imported_templates": cloned_templates,
    "temp_dir": temp_dir,
    "templates_dir": templates_dir
}

manifest_path = os.path.join(base_dir, "_import_manifest.json")
with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print(f"\n💾 Import manifest saved to: {manifest_path}")
