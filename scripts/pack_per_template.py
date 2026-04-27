"""
Pack per-template flat zips for the AeroCV GPT agent.

Output (into agent_output/):
  - metadata.md         (plain text, GPT reads natively)
  - previews.zip        (just preview PNGs)
  - modern-cv.zip       (flat, self-contained template)
  - vantage.zip         (flat, self-contained template)
  - designer-cv.zip     ...
  - executive-cv.zip
  - portfolio-cv.zip
  - typst-cv.zip
  - vercanard.zip
"""

import os
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = ROOT / "templates"
PACKAGES_DIR = ROOT / "packages"
PREVIEW_DIR = ROOT / "template_images" / "resumes"
OUTPUT_DIR = ROOT / "agent_output"

# Template definitions: id -> {source files to include, main_file rename}
TEMPLATES = {
    "modern-cv": {
        "source_dir": TEMPLATES_DIR / "modern-cv" / "source",
        "files": ["lib.typ", "lang.toml", "typst.toml"],
        "main_file": "lib.typ",  # already named lib.typ
    },
    "vantage": {
        "source_dir": TEMPLATES_DIR / "vantage" / "source",
        "files": ["vantage-typst.typ", "example.typ", "configuration.yaml"],
        "dirs": ["icons"],
        "main_file": "vantage-typst.typ",  # rename to lib.typ
    },
    "designer-cv": {
        "source_dir": TEMPLATES_DIR / "designer-cv" / "source",
        "files": ["designer-cv.typ", "lib.typ"],
        "main_file": "designer-cv.typ",  # this IS the show rule, lib.typ has helpers
    },
    "executive-cv": {
        "source_dir": TEMPLATES_DIR / "executive-cv" / "source",
        "files": ["executive-cv.typ", "lib.typ"],
        "main_file": "executive-cv.typ",
    },
    "portfolio-cv": {
        "source_dir": TEMPLATES_DIR / "portfolio-cv" / "source",
        "files": ["portfolio-cv.typ", "lib.typ"],
        "main_file": "portfolio-cv.typ",
    },
    "typst-cv": {
        "source_dir": TEMPLATES_DIR / "typst-cv" / "source",
        "files": ["template.typ", "cv_params.toml", "example.typ"],
        "main_file": "template.typ",
    },
    "brilliant-cv": {
        "source_dir": TEMPLATES_DIR / "brilliant-cv" / "source" / "src",
        "files": ["cv.typ", "letter.typ", "lib.typ", "../template/metadata_clean.toml"],
        "dirs": ["utils"],
        "main_file": "lib.typ",
    },
    "vercanard": {
        "source_dir": TEMPLATES_DIR / "vercanard" / "source",
        "files": ["template.typ", "typst.toml"],
        "dirs_flat": {"template": ["main.typ"]},  # flatten template/main.typ -> main.typ
        "main_file": None,  # complex: template.typ imports template/main.typ
    },
}

# Template metadata for metadata.md
TEMPLATE_META = {
    "modern-cv":    ("Classic & Header-centric", "Traditional corporate, Academic, Legal. Basic lists with a large top header."),
    "vantage":      ("High-Impact Tech & Skills", "Backend/Frontend Engineers, SRE, DevOps, Data Science. High IT/Tech focus with side-by-side layout and skill bars."),
    "designer-cv":  ("Creative & Vibrant color", "UI/UX Designers, Frontend Devs, Marketers. Visually striking with an accent sidebar."),
    "executive-cv": ("Formal Leadership",        "C-Level, Management, Consulting, Finance. Very clean, conservative, structured."),
    "portfolio-cv": ("Developer Portfolio",      "Fullstack Engineers, Open-Source Contributors. Prominently highlights GitHub projects and tech stacks."),
    "typst-cv":     ("Academic & Minimalist",    "Researchers, PhDs, Scientists. Extremely sparse styling focused purely on content and publications."),
    "vercanard":    ("Modern Asymmetric Sidebar", "Product Managers, Startup Roles. Stylish left-aligned contact/skills sidebar with rich main content area."),
    "brilliant-cv": ("Modern & Multilingual",    "Universal, clean design with excellent typography. Highly adaptable for Software Engineers, Managers, and general professional use."),
}


def add_dir_to_zip(zf: zipfile.ZipFile, dir_path: Path, arc_prefix: str = ""):
    """Recursively add a directory to a zip file."""
    for item in sorted(dir_path.rglob("*")):
        if item.is_file():
            arc_name = arc_prefix + str(item.relative_to(dir_path))
            zf.write(item, arc_name)


def pack_template(template_id: str, config: dict):
    """Pack a single template into a flat zip."""
    out_path = OUTPUT_DIR / f"{template_id}.zip"
    src = config["source_dir"]
    fonts_dir = TEMPLATES_DIR / template_id / "fonts"

    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        # Add template source files
        for fname in config.get("files", []):
            fpath = src / fname
            if fpath.exists():
                zf.write(fpath, fpath.name)
            else:
                print(f"  WARNING: {fpath} not found, skipping")

        # Add subdirectories (keep structure)
        for dname in config.get("dirs", []):
            dpath = src / dname
            if dpath.exists():
                add_dir_to_zip(zf, dpath, f"{dname}/")

        # Add flattened subdirectories
        for dname, files in config.get("dirs_flat", {}).items():
            for fname in files:
                fpath = src / dname / fname
                if fpath.exists():
                    zf.write(fpath, fname)

        # Add template-specific fonts
        if fonts_dir.exists():
            add_dir_to_zip(zf, fonts_dir, "fonts/")

        # Add shared packages (fontawesome, linguify)
        if PACKAGES_DIR.exists():
            add_dir_to_zip(zf, PACKAGES_DIR, "packages/")

    size_mb = out_path.stat().st_size / (1024 * 1024)
    print(f"  Packed {template_id}.zip ({size_mb:.1f} MB)")


def pack_previews():
    """Pack only preview images for the supported templates into previews.zip."""
    out_path = OUTPUT_DIR / "previews.zip"
    supported_names = {f"{k}-preview.png" for k in TEMPLATES.keys()}
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        if PREVIEW_DIR.exists():
            for img in sorted(PREVIEW_DIR.glob("*.png")):
                if img.name in supported_names:
                    zf.write(img, img.name)
                    print(f"  Added preview: {img.name}")
    size_kb = out_path.stat().st_size / 1024
    print(f"  Packed previews.zip ({size_kb:.0f} KB)")


def generate_metadata():
    """Generate metadata.md for GPT to read natively."""
    out_path = OUTPUT_DIR / "metadata.md"
    lines = [
        "# AeroCV Template Catalog",
        "",
        "| ID | Style | Best For |",
        "|---|---|---|",
    ]
    for tid, (style, best_for) in TEMPLATE_META.items():
        lines.append(f"| `{tid}` | {style} | {best_for} |")

    lines += [
        "",
        "## Import Syntax Per Template",
        "",
        "Each template zip is flat. After extraction, use these imports in your `.typ` file:",
        "",
    ]
    import_map = {
        "modern-cv":    '#import "lib.typ": *',
        "vantage":      '#import "vantage-typst.typ": *',
        "designer-cv":  '#import "designer-cv.typ": *',
        "executive-cv": '#import "executive-cv.typ": *',
        "portfolio-cv": '#import "portfolio-cv.typ": *',
        "typst-cv":     '#import "template.typ": conf, date, show_skills',
        "vercanard":    '#import "template/main.typ": *',
    }
    for tid, imp in import_map.items():
        lines.append(f"- **{tid}**: `{imp}`")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"  Generated metadata.md")


def main():
    # Clean and create output dir
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    print("=== Packing per-template zips ===")
    for tid, config in TEMPLATES.items():
        pack_template(tid, config)

    print("\n=== Packing previews ===")
    pack_previews()

    print("\n=== Generating metadata ===")
    generate_metadata()

    print(f"\nAll files written to {OUTPUT_DIR}/")
    print(f"   Total files: {len(list(OUTPUT_DIR.iterdir()))}")


if __name__ == "__main__":
    main()
