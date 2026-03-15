import os
import re
import subprocess

base_dir = r"c:/Users/bbog2/Downloads/AWESOME_CV"
prompt_path = os.path.join(base_dir, "SYSTEM_PROMPT_TYPST.md")
build_dir = os.path.join(base_dir, "cv_build_test")
os.makedirs(build_dir, exist_ok=True)

with open(prompt_path, "r", encoding="utf-8") as f:
    prompt_text = f.read()

# Extract blocks
# Pattern: #### Resume Example 1: `modern-cv`\n```typst\n(.*?)\n```
pattern = r"#### Resume Example \d+: `(.*?)`\n```typst\n(.*?)\n```"
matches = re.finditer(pattern, prompt_text, re.DOTALL)

for match in matches:
    template_name = match.group(1)
    code = match.group(2)
    
    print(f"Testing {template_name}...")
    
    # Apply dummy data to avoid Typst placeholder syntax errors (if any)
    # Most placeholders are strings so they should compile, but let's fix pathing
    code = code.replace('"/mnt/data/', '"/')
    
    # Write to test file
    typst_path = os.path.join(build_dir, f"test_{template_name}.typ")
    pdf_path = os.path.join(build_dir, f"test_{template_name}.pdf")
    
    with open(typst_path, "w", encoding="utf-8") as f:
        f.write(code)
        
    proc = subprocess.run([
        os.path.join(base_dir, "typst.exe"), "compile",
        "--root", base_dir,
        typst_path,
        pdf_path
    ], capture_output=True, text=True)
    
    if proc.returncode == 0:
        print(f"  [SUCCESS] {template_name} compiled.")
    else:
        print(f"  [FAILED] {template_name}")
        print(proc.stderr)

