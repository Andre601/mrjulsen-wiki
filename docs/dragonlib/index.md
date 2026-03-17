---
icon: fontawesome/solid/dragon
categories:
  - DragonLib
---

# DragonLib 3

![dragonlib_banner](../assets/img/dragonlib_banner.png)

**DragonLib** is a multiloader Minecraft library created by MrJulsen and built on top of [Architectury API](https://github.com/architectury/architectury-api){ target="_blank" rel="nofollow" }. It offers many useful tools, abstraction layers, and its own systems to simplify modding in Minecraft between different modloaders and versions.

## Features

The following is a non-exhaustive list of features in DragonLib:

/// html | div.grid.cards
- Custom GUIs
- Custom Networking
- Simple Modeling tools (To modify block/items at runtime)
- OBJ Model support
- Property and Event System
- Many useful utilities
- All features in Architectury API
- And more...
///

/// note
Since DragonLib is based on the Architectury API, you'll need some of its features too (e.g. registries, mod events). Read the [Architectury documentation](https://docs.architectury.dev/start){ target="_blank" rel="nofollow" } for more information.
///

## How to use

DragonLib can easily be integrated into your project via gradle. Further information can be found in [Getting started](getting_started.md).

/// note
Users of your mod will need to install DragonLib as a library. It is **not** recommended to integrate DragonLib into your mod via jar-in-jar, as this prevents library patches from being deployed without updating your mod.
///

## Download

The latest versions of DragonLib can always be found on CurseForge and Modrinth. You can use the version numbers of the files there for the dependencies in your project. For Maven releases (which you'll need for your project), read [Getting started](getting_started.md).

/// html | div.grid.cards
- ### [:simple-curseforge: CurseForge](https://www.curseforge.com/minecraft/mc-mods/dragonlib){ target="_blank" rel="nofollow" }
- ### [:simple-modrinth: Modrinth](https://modrinth.com/mod/dragonlib){ target="_blank" rel="nofollow" }
///

## Community

The entire library is open source and available on GitHub. Feel free to take a look at the code. If you'd like to help and contribute to the project by fixing bugs or adding new features, you're welcome to do so by submitting pull requests on GitHub!

If you'd like to talk with the community, there's a dedicated channel for modders on my Discord server (in addition to the channels for my other mods).

/// html | div.grid.cards
- ### [:simple-github: GitHub](https://github.com/MisterJulsen/MC-Dragonlib2){ target="_blank" rel="nofollow" }
- ### [:simple-discord: Discord](https://discord.mrjulsen.net/){ target="_blank" rel="nofollow" }
///

## Why is the mod called DragonLib?

Because Dragons are cool :dragon:

## Credits

DragonLib uses the following projects:

- [Architectury API](https://github.com/architectury/architectury-api){ target="_blank" rel="nofollow" }
- [Forge Config API Port](https://github.com/Fuzss/forgeconfigapiport){ target="_blank" rel="nofollow" } (Fabric Only)

## License

The current license can be found on GitHub.