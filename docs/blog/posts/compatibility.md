---
date: 2026-03-01
description: An overview of which of my mods are compatible with each other and which version of dragonLib is required.
categories:
  - DragonLib
---

# DragonLib 3 Compatibility

With the introduction of [DragonLib 3](https://mrjulsen.net/mods/dragonlib/docs/), several technical changes have been made in my mods. Not only are mods that use DragonLib 3 **no longer** compatible with older versions of my mods that don't use it, but DragonLib 3 is also no longer integrated into my mods via jar-in-jar and must be installed manually.

<!-- more -->

## Compatibility Matrix

* Only versions in the same column are compatible with each other
* If DragonLib is not required, delete it from the mods folder
* The cells show the version ranges (no distinction between alpha/beta/release)
* You can also say: All versions released after **December 18, 2025** require DragonLib (right column)

| Mod | DragobLib not required { .dl-table--red } | DragonLib required { .dl-table--green } | Downloads |
|-----|:-----------------------------------------:|:---------------------------------------:|-----------|
| <div class="dl-icon"><img src="https://cdn.modrinth.com/data/FdE7Dv6P/9be933f800d95280aecbac4875c6544ce161106e_96.webp"> BlockBeats</div> | <= 0.2.0 { .dl-table--red } | >=0.2.1 { .dl-table--green } | [:simple-curseforge: CurseForge](https://www.curseforge.com/minecraft/mc-mods/blockbeats){ target="_blank" rel="nofollow" }<br>[:simple-modrinth: Modrinth](https://modrinth.com/mod/blockbeats){ target="_blank" rel="nofollow" } |
| <div class="dl-icon"><img src="https://cdn.modrinth.com/data/apgVYbxQ/be74494fe92eedde4ca3f3e8d7dc6891d8934d7c_96.webp"> DragNSounds API</div> | <= 0.2.1 { .dl-table--red } | >=0.2.2 { .dl-table--green } | [:simple-curseforge: CurseForge](https://www.curseforge.com/minecraft/mc-mods/dragnsounds-api){ target="_blank" rel="nofollow" }<br>[:simple-modrinth: Modrinth](https://modrinth.com/mod/dragnsounds-api){ target="_blank" rel="nofollow" } |
| <div class="dl-icon"><img src="https://cdn.modrinth.com/data/VzdCnMqW/86d874140963047f059c1d9cf88db55037d76a08_96.webp"> Create: Pantographs and Wires</div> | <= 0.1.2 { .dl-table--red } | >=0.2.0 { .dl-table--green } | [:simple-curseforge: CurseForge](https://www.curseforge.com/minecraft/mc-mods/create-pantographs-and-wires){ target="_blank" rel="nofollow" }<br>[:simple-modrinth: Modrinth](https://modrinth.com/mod/create-pantographs-and-wires){ target="_blank" rel="nofollow" } |
| <div class="dl-icon"><img src="https://cdn.modrinth.com/data/Dq3STxps/10e1b3796f2fcf5b70bb77110e68b59c750310ac_96.webp"> Create Railways Navigator</div> | <= 0.8.5 { .dl-table--red } | >=0.9.0 { .dl-table--green } | [:simple-curseforge: CurseForge](https://www.curseforge.com/minecraft/mc-mods/create-railways-navigator){ target="_blank" rel="nofollow" }<br>[:simple-modrinth: Modrinth](https://modrinth.com/mod/create-railways-navigator){ target="_blank" rel="nofollow" } |
| <div class="dl-icon"><img src="https://cdn.modrinth.com/data/Y1PXWvWn/ef2dca01949b6b24630864f81a6786458cf00e91_96.webp"> TrafficCraft</div> | <= 1.1.3 { .dl-table--red } | >=1.2.0 { .dl-table--green } | [:simple-curseforge: CurseForge](https://www.curseforge.com/minecraft/mc-mods/trafficcraft){ target="_blank" rel="nofollow" }<br>[:simple-modrinth: Modrinth](https://modrinth.com/mod/trafficcraft){ target="_blank" rel="nofollow" } |

Download DragonLib:  
[:simple-curseforge: CurseForge](https://www.curseforge.com/minecraft/mc-mods/dragonlib)  
[:simple-modrinth: Modrinth](https://modrinth.com/mod/dragonlib)

## FAQ

### Why is DragonLib 2.2.24 or 2.2.28 not available on your mod page?

These versions of DragonLib are included in the JAR files of my mods. You don't need to install them manually. If you're getting an error, you've probably combined versions of my mods from different columns of the table above, or DragonLib is installed as a separate mod in your modpack.

### Now, which versions exactly are compatible with each other?

The two columns above show the version ranges. All versions of a mod in this range are compatible with all versions of any other mod in the same column. For example, if **Create Railways Navigator** uses a version from the <span style="background:rgba(255, 0, 0, 0.15); padding:2px 4px;">left column</span>, but **BlockBeats** uses a version from the <span style="background:rgba(0, 255, 0, 0.15); padding:2px 4px;">right column</span>, it will not work.

### Why is DragonLib no longer included in the mods?

To simplify maintenance. In the past, there were some bugs in DragonLib that required updating each mod individually. Now I'm just rolling out an update for DragonLib that users can install.

### Why is DragonLib 3 not compatible with older versions?

Because DragonLib 3 was almost completely rewritten to meet modern requirements. Many systems no longer exist or have been completely rebuilt, which is why older mod versions cannot use them.

### Why so complicated? I hate you for this!

You're welcome to hate me for this, but these changes were necessary to improve quality and maintainability, especially when looking to future Minecraft versions.
