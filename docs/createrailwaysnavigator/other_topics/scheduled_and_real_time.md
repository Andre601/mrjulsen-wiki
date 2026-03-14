# Scheduled Time and Real Time

There are two types of times: scheduled times and real-time data. The scheduled time is calculated at a specific point from the real-time data available at that moment and then stored as a reference value for delays, dynamic waiting times, etc.

## Total duration calculation
CRN constantly measures the time that trains need to travel from one station to another and stores this as a reference value for the total journey duration of a train. If the time in the same section of the route between two stations deviates too often from the current reference value (default: 3x, can be changed in the config), this will get included in the timetable and the total journey duration of the train.

## Automatic timetable adjustment
In order to prevent permanent delays and to adjust the timetables to the current real-time values, the train travel times are updated regularly. The real-time data at that moment is then set as the new scheduled time as a reference value.
The automatic adjustment is triggered when:
- the train changes its total journey duration
- the world/server is restarted
- the train receives a new train schedule or is newly put into operation
- after each schedule section (if the train does not use dynamic delays)
- after every X schedule sections (if the train uses dynamic delays and this has not been deactivated in the config)
- never (if the train uses dynamic delays and this has been deactivated in the config) (not recommended)