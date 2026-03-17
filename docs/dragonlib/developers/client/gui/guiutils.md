---
categories:
  - DragonLib
---

# `GuiUtils`
This is one of the most important classes for GUI rendering. This static utility provides many methods to render textures, colors, text and more.

Prefer using `GuiUtils` in DragonLib GUIs instead of calling the vanilla API directly. `GuiUtils` acts as a small abstraction layer: internally it uses vanilla functions but shields callers from API changes so updates are less likely to break many lines of code.

Additionally, `GuiUtils` offers convenient helper methods for complex tasks like rendering blocks, items and entities inside the GUI.