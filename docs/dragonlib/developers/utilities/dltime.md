---
categories:
  - DragonLib
---

# DLTime

This class simplifies working with time in Minecraft. It helps convert in-game time to real-world time and vice versa. Furthermore, its configuration options also offer support for time-changing mods, which can, for example, alter the tick speed.

## Concepts overview

The following classes are relevant:

- DLTime: immutable absolute moment or duration stored internally as real-world milliseconds (double).
- ITimeSystem: maps "game ticks" and game-relative units to real milliseconds. Defines ticks-per-day, time zones (variable TPS), and an optional daytime offset.
- TimeZone: contiguous segment of the in-game day with its own ticks-per-second (tps). Used to model variable tick lengths.
- DLTimeUnit: enumerates MILLIS, SECONDS, MINUTES, HOURS, DAYS, TICKS. Real units carry a `millis` factor; TICKS convert via ITimeSystem.
- Formatters: multiple ITimeFormatter implementations produce human-readable strings (digital, verbose, ISO8601, ticks-only, 12/24 hour time).
- TimePool: mutable budget container measured in real milliseconds; supports extracting whole units.
- DLTimeApi: registry to register/resolve mod compatibility time systems.

## Example: basics and conversions

Create DLTime from real units:
```java
DLTime t1 = DLTime.fromReal(2.5, DLTimeUnit.SECONDS); // 2500 ms
```

Create from game ticks or game seconds (requires an ITimeSystem):
```java
ITimeSystem system = DLTime.defaultTimeSystem(); // resolved system (datapack/config/vanilla)
DLTime t2 = DLTime.fromGameTicks(24000.0, system); // one full game day
DLTime t3 = DLTime.fromGameSeconds(30.0, system);  // 30 game-seconds
```

Convert DLTime to ticks/seconds using a system:
```java
double ticks = t1.toTicks(system);
double gameSeconds = t1.toGameSeconds(system);
```

Use Builder for compound construction:
```java
DLTime built = DLTime.builder()
    .real(500, DLTimeUnit.MILLIS)
    .gameMinutes(3, system)
    .build();
```

---

## Time systems

- VanillaTimeSystem: singleton for vanilla behaviour (24000 ticks/day, 20 TPS).
- ConfiguredTimeSystem: singleton that reads values from ModCommonConfig; useful to reflect server config.
- DatapackTimeSystem: parsed from a datapack JSON defining ticks_per_day, daytime_offset and zones; validates ranges and produces immutable zones list.

!!! tip
    For datapacks, please read [this page](../data/timesystem.md).

### Default resolution
`DLTime.defaultTimeSystem()` uses a TTL-cached resolver that may prefer datapack definitions, mod compatibility providers (DLTimeApi) or fall back to configured/vanilla systems based on server config.

---

## TimeZone: variable TPS

A `TimeZone` describes [startTick, endTick) with a `tps` value. Use it to model days where tick duration varies (e.g., slow night ticks). ITimeSystem default implementations iterate zones for conversions.

---

## Formatting time

Formatters implement ITimeFormatter and accept a DLTime, TimeContext (INGAME or REAL) and an optional ITimeSystem for INGAME:

- TimeFormatDigitalDuration – colon-separated HH:MM:SS style; configurable minimum unit and fractional part.
- TimeFormatVerboseDuration – verbose human-readable (e.g. "1d 3h 12m 5s"); configurable fields.
- TimeFormatTicks – shows ticks (e.g. "123t").
- TimeFormatISO8601 – ISO-8601 style (P...T...).
- TimeFormat24Hours / TimeFormat12Hours – render time-of-day given a system.

Example:
```java
String digital = TimeFormatDigitalDuration.DEFAULT_REAL_INSTANCE.format(t1, TimeContext.REAL, null);
String verbose = TimeFormatVerboseDuration.DEFAULT_INSTANCE.format(t2, TimeContext.INGAME, system);
```

---

## DLTimeOfDay: wrap-aware daily comparisons

Convert absolute DLTime to DLTimeOfDay to reason about daily intervals that may cross midnight:
```java
DLTimeOfDay now = new DLTimeOfDay(currentTime, system);
boolean isBetween = now.isBetween(new DLTimeOfDay(start, system), new DLTimeOfDay(end, system));
```

---

## TimePool: consuming time budgets

TimePool holds remaining real milliseconds and supports extracting whole units (real or game units via a system). Extraction mutates the pool.

Example:
```java
TimePool pool = new TimePool(DLTime.fromReal(5000, DLTimeUnit.MILLIS));
long seconds = pool.extractSeconds(); // consumes seconds from the pool
```

---

## DLTimeApi: mod compatibility

Other mods can register an ITimeSystem supplier:
```java
DLTimeApi.registerCompat("othermod", () -> new OtherModTimeSystem());
```
DLTime.defaultTimeSystem() may pick a compat system based on ModServerConfig.PREFERRED_MOD or automatic detection.

---

## Best practices & notes

When working with in-game time, an `ITimeSystem` object must always be specified to determine the time mapping. Even though it's possible to define a fixed time system manually, it's recommended to use the value from `DLTime.defaultTimeSystem()`. This method selects the appropriate time system based on the mod configuration, datapacks, and installed time mods. Of course, if you're working with times that aren't affected by such mods (e.g., furnace tick speed), the vanilla system should be used.

- Prefer expressing durations explicitly (DLTime.fromReal, fromGameTicks) instead of relying on now()-style helpers.
- When converting between real and game units, always pass an appropriate ITimeSystem to avoid ambiguity with ticks.
- Datapack time systems should ensure zones cover the full day and contain valid ranges.
- Formatting in INGAME context requires a non-null ITimeSystem.
