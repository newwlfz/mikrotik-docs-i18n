# LoRa

> 本页介绍 MikroTik RouterOS 的 LoRa 和 LoRaWAN 配置，涵盖网关设置、通用属性、服务器集成，以及通过 MQTT/HTTP 转发非 LoRaWAN 负载。文中详细说明了支持的硬件、拓扑要素，以及加密负载所需的脚本编写要求。

import DocCardList from '@theme/DocCardList';

# LoRa

本节涵盖 RouterOS 中的 LoRa 和 LoRaWAN 功能。使用它来配置 LoRa 网关、通用属性，以及与受支持的 LoRaWAN 网络的集成。

<DocCardList />

可用设置：

- ## [通用属性](./general-properties.md)

网关初始步骤及不同的 LoRaWAN 设置示例：

- ## [用户指南](./user-guides/index.md)

术语“LoRa”代表“无线电”本身（“LoRa 负载”是节点使用 LoRa 频率广播的数据包），而术语“LoRaWAN”则代表其上的逻辑/链路层，使“LoRa”设备之间能够通信。换句话说，“LoRaWAN”是“LoRa”无线电设备通信的方式。

**R11e-LR8**（工作于 863-870 MHz 频段）、**R11e-LR9**（工作于 902-928 MHz 频段）和 **R11e-LR2**（使用 2.4 GHz 频段）是基于 Semtech 芯片组的 mini PCIe 形态 LoRa® 技术集中器网关卡。它们为任何具有 mPCIe 插槽并连接 USB 线路的 MikroTik 产品提供 LoRa® 连接。

典型的 LoRaWAN 拓扑由 3 个主要元素组成 → 服务器、节点和网关。网关的工作是简单地将节点广播的（在相同支持频段内的）LoRa 数据包转发到服务器。

MikroTik LoRaWAN 网关是装有 R11e-LR**x** miniPCIe 卡并安装了“iot”[软件包](../../getting-started/installation-and-upgrade/packages.md)（启用 LoRa 驱动）的设备。

MikroTik 网关设备的主要设计目标是作为 LoRaWAN 设备运行。要实现这一点，只需在 LoRa 接口设置中配置/选择正确的服务器即可。一些示例可在[用户指南部分](./user-guides/index.md)中找到。

#### 非 LoRaWAN 设置

然而，如果您不希望使用 LoRaWAN 网络/拓扑，而是希望将“原始 LoRa”负载转发到您自己的服务器，您也可以这样做。您可以使用 [MQTT](../mqtt/index.md) 或 [HTTP post](../../system-information-and-utilities/fetch.md) 将接收到的负载转发到您的 MQTT/HTTP 服务器，但这需要额外的[脚本编写](../../developer-guides/scripting/index.md)。脚本必须从 `IoT>LoRa>Traffic` 选项卡收集信息（负载），将这些负载存储为变量，将变量构造成 MQTT/HTTP 消息并发布。

:::info
请注意，如果节点广播的负载是加密的，并且您希望将其转发到您自己的 MQTT/HTTP 服务器（不使用 LoRaWAN），您需要在服务器端解密负载。网关没有内置功能来解密节点数据。服务器负责此任务。

此外，没有选项可以将 MQTT/HTTP 下行消息从 MQTT/HTTP 服务器“中继”回 LoRa 节点（只能将节点的“上行”负载“转发”到服务器），主要是因为无法“使”LR 卡“广播”自定义负载（无法将 MQTT/HTTP 下行消息的内容传递到 LoRa 芯片中）。
:::