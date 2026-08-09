# 存储

> 本文档介绍 RouterOS 的存储功能，包括磁盘加密、RAID 配置、Btrfs/XFS 文件系统、iSCSI 和 NFS 等网络协议、通过 DLNA 进行媒体共享、使用 rsync 进行文件同步，以及 ROSE 包在多个平台上为企业级存储管理提供的增强功能。

# 存储

import DocCardList from '@theme/DocCardList';

本节涵盖 RouterOS 的存储功能：磁盘级选项（加密、RAID、Btrfs 等文件系统）、网络存储协议（iSCSI、NFS、SMB、NVMe over TCP）、媒体共享（DLNA）以及文件同步（rsync）。

<DocCardList />

:::info

虽然支持常规驱动器，但出于可靠性考虑，我们建议使用具有断电保护（PLP）功能的驱动器。

:::

**ROSE（RouterOS Enterprise）** 包为 RouterOS 增加了数据中心功能——支持磁盘监控、使用 BTRFS 和 XFS 文件系统进行改进的格式化、RAID、rsync、iSCSI、NVMe over TCP、NFS 以及 SMB 客户端。此功能目前支持 **arm、arm64、x86** 和 **tile** 平台。

内置的 SMB **服务器** 和 DLNA 媒体服务器属于基础系统的一部分，不需要 ROSE 包——请参阅 [SMB](./smb.md) 和 [DLNA 媒体服务器](./dlna.md) 页面。