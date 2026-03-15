# Profile Photo Quick Reference for AI Agent

## Quick Decision Tree

```
User wants CV
    ↓
Does template support photo?
    ├─ YES → Ask: "Do you want to include a profile photo?"
    │   ├─ YES → "Please upload a PNG/JPG photo (min 200x200px)"
    │   │   ↓
    │   │   Detect photo in /mnt/data/
    │   │   ↓
    │   │   Use template-specific syntax
    │   └─ NO → Use default (no photo)
    └─ NO → Skip photo question
```

## Template Photo Support

| Template | Ask User? | Parameter | Syntax |
|----------|-----------|-----------|--------|
| modern-cv | ✅ Yes | `profile-picture` | `profile-picture: image("photo.png"),` |
| typst-cv | ✅ Yes | `picture` | `picture = "photo.png"` |
| brilliant-cv | ✅ Yes | `display_profile_photo` | `display_profile_photo = true` |
| neat-cv | ✅ Yes | `profilePhoto` | `#let profilePhoto = "photo.png"` |
| vercanard | ❌ No | N/A | N/A |
| vantage | ❌ No | N/A | N/A |

## Python Detection Code

```python
import os

def detect_user_photo():
    """Returns path to user photo or None"""
    data_dir = "/mnt/data"
    photo_ext = [".png", ".jpg", ".jpeg", ".webp"]
    skip = ["avatar.png", "profile.png", "signature.png", 
            "picture.png", "photo.png", "thumbnail.png"]
    
    for f in os.listdir(data_dir):
        if f.lower() in skip:
            continue
        if any(f.lower().endswith(e) for e in photo_ext):
            return os.path.join(data_dir, f)
    return None

# Usage
photo = detect_user_photo()
if photo:
    print(f"Using photo: {photo}")
```

## Typst Code Generation

### modern-cv
```typst
#show: resume.with(
  author: (firstname: "John", lastname: "Doe", ...),
  profile-picture: image("/mnt/data/user_photo.png"),  // <-- PHOTO
  ...
)
```

### typst-cv
```typst
picture = "/mnt/data/user_photo.png"  // <-- PHOTO
#import "template.typ"
```

### brilliant-cv
```typst
display_profile_photo = true
profile_photo_path = "/mnt/data/user_photo.png"  // <-- PHOTO
#import "cv.typ"
```

### neat-cv
```typst
#let profilePhoto = "/mnt/data/user_photo.png"  // <-- PHOTO
#import "src/template.typ"
```

## User Instructions

**When asking for photo:**
```
📸 Profile Photo

This template supports profile photos!

To add your photo:
1. Upload a PNG or JPG file (minimum 200x200px)
2. Use a professional headshot
3. Plain background recommended

The photo will be [circular/rectangular] and positioned 
at the [top-right/top-left/left-sidebar] of your CV.

Reply "yes" to include a photo, or "no" to skip.
```

**If user uploads photo:**
```
✅ Photo detected! 

I found: {filename}
Size: {filesize}KB
Format: {format}

Your CV will include this photo. Ready to proceed?
```

**If no photo:**
```
⚠️  No photo detected

Your CV will be generated without a profile photo.

To add a photo later:
1. Upload a PNG/JPG file
2. Tell me "add my photo"
3. I'll regenerate your CV
```

## Common Issues

| Issue | Solution |
|-------|----------|
| Photo too large (>5MB) | Ask user to compress or use smaller image |
| Wrong format (GIF, BMP) | Ask user to convert to PNG/JPG |
| Template doesn't support | Suggest alternative template |
| Photo not found | Check /mnt/data/ again, ask user to re-upload |
| Multiple photos | Use the most recently uploaded one |

## Example Flow

```
User: "I need a CV using modern-cv template"

Agent: "Great choice! Modern CV supports profile photos.
        Do you want to include your photo?"

User: "Yes"

Agent: "Please upload a PNG or JPG photo (min 200x200px)"

[User uploads headshot.png]

Agent: [Detects photo]
        "Found: headshot.png (245KB)
        
        Now I'll create your CV with this photo..."

[Generates Typst code with photo]
```
