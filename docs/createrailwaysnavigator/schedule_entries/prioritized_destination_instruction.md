---
categories:
  - Create Railways Navigator
  - Create Railways Navigator/Schedule Feature
---

# Prioritized Destination Instruction

This is an instruction for the [[c:Train Schedule]] of Create.

The Prioritized Destination Instruction is similar to wildcards in the Destination Instruction, with the difference that you can define a precise order the train should attempt to select stations from.  
Wildcards can often time create random selections due to the Train trying to take the route with the least obstacles (See [the Penalty System in the Penalty Anchor page](../blocks/penalty_anchor.md)). With this instruction can you create a list of Stations to prioritize.  
The first available station in the list will be selected to route towards.

/// tip
You can also use wildcards for the entries. If such an entry is then used as the destination, all stations that match the pattern can be accessed (just like normal). This feature is a good fallback option if there is nothing better available.
///

## Additional options
- **Avoid other trains**

    If this option is active, the next entry will be used in the list if the current target station is blocked by another train. If the end of the priority list is reached, the train selects the last option of the list and then waits if necessary.

- **Avoid red signals**
    
    If this option is active, the next entry will be used in the list if there is a red signal on the route to the selected target station. The signal must be set to red by redstone! If the signal is red due to another train and the `Avoid other trains` option is deactivated, the train will still select this target and then waits in front of the red signal.

## Edit the priority list
The entries can be reordered by drag and drop. The top entry has the highest priority and is chosen first. The next entry of the list is only selected if the current station is not possible due to the selected options and other circumstances.
