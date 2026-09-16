---
status: unreleased
categories:
  - Create Railways Navigator
---

# Penalty Anchor

The **Penalty Anchor** is a Block that can be used to force a train to take a certain route by assigning a penalty value.

## Usage

Similar to a [[c:Train Signal]] is the Penalty Anchor assigned to a track by right-clicking it with the item in hand, followed by placing the block nearby.  
Once placed, the Block acts as an obstacle on the targeted track and adds its penalty value to any route that runs across it, making the train prefer alternative paths.

### Penalty Value

The penalty value can be adjusted while clicking and holding a [[c:Wrench]] and hovering over one of the block's sides. It ranges from `0` to `1000` in steps of `10` and defaults to `50`. A value of `0` disables the anchor entirely.

### Affected Trains

The block has a filter slot on the top face that accepts an item filter.  
When a filter is set, the penalty only applies to trains that carry matching cargo. If the filter is empty, the penalty applies to all trains.

### Redstone

The Penalty Anchor reacts to redstone from **above or below** only. A redstone signal weakens the penalty the stronger it gets, following `result = penalty * (15 − signal) / 15`. At full signal strength (`15`) the anchor is turned off completely, indicated by the arrow turning black.

Whenever a Train passes, the Penalty Anchor emits a redstone signal from its **four sides** for a short moment, similar to a [[c:Train Observer]] from Create.

Using a **Comparator**, you can read the effective penalty.

### Penalty System

The Penalty System is explained in detail in the Blog Post [Train Penalty System Guide](../../blog/posts/train-penalty-system-guide.md).

## Obtaining

### Crafting

{{ crafting_recipe("createrailwaysnavigator:penalty_anchor") }}
