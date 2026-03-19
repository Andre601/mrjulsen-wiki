# Global Settings

The Global Settings are (as the name suggests) settings for Create Railways Navigator that apply globally to the entire server/world and not to individual trains or stations. The settings there are then used for navigation or the displays. Since these settings can fundamentally impact the behavior of CRN, you can change the [[mc:permission level]] required to change these settings in the `common-config` of the server.
Details about the various options in the Global Settings can be found in the individual help pages.
The Global Settings can be accessed wherever they are needed. For example, in the Navigator, the display settings, etc.

## Add multiple entries at once
To make work easier, wildcards and globs can be used to add several entries at once that match the pattern. This works with station tags, all blacklists and Train Lines/Categories.

**Example:**

Data source: `Station 1`, `Station 2`, `Station 3b`, `Station4`, `Depot 5`, `My Station 6`

The pattern `Station *` adds the entries `Station 1`, `Station 2`, `Station 3b` to the list.

## Wildcards in Station Tags
There is an additional feature for Station Tags that the wildcards in the station string can be used to automatically set the platform string.
So you can write `Station *` / `Pl. *` or simply `Station *` / `*`

-   For each element from the data source that matches the station string pattern, the text, which is represented by the placeholder, is inserted into the placeholder of the platform string.  
    Example: `Station *` / `Pl. *` will result in `Station 1` / `Pl. 1`, `Station 2` / `Pl. 2`, `Station 3b` / `Pl. 3b`
-   In the case of multiple wildcards, the text parts of the individual placeholders in the station string are individually inserted into the placeholders of the platform string in the same order. Placeholder 1 goes in placeholder 1, 2 in 2, etc.  
    Example: `St*n *` / `* Pl. *` will result in `Station 1` / `atio Pl. 1`, `Station 2` / `atio Pl. 2`, `Station 3b` / `atio Pl. 3b`
-   If the platform string has less placeholders than the station string, all remaining text parts are inserted into the last placeholder in the platform string.  
    Example: `St*n *` / `Pl. *` will result in `Station 1` / `Pl. atio1`, `Station 2` / `Pl. atio2`, `Station 3b` / `Pl. atio3b`
-   If the station string has less placeholders than the platform string, all remaining placeholders in the platform string will be removed.  
    Example: `Station *` / `* Pl. *` will result in `Station 1` / `1 Pl.`, `Station 2` / `2 Pl.`, `Station 3b`, `3b Pl.`