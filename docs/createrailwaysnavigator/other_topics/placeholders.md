# Placeholders

On [[Advanced Displays]] with static text you can use various placeholders to display all kinds of data. Placeholders are always enclosed in `%`, e.g. `%time%`.

/// note
`n` is the index of the entry, starting with `0`. `0` = the first entry (e.g. the next train), `4` = the 5th entry (e.g. the 5th next train) and so on.
///

## Generic placeholders

These placeholders always work.

- `time` - the current in-game time of day
- `day` - the current in-game day

## On-board placeholders

These placeholders only work on assembled trains. For some of them, the train must also be in service.

- `via` - a comma separated list of all stopovers
- `line` - the train name or, if defined, the line name
- `carriages` - the amount of carriages this train has
- `origin.` where the train started its journey **OR**

    `destination.` where the train will end its journey **OR**

    `next.` the next stop, includes the destination **OR**

    `stopN.` the following stops, where `N=0` is the next stop, excludes the destination,
    
    followed by:

    - `station_name` - the arrival station
    - `platform` - the arrival platform number
    - `arrival` - arrival time in in-game `hh:mm` format
    - `departure` - departure time in in-game `hh:mm` format
    - `arrival_eta` - arrival time as an eta
    - `departure_eta` - departure time as an eta

## Station placeholders

These placeholders only work on displays in the world. For some of them, the train must also be in service.

- `trainN.`, followed by:
    - `station_name` - the arrival station
    - `platform` - the arrival platform number
    - `arrival` - arrival time in in-game `hh:mm` format
    - `departure` - departure time in in-game `hh:mm` format
    - `arrival_eta` - arrival time as an eta
    - `departure_eta` - departure time as an eta
    - `via` - a comma separated list of all stopovers
    - `line` - the train name or, if defined, the line name
    - `origin` - where the train started its journey
    - `destination` - where the train will end its journey
    - `carriages` - the amount of carriages a train has
    - `stopN` - the following stops, where `N=0` is the next stop
