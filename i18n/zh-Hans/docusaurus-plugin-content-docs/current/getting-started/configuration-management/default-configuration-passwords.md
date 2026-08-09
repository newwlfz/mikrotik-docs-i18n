# 默认配置密码

> 查找 MikroTik RouterOS 设备出厂或完全重置后的默认登录凭据。

MikroTik 设备出厂时带有默认配置，其中包含预设密码。每当您执行标准系统重置时，该密码会重新应用。了解如何找到此密码对于初始设备访问至关重要。

:::tip[观看我们的官方解说视频]
[默认密码：为什么？！](https://www.youtube.com/watch?v=mq7nIIILrVc) — 简要概述 MikroTik 设备为何现在配备独特的出厂密码。
:::

早期的 MikroTik 型号通常使用用户名 `admin` 且无密码——在登录时输入 `admin`，并在提示时按 **Enter** 键。较新的型号每台设备都配有独特的默认密码。

:::note[定制品牌设备]
定制品牌或 OEM 设备可能具有不同的默认密码。如果您找不到标准标签，仍可通过 **[Netinstall 工具](../installation-and-upgrade/netinstall)** 重置设备。
:::

## 密码查找位置

默认密码印在以下几个物理位置：

- 设备本身上的序列号标签上
- 设备包装上的序列号标签上
- 产品盒内附带的印刷快速指南页上

部分 MikroTik [室内无线](https://mikrotik.com/products/indoor-wireless) 设备（如 [hAP ac³](https://mikrotik.com/product/hap_ac3) 和 [hAP ax³](https://mikrotik.com/product/hap_ax3)）设有专用的 **产品信息舱**——设备底部的一个小面板，内藏带有默认凭据的标签。请在以太网端口附近或射频连接器盖板下方寻找该舱位。打开面板即可看到内部标签上印制的序列号和默认密码。

:::warning

在联系支持人员之前，请务必检查这些标签。密码仅印在物理材料上——不会以数字形式存储在任何在线系统中。

:::

## 如果找不到密码

如果标签缺失或无法辨认，请联系供应设备的 MikroTik 分销商。提供设备序列号和购买该设备的卖家或商店名称。分销商维护有密码数据库，可通过序列号检索默认密码。

:::tip

观看我们的视频指南：[用于无缝配置的秘密 CSV 密码文件](https://www.youtube.com/watch?v=q9F871KkGBw) — 了解如何使用 CSV 密码文件进行自动化设备设置。

:::

如果您无法联系到分销商或密码无法检索，您仍可通过使用 **[Netinstall](../installation-and-upgrade/netinstall)** **重新安装 RouterOS** 或执行 **[完全配置重置](./routeros-configuration-reset)** 来重新获得访问权限。

:::tip[使用 Flashfig 进行批量配置]

如需大规模部署多台设备，请使用 Flashfig 工具：

- [使用 flashfig 批量配置 MikroTik](https://www.youtube.com/watch?v=gticPeOdN54)（Windows）
- [从 Linux 使用 flashfig 批量配置 MikroTik](https://www.youtube.com/watch?v=xasM81Qc11g)（Linux）

:::