---
no_wikilinks: true
categories:
  - DragonLib
---

# Getting Started

Welcome to DragonLib 3! This page explains how to add DragonLib to your project.

## Versions

You can search for a version on the CurseForge or Modrinth pages.

## Setup

First, create a new multiloader project using Architectury. Follow the instructions in the [Architectury Documentation](https://docs.architectury.dev/plugin/get_started){ target="_blank" rel="nofollow" }. Ensure that the **Architectury API** is available, as DragonLib uses it.

Add this to the `build.gradle` of your root project:

```groovy
repositories {
    // Other repos
    maven { url = "https://maven.mrjulsen.net" } // DragonLib
    maven { url = "https://raw.githubusercontent.com/Fuzss/modresources/main/maven" } // Forge Config API Port
}
```

Add this to the `build.gradle` of your sub-projects:
```groovy
dependencies {
    // Other dependencies
    modImplementation("de.mrjulsen.mcdragonlib:dragonlib-{modloader}:{minecraft_version}-{dragonlib_version}")
}
```

Replace `{modloader}` with `forge`/`neoforge` or `fabric`. In the `common` project, `fabric` is usually used. There is no dedicated `common` version of the Library!

Now edit your `mods.toml` and `fabric.mod.json` file and add DragonLib as dependency.

/// tab | `mods.toml`
```toml
[[dependencies.examplemod]]
modId = "dragonlib"
mandatory = true
versionRange = "[{dragonlib_version},)"
ordering = "BEFORE"
side = "BOTH"
```
///

/// tab | `fabric.mod.json`
```json
{
    "depends": {
        "dragonlib": ">={dragonlib_version}"
    }
}
```
///