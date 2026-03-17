---
categories:
  - DragonLib
---

# Texture Sheets

Texture sheets are often used to collect many icons into a single texture. They are commonly used in GUIs where multiple components are composed dynamically. This normally requires UV coordinates hard-coded in the source.

To give resource packs more flexibility, DragonLib introduces a new section in `texture.png.mcmeta` files where sprites can be defined outside the code.

## Creating the files
Assume you have a texture named `sprite_sheet.png` in your assets. Add a mcmeta file next to it:

```
sprite_sheet.png
sprite_sheet.png.mcmeta
```

In the mcmeta add a `dragonlib-gui` section:

```json
{
  "dragonlib-gui": {
    "texture_size": [256, 256],   // Texture size in pixels
    "sprites": {
      // Sprite definitions with UVs and other properties
    }
  }
}
```

## Defining sprites
Instead of hard-coding UVs, list sprites in this file. Resource packs can override it. Different sprite types determine rendering and available properties.

Example:
```json
"custom_icon": {
  "type": "stretched",      // Rendering type
  "uv": [20, 5],            // UV start coordinates
  "size": [5, 5]            // Size on the texture sheet
}
```

### stretched
The sprite is rendered stretched into the target area and may be distorted if sizes don't match.

Properties:

- `uv` (int[2]) — x, y start coordinates on the sheet.
- `size` (int[2]) — width, height on the sheet.

Example:
```json
"icon": {
  "type": "stretched",
  "uv": [64, 128],
  "size": [16, 16]
}
```

### tiled
The sprite is rendered at its original size and repeated or clipped to fill the target area. No distortion occurs.

Properties:

- `uv` (int[2])
- `size` (int[2])

Example:
```json
"dirt_background": {
  "type": "tiled",
  "uv": [0, 0],
  "size": [16, 16]
}
```

### nine_slice
A nine-slice sprite consists of 9 parts: corners, edges and center. This allows scalable framed sprites (e.g., buttons). The parts are arranged in a 3×3 grid.

Properties:

- `uv` (int[2]) — x, y start coordinates.
- `size` (int[2]) — width, height on the sheet.
- `border` (int[4]) — left, top, right, bottom border sizes in pixels.
- `tiledContent` (boolean) — if true, center is tiled; if false, center is stretched.
- `tiledBorder` (boolean) — if true, borders are tiled; if false, borders are stretched.

Example:
```json
"button_selected": {
  "type": "nine_slice",
  "uv": [10, 5],
  "size": [5, 5],
  "border": [2, 2, 2, 2],
  "tiledContent": true,
  "tiledBorder": false
}
```

Example (full file):
```json
{
  "dragonlib-gui": {
    "texture_size": [256, 256],
    "sprites": {
      "button_gray_disabled": {
        "type": "nine_slice",
        "uv": [20, 5],
        "size": [5, 5],
        "border": [2, 2, 2, 2]
      },
      "button_gray_normal": {
        "type": "nine_slice",
        "uv": [0, 5],
        "size": [5, 5],
        "border": [2, 2, 2, 2]
      },
      "button_gray_selected": {
        "type": "nine_slice",
        "uv": [5, 5],
        "size": [5, 5],
        "border": [2, 2, 2, 2]
      },
      "button_gray_down_selected": {
        "type": "nine_slice",
        "uv": [10, 5],
        "size": [5, 5],
        "border": [2, 2, 2, 2]
      },
      "button_gray_down": {
        "type": "nine_slice",
        "uv": [15, 5],
        "size": [5, 5],
        "border": [2, 2, 2, 2]
      }
    }
  }
}
```

## Usage
Create a `DLTextureSheet` with the texture resource location:

```java
DLTextureSheet sheet = new DLTextureSheet(new ResourceLocation("examplemod", "textures/gui/texture_sheet.png"));
```

Load a sprite by name:

```java
AbstractSprite sprite = sheet.getSprite("my_sprite");
```

`AbstractSprite` provides common properties. Specific types (e.g., `StretchedSprite`) inherit from it. The variants are inner classes of `DLTextureSheetData`.

Render a sprite:

```java
sprite.render(graphics, 0, 0, 16, 16);  // position and rendered size
```

