import os, zipfile

base = r"c:/Users/bbog2/Downloads/AWESOME_CV"
modern_zip = os.path.join(base, 'templates/modern-cv/assets/typst_assets.zip')

def build(typ, name, entry):
    dest = os.path.join(base, typ, name, 'assets')
    os.makedirs(dest, exist_ok=True)
    out_zip = os.path.join(dest, 'typst_assets.zip')
    
    with zipfile.ZipFile(modern_zip, 'r') as zin, zipfile.ZipFile(out_zip, 'w', zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            if item.filename not in ['lib.typ', 'resume.typ', 'lang.toml', 'typst.toml', 'profile.png']:
                zout.writestr(item, zin.read(item.filename))
        
        zout.write(os.path.join(base, typ, name, 'source', 'lib.typ'), 'lib.typ')
        zout.write(os.path.join(base, typ, name, 'source', entry), 'resume.typ')
    print(f"Created {out_zip}")

build('templates', 'designer-cv', 'designer-cv.typ')
build('templates', 'executive-cv', 'executive-cv.typ')
build('templates', 'portfolio-cv', 'portfolio-cv.typ')
build('cover_letters', 'designer-cover-letter', 'designer-cover-letter.typ')
build('cover_letters', 'executive-cover-letter', 'executive-cover-letter.typ')
build('cover_letters', 'portfolio-cover-letter', 'portfolio-cover-letter.typ')

print("All asset zips created successfully!")
