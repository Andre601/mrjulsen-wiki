# Prioritized Destination Instruction

This is an instruction for the [[c:Train Schedule]] of Create.

The Prioritized Destination Instructation is similar to wildcards in the Destination Instruction, with the difference that you can decide at which stations the train can arrive and in what order the stations should be selected. Wildcards are often very random because the train selects the best way and can not properly predicted in many cases in large stations. With this instruction you can create a list of priorities containing all the desired stations. You can even combine stations that are not possible with wildcards because they have a completely different name. The first available station will be chosen.

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