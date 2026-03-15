---
categories:
  - Create Railways Navigator
---

# Train Schedule Features

Create Railways Navigator adds a few features to the [[c:Train Schedule]] of Create to allow more customization of a Train and Train Routes.

## New Schedule Section

**Type:** Action

The **New Schedule Section** allows you to define a Train's category and line number from the Global Settings.  
It also allows to set, whether stations from the next section should be included in any advanced Displays on the Train and if it should be searchable by the Navigator.

## Prioritized Destination

**Type:** Action

The **Prioritized Destination** allows you to set a list of stations the Train should target.  
Unlike Glob Patterns in **Travel to Station** Actions, which result in a more or less random selection, does this Action allow to set a specific order of Stations. The train will try to target the first station and if not successful, move on to the next entry, repeating as necessary.  
Glob patterns are still supported in Station names, if necessary.

Additionally can it be configured to avoid red signals and other trains when determaning the Station to target.

## Dynamic Delay

**Type:** Condition

The **Dynamic Delay** allows to configure minimum and maximum waiting time for a Train to wait.  
If a train is delayed (behind its calculated schedule) will it only wait the minimum time, where it otherwise will wait for the maximum time.

This allows you to have a train "catch up" if it fell behind its normal schedule.

## Train Separation

**Type:** Condition

The **Train Separation** allows you to better distribute trains of a route for a more consistent timetable.  
The configured time determines how long a train should remain at the station. If its travel time to the station was less than the configured time, will it wait until it was reached, at which point it will continue to the next task in its Schedule.

Unlike other conditions does this one not execute immediately and instead *wait* until the specified time passed. Any other Conditions will be executed, so the order does not matter.

A Train Filter can be set to include trains of the same line, category, name or without any criteria.  
Additionally can a Train Station be defined as filter for the actual separation. This defaults to the configured Station for the **Travel to Station** configured.