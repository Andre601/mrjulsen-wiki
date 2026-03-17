---
categories:
  - DragonLib
---

# DLColor

A compact, immutable ARGB color value type used throughout DragonLib. DLColor stores 8‑bit alpha, red, green and blue channels and offers creation helpers, conversions, transformations and compositing utilities.

## Key features

- Immutable value object representing ARGB colors.
- Factory methods for ints, normalized floats, hex strings, HSV and packed ARGB ints.
- Accessors for integer (0–255) and normalized float (0.0–1.0) channels.
- HSV/HSB conversion helpers and derived properties (hue, saturation, brightness).
- Common color transforms: lighten, darken, invert, grayscale, saturate, rotate hue, swap channels.
- Blending and compositing: blend, alphaBlend, combine, mixTint.
- Predicates and utilities: isLight, hasTransparency, distance, UNDEFINED sentinel.

!!! note
    The special `DLColor.UNDEFINED` acts as a sentinel; most instance methods throw `IllegalStateException` when invoked on it.

## Quick examples

Create colors
```java
// opaque red
DLColor red = DLColor.of(255, 0, 0);

// with alpha (50% opaque blue)
DLColor semiBlue = DLColor.of(128, 0, 0, 255);

// from hex
DLColor fromHex = DLColor.fromHex("#FF7F50");

// from normalized floats (r,g,b)
DLColor fromFloats = DLColor.of(0.5f, 0.25f, 1.0f);

// from HSV (h in degrees)
DLColor fromHsv = DLColor.fromHsv(200f, 0.8f, 0.9f);
```

Transform and combine
```java
DLColor original = DLColor.of(100, 150, 200);
DLColor lighter = original.lighten(0.3f);
DLColor darker = original.darken(0.2f);
DLColor inverted = original.invert();
DLColor gray = original.grayscale();

// blend two colors 70% toward colorB
DLColor blended = DLColor.blend(original, DLColor.BLUE, 0.7f);

// alpha composite: foreground over background
DLColor composited = DLColor.alphaBlend(semiBlue, original);
```

Conversions and inspection
```java
int argb = original.getAsARGB();        // 0xAARRGGBB
String hex = original.getAsHEX(true);   // "#AARRGGBB" or "#RRGGBB"
float[] hsb = original.getAsHSB();      // {hue, saturation, brightness}
boolean light = original.isLight(0.5f); // compare luminance to threshold
```

## Notes & best practices

- Float parameters are clamped to [0.0, 1.0], integer channels to [0, 255].
- Methods that return a new DLColor never mutate the original.
- Use DLColor.UNDEFINED for representing "no color" — guard calls or catch IllegalStateException as appropriate.
