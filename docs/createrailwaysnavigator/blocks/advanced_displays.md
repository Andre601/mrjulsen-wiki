---
categories:
  - Create Railways Navigator
---

# Advanced Displays

/// redirect | All Advanced Display Blocks redirect to here.
///

**Advanced Displays** are blocks that appear similar to monitors and can display data similar to a [[c:Display Board]] from Create.

## Usage

Placed Advanced Displays of the same type will connect to each other horizontally and vertically (depending on the selected display variant) when forming a rectangle.  

- Right-clicking with a [[c:Wrench]] opens a GUI allowing to configure the display.
- Right-clicking with a block applies it to all sides except the front side (similar to Copycats).
- Shift + Right-clicking with a Wrench will remove the copycat block or destroy the display (if it was empty).

The "Double-sided" option toggles whether the content is displayed on both sides or only on the front.

More options are [explained below](#options).

### Train Destination

Displays information about the train's next stations and final station.  
This option is recommended for displays on the outside of a train to show to players information about where it comes from and where it is heading.

### Passenger Information

Displays information about a trains next stops and optional statistics.  
This option is recommended for displays inside a train.

### Platform Display

Allows displaying info about an arriving/departing train such as the ingame time for when it will arrive/depart.  
This option is recommended to be used at station platforms and requires data to be provided from a [[c:Display Link]] connected to a [[c:Train Station|Station]].

/// details | Glob Patterns supported
    type: tip

Glob Patterns can be used to include multiple stations. Some examples:

- `Station *`: Include any Station starting with `Station`
- `Station [1-3]`: Include any Station with a name starting with `Station` followed by a number from 1 to 3.
///

### Departure Board

Displays all trains that arrive at/depart from a specified station.  
This option is recommended to be used as a general info board for arrivals and departures of trains at a station and requires data to be provided from a Display Link connected to a station.

/// details | Glob Patterns supported
    type: tip

Glob Patterns can be used to include multiple stations. Some examples:

- `Station *`: Include any Station starting with `Station`
- `Station [1-3]`: Include any Station with a name starting with `Station` followed by a number from 1 to 3.
///

### Static Text

Allows to display static text.  
The provided text can either be a simple String or a supported json [[mc:text component format]]. The `Rich Text` option allows defining up to 50 separate text lines, each with own customization settings, like scaling, offset, etc.

Static text also supports placeholders to display dynamic data. See [[Placeholders]] for more information.

### Other data sources

The Advanced Displays are also capable of displaying data from other sources, such as boiler status. Please note, however, that the format is very simple, and the information is presented as plain static text. The Advanced Displays are optimized and designed for trains and are not meant to be used for other purposes.


## Options

Advanced Displays provide various options for their different display types.  
Below are all options available. Unless stated otherwise are these options available for all display types.

### Font Color/Background Color

Allows to set the Text and Background color to display.  
Only the pre-made colors can be selected.

### Carriage Index Offset

/// info | Available for [`Train Destination (Detailed mode)`](#train-destination) and [`Passenger Information (Detailed with Schedule mode)`](#passenger-information)
///

Allows to offset the displayed carriage number by the specified value.  
When `Overwrite index` is enabled will the provided number instead be used as the value to display.

### Show 'Do not board' text

/// info | Available for [`Train Destination`](#train-destination) and [`Passenger Information`](#passenger-information)
///

When enabled, displays a `Do not board` message whenever the train reaches the final stop in its schedule. This setting is ignored if the train is about to enter a non-navigable Schedule Section.

### Show train line color

Sets whether the train line color, if any, should be displayed.  
The train line color is configured through the global settings and applied through the Schedule Section option in a Train Schedule.

### Train Name Width

/// info | Available for [`Train Destination (Compact and Extended mode)`](#train-destination), [`Platform Display (Focus and Table mode)`](#platform-display) and [`Departure Board`](#departure-board)
///

Sets the max width that the displayed train name should have.  
Any text beyond the max width will result in the text scrolling.

### Platform Width

/// info | Available for [`Platform Display (Focus and Table mode)`](#platform-display)
///

Sets the max width that the displayed platform should have.  
Any text beyond the max width will result in the text scrolling.

### Stopovers Section Width

/// info | Available for [`Departure Board`](#departure-board)
///

Sets the max width that the displayed stopovers should have.  
Any text beyond the max width will result in the text scrolling.

### Info Section Width

/// info | Available for [`Departure Board`](#departure-board)
///

Sets the max width that any info about the train (i.e. delays) should have.  
Any text beyond the max width will result in the text scrolling.

### Time Display

/// info | Available for [`Passenger Information (Detailed with Schedule mode)`](#passenger-information) and [`Departure Board`](#departure-board)
///

Sets the time displayed for when the train arrives at the (next) station.  
Available options are `ABS` (default) for absolute time (i.e. `13:00`) or `ETA` for Estimated Time of Arrival (i.e. `1 min`). Both time are ingame based.

### Show train stats

/// info | Available for [`Passenger Information`](#passenger-information)
///

Sets whether Train statistics such as speed should be displayed.

### Show exit direction

/// info | Available for [`Passenger Information`](#passenger-information)
///

Sets whether the display should display possible exit directions using an arrow.  
The direction will be displayed when "Next Stop: ..." is shown.

### Show next connections

/// info | Available for [`Passenger Information`](#passenger-information)
///

Sets whether the display should display connections for the station it arrives at.

### Show train multiple times

/// info | Available for [`Passenger Information`](#passenger-information), [`Departure Board`](#departure-board)
///

Sets whether the same train can be displayed multiple times in the next connections (i.e. when arriving from different sides).

### Train Text Component

Sets what text component should be displayed.

| Option             | Description                           |
|--------------------|---------------------------------------|
| `All`              | Show both Train Name and Destination. |
| `Train Name only`  | Default. Only display the Train name. |
| `Destination only` | Only display the Train's destination. |

### Show time and date

/// info | Available for [`Passenger Information (Scrolling text mode)`](#passenger-information)
///

Sets whether the current ingame time and number of ingame days since world creation should be displayed.

### Train Stop Display Type

Sets what kind of train stop should be displayed.

| Option                 | Description                                                           |
|------------------------|-----------------------------------------------------------------------|
| `All`                  | Displays Arrivals and Departures.                                     |
| `Arrivals only`        | Only displays Arrivals.                                               |
| `Arrivals preferred`   | Prioritizes Arrivals, but falls back to showing Departures otherwise. |
| `Departures only`      | Only displays Departures.                                             |
| `Departures preferred` | Prioritizes Departures, but falls back to showing Arrivals otherwise. |

### Displayed Text

/// info | Available only for [Static Text](#static-text)
///

Allows you to set the text that should be displayed on the Display.  
The input field accepts normal text, but also Chat Components.

### X/Y Position

/// info | Available only for [Static Text (Rich Text mode)](#static-text)
///

Sets the X and Y position of the text.  
The X offset is based on the current [Text Alignment](#text-alignment) with Right alignment using the left side of the text as anchor point, while the Y offset uses the top of the Display Area as anchor point.

### Text Alignment

/// info | Available only for [Static Text (Rich Text mode)](#static-text)
///

Allows to set the text to either be on the left, center or right of the Display.

### Minimum X Scale/X Scale/Y Scale

/// info | Available only for [Static Text (Rich Text mode)](#static-text)
///

Sets the Minimum X scale and maximum X and Y scale for the text.  
The text will be scaled as close as possible and if not possible, apply the configured [Boundary Behaviour](#boundary-behaviour) to the text.

### Text Max Width

/// info | Available only for [Static Text (Rich Text mode)](#static-text)
///

Sets the max width of the text. The text will be scaled as close as possible and if not possible, apply the configured [Boundary Behaviour](#boundary-behaviour) to the text.

### Boundary Behaviour

/// info | Available only for [Static Text (Rich Text mode)](#static-text)
///

Sets how text going beyond the [Max text width](#text-max-width) should be handled.

| Option          | Description                                                        |
|-----------------|--------------------------------------------------------------------|
| `Cut Off`       | Cuts off any excess text.                                          |
| `Scale/Scroll`  | Scales the text as good as possible and otherwise makes it scroll. |
| `Always Scroll` | Makes the text scroll, no matter its actual width.                 |

### Label Background Color

/// info | Available only for [Static Text (Rich Text mode)](#static-text)
///

Sets the background color that should be used for the text. Custom colors using the Hex Code format are supported.  
Activating `Full Size` will make the color fill the entire configured area of the text instead of just the text itself.

## Obtaining

### Crafting

{{ crafting_recipe("createrailwaysnavigator:advanced_display", footer=False) }}
{{ crafting_recipe("createrailwaysnavigator:advanced_display_block", header=False , footer=False) }}
{{ crafting_recipe("createrailwaysnavigator:advanced_display_small", header=False , footer=False) }}
{{ crafting_recipe("createrailwaysnavigator:advanced_display_panel", header=False , footer=False) }}
{{ crafting_recipe("createrailwaysnavigator:advanced_display_slab", header=False , footer=False) }}
{{ crafting_recipe("createrailwaysnavigator:advanced_display_half_panel", header=False , footer=False) }}
{{ crafting_recipe("createrailwaysnavigator:advanced_display_sloped", header=False) }}

## Advancements

{{ advancement("createrailwaysnavigator:not_quite_4k") }}
