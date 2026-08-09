# 与 MikroTik 云服务的通信

> 本页详细介绍了 MikroTik RouterOS 与云服务器及 Mikrotik 服务之间的连接，列出了子菜单、域名、默认状态以及每种连接类型的禁用方法。

# 与 MikroTik 云服务的通信

下表列出了 RouterOS 可能向 MikroTik 服务器发起的所有连接信息，以及如何禁用这些连接的说明。

| 子菜单 | 域名 | 默认启用/激活 | 确保通信禁用/不激活 |
| :-- | :-- | :-- | :-- |
| **system clock time-zone-autodetect** | cloud2.mikrotik.com | 是 | `/system/clock/set` time-zone-autodetect=no （[参见时钟文档](../../system-information-and-utilities/clock)） |
| **system backup cloud** | cloud2.mikrotik.com | 否 | 仅通过 upload-file、download-file、remove-file 命令触发通信。（[参见备份](./index.md#cloud-backup)） |
| **ip cloud update-time** | cloud2.mikrotik.com | 是 | `/ip/cloud/set` update-time=no （[参见更新时间](./index.md#update-time)） |
| **ip cloud ddns-enabled** | cloud2.mikrotik.com | 否 | `/ip/cloud/set` ddns-enabled=auto （[参见DDNS](./index.md#ddns)） |
| **ip cloud back-to-home-vpn** | cloud2.mikrotik.com | 否 | `/ip/cloud/set` back-to-home-vpn=revoked-and-disabled （[参见BTH VPN](./back-to-home.md#ip-cloud)） |
| **ip cloud back-to-home-file** | cloud2.mikrotik.com | 否 | 仅通过启用或禁用“ip cloud back-to-home-file”中的文件共享来触发通信。（[参见文件共享](./file-share)） |
| **system license** | licence.mikrotik.com | 是（仅与[CHR](../../getting-started/routeros-licensing/chr)相关） | 对于CHR，无法通过RouterOS中的特定命令或设置来禁用与许可证服务器的通信。（[参见CHR许可证](../../getting-started/routeros-licensing/chr/chr-licensing)） |
| **interface lte firmware-upgrade** | upgrade.mikrotik.com | 否 | 仅通过 firmware-upgrade 命令触发通信。（[参见LTE固件升级](../../mobile-networking/lte-5g.md#modem-firmware-upgrade-command)） |
| **interface detect-internet** | cloud.mikrotik.com | 否 | `/interface/detect-internet/set` detect-interface-list=none （[参见互联网检测](../../diagnostics-monitoring-and-troubleshooting/detect-internet)） |
| **system package update** | upgrade.mikrotik.com | 否 | 仅通过 check-for-updates 命令以及从升级服务器下载软件包来触发通信。（[参见软件包更新](../../getting-started/installation-and-upgrade/packages)） |
| **system swos upgrade** | upgrade.mikrotik.com | 否 | 仅通过 upgrade 命令触发通信。（[参见SWOS升级](../../bridging-and-switching/marvell-prestera-switch-chip-features.md#configuring-swos-using-routeros)） |