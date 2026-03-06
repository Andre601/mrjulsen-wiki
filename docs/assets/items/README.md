# Items Data folder

This folder contains various JSON files representing individual items.  
The purpose for them is to be used in Macros to render things such as crafting or smelting recipes.

## Structure

Item Files use their item ID as file name while being stored in a folder matching their namespace.  
As an example, the Traffic Light of TrafficCraft is stored as [`trafficcraft/traffic_light.json`](trafficcraft/traffic_light.json).

Here is an example of a JSON files possible structure:
```json
{
    "name": "<string>",
    "lore": "<string>",
    "gif": <boolean>,
    "crafting": {
        "ingredients": {
            "<slot>": "<item>"
        },
        "amount": <integer>,
        "shapeless": <boolean>
    },
    "smelting": {
        "input": "<item>",
        "experience": <float>
    },
    "smithing": {
        "template": "<item>",
        "item": "<item>",
        "material": "<item>"
    }
}
```

(Note: A `?` suffix indicates the option to be optional.)

- `name`: The Item Name to display. Supports [formatting options](#formatting).
- `lore`?: Item Description to display. Supports [formatting options](#formatting).
- `gif`?: Whether the image to display is a Gif or not. Default: false.
- `crafting`:
    - `ingredients`: Contains the individual ingredients used in the Recipe. Each entry uses the slot number (1-9) as key and the [Item ID](#item-ids) as value.
    - `amount`?: Amount of items this crafting recipe gives. Default: 1
    - `shapeless`?: Whether the recipe is shapeless (Order of items doesn't matter). Default: false.
- `smelting`:
    - `input`: The [Item ID](#item-ids) of the Item that gets smelted.
    - `experience`: Number of XP points a player gets per smelted item. This can be a float number and contain decimal points.
- `smithing`:
    - `template`: The [Item ID](#item-ids) of the Item used as the template ingredient.
    - `item`: The [Item ID](#item-ids) of the Item used to apply the template and material on.
    - `material`: The [Item ID](#item-ids) of the Item used as the material to apply on the item.

### Item IDs

When referencing an item as an ingredient or input can either just the item name (i.e. `stick`) be used, or a namespaced ID (i.e. `minecraft:stick`) be used for it.  
The name/ID should match the file name of the actual item while the namespace should match the name of the folder it's located in.  
Not providing a Namespace assumes the `minecraft` namespace is used.

### Formatting

The `name` and `lore` options allow the usage of formatting tags.  
These tags are inspired by the [MiniMessage formatting](https://docs.papermc.io/adventure/minimessage/format/) and use the same naming.  
`\n` may also be used to indicate a line break to apply.
