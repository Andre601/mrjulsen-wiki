# Advancements folder

This folder contains various JSON files representing individual advancements.  
The purpose for them is to be used in Macros to render things such as tables with Advancement info.

## Structure

Advancement Files are store in folders that are used as the mod namespace.  
This allows to reference them in Macros using the `namespace:advancement_name` format.

Here is an example of the JSON structure of an Advancement:

```json
{
    "name": "<name>",
    "icon": "<item>",
    "type": "<type>",
    "description": "<description>",
    "requirements": "<requirements>"
}
```

- name: The name of the Advancement as shown in the Advancement Screen, Chat and Toasts.
- icon: Item to display in the advancement image. Should be in the `namespace:id` format. Not providing a namespace assumes the `minecraft` one.
- type: The Advancement type. Supported values are `normal` (default), `goal` and `challenge`. Optional.
- description: The Advancement's description, as shown in the Advancement Screen.
- requirements: The actual requirements to get this advancement. Only needed if the description isn't explaining this already.
