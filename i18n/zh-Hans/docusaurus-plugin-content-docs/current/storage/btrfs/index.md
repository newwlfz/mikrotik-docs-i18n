# Btrfs

> Btrfs 是一种稳定的写时复制文件系统，具备防位腐、子卷和快照等功能。自 RouterOS v7.18beta2 起，随 Storage 软件包提供，支持 RAID 配置、子卷管理和快照传输。

# Btrfs

:::info
Btrfs 页面所述功能自 RouterOS v7.18beta2 起可用，并需安装 [Storage](../index.md) 软件包。
:::

Btrfs 是一种功能丰富的写时复制文件系统，自 2007 年问世以来，已成为 [Fedora](https://en.wikipedia.org/wiki/Fedora_Linux) 等热门 Linux 发行版的默认文件系统，并被 [Meta](https://en.wikipedia.org/wiki/Meta_Platforms) 等众多大型企业用于其数据中心。多年实践已证明，它比其他主流文件系统更稳定、更灵活。其最显著的特性包括：

- 防位腐保护（在 Btrfs-RAID 模式下使用时）。
- 子卷。
- 快照。
- 传输。

## 快速入门：将磁盘格式化为 Btrfs

将单个磁盘格式化为 Btrfs，并在默认挂载点下访问：

```routeros
/disk/print
/disk/format <disk-name> file-system=btrfs
/disk/btrfs/filesystem/print
```

格式化完成后，磁盘会在 `/disk/btrfs/filesystem/print` 下显示为 Btrfs 文件系统条目。在此处，您可以为其设置标签、配置子卷/快照，或将多个磁盘组合成 Btrfs RAID。

## 另请参阅

- [Btrfs RAID](./raid.md) — RAID1 和 RAID10 配置、磁盘更换以及 BraidHealthCheck 脚本。
- [Btrfs 子卷与快照](./snapshots.md) — 创建子卷、拍摄快照、在设备间传输快照。
- [Btrfs 维护](./maintenance.md) — 定期巡检、平衡、自动快照轮换及空闲空间管理。