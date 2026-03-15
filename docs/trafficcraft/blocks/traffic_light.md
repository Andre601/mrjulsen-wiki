---
categories:
  - TrafficCraft
  - TrafficCraft/Paintable
  - TrafficCraft/Wrenchable
---

# Traffic Light

The **Traffic Light** is a decorative block that can be used for roads, crosswalks and similar.  
It can display colored lights or symbols, or white symbols if set to *Tram* mode.

## Usage

Right-clicking the Traffic Light with a [[Wrench]] will open up a GUI containing various features to edit.

### General Traffic Light Settings

On the top-left is a current display of the Traffic Light as it is shown in the world. Clicking the Traffic Light itself will open a Menu where you can change its general settings such as the Type (Vehicular or Tram), how many ligths to show and if symbols should be displayed. Note that only the *Vehicular* type allows colors and no Symbols to be displayed.

### Signal Settings

Right-clicking any of the displayed lights allows you to change the displayed Color, or the Symbol if in Tram Mode.

### Traffic Light Control Type

Clicking the button allows you to toggle between different modes:

- Static (Default): Lights either are on or off based on what is configured. They can be toggled by pressing the corresponding icon shown underneath the button.
- Own Schedule: Allows you to configure a Schedule that the Traffic Light is following and whether it's enabled or not.
- [[Traffic Light Controller]]: Allows you to set an ID that is then used in the Traffic Light Controller to remotely change the Traffic Light. Note that this requires you to link the Traffic Light to the Controller using a Traffic Light Linker.

## Redstone output

Using a Comparator, the current state of the Traffic Light can be read as a Redstone Signal Strength.

The outputed signal strength depends on the lights that are currently turned on:

| Lights             | Redstone Signal Strength |
|--------------------|-------------------------:|
| ![all_off]         | 0                        |
| ![green_on]        | 2                        |
| ![yellow_on]       | 4                        |
| ![yellow_green_on] | 6                        |
| ![red_on]          | 8                        |
| ![red_green_on]    | 10                       |
| ![red_yellow_on]   | 12                       |
| ![all_on]          | 14                       |


[all_off]: ../../assets/img/ui/trafficcraft/traffic_light_all_off.png
[green_on]: ../../assets/img/ui/trafficcraft/traffic_light_green_on.png
[yellow_on]: ../../assets/img/ui/trafficcraft/traffic_light_yellow_on.png
[yellow_green_on]: ../../assets/img/ui/trafficcraft/traffic_light_yellow_green_on.png
[red_on]: ../../assets/img/ui/trafficcraft/traffic_light_red_on.png
[red_green_on]: ../../assets/img/ui/trafficcraft/traffic_light_red_green_on.png
[red_yellow_on]: ../../assets/img/ui/trafficcraft/traffic_light_red_yellow_on.png
[all_on]: ../../assets/img/ui/trafficcraft/traffic_light_all_on.png

## Obtaining

### Crafting

{{ crafting_recipe("trafficcraft:traffic_light") }}

## Advancements

{{ advancement("trafficcraft:you_shall_not_pass") }}