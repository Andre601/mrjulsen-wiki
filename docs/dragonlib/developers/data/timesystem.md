---
categories:
  - DragonLib
---

# Time System
To ensure compatibility with mods that modify the in‑game time, DragonLib provides not only simple configuration options but also the ability to fully customize the time system through datapacks. DragonLib already includes support for several time‑altering mods (such as Time Control), but not all of them. If no built‑in support exists, you can define your own configuration using a datapack.

!!! warning
    This configuration and the `DLTime` class cannot directly change the time in Minecraft, they only adjust the calculations in DragonLib to reflect the changes made by external mods. Therefore, time-changing mods must be installed. If no such mod is installed and these values ​​are changed, the calculations may be wrong and display incorrect times.

## Configuration File
To create a custom time configuration, add the following file to your datapack. This file contains all settings related to the time system:

```txt
data/dragonlib/config/time_system.json
```

## Structure
The structure of the file is shown below using the default Vanilla configuration as an example:

```json
{
  "ticks_per_day": 24000,
  "daytime_offset": 6000,
  "zones": [
    {
      "start_tick": 0,
      "end_tick": 24000,
      "tps": 20.0
    }
  ]
}
```

## Field Descriptions

- `ticks_per_day`: The number of ticks that a full Minecraft day/night cycle lasts.

- `daytime_offset`: The number of ticks by which the daytime value is shifted. In Vanilla, tick 0 (and 24000) corresponds to 06:00 AM. Since the day typically transitions at midnight, the time must be shifted by 6 hours. With a 24‑hour day lasting 24000 ticks, this results in an offset of 6000 ticks.

- `zones`: Some time‑altering mods allow day and night to progress at different speeds. Using time zones, you can define different tick speeds for different parts of the day — for example, slower during daytime (0–12000) and faster at night (12000–24000).


Each `zone` contains:

- `start_tick`: The tick of the day at which this zone becomes active (without applying `daytime_offset`).

- `end_tick`: The tick of the day at which this zone stops being active (without applying `daytime_offset`).

- `tps`: The tick speed in TPS (ticks per second).

!!! warning "Please note!"
    - The `start_tick` and `end_tick` values refer to Minecraft’s raw daytime ticks, not the shifted time using `daytime_offset`. This means the day always begins at tick 0 = 06:00 AM, which matches the example above.
    - Time zones must cover the entire day. If there is any gap between zones, time will stop during that period.
    - Time zones cannot cross midnight. A zone like `start_tick`: 18000 (evening), end_tick: `12000` (next day noon) is invalid. Instead, you must split it into two separate zones.
    - Zones that exceed the maximum day length (`ticks_per_day`) are ignored. For example: If Zone 1 starts at tick 6000 and Zone 2 ends at tick 30000, Zone 2 will automatically end at tick 24000 (day reset). Since Zone 1 only starts again at tick 6000, time will stand still between tick 24000 and 6000.

## Custom time system example
```json
{
  "ticks_per_day": 24000,   // Default ticks per day (one day lasts 24000 ticks)
  "daytime_offset": 6000,   // Default offset (tick 0 is midnight)
  "zones": [
    {                       // DAY TIME
      "start_tick": 0,      // morning, 06:00 AM
      "end_tick": 12000,    // evening, 06:00 PM
      "tps": 10.0           // tickspeed of 10 ticks per second
                            //   -> slower day progression
                            //   -> 20 min per day
    },
    {                       // NIGHT TIME
      "start_tick": 12000,  // evening, 06:00 PM
      "end_tick": 24000,    // next day morning, 06:00 AM
      "tps": 40.0           // tickspeed of 40 ticks per second
                            //   -> faster night progression
                            //   -> 5 min per night
    }
  ]
}
```