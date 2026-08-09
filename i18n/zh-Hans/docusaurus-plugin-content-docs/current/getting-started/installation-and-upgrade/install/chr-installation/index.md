# CHR：安装

> 本页概述了在虚拟环境中安装和配置云托管路由器（CHR）的相关信息，涵盖系统要求、RAM 计算、磁盘镜像格式、下载说明、虚拟机设置及访问详情。

# CHR：安装

## 概述与系统要求

云托管路由器（CHR）是 RouterOS 的虚拟化版本，专为在 x86_64 虚拟环境中运行而设计。它提供了 MikroTik 硬件设备上可用的相同核心路由、防火墙、VPN 及管理功能。

## 主机系统要求

- **CPU**：支持虚拟化的 64 位处理器
- **RAM**：256 MB 或更高
- **磁盘**：128 MB 或更高

## 容量限制

### RouterOS 版本 6

- CHR 虚拟硬盘最大容量：16 GB

### RouterOS 版本 7

- 最大 RAM 和磁盘空间受 Linux 内核 5.6.3 限制，并取决于具体硬件。

## 计算最低 RAM 要求

所需的最低 RAM 取决于您的 CPU 数量和接口数量。请使用以下相应公式计算近似值：

- **RouterOS v6**：
  
  `RAM = 128 + [ 8 × (CPU_COUNT) × (INTERFACE_COUNT - 1) ]`

- **RouterOS v7**：
  
  `RAM = 512 + [ 8 × (CPU_COUNT) × (INTERFACE_COUNT - 1) ]`

**建议**：对于 CHR 实例，请至少分配 1024 MiB 的 RAM。

## 软件要求

- **软件包版本**：RouterOS v6.34 或更高版本

## 可用磁盘镜像格式

- **RAW 磁盘镜像**：`.img` 文件
- **VirtualBox 磁盘镜像**：`.vdi` 文件
- **VMware 磁盘镜像**：`.vmdk` 文件
- **Hyper-V 磁盘镜像**：`.vhdx` 文件
- **OVA 设备**：`.ova` 文件

:::warning
这些仅为磁盘镜像，必须附加到虚拟机中。
:::

## 下载 CHR 镜像

1. 前往 [MikroTik 下载页面](https://mikrotik.com/download/chr) 的 Cloud Hosted Router 部分。
2. 选择适用于您平台的镜像格式。
3. 下载文件。

## 创建并配置虚拟机

1. 在您的虚拟机管理程序中创建新的虚拟机。
2. 将 CHR 磁盘镜像附加为系统磁盘。
3. 启动虚拟机。

### 虚拟网络适配器

:::info
**Fast Path 支持**

- RouterOS v7：支持 **vmxnet3** 和 **virtio-net** 接口的 Fast Path。
- RouterOS v6：不支持 Fast Path。

:::

## 访问 CHR

- 用户名：`admin`
- 密码：无（首次登录后应立即设置强密码）

首次启动后，CHR 默认以 Free 许可证运行。要激活试用版或升级，请使用 `/system/license/renew`。

## 平台特定指南

### 支持的虚拟化平台

- [VMware ESXi](./esxi.md)
- VMware Fusion
- [Proxmox VE (KVM/QEMU)](./proxmox.md)
- [Hyper-V](./hyperv.md)
- [VirtualBox](./virtualbox.md)
- Xen Server

:::warning
CHR 无法在 **bhyve** 虚拟机管理程序上运行。CHR 不支持半虚拟化平台。
:::

> **注意：** 使用 Hyper-V 时，仅支持第 1 代虚拟机。

> **重要提示：** 任何虚拟机管理程序均不支持半虚拟化。

### 支持的云平台

- Amazon Web Services (AWS)
- Google Cloud Platform (GCP)
- [Hetzner Cloud](./hetzner.md)
- Linode
- Microsoft Azure
- [Vultr](./vultr.md)