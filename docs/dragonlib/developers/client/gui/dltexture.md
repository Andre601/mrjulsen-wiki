---
categories:
  - DragonLib
---

# DLTexture
A small helper class for managing textures.

Usually you need a `ResourceLocation` to load a texture from assets and often the texture size (commonly 256x256) as well.

`DLTexture` bundles these values to avoid mixing up parameters. Some DragonLib rendering methods can work directly with `DLTexture`, which simplifies texture usage.

A `DLTexture` only stores the key information of a 2D texture. It does not render itself — use `DLSprite` or render helper methods for drawing.