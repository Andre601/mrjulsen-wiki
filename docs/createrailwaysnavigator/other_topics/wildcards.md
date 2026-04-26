---
categories:
  - Create Railways Navigator
---

# Wildcards & Glob Patterns

Wildcards (`*`) and Glob Patterns (i.e. `[1-3]`) are placeholders that can be used to represent any number of characters, a range of specific characters or specific character (sets).  
Note that Glob Patterns are only supported for Create 6 and CRN 0.9.0 and newer.

## Examples

/// note
These examples are about wildcards and Glob Patterns in [[c:Train Schedule|Train Schedules]]. The same applies to display links and other places supporting these.
///

The following examples assume the following Data sources: `Station 1`, ` Station 2`, `Station 3b`, ` Station4`, `Depot 5`, ` My Station 6`

### No Wildcard/Glob Pattern

If we write `Station 1`, the train only travels to a Train Station named `Station 1`, since the names match.

### Wildcards

If you want to allow the train to have the choice between several destinations, you can write `Station *`.  
All Stations whos name starts with `Station` (Including the space!) are valid, meaning `Station 1`, `Station 2` and `Station 3b` are selectable.

- `Station4` is not valid due to not having a space between `Station` and the number. `Station*` would consider this name valid too.
- `Depot 5` is not valid due to its name not starting with `Station`.
- `My Station 6` is not valud due to its name starting with `My` and not `Station`.

### Glob Patterns

Glob Patterns are similar to [Wildcards](#wildcards) but allow a higher level of selection when defining any.

/// details | Supported Patterns
    type: info

| Pattern  | Description                                                                                        |
|----------|----------------------------------------------------------------------------------------------------|
| `?`      | Matches any single character                                                                       |
| `[...]`  | Matches any single character defined in between the square brackets                                |
| `[x-y]`  | Matches any single character defined in the provided range (i.e. `0-9` for any digit from 0 to 9)  |
| `[!...]` | Matches any single character **not** defined in between the square brackets                        |
| `{...}`  | Matches any text defined in-between the curly brackets (Each word is separated by a comma)         |
| `{!...}` | Matches any text **not** defined in-between the curly brackets (Each word is separated by a comma) |
///

As an example, if we want to target any Station named `Station <number>` with `<number>` being any single digit and not text, we can use `Station [0-9]`.  
This means `Station 1`, and `Station 2` are valid selections for the Train.

- `Station 3b` is not valid as it also contains `b` rather than just a digit.
- `Station4` is not valid due to not having a space between `Station` and the number. `Station{ [0-9],[0-9]}` would consider this name valid too.
- `Depot 5` is not valid due to its name not starting with `Station`.
- `My Station 6` is not valud due to its name starting with `My` and not `Station`.

## Further Examples

| Pattern      | Valid Entries                                      |
|--------------|----------------------------------------------------|
| `Station *b` | `Station 3b`                                       |
| `S*n*`       | `Station 1`, `Station 2`, `Station 3b`, `Station4` |
| `*5`         | `Depot 5`                                          |

## Additional Resources

The [Create Glob Tester](https://tobi-blackscale.github.io/Create-Glob-Tester/GlobRegExTest.html){ target="_blank" rel="nofollow" } can be used to create and test Glob Patterns for Create.
