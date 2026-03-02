import posixpath
import json

def define_env(env):

    @env.macro
    def crafting_recipe(id: str, header = True, footer = True):
        if not id:
            return "<div class=\"admonition warning\"><p class=\"admonition-title\">No id specified!</p></div>"
        
        item = get_item_path(id)

        if not item:
            return "<div class=\"admonition warning\"><p class=\"admonition-title\">No item found!</p></div>"

        json_data = read_json(f"docs/assets/items/{item}.json")
        if not json_data:
            return f"<div class=\"admonition warning\"><p class=\"admonition-title\">Couldn't find <code>{item}.json</code> in <code>assets/items/</code>!</p></div>"

        crafting = json_data["crafting"]
        if not crafting:
            return "<div class=\"admonition warning\"><p class=\"admonition-title\">No crafting recipe found!</p></div>"
        
        if not crafting.get("ingredients"):
            return '<div class="admonition warning"><p class="admonition-title">No ingredients specified!</p></div>'
        
        ingredients = crafting["ingredients"]

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
        if not id:
            return '<div class="admonition warning"><p class="admonition-title">No id specified!</p></div>'
        
        result = get_item_path(id)

        if not result:
            return '<div class="admonition warning"><p class="admonition-title">No result item found!</p></div>'
        
        json_data = read_json(f"docs/assets/items/{result}.json")
        if not json_data:
            return f'<div class="admonition warning"><p class="admonition-title">Couldn\'t find <code>{result}.json</code> in <code>assets/items/</code>!</p></div>'
        
        smithing = json_data["smithing"]
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

    def get_item_path(item: str):
        if not item:
            return None
            
        if ":" in item:
            return item.replace(":", "/")
        else:
            return f"minecraft/{item}"
    
    def read_json(file_path: str):
        path = posixpath.sep.join([env.project_dir, file_path])

        try:
            with open(path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return None