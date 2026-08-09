# CHR：Hetzner Cloud 安装指南

> 本页概述了在 Hetzner Cloud 上部署 MikroTik RouterOS Cloud Hosted Router (CHR) 的流程，详细说明了服务器创建、救援系统激活、通过 SSH 部署 CHR 镜像以及重启指令等安装步骤，同时强调了安全最佳实践。

# CHR：Hetzner Cloud 安装指南

## 概述

**[Hetzner Cloud](https://www.hetzner.com/cloud)** 是一个云计算平台，提供可扩展的虚拟机基础设施以及一系列预配置的 Linux 发行版。对于需要高级网络功能的用户，Hetzner Cloud 也是部署 **RouterOS Cloud Hosted Router (CHR)** 的合适平台。

Cloud Hosted Router (CHR) 是 MikroTik RouterOS 的一个版本，专为在 x86_64 虚拟化环境中运行而设计。它提供与 MikroTik 硬件设备相同的核心路由、防火墙、VPN 和管理功能，适用于基于云的网络、VPN 服务以及通用网络管理。

当部署在 Hetzner Cloud 上时，CHR 既能受益于可扩展的虚拟基础设施，又能保持完整的 RouterOS 功能，使用户能够构建灵活且强大的网络解决方案。

## 创建 CHR 虚拟机

1. **创建 Hetzner Cloud 服务器**  
   开始在 Hetzner Cloud 上创建新服务器。任何可用的服务器选项均可使用。
2. **激活救援系统**
   - 在 Hetzner Cloud 管理界面中，通过选择 **ENABLE RESCUE & POWER CYCLE** 来激活 **Enable Rescue** 系统。
   - 选择 `linux64` 作为救援操作系统。
   - 系统将显示用户名和密码。使用这些凭据通过 SSH 登录救援系统。
3. **安装 Cloud Hosted Router (CHR)**
   - 登录救援系统后，下载 CHR **RAW** 磁盘镜像，并使用以下命令将其写入云服务器的系统磁盘：

   ```bash
   curl -L https://download.mikrotik.com/routeros/7.21.4/chr-7.21.4.img.zip | funzip | dd of=/dev/sda bs=1M
   ```

   >`/dev/sda` 设备名称可能因云提供商配置而异。

:::warning
请将 URL 替换为 MikroTik [下载页面](https://mikrotik.com/download) 上提供的最新 CHR 版本链接。
:::

## 重启服务器

安装完成后，通过执行 `reboot` 命令重启服务器。
:::warning
立即[保护您的 RouterOS](../../../securing-your-router.md) 安装至关重要！
:::

请确保保持 RouterOS 更新，并遵循最佳安全实践，以维护服务器的安全性和性能。