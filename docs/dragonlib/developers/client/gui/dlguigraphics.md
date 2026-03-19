---
categories:
  - DragonLib
---

# `DLGuiGraphics`
Recent game versions introduced the `GuiGraphics` object as a rendering parameter. DragonLib adopts the same idea.

`DLGuiGraphics` wraps the vanilla `GuiGraphics` and also provides direct access to the `PoseStack`, the default font, and other data. The advantage is stability: if parameters change between versions, `DLGuiGraphics` can remain stable and prevent many render methods from breaking.

## Usage
`DLGuiGraphics` is used in all DragonLib GUI render methods to provide a consistent API across the library. If you need the vanilla object, call `graphics()` to get the wrapped `GuiGraphics`. Conversely, you can create a `DLGuiGraphics` from a vanilla `GuiGraphics` to use DragonLib features externally.