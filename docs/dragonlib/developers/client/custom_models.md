---
categories:
  - DragonLib
---

# Custom Models

DragonLib offers some simple tools for working with 3D models and represents models as editable, renderable meshes that can be programmatically manipulated before being turned into the final rendering primitives used by Minecraft (BakedQuads). This approach enables dynamic model generation, mesh combination, texture swapping, and runtime transformations.

You can split this system across two layers:

- The mesh layer: classes such as `Mesh`, `CubeMesh`, and `BasicMesh` describe geometry and operations on geometry (merging, transforming, splitting faces, etc.).
- The model layer: `DLModel` sits above meshes and provides rendering orchestration, caching, and integration with Minecraft's `BakedModel`/render pipeline.

Together they allow you to build dynamic visuals while minimizing repeated work via caching and careful organization of baked quads.

---

## Core Concepts

- `Vertex` — a 3D point with optional attributes (e.g. normal, UV) used by `Face` corners.
- `Edge` — connection between two vertices.
- `Face` — a polygon (usually quad) composed of vertices and edges; can produce `BakedQuad` instances for rendering.
- `Mesh` — an abstract container of vertices, edges, and faces with utilities to transform and clean geometry.
- `DLModel` — high-level model that turns a `Mesh` into baked quads grouped by render type and cullface, with caching and rendering logic.

---

## `Mesh` (abstract)

A mesh represents a "raw" geometric model as lists of `Vertex`, `Edge`, and `Face` objects. It provides common operations for cleaning up redundant geometry, merging overlapping elements, and rendering faces via `DLGraphics`. It is used if you need to build or modify geometry procedurally before baking into quads or if you plan to combine multiple models and want an intermediate editable representation.

## `BasicMesh`
The base implementation of `Mesh`. It has some additional features and methods to create meshes from existing Minecraft `BakedModel` data. This class helps adapt vanilla or custom `BakedModel` quads into a single `Mesh` representation suitable for manipulation and combination. This is useful when you want to programmatically modify existing block/item models at runtime. 

## `CubeMesh`
A small specialized `Mesh` representing an axis-aligned cube built from six `Face` instances (one per `Direction`). It is useful to quickly produce box-shaped meshes (e.g., block parts, simplified hitboxes, block element prototypes) without the need to build your own by adding all faces manually.

---

## `DLModel`
This is a high-level model abstraction that turns `Mesh` instances into renderable `BakedQuad` collections, groups quads by `RenderType` and cullface, and caches the results for efficient reuse. It provides an abstract `getMesh()` method to generate a `Mesh` for the given inputs.

```java
Mesh getMesh(ModelType type, BakedModel originalModel, BlockState state, RandomSource random, ModelContext context);
```

This allows you to even use block entity data to dynamically adapt the model, eliminating the need to first create a model for every possible combination of properties in the assets.
The model data is then cached for better performance. Caching is keyed by `ModelCacheKey` (created via `createCacheKey`). For block models this key typically includes block state and model context; for items the key may be simpler.

A `DLModel` is the finished model that can be registered as a custom model for blocks and items via `DLBlockModelRegistry`.

## Register custom models
To register a custom `DLModel` for use with a block or item, the `DLBlockModelRegistry` class is used.
The `register*` methods can then be used to specify for which blocks, BlockStates, and items the models should be registered.

```java
DLBlockModelRegistry.registerForBlock(
    EXAMPLE_BLOCK,      // The block for which the model should be registered
    MyFancyModel::new,  // The DLModel instance which is used as the block model
    MyFancyModel::new   // The DLModel instance which is used as the item model
);
```

The models loaded from Minecraft's assets are then replaced by `DLModel`. However, the `DLModel` implementation allows you to use the original model to, for example, swap only the texture or make other changes to the original without having to completely recreate it manually.

## Example `DLModel` class

```java
/**
 * Minimal example showing how to extend DLModel.
 * - obtains a BasicMesh from the original model
 * - swaps a texture (example)
 * - runs mesh.cleanUp()
 */
public class MyFancyModel extends DLModel {

    private final ResourceLocation exampleSwapFrom = new ResourceLocation("minecraft:block/stone");
    private final ResourceLocation exampleSwapTo = new ResourceLocation("minecraft:block/diamond_block");


    // This method is where all the magic happens: Here, the mesh is created,
    // processed, and returned. DragonLib then takes care of the rest. It's also
    // possible to use the old model via `originalModel` (as in this example).
    // Furthermore, it's perfectly safe to calculate everything within this method,
    // since the code is only called once if there's no existing model for the
    // given `BlockState` and model data, as the model is then cached. The caching
    // rules can be modified in other methods (see below).
    @Override
    protected Mesh getMesh(ModelType type, BakedModel originalModel, BlockState state, RandomSource random, ModelContext context) {
        // Create a BasicMesh from the original baked model
        BasicMesh mesh = BasicMesh.fromBakedModel(state, originalModel, random);

        // Example modification: swap any faces that use `exampleSwapFrom` to `exampleSwapTo`.
        try {
            mesh.swapTextures(exampleSwapFrom, exampleSwapTo);
        } catch (Exception e) {
            // swapping textures can throw if atlas/sprite not available in some environments;
            // handle as needed for your mod (log, fallback, etc.)
        }

        // Optionally apply a simple transform (scale down slightly)
        mesh.scale(0.95f, mesh.getTransformableElements().get(0).getTransformOrigin());

        // Cleanup merges duplicate vertices/edges/faces
        mesh.cleanUp();

        return mesh;
    }

    @Override
    protected ModelCacheKey createCacheKey(BlockState state, RandomSource random, ModelContext contex) {
        // Use the default behavior (ModelContext + state). If your model depends on extra data,
        // include it in the cache key here.
        return super.createCacheKey(state, random, contex);
    }

    @Override
    protected boolean invalidateCacheFor(ModelType type, BlockState state, RandomSource random, ModelContext context) {
        // Return true if external data changed and cache should be invalidated. Default:
        return false;
    }
}
```