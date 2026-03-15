"""
Analyze imported templates and show their structure.
"""
import os
import json

temp_dir = r"C:\Users\bbog2\Downloads\AWESOME_CV\_temp_import"

templates = [
    "typst-cv",
    "brilliant-cv", 
    "vercanard",
    "vantage",
    "neat-cv"
]

print("=" * 70)
print("=== Template Structure Analysis ===")
print("=" * 70)

analysis = {}

for template_id in templates:
    template_dir = os.path.join(temp_dir, template_id)
    print(f"\n{'='*70}")
    print(f"TEMPLATE: {template_id}")
    print(f"{'='*70}")
    
    if not os.path.exists(template_dir):
        print(f"  [WARN] Not found!")
        continue
    
    # List all files
    print("\nFiles:")
    files = []
    for root, dirs, filenames in os.walk(template_dir):
        # Skip .git
        if '.git' in root:
            continue
        level = root.replace(template_dir, '').count(os.sep)
        indent = '  ' * level
        subindent = '  ' * (level + 1)
        
        # Show directory
        dirname = os.path.basename(root)
        if dirname and level <= 2:
            print(f"{indent}[DIR] {dirname}/")
        
        # Show files (limit depth)
        if level <= 3:
            for filename in filenames[:10]:  # Limit files shown
                if not filename.startswith('.'):
                    filepath = os.path.join(root, filename)
                    size = os.path.getsize(filepath)
                    size_str = f"{size:,} B" if size < 1000 else f"{size/1024:.1f} KB"
                    print(f"{subindent}[FILE] {filename} ({size_str})")
    
    # Find main .typ files
    print("\nMain .typ files:")
    typ_files = []
    for root, dirs, filenames in os.walk(template_dir):
        if '.git' in root:
            continue
        for filename in filenames:
            if filename.endswith('.typ'):
                filepath = os.path.join(root, filename)
                rel_path = os.path.relpath(filepath, template_dir)
                typ_files.append(rel_path)
                print(f"  - {rel_path}")
    
    # Find typst.toml
    print("\nPackage config (typst.toml):")
    toml_path = os.path.join(template_dir, "typst.toml")
    if os.path.exists(toml_path):
        print(f"  [OK] Found")
        with open(toml_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Extract name and version
            for line in content.split('\n'):
                if line.startswith('name') or line.startswith('version') or line.startswith('entrypoint'):
                    print(f"    {line.strip()}")
    else:
        print(f"  [ ] Not found (standalone template)")
    
    # Find font requirements
    print("\nFonts:")
    font_mentions = []
    for root, dirs, filenames in os.walk(template_dir):
        if '.git' in root:
            continue
        for filename in filenames:
            if filename.endswith(('.typ', '.toml', '.md', 'README')):
                filepath = os.path.join(root, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read().lower()
                        if 'roboto' in content:
                            font_mentions.append('Roboto')
                        if 'source sans' in content:
                            font_mentions.append('Source Sans')
                        if 'noto' in content:
                            font_mentions.append('Noto')
                        if 'inter' in content:
                            font_mentions.append('Inter')
                except:
                    pass
    
    font_mentions = list(set(font_mentions))
    if font_mentions:
        for font in font_mentions:
            print(f"  - {font}")
    else:
        print(f"  - System fonts (no specific requirements)")
    
    # Find package imports
    print("\nExternal packages (@preview):")
    packages = set()
    for root, dirs, filenames in os.walk(template_dir):
        if '.git' in root:
            continue
        for filename in filenames:
            if filename.endswith('.typ'):
                filepath = os.path.join(root, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        import re
                        matches = re.findall(r'#import\s+"@preview/([^"]+)"', content)
                        packages.update(matches)
                except:
                    pass
    
    if packages:
        for pkg in packages:
            print(f"  - {pkg}")
    else:
        print(f"  - None detected")
    
    # Find images
    print("\nImages:")
    images = []
    for root, dirs, filenames in os.walk(template_dir):
        if '.git' in root:
            continue
        for filename in filenames:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.svg', '.webp')):
                filepath = os.path.join(root, filename)
                rel_path = os.path.relpath(filepath, template_dir)
                images.append(rel_path)
                size = os.path.getsize(filepath)
                print(f"  - {rel_path} ({size/1024:.1f} KB)")
    
    analysis[template_id] = {
        "typ_files": typ_files,
        "packages": list(packages),
        "fonts": font_mentions,
        "images": images
    }

# Save analysis
analysis_path = os.path.join(temp_dir, "_template_analysis.json")
with open(analysis_path, 'w', encoding='utf-8') as f:
    json.dump(analysis, f, indent=2, ensure_ascii=False)

print(f"\n{'='*70}")
print(f"Analysis saved to: {analysis_path}")
print(f"{'='*70}")
