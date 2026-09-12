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

Whenever the Train has to travel to a location (i.e. a Train Station) does it check all available routes and pick one based on its "penalty value".  
The penalty value is calculated by looking for certain Blocks and Trains on a route, getting their penalty value and adding it to the total. The train then picks the route with the lowest penalty value.

This can cause weird routing where a train takes a junction it shouldn't due to it avoiding a Station on the intended path.  
Using the Penalty Anchor, a custom Penalty value can be added to a route to make it less likely for the Train to take it.

The following Trains and Blocks have a Penalty Value:

| Train/Block                   | Description                                     | Penalty Value                         |
|-------------------------------|-------------------------------------------------|--------------------------------------:|
| Manual Train                  | A Player-controlled Train                       | 200                                   |
| Idle Train                    | A train with a paused or no schedule            | 700                                   |
| Waiting Train                 | A Train waiting at a signal.                    | 50 + (wait time in seconds)^[1](#n1)^ |
| Arriving Train                | A Train arriving at a Station or Signal         | 50                                    |
| Any Train                     | Any other Train not matching previous criterias | 25                                    |
| Station                       | A Train Station                                 | 50                                    |
| Station w/ Train              | A Train Station with a Train on it              | 300                                   |
| Red Signal                    | A red Signal                                    | 25                                    |
| Red Signal (Redstone powered) | A Signal forced red through Redstone            | 400                                   |

<small>^1^{ #n1 } If the wait time is less than `1000` will a hardcoded value of `1000` be added making a Waiting Train always at least `1050`.</small>

## Obtaining

### Crafting

{{ crafting_recipe("createrailwaysnavigator:penalty_anchor") }}
