# RouterOS 许可证密钥

> 本文详细介绍了 MikroTik 硬件、CHR 和 x86 系统的 RouterOS 许可机制，涵盖 Software ID 和 System ID。针对各平台的许可特定说明及安装指南，请参阅相应独立文档。

# RouterOS 许可证密钥

## 概述

RouterOS 许可基于两个标识符：**Software ID** 和 **System ID**。这两个标识符决定了许可证在不同平台上的分配与管理方式。

- **Software ID** 用于 MikroTik 产品（RouterBOARD）和 x86 系统。
- **System ID** 用于云托管路由器（CHR）。

由于不同平台的许可行为有所差异，本文档为每种情况提供了独立的指南。

## 许可指南

### MikroTik 硬件许可

说明 MikroTik 硬件设备的许可级别、Software ID 行为及许可方式。

[MikroTik 硬件许可指南](./mikrotik-hardware/index.md)

### CHR 许可

说明基于 System ID 的许可机制、CHR 激活方式以及虚拟环境中的许可选项。

[CHR 许可指南](./chr/chr-licensing.md)

### x86 许可

涵盖 x86 平台 RouterOS 安装的许可证获取、Software ID 行为及许可级别。

[x86 许可指南](./x86/index.md)

## 安装指南

### MikroTik 硬件重装

涵盖使用 Netinstall 进行 RouterOS 重装与恢复。

[Netinstall 指南](../installation-and-upgrade/netinstall)

### x86 安装

涵盖 x86 系统要求及安装方法，包括 USB 和 Netinstall 部署。

[x86 安装指南](../installation-and-upgrade/install/x86-installation)

### CHR 安装

涵盖 CHR 在受支持的虚拟化平台上的部署与安装。

[CHR 安装指南](../installation-and-upgrade/install/chr-installation)