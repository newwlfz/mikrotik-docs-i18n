# Ramdisk

> RAMdisk 支持将 RAM 用作块设备进行存储，支持 RAID 配置，并需要 Storage 软件包。重启或断电后数据将被清除，大小可通过 ramdisk-size 属性进行配置。

# Ramdisk

:::info
此功能需要 [Storage](./index.md) 软件包。
:::

RAMdisk 允许将部分 RAM 用作附加设备（块设备）。与 tmpfs 相比，这允许将 RAM 用作 RAID 的一部分，或在任何需要设备（而非文件夹）的配置中使用。

:::warning

RAMdisk 在重启或断电后将被清除。

:::

## 属性

| 属性 | 描述 |
| :-- | :-- |
| **ramdisk-size** | 您要创建的块设备的大小 |

## 配置示例

```ros
/disk/add type=ramdisk ramdisk-size=500M
```

使用前请格式化 ramdisk：

```routeros
/disk/format ramdisk1
```