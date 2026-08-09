# Rsync

> Rsync in RouterOS allows efficient file synchronization between systems using ipsec encryption, with configurable local/remote paths and modes for upload/download. Dynamic IPsec entries are created when a password is set, ensuring secure transfers over TCP/8291 and UDP/500.

# Rsync

:::info
This feature requires the [Storage](./index.md) package.
:::

`rsync` (Remote Sync) is a powerful file synchronization and file transfer program used in Unix-based systems. It allows for efficient transfer and synchronization of files and directories between different systems or within the same system.

If you make changes in a file, only changes to files are transferred, reducing data transfer volume. RouterOS RSYNC implementation uses ipsec for data transfer (if password is set). When configured, you will see dynamic ipsec entries.

Rsync settings can be found in the `file/sync` menu.

:::warning

Port TCP/873 is used for the rsync control connection (if not open in the status (*file sync print*) you will be stuck at making control connection to *192.168.88.2*)

Port UDP/500 and protocol 50 (ipsec-esp) are used to create a secure connection and start the transfer (if not open in the status (*file sync print*) you will be stuck at initializing transfer)

:::

## Properties

| Property | Description |
| :-- | :-- |
| **local-path** | File/folder path. Used for mode *Upload* to set the path of the file/folder to upload to the device |
| **mode** | Sets if you want to download/upload the file (direction of the sync) |
| **password** | Target device password |
| **remote-address** | Target device IP |
| **remote-path** | File/folder path. Used with mode *download* to set the path on the target device to be downloaded |
| **user** | Target device username |

## Configuration example

Basic configuration is really easy. On the host device you need to add the file you want to sync to another device, the ip, user/password and the mode.

```ros
/file/sync
add local-path=/ipv6route.txt.rsc mode=upload remote-address=192.168.88.2 remote-path=RAID/

```

If configured correctly, you will see on the host device:

```ros
0 192.168.88.2  upload  /ipv6route.txt.rsc  RAID/        in sync
```

And on the client device:

```ros
#   REMOTE-ADDRESS   MODE      LOCAL-PATH  REMOTE-PATH         STATUS 
0 D 192.168.88.1 download  RAID/       /ipv6route.txt.rsc  in sync
```

### IPSec dynamic entries

When rsync is configured with a password, it creates dynamic IPSec entries for the secure transfer:

```ros
#     PEER                     TUNNEL  SRC-ADDRESS       DST-ADDRESS       PROTOCOL  ACTION   LEVEL    PH2-COUNT
;;; file-sync-10.155.145.11
1  D  file-sync-10.155.145.11  no      10.155.145.17/32  10.155.145.11/32  tcp       encrypt  require          1

/ip/ipsec/peer> print
 0  D  name="file-sync-10.155.145.11" address=10.155.145.11/32 local-address=10.155.145.17 profile=default exchange-mode=main send-initial-contact=yes
/ip/ipsec/identity> print
 0 D  ;;; file-sync-10.155.145.11
      peer=file-sync-10.155.145.11 auth-method=pre-shared-key secret="secret" generate-policy=no
```
