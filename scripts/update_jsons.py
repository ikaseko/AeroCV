import json, os
base = r"c:/Users/bbog2/Downloads/AWESOME_CV"
q_path = os.path.join(base, "quick_reference.json")
with open(q_path, "r", encoding="utf-8") as f:
    data = json.load(f)

new_resumes = [
    {
        "id": "designer-cv",
        "name": "Designer CV",
        "bestFor": ["designers", "creatives", "high-end", "modern"],
        "assetsPath": "templates/designer-cv/assets/typst_assets.zip",
        "languages": 1,
        "hasCoverLetter": True,
        "supportsPhoto": True,
        "photoType": "circular",
        "keyFeatures": ["Visually striking", "2-column layout", "Stylized typography"]
    },
    {
        "id": "executive-cv",
        "name": "Executive CV",
        "bestFor": ["executives", "directors", "academics", "conservative"],
        "assetsPath": "templates/executive-cv/assets/typst_assets.zip",
        "languages": 1,
        "hasCoverLetter": True,
        "supportsPhoto": True,
        "photoType": "strict-right",
        "keyFeatures": ["Highly structured", "ATS optimized", "Minimalist"]
    },
    {
        "id": "portfolio-cv",
        "name": "Portfolio CV",
        "bestFor": ["developers", "artists", "engineers"],
        "assetsPath": "templates/portfolio-cv/assets/typst_assets.zip",
        "languages": 1,
        "hasCoverLetter": True,
        "supportsPhoto": True,
        "photoType": "rounded",
        "keyFeatures": ["Highlights projects", "Prominent portfolio links", "Modern header"]
    }
]

new_cls = [
    {
        "id": f"{cid.replace('-cv','')}-cover-letter",
        "name": f"{cid.replace('-cv','').capitalize()} Cover Letter",
        "matchesResume": cid,
        "assetsPath": f"cover_letters/{cid.replace('-cv','')}-cover-letter/assets/typst_assets.zip",
        "keyFeatures": [f"Matches {cid} design"]
    } for cid in ["designer-cv", "executive-cv", "portfolio-cv"]
]

data["availableTemplates"]["resumes"].extend(new_resumes)
data["availableTemplates"]["coverLetters"].extend(new_cls)

for cid in ["designer-cv", "executive-cv", "portfolio-cv"]:
    data["photoSupport"]["templates"][cid] = {"parameter": "profile-picture", "syntax": "profile-picture: image(\"path/to/photo.png\")", "display": "standard", "position": "header-right"}
    data["quickCommands"][cid] = {"experience": "#resume-entry(...)","education": "#resume-entry(...)","skills": "#resume-skill-item(...)"}

with open(q_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

t_path = os.path.join(base, "templates_registry.json")
try:
    with open(t_path, "r", encoding="utf-8") as f:
        tdata = json.load(f)
        
    for r in new_resumes:
        tdata["templates"].append({
            "id": r["id"],
            "name": r["name"],
            "type": "resume",
            "paths": {
                "assets": r["assetsPath"],
                "source": f"templates/{r['id']}/source",
                "templateFile": f"templates/{r['id']}/source/{r['id']}.typ"
            },
            "preview": { "image": f"template_images/resumes/{r['id']}-preview.png"}
        })
        
    for cl in new_cls:
        if "coverLetterTemplates" not in tdata:
            tdata["coverLetterTemplates"] = []
        tdata["coverLetterTemplates"].append({
            "id": cl["id"],
            "name": cl["name"],
            "type": "cover_letter",
            "paths": {
                "assets": cl["assetsPath"],
                "source": f"cover_letters/{cl['id']}/source",
                "templateFile": f"cover_letters/{cl['id']}/source/{cl['id']}.typ"
            },
            "preview": { "image": f"template_images/cover_letters/{cl['id']}-preview.png"}
        })

    with open(t_path, "w", encoding="utf-8") as f:
        json.dump(tdata, f, indent=2)
except Exception as e:
    print(f"Error on registry: {e}")

print("JSONs updated successfully")
