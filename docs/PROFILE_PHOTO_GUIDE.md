# Profile Photo Support Guide

## Overview

Several templates support profile photo insertion. This guide explains how to handle user photos in AeroCV.

---

## Template Support Matrix

| Template | Photo Support | Parameter | Default | Notes |
|----------|---------------|-----------|---------|-------|
| `modern-cv` | ✅ Yes | `profile-picture` | `none` | Circular crop |
| `typst-cv` | ✅ Yes | `picture` | `""` (empty) | Rectangular |
| `brilliant-cv` | ✅ Yes | `display_profile_photo` | `true` | Circular crop, configurable radius |
| `neat-cv` | ✅ Yes | `profilePhoto` | `"images/avatar.png"` | Rectangular |
| `vantage` | ❌ No | N/A | N/A | Icons only |
| `vercanard` | ❌ No | N/A | N/A | No photo support |

---

## Usage Examples

### Modern CV

```typst
#import "lib.typ": *

#show: resume.with(
  author: (
    firstname: "John",
    lastname: "Doe",
    // ... other fields
  ),
  // Option 1: No photo (default)
  profile-picture: none,
  
  // Option 2: With photo
  profile-picture: image("profile.png"),
  
  // Option 3: Custom photo path
  profile-picture: image("/mnt/data/user_photo.png"),
)
```

**Photo Requirements:**
- Format: PNG, JPG, WEBP
- Recommended size: 200x200px (square)
- Will be cropped to circle automatically
- Positioned top-right or top-left of header

---

### Typst CV

```typst
// In cv_params.toml or directly in .typ file
picture = "profile.png"  // Path to photo
// picture = ""  // Empty = no photo
```

**Photo Requirements:**
- Format: PNG, JPG
- Recommended size: 150x150px minimum
- Rectangular display
- Positioned in header grid

---

### Brilliant CV

```typst
// In metadata.toml or template file
display_profile_photo = true      // Show/hide photo
profile_photo_radius = "50%"      // Circular crop
profile_photo_path = "avatar.png" // Path to photo
```

**In cv.typ:**
```typst
#show: cv.with(
  author: (
    firstname: "John",
    lastname: "Doe",
  ),
  // Pass photo as content
  profile-photo: image("avatar.png"),
)
```

**Photo Requirements:**
- Format: PNG with transparency recommended
- Recommended size: 300x300px
- Circular crop (configurable radius)
- Positioned left of header

---

### Neat CV

```typst
// In src/metadata.typ
#let profilePhoto = "images/avatar.png"  // Path to photo
// #let profilePhoto = ""  // Empty = no photo
```

**Photo Requirements:**
- Format: PNG, JPG
- Recommended size: 200x250px (portrait)
- Rectangular display
- Positioned left of content

---

## For GPT Agent: Handling User Photos

### Step 1: Ask User About Photo

```
Do you want to include a profile photo in your CV?
- Yes, I'll upload a photo
- No, skip the photo
```

### Step 2: If User Uploads Photo

**In Code Interpreter:**

```python
import os

# Check if user uploaded a photo
uploaded_files = os.listdir("/mnt/data")
photo_extensions = [".png", ".jpg", ".jpeg", ".webp"]

user_photo = None
for file in uploaded_files:
    if any(file.lower().endswith(ext) for ext in photo_extensions):
        # Skip template default photos
        if "avatar" not in file.lower() and "profile" not in file.lower():
            user_photo = f"/mnt/data/{file}"
            break

if user_photo:
    print(f"Found user photo: {user_photo}")
else:
    print("No user photo found, using default (no photo)")
```

### Step 3: Generate Typst Code

**With Photo:**
```typst
#import "lib.typ": *

#show: resume.with(
  author: (
    firstname: "John",
    lastname: "Doe",
    email: "john@example.com",
    // ...
  ),
  profile-picture: image("/mnt/data/user_photo.png"),
  // ...
)
```

**Without Photo:**
```typst
#import "lib.typ": *

#show: resume.with(
  author: (
    firstname: "John",
    lastname: "Doe",
    email: "john@example.com",
    // ...
  ),
  profile-picture: none,
  // ...
)
```

---

## Photo Guidelines for Users

### ✅ DO

- Use professional headshot
- Plain background (white, gray, blue)
- Business attire
- Good lighting
- Square or portrait orientation
- High resolution (minimum 200x200px)

### ❌ DON'T

- Selfies or casual photos
- Group photos
- Busy backgrounds
- Sunglasses or hats (unless religious)
- Low resolution or pixelated
- Landscape orientation (will be cropped)

---

## File Handling in GPT

### Upload Instructions for User

```
To add a profile photo to your CV:

1. Upload your photo (PNG or JPG, at least 200x200px)
2. I'll automatically detect and use it
3. The photo will be positioned according to your template choice

Supported templates with photo support:
- Modern CV (circular crop)
- Typst CV (rectangular)
- Brilliant CV (circular, configurable)
- Neat CV (rectangular, left side)
```

### Automatic Detection

```python
def detect_user_photo():
    """Detect if user uploaded a profile photo"""
    import os
    
    data_dir = "/mnt/data"
    photo_extensions = [".png", ".jpg", ".jpeg", ".webp"]
    
    # Common template photo names to skip
    template_photos = [
        "avatar.png", "profile.png", "signature.png",
        "picture.png", "photo.png"
    ]
    
    for file in os.listdir(data_dir):
        lower_file = file.lower()
        # Skip template default photos
        if any(template in lower_file for template in template_photos):
            continue
        # Check for photo extensions
        if any(lower_file.endswith(ext) for ext in photo_extensions):
            return os.path.join(data_dir, file)
    
    return None
```

---

## Template-Specific Photo Handling

### Modern CV - Circular Photo

```typst
// The template automatically crops to circle
profile-picture: image("photo.png"),
```

**Customization:**
- Position: Configured in template (default: right)
- Size: Fixed in template (1.3cm diameter)
- Border: Optional (configured in template)

### Typst CV - Grid Photo

```typst
// Photo is placed in grid layout
#grid(
  columns: (80%, 20%),
  [Text content],
  [image("photo.png", width: 100%)],
)
```

**Customization:**
- Position: Right column
- Size: 20% of width

### Brilliant CV - Circular with Radius

```typst
// Configurable circular crop
display_profile_photo = true
profile_photo_radius = "50%"  // Circle
// profile_photo_radius = "10%"  // Rounded rectangle
profile_photo_path = "photo.png"
```

**Customization:**
- Radius: 0-50% (50% = full circle)
- Position: Left of header
- Size: 3.6cm height

### Neat CV - Side Photo

```typst
// Photo on left side
#let profilePhoto = "photo.png"

// In template:
if profilePhoto != "" {
    image(profilePhoto, height: 3.6cm)
}
```

**Customization:**
- Position: Left sidebar
- Size: 3.6cm height
- Shape: Rectangular

---

## Error Handling

### Photo Not Found

```typst
// Fallback to no photo
profile-picture: none,  // or omit parameter
```

### Invalid Photo Path

```python
import os

photo_path = "/mnt/data/photo.png"
if not os.path.exists(photo_path):
    print(f"Warning: Photo not found at {photo_path}")
    # Use fallback
    typst_code = typst_code.replace(
        f'image("{photo_path}")',
        'none'
    )
```

### Photo Too Large

```python
from PIL import Image

def check_photo_size(photo_path):
    """Check if photo is reasonable size"""
    max_size_mb = 5
    file_size_mb = os.path.getsize(photo_path) / (1024 * 1024)
    
    if file_size_mb > max_size_mb:
        print(f"Warning: Photo too large ({file_size_mb:.1f}MB)")
        # Optionally resize
        return False
    return True
```

---

## Quick Reference for Agent

```
User asks about photo → Check template support
                        ↓
Template supports photo → Ask user to upload
                        ↓
User uploads photo → Detect in /mnt/data/
                        ↓
Generate Typst code with image()
                        ↓
Compile and return PDF
```

### Code Snippet for Agent

```python
# Detect photo
photo = detect_user_photo()

# Generate code
if photo and template_supports_photo[template_id]:
    if template_id == "modern-cv":
        code = f'profile-picture: image("{photo}"),'
    elif template_id == "typst-cv":
        code = f'picture = "{photo}"'
    elif template_id == "brilliant-cv":
        code = f'display_profile_photo = true\nprofile_photo_path = "{photo}"'
    elif template_id == "neat-cv":
        code = f'#let profilePhoto = "{photo}"'
else:
    # No photo or template doesn't support
    code = get_no_photo_default(template_id)
```

---

## Resources

- [Typst Image Documentation](https://typst.app/docs/reference/visualize/image/)
- [Modern CV Photo Example](../template_images/resumes/modern-cv-preview.png)
- [Brilliant CV Photo Example](../template_images/resumes/brilliant-cv-preview.png)
