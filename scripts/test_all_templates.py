import os
import subprocess
import json

base_dir = r"c:/Users/bbog2/Downloads/AWESOME_CV"
typst_bin = os.path.join(base_dir, "typst.exe")

def test_compile():
    registry_path = os.path.join(base_dir, "templates_registry.json")
    with open(registry_path, 'r', encoding='utf-8') as f:
        registry = json.load(f)
        
    all_passed = True
    failed = []
    print("Starting Compilation Tests...")
    log_path = os.path.join(base_dir, "output", "test_errors.log")
    with open(log_path, 'w', encoding='utf-8') as log_file:
        log_file.write("Compilation Error Log\n====================\n\n")
    
    # Test Resumes and Cover Letters
    all_items = registry.get('templates', []) + registry.get('coverLetterTemplates', [])
    for t in all_items:
        name = t['name']
        print(f"\nTesting: {name}")
        
        template_file = os.path.join(base_dir, t['paths']['templateFile'])
        out_pdf = os.path.join(base_dir, "output", f"test_{t['id']}.pdf")
        
        # Ensure output dir exists
        os.makedirs(os.path.dirname(out_pdf), exist_ok=True)
        
        font_paths = []
        if 'fonts' in t['paths']:
            font_dir = os.path.join(base_dir, t['paths']['fonts'])
            if os.path.exists(font_dir):
                font_paths = ["--font-path", font_dir]
                
        cmd = [typst_bin, "compile", "--root", base_dir] + font_paths + [template_file, out_pdf]
        
        try:
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            print(f"[SUCCESS]: {name}")
        except subprocess.CalledProcessError as e:
            print(f"[FAILED]: {name}")
            with open(log_path, 'a', encoding='utf-8') as log_file:
                log_file.write(f"\n--- FAILED: {name} ---\n{e.stderr}\n")
            all_passed = False
            failed.append(name)
            
    print("\n" + "="*50)
    if all_passed:
        print("ALL TEMPLATES COMPILED SUCCESSFULLY!")
    else:
        print(f"{len(failed)} TEMPLATE(S) FAILED: {', '.join(failed)}")
        print(f"Check {log_path} for detailed error messages.")
        
if __name__ == "__main__":
    test_compile()
