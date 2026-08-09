# 自加密硬盘（SED）

> 本文档介绍 MikroTik RouterOS 对自加密硬盘（SED）的支持，需使用 Storage 软件包。文中说明了 Opal 合规性，展示了带标志（o/O）的受支持硬盘，并提供了为 SATA 设备设置或取消加密密码的命令。

# 自加密硬盘（SED）

:::info
此功能需要 [Storage](./index.md) 软件包。
:::

要使用 SED，硬盘必须符合 [Opal](https://en.wikipedia.org/wiki/Opal_Storage_Specification) 标准。请在购买硬盘前查阅硬盘制造商的文档，以确认特定硬盘是否支持此功能。

SED 不支持使用 USB 桥接器的配置。

RouterOS 为受支持的硬盘添加 **o（支持但未激活）** 或 **O（支持且已激活）** 标志：

```ros
/disk/print
Flags: B - BLOCK-DEVICE; M, F - FORMATTING; o - TCG-OPAL-SELF-ENCRYPTION-SUPPORTED (inactive); O - TCG-OPAL-SELF-ENCRYPTION-SUPPORTED (active)
Columns: SLOT, MODEL, SERIAL, INTERFACE, SIZE, FREE, FS, RAID-MASTER
#     SLOT   MODEL                  SERIAL           INTERFACE                   SIZE             FREE  FS    RAID
0 BMo sata1  Samsung SSD 860 2.5in  S3Z9NX0N414510L  SATA 6.0 Gbps  1 000 204 886 016  983 351 111 680  ext4  none
1 BMo sata2  Samsung SSD 860        S5GENG0N307602J  SATA 6.0 Gbps  1 000 204 886 016  983 351 128 064  ext4  none
2 BMO sata3  Samsung SSD 860        S5GENG0N307604H  SATA 6.0 Gbps  1 000 204 886 016  983 351 128 064  ext4  none
3 BMO sata4  Samsung SSD 860 2.5in  S4CSNX0N838150B  SATA 6.0 Gbps  1 000 204 886 016  983 351 128 064  ext4  none
```

设置 TCG-OPAL 自加密：

```ros
/disk
/disk/set sata1 self-encryption-password=securepassword
```

取消设置：

```ros
/disk
/disk/unset sata1 self-encryption-password
```

或

```ros
/disk
/disk/set sata1 !self-encryption-password

```