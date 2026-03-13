# MrJulsen Mods Wiki

This repository hosts the content shown at [wiki.mrjulsen.net](https://wiki.mrjulsen.net).

## Structure

The Wiki source has the following Structure:
```
mkdocs.yml
requirements.txt
docs/
└── ...
hooks/
└── wikilinks.py
macros/
└── macros.py
theme/
├── main.html
└── partials/
    ├── content.html
    ├── tags.html
    └── nav_list/
        └── ...
```

- The `docs` folder is where the main Wiki content is located in.  
  It contains markdown files which get converted into HTML files through MkDocs and using the Material for MkDocs theme.
- `hooks` contains python hook files (currently only `wikilinks.py`) which are used in MkDocs for quick functionality to be added.
- `macros` contains the `macros.py` file which itself contains the individual macros used through the MkDocs Macros plugin, to insert features like displaying a crafting recipe.
- `theme` contains theme overrides/extensions used to customize certain aspects of the Wiki.

## Contributions

Any contributions are welcome! Just make sure to follow any necessary instructions provided through you through additional README files or pages. The [Contribute](https://wiki.mrjulsen.net/contribute/) pahe may also help you with certain questions.

In order for you to use this wiki, make sure you install all required dependencies through `pip`.  
The easiest way to install them is through the requirements.txt file:
```shell
pip install -r requirements.txt
```

## License

This project is licensed under MIT. See the [LICENSE](LICENSE) file for further details.