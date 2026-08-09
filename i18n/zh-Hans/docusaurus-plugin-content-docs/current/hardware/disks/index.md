# 磁盘

> 本文档介绍 MikroTik RouterOS 中的磁盘管理，涵盖存储设备检测、格式化、交换空间及 S.M.A.R.T. 监控。内容说明如何添加外部驱动器、管理挂载点、使用多种文件系统格式化磁盘以及利用 RAID 功能。同时强调安全弹出磁盘以防止数据丢失。

import DocCardList from '@theme/DocCardList';

# 磁盘

本节涵盖 RouterOS 上的物理磁盘处理——磁盘检测、格式化、交换空间及 S.M.A.R.T.。有关网络存储协议（iSCSI、NFS、SMB、NVMe over TCP）、RAID、文件系统（Btrfs）以及 ROSE 软件包添加的其他功能，请参阅 [存储](../../storage/index.md) 部分。

## 概述

**子菜单：** `/disk`

此菜单列出所有已连接的存储设备，前提是这些设备受支持且工作正常。这对于带有 SD/CF/USB/SATA/NVMe 插槽的 RouterBOARD 设备以及带有额外专用存储驱动器的 x86 系统尤其有用，因为内置存储空间相当小。当您需要大型 User Manager 数据库、代理缓存或路由器上的 SMB 共享时，外部驱动器会非常方便。

您可以根据需要添加任意数量的外部或辅助驱动器，并为上述每种功能用途选择任意数量的驱动器。例如，User Manager 可以用于三个磁盘设备，其中一个作为活动数据库，其余作为备份。然后您可以添加第四个磁盘，将活动数据复制到其中，卸载并拔出该磁盘，再将其移至另一台服务器以继续使用实际数据库。这使得迁移和备份变得简单。

磁盘名称基于其物理连接位置命名。

:::info
**[存储](../../storage/index.md)** 软件包增加了磁盘监控、高级文件系统、RAID、rsync、iSCSI、NVMe over TCP、NFS 和 SMB 客户端功能。详情请参阅 [存储](../../storage/index.md) 部分。

:::

:::danger
**在从 RouterOS 设备物理移除任何磁盘之前，务必使用 `/disk/eject` 命令，以防止数据丢失！**

:::

## 属性

| 属性 | 描述 |
| :-- | :-- |
| **eject** | 通过使用分配给驱动器的“插槽”安全卸载（弹出）所选驱动器。发出此命令后，即可将其从主机设备中移除。 |
| **format** | 启动磁盘格式化过程的命令。包含其自身的附加属性，如“file-system”和“label”。选择应格式化的磁盘（插槽）file-system（'exfat'、'ext4'、'fat32'、'xfs'、'btrfs'、'discard'、'discard-secure'、'wipe'）- 应用可用的文件系统类型之一；或者可用于丢弃存储块（相当于 blkdiscard）或安全擦除（覆写）数据。mbr-partition-table - 创建 MBR 分区表 |
| **trim** | 丢弃未使用的数据块以提高性能（相当于 fstrim）。某些 NVMe 硬盘盒可能不支持磁盘修剪。 |
| **reset-counters** | 重置磁盘（插槽）统计信息 |
| **monitor-traffic** | 检查实时磁盘性能和健康状态统计信息 |
| **test** | 允许对所选设备执行性能测试（自 RouterOS 7.16 起可用）disk - 用于测试的设备或设备列表direction -（'read'、'write'）duration -（整数）pattern -（'random'、'sequential'）thread-count -（整数）block-size - 用于测试的块大小type -（'device'、'filesystem'） |
| **mount-read-only** | 设置为 *yes* 时，将已挂载的磁盘设置为只读模式。 |
| **mount-point-template** | 设置文件系统的挂载点。可以根据磁盘设置以下参数的挂载点：[slot]（默认）- 将挂载点设置为插槽名称。[model] - 将挂载点设置为设备型号名称。[serial] - 将挂载点设置为设备序列号[fw-version] - 将挂载点设置为设备固件版本。[fs-label] - 将挂载点设置为设备文件系统标签。[fs-uuid] - 将挂载点设置为设备 UUID[fs] - 将挂载点设置为设备文件系统 `/disk/set nvme1 mount-point-template="[model]"`   此外，还可以组合多个变量以创建单个挂载点：  `/disk/set nvme1 mount-point-template="[model]-[fs]"`    |

:::info
/disk trim 不支持 USB 驱动器
:::

## 标志

| 属性 | 描述 |
| :-- | :-- |
| **X - disabled** | 已禁用设备 |
| **E - empty** | 空插槽 |
| **B - BLOCK-DEVICE** | “B - BLOCK-DEVICE”标志表示该设备使用块进行输入/输出操作。在 RouterOS 的上下文中，这一区别至关重要，因为它有助于确定设备是作为数据载体运行，还是仅提供有关磁盘布局结构的信息。当考虑设备后方的扩展器时，这一差异变得重要。如果设备标记有字母“B”，则表示其能够用作存储或内存。相反，没有“B”标记的设备主要用于理解磁盘结构。这使您可以快速识别 PCIe 或 SAS 扩展器的存在，以及检测第一个扩展器中是否存在驱动器。此外，它还可以让您估算每个设备所连接链路的速度。然而，“B”标志最显著的好处是能够即时指示设备是否可格式化或用于 RAID 目的。 |
| **M - mounted** | 已挂载分区 |
| **F - formatting** | 设备当前正在格式化过程中 |
| **p - partition** | 设备具有分区 |
| **f - raid-member-failed** | 这些选项与 [ROSE](../../storage/index.md) 软件包一起使用。 |
| **r - raid-member** |  |
| **c - encrypted** |  |
| **g - guid-partition-table** |  |
| **t - nvme-tcp-export** |  |
| **i - iscsi-export** |  |
| **s - smb-sharing** |  |
| **n - nfs-sharing** |  |
| **O - tcg-opal-self-encryption-enabled** |  |
| **o - tcg-opal-self-encryption-supported** |  |

## 设置

| 属性 | 描述 |
| :-- | :-- |
| **auto-smb-sharing** (yes \| no; 默认：) | 在“/disk”中添加新的磁盘/分区项目时，启用动态 SMB 共享 |
| **auto-smb-user** (字符串列表; 默认：) | 在“/disk”中添加新的磁盘/分区项目时，smb-sharing/smb-user 设置的默认值 |
| **auto-media-sharing** (yes \| no; 默认：) | 在“/disk”中添加新的磁盘/分区项目时，动态启用 DLNA |
| **auto-media-interface** (字符串列表; 默认：) | 在“/disk”中添加新的磁盘/分区项目时，用于 `/ip/media` 动态实例的接口 |
| **default-mount-point-template** (字符串, 默认：) | 为“/disk”中添加的每个项目设置默认挂载点模板 |

:::note

### 备注

当“auto-smb-sharing=yes”且“/ip/smb/share enabled=auto”时，SMB 服务器会在物理插入存储设备时自动启用。

:::

## 示例

### 格式化连接的存储单元 - 简单模式

1. 磁盘已连接，并由系统自动挂载。

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

1. 使用任一支持的文件系统（ext4、fat32、exfat、xfs、btrfs）格式化磁盘。

```ros
[admin@MikroTik] > /disk/format usb1 file-system=ext4 mbr-partition-table=no
  formatted: 100%
```

1. 完成！驱动器已格式化，格式化过程结束后应自动挂载。

### 格式化连接的存储单元 - 详细模式

在进行手动格式化之前，请确保存储设备已正确连接到您的 RouterOS 设备。如果存储包含受支持的文件系统和分区表，系统将自动尝试挂载该存储。挂载后，设备将在插入后不久出现在 `/file` 菜单中。

如果存储未被自动检测或挂载，请按照以下步骤操作：

1. 通过检查磁盘菜单，验证路由器是否识别已连接的存储：

```ros
[admin@MikroTik] > disk print
Flags: B - BLOCK-DEVICE; M, F - FORMATTING
Columns: SLOT, MODEL, SERIAL, INTERFACE, SIZE, FREE, FS
#    SLOT  MODEL           SERIAL            INTERFACE                  SIZE           FREE  FS
0 BM usb1  USB Flash Disk  FBA0911260071572  USB 2.00 480Mbps  2 004 877 312  1 921 835 008  ext4
```

此输出确认系统检测到存储驱动器并显示其当前文件系统类型。

1. 通过检查文件菜单，验证磁盘是否已挂载：

```ros
[admin@MikroTik] > /file/print
 # NAME     TYPE    SIZE CREATION-TIME
 0 usb1     disk         2022-03-07 14:05:16
 1 skins    directory    1970-01-01 03:00:01
 2 pub      directory    1970-02-04 21:31:40
```

1. 要格式化驱动器，请使用磁盘插槽名称或 ID 以及您首选的文件系统（ext4、fat32、exfat、xfs 或 btrfs）。您还可以为设备分配标签，并指定是否创建 MBR 分区表：

```ros
[admin@MikroTik] > /disk/format usb1 file-system=ext4 label=usb-flash mbr-partition-table=yes
  formatted: 100%
```

:::note
**注意：** 格式化过程会显示进度百分比指示器。较大的存储驱动器可能需要更多时间才能完成。请等待过程结束后再移除设备。

:::

### 创建多个磁盘分区

要创建多个 GPT 分区，请先不带分区表格式化驱动器，然后手动添加分区：

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
**备注：**

- 插槽名称（分区或磁盘）自动分配，但可以使用 `slot` 参数手动指定。
- 当未指定分区大小时，剩余可用空间将用于最后一个分区。
- 要调整分区的起始位置，请使用 `partition-offset` 参数。

:::

### Web-Proxy 缓存配置示例

在 IP -> Proxy 菜单中输入代理缓存路径，web proxy 存储将自动在文件菜单中创建。如果使用了不存在的目录路径，也会自动创建额外的子目录。

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

### 磁盘日志配置示例

在配置磁盘日志时，请确保手动创建要存储日志文件的目录，因为在这种情况下，不存在的目录将不会自动创建。

```ros
[admin@MikroTik] >  /system/logging/action/set disk disk-file-name=disk1/log

...

[admin@MikroTik] >  /file/print where name~"disk1/log"
 # NAME                                              TYPE                             SIZE CREATION-TIME       
 0 disk1/log                                        directory                             2015-07-03 12:44:09
 1 disk1/log/syslog.0.txt                           .txt file                         160 2015-07-03 12:44:11
```

:::note
**注意：** 诸如防火墙、web-proxy 等倾向于在系统 NAND 磁盘上保存大量或快速打印日志的日志主题可能会导致其磨损加快，因此在这种情况下建议使用外部存储或远程日志记录，或将数据保存在 RAM 文件夹中。

:::

### 分配 RAM 到文件夹

可以添加链接到 RAM 的文件夹。重启或断电时，文件夹将被清空。  
RAM 将被填充至 tmpfs-max-size 限制，如果未提供此变量，则填充至可用 RAM 的 1/2。

```ros
[admin@MikroTik] >  /disk/add type=tmpfs tmpfs-max-size=100M
[admin@MikroTik] > file print 
Columns: NAME, TYPE, SIZE, CREATION-TIME
#  NAME            TYPE       SIZE             CREATION-TIME       
0  tmp1             disk     100 003 840        2022-12-12 11:01:48
```

### 测试磁盘性能

:::danger
磁盘性能测试可能会缓慢降低磁盘健康状态

写入测试将销毁磁盘上的所有文件和文件系统

:::

从 7.16 版本开始可运行磁盘性能测试。磁盘必须已禁用或不具有可挂载的文件系统（未格式化）。  
检查可用磁盘，如果磁盘已挂载 - 请将其禁用。

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

### 交换空间

可以为您的 RouterOS 设备添加交换空间。当在 RouterOS 上使用 [容器](../../containers/index.md) 以运行需要比 RouterOS 设备可用 RAM 多得多的容器时，此功能非常有用。您可以使用磁盘（或分区）作为交换空间，或使用文件作为交换空间。

交换空间保留仅供 [容器](../../containers/index.md) 使用。

:::info
交换大小限制为设备可用 RAM 的 10 倍。
:::

#### 交换分区

交换分区要求您的 RouterOS 设备连接有磁盘（或分区）。整个磁盘（或分区）将用作交换空间，不能用于其他用途。请确保为交换分区使用高速磁盘。使用交换分区的性能优于使用交换文件。   |

要将磁盘（或分区）用作交换分区，可以使用以下命令：

```routeros
/disk/set disk1 swap=yes   
```

请务必将 `disk1` 更改为您正确的磁盘名称！

#### 交换文件

交换文件要求您有一个已格式化为文件系统的磁盘，例如 [Btrfs](../../storage/btrfs/index.md)。与交换分区选项相比，整个磁盘（或分区）不会全部用作交换空间，仅交换文件的大小会占用您的磁盘（或分区）。使用交换文件的性能低于使用交换分区。

要在现有文件系统上创建交换文件，可以使用以下命令：

```routeros
/disk/add type=file file-path=disk1/swapfile file-size=1G swap=yes
```

请务必将 `disk1` 更改为您磁盘挂载的正确路径。

### 挂载镜像

RouterOS 还可以直接挂载 **.iso** 和 **.squashfs** 镜像。要挂载镜像，请使用以下命令：

```routeros
/disk/add type=file file-path=disk1/mycopy.iso 
```

请务必将 `disk1/mycopy.iso` 更改为镜像所在的正确路径。