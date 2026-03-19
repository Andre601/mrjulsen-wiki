---
categories:
  - DragonLib
---

# Block Entity Renderers

DragonLib provides enhanced Block Entity Renderer (BER) classes that extend Minecraft's `BlockEntityRenderer` with sensible defaults and safety checks.

## Basic Implementations

Prefer extending `SafeBlockEntityRenderer` instead of implementing `BlockEntityRenderer` directly. `SafeBlockEntityRenderer` performs important validity checks and integrates with the DragonLib rendering system.

Use `renderSafe` to render:

```java
void renderSafe(BERGraphics<T> graphics, float partialTick)
```

Common implementations:

- `BasicBlockEntityRenderer`: A simple base with recommended defaults (for example, scaling so an integer maps to block pixels).
- `RotatableBlockEntityRenderer`: Accounts for block rotation so the renderer's "front" matches the block's front.

Register a BER via Architectury API:

```java
BlockEntityRendererRegistry.register(EXAMPLE_BLOCK_ENTITY, ExampleBlockEntityRenderer::new);
```

## Instance-based renderers

Normally a block entity type uses a single shared renderer instance. That prevents storing per-block-entity data in the renderer.

Instance-based renderers solve this by giving each block entity its own renderer instance.

The BER instances implement `IBlockEntityRendererInstance`, which provides `render`, `tick` and `update` methods. A common base class is `AbstractBlockEntityRenderInstance`, which also offers a `preinit` method.

### Usage
Start by creating a renderer class that implements `IBlockEntityRendererInstance` or extends `AbstractBlockEntityRenderInstance`.

Make the Block Entity implement `IBERInstance` to provide its renderer instance:

```java
@Override
public IBlockEntityRendererInstance<ExampleBlockEntity> getRenderer() {
    return renderer;
}
```

!!! warning
    - Ensure the renderer is used only on the client side to avoid crashes.
    - Do not create a new renderer inside `getRenderer()` on each call — that method is called frequently and allocating there causes severe    performance issues. Use a cache instead:
    ```java
    final Cache<IBlockEntityRendererInstance<ExampleBlockEntity>> renderer =
        new Cache<>(() -> new ExampleBlockEntityRendererInstance(this), ECachingPriority.ALWAYS);
    ```

### Registration
Register a static renderer that delegates to the instance stored in the block entity:

```java
BlockEntityRendererRegistry.register(EXAMPLE_BLOCK_ENTITY, StaticBlockEntityRenderer::new);
```

`StaticBlockEntityRenderer` extends `RotatableBlockEntityRenderer` and supports the same features.