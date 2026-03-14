# Dynamic Delay

This is a condition for the [[c:Train Schedule]] of Create.

Dynamic delays work in a similar way to Create's wait delays. The difference is that a minimum waiting time can be set.

Since trains can now officially be delayed, the problem arises that trains can never compensate their delays, since they cannot travel faster and have always the same waiting time at the stations.

Dynamic delays, on the other hand, provide some buffer time and simply allow a delayed train to depart earlier to compensate the delay, until the minimum waiting time is reached. In addition, trains that arrive too early simply wait longer at the station so that they can then depart on time at the scheduled time.

/// warn
As soon as one dynamic delay exists in the schedule with a buffer time `> 0`, the travel times are no longer automatically updated after each section. If used incorrectly, this can result in permanent delays that a train cannot compensate.
///

/// tip
The larger the rail network, the longer buffer times should be planned with the dynamic delays in order to prevent permanent delays. For example, in a large network, a stay of several minutes buffer time could be planned in the depot.
///