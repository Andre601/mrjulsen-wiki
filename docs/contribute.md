# Contribute

This wiki is happy for any contributions it gets to keep the info shown updated.  
This page acts as a source of info regarding how you can contribute changes and what to look out for.

## Requirements

This wiki is build using [MkDocs](https://mkdocs.org){ target="_blank" rel="nofollow" } and the following additional dependencies:

/// html | div.grid.cards
-   [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/){ target="_blank" rel="nofollow" }
    
    ----

    Provides the Material theme used for this site alongside various QoL features.

-   [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/){ target="_blank" rel="nofollow" }
    
    ----

    Various Extensions used on this Site.

-   [MkDocs-Macros](https://mkdocs-macros-plugin.readthedocs.io/){ target="_blank" rel="nofollow" }
    
    ----

    Used for creating Jinja2 macros which are used for features like displaying crafting recipes and advancements.

-   [MkDocs GLightbox](https://github.com/blueswen/mkdocs-glightbox){ target="_blank" rel="nofollow" }
    
    ----

    Adds the ability to click an image to view in a gallery.

-   [mkdocs-redirects](https://github.com/mkdocs/mkdocs-redirects){ target="_blank" rel="nofollow" }
    
    ----

    Adds the ability to create redirects from old (non-existant) pages to new ones.
///

To contribute to the wiki, we suggest to fork the repository, clone it to your desktop and install the necessary dependencies.  
The easiest way to install all necessary dependencies, is by running `pip install -r requirements.txt` in the folder where the `mkdocs.yml` is located in.

## Formatting

This Wiki has some special ways of formatting certain content to provide what it is currently offering.

### Links

The wiki supports wikimedia-inspired links:

| Format                          | Description                                                                           |
|---------------------------------|---------------------------------------------------------------------------------------|
| <code>\[\[Page]]</code>         | to link to a page.                                                                    |
| <code>\[\[Page\|Text]]</code>    | to link to a page with a custom text displayed.                                       |
| <code>\[\[mc:Page]]</code>      | to link to an external page (in this example to the [[mc:Main Page|Minecraft Wiki]]). |
| <code>\[\[mc:Page\|Text]]</code> | to link to an external page with a custom text displayed.                             |

Links to unknown Wiki pages will be displayed as non-clickable red-links. Example: <code>\[\[Unknown]]</code> shows as [[Unknown]].  
External sites are defined in the `mkdocs.yml` in the `interwiki` section under `extra`.

### Recipes

Macros for displaying crafting, smelting and smithing recipes have been created that are implemented using the following formats:

{% raw %}
| Format                                  | Description                                                 |
|-----------------------------------------|-------------------------------------------------------------|
| `{{ crafting_recipe("namespace:id") }}` | Displays a Crafting recipe from the provided namespaced ID. |
| `{{ smelting_recipe("namespace:id") }}` | Displays a Smelting recipe from the provided namespaced ID. |
| `{{ smithing_recipe("namespace:id") }}` | Displays a Smithing recipe from the provided namespaced ID. |
{% endraw %}

/// note | Notes
- The namespace can be omitted in which case the `minecraft` one is assumed.
- An optional `header` and `footer` option exist to enable the prepending and appending of a table start (header row) and table end respectively. Default is `True`.
///

In order for a recipe to be displayed, are certain criterias to be met:

1. A JSON file matching the `id` exists in a folder matching `namespace` in `docs/assets/items/`
2. The JSON file contains a `crafting`, `smelting` or `smithing` section with their respective required options, based on what macros is used.
3. Additional JSON files for ingredient items exist. This is primarely to display their images.

### Advancements

A Macros has been made to display advancements with an icon, name, description and optional requirements.  
The format is {% raw %}`{{ advancement("namespace:id") }}`{% endraw %} with an optional `header` and `footer` option existing to enable the creation of a table start (header row) and table end respectively. Default is `True`.

In order for an advancement to be displayed, are certain criterias to be met:

1. A JSON file matching the `id` exists in a folder matching `namespace` in `docs/assets/advancements/`
2. The JSON file contains a `name`, `icon` and `description`.

## Structure

The site has a very distinct structure that needs to be followed:

- `categories/<modname>.md` lists the tags/categories used in the respective mod pages while also linking to them. 
- `docs/<modname>/` contains the individual wikipages for the respective mod.
- `docs/assets/advancements/` contains JSON files with Advancement Data for the respective mods.
- `docs/assets/img/` contains images used for various parts in the Wiki, such as recipe displays.
- `docs/assets/items/` contains assets - primarely JSON files - related to Items used in crafting recipes and similar.

Should you add any new page to the wiki itself, is the `nav` section in `mkdocs.yml` to be updated accordingly. Make sure that pages are sorted alphabetically and properly categorized (i.e. Blocks are to be stored in a sub-page named blocks.).  
Categories are to be added to a page via the YAML frontmatter using the `tags` key:   
```yaml
tags:
  - modname/some_category
```

Note that the tag has to start with the modname followed by a slash, to make it a sub-category.

Should you need to add a tag to all pages of the mod folder itself, add it to the `.meta.yml` inside the folder. If no such file exists, create it.