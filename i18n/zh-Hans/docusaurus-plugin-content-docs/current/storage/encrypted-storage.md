# 加密存储（dm-crypt）

> 加密存储（dm-crypt）利用 `dm_crypt` 为块设备提供透明的磁盘加密功能，支持槽名称、加密密钥和后端驱动器等属性。示例展示了如何在 USB 或 RAID1 阵列上创建加密文件系统，并附有格式化说明。

# 加密存储（dm-crypt）

:::info
此功能需要 [Storage](./index.md) 软件包。
:::

与 `type=crypted` 配合使用的驱动器或设备，用于创建 `dm_crypt` 加密存储。`dm-crypt` 是一种透明的磁盘加密子系统，旨在为块设备提供加密功能。

## 属性

| 属性 | 说明 |
| :-- | :-- |
| **slot** *(字符串；默认值：)* | 文件系统的名称 |
| **encryption-key** *(字符串；默认值：)* | 用于解密的密钥 |
| **crypted-backend** *(字符串；默认值：)* | 需要加密的驱动器或分区 |

## 示例

### 简单的加密文件系统

创建加密文件系统：

```ros
/disk
add crypted-backend=usb1 encryption-key=<secret_key> slot=crypted-usb1 type=crypted
```

创建完成后，格式化文件系统即可使用。

```ros
/disk/format crypted-usb1 file-system=ext4 
```

### 带完整性检查的加密 RAID1 阵列

创建 RAID1 阵列，并在其上创建加密文件系统：

```routeros
/disk
add raid-device-count=2 raid-type=1 slot=raid1 type=raid
set nvme3 raid-master=raid1 raid-role=0
set nvme4 raid-master=raid1 raid-role=1
add crypted-backend=raid1 encryption-key=<secret_key> slot=crypted-raid1 type=crypted  crypt-mode=encryption-and-integrity

```

将加密文件系统格式化为 Btrfs：

```routeros
/disk
 format crypted-raid1 file-system=btrfs  
```