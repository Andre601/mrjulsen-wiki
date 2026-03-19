---
categories:
  - DragonLib
---

# OBJ Models

Minecraft Forge includes its own API for using OBJ models in mods. DragonLib ports this system to Fabric and adds an extended loader with extra features.

## Forge OBJ Model Loader on Fabric
This API is used the same way on Fabric as on Forge. Create the model JSON file and place the .obj and .mtl files in the same directory. In the JSON file use the same loader id as in Forge:

```json
{
  "loader": "forge:obj",
  // ...
}
```

This is especially useful for multi-loader projects that keep shared model assets in a common module without changing the loader id.

## Multipart OBJ Loader
DragonLib adds its own model loader to extend the OBJ loader. As the name implies, a model can be composed of several parts that are combined in the model JSON. This is useful when similar models share components: you can model parts separately and assemble them in one file.

The loader id is `dragonlib:multipart_obj`. An example model JSON looks like this:

```json
{
  "loader": "dragonlib:multipart_obj",
  "automatic_culling": true,
  "shade_quads": true,
  "flip_v": true,
  "emissive_ambient": false,
  "model": "examplemod:models/block/example_model.obj",
  "textures": {
    "particle": "minecraft:block/stone"
  },
  "add": [
    {
      "model": "examplemod:models/block/submodel1.obj",
      "rotation": [90.0, 0.0, 0.0],
      "offset": [8.0, 9.0, 11.0]
    },
    {
      "model": "examplemod:models/block/submodel2.obj",
      "rotation": [0.0, 180.0, 0.0],
      "offset": [8.0, 12.0, 5.0]
    }
  ]
}
```

### Structure
The JSON is largely the same as the Forge OBJ loader. Key additions:

- `add`: An array of models to combine with the main model.
    - `model`: Reference to the model file (relative to the namespace root, not the models folder).
    - `rotation`: Rotation for the part as [x, y, z] in degrees when combined.
    - `offset`: Translation for the part as [x, y, z] relative to the origin of the current model.