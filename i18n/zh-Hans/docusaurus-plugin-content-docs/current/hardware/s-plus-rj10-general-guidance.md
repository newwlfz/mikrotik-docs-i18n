# S+RJ10 通用指南

> S+RJ10 是 MikroTik 的一款 6 速 RJ45 SFP+ 模块，通过铜缆提供 10 Gbps 速率。本文提供其在 MikroTik 设备中的使用指南，包括在与光模块一同使用或高密度 SFP+ 插槽中时，为避免过热而推荐的放置方式。

# S+RJ10 通用指南

### 概述

[MikroTik S+RJ10](https://mikrotik.com/product/s_rj10) 是一款基于 Marvell 88X3310P 收发器的独特 6 速 RJ-45 SFP+ 模块。它利用双绞铜缆可提供高达 10 Gbps 的速率。所有当前带有 SFP+ 插槽的 MikroTik 设备均支持 S+RJ10 模块。本文作为 S+RJ10 在 MikroTik 设备（包括被动散热和主动散热设备）中使用的指南。

### 通用指南

#### 产品规格

该收发器的平均功耗为 2.7 W（10GBASE-T，30 m 链路），相较于最大功耗为 0.8W 的 [S+85DLC03D](https://mikrotik.com/product/Splus85DLC03D) 光模块而言相对较高。其工作温度为 0 至 +70 C，但收发器自身可升温至 90 C。

#### S+RJ10 在设备中的放置

鉴于较高的工作温度，建议在使用 S+RJ10 收发器时，在其之间放置一个光模块或空闲的 SFP+ 接口。请参阅收发器支持距离的[对比表](../wired-connections/mikrotik-wired-interface-compatibility.mdx#srj10)。

如前所述，S+RJ10 比普通收发器发热更多，并排使用可能导致过热，尤其是在具有 4 个线性 SFP 插槽的设备中。建议每隔一个接口放置 S+RJ10，并在其间保留一个光模块或空端口。

![](https://manual.mikrotik.com/docs/hardware/img/s-plus-rj10-general-guidance-01.webp)

即使在使用带有独立 SFP+ 插槽的设备（例如 CRS309-1G-8S+）时，仍不建议将 S+RJ10 收发器并排部署。请每隔一个接口使用 S+RJ10，以避免收发器过热，从而可能导致不可预测的行为。

![](https://manual.mikrotik.com/docs/hardware/img/s-plus-rj10-general-guidance-02.webp)推荐的 S+RJ10 放置方式![](https://manual.mikrotik.com/docs/hardware/img/s-plus-rj10-general-guidance-03.webp)不建议将收发器并排放置

配备 4 块或 8 块 SFP+ 插槽的设备也不例外。建议每个 4xSFP+ 插槽块使用一个 S+RJ10 收发器，并避免并排放置。在插入 S+RJ10 收发器后，至少保持一个垂直行空闲（不安装 S+RJ10）。

![](https://manual.mikrotik.com/docs/hardware/img/s-plus-rj10-general-guidance-04.webp)推荐的 S+RJ10 放置方式![](https://manual.mikrotik.com/docs/hardware/img/s-plus-rj10-general-guidance-05.webp)我们不建议将收发器并排放置

### 并排使用 S+RJ10 或与被动散热设备配合使用

在某些情况下，可能无法采用推荐的收发器布局。例如，当两个或更多 S+RJ10 收发器并排插入，或模块用于被动散热设备时，网络管理员必须确保额外的散热措施。应增加设备周围的气流，或降低整体环境温度，以使收发器温度保持在推荐范围内。