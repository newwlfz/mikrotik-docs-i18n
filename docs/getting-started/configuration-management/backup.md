# Backup

> The RouterOS backup feature enables saving and restoring router configurations, including MAC addresses, with options for encrypted or unencrypted storage. It supports saving backups to files and loading them back onto the same device, with warnings about version compatibility and sensitive data handling.

# Backup

The RouterOS backup feature allows saving the router configuration in a binary format file, which can then be re-applied on the same device. The system's backup file also contains the device's MAC addresses, which are restored when the backup file is loaded.

We recommend restoring the backup on the same version of RouterOS.

:::danger
If The Dude or User-manager is installed on the router, then the system backup will not contain configuration from these services, therefore, additional care should be taken to save configuration from these services. Use the provided tool mechanisms to save/export configuration if you want to save it.

**Warning:** System backups contain sensitive information about your device and its configuration; always consider encrypting the backup file and keeping the backup file in a safe place.
:::

## Saving a backup

**Sub-menu:** `/system/backup/save`

| Property | Description |
| :-- | :-- |
| **dont-encrypt** (*yes \| no*; Default: **no**) | Disable backup file encryption. Note that since RouterOS v6.43 without a provided password, the backup file is unencrypted. |
| **encryption** (*aes-sha256 \| rc4*; Default: **aes-sha256**) | The encryption algorithm to use for encrypting the backup file. Note that `rc4` is not considered a secure encryption method and is only available for compatibility reasons with older RouterOS versions. |
| **name** (*string*; Default: **[identity]-[date]-[time].backup**) | The filename for the backup file. |
| **password** (*string*; Default: ) *[sensitive](./list-of-menus-with-sensitive-parameters.md)* | Password for the encrypted backup file. Note that since RouterOS v6.43 without a provided password, the backup file is unencrypted. |

:::danger
If a password is not provided in RouterOS versions older than v6.43, then the backup file will be encrypted with the current user's password, except if the *dont-encrypt* property is used or the current user's password is empty.
:::

The backup file will be available under the `/file` menu, which can be downloaded using FTP or using Winbox.

## Loading a backup

Load a backup without password:

```ros
[admin@MikroTik] > /system/backup/load name=auto-before-reset.backup password=""
```

| Property | Description |
| :-- | :-- |
| **name** (*string*; Default: ) | File name for the backup file. |
| **password** (*string*; Default: ) *[sensitive](./list-of-menus-with-sensitive-parameters.md)* | Password for the encrypted backup file. |

## Example

To save the router's configuration to the file test and a password:

```ros
[admin@MikroTik] > /system/backup/save name=test password=<YOUR_PASSWORD> 
Configuration backup saved 
```

To see the files stored on the router:

```ros
[admin@MikroTik] > /file/print 
# NAME TYPE SIZE CREATION-TIME 
0 test.backup backup 12567 2018-09-08 21:07:50 
[admin@MikroTik] >
```

To load the saved backup file test:

```ros
[admin@MikroTik] > /system/backup/load name=test 
password: <YOUR_PASSWORD> 
Restore and reboot? [y/N]: y 
Restoring system configuration 
System configuration restored, rebooting now
```

## Cloud backup

Since RouterOS v6.44 it is possible to securely store your device's backup file on MikroTik's Cloud servers. Read more about this feature on the [IP/Cloud](../../network-management/cloud/index.md) page.
