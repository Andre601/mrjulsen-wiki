<!-- --8<-- [start:colors]  -->
#### Font Color

Sets the color that the displayed text should have.

#### Background Color

Sets the color that the Background should have.
<!-- --8<-- [end:colors] -->

<!-- --8<-- [start:carriage_index_offset]  -->
#### Carriage Index Offset

Allows to modify the displayed carriage number by either adding an offset to it or display the set number instead.  
Carriages are counted from the start of a train (closest to station at assembly).
<!-- --8<-- [end:carriage_index_offset] -->

<!-- --8<-- [start:show_line_color] -->
#### Show train line color

Sets whether Train Line Colors are to be displayed, if one is configured.  
Train Lines and their color are configured through the Global settings while the Train Line itself is assigned to the train via a Schedule Section.
<!-- --8<-- [end:show_line_color] -->

<!-- --8<-- [start:show_do_not_board] -->
#### Show 'Do not board' text

Sets whether the Display should show `Do not board` when the train reaches its final destination in its Schedule.
<!-- --8<-- [end:show_do_not_board] -->

<!-- --8<-- [start:train_name_width] -->
#### Train Name Width

Sets the max width that the train name should have.  
Any text that goes beyond the configured width will start to scroll.

The display prioritizes any configured Train Line and falls back to the Train's own name when none is available.
<!-- --8<-- [end:train_name_width] -->

<!-- --8<-- [start:platform_text_widths_focus] -->
#### Train Name Width

Sets the max width for displaying Train Names.  
Any text longer than the configured width will scroll.

#### Platform Width

Sets the max width for displaying the Platform.  
Any text longer than the configured width will scroll.

/// note
The same options exist also for the next departing train.
///
<!-- --8<-- [end:platform_text_widths_focus] -->

<!-- --8<-- [start:platform_text_widths_table] -->
#### Train Name Width

Sets the max width for displaying Train Names.  
Any text longer than the configured width will scroll.

#### Platform Width

Sets the max width for displaying the Platform.  
Any text longer than the configured width will scroll.
<!-- --8<-- [end:platform_text_widths_table] -->

<!-- --8<-- [start:time_display] -->
#### Time Display

Sets how time should be displayed. Available options are `ABS` (Absolute time, i.e. `13:00`) and `ETA` (Estimated Time of Arrival, i.e. `2 min`).
<!-- --8<-- [end:time_display] -->

<!-- --8<-- [start:show_train_stats] -->
#### Show Train Stats

Whether Train statistics such as current speed and what day it is should be displayed.
<!-- --8<-- [end:show_train_stats] -->

<!-- --8<-- [start:show_exit_direction] -->
#### Show exit direction

Whether the display should indicate on what side of the train you can exit when it aproaches a station.  
The indicator will be an arrow on the same line where the `Next Stop:` text will appear.
<!-- --8<-- [end:show_exit_direction] -->

<!-- --8<-- [start:show_next_connections] -->
#### Show next connections

Whether the display should list trains that also stop at the same station.  
This will include all train stations that are part of a Station Tag.
<!-- --8<-- [end:show_next_connections] -->

<!-- --8<-- [start:show_train_multiple_times] -->
#### Show train multiple times

Whether to show Trains aproaching the same Station (tag) multiple times (i.e. once in one direction and again in another) or if each train should only be shown once.
<!-- --8<-- [end:show_train_multiple_times] -->

<!-- --8<-- [start:train_text_components] -->
#### Train Text Components

Sets what Text Components should be displayed.  
Default is `Train Name only` but can be changed to `Destination only` and `All`.

Should the text component be too long to show will the text scroll.
<!-- --8<-- [end:train_text_components] -->

<!-- --8<-- [start:train_stop_display_type] -->
#### Train Stop Display Type

Sets the display type for the Train Stop.

| Type                   | Description                                                                    |
|------------------------|--------------------------------------------------------------------------------|
| `All`                  | Display Arrivals and Departures.                                               |
| `Arrivals only`        | Only display Trains arriving at the station.                                   |
| `Arrivals preferred`   | Display Arriving trains where possible, but fall back to departures otherwise. |
| `Departures only`      | Only display Trains departing from the station.                                |
| `Departures preferred` | Display departing trains where possible, but fall back to arrivals otherwise.  |
<!-- --8<-- [end:train_stop_display_type] -->

<!-- --8<-- [start:show_time_and_date] -->
#### Show time and date

Whether the display should also display the current ingame Time and date (number of ingame days since world creation).
<!-- --8<-- [end:show_time_and_date] -->

<!-- --8<-- [start:departure_text_width] -->
#### Train Name Width

Sets the max width for displaying Train Names.  
Any text longer than the configured width will scroll.

#### Platform Width

Sets the max width for displaying the Platform.  
Any text longer than the configured width will scroll.

#### Stopovers Section Width

Sets the remaining percentage of the screen width that should be used to display Stopovers.

#### Info Section Width

Sets the remaining percentage of the screen width that should be used to display Info.
<!-- --8<-- [end:departure_text_width] -->

<!-- --8<-- [start:text_input] -->
#### Text input

This field allows to input custom text that should be displayed.  
The field supports normal strings, but can also accept JSON Message Components for further customization to be used.
<!-- --8<-- [end:text_input] -->

<!-- --8<-- [start:text_alignment] -->
#### X Position

Sets the position on the X axis (horizontally from the left) in block pixel.  
This option is influenced by the text alignment.

#### Y Position

Sets the position on the Y axis (vertically from the top) in block pixel.

#### Text Alignment

Sets how the text should be aligned.  
Available options are `Left Aligned Text`, `Centered Text` (default) and `Right Aligned Text`.
<!-- --8<-- [end:text_alignment] -->

<!-- --8<-- [start:text_scale] -->
#### Minimum X Scale

Sets the minimum width in relation to screen width that the text should have.  
Should it not be possible will the text scroll or get cut off, depending on what has been configured.

Min value is `10%` and max is `75%` which is also the default.

#### X Scale

The maximum width in relation to screen width that the text should have.  
Should it not be possible will the text scroll or get cut off, depending on what has been configured.

#### Y Scale

The maximum height in relation to screen height that the text should have.  
Should it not be possible will the text scroll or get cut off, depending on what has been configured.
<!-- --8<-- [end:text_scale] -->

<!-- --8<-- [start:text_width] -->
#### Text Max Width

The max width in block pixels that the text should have.  
This option is limited by the display's actual display width.

#### Boundary behavior

How the text should be treated when it goes beyond the configured boundaries.  
Default is `Scale/Scroll` which tries to scale the text and eventuall scrolls it, but can be set to `Cut Off` and `Always Scroll`
<!-- --8<-- [end:text_width] -->

<!-- --8<-- [start:label_background] -->
#### Label Background Color

Sets a separate background color independant of the currently configured one.  
By default does it only cover the width and height of the text, but enabling `Full Size` will cover the full configured area of the text.
<!-- --8<-- [end:label_background] -->