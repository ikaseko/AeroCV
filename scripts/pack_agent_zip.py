import os
import zipfile

def pack_agent_data():
    base_dir = r"c:/Users/bbog2/Downloads/AWESOME_CV"
    out_zip_path = os.path.join(base_dir, "AeroCV_Agent_Data.zip")
    
    # Files and directories to include in the master zip
    includes = [
        "quick_reference.json",
        "templates_registry.json",
        "SYSTEM_PROMPT_TYPST.md",
        "typst", # Linux binary for GPT
    ]
    
    # Directories to walk and include entirely
    dirs_to_include = [
        "templates",
        "cover_letters",
        "docs",
        "template_images" # Critical: GPT agent needs to render these visuals to the user
    ]
    
    print(f"Packaging agent data to {out_zip_path}...")
    
    with zipfile.ZipFile(out_zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Add explicit include files
        for item in includes:
            full_path = os.path.join(base_dir, item)
            if os.path.exists(full_path):
                print(f"Adding {item}")
                zf.write(full_path, item)
            else:
                print(f"Warning: Could not find {item}")
                
        # Add directories
        for d in dirs_to_include:
            dir_path = os.path.join(base_dir, d)
            if not os.path.exists(dir_path):
                continue
                
            for root, _, files in os.walk(dir_path):
                for file in files:
                    # Skip zip assets in source folders since we generate fresh ones now
                    if file.endswith('.zip'):
                        continue
                        
                    # Let PNGs pass through, especially for template_images/
                    full_file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_file_path, base_dir)
                    zf.write(full_file_path, rel_path)
                    
    print(f"\nSuccess! Agent data packaged to: {out_zip_path}")
    print(f"File size: {os.path.getsize(out_zip_path) / (1024*1024):.2f} MB")

if __name__ == "__main__":
    pack_agent_data()
