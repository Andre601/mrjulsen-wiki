---
categories:
  - DragonLib
---

# TextUtils

This utility class contains helpful helper methods for working with text. Most importantly, it provides a version-independent way to create text Components.

Over time, the way to create text Components in Minecraft has changed. For example, in 1.20 you create a text component with `Component.literal("Hello World")`. To avoid changing thousands of component calls when updating Minecraft versions, DragonLib offers convenience methods in this class that wrap the vanilla APIs and provide a stable interface.