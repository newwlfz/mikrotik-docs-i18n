# SMB

> RouterOS includes a built-in SMB server for file sharing over SMB/CIFS protocols, supporting SMB2.1, 3.0, and 3.1.1 with security warnings for SMB1 and SMIPS devices. Users can configure shares, set user permissions, and manage access rights through `/ip/smb`, `/ip/smb/shares`, and `/ip/

# SMB

RouterOS includes a built-in **SMB server** for sharing folders of the router with network clients. In addition, the [ROSE package](./index.md) adds an **SMB client** that lets RouterOS mount remote SMB shares as disks.

## SMB server

**Sub-menu:** `/ip/smb` **Packages required:** `system`

SMB server provides file sharing access to configured folders of the router, allowing network clients to browse, read, write, and manage files stored on the router's storage media over the SMB/CIFS protocol. This enables the router to function as a simple network-attached storage (NAS) device for local network sharing of files, backups data, or router configuration backups files.

:::warning
RouterOS only supports SMB2.1, SMB3.0, and SMB3.1.1. SMB1 is not supported due to security vulnerabilities.

**Caution:** SMB is not supported on SMIPS devices.
:::

### Server settings

| Property | Description |
| :-- | :-- |
| **comment** (*string*; Default: **MikrotikSMB**) | Set a comment for the server |
| **domain** (*string*; Default: **MSHOME**) | Name of the Windows Workgroup |
| **enabled** (*yes \| no \| auto* Default: **auto**) | The default value is 'auto.' This means that the SMB server will automatically be enabled when the first non-disabled SMB share is configured under `/ip/smb/share` |
| **interface** (*string*; Default: **all**) | List of interfaces on which the SMB service will be running. all - SMB will be available on all interfaces. |

:::warning
Starting from version 7.14, the 'allow-guest' option has been replaced by a default guest user located in `/ip/smb/users`. This default guest user can now be disabled or enabled in this section.
:::

### Share settings

**Sub-menu:** `/ip/smb/shares`

Allows configuring share names and directories that will be accessible by SMB.

If the directory provided in the configuration does not exist it will be created automatically.

| Property | Description |
| :-- | :-- |
| **comment** (*string*; Default: **default share**) | Set a comment for the share |
| **disabled** (*yes \| no*; Default: **no**) | If disabled, the share will not be accessible. |
| **valid-users**(list of *strings*; \| Default:) | Specifies which users are allowed to access the Samba share. If it is left empty, all users will be able to access the share. Once a user or users are defined here, only they will be able to access the share |
| **invalid-users**(list of *strings*; \| Default: ) | Used to specify users who are explicitly denied access to the Samba share. |
| **require-encryption** (*yes*\| *no*; Default: ***no***) | Enforces the use of encryption for all connections to a particular Samba share. It is recommended to change this to "Yes" to ensure better stability with macOS clients. |
| **name** (*string*; Default: ) | Name of the SMB share |
| **directory** (*string*; Default: ) | Directory on the router assigned to the SMB share. If left empty, the value of the *name* argument will be used from the root folder. |

### User setup

**Sub-menu:** `/ip/smb/users`

Set up users that can access SMB shares of the router.

| Property | Description |
| :-- | :-- |
| **comment** (*string*; Default: ) | Set a description for the user |
| **disabled** (*yes \| no*; Default: **no**) | Defines whether the user is enabled or disabled |
| **name** (*string*; Default: ) | Login name of the SMB service user |
| **password** (*string*; Default: ) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | Password for the SMB user to connect to the SMB service |
| **read-only** (*yes \| no*; Default: **yes**) | Sets if the user has only read-only rights when accessing shares or full access rights. |

### Example

To make the RouterOS folder available through the SMB service follow these steps:

- Create user.

```ros
/ip/smb/users/add read-only=no name=mtuser password=mtpasswd
```

- add shared folder.

```ros
/ip/smb/shares/add directory=backup name=backup
```

- enable SMB service:

```ros
#this step is optional, as the default is "enabled=auto"
/ip/smb/set enabled=yes
```

Now check for results:

- Check general service settings.

```ros
/ip/smb/print
      enabled: yes
       domain: MSHOME
      comment: MikrotikSMB
   interfaces: all
```

- SMB user settings

```ros
/ip/smb/users/print
Flags: X - DISABLED; * - DEFAULT; r - READ-ONLY
Columns: NAME, PASSWORD
#     NAME    PASSWORD
0 X*r guest          
1     mtuser  mtpasswd
```

- And finally SMB shares settings.

```ros
/ip/smb/shares/print
Flags: X - DISABLED; * - DEFAULT
Columns: NAME, DIRECTORY, REQUIRE-ENCRYPTION
#    NAME    DIRECTORY  REQUIRE-ENCRYPTION
;;; default share
0 X* pub     /pub       no               
1    backup  backup     no
```

Now, additional configuration changes can be done, like disabling the default user and share, etc.

## SMB client

**Sub-menu:** `/disk` **Packages required:** [`rose-storage`](./index.md)

The ROSE package adds an SMB client that mounts a remote SMB share as a local disk on the router. The ROS package currently supports SMB2.1, SMB3.0, and SMB3.1.1 dialects (SMB1 is not supported due to security vulnerabilities).

### Properties

| Property | Description |
| :-- | :-- |
| **smb-address** | IP address of the SMB server |
| **smb-password***[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | SMB password |
| **smb-share** | Name of the share you want to connect to |
| **smb-user** | SMB user |

### Configuration example

Client

```ros
add smb-address=10.155.145.11 smb-share=share1 smb-user=user smb-password=password type=smb
```
