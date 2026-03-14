# Station Tag

Station tags can be used for grouping several train stations with a custom display name. They are also essential for navigation between different trains at stations with multiple platforms. All train stations in a station tag are considered as one single station with the name of the tag.
Station tags can be created in the `Global Settings`. There you can then add the train stations (by their name) and a custom platform number/name.

/// warn
If a train station is renamed, these changes are not automatically reflected in the station tags and the renamed station may no longer be part of the station tag (if the new name is not added there). Since several train stations can have the same name, ALL train stations with the same name will be part of the station tag.
///

While station tags or the platform names of individual stations can be changed at any time, renamed train stations must be added again and the old entry removed accordingly. Train station can only be added in the global settings and not in the corresponding train station block or anywhere else.

/// warn
If you delete a station tag and create it again with the same name, all settings in which this station tag was selected will no longer be able to use it. This is because the ID of the tag and not the name is stored internally.
///

## Example
Let's assume there is a train station with the stations `MyStation 1`, `MyStation 2`, `MyStation 3`. Then you can create a station tag so that CRN can suggest transfers between these three platforms. The station tag could be called `My Train Station` and would contain the individual stations with custom defined platform number.


/// note
Please note that (unlike in Create) the platform name must be specified manually and cannot be determined using wildcards in the station name.
///