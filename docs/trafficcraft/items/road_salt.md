---
categories:
  - TrafficCraft
---

# Road Salt

**Road Salt** is an item obtained from breaking [[Salt]].

## Usage

Road Salt can be placed on a Block by right-clicking it with the item to melt ice and snow in the surrounding area.

### Effects

Road Salt has an influence on the surrounding 4 block area (diamond-shaped) it was placed in.

- [[mc:Ice]] and [[mc:Snow]] melt.
    - The speed at which they melt is influenced by the Road Salt's [quality level](#quality-levels).
- [[mc:Grass Block|Grass Blocks]] in the area will turn into [[mc:Coarse Dirt]]
- Other forms of vegitation (plants, flowers, etc) break.

The effects are configurable.

## Quality Levels

Road Salt when placed is "fresh" but will lose quality over time.  
How fast it loses quality is influenced by the [[mc:randomtickspeed|`randomTickSpeed` Gamerule]].

Road Salt can have one of three quality levels:

| Level     | Effectiveness compared to `fresh` |
|-----------|----------------------------------:|
| `fresh`   | -                                 |
| `muddy`   | 50%                               |
| `diluted` | 25%                               |

The speed at which Road Salt changes quality will also take 2 times longer per level, meaning it takes 2 times longer for it to change from `muddy` to `diluted` than it took to turn from `fresh` to `muddy`.  
Once it reached the final Level will any future update remove it completely, allowing snow and Ice to form again in the area.

## Obtaining

### Mining

Road Salt is obtained from mining Salt Blocks which spawn naturally in oceans and rivers.  
[[mc:Fortune]] has an influence on the drop rate.

## Advancements

{{ advancement("trafficcraft:salty") }}