# Communication with MikroTik Cloud Services

> This page details MikroTik RouterOS connections to cloud servers and Mikrotik services, listing sub-menus, domain names, default statuses, and methods to disable communication for each connection type.

# Communication with MikroTik Cloud Services

This table lists information about all connections that can occur from RouterOS to MikroTik servers, as well as instructions on how to disable such connections.

| Sub-menu | Domain name | Enabled/Active by default | Ensuring communication is disabled/inactive |
| :-- | :-- | :-- | :-- |
| **system clock time-zone-autodetect** | cloud2.mikrotik.com | Yes | `/system/clock/set` time-zone-autodetect=no ([See Clock Docs](../../system-information-and-utilities/clock)) |
| **system backup cloud** | cloud2.mikrotik.com | No | Communication is only invoked by upload-file, download-file, remove-file commands. ([See Backup](./index.md#cloud-backup)) |
| **ip cloud update-time** | cloud2.mikrotik.com | Yes | `/ip/cloud/set` update-time=no ([See Update Time](./index.md#update-time)) |
| **ip cloud ddns-enabled** | cloud2.mikrotik.com | No | `/ip/cloud/set` ddns-enabled=auto ([See DDNS](./index.md#ddns)) |
| **ip cloud back-to-home-vpn** | cloud2.mikrotik.com | No | `/ip/cloud/set` back-to-home-vpn=revoked-and-disabled ([See BTH VPN](./back-to-home.md#ip-cloud)) |
| **ip cloud back-to-home-file** | cloud2.mikrotik.com | No | Communication is only invoked by enabling or disabling file sharing in "ip cloud back-to-home-file". ([See File Share](./file-share)) |
| **system license** | licence.mikrotik.com | Yes (relevant only for [CHRs](../../getting-started/routeros-licensing/chr)) | In the case of CHRs, it is impossible to disable communication with the license server using a specific command or setting in RouterOS. ([See CHR License](../../getting-started/routeros-licensing/chr/chr-licensing)) |
| **interface lte firmware-upgrade** | upgrade.mikrotik.com | No | Communication is only invoked by the firmware-upgrade command. ([See LTE Firmware Upgrade](../../mobile-networking/lte-5g.md#modem-firmware-upgrade-command)) |
| **interface detect-internet** | cloud.mikrotik.com | No | `/interface/detect-internet/set` detect-interface-list=none ([See Detect Internet](../../diagnostics-monitoring-and-troubleshooting/detect-internet)) |
| **system package update** | upgrade.mikrotik.com | No | Communication is only initiated by the check-for-updates command and by downloading packages from the upgrade server. ([See Package Updates](../../getting-started/installation-and-upgrade/packages)) |
| **system swos upgrade** | upgrade.mikrotik.com | No | Communication is only invoked by the upgrade command. ([See SWOS Upgrade](../../bridging-and-switching/marvell-prestera-switch-chip-features.md#configuring-swos-using-routeros)) |
