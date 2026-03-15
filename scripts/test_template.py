import os
import shutil
import zipfile
import subprocess

base_dir = r"C:\Users\bbog2\Downloads\AWESOME_CV"
assets_zip = os.path.join(base_dir, "assets_typst.zip")
build_dir = os.path.join(base_dir, "build_typst_test")
typst_win_dir = os.path.join(base_dir, "typst-x86_64-pc-windows-msvc")

# Clean build
if os.path.exists(build_dir):
    shutil.rmtree(build_dir)
os.makedirs(build_dir, exist_ok=True)

print("=== Testing FULL OFFLINE Typst compilation ===\n")

# Extract assets
print("Extracting assets_typst.zip...")
with zipfile.ZipFile(assets_zip, 'r') as zip_ref:
    zip_ref.extractall(build_dir)
print(f"Extracted to {build_dir}")

# Use Windows typst for testing
typst_exe = os.path.join(typst_win_dir, "typst.exe")

# Compile
os.chdir(build_dir)
print(f"\nRunning: typst compile --font-path fonts resume.typ")
result = subprocess.run([typst_exe, "compile", "--font-path", "fonts", "resume.typ"], 
                       capture_output=True, text=True)

print("\n=== STDOUT ===")
print(result.stdout[-3000:] if len(result.stdout) > 3000 else result.stdout)
print("\n=== STDERR ===")
print(result.stderr[-3000:] if len(result.stderr) > 3000 else result.stderr)
print(f"\nReturn code: {result.returncode}")

# Check result
pdf_path = os.path.join(build_dir, "resume.pdf")
if os.path.exists(pdf_path):
    print(f"\n✓ SUCCESS! resume.pdf created")
    print(f"  Size: {os.path.getsize(pdf_path):,} bytes")
else:
    print(f"\n✗ FAILED! resume.pdf not created")
