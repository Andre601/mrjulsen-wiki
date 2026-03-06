# Road Construction Tool

The **Road Construction Tool** is an item that can be used for the quick creation of roads, including slopes.  
The item comes in [[mc:Tiers|Tool tiers]] Wood, Stone, Iron, Gold, Diamond and Netherite which each offer higher durability.

## Functionality

A line where a road should be placed can be selected by right-clicking two lines. This will select a direct line between the two points, which also works diagonally.

Right-clicking with the tool in the air will display a GUI. This GUI will display the selected coordinates, settings related to road placement and how many blocks and slopes are required for building.  
At the bottom is a *BUILD* button, which can be used to start the road construction.

Once started, the road is placed one row at a time, using durability from the tool for every use. Additionally will a cooldown be applied to the tool that matches the time it takes for constructing the road.

### Replace Blocks

Sets whether existing blocks should be broken and replaced, or skipped. Default is on.

### Road Width

This slider allows to set the max width of the road.  
The range can go from 1 to 9 with 7 being the default width.

### Road Building Blocks

The buttons in this section allow you to switch between [[Asphalt]] and [[Concrete]] Blocks and slopes to be used.

## Obtaining

### Crafting

{{ crafting_recipe("trafficcraft:wood_road_construction_tool", footer=False) }}
{{ crafting_recipe("trafficcraft:stone_road_construction_tool", header=False, footer=False) }}
{{ crafting_recipe("trafficcraft:iron_road_construction_tool", header=False, footer=False) }}
{{ crafting_recipe("trafficcraft:gold_road_construction_tool", header=False, footer=False) }}
{{ crafting_recipe("trafficcraft:diamond_road_construction_tool", header=False) }}

### Smithing

{{ smithing_recipe("trafficcraft:netherite_road_construction_tool") }}

## Advancements

{{ advancement("trafficcraft:under_construction", footer=False) }}
{{ advancement("trafficcraft:highway_to_hell", header=False, footer=False) }}
{{ advancement("trafficcraft:final_destination", header=False) }}