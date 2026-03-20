---
categories:
  - Create Railways Navigator
---

# Wildcards

Wildcards (`*`) are placeholders for any number of characters in a text. All entries from a data source are valid that matches the corresponding pattern.

## Example

/// note
This example is about wildcards in Train Schedules. The same applies to display links and other uses of wildcards.
///

We have a data source: `Station 1`,` Station 2`, `Station 3b`,` Station4`, `Depot 5`,` My Station 6`

If we now write `Station 1`, the train only drives to a train station called `Station 1`, since the names match.

If you now have several stations (see data source) and want the train to have the choice between several destinations, you can write `Station *`. All stations are valid of which the name begins with `Station ` (with spaces!) and then contains any amount of characters (represented by the `*`). In this case only: `Station 1`, `Station 2`, `Station 3b`.

- `Station4` is not valid because the pattern is `Station *` is (with spaces) and `Station4` doesn't contain any spaces after `Station`. With the pattern `Station*` (without spaces), this entry would be valid.
- `Depot 5` is not valid because the text does not start with `Station `.
- `My Station 6` is not valid, since there is `My ` in front of the `Station` text. With the pattern `* Station *` (or `*Station*`) this entry would be valid.

Other examples are:

| Pattern | Valid Entries |
| - | - |
| `Station *b` | `Station 3b` |
| `S*n*` | `Station 1`, `Station 2`, `Station 3b`, `Station4` |
| `*5` | `Depot 5` |