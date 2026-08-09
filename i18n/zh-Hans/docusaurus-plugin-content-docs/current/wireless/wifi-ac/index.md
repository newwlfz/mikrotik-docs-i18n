# Wi-Fi 5 (802.11ac)

> MikroTik 802.11ac (Wi-Fi 5) ARM 设备可通过两种方式驱动：使用 `wifi-qcom-ac` 包通过新的 `/interface/wifi` 菜单（支持 WPA3、快速漫游、新版 CAPsMAN），或使用 `wireless` 包通过传统的 `/interface/wireless` 菜单（支持 Nstreme、Nv2、旧版 CAPsMAN）。本页帮助您在两者之间做出选择，并提供相应的配置参考链接。

# Wi-Fi 5 (802.11ac)

本节涵盖 MikroTik **802.11ac (Wi-Fi 5)** ARM 架构设备。这些产品较为特殊：**同一硬件可根据所安装的驱动包，通过两个 RouterOS 菜单中的任意一个进行配置**。请根据您所需的功能选择其一。
:::warning
`wifi-qcom-ac` 驱动资源占用较高。我们建议使用我们的 WiFi 5 (802.11ac) 设备时保留其原有的 `wireless` 驱动，因其更为轻量。
:::

## 运行 802.11ac 设备的两种方式

| 如果您需要… | 安装包 | 配置位置 | 文档 |
| :-- | :-- | :-- | :-- |
| WPA3、快速漫游 (802.11r)、新版 CAPsMAN | `routeros` + `wifi-qcom-ac` | `/interface/wifi` | [Wi-Fi 6 / 7 (802.11ax/be)](../wifi/index.md) — `/interface/wifi` 菜单为共用 |
| Nstreme、Nv2、WDS、HWMP+ mesh、旧版 CAPsMAN | `routeros` + `wireless` | `/interface/wireless` | [802.11 a/b/g/n](../abgn/index.md) — `/interface/wireless` 菜单为共用 |

您无法在内置无线接口上同时使用这两个包 — 有关切换方法，请参阅 [替换 'wireless' 包](../wifi/index.md)。

:::info
新的 `/interface/wifi` 菜单管理 **Wi-Fi 5 wave2 及更新版本**的接口，因此运行 `wifi-qcom-ac` 的 802.11ac 设备与 [Wi-Fi 6 / 7 (802.11ax/be)](../wifi/index.md) 文档中所述的 802.11ax/be 设备使用完全相同的配置。因此，本节直接链接至该参考文档，不再重复编写。
:::

## 可选择驱动的设备

以下 802.11ac ARM 型号可运行 `wifi-qcom-ac`（新 `/interface/wifi` 菜单）或 `wireless`（传统 `/interface/wireless` 菜单）：

> Audience、Audience LTE kit、Chateau（D53 全系列）、hAP ac²、hAP ac³、cAP ac、cAP XL ac、LDF 5 ac、LHG XL 5 ac、LHG XL 52 ac、NetMetal ac²、mANTBox 52 15s、wAP ac (RBwAPG-5HacD2HnD)、SXTsq 5 ac

如需根据设备类型和 CAPsMAN 场景选择包，请参阅 [无线概览](../index.md) 中的决策表。