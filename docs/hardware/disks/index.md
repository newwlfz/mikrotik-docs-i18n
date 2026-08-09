# Disks

> This page documents disk management in MikroTik RouterOS, covering storage device detection, formatting, swap space, and S.M.A.R.T. monitoring. It explains how to add external drives, manage mount points, format disks with various filesystems, and use RAID features. It also emphasizes safely ejecting disks to prevent data loss.

import DocCardList from '@theme/DocCardList';

# Disks

This section covers physical disk handling on RouterOS â€” disk detection, formatting, swap, and S.M.A.R.T. For network storage protocols (iSCSI, NFS, SMB, NVMe over TCP), RAID, filesystems (Btrfs), and other features added by the ROSE package, see the [Storage](../../storage/index.md) section.

## Summary

**Sub-menu:** `/disk`

This menu lists all attached storage devices, provided they are supported and in working condition. This is especially useful for RouterBOARD devices with SD/CF/USB/SATA/NVMe slots and x86 systems with additional dedicated storage drives, as the built-in storage is quite small. An external drive comes in handy when you need a large User Manager database, proxy cache, or possibly SMB shares on your router.

You can add as many external or secondary drives as you want and select any number of them for each of the mentioned feature usages. For example, User Manager could be used on three disks devices, with one as the active database and the rest as backups. You can then add a fourth disk, copy the active data to it, unmount it, unplug it, and move it to another server to keep using the actual database. This makes migration and backup easy.

Disks carry names based on where they are physically connected.

:::info
The **[Storage](../../storage/index.md)** package adds disk monitoring, advanced filesystems, RAID, rsync, iSCSI, NVMe over TCP, NFS, and an SMB client. See the [Storage](../../storage/index.md) section for details.

:::

:::danger
**Always use `/disk/eject` before physically removing any disk from your RouterOS device to prevent data loss!**

:::

## Properties

| Property | Description |
| :-- | :-- |
| **eject**| Safely unmounts (ejects) drive of your selection by using the "slot" that is assigned to it. After issuing this command it can be removed from the host device. |
| **format**| Command to initiate the disk formatting process. Contains additional properties of its own. Such as "file-system" and "label".select the disk (slot) that should be formattedfile-system ('exfat', 'ext4', 'fat32', 'xfs', 'btrfs', 'discard', 'discard-secure', 'wipe') - applies one of the available file system types; alternatively can be used to discard storage blocks (blkdiscard equivalent) or securely wipe (overwrite) data.mbr-partition-table - make an mbr partition table |
| **trim** | Discards the unused data blocks for performance (fstrim equivalent). Some NVMe enclosures might not support disk trimming. |
| **reset-counters** | Resets disk (slot) statistics |
| **monitor-traffic** | Checks real time disk performance and health stats |
| **test** | Allows performing performance tests of the selected device (Available from RouterOS 7.16) disk - device or devices for testdirection - ('read','write') duration - (int) pattern - ('random', 'sequential')thread-count - (int)block-size - size of block to be used for testingtype - ('device', 'filesystem') |
| **mount-read-only** | Sets the mounted disk in read only mode when set to *yes*. |
| **mount-point-template** | Sets the mounting point for the file system. It is possible to set the mount point as the following parameters based on the disk: [slot] (default) - sets the mount point as the slot name.[model] - sets the mount point as the device's model name.[serial] - sets the mount point as the device serial[fw-version] - sets the mount point as the device's firmware version.[fs-label] - sets the mount point as the device's file system label.[fs-uuid] - sets the mount point as the device's UUID[fs] - sets the mount point as the device's file system `/disk/set nvme1 mount-point-template="[model]"`   Additionally, it is possible to combine multiple variables to create a single mount point:  `/disk/set nvme1 mount-point-template="[model]-[fs]"`    |

:::info
/disk trim is not supported on USB drives
:::

## Flags

| Property | Description |
| :-- | :-- |
| **X - disabled** | Disabled device |
| **E - empty** | Empty slot |
| **B - BLOCK-DEVICE** | The "B - BLOCK-DEVICE" flag means that this device works using blocks for input/output operations. In the context of RouterOS, its distinction is crucial, as it helps determine whether a device is functioning as a data carrier or simply providing information about the disk layout structure. This difference becomes important when considering the extender with the device behind it. If a device is marked with the letter "B", this indicates its ability to be used as storage or memory. In contrast, devices that do not have a "B" mark are designed primarily to understand the structure of the disk.  This allows you to quickly recognize the presence of a PCIe or SAS expander, as well as detect the presence of drives in the first expander. In addition, it allows you to estimate the speed of the connection to which each device is connected.  However, the most notable benefit of the "B" flag is its ability to instantly indicate whether a device can be formatted or used for RAID purposes. |
| **M - mounted** | Mounted partition |
| **F - formatting** | The device is currently in the formatting process |
| **p - partition** | The device has a partition |
| **f - raid-member-failed** | These options are used with the [ROSE](../../storage/index.md) package. |
| **r - raid-member** |  |
| **c - encrypted** |  |
| **g - guid-partition-table** |  |
| **t - nvme-tcp-export** |  |
| **i - iscsi-export** |  |
| **s - smb-sharing** |  |
| **n - nfs-sharing** |  |
| **O - tcg-opal-self-encryption-enabled** |  |
| **o - tcg-opal-self-encryption-supported** |  |

## Settings

| Property | Description |
| :-- | :-- |
| **auto-smb-sharing** (yes \| no; Default: ) | Enables dynamic SMB shares when a new disk/partition item is added in "/disk" |
| **auto-smb-user** (list of strings; Default: ) | Default value for smb-sharing/smb-user setting, when a new disk/partition item is added in "/disk" |
| **auto-media-sharing** (yes \| no; Default: ) | Enables DLNA dynamically when a new disk/partition item is added in "/disk" |
| **auto-media-interface** (list of strings; Default: ) | Interface that will be used in a dynamic instance for `/ip/media` when a new disk/partition item is added in "/disk" |
| **default-mount-point-template** (string, Default: ) | Sets the default mount point template for each item added in "/disk" |

:::note

### Notes

With "auto-smb-sharing=yes" and "/ip/smb/share enabled=auto", the SMB server gets enabled when a storage device is physically plugged in

:::

## Examples

### Formatting attached storage unit - Simple

1. The disk is attached, and already mounted automatically by the system.

```ros
[admin@MikroTik] > disk print
Flags: B - BLOCK-DEVICE; M, F - FORMATTING
Columns: SLOT, MODEL, SERIAL, INTERFACE, SIZE, FREE, FS
#    SLOT  MODEL           SERIAL            INTERFACE                  SIZE           FREE  FS
0 BM usb1  USB Flash Disk  FBA0911260071572  USB 2.00 480Mbps  2 004 877 312  1 921 835 008  ext4
```

```ros
[admin@MikroTik] > /file/print
 # NAME                        TYPE          SIZE CREATION-TIME
 0 skins                       directory          1970-01-01 03:00:01
 1 pub                         directory          1970-02-04 21:31:40
 2 usb1                        disk               2022-03-07 14:05:16
```

1. Formatting the disk, in either of the supported file-systems (ext4, fat32, exfat, xfs, btrfs).

```ros
[admin@MikroTik] > /disk/format usb1 file-system=ext4 mbr-partition-table=no
  formatted: 100%
```

1. It's done! The drive is formatted and should be automatically mounted after the formatting process is finished.

### Formatting Attached Storage Unit - Detailed

Before proceeding with manual formatting, ensure that the storage device has been properly connected to your RouterOS device. The system will automatically attempt to mount the storage if it contains a supported file system and partition table. Once mounted, the device will appear in the `/file` menu shortly after being plugged in.

If the storage is not automatically detected or mounted, follow these steps:

1. Verify that the router recognizes the attached storage by checking the disk menu:

```ros
[admin@MikroTik] > disk print
Flags: B - BLOCK-DEVICE; M, F - FORMATTING
Columns: SLOT, MODEL, SERIAL, INTERFACE, SIZE, FREE, FS
#    SLOT  MODEL           SERIAL            INTERFACE                  SIZE           FREE  FS
0 BM usb1  USB Flash Disk  FBA0911260071572  USB 2.00 480Mbps  2 004 877 312  1 921 835 008  ext4
```

This output confirms that the system detects the storage drive and shows its current file system type.

1. Verify that the disk is mounted by checking the file menu:

```ros
[admin@MikroTik] > /file/print
 # NAME     TYPE    SIZE CREATION-TIME
 0 usb1     disk         2022-03-07 14:05:16
 1 skins    directory    1970-01-01 03:00:01
 2 pub      directory    1970-02-04 21:31:40
```

1. To format the drive, use the disk slot name or ID along with your preferred file system (ext4, fat32, exfat, xfs, or btrfs). You may also assign a label to the device and specify whether to create an MBR partition table:

```ros
[admin@MikroTik] > /disk/format usb1 file-system=ext4 label=usb-flash mbr-partition-table=yes
  formatted: 100%
```

:::note
**Note:** The formatting process displays a progress percentage indicator. Larger storage drives may require more time to complete. Please wait until the process finishes before removing the device.

:::

### Creating Multiple Disk Partitions

To create multiple GPT partitions, format the drive without a partition table and then add partitions manually:

```ros
[admin@MikroTik] > /disk/format usb1 file-system=ext4 label=usb-flash mbr-partition-table=no
  formatted: 100%
```

```ros
[admin@MikroTik] > /disk/add type=partition parent=usb1 partition-size=200M
[admin@MikroTik] > /disk/add type=partition parent=usb1 partition-size=500M
[admin@MikroTik] > /disk/add type=partition parent=usb1 slot=usb1-last-partition
```

:::info
**Notes:**

- The slot name (partition or disk) is assigned automatically but can be manually specified using the `slot` parameter.
- When partition size is not specified, the remaining available space will be used for the last partition.
- To adjust the starting position of a partition, use the `partition-offset` parameter.

:::

### Web-Proxy cache configuration example

Enter the proxy cache path under IP -> Proxy menu and the web proxy store is automatically created in the files menu. If a non-existent directory path is used, an additional sub-directory is also created automatically.

```ros
[admin@MikroTik] >  /ip/proxy/set cache-path=usb1/cache-n-db/proxy/

...

[admin@MikroTik] >  /file/print
 # NAME                                              TYPE                             SIZE CREATION-TIME       
 0 skins                                             directory                             2015-03-02 18:56:23
 1 sys-note.txt                                      .txt file                        23   2015-07-03 11:40:48
 2 usb1                                             disk                                  2015-07-03 11:35:05
 3 usb1/lost+found                                  directory                             2015-07-03 11:34:56
 4 usb1/cache-n-db                                  directory                             2015-07-03 11:41:54
  5 usb1/cache-n-db/proxy                            web-proxy store                       2015-07-03 11:42:09
```

### Log on disk configuration example

When configuring logging on disk, make sure that you create directories in which you want to store the log files manually, as non-existent directories will NOT be automatically created in this case.

```ros
[admin@MikroTik] >  /system/logging/action/set disk disk-file-name=disk1/log

...

[admin@MikroTik] >  /file/print where name~"disk1/log"
 # NAME                                              TYPE                             SIZE CREATION-TIME       
 0 disk1/log                                        directory                             2015-07-03 12:44:09
 1 disk1/log/syslog.0.txt                           .txt file                         160 2015-07-03 12:44:11
```

:::note
**Note:** Logging topics such as firewall, web-proxy and some other topics that tend to save a large amount or rapid printing of logs on the system NAND disk might cause it to wear out faster, so using some attached storage or remote logging is recommended in this case or saving data in RAM folder

:::

### Allocate RAM to folder

It is possible to add folders linked to RAM. Folders will be emptied on reboot or power loss.  
RAM will be filled up to tmpfs-max-size and if this variable is not provided - up to 1/2 of available RAM.

```ros
[admin@MikroTik] >  /disk/add type=tmpfs tmpfs-max-size=100M
[admin@MikroTik] > file print 
Columns: NAME, TYPE, SIZE, CREATION-TIME
#  NAME            TYPE       SIZE             CREATION-TIME       
0  tmp1             disk     100 003 840        2022-12-12 11:01:48
```

### Test disk performance

:::danger
Disk performance tests may slowly degrade disk health

On write tests all files and file systems on disks will be destroyed

:::

Starting from 7.16 to run disk performance tests. Disks have to be disabled or without a mountable file system (unformatted).  
Check available disks, if a disk is already mounted - disable it.

```ros
[admin@MikroTik] > /disk/print
Flags: B - BLOCK-DEVICE; M - MOUNTED
Columns: SLOT, MODEL, SERIAL, INTERFACE, SIZE, FREE, FS
#    SLOT  MODEL             SERIAL         INTERFACE                    SIZE            FREE  FS
0 BM usb1  JMicron External  DD56419883891  USB 3.10 5000Mbps  64 023 257 088  62 692 188 160  ext4

[admin@MikroTik] > disk disable usb1

[admin@MikroTik] > disk test disk=usb1 pattern=sequential  type=device thread-count=4 block-size=4K direction=write
Columns: SEQ, RATE, IOPS, DISK, TYPE, PATTERN, DIR, BSIZE, THREADS
SEQ  RATE          IOPS  DISK  TYPE    PATTERN     DIR    BSIZE  THREADS
0    1622.5Mbps  49 516  usb2  device  sequential  write   4096        4
1    26.2Mbps       800  usb2  device  sequential  write   4096        4
2    33.0Mbps     1 008  usb2  device  sequential  write   4096        4
3    11.7Mbps       360  usb2  device  sequential  write   4096        4
4    28.5Mbps       872  usb2  device  sequential  write   4096        4
5    34.6Mbps     1 056  usb2  device  sequential  write   4096        4
6    33.8Mbps     1 032  usb2  device  sequential  write   4096        4
TOT  255.7Mbps    7 806  usb2  device  sequential  write   4096        4

```

### Swap space

It is possible to add a swap space to your RouterOS device. This is useful when using [containers](../../containers/index.md) on RouterOS to be able to run containers that require much more RAM than your RouterOS device has. You can use a disk (or a partition) as a swap space or file as a swap space.

Swap space is reserved to be used only by [containers](../../containers/index.md).

:::info
Swap size is limited to 10 times the device's available RAM.
:::

#### Swap partition

Swap partition requires you to have a disk (or partition) connected to your RouterOS device. All of the disk (or partition) will be used as swap space and cannot be used for other purposes. Make sure you have a high speed disk for your swap partition. Using a swap partition has better performance than using a swap file.   |

To use a disk (or partition) as a swap partition, you can use the following command:

```routeros
/disk/set disk1 swap=yes   
```

Make sure you change `disk1` to your correct disk's name!

#### Swap file

A swap file requires you to have a disk that is formatted with a file system, for example, [Btrfs](../../storage/btrfs/index.md). Compared to the swap partition option, the whole disk (or partition) will not be used as swap space, only the swap file's size will be used on your disk (or partition). Using a swap file will have lower performance than using a swap partition.

To create a swap file on your existing file system, you can use the following command:

```routeros
/disk/add type=file file-path=disk1/swapfile file-size=1G swap=yes
```

Make sure you change `disk1` to your correct path, where your disk is mounted.

### Mount images

RouterOS can also mount **.iso** and **.squashfs** images directly. To mount an image, use the following command:

```routeros
/disk/add type=file file-path=disk1/mycopy.iso 
```

Make sure you change `disk1/mycopy.iso` to your correct path, where the image is located.
