# Permissions

Some entries in the global settings (e.g. Station Tags, Train Lines) can be protected for modifications with permissions. This might be useful for larger servers to prevent players from editing settings of other players and causing problems. Server Owners can restrict the permissions to operators only, which means that players cannot change any of to the global settings.

## Ownership
The player who creates a new entry has the ownership and full control over this entry. The owner can limit the permissions for other players and decide exactly who should have access to it. This player also has the opportunity to transfer his ownership to another player or the server. Entries that belong to the server can only be managed by operators according to the settings in the Common Config.

## Change permissions
By clicking on the Lock icon, the entry can be locked or unlocked. Locked entries can only be changed by the owner, trusted players or server operators. Only the owner or server operators can change the permissions.

## Trusted Players
A list of players who are allowed to make changes to this entry. They cannot change permissions.

## Admin Mode
All players who meet the permission level defined in the config. These players can edit any entry (even the permissions), regardless of whether it is blocked or who owns it. A minimum permission level of `0` (not recommended!) means that the permissions system is deactivated. A permission level of `-1` prevents everybody to edit the settings (even operators/server owners).

## Global Settings Read only Mode
If access to the global settings is deactivated in the config, players can still view them in read only mode. However, they cannot make any changes, even if they are owners of entries.

## Updating from older version
If the global settings were created in an older mod version, the existing entries automatically belong to the server. Operators can transfer the ownerships to their respective players.