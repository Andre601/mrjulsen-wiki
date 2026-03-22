---
no_wikilinks: true
categories:
  - DragonLib
---

# Getting Started

This page explains how to add DragonLib to your project.

## Versions

You can search for a version on the [Maven GitHub repository](https://github.com/MisterJulsen/mod-resources/tree/main/maven/de/mrjulsen/mcdragonlib).

/// warning
The current version, which is documented here, is DragonLib 3.x.x. DragonLib 2.x.x is no longer supported and not compatible with newer versions.
///

## Setup

First, create a new multiloader project using Architectury. Follow the instructions in the [Architectury Documentation](https://docs.architectury.dev/plugin/get_started){ target="_blank" rel="nofollow" }. Ensure that the **Architectury API** is available, as DragonLib uses it.

Add this to the `build.gradle` of your root project:

```groovy
repositories {
    maven { url = "https://maven.mrjulsen.net" } // DragonLib
    maven { url = "https://raw.githubusercontent.com/Fuzss/modresources/main/maven" } // Forge Config API Port
}
```

Add this to the `build.gradle` of your sub-projects:
```groovy
dependencies {
    modImplementation("de.mrjulsen.mcdragonlib:dragonlib-{modloader}:{minecraft_version}-{dragonlib_version}")
    compileOnly(annotationProcessor("io.github.llamalad7:mixinextras-common:0.4.1"))
    implementation("io.github.llamalad7:mixinextras-forge:0.4.1")
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