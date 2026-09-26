import posixpath
import json
from markupsafe import escape

def define_env(env):
    @env.macro
    def infobox(*ids: str) -> str:
        if not ids:
            return admo_warning("No IDs specified!")

        if len(ids) == 1:
            id = ids[0]

            item_path = get_item_path(id)
            if not item_path:
                return admo_warning(f"No valid Item Path found for <code>{id}</code>!")
            
            item = read_json(f"docs/assets/items/{item_path}.json")
            if not item:
                return admo_warning(f"No Item File found for <code>assets/items/{item_path}.json</code>!")
            
            strings = [
                '<div class="infobox">',
                f'<div class="title">{item["name"] if "name" in item else env.page.title}</div>'
            ]

            strings.extend(
                get_item_table(id, item, item_path)
            )

            strings.append('</div>')

            return '\n'.join(strings)
        
        entries = []

        for id in ids:
            item_path = get_item_path(id)

            if not item_path:
                return admo_warning(f"No valid Item Path found for <code>{id}</code>!")
            
            item = read_json(f"docs/assets/items/{item_path}.json")
            if not item:
                return admo_warning(f"No Item File found for <code>assets/items/{item_path}.json</code>")
            
            entries.append((id, item_path, item))
        
        strings = [
            html_block('div.infobox'),
            html_block('p.title', env.page.title, 1),
        ]

        for id, item_path, item in entries:
            strings.append(f'//// tab | {item.get("name", id)}')

            strings.extend(get_item_table(id, item, item_path))

            strings.append("////")
        
        strings.append(close_block())

        return '\n'.join(strings)

    @env.macro
    def crafting_recipe(id: str, header: bool = True, footer: bool = True) -> str:
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
            return admo_warning("No ID specified!")
        
        item = get_item_path(id)

        if not item:
            return admo_warning(f"No Item found for <code>{id}</code>!")
        
        json_data = read_json(f"docs/assets/items/{item}.json")
        if not json_data:
            return admo_warning(f"Couln't find <code>assets/items/{item}.json</code>!")

        crafting = json_data.get("crafting")
        if not crafting:
            return admo_warning(f"No crafting recipe found for <code>{id}</code>!")
        
        ingredients = crafting.get("ingredients")
        if not ingredients:
            return admo_warning(f"No Ingredients found for <code>{id}</code>!")

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
        
        create_recipe = crafting.get("create_recipe", False)
        unique_ingredients = {}
        ingredients_names = []

        for num in range(1, (13 if create_recipe else 10)):
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

        strings.extend([
            " + ".join(ingredients_names),
            "</td>",
            "<td>",
            f'<div class="crafting-table {"create" if create_recipe else ""} tooltips">'
        ])

        for num in range(1, (13 if create_recipe else 10)):
            ingredient_id = ingredients.get(f"{num}")
            if not ingredient_id or not unique_ingredients.get(ingredient_id):
                strings.append(f'<span class="invslot-item slot{num}"></span>')
                continue

            ingredient_data = unique_ingredients[ingredient_id]
            item_path = get_item_path(ingredient_id)

            item_slot = [
                f'<span class="{"animated " if isinstance(ingredient_data.get("variants"), list) else ""}invslot-item slot{num}" data-minetip-title="',
                ingredient_data.get("name", ingredient_id.replace("_", " ").title()),
                '"',
                f' data-minetip-text="{ingredient_data["lore"]}">' if "lore" in ingredient_data else ">"
            ]

            if isinstance(ingredient_data.get("variants"), list):
                for i, variant in enumerate(ingredient_data["variants"]):
                    item_slot.append(f'<img src="/assets/img/items/{get_item_path(variant)}.png" class="{"animated-active " if i == 0 else ""}no-glight" loading="eager" alt="{ingredient_id}">')
            else:
                item_slot.append(f'<img src="/assets/img/items/{item_path}.{"gif" if "gif" in ingredient_data and ingredient_data["gif"] else "png"}" class="no-glight" loading="lazy" alt="{ingredient_id}">')
            
            item_slot.append('</span>')

            strings.append(''.join(item_slot))

        result_slot = [
            f'<span class="{"animated " if isinstance(json_data.get("variants"), list) else ""}invslot-item slot0" data-minetip-title="',
            json_data["name"] if "name" in json_data else id,
            '"',
            f' data-minetip-text="{json_data["lore"]}">' if "lore" in json_data else ">"
        ]
        
        if isinstance(json_data.get("variants"), list):
            for i, variant in enumerate(json_data["variants"]):
                result_slot.append(f'<img src="/assets/img/items/{get_item_path(variant)}.png" class="{"animated-active " if i == 0 else ""}"no-glight" loading="eager" alt="{id}">')
        else:
            result_slot.append(f'<img src="/assets/img/items/{item}.{"gif" if json_data.get("gif", False) else "png"}" class="no-glight" loading="lazy" alt="{id}">')
        
        result_slot.extend([
            f'<div class="quantity">{crafting["amount"]}</div>' if "amount" in crafting and crafting["amount"] > 1 else "",
            '</span>'
        ])

        strings.append(''.join(result_slot))

        if create_recipe:
            strings.append(''.join([
                '<span class="invslot-item slot-crafter" data-minetip-title="Requires 12 Mechanical Crafters">',
                '<img src="/assets/img/items/create/mechanical_crafter.png" class="no-glight" loading="lazy" alt="" draggable="false">',
                '<div class="quantity">12</div>',
                '</span>'
            ]))

        strings.extend([
            f'<img src="/assets/img/recipes/{"create-" if create_recipe else ""}arrow.png" class="arrow" alt="" draggable="false">',
            '<span class="shapeless" data-minetip-title="This recipe is shapeless">' if "shapeless" in crafting and crafting["shapeless"] else "",
            '<img src="/assets/img/recipes/shapeless.png" class="no-glight" alt="" draggable="false">' if "shapeless" in crafting and crafting["shapeless"] else "",
            "</span>" if "shapeless" in crafting and crafting["shapeless"] else "",
            "</div>",
            "</td>",
            "</tr>"
        ])

        if footer:
            strings.extend(['</tbody>', '</table>'])
        
        return '\n'.join(strings)

    @env.macro
    def smithing_recipe(id: str, header: bool = True, footer: bool = True) -> str:
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
            return admo_warning("No ID specified!")
        
        result = get_item_path(id)

        if not result:
            return admo_warning(f"No Item found for <code>{id}</code>!")
        
        json_data = read_json(f"docs/assets/items/{result}.json")
        if not json_data:
            return admo_warning(f"Couln't find <code>assets/items/{item}.json</code>!")
        
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
    def smelting_recipe(id: str, header: bool = True, footer: bool = True) -> str:
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
            return f'<div class="admonition warning"><p class="admonition-title">No item <code>{item}</code> found in <code>/assets/items/</code>!</p></div>'

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

        ingredient = [
            f'<span class="{"animated " if isinstance(item.get("variants"), list) else ""}invslot-item slot1" data-minetip-title="{item["name"]}"',
            f' data-minetip-text="{item["lore"]}">' if "lore" in item else ">"
        ]

        if isinstance(item.get("variants"), list):
            for i, variant in enumerate(item["variants"]):
                ingredient.append(f'<img src="/assets/img/items/{get_item_path(variant)}.png" class="{"animated-active " if i == 0 else ""}no-glight" loading="eager" alt="{variant}">')
        else:
            ingredient.append(f'<img src="/assets/img/items/{item_path}.png" class="no-glight" loading="lazy" alt="{smelting["item"]}">')
        
        ingredient.append('</span>')

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
            ''.join(ingredient),
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
    def advancement(id: str, header: bool = True, footer: bool = True) -> str:
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
    
    @env.macro
    def version_history(versions: dict):
        rows = []

        for version, entries in versions.items():
            if isinstance(entries, str):
                entries = [entries]
            
            rowspan = len(entries)

            for index, entry in enumerate(entries):

                if index == 0:
                    rows.extend([
                        "<tr>",
                        f'<th rowspan="{rowspan}" class="version">{escape(version)}</th>',
                        f'<td>{escape(entry)}</td>',
                        "</tr>"
                    ])
                else:
                    rows.extend([
                        "<tr>",
                        f'<td>{escape(entry)}</td>',
                        "</tr>"
                    ])
        
        return "\n".join([
            '<table class="version-history">',
            "<thead>",
            "<tr>",
            "<th>Version</th>",
            "<th>Changes</th>",
            "</tr>",
            "</thead>",
            "<tbody>",
            "\n".join(rows),
            "</tbody>",
            "</table>"
        ])

    def get_item_path(item: str) -> str:
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
    
    def admo_warning(text: str) -> str:
        return f'<div class="admonition warning"><p class="admonition-title">{text}</p></div>'
    
    def invslot(data, fallback: str) -> str:
        slot = [
            f'<span class="{"animated " if isinstance(data.get("variants"), list) else ""}invslot-item" data-minetip-title="',
            data.get("name", fallback.replace("_", " ").title()),
            '"',
            f' data-minetip-text="{data["lore"]}">' if "lore" in data else ">"
        ]

        if isinstance(data.get("variants"), list):
            for i, variant in enumerate(data["variants"]):
                slot.append(f'<img src="/assets/img/items/{get_item_path(variant)}.png" class="{"animated-active " if i == 0 else ""}no-glight" loading="eager" alt="{fallback}">')
        else:
            slot.append(f'<img src="/assets/img/items/{get_item_path(fallback)}.{"gif" if "gif" in data and data["gif"] else "png"}" class="no-glight" loading="lazy" alt="{fallback}">')
        
        slot.append('</span>')

        return ''.join(slot)
    
    def html_block(element: str, content: str = "", level: int = 0) -> str:
        slashes = "/" * (3 + level)

        if content:
            return '\n'.join([
                f'{slashes} html | {element}',
                content,
                slashes
            ])
        
        return f'{slashes} html | {element}'
    
    def close_block(level: int = 0) -> str:
        return "/" * (3 + level)
    
    def get_item_table(id: str, json_data: dict, item_path: str) -> list[str]:
        strings = [f'<div class="{"animated " if isinstance(json_data.get("variants"), list) else ""}icon">']
        
        if isinstance(json_data.get("variants"), list):
            for i, variant in enumerate(json_data["variants"]):
                strings.append(f'<img src="/assets/img/icons/{get_item_path(variant)}.png" class="{"animated-active " if i == 0 else ""}no-glight" loading="eager" alt="{id}">')
        else:
            strings.append(f'<img src="/assets/img/icons/{item_path}.png" class="no-glight" loading="lazy" alt="{id}">')
        
        strings.extend([
            '</div>',
            '<table class="infobox-table">',
            '<tbody>',
        ])
        
        if isinstance(json_data.get("attributes"), dict):
            for key, value in json_data["attributes"].items():
                strings.extend([
                    '<tr>',
                    f'<td><b>{"Stackable" if key.lower() == "stack_size" else key.replace("_", " ").title()}</b></td>'
                ])

                if isinstance(value, dict):
                    values = []

                    for vKey, vValue in value.items():
                        if key.lower() == "stack_size":
                            values.append(f"{vKey}: {f"Yes ({vValue})" if isinstance(vValue, int) and vValue > 1 else "No"}")
                        elif key.lower() == "tool":
                            tool = read_json(f"docs/assets/items/{get_item_path(vValue)}.json")

                            values.append(f"{vKey}:{f"<br>{invslot(tool, vValue)}" if tool else f" {vValue}"}")
                        else:
                            values.append(f"{vKey}: {vValue}")
                    
                    cell_content = "<br>".join(values)
                elif isinstance(value, bool):
                    cell_content = "Yes" if value else "No"
                elif isinstance(value, list):
                    cell_content = "<br>".join(value)
                else:
                    if key.lower() == "stack_size" and isinstance(value, int):
                        cell_content = f"Yes ({value})" if value > 1 else "No"
                    elif key.lower() == "tool":
                        tool = read_json(f"docs/assets/items/{get_item_path(value)}.json")

                        cell_content = invslot(tool, value) if tool else str(value)
                    else:
                        cell_content = str(value)
                
                strings.extend([
                    f'<td>{cell_content}</td>',
                    '</tr>'
                ])
        
        strings.extend([
            '</tbody>',
            '</table>'
        ])

        return strings
        