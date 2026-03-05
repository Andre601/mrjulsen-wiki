import posixpath
import json

def define_env(env):

    @env.macro
    def crafting_recipe(id: str, header = True, footer = True):
        """Generates a table displaying the required materials and also a crafting table example.
        
        This function performs the following checks in order:

        - Looks for docs/assets/items/{namespace}/{item}.json with {namespace} and {item} being obtained from the id parameter.
        - Looks for a "crafting" object with a "ingredients" object
        
        Parameters:  
            id (str): ID of the item to display in the format namespace:id. Omitting namespace assumes the minecraft namespace.
            header (bool): Whether to include the <table>, <thead>, header rows and <tbody> tags in the table. (default True)
            footer (bool): Whether to include the </tbody> and </table> tags in the table. (default True)
        
        Returns:  
            String containing a Admonition warning div if something is missing, or the actual table.
        
        """
        if not id:
            return "<div class=\"admonition warning\"><p class=\"admonition-title\">No id specified!</p></div>"
        
        item = get_item_path(id)

        if not item:
            return "<div class=\"admonition warning\"><p class=\"admonition-title\">No item found!</p></div>"

        json_data = read_json(f"docs/assets/items/{item}.json")
        if not json_data:
            return f"<div class=\"admonition warning\"><p class=\"admonition-title\">Couldn't find <code>{item}.json</code> in <code>assets/items/</code>!</p></div>"

        crafting = json_data.get("crafting")
        if not crafting:
            return "<div class=\"admonition warning\"><p class=\"admonition-title\">No crafting recipe found!</p></div>"
        
        ingredients = crafting.get("ingredients")
        if not ingredients:
            return '<div class="admonition warning"><p class="admonition-title">No ingredients specified!</p></div>'

        strings = [
            '<table>',
            '<thead>',
            '<tr>',
            '<th>Ingredients</th>',
            '<th>Crafting recipe</th>',
            '</tr>',
            '</thead>',
            '<tbody>',
            '<tr>',
            '<td>'
        ] if header else [
            '<tr>',
            '<td>'
        ]
        
        unique_ingredients = {}
        ingredients_names = []

        for num in range(1, 10):
            ingredient_id = ingredients.get(f"{num}")
            if not ingredient_id or unique_ingredients.get(ingredient_id):
                continue

            item_path = get_item_path(ingredient_id)
            ingredient_data = read_json(f"docs/assets/items/{item_path}.json")

            if not ingredient_data:
                continue

            ingredients_names.append(ingredient_data["name"] if "name" in ingredient_data else ingredient_id)
            unique_ingredients[ingredient_id] = ingredient_data
        
        ingredients_names.sort()

        strings.extend([" + ".join(ingredients_names), "</td>", "<td>"])
        strings.append("<div class=\"crafting-table tooltips\">")

        for num in range(1, 10):
            ingredient_id = ingredients.get(f"{num}")
            if not ingredient_id or not unique_ingredients.get(ingredient_id):
                strings.append(f'<span class="invslot-item slot{num}"></span>')
                continue

            ingredient_data = unique_ingredients[ingredient_id]
            item_path = get_item_path(ingredient_id)


            item_slot = [
                f'<span class="invslot-item slot{num}" data-minetip-title="',
                ingredient_data["name"] if "name" in ingredient_data else ingredient_id,
                '"',
                f' data-minetip-text="{ingredient_data["lore"]}">' if "lore" in ingredient_data else ">",
                f'<img src="/assets/img/items/{item_path}.{"gif" if "gif" in ingredient_data and ingredient_data["gif"] else "png"}" class="no-glight" loading="lazy" alt="{ingredient_id}">',
                "</span>"
            ]
            strings.append(''.join(item_slot))
        
        result_slot = [
            f'<span class="invslot-item slot0" data-minetip-title="',
            json_data["name"] if "name" in json_data else id,
            '"',
            f' data-minetip-text="{json_data["lore"]}">' if "lore" in json_data else ">",
            f'<img src="/assets/img/items/{item}.png" class="no-glight" loading="lazy" alt="{id}">',
            f'<div class="quantity">{crafting["amount"]}</div>' if "amount" in crafting and crafting["amount"] > 1 else "",
            "</span>"
        ]
        strings.append(''.join(result_slot))

        strings.extend([
            "<img src=\"/assets/img/recipes/arrow.png\" class=\"arrow\" alt=\"\" draggable=\"false\">",
            "<span class=\"shapeless\" data-minetip-title=\"This recipe is shapeless\">" if "shapeless" in crafting and crafting["shapeless"] else "",
            "<img src=\"/assets/img/recipes/shapeless.png\" alt=\"\" draggable=\"false\">" if "shapeless" in crafting and crafting["shapeless"] else "",
            "</span>" if "shapeless" in crafting and crafting["shapeless"] else "",
            "</div>",
            "</td>",
            "</tr>"
        ])

        if footer:
            strings.extend(['</tbody>', '</table>'])
        
        return '\n'.join(strings)

    @env.macro
    def smithing_recipe(id: str, header = True, footer = True):
        """Generates a table displaying the required materials and also a smithing recipe display.
        
        This function performs the following checks in order:

        - Looks for docs/assets/items/{namespace}/{item}.json with {namespace} and {item} being obtained from the id parameter.
        - Looks for a "smithing" object with a "template", "item" and "material" object
        
        Parameters:  
            id (str): ID of the item to display in the format namespace:id. Omitting namespace assumes the minecraft namespace.
            header (bool): Whether to include the <table>, <thead>, header rows and <tbody> tags in the table. (default True)
            footer (bool): Whether to include the </tbody> and </table> tags in the table. (default True)
        
        Returns:  
            String containing a Admonition warning div if something is missing, or the actual table.
        
        """
        if not id:
            return '<div class="admonition warning"><p class="admonition-title">No id specified!</p></div>'
        
        result = get_item_path(id)

        if not result:
            return '<div class="admonition warning"><p class="admonition-title">No result item found!</p></div>'
        
        json_data = read_json(f"docs/assets/items/{result}.json")
        if not json_data:
            return f'<div class="admonition warning"><p class="admonition-title">Couldn\'t find <code>{result}.json</code> in <code>assets/items/</code>!</p></div>'
        
        smithing = json_data.get("smithing")
        if not smithing:
            return '<div class="admonition warning"><p class="admonition-title">No smithing recipe found!</p></div>'
        
        if not smithing.get("template"):
            return '<div class="admonition warning"><p class="admonition-title">No template specified!</p></div>'
        
        if not smithing.get("item"):
            return '<div class="admonition warning"><p class="admonition-title">No item specified!</p></div>'
        
        if not smithing.get("material"):
            return '<div class="admonition warning"><p class="admonition-title">No material specified!</p></div>'

        template_path = get_item_path(smithing["template"])
        item_path = get_item_path(smithing["item"])
        material_path = get_item_path(smithing["material"])

        template = read_json(f"docs/assets/items/{template_path}.json")
        item = read_json(f"docs/assets/items/{item_path}.json")
        material = read_json(f"docs/assets/items/{material_path}.json")

        if not template:
            return f'<div class="admonition warning"><p class="admonition-title">No template item <code>{template_path}</code> found in <code>/assets/items/</code>!</p></div>'
        
        if not item:
            return f'<div class="admonition warning"><p class="admonition-title">No template item <code>{item_path}</code> found in <code>/assets/items/</code>!</p></div>'
        
        if not material:
            return f'<div class="admonition warning"><p class="admonition-title">No template item <code>{material_path}</code> found in <code>/assets/items/</code>!</p></div>'

        strings = [
            '<table>',
            '<thead>',
            '<tr>',
            '<th>Ingredients</th>',
            '<th>Smithing recipe</th>',
            '</tr>',
            '</thead>',
            '<tbody>',
            '<tr>',
            '<td>'
        ] if header else [
            '<tr>',
            '<td>'
        ]

        strings.extend([
            ' + '.join([
                template["name"],
                item["name"],
                material["name"]
            ]),
            "</td>",
            "<td>",
            '<div class="smithing tooltips">',
            ''.join([
                f'<span class="invslot-item slot0" data-minetip-title="{json_data["name"]}"',
                f' data-minetip-text="{json_data["lore"]}">' if "lore" in json_data else ">",
                f'<img src="/assets/img/items/{result}.png" class="no-glight" loading="lazy" alt="{id}">',
                "</span>"
            ]),
            ''.join([
                f'<span class="invslot-item slot1" data-minetip-title="{template["name"]}"',
                f' data-minetip-text="{template["lore"]}">' if "lore" in template else ">",
                f'<img src="/assets/img/items/{template_path}.png" class="no-glight" loading="lazy" alt="{template_path.replace("/", ":")}">',
                "</span>"
            ]),
            ''.join([
                f'<span class="invslot-item slot2" data-minetip-title="{item["name"]}"',
                f' data-minetip-text="{item["lore"]}">' if "lore" in item else ">",
                f'<img src="/assets/img/items/{item_path}.png" class="no-glight" loading="lazy" alt="{item_path.replace("/", ":")}">',
                "</span>"
            ]),
            ''.join([
                f'<span class="invslot-item slot3" data-minetip-title="{material["name"]}"',
                f' data-minetip-text="{material["lore"]}">' if "lore" in material else ">",
                f'<img src="/assets/img/items/{material_path}.png" class="no-glight" loading="lazy" alt="{material_path.replace("/", ":")}">',
                "</span>"
            ]),
            '<img src="/assets/img/recipes/arrow.png" alt="" class="arrow" draggable="false">'
            "</div>",
            "</td>",
            "</tr>"
        ])

        if footer:
            strings.extend([
                "</tbody>",
                "</table>"
            ])
        
        return '\n'.join(strings)
    
    @env.macro
    def smelting_recipe(id: str, header = True, footer = True):
        """Generates a table displaying the required materials and also a smelting recipe display.
        
        This function performs the following checks in order:

        - Looks for docs/assets/items/{namespace}/{item}.json with {namespace} and {item} being obtained from the id parameter.
        - Looks for a "smelting" object with a "item" object
        
        Parameters:  
            id (str): ID of the item to display in the format namespace:id. Omitting namespace assumes the minecraft namespace.
            header (bool): Whether to include the <table>, <thead>, header rows and <tbody> tags in the table. (default True)
            footer (bool): Whether to include the </tbody> and </table> tags in the table. (default True)
        
        Returns:  
            String containing a Admonition warning div if something is missing, or the actual table.
        
        """
        if not id:
            return '<div class="admonition warning"><p class="admonition-title">No id specified!</p></div>'
        
        result = get_item_path(id)

        if not result:
            return '<div class="admonition warning"><p class="admonition-title">No result item found!</p></div>'
        
        json_data = read_json(f"docs/assets/items/{result}.json")
        if not json_data:
            return f'<div class="admonition warning"><p class="admonition-title">Couldn\'t find <code>{result}.json</code> in <code>assets/items/</code>!</p></div>'
        
        smelting = json_data.get("smelting")
        if not smelting:
            return '<div class="admonition warning"><p class="admonition-title">No smelting recipe found!</p></div>'
        
        item_path = get_item_path(smelting["item"])

        item = read_json(f"docs/assets/items/{item_path}.json")

        if not item:
            return f'<div class="admonition warning"><p class="admonition-title">No item <code>{template_path}</code> found in <code>/assets/items/</code>!</p></div>'

        strings = [
            '<table>',
            '<thead>',
            '<tr>',
            '<th>Ingredients</th>',
            '<th>Smelting recipe</th>',
            '</tr>',
            '</thead>',
            '<tbody>',
            '<tr>',
            '<td>'
        ] if header else [
            '<tr>',
            '<td>'
        ]

        strings.extend([
            item["name"] if "name" in item else "Unknown Item",
            "</td>",
            "<td>",
            '<div class="furnace tooltips">',
            ''.join([
                f'<span class="invslot-item slot0" data-minetip-title="{json_data["name"]}"',
                f' data-minetip-text="{json_data["lore"]}">' if "lore" in json_data else ">",
                f'<img src="/assets/img/items/{result}.png" class="no-glight" loading="lazy" alt="{id}">',
                "</span>"
            ]),
            ''.join([
                f'<span class="invslot-item slot1" data-minetip-title="{item["name"]}"',
                f' data-minetip-text="{item["lore"]}">' if "lore" in item else ">",
                f'<img src="/assets/img/items/{item_path}.png" class="no-glight" loading="lazy" alt="">',
                "</span>"
            ]),
            '<span class="invslot-item slot2"></span>'
            '<img src="/assets/img/recipes/fire.gif" alt="fire" class="fire" draggable="false">',
            '<img src="/assets/img/recipes/arrow.gif" alt="arrow" class="arrow" draggable="false">',
            f'<span class="exp">{smelting.get("exp", 0.0)} XP</span>',
            f'<span class="time">{smelting.get("time", 10)}s</span>',
            "</div>"
            "</td>",
            "</tr>"
        ])

        if footer:
            strings.extend([
                "</tbody>",
                "</table>"
            ])
        
        return '\n'.join(strings)
    
    @env.macro
    def advancement(id: str, header = True, footer = True):
        """Generates a table displaying an advancement with its icon, name, description and actual requirement (if provided).
        
        This function performs the following checks in order:

        - Looks for docs/assets/advancements/{namespace}/{item}.json with {namespace} and {item} being obtained from the id parameter.
        - Looks for a "name", "icon" and "description" object.
        
        Parameters:  
            id (str): ID of the item to display in the format namespace:id. Omitting namespace assumes the minecraft namespace.
            header (bool): Whether to include the <table>, <thead>, header rows and <tbody> tags in the table. (default True)
            footer (bool): Whether to include the </tbody> and </table> tags in the table. (default True)
        
        Returns:  
            String containing a Admonition warning div if something is missing, or the actual table.
        
        """
        if not id:
            return '<div class="admonition warning"><p class="admonition-title">No id specified!</p></div>'
        
        advancement_path = get_item_path(id)

        if not advancement_path:
            return '<div class="admonition warning"><p class="admonition-title">No advancement found!</p></div>'
        
        advancement = read_json(f"docs/assets/advancements/{advancement_path}.json")
        if not advancement:
            return f'<div class="admonition warning"><p class="admonition-title">Couldn\'t find <code>{advancement_path}</code> in <code>assets/advancements/</code>!</p></div>'
        
        background = advancement.get("type", "normal").lower()
        if background != "normal" and background != "goal" and background != "challenge":
            return f'<div class="admonition warning"><p class="admonition-title">Invalid Advancement type. Need <code>normal</code>, <code>goal</code> or <code>challenge</code> but got <code>{background}</code>!</p></div>'
        
        icon = get_item_path(advancement.get("icon"))
        if not icon:
            return f'<div class="admonition warning"><p class="admonition-title">No <code>icon</code> set!</p></div>'
        
        name = advancement.get("name")
        if not name:
            return f'<div class="admonition warning"><p class="admonition-title">No <code>name</code> set!</p></div>'
        
        description = advancement.get("description")
        if not description:
            return f'<div class="admonition warning"><p class="admonition-title">No <code>description</code> set!</p></div>'
        
        requirements = advancement.get("requirements", "")

        strings = [
            "<table>",
            "<thead>",
            "<tr>",
            "<th>Icon</th>",
            "<th>Advancement</th>",
            "<th>In-game description</th>",
            "<th>Actual requirements (if different)</th>",
            "</tr>",
            "</thead>",
            "<tbody>",
            "<tr>",
            "<td>"
        ] if header else [
            "<tr>",
            "<td>"
        ]

        strings.extend([
            '<span class="advancement-background">',
            f'<img src="/assets/img/advancements/{background}.png" class="pixelated no-glight" draggable="false">',
            '<span class="advancement-icon">',
            f'<img src="/assets/img/items/{icon}.png" class="no-glight" draggable="false">'
            "</span>",
            "</span>",
            "</td>",
            "<td>",
            name,
            "</td>",
            "<td>",
            description,
            "</td>",
            "<td>",
            requirements,
            "</td>",
            "</tr>"

        ])

        if footer:
            strings.extend([
                "</tbody>",
                "</table>"
            ])

        return '\n'.join(strings)

    def get_item_path(item: str):
        """Takes the provided item string and converts it from {namespace}:{id} to {namespace}/{id}.  
        Should no colon be present will it assume no namespace and return minecraft/{item} instead.
        
        Providing None returns None.
        
        """
        if not item:
            return None
            
        if ":" in item:
            return item.replace(":", "/")
        else:
            return f"minecraft/{item}"
    
    def read_json(file_path: str):
        """Takes the provided file_path, appends it to the project's directory and tries to load it as a JSON.

        Should the load fail due to a FileNotFoundError will None be returned.
        
        """
        path = posixpath.sep.join([env.project_dir, file_path])

        try:
            with open(path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return None