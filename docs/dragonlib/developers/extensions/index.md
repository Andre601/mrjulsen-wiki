---
categories:
  - DragonLib
---

# Extensions

DragonLib provides a few extensions for Block Entities and Items via the interfaces `IBlockEntityExtension` and `IItemExtension`.

These interfaces are implemented on vanilla classes, so you can safely cast to them to access the additional methods. To override behavior, simply implement the interfaces on your own classes.

Example:

```java
public class MyItem extends Item implements IItemExtension {
    // ...
}
```