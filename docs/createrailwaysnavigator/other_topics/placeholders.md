---
categories:
  - Create Railways Navigator
---

# Placeholders

On [[Advanced Displays]] with static text you can use various placeholders to display all kinds of data. Placeholders are always enclosed in `%`, e.g. `%time%`.

/// note | Notes
- With the exception of `time` are all placeholders here only available in `Beta-0.9.0` and newer!
- `n` is the index of the entry, starting with `0`. `0` = the first entry (e.g. the next train), `4` = the 5th entry (e.g. the 5th next train) and so on.
///

## Generic placeholders

These placeholders always work.

- `time` - the current in-game time of day
- `day` - the current in-game day

## On-board placeholders

These placeholders only work on assembled trains. For some of them, the train must also be in service.

- `title` - the schedule title, if set, otherwise the destination
- `via` - a comma separated list of all stopovers
- `via:<delimiter>` - a list of all stopovers with a custom delimiter (separator)
- `line` - the train name or, if defined, the line name
- `carriages` - the amount of carriages this train has
- `origin.<option>` - see [Stopover options](#stopover-options) for options
- `destination.<option>` - see [Stopover options](#stopover-options) for options
- `next.<option>` - see [Stopover options](#stopover-options) for options
- `stopN.<option>` - see [Stopover options](#stopover-options) for options

## Station placeholders

These placeholders only work on displays in the world. For some of them, the train must also be in service.

- `trainN.<option>`, available options are as follows:
    - any option under [Stopover options](#stopover-options)
    - `via` - a comma separated list of all stopovers
    - `via:<delimiter>` - a list of all stopovers with a custom delimiter (separator)
    - `line` - the train name or, if defined, the line name
    - `origin` - where the train started its journey
    - `destination` - where the train will end its journey
    - `carriages` - the amount of carriages a train has
    - `stopN` - the following stops, where `N=0` is the next stop
    - `delay_reason` - the reason for the delay

## Stopover options

- `station_name` - the arrival station
- `platform` - the arrival platform number
- `arrival` - arrival time in in-game `hh:mm` format
- `departure` - departure time in in-game `hh:mm` format
- `arrival_eta` - arrival time as an eta
- `departure_eta` - departure time as an eta
- `delay_time` - the train delay as formatted text

## Elevator placeholders

These placeholders only work on elevators.

- `elevator.<option>`, available options are as follows:
    - `current.short` - short name of the current floor eg. `0`
    - `current.long` - long name of the current floor eg. `Main Lobby`
    - `destination.short` - short name of the floor the elevator is heading to, eg. `21`
    - `destination.long` - long name of the floor the elevator is heading, eg. `Gym`
    - `sign` - arrows indicating if the elevator is moving up or down
    - `sign.triangle` - the same thing as above but using a different pair of characters.
