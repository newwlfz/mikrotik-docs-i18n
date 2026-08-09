# CHR：Proxmox VE 安装指南

> 本页提供了在 Proxmox VE 虚拟化环境中部署 MikroTik Cloud Hosted Router (CHR) 的概述和详细安装步骤，涵盖虚拟机创建、镜像处理及配置方法。

# CHR：Proxmox VE 安装指南

## 概述

Cloud Hosted Router (CHR) 是 MikroTik RouterOS 的一个版本，专为在 x86_64 虚拟化环境中运行而设计。它提供完整的路由、防火墙、VPN 和管理功能，适用于本地及基于云的虚拟基础设施，如 Proxmox VE。

Proxmox VE (KVM/QEMU) 允许使用 raw 或 qcow2 磁盘镜像灵活部署 CHR，并提供多种存储后端和网络适配器选项。

## 安装步骤

### 步骤 1：创建虚拟机

- 使用 Web 界面在 Proxmox VE 中创建新的虚拟机。
- 根据需要分配 CPU、内存和网络接口。
- 不要安装操作系统（CHR 磁盘将手动附加）。

### 步骤 2：下载并解压 CHR 镜像

从 MikroTik 下载页面下载最新的 CHR 镜像：https://mikrotik.com/download 到 Proxmox 主机：

```bash
wget https://download.mikrotik.com/routeros/7.21.4/chr-7.21.4.img.zip
```

:::warning
请将 URL 替换为 MikroTik [下载页面](https://mikrotik.com/download) 上提供的最新 CHR 版本。
:::

解压镜像：

```bash
unzip chr-7.21.4.img.zip
```

这将生成一个用于安装的 `.img` 文件。

### 步骤 3：将镜像移动到虚拟机存储

Proxmox 默认本地存储位置：

```bash
/var/lib/vz/images/<VM_ID>/
```

如有需要，创建目录：

```bash
mkdir -p /var/lib/vz/images/<VM_ID>
```

移动镜像：

```bash
mv chr-7.21.4.img /var/lib/vz/images/<VM_ID>/
```

### 步骤 4：将镜像转换为 QCOW2 格式

将 raw 格式的 CHR 镜像转换为 qcow2 格式：

```bash
qemu-img convert -f raw -O qcow2 /var/lib/vz/images/<VM_ID>/chr-7.21.4.img /var/lib/vz/images/<VM_ID>/vm-<VM_ID>-disk-1.qcow2
```

### 步骤 5：将磁盘附加到虚拟机

虚拟机配置文件位置：

```bash
/etc/pve/qemu-server/<VM_ID>.conf
```

通过虚拟机配置文件或使用 Proxmox Web 界面手动附加磁盘。

:::tip
建议先使用测试虚拟机验证配置语法是否正确。
:::

## 基于 GUI 的替代方法

1. 通过 Proxmox Web 界面创建基础虚拟机。
2. 确保存储设置为本地存储。
3. 将 CHR 镜像上传至：`/var/lib/vz/images/<VM_ID>/`
4. 将镜像转换为 qcow2 格式：

```bash
qemu-img convert -f raw -O qcow2 chr.img vm-<VM_ID>-disk-1.qcow2
```

1. 通过 Proxmox GUI 或 `.conf` 文件附加磁盘。

## 自动化安装脚本

CHR 也可以通过 Proxmox 主机上的 Bash 脚本进行部署。

**脚本功能说明：**

- 创建临时目录 (/root/temp)。
- 下载 CHR 镜像。
- 解压并转换镜像。
- 创建虚拟机并附加磁盘。

```bash
#!/bin/bash

version="nil"
vmID="nil"

echo "############## 脚本开始 ##############"

if [ ! -d /root/temp ]; then
    mkdir /root/temp
fi

read -p "请输入 CHR 版本 (例如 7.21.4): " version

cd /root/temp

wget https://download.mikrotik.com/routeros/$version/chr-$version.img.zip
unzip chr-$version.img.zip

read -p "请输入虚拟机 ID: " vmID

mkdir -p /var/lib/vz/images/$vmID

qemu-img convert -f raw -O qcow2 \
chr-$version.img \
/var/lib/vz/images/$vmID/vm-$vmID-disk-1.qcow2

qm create $vmID \
  --name chr-$version \
  --net0 virtio,bridge=vmbr0 \
  --bootdisk virtio0 \
  --ostype l26 \
  --memory 512 \
  --sockets 1 \
  --cores 1 \
  --virtio0 local:$vmID/vm-$vmID-disk-1.qcow2

echo "############## 脚本结束 ##############"
```

### 实用技巧

修复脚本中的 Windows 换行符：

```bash
sed -i -e 's/\r$//' *.sh
```

## 支持的网络和磁盘接口

### Proxmox VE (KVM/QEMU)

**网络适配器：**

- Virtio（半虚拟化）
- E1000

**磁盘控制器：**

- IDE
- SATA
- Virtio（半虚拟化）