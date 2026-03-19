---
categories:
  - DragonLib
---

# DLSprite

A small class that stores a configured texture so it can be rendered easily later.

Instead of calling `GuiUtils.renderTexture(...)` with many parameters every time, create a `DLSprite` once and render it where needed:

```java
sprite.render(graphics, x, y);
```

## Creating sprites
A sprite can be created from different sources: a 2D texture via `ResourceLocation`, a texture ID (`int`), a `DLTexture`, or even items.

With parameters like texture size and UV coordinates you can create a reusable sprite configuration to render later.

## Usage
Some properties (e.g. an `icon` property) use `DLSprite` because it is easy to pass around: configure the texture once and let the component render it as needed.