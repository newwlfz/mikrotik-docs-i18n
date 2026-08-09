# Storage

> This page documents RouterOS storage features including disk encryption, RAID configurations, Btrfs/XFS filesystems, network protocols like iSCSI and NFS, media sharing via DLNA, file synchronization with rsync, and ROSE package enhancements for enterprise-level storage management across multiple platforms.

# Storage

import DocCardList from '@theme/DocCardList';

This section covers RouterOS storage features: disk-level options (encryption, RAID, filesystems such as Btrfs), network storage protocols (iSCSI, NFS, SMB, NVMe over TCP), media sharing (DLNA), and file synchronization (rsync).

<DocCardList />

:::info

While regular drives are supported, for reliability purposes we recommend using drives that have Power Loss Protection (PLP).

:::

The **ROSE (RouterOS Enterprise)** package adds data center functionality to RouterOS — supporting disk monitoring, improved formatting with BTRFS and XFS file systems, RAIDs, rsync, iSCSI, NVMe over TCP, NFS, and an SMB client. This functionality is currently supported on **arm, arm64, x86** and **tile** platforms.

The built-in SMB **server** and DLNA media server are part of the base system and do not require the ROSE package — see the [SMB](./smb.md) and [DLNA Media Server](./dlna.md) pages.
