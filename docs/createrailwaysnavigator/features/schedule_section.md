# Schedule Section

Schedule sections allow you to divide a train's schedule into several small parts. For each of these sections, you can then define your own settings that influence the navigation and behavior of the train. This feature also allows to specify the final stop by yourself that should be shown on the displays or in the navigator as the train destination.

## Usage
Train sections are defined in the schedule and must always be added **before** the first stop of a section. If the first stop is also the last stop of the previous section, the `Include start of next section` option must be enabled in the previous section's settings.

#### Example
In the following route:
`A B C D E F G`
- **There should be a section with `A B C` and `D E F G`.**

    In this case, a new section must be created before `A` and `D` without any further settings. It is important to note that there won't be o train connection between `C` - `D` or `G` - `A`, as they are not in any section. Since `C` is the final stop and `D` is the beginning, you cannot get from `C` to `D`.

- **To avoid this problem, you can include `D` in both sections. So you now have a section `A B C D` and `D E F G` (`D` is both, the final stop and the start).**

    The new section must be defined **before** `D` (because `D` should be the first stop) and the `Include start of next section` option must be enabled in the previous section so that `D` is included in the previous section as the final stop as well. Since `D` is now the start and the end at the same time, you can navigate via the station, although a transfer is necessary, since the train ends in `D` (because it starts a new section there).

If you want to do the same with `G` - `A` (so that `A` is the final stop and the start) the entry for this section must be created before `A` or after `G`. 

## Exclude train sections
You can also use sections to hide trains (e.g. when driving to the depot). To achieve this, simply create a new section and deactivate the `Navigable` option. If you want the train to be usable again, create a new section before the first stop with `Navigable` activated.

## Train Groups and Train Lines
When entering a new schedule section, train groups and train lines can be assigned to the trains, which then change the appearance of it. More details about these two features on their respective help pages.

## Default behaviour
In schedules that do not define their own sections, there is still a default section that is added internally at the very beginning and with the option `Include start of next section` turned on. Trains without sections show the first stop in the train schedule as the first stop and the final stop.
