# Traffic Light

The **Traffic Light** is a decorative block that can be used for roads, crosswalks and similar.

## Functionality

The Traffic Light can display either colored lights or symbols, or white symbols when set to *Tram* mode.

Right-clicking the Traffic Light with a Wrench will open up a GUI containing various features to edit.

### General Traffic Light Settings

On the top-left is a current display of the Traffic Light as it is shown in the world. Clicking the Traffic Light itself will open a Menu where you can change its general settings such as the Type (Vehicular or Tram), how many ligths to show and if symbols should be displayed. Note that only the *Vehicular* type allows colors and no Symbols to be displayed.

### Signal Settings

Right-clicking any of the displayed lights allows you to change the displayed Color, or the Symbol if in Tram Mode.

### Traffic Light Control Type

Clicking the button allows you to toggle between different modes:

- Static (Default): Lights either are on or off based on what is configured. They can be toggled by pressing the corresponding icon shown underneath the button.
- Own Schedule: Allows you to configure a Schedule that the Traffic Light is following and whether it's enabled or not.
- Traffic Light Controller: Allows you to set an ID that is then used in the Traffic Light Controller to remotely change the Traffic Light. Note that this requires you to link the Traffic Light to the Controller using a Traffic Light Linker.

## Redstone output

Using a Comparator, you can read the Traffic Light's curren state as a redstone signal.

The Signal Strength is based on what signals are currently active, with multiple ones having their individual signal strengths added together.

| Active Signal | Redstone Signal Strength |
|---------------|--------------------------|
| Off (None)    | 0                        |
| Red           | 8                        |
| Yellow        | 4                        |
| Green         | 2                        |

As an example, Red and Yellow would output a Signal Strength of 12 (8 + 4) while Green and Yellow would output 6 (2 + 4).

## Obtaining

### Crafting

{{ crafting_recipe("trafficcraft:traffic_light") }}

## Advancements

{{ advancement("trafficcraft:you_shall_not_pass") }}