# Train separation

This feature allows the trains on a route to be better distributed in order to create a consistent frequency.
This condition can be selected and configured in a destination instruction in the train schedule. Unlike other conditions, this one is not executed immediately when the other conditions are processed while waiting at a station, but when the train would actually depart again. So the order doesn't matter and doesn't affect other conditions. By subsequently processing this condition, a train behaves as if it were standing in front of a red signal at a train station. The travel time between the current and the next station is measured while waiting, which is helpful so that the train can adjust its total journey time in order to prevent permanent delays that can arise from incorrect configuration.

## Setup
When editing the condition, a time period can be specified that indicates the time interval by which the train should depart after the previous train (in real life or in-game time). The Train Filter option can be used to select whether the train should depart after the departure of any other train, or whether only trains from the same train line or train group should be taken into account. This means you can also use the feature on routes that are served by different lines without other trains influencing the timing.

/// note
Time is calculated using game ticks. Bad TPS may extend the time span, even if real-life time is used.
///

## Status and Departure History
With the Engineer's Goggles you can see when previous trains departed at a train station while looking at it. The data is updated every 5 seconds, so watch a little longer if nothing is displayed or the data appears incorrect.