# Items Data folder

This folder contains various JSON files representing individual items.  
The purpose for them is to be used in Macros to render things such as crafting or smelting recipes.

## Structure

Item Files use their item ID as file name while being stored in a folder matching their namespace.  
As an example, the Traffic Light of TrafficCraft is stored as [`trafficcraft/traffic_light.json`](trafficcraft/traffic_light.json).

Here is an example of a JSON files possible structure:
```json
{
    "name": "<item_name>",
    "lore": "<lore>",
    "gif": <gif>,
    "crafting": {
        "ingredients": {
            "<slot>": "<ingredient>"
        },
        "amount": <amount>,
        "shapeless": <shapeless>
    },
    "smelting": {
        "input": "<input>",
        "experience": <experience>
    },
    "smithing": {
        "template": "<item>",
        "item": "<item>",
        "material": "<item>"
    }
}
```

- name: Name of the Item to display. See [Formatting](#formatting) for formatting options.
- lore: Lore of the Item to display. See [Formatting](#formatting) for formatting options.
- gif: Whether the image to display is actually a gif and not a png.
- crafting: Contains the crafting recipe for the Item.
    - ingredients: Contains the individual ingredients for the Crafting recipe.
        -   &lt;slot&gt;: Slot number the item should be displayed in. Should be between 1 and 9.  
            The value itself should be the item-id in the `namespace:id` format. Not providing a namespace assumes the `minecraft` one.
    - amount: The number of items you obtain from this recipe. Defaults to 1.
    - shapeless: Whether the order of items does not matter. Default is false.
- smelting: Contains the smelting recipe for the Item.
    - input: The Item to put in to smelt. Should be in the `namespace:id` format. Not providing a namespace assumes the `minecraft` one.
    - experience: Amount of Experience points you get per item smelted. This is a float number, so decimal points can be used.
- smithing: Contains the smithing recipe for the Item.
    - template: The template item to use. Should be in the `namespace:id` format. Not providing a namespace assumes the `minecraft` one.
    - item: The main item to apply the template and material on. Should be in the `namespace:id` format. Not providing a namespace assumes the `minecraft` one.
    - material: The Item to apply. Should be in the `namespace:id` format. Not providing a namespace assumes the `minecraft` one.

### Formatting

The `name` and `lore` options allow usage of MiniMessage-inspired formatting tags, such as `<blue>`, `<aqua>`, `<bold>`, etc.  
Additionally may `\n` be used for line breaks, which primarely would be used within lore.
