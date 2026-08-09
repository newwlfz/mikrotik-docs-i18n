# 802.11 a/b/g/n

> MikroTik 802.11 a/b/g/n 设备使用由 wireless 软件包提供的传统 /interface/wireless 菜单。本节涵盖无线接口、MikroTik 专有协议（Nstreme、Nv2）、HWMP+ mesh、互通配置文件、频谱扫描、/caps-man CAPsMAN 控制器及相关案例研究。

# 802.11 a/b/g/n

import DocCardList from '@theme/DocCardList';

本节涵盖 MikroTik **802.11 a/b/g/n** 设备（以及任何运行 `wireless` 软件包的 802.11ac 设备），通过 **`/interface/wireless`** 菜单（**`wireless`** 驱动软件包）进行配置——这是基于 MIPS 设备上的唯一选项。

该菜单也是 MikroTik 专有的、面向吞吐量特性的所在地——**Nstreme** 和 **Nv2**（TDMA）、**WDS** 以及 **HWMP+ mesh**——以及原始的 **[CAPsMAN](./capsman/ap-controller-capsman.md)**（`/caps-man`）控制器。

:::info
部分 802.11ac 设备可以通过 `wifi-qcom-ac` 软件包运行新的 `/interface/wifi` 菜单——请参阅 [Wi-Fi 5 (802.11ac)](../wifi-ac/index.md) 进行选择。WPA3 和快速漫游仅可通过新菜单使用。
:::

<DocCardList />