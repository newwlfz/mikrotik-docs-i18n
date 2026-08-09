# User

> MikroTik RouterOS User management page details user authentication via local or RADIUS servers, password complexity settings, user group policies defining access rights, and router user database properties including login addresses, inactivity actions, and password management.

# User

## Summary

MikroTik RouterOS router user facility manages the users connecting to the router from any of the Management tools. The users are authenticated using either a local database or a designated RADIUS server. Each user is assigned to a user group, which denotes the rights of this user. A group policy is a combination of individual policy items.

In case the user authentication is performed using RADIUS, the [RADIUS](./radius.md) client should be previously configured.

## User Settings

The settings submenu allows controlling the password complexity requirements of the router users.

| Property | Description |
| :-- | :-- |
| **minimum-password-length** (*integer*; 0..4294967295; Default: ) | Specifies the minimum character length of the user password |
| **minimum-categories** (*integer*; 0..4; Default: ) | Specifies the complexity requirements of the password, with categories being *uppercase, lowercase, digit, symbol.*  |

## User Groups

The router user groups provide a convenient way to assign different permissions and access rights to different user classes.

### Properties

| Property | Description |
| :-- | :-- |
| **name** (*string*; Default: ) | The name of the user group |
| **policy** (*local \| telnet \| ssh \| ftp \| reboot \| read \| write \| policy \| test \| winbox \| password \| web \| sniff \| sensitive \| api \| rest-api \| romon*; Default: **none**) | List of allowed policies:   Login policies: local - policy that grants rights to log in locally via consoletelnet - policy that grants rights to log in remotely via telnetssh - policy that grants rights to log in remotely via secure shell protocolweb - policy that grants rights to log in remotely via WebFig.winbox - policy that grants rights to log in remotely via WinBox and bandwidth test authenticationpassword - policy that grants rights to change the password for currently logged in user (own password) api - grants rights to access the router via API.rest-api - grants rights to access the router via REST API.ftp - policy that grants full rights to log in remotely via FTP.  Allows reading/writing/erasing files and to transfer files from/to the router. Should be used together with read/write policies.romon - policy that grants rights to connect to the RoMon server. Config Policies: reboot - policy that allows rebooting the routerread - policy that grants read access to the router's configuration. All console commands that do not alter the router's configuration are allowed. Doesn't affect FTPwrite - policy that grants write access to the router's configuration, except for user management. This policy does not allow reading the configuration, so make sure to enable read policy as wellpolicy - policy that grants user management rights. Should be used together with the write policy. Also allows seeing global variables created by other users (requires also 'test' policy). Allows designing skins (requires also "sensitive" policy).test - policy that grants rights to run ping, traceroute, bandwidth-test, wireless scan, snooper, fetch, email and other test commandssensitive - grants rights to change the "hide sensitive" option, if this policy is disabled sensitive information is not displayed.sniff - policy that grants rights to use the packet sniffer tool, torch tool, traffic generator. |
| **skin** (*name*; Default: **default**) | The skin used for WebFig |

### Default groups

There are three default system groups which cannot be deleted:

```ros
[admin@MikroTik] > /user/group/print 
0 name="read" policy=local,telnet,ssh,reboot,read,test,winbox,password,web,sniff,sensitive,api,romon,rest-api,!ftp,!write,!policy skin=default 

1 name="write" policy=local,telnet,ssh,reboot,read,write,test,winbox,password,web,sniff,sensitive,api,romon,rest-api,!ftp,!policy skin=default 

2 name="full" policy=local,telnet,ssh,ftp,reboot,read,write,policy,test,winbox,password,web,sniff,sensitive,api,romon,rest-api skin=default 
```

Please note, that even the "*read*" group includes *sensitive*, *reboot,* and other important policies, meaning that this group should not be given to untrusted users. For truly limited groups, make a custom group, defining specific policies. All groups have access to file operations. The exclamation sign '!' just before the policy item name means NOT.

## Router Users

The router user database stores information such as username, password, allowed access addresses, and group, about router management personnel.

### Properties

| Property | Description |
| :-- | :-- |
| **address** (*IP/mask \| IPv6 prefix*; Default: ) | Host or network address from which the user is allowed to log in |
| **group** (*string*; Default: ) | Name of the group the user belongs to |
| **inactivity-policy** (*lockscreen* \| *logout* \| *none*; Default: ***none***) | Specifies inactivity action - logout (the user will be logged out) or lockscreen (the session will be locked, requiring password input to continue). Works only for CLI sessions. |
| **inactivity-timeout** (*time*; Default: ***10min***) | Specifies time after which the user will be logged out or the session will be locked. Minimal timeout - 1 minute, maximal timeout - 24 hours. Works only for CLI sessions. |
| **name** (*string*; Default: ) | User name. Must start and end with an alphanumeric character but can include "\_", ".", "#", "-", and "@" symbols. However, the "\*" symbol is prohibited in the user name. |
| **password** (*string*; Default: ) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | User password. If not specified, it is left blank (hit <kbd>Enter</kbd> when logging in). It conforms to standard Unix characteristics of passwords and may contain letters, digits, "\*" and "\_" symbols. |
| **last-logged-in** (*time and date*; Default: **""**) | Read-only field. Last time and date when a user logged in. |

### Actions

Actions for an existing router user.

| Action | Description |
| :-- | :-- |
| **password** | Option to change the user password. |
| **expire-password** | Expires the user password, on the next login, the router will prompt to change the password. |

### Notes

There is one predefined user with full access rights:

```ros
[admin@MikroTik] /user> print
Flags: X - disabled
# NAME GROUP ADDRESS LAST-LOGGED-IN
0 ;;; system default user
admin full 0.0.0.0/0 2010-12-08 16:19:24

```

There always should be at least one user with full access rights. If the user with full access rights is the only one, it cannot be removed.

## Monitoring Active Users

```ros
/user/active/print
```

 The command shows the currently active users along with respective statistics information.

### Properties

All properties are read-only.

| Property | Description |
| :-- | :-- |
| **address** (*IP/IPv6 address/MAC address*) | Host IP/IPv6/MAC address from which the user is accessing the router. |
| **group** (*string*) | A group that the user belongs to. |
| **name** (*string*) | Username. |
| **radius** (*true \| false*) | Whether a user is authenticated by the RADIUS server. |
| **via** (*telnet \| ssh \| winbox \| api \| rest-api \| web \| ftp* ) | User's access method |
| **by-romon**(MAC address) | RoMON agent MAC address |
| **when** (*time*) | Time and date when the user logged in. |

### Request logout

It is possible to close an active session using the request logout function.

```routeros
 /user/active/request-logout ACTIVE_USER_SESSION_NUMBER
```

## Remote AAA

Router user remote AAA enables router user authentication and accounting via a RADIUS server. The RADIUS user database is consulted only if the required username is not found in the local user database.

### Properties

| Property | Description |
| :-- | :-- |
| **accounting** (*yes \| no*; Default: **yes**) | If the RADIUS server should be sent accounting for login, logout. Bandwidth usage statistics are not part of `/user` accounting |
| **exclude-groups** (*list of group names*; Default: ) | Exclude-groups consist of the groups that should not be allowed to be used for users authenticated by radius. If the radius server provides a group specified in this list, the default-group will be used instead. This is to protect against privilege escalation when one user (without policy permission) can change the radius server list, set up their own radius server and log in as admin. |
| **default-group** (*string*; Default: **read**) | User group used by default for users authenticated via a RADIUS server. |
| **interim-update** (*time*; Default: **0s**) | Interim-Update time interval |
| **use-radius** (*yes \|no*; Default: **no**) | Enable user authentication via RADIUS |

:::info
If you are using RADIUS, you need to have CHAP support enabled in the RADIUS server for WinBox to work.
:::

## SSH Keys

 This menu allows importing of private and public keys used for SSH authentication.

:::warning
By default, the user is not allowed to log in via SSH by password if an SSH key for the user is added. For more details see the [SSH](../management-tools/ssh.md) page.
:::

### Public keys

This menu is used to import (or add) and list imported public keys. Public keys are used to approve another device's identity when logging into a router using an SSH key.

:::info
RSA, Ed25519 and Ed25519-sk keys are supported in PEM, PKCS#8, or OpenSSH format.
:::

| Property | Description |
| :-- | :-- |
| **user** (read-only*)* | system user to which the SSH key has been assigned |
| **info** (read-only*)* | key info |
| **key-type** (read-only*)* | key type |
| **bits** (read-only*)* | key length |
| **fingerprint** (read-only*)* | key fingerprint in SHA256 (Base64) format |

#### Import public SSH key

On public SSH key import, you must specify the key file, the system user to which SSH key will be assigned, optionally, it is possible to specify the key owner.

| Property | Description |
| :-- | :-- |
| **user** (*string*; Default: ) | system user to which the SSH key has been assigned |
| **key-owner** (*string*) | SSH key owner |
| **public-key-file** (*string*) | file name in the router's root directory containing the public key |

#### Add public SSH key

It is possible to *add* a public SSH key (pasting the SSH key string), you must provide the key string, and the system user to which the SSH key has been assigned.

:::note
It is possible to *add* keys only in OpenSSH format
:::

| Property | Description |
| :-- | :-- |
| **user** (*string*; Default: ) | system user to which the SSH key has been assigned |
| **key** (*string*) | public key |

### Private keys

This menu is used to import and list imported private keys. Private keys are used to approve the router's identity during login to another device using an SSH key.

On private key import, it is possible to specify key-owner.

:::info
RSA and Ed25519 keys are supported in PEM or PKCS#8 format.
:::

| Property | Description |
| :-- | :-- |
| **user** (*string*; Default: ) | system user to which the SSH key has been assigned |
| **key-owner** (*string*) | SSH key owner |
| **key-type** (read-only*)* | key type |
| **bits** (read-only*)* | key length |

#### Import private SSH key

On private SSH key import, you must specify key file, system user to which SSH key will be assigned, optionally it is possible to provide key passphrase and specify key owner.

| Property | Description |
| :-- | :-- |
| **user** (*string*; Default: ) | system user to which the SSH key has been assigned |
| **key-owner** (*string*) | SSH key owner |
| **passphrase** *(string) [sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | key file passphrase |
| **private-key-file** (*string*) | file name in the router's root directory containing the private key |
