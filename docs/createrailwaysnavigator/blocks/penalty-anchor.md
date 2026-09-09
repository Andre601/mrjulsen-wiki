---
unreleased: true

title: Penalty Anchor
categories:
  - Create Railways Navigator
---

# Penalty Anchor

The **Penalty Anchor** is a Block that can be used to force a train to take a certain route by assigning the selected one a penalty value.

## Usage

Similar to a [[c:Train Signal]] is the Penalty Anchor assigned to a track by right-clicking it with the item in hand, followed by placing it nearby.  
Once placed does the Block assign a penalty value to the track, which can be modified by clicking and holding the right mouse button while hovering over the side of the block. This opens a slider where a Penalty value can be assigned.

### Redstone

Powering the Penalty Anchor with redstone disables it, indicated by the red arrow turning black.

The Penalty Anchor emits a redstone signal whenever a Train is passing it, similar to a [[c:Train Observer]] from Create.

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

<small>^1^{ #n1 } If the wait time is less than 1000 will a hardcoded value of 1000 be added making a Waiting Train always at least 1050.</small>

## Obtaining

### Crafting

{{ crafting_recipe("createrailwaysnavigator:train_station_clock") }}
