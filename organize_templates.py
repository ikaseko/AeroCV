"""
Organize imported templates into the project structure.
Copies templates to templates/<id>/ with proper structure.
"""
import os
import shutil
import json

base_dir = r"C:\Users\bbog2\Downloads\AWESOME_CV"
temp_dir = os.path.join(base_dir, "_temp_import")
templates_dir = os.path.join(base_dir, "templates")
template_images_dir = os.path.join(base_dir, "template_images")

# Template configurations
template_configs = {
    "typst-cv": {
        "name": "Typst CV",
        "type": "resume",
        "main_file": "template.typ",
        "preview": "example.png",
        "has_cover_letter": False,
        "fonts": [],
        "packages": [],
        "description": "Simple and clean Typst CV template with customizable parameters."
    },
    "brilliant-cv": {
        "name": "Brilliant CV",
        "type": "resume",
        "main_file": "template/cv.typ",
        "preview": "thumbnail.png",
        "has_cover_letter": True,
        "cover_letter_file": "template/letter.typ",
        "fonts": ["Roboto", "Inter", "Source Sans"],
        "packages": ["fontawesome:0.6.0", "tidy:0.4.2"],
        "description": "Professional multi-language CV with modular sections and ATS-friendly design."
    },
    "vercanard": {
        "name": "VerCanard",
        "type": "resume", 
        "main_file": "template.typ",
        "preview": "thumbnail.png",
        "has_cover_letter": False,
        "fonts": [],
        "packages": ["vercanard:1.0.3"],
        "description": "Minimalist single-page CV template."
    },
    "vantage": {
        "name": "Vantage",
        "type": "resume",
        "main_file": "vantage-typst.typ",
        "preview": "screenshot.png",
        "has_cover_letter": False,
        "fonts": [],
        "packages": [],
        "description": "Clean CV with SVG icon support."
    },
    "neat-cv": {
        "name": "Neat CV",
        "type": "resume",
        "main_file": "src/template.typ",
        "preview": "output/cv_en.pdf",  # Will generate preview from PDF
        "has_cover_letter": True,
        "cover_letter_file": "src/letter.typ",
        "fonts": ["Source Sans Pro"],
        "packages": [],
        "description": "Clean bilingual (EN/FR) CV with cover letter support."
    }
}

print("=" * 70)
print("=== Organizing Templates ===")
print("=" * 70)

organized = []

for template_id, config in template_configs.items():
    print(f"\n{'='*70}")
    print(f"Processing: {config['name']} ({template_id})")
    print(f"{'='*70}")
    
    source_dir = os.path.join(temp_dir, template_id)
    target_dir = os.path.join(templates_dir, template_id)
    
    if not os.path.exists(source_dir):
        print(f"  [WARN] Source not found: {source_dir}")
        continue
    
    # Create target directory
    os.makedirs(target_dir, exist_ok=True)
    os.makedirs(os.path.join(target_dir, "source"), exist_ok=True)
    os.makedirs(os.path.join(target_dir, "assets"), exist_ok=True)
    os.makedirs(os.path.join(target_dir, "fonts"), exist_ok=True)
    os.makedirs(os.path.join(target_dir, "packages"), exist_ok=True)
    
    # Copy source files
    print(f"  Copying source files...")
    
    # Copy all files except .git
    for item in os.listdir(source_dir):
        if item == '.git':
            continue
        source_item = os.path.join(source_dir, item)
        target_item = os.path.join(target_dir, "source", item)
        
        if os.path.isdir(source_item):
            if not os.path.exists(target_item):
                shutil.copytree(source_item, target_item)
                print(f"    [DIR] {item}/")
        else:
            shutil.copy2(source_item, target_item)
            print(f"    [FILE] {item}")
    
    # Copy preview image
    preview_path = None
    if config["preview"]:
        source_preview = os.path.join(source_dir, config["preview"])
        if os.path.exists(source_preview):
            # Copy to template_images
            preview_target_dir = os.path.join(template_images_dir, "resumes")
            os.makedirs(preview_target_dir, exist_ok=True)
            
            preview_name = f"{template_id}-preview{os.path.splitext(config['preview'])[1]}"
            preview_target = os.path.join(preview_target_dir, preview_name)
            
            shutil.copy2(source_preview, preview_target)
            preview_path = f"template_images/resumes/{preview_name}"
            print(f"  Preview: {preview_path}")
        else:
            print(f"  [WARN] Preview not found: {config['preview']}")
    
    # Copy fonts if included in template
    if config["fonts"]:
        print(f"  Checking fonts...")
        # Look for font directories in source
        for font_dir_name in ["fonts", "assets/fonts", "src/fonts"]:
            font_source = os.path.join(source_dir, font_dir_name)
            if os.path.exists(font_source):
                font_target = os.path.join(target_dir, "fonts")
                for font_file in os.listdir(font_source):
                    if font_file.endswith(('.ttf', '.otf')):
                        shutil.copy2(
                            os.path.join(font_source, font_file),
                            os.path.join(font_target, font_file)
                        )
                        print(f"    [FONT] {font_file}")
    
    organized.append({
        "id": template_id,
        "config": config,
        "target_dir": target_dir,
        "preview_path": preview_path
    })
    
    print(f"  [OK] Organized: {target_dir}")

# Save organization manifest
manifest = {
    "organized_templates": organized,
    "template_configs": template_configs
}

manifest_path = os.path.join(base_dir, "_organization_manifest.json")
with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print(f"\n{'='*70}")
print(f"Organization complete!")
print(f"Manifest saved to: {manifest_path}")
print(f"{'='*70}")

print(f"\nNext steps:")
print(f"1. Run: python build_template_assets.py")
print(f"2. Run: python update_registry.py")
