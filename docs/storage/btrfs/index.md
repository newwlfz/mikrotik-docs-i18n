# Btrfs

> Btrfs is a stable, copy-on-write file system with features like bitrot protection, subvolumes, and snapshots. It is available in RouterOS v7.18beta2+ with the Storage package and supports RAID configurations, subvolume management, and snapshot transfers.

# Btrfs

:::info
Features described on the Btrfs pages are available starting from RouterOS v7.18beta2 and require the [Storage](../index.md) package.
:::

Btrfs is a feature-rich copy-on-write file system that has been around since 2007. It is the default file system for some popular Linux distributions such as [Fedora](https://en.wikipedia.org/wiki/Fedora_Linux) and is used by many large companies such as [Meta](https://en.wikipedia.org/wiki/Meta_Platforms) in their datacenters. Over the years it has proven itself to be stable and more flexible than other popular file systems. The most significant features are:

- Bitrot protection (when used in Btrfs-RAID mode).
- Subvolumes.
- Snapshots.
- Transfer.

## Quickstart: format a disk as Btrfs

Format a single disk to Btrfs and access it under the default mount point:

```routeros
/disk/print
/disk/format <disk-name> file-system=btrfs
/disk/btrfs/filesystem/print
```

Once formatted, the disk appears with a Btrfs filesystem entry under `/disk/btrfs/filesystem/print`. From here you can label it, configure subvolumes/snapshots, or combine multiple disks into a Btrfs RAID.

## See also

- [Btrfs RAID](./raid.md) — RAID1 and RAID10 setups, disk replacement, and the BraidHealthCheck script.
- [Btrfs subvolumes and snapshots](./snapshots.md) — creating subvolumes, taking snapshots, transferring snapshots between devices.
- [Btrfs maintenance](./maintenance.md) — periodic scrubbing, balancing, automated snapshot rotation, and free-space management.
