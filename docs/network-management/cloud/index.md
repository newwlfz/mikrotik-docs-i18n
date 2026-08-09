# Cloud

> MikroTik Cloud section provides configuration for Back To Home, DDNS, file sharing, and other cloud-assisted services with detailed instructions on enabling/disabling DDNS, triggering updates, and managing IP addresses for remote access.

import DocCardList from '@theme/DocCardList';

# Cloud

This section covers MikroTik Cloud features. Use it to configure Back To Home, Cloud communication, file sharing, and other cloud-assisted services.

<DocCardList />

MikroTik offers multiple services for your RouterBOARD devices that are connected to the Internet. These services are meant to ease the inconveniences when configuring, setting up, controlling, maintaining, or monitoring your device. A more detailed list of available services that IP/Cloud can provide can be found below.

## Services

:::danger
Be aware that if the router has multiple public IP addresses and/or multiple internet gateways, the exact IP used for communicating with MikroTik's Cloud server may not be as expected!

**Warning:** IP/Cloud requires a paid perpetual license for Cloud Hosted Router (CHR).

**Warning:** Cloud services are not supported on x86 systems.
:::

### DDNS

DDNS or Dynamic DNS is a service that updates the IPv4 address for A records and the IPv6 address for AAAA records periodically. Such a service is very useful when your ISP has provided a dynamic IP address that changes periodically, but you always need an address that you can use to connect to your device remotely. Below you can find operation details that are relevant to the IP/Cloud's DDNS service:

- Checks for outgoing IP address change: every 60 seconds.
- Waits for the MikroTik Cloud server's response: 15 seconds.
- DDNS record TTL: 60 seconds.
- Sends encrypted packets to **cloud2.mikrotik.com** using UDP port 15252.

Since RouterOS v6.43, if your device is able to reach **cloud2.mikrotik.com** using IPv6, then a DNS **AAAA** record is going to be created for your public IPv6 address. If your device is only able to reach cloud2.mikrotik.com using IPv4, then only a DNS **A** record is going to be created for your public IPv4 address. cloud.mikrotik.com is used for older RouterOS versions prior to 6.44

To enable the DDNS service:

```ros
[admin@MikroTik] /ip/cloud/set ddns-enabled=yes
[admin@MikroTik] /ip/cloud/print
         ddns-enabled: yes
 ddns-update-interval: none
          update-time: yes
       public-address: 159.148.147.196
  public-address-ipv6: 2a02:610:7501:1000::2
             dns-name: 529c0491d41c.sn.mynetname.net
               status: updated
```

:::warning
When the service is enabled, a DNS name will be stored on MikroTik's Cloud server permanently and this DNS name will resolve to the last IP that your RouterOS instance has sent to MikroTik's Cloud server.
:::

To disable the DDNS service:

```ros
/ip/cloud/set ddns-enabled=auto
```

:::warning
Before 7.17, the default value for ddns-enabled was "no". In versions including 7.17 and later, if you want to disable DDNS, make sure to disable the [Back To Home](./back-to-home.md) feature first, if it was enabled, then set "ddns-enabled=auto"

**Warning:** As soon as you disable the service, your device sends a command to MikroTik's Cloud server to remove the stored DNS name.
:::

To manually trigger a DNS update:

```ros
[admin@MikroTik] > /ip/cloud/force-update
```

:::warning
To actually connect to the device using the DNS name provided by the cloud server, a user must configure the router's firewall to permit such access from the WAN port. (The default MikroTik configuration does not permit access to services such as WebFig, WinBox, etc. from the WAN port).
:::

### Update time

Correct time on a device is important, it causes issues with the system's logs, breaks HTTPS connectivity to the device, breaks tunnel connectivity, and other issues. To have your system's clock updated, you can use  [NTP](../../system-information-and-utilities/ntp.md)  or  [SNTP](../../system-information-and-utilities/ntp.md), though it requires you to specify an IP address for the NTP Server. In most cases, NTP/SNTP is not required in order to simply have a correct time set on the device, for simplicity, you can use the IP Cloud's update time service. Below you can find operation details that are relevant to the IP/Cloud's update time service:

- Approximate time (accuracy of several seconds, depends on UDP packet latency).
- Updates time after a reboot and during every DDNS update (when the router's WAN IP address changes or after the force-update command is used).
- Sends encrypted packets to **cloud2.mikrotik.com** using UDP/15252 port.
- Detects time-zone depending on the router's public IP address and our commercial database.

To enable the time update service:

```ros
[admin@MikroTik] > /ip/cloud/set update-time=yes 
```

To enable automatic time zone detection:

```ros
[admin@MikroTik] > /system/clock/set time-zone-autodetect=yes 
```

:::warning
If `/ip/cloud/update-time` is set to `auto`, then the device's clock will be updated with MikroTik's Cloud server time (if no  [NTP](../../system-information-and-utilities/ntp.md)  or  [SNTP](../../system-information-and-utilities/ntp.md)  client is enabled).
:::

### Backup

It is possible to store your device's [backup](../../getting-started/configuration-management/backup.md) on MikroTik's Cloud server. The backup service allows you to upload an encrypted backup file, download it and apply the backup file to your device as long as your device is able to reach MikroTik's Cloud server. Below you can find operation details that are relevant to the IP/Cloud's backup service:

- 1 free backup slot for each device.
- Allowed backup size: 15MB.
- Sends encrypted packets to **cloud2.mikrotik.com** using UDP/15252 and TCP/15252 ports.

To create a new backup and upload it to the MikroTik's Cloud server:

```ros
[admin@MikroTik] > /system/backup/cloud/upload-file action=create-and-upload password=test123!!!
[admin@MikroTik] > /system/backup/cloud/print 
 0 name="cloud-20180921-162649" size=13.2KiB ros-version="6.44beta9" date=2018-09-21 16:26:49 status="ok" secret-download-key="AbCdEfGhIjKlM1234567890" 
```

:::warning
The `create-and-upload` action command will create a new system's backup file, encrypt the backup file with AES using the provided password and upload it. For the `upload` action command the password property has no effect since the `upload` action command uploads only already created system's backup files.
:::

To download the uploaded backup file and save it to the device's memory:

```ros
[admin@MikroTik] > /system/backup/cloud/download-file action=download number=0
### OR
[admin@MikroTik] > /system/backup/cloud/download-file action=download secret-download-key=AbCdEfGhIjKlM1234567890
```

:::warning
**Warning:** The secret-download-key is a unique identifier that can be used to download your encrypted backup to your other devices. Since you can download your encrypted backup from any location and any device by using the secret-download-key, you should try to keep this identifier a secret. The downloaded backup is still encrypted using AES; nevertheless, make sure you are using a strong password!
:::

To remove the uploaded backup:

```ros
/system/backup/cloud/remove-file number=0
```

To replace an existing file with a new backup file, use the following command:

```ros
/system/backup/cloud/upload-file action=create-and-upload replace=_your_previously_created_backup_file_ password=test123!!!
```

To upload an existing backup file (created previously):

```ros
[admin@MikroTik] > /system/backup/save encryption=aes-sha256 name=old_backup password=test123!!!
[admin@MikroTik] > /system/backup/cloud/upload-file action=upload src-file=old_backup.backup
[admin@MikroTik] > /system/backup/cloud/print 
 0 name="cloud-20180921-164044" size=13.2KiB ros-version="6.44beta9" date=2018-09-21 16:40:44 status="ok" secret-download-key="AbCdEfGhIjKlM1234567890"
```

:::warning
Make sure that the backup was encrypted using AES, otherwise, the IP/Cloud will reject the backup upload. Since there is only 1 free backup slot per device, you need to remove the existing backup before uploading a new one.
:::

### Back to Home

For more info about the Back to Home (BTH) service, see the separate [documentation page](./back-to-home.md).

### File share

For more info about File Share service, see the separate [documentation page](./file-share.md).

### Relay service

Back to home and File Share both partially rely on the MikroTik cloud relay service. All transmissions through the relay service are end-to-end encrypted, the relay is purely to facilitate connection and is designed to never require decryption of user data or metadata. See respective manuals for details on how each service uses the relay.

## Properties

**Sub-menu:** `/ip/cloud`

| Property | Description |
| :-- | :-- |
| **ddns-enabled** (*yes \| auto*; Default: **auto**) | If set to `yes`, then the device will send an encrypted message to MikroTik's Cloud server. The server will then decrypt the message and verify that the sender is an authentic MikroTik device. If all is OK, then MikroTik's Cloud server will create a DDNS record for this device and send a response to the device. Every minute the IP/Cloud service on the router will check if the WAN IP address matches the one sent to MikroTik's Cloud server and will send an encrypted update to the cloud server if the IP address changes.  If set to auto, ddns will only be enabled if [Back To Home](./back-to-home) is enabled. **Important:** Prior to the 7.17 versions, the default value was "no".     |
| **ddns-update-interval** (*time, minimum 60 seconds*; Default: **none**) | If set, DDNS will attempt to connect to IP Cloud servers at the set interval. If set to **none**, it will continue to internally check IP address update and connect to IP Cloud servers as needed. Useful if the IP address used is not on the router itself and thus cannot be checked as a value internal to the router. |
| **update-time** (*yes \| no*; Default: **yes**) | If set to `yes`, then the router clock will be set to the time, provided by the cloud server **IF** there is no  [NTP](../../system-information-and-utilities/ntp)  or  [SNTP](../../system-information-and-utilities/ntp)  client enabled. If set to `no`, then IP/Cloud service will never update the device's clock. If update-time is set to `yes`, clock will be updated even when ddns-enabled is set to auto. |
| **public-address** (*read-only: address*) | Shows the device's IPv4 address that was sent to the cloud server. This field is visible only after at least one IP Cloud request was successfully completed. |
| **public-address-ipv6** (*read-only: address*) | Shows the device's IPv6 address that was sent to the cloud server. This field is visible only after at least one IP Cloud request was successfully completed. |
| **warning** (*read-only: string*) | Shows a warning message if the IP address sent by the device differs from the IP address in the UDP packet header as visible by MikroTik's Cloud server. Typically this happens if the device is behind NAT. Example: "DDNS server received a request from IP `123.123.123.123` but your local IP was `192.168.88.23`; DDNS service might not work" |
| **dns-name** (*read-only: name*) | Shows the DNS name assigned to the device. The name consists of a 12-character serial number appended by *.sn.mynetname.net*. This field is visible only after at least one ddns-request is successfully completed. |
| **status** (*read-only: string*) | Contains a text string that describes the current dns-service state. The messages are self-explanatory:updating...updatedError: no Internet connectionError: request timed outError: REJECTED. Contact MikroTik supportError: internal error - should not happen. One possible cause is if the router runs out of memory |

### Advanced

**Sub-menu:** `/ip/cloud/advanced`

| Property | Description |
| :-- | :-- |
| **use-local-address** (*yes \| no*; Default: **no**) | By default, the DNS name will be assigned to the detected public address (from the UDP packet header). If you wish to send your "local" or "internal" IP address, then set this to `yes`. |

### Cloud backup

**Sub-menu:** `/system/backup/cloud`

Below you can find commands and properties that are relevant to the specific command, other properties will not have any effect:

- download-file

| Property | Description |
| :-- | :-- |
| **action** (*download*) | Downloads an uploaded backup file from MikroTik's Cloud server. |
| **number** (*integer*) | Specifies the backup slot on MikroTik's Cloud server. The free backup slot is always going to be in the `0th` slot. |
| **secret-download-key** (*string*) | Unique identifier that can be used to download your uploaded backup file. When downloading the uploaded backup file, you do not have to be using the same device, from which the backup was uploaded. Useful when deploying a backup on a new device. |

- remove-file

| Property | Description |
| :-- | :-- |
| **number** (*integer*) | Deletes the backup file in the specified backup slot. The free backup slot is always going to be in the `0th` slot. |

- upload-file

| Property | Description |
| :-- | :-- |
| **action** (*create-and-upload*) | Uploads a backup file to MikroTik's Cloud server.<code>create-and-upload</code> - creates a new backup file with the specified password and uploads it<code>upload</code> - uploads a created system's backup file. |
| **name** (*string*) | Specifies the backup's name that will show up in the uploaded backups list. This is **NOT** the source backup's name, this name is only used for visual representation. |
| **src-file** (*file*) | Backup's file name to upload that was created using `/system/backup`. This property only has an effect when the action is set to `upload`. |
| **password** (*string*) | Creates, encrypts and uploads a backup file with the specified password. This property only has an effect when the action is set to `create-and-upload`. |
