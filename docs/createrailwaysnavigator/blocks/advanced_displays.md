# Advanced Displays

/// redirect | All Advanced Display Blocks redirect to here.
///

**Advanced Displays** are blocks that appear similar to monitors and can display data similar to a [[c:Display Board]] from Create.

## Usage

Placed Advanced Displays of the same type will connect to each other vertically and horizontally when forming a rectangle.  
Right-clicking the Advanced Display with a Create [[c:Wrench]] opens their GUI, allowing to configure the displayed data based on the selected type.

The "Double-sided" option available toggles whether the same info is to be displayed on the fron and back, or only the front.

More options are [explained below](#options).

### Train Destination

Displays information about the trains next stations and final station.  
This option is recommended for displays on the outside of a train to show to players information about where it comes from and where it is heading.

### Passenger Information

Displays information about a trains next stops and optional statistics.  
This option is recommended for displays inside a train.

### Platform Display

Allows displaying info about an arriving/departing train such as the ingame time for when it will arrive/depart.  
This option is recommended to be used at station platforms and requires data to be provided from a [[c:Display Link]] connected to a [[c:Train Station|Station]].

The configured name in the display link can use Glob patterns to match multiple stations. The name also does not need to match the name of the station it is connected to.  
Some examples:

- `Station *`: Display from any Station with a name starting with `Station`
- `Station [1-3]`: Display from Stations named `Station 1`, `Station 2` and `Station 3`

### Departure Board

Displays all trains that arrive at/depart from a specified Station.  
This option is recommended to be used as a general info board for arrivals and departures of trains at a station and requires data to be provided from a Display Link connected to a station.

The configured name in the display link can use Glob patterns to match multiple stations. The name also does not need to match the name of the station it is connected to.  
Some examples:

- `Station *`: Display from any Station with a name starting with `Station`
- `Station [1-3]`: Display from Stations named `Station 1`, `Station 2` and `Station 3`

### Static Text

Allows to display static text.  
The provided text can either be a String or a supported Chat Component. The `Rich Text` option allows defining up to 50 separate text lines, each with own scaling, offset, etc.

## Options

Advanced Displays provide various options for their different display types.  
Below are all options available. Unless stated otherwise are these options available for all display types.

### Font Color/Background Color

Allows to set the Text and Background color to display.  
Only the pre-made colors can be selected.

### Carriage Index Offset

/// info | Availability
This option is only available for:

- Train Destination (Detailed mode)
- Passenger Information (Detailed with Schedule mode)
///

Allows to offset the displayed carriage number by the specified value.  
When `Overwrite index` is enabled will the provided number instead be used as the value to display.

### Show 'Do not board' text

/// info | Availability
This option is only available for:

- Train Destination
- Passenger Information
///

When enabled, displays a `Do not board` message whenever the train reaches the final stop in its schedule.

### Show train line color

Sets whether the train line color, if any, should be displayed.  
The train line color is configured through the global settings and applied through the Schedule Section option in a Train Schedule.

### Train Name Width

/// info | Availability
This option is only available for:

- Train Destination (Compact and Extended mode)
///

Sets the max width that the displayed train name should have.  
Any text beyond the max width will result in the text scrolling.

### Time Display

/// info | Availability
This option is only available for:

- Passenger Information (Detailed with Schedule mode)
///

Sets the time displayed for when the train arrives at the (next) station.  
Available options are `ABS` (default) for absolute time (i.e. `13:00`) or `ETA` for Estimated Time of Arrival (i.e. `1 min`). Both time are ingame based.

### Show train stats

/// info | Availability
This option is only available for:

- Passenger Information
///

Sets whether Train statistics such as speed should be displayed.

### Show exit direction

/// info | Availability
This option is only available for:

- Passenger Information
///

Sets whether the display should display possible exit directions using an arrow.  
The direction will be displayed when "Next Stop: ..." is shown.

### Show next connections

/// info | Availability
This option is only available for:

- Passenger Information
///

Sets whether the display should display connections for the station it arrives at.

### Show train multiple times

/// info | Availability
This option is only available for:

- Passenger Information
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

/// info | Availability
This option is only available for:

- Passenger Information (Scrolling Text mode)
///

Sets whether the current ingame time and number of ingame days since world creation should be displayed.