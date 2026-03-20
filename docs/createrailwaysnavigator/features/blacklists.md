---
categories:
  - Create Railways Navigator
  - Create Railways Navigator/Settings
---

# Blacklists

Blacklists are used in CRN to hide certain information from navigation or displays.

## Station blacklist

This list contains all train stations that should not be used in the navigation or route calculation. However, trains that have these stations in their schedule are still suggested and displayed. The stations are just ignored in the route and it is not possible to get on, off or transfer there. This feature is useful for hiding stations that are not intended for passenger rail transport or that fulfill a technical function, e.g. stations in depots, waypoints, etc.

## Train blacklist

This list contains all trains that should not be shown in the navigation or on the displays. The navigator does not suggest routes that require these trains and acts as if they don't exist at all. This feature can be used for all train contraptions that should not be part of the passenger rail network, e.g. freight trains, construction trains, etc.

/// warning
Stations and trains are excluded by their name, which means that all other stations and trains with the same name will be excluded as well! If this is a problem, use different names for the stations and trains you want to exclude.
///