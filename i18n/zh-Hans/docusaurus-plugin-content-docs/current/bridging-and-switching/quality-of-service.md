# 服务质量（QoS）

> 本文档介绍了 MikroTik RouterOS 中针对搭载 Marvell Prestera 交换芯片设备的服务质量（QoS）功能，详细说明了 QoS 优先级划分、流量整形和拥塞管理。内容涵盖 RouterOS v7.23 的增强功能，如无损流量支持、动态缓冲区，以及适用于各种交换机型号的 QoS 设备兼容性表。

import WideTable from '@site/src/components/WideTable';

# 服务质量（QoS）

本文档描述了 RouterOS 中针对搭载 **[Marvell Prestera 交换芯片](./marvell-prestera-switch-chip-features.md)** 的设备的 **服务质量（QoS）** 实现。

QoS 是网络交换机中的一组功能集合，允许网络管理员对流量进行优先级排序并分配网络资源，以确保关键数据流以低延迟平稳传输。

网络交换机中 QoS 的主要功能是以满足不同类型网络应用特定需求的方式来管理流量。例如，语音和视频数据需要低延迟和最小化数据包丢失以确保高质量的通信，而文件传输和其他数据应用则可以容忍较高的延迟和数据包丢失。

QoS 通过识别流经交换机的流量类型，并根据其需求分配优先级级别来工作。然后，交换机利用此信息修改数据包头并优先处理流量流，确保高优先级流量比低优先级流量获得更优的处理。

需要 RouterOS v7.15 或更高版本才能支持所有 QoS 功能：

1.  **QoS 标记。** 根据入站数据包头匹配 QoS 配置文件，然后根据分配的 QoS 配置文件在出站时修改数据包头。
2.  **QoS 执行。** 根据分配的 QoS 配置文件和流量整形来避免或解决拥塞。
3.  **QoS 策略。** 通过 ACL 规则分配 QoS 配置文件。
4.  主动队列管理：**WRED**（加权随机早期检测）、**ECN** 通知和处理、**PFC**（基于优先级的流控）。
5.  流量整形。

### RouterOS v7.23 中的 QoS 变更

RouterOS v7.23 引入了对服务质量（QoS）卸载的重大变更。这些变更简化了配置过程，并增加了对“无损”流量类别的支持。尽管硬件资源是有限的，但当所有连接的设备都支持并正确配置了 ECN 和/或 PFC 时，使用 ECN 和/或 PFC 的主动队列管理可以防止数据包丢失。以前的 RouterOS 版本已经支持 ECN 和 PFC，但 v7.23 简化了它们的设置方式。

:::info
并非所有设备都支持无损流量。请查看 QoS 设备支持表。
:::

#### 配置变更摘要

-   QoS 设置：大多数设置默认设为“自动”，允许 RouterOS 为配置选择最佳已知设置。
-   QoS 设置：新增了 `lossless-traffic-class` 和 `lossless-buffers`，允许显式指定无损流量并为其预留队列资源。用户也可以将这些字段保留为“自动”。
-   QoS 监视器：分别显示有损和无损的共享池使用情况。
-   Tx 队列：移除了共享池索引。RouterOS 根据流量类型（有损或无损）自动选择共享池。
-   QoS 配置文件：新增了到指定 PCP 和 DSCP 值的自动映射（默认启用）。例如，添加一个 DSCP=46 的 QoS 配置文件会自动将该配置文件应用于从受信任端口接收的流量。

## QoS 术语

本节定义了本文档中使用的关键术语和缩写：

-   **QoS** - 服务质量，允许网络管理员对流量进行优先级排序并分配网络资源的功能集合。
-   **ACL** - 访问控制列表，一组用于根据指定标准过滤网络流量的交换机规则。
-   **AQM** - 主动队列管理，一种拥塞控制机制，通过在队列溢出前丢弃或标记数据包来管理流量流。
-   **DSCP** - 差分服务代码点，IP 头中的 6 位字段，用于对网络流量进行优先级排序。
-   **ECN** - 显式拥塞通知，一种允许路由器在不丢弃数据包的情况下向端点设备发出拥塞信号的机制。
-   **ETS** - 增强传输选择，一种流量调度方法，使用加权循环在多个队列组之间分配带宽。
-   **PCP** - 优先级代码点，VLAN 头中的 3 位字段，用于在 VLAN 内对流量进行优先级排序。
-   **PFC** - 基于优先级的流控（IEEE 802.1Qbb），一种流控机制，通过暂停特定优先级队列上的流量来防止数据包丢失。
-   **RoCE** - 融合以太网上的 RDMA，一种协议，支持在以太网上实现远程直接内存访问。
-   **WRED** - 加权随机早期检测，一种拥塞避免机制，当队列接近容量时随机丢弃数据包。
-   **/in/eth/sw/** - `/interface/ethernet/switch/` 的 CLI 快捷方式。

## 新一代 Marvell Prestera 交换芯片的 QoS 增强功能

搭载新一代 Marvell Prestera 交换芯片（例如运行 [switch-marvell 包](../getting-started/installation-and-upgrade/packages.md#extra-packages) 的 CRS8xx 系列）的 MikroTik 设备在 QoS 执行方面提供了新方法。以前的型号需要在保证的 Tx 队列缓冲区和共享 Tx 队列缓冲区之间做出权衡。通过增加共享缓冲区百分比，设备可以吸收更大的流量突发，但同时，一个拥塞的端口可能会占用所有共享缓冲区，从而限制了其他端口的 QoS 能力。使用新一代交换芯片通过引入**动态缓冲区**实现了两全其美。交换芯片根据当前拥塞级别动态调整端口和队列缓冲区限制。如果设备内部没有拥塞，单个端口可以吸收大量流量突发，防止数据包丢失。当多个端口的 Tx 队列大小增加时，设备会减少每端口和每队列的限制，强制公平使用共享资源，同时确保为非拥塞队列提供足够的缓冲区以继续转发流量。整个过程是自动化的，无需用户进行任何配置。

新一代 Marvell Prestera 交换芯片的另一个改进是消除了用于存储控制数据的入队数据包描述符短缺问题。上一代设备有 Packet Cap 和 Use 统计信息。当设备接收到小数据包突发时，即使它有足够的队列缓冲区来存储有效负载，也可能因为达到 Packet Cap 而开始尾丢弃数据包。新一代设备确保始终有足够的内存来存储控制数据，使动态缓冲区大小成为唯一的限制因素。这就是新一代设备中没有 Packet Cap/Use 统计信息的原因。

新一代设备要求始终启用 QoS 硬件卸载（**qos-hw-offloading=yes**）。RouterOS 会忽略用户禁用它（该功能）的请求，同时保留该字段以实现向后兼容。

## QoS 设备支持

<WideTable>

| 交换芯片 | 型号 | QoS 配置文件 | QoS 映射 | Tx 管理器 | WRED | ECN | PFC | 无损缓冲区 | 动态缓冲区 | 端口/队列使用统计 |
| :-- | :-- | --: | --: | --: | :-- | :-- | :-- | :-- | :-- | :-- |
| **98DX3236** | CRS305-1G-4S+IN CRS326-24G-2S+ (RM/IN) CRS328-24P-4S+RM CRS328-4C-20S-4S+RM | 128 | 1 | 8 |  |  |  |  |  | 当前值 |
| **98DX226S** | CRS305-1G-4S+OUT (FiberBox Plus) CRS310-1G-5S-4S+ (netFiber 9/IN) CRS310-8G+2S+IN CRS318-16P-2S+OUT (netPower 16P) CRS320-8P-8B-4S+RM CRS418-8P-8G-2S+RM CRS418-8P-8G-2S+5axQ2axQ-RM | 128 | 1 | 8 |  |  |  |  |  | 当前值 |
| **98DX224S** | CRS318-1Fi-15Fr-2S-OUT (netPower 15FR) | 128 | 1 | 8 |  |  |  |  |  | 当前值 |
| **98DX2528** | CRS304-4XG-IN | 128 | 1 | 8 |  |  |  |  |  | 当前值 |
| **98DX8525** | CCR2216-1G-12XS-2XQ CRS518-16XS-2XQ-RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 最大填充 <sup>1</sup> |
| **98DX4310** | CRS504-4XQ (IN/OUT) CRS510-8XS-2XQ-IN RDS2216-2XG-4S+4XS-2XQ | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 最大填充 <sup>1</sup> |
| **98DX8208** | CRS309-1G-8S+IN | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 当前值 <sup>2</sup> |
| **98DX8212** | CRS312-4C+8XG-RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 当前值 <sup>2</sup> |
| **98DX8216** | CRS317-1G-16S+RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 当前值 <sup>2</sup> |
| **98DX8332** | CRS326-24S+2Q+RM CRS326-4C+20G+2Q+RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 当前值 <sup>2</sup> |
| **98DX3257** | CRS354-48G-4S+2Q+RM CRS354-48P-4S+2Q+RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 当前值 <sup>2</sup> |
| **98DX3255** | CCR2116-12G-4S+ | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 当前值 <sup>2</sup> |
| **98CX8410** | CRS520-4XS-16XQ-RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 不可用 <sup>3</sup> |
| **98DX7335** | CRS812-8DS-2DQ-2DDQ-RM CRS804-4DDQ-hRM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ | ✔ | 当前值 + 最大填充 |

</WideTable>

<sup>**1**</sup> 设备收集最大队列填充统计信息，而不是显示当前使用值。使用 `reset-counters` 命令清除这些统计信息。
<sup>**2**</sup> 由于硬件限制，某些交换芯片型号在读取或轮询 QoS 端口/队列使用数据时可能会遇到暂时的流量中断。
<sup>**3**</sup> 无法获取端口上单个队列的使用数据；只能访问整个物理端口的聚合总使用量。

## 应用与使用示例

---

### 基本配置示例

此示例演示了如何在标准尽力而为（Best Effort）类别之上为 VoIP（IP 电话）配置单个 QoS 级别。该配置使用 CRS326-24G-2S+ 设备，设置如下：

-   所有端口均已桥接并使用 **[vlan-filtering](index.md#bridge-vlan-filtering)**；
-   sfp-sfpplus1 作为连接到另一台交换机的 VLAN 中继；
-   ether1 至 ether9 是 IP 电话的专用端口；
-   ether10 至 ether24 是用于主机连接的标准端口。

首先，定义一个 QoS 配置文件。此配置文件指定了将在出站时应用于转发数据包的 DSCP 和 PCP 值：

```ros
/interface/ethernet/switch/qos/profile
add dscp=46 name=voip pcp=5 traffic-class=5
```

接下来，将 VoIP QoS 配置文件分配给 IP 电话的专用端口。这会将配置文件应用于这些端口的入站流量。所有其他以太网端口将使用默认配置文件（其中 dscp=0 且 pcp=0）：

```ros
/interface/ethernet/switch/qos/port
set ether1 profile=voip
set ether2 profile=voip
set ether3 profile=voip
set ether4 profile=voip
set ether5 profile=voip
set ether6 profile=voip
set ether7 profile=voip
set ether8 profile=voip
set ether9 profile=voip
```

中继端口接收两种类型的 QoS 流量。为了区分它们，启用 trust-l3 和 trust-l2：

```ros
/interface/ethernet/switch/qos/port
set sfp-sfpplus1 trust-l3=trust trust-l2=trust
```

> **注意：** 如果您运行的是 RouterOS 7.23 或更高版本，VLAN 优先级和 IP DSCP 映射会自动创建，因此此步骤不是必需的。如果您使用的是较早的 RouterOS 版本，则必须使用 QoS 配置文件手动创建 VLAN 优先级和 IP DSCP 映射：

```routeros
/interface/ethernet/switch/qos/map/ip
add dscp=46 profile=voip

/interface/ethernet/switch/qos/map/vlan
add pcp=5 profile=voip
```

最后，启用 QoS 硬件卸载以使上述设置生效：

```ros
/interface/ethernet/switch
set switch1 qos-hw-offloading=yes
```

您可以使用 `print` 命令验证端口 QoS 设置：

```ros
[admin@MikroTik] /interface/ethernet/switch/qos/port/print
Column: NAME, SWITCH, PROFILE, MAP, TRUST-L2, TRUST-L3
 # NAME          SWITCH   PROFILE  MAP      TRUST-L2  TRUST-L3  TX-MANAGER
 0 ether1        switch1  voip     default  ignore    ignore    default
 1 ether2        switch1  voip     default  ignore    ignore    default
 2 ether3        switch1  voip     default  ignore    ignore    default
 3 ether4        switch1  voip     default  ignore    ignore    default
 4 ether5        switch1  voip     default  ignore    ignore    default
 5 ether6        switch1  voip     default  ignore    ignore    default
 6 ether7        switch1  voip     default  ignore    ignore    default
 7 ether8        switch1  voip     default  ignore    ignore    default
 8 ether9        switch1  voip     default  ignore    ignore    default
 9 ether10       switch1  default  default  ignore    ignore    default
10 ether11       switch1  default  default  ignore    ignore    default
11 ether12       switch1  default  default  ignore    ignore    default
12 ether13       switch1  default  default  ignore    ignore    default
13 ether14       switch1  default  default  ignore    ignore    default
14 ether15       switch1  default  default  ignore    ignore    default
15 ether16       switch1  default  default  ignore    ignore    default
16 ether17       switch1  default  default  ignore    ignore    default
17 ether18       switch1  default  default  ignore    ignore    default
18 ether19       switch1  default  default  ignore    ignore    default
19 ether20       switch1  default  default  ignore    ignore    default
20 ether21       switch1  default  default  ignore    ignore    default
21 ether22       switch1  default  default  ignore    ignore    default
22 ether23       switch1  default  default  ignore    ignore    default
23 ether24       switch1  default  default  ignore    ignore    default
24 sfp-sfpplus1  switch1  default  default  trust     ignore    default
25 sfp-sfpplus2  switch1  default  default  ignore    ignore    default
26 switch1-cpu   switch1   
```

使用此配置，在端口 ether1 至 ether9 上接收的入站数据包被标记为优先级代码点（PCP）值 5 和差分服务代码点（DSCP）值 46。在端口 ether10 至 ether24 上接收的入站数据包被标记为 PCP 和 DSCP 值 0。当在 sfp-sfpplus1 端口上接收到数据包时，任何 PCP 值为 5 的数据包保留其 PCP 值 5 和 DSCP 值 46，而所有其他数据包被标记为 PCP 和 DSCP 值 0。

## Dante

从 RouterOS v7.15 开始，所有支持 QoS 的 MikroTik 设备都与 Dante 音频网络兼容。

Dante 硬件使用以下 DSCP/Diffserv 优先级值进行流量优先级划分：

| Dante 优先级 | 用途 | DSCP 标签 | DSCP 值 |
| :-- | :-- | :-- | --: |
| 高 | 时间关键的 PTP 事件 | CS7 | 56 |
| 中 | 音频， PTP | EF | 46 |
| 无 | 其他流量 | BE | 0 |

此示例假定交换机使用其默认配置，其中包括一个默认桥接接口，所有以太网接口都已添加为桥接端口。这些接口中的任何一个都可以用于 Dante。

首先，创建 QoS 配置文件以匹配 Dante 流量类别。已有一个预先存在的“default”配置文件，对应于 Dante 的 None 优先级。

```ros
/interface/ethernet/switch/qos/profile
add name=dante-ptp dscp=56 pcp=7 traffic-class=7
add name=dante-audio dscp=46 pcp=5 traffic-class=5
```

如果您运行的是 RouterOS 7.23 或更高版本，IP DSCP 映射会自动创建，因此此步骤不是必需的。如果您使用的是较早的 RouterOS 版本，请创建 QoS 映射以根据 DSCP 值匹配 QoS 配置文件：

```ros
/interface/ethernet/switch/qos/map/ip
add dscp=56 profile=dante-ptp
add dscp=46 profile=dante-audio
```

配置硬件队列以对 Dante 流量执行 QoS：

```ros
/interface/ethernet/switch/qos/tx-manager/queue
set [find where traffic-class=7] schedule=strict-priority
set [find where traffic-class=5] schedule=strict-priority
```

Dante 的高优先级和中优先级流量按严格优先级顺序调度。设备传输时间关键的 PTP 数据包直到 queue7 为空，然后继续传输音频（queue5）。仅当 PTP 和音频队列为空时，才传输其他流量。

下一步是为传入的第 3 层数据包（IP DSCP 字段）启用信任模式：

```ros
/interface/ethernet/switch/qos/port
set [find] trust-l3=keep
```

最后，启用 QoS 硬件卸载以使上述设置生效：

```ros
/interface/ethernet/switch
set switch1 qos-hw-offloading=yes
```

在组播模式下使用 Dante 时，在交换机上启用 IGMP Snooping 是有益的。此功能仅将流量定向到具有订阅设备的端口，防止不必要的泛洪。此外，启用 IGMP Querier（如果同一 LAN 中的另一台设备尚未启用）、调整查询间隔以及激活 fast-leave 可以进一步优化组播性能。

```ros
/interface/bridge
set [find name=bridge] igmp-snooping=yes multicast-querier=yes query-interval=60s

/interface/bridge/port
set [find] fast-leave=yes
```

## 融合以太网上的 RDMA (RoCE)

RoCE 支持在不涉及主机 CPU 的情况下，通过以太网网络对远程存储系统进行直接内存访问。这显著降低了延迟和 CPU 开销，使 RoCE 成为高性能计算和数据中心环境的理想选择。RoCE 还允许融合网络，其中各种服务（如数据存储、网络和多媒体的）在单个以太网基础设施上运行，简化了网络管理，并降低了维护独立网络的成本和复杂性。

RoCE 通过使用 **ECN** 和 **PFC** 机制实现这一点。这些功能有助于防止网络拥塞和数据包丢失，确保可靠、无损的通信。有关兼容的交换机，请参阅[设备功能表](quality-of-service.md#qos-device-support)。虽然交换机可以支持 RoCE 环境，但终端主机也必须兼容 RoCE 协议，并配备支持 RDMA 的网络接口卡（NIC）。

RoCE 有两个主要版本。RoCEv1 作为以太网链路层协议运行，使用 Ethertype 0x8915。RoCEv2 在标准 IP 网络上工作，使用 UDP 目标端口号 4791。IP 头中的 ECN 位被标记以指示网络拥塞，并使用拥塞通知包（CNP）向发送方确认拥塞。对于流量优先级划分，RoCEv2 流量使用 DSCP 26，而 CNP 使用 DSCP 48。

以下示例可用于使用 PFC 和 ECN 的无损 RoCEv2，并假定交换机使用其默认配置，其中包括一个默认桥接接口，所有以太网接口都已添加为桥接端口。最低推荐的 RouterOS 版本是 7.17。

首先，配置额外的配置文件。非 RoCE 流量将被分配到已存在的“default”配置文件（traffic-class 1），RoCEv2 分配到 traffic-class 3，CNP 分配到 traffic-class 6。

```routeros
/interface/ethernet/switch/qos/profile
add dscp=26 name=roce traffic-class=3
add dscp=48 name=cnp traffic-class=6
```

如果您运行的是 RouterOS 7.23 或更高版本，IP DSCP 映射会自动创建，因此此步骤不是必需的。如果您使用的是较早的 RouterOS 版本，请创建 QoS 映射以根据 DSCP 值匹配 QoS 配置文件。

```routeros
/interface/ethernet/switch/qos/map/ip
add dscp=26 profile=roce
add dscp=48 profile=cnp
```

配置硬件队列和调度器。对 traffic-class 1 和 traffic-class 3 使用 ETS（`schedule=high-priority-group`），各自分配 50% 的带宽（`weight=1`），并对 traffic-class 6 使用严格优先级调度。此外，为 traffic-class 3 启用 ECN（`ecn=yes`），以标记交换机中遇到拥塞的 IP 数据包。

```routeros
/interface/ethernet/switch/qos/tx-manager/queue
set 1 schedule=high-priority-group weight=1
set 3 schedule=high-priority-group weight=1 ecn=yes
set 6 schedule=strict-priority
```

:::tip
虽然使用 `schedule=low-priority-group` 允许您为不同的流量类别集创建单独的 ETS 调度和带宽分配，但不建议将此设置与 `lldp-dcbx=yes` 一起使用。原因是 ETS 配置/推荐 TLV 旨在处理跨流量类别的单一带宽分配，因此应使用 `schedule=high-priority-group`。
:::

为 traffic-class 3 配置 PFC 配置文件，以确保 RoCEv2 流量的无损环境。

```routeros
/interface/ethernet/switch/qos/priority-flow-control
add name=pfc-tc3 rx=yes traffic-class=3 tx=yes
```

在预期有 RoCEv2 流量的交换机端口上设置第 3 层信任模式（`trust-l3=keep`）。设置 PFC（`pfc=pfc-tc3`）和 queue3 的出口速率以符合 PFC 要求（`egress-rate-queue3=10.0Gbps`）。在此示例中，使用了 10Gbps SFP+ 接口，出口速率可以设置为匹配接口的物理速度。根据您的接口速度更改此属性。

```routeros
/interface/ethernet/switch/qos/port
set sfp-sfpplus1 egress-rate-queue3=10.0Gbps pfc=pfc-tc3 trust-l3=keep
set sfp-sfpplus2 egress-rate-queue3=10.0Gbps pfc=pfc-tc3 trust-l3=keep
set sfp-sfpplus3 egress-rate-queue3=10.0Gbps pfc=pfc-tc3 trust-l3=keep
set sfp-sfpplus4 egress-rate-queue3=10.0Gbps pfc=pfc-tc3 trust-l3=keep
```

启用 QoS 硬件卸载以使上述设置开始工作。

```routeros
/interface/ethernet/switch
set switch1 qos-hw-offloading=yes
```

启用 LLDP 数据中心桥接能力交换协议（DCBX），以与其他邻居设备共享 QoS 设置和能力。

```routeros
/ip/neighbor/discovery-settings
set lldp-dcbx=yes
```

作为可选步骤，增加 L2MTU 以容纳更大的数据包。

```routeros
/interface/ethernet
set [find switch=switch1] l2mtu=9500
```

## QoS 标记

---

### 理解映射范围

为避免单独定义每个可能的 PCP 和 DSCP 映射，RouterOS 允许您在创建 QoS 配置文件映射时为 PCP 和 DSCP 指定多个值或范围。

在此示例中，PCP 值 0 和 2 使用默认 QoS 配置文件，值 1 和 3-4 使用 streaming 配置文件，值 5 使用 voip 配置文件，值 6-7 使用 control 配置文件：

```ros
/interface/ethernet/switch/qos/map/vlan
add pcp=1,3-4 profile=streaming
add pcp=5 profile=voip
add pcp=6-7 profile=control
```

这种方法通过将相关的优先级值分组在一起，而不是为每个单独的值创建单独的映射规则，从而简化了配置。

### 理解端口、配置文件和映射的关系

每个交换机端口都有第 2 层和第 3 层信任设置，这些设置将改变入站数据包如何被分类到 QoS 配置文件，以及将使用哪些 PCP 和 DSCP 值。下表描述了所有可能的选项：

| **qos-trust-l2** | **qos-trust-l3** | 行为 |
| :-- | :-- | :-- |
| **ignore** | **ignore** | 该端口被视为不受信任。两个头部都被忽略，端口的 **profile** 被强制应用于所有入站数据包。这是默认设置。 |
| **ignore** | **trust** | 信任第 3 层头部。使用入站数据包 IP 头中的 DSCP 字段进行 QoS 配置文件查找（参见 `/in/eth/sw/qos/map/ip`）。如果查找失败（没有 QoS 配置文件映射到给定的 DSCP 值），则使用 **default** QoS 配置文件（不是交换机端口的 QoS 配置文件）。交换机端口的 **profile** 字段仅用于非 IP 流量。 |
| **ignore** | **keep** | 信任第 3 层头部。使用入站数据包 IP 头中的 DSCP 字段进行 QoS 配置文件查找（参见 `/in/eth/sw/qos/map/ip`）。如果查找失败，则使用 **default** QoS 配置文件。交换机端口的 **profile** 字段仅用于非 IP 流量。如果转发/路由的数据包带有 VLAN 标签，则其 PCP 值根据所选 QoS 配置文件设置。但是，数据包的原始 DSCP 值保持不变。 |
| **trust** | **ignore** | 信任第 2 层头部，但忽略 L3。如果入站数据包带有 VLAN 标签，则使用 VLAN 头中的 PCP 字段进行 QoS 配置文件查找（参见 `/in/eth/sw/qos/map/vlan`）。如果查找失败（没有 QoS 配置文件映射到给定的 PCP 值），则使用 **default** QoS 配置文件。交换机端口的 **profile** 字段仅用于未标记的流量。 |
| **trust** | **trust** | 信任两个头部，但第 3 层具有更高优先级。对于 IP 数据包，使用 DSCP 字段进行 QoS 配置文件查找（参见 `/in/eth/sw/qos/map/ip`）。如果 DSCP 到 QoS 的查找失败，则使用 **default** 配置文件。如果数据包不是 IP 数据包但带有 VLAN 标签，则使用 VLAN 头中的 PCP 字段进行 QoS 配置文件查找（参见 `/in/eth/sw/qos/map/vlan`）。如果 VLAN 到 QoS 的查找失败，则使用 **default** QoS 配置文件。非 IP 未标记数据包使用交换机端口的 **profile**。 |
| **trust** | **keep** | 与 **trust+trust** 相同，但转发/路由的数据包中保留原始 DSCP 值。 |
| **keep** | **ignore** | 信任第 2 层头部，但忽略 L3。如果入站数据包带有 VLAN 标签，则使用 VLAN 头中的 PCP 字段进行 QoS 配置文件查找（参见 `/in/eth/sw/qos/map/vlan`）。如果查找失败（没有 QoS 配置文件映射到给定的 PCP 值），则使用 **default** QoS 配置文件。交换机端口的 **profile** 字段仅用于未标记的流量。如果数据包在入站和出站时都带有 VLAN 标签，则保留原始 PCP 值。 |
| **keep** | **trust** | 信任两个头部，但第 3 层具有更高优先级。对于 IP 数据包，使用 DSCP 字段进行 QoS 配置文件查找（参见 `/in/eth/sw/qos/map/ip`）。如果 DSCP 到 QoS 的查找失败，则使用 **default** 配置文件。如果数据包不是 IP 数据包但带有 VLAN 标签，则使用 VLAN 头中的 PCP 字段进行 QoS 配置文件查找（参见 `/in/eth/sw/qos/map/vlan`）。如果 VLAN 到 QoS 的查找失败，则使用 **default** QoS 配置文件。非 IP 未标记数据包使用交换机端口的 **profile**。如果数据包在入站和出站时都带有 VLAN 标签，则保留原始 PCP 值。转发/路由的数据包中的 DSCP 值根据所选 QoS 配置文件设置。 |
| **keep** | **keep** | 信任两个头部，但第 3 层具有更高优先级。对于 IP 数据包，使用 DSCP 字段进行 QoS 配置文件查找（参见 `/in/eth/sw/qos/map/ip`）。如果 DSCP 到 QoS 的查找失败，则使用 **default** 配置文件。如果数据包不是 IP 数据包但带有 VLAN 标签，则使用 VLAN 头中的 PCP 字段进行 QoS 配置文件查找（参见 `/in/eth/sw/qos/map/vlan`）。如果 VLAN 到 QoS 的查找失败，则使用 **default** QoS 配置文件。非 IP 未标记数据包使用交换机端口的 **profile**。在分别处理 VLAN 标记和/或 IP 数据包的情况下，保持原始 PCP 和/或 DSCP 值不变。 |

<WideTable>

| **端口设置** |  | 所选 QoS 配置文件以及转发/路由数据包中 PCP / DSCP 字段值的来源 |  |  |  |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **qos-trust-l2** | **qos-trust-l3** | VLAN 标记的 IP |  |  | 未标记的 IP |  |  | VLAN 标记的非 IP |  |  | 未标记的非 IP |  |  |
|  |  | QoS 配置文件 | PCP | DSCP | QoS 配置文件 | PCP <sup>1</sup> | DSCP | QoS 配置文件 | PCP | DSCP | QoS 配置文件 | PCP <sup>1</sup> | DSCP |
| ignore | ignore | profile | profile | profile | profile | profile | profile | profile | profile | - | profile | profile | - |
| ignore | trust | map/ip | map/ip | map/ip | map/ip | map/ip | map/ip | profile | profile | - | profile | profile | - |
| ignore | keep | `/map/ip` | `/map/ip` | original | `/map/ip` | `/map/ip` | original | profile | profile | - | profile | profile | - |
| trust | ignore | map/vlan | map/vlan | map/vlan | profile | profile | profile | map/vlan | map/vlan | - | profile | profile | - |
| trust | trust | `/map/ip` | `/map/ip` | `/map/ip` | `/map/ip` | `/map/ip` | `/map/ip` | `/map/vlan` | `/map/vlan` | - | profile | profile | - |
| trust | keep | `/map/ip` | `/map/ip` | original | `/map/ip` | `/map/ip` | original | `/map/vlan` | `/map/vlan` | - | profile | profile | - |
| keep | ignore | map/vlan | original | map/vlan | profile | profile | profile | map/vlan | original | - | profile | profile | - |
| keep | trust | map/ip | original | map/ip | map/ip | profile | map/ip | map/vlan | original | - | profile | profile | - |
| keep | keep | map/ip | original | original | map/ip | profile | original | map/vlan | original | - | profile | profile | - |

</WideTable>

<sup>**1**</sup> 仅当入站流量未标记，但出站接口要求帧带有 VLAN 标签时适用。

### 通过交换机规则（ACL）进行 QoS 标记

从 **RouterOS v7.15** 开始，您可以使用交换机规则（ACL）为网络流量分配 QoS 配置文件。此方法允许基于各种数据包属性进行灵活的流量分类。

**子菜单：** `/interface/ethernet/switch/rule`

| 新增/更改的属性 | 描述 |
| :-- | :-- |
| **new-qos-profile** (*名称*) | 要分配给匹配数据包的 [QoS 配置文件](#qos-profile) 的名称。 |
| **keep-qos-fields** (*yes \| no*; 默认值：**no**) | 是否应保留 QoS 字段（PCP、DSCP）的原始值（*yes*），还是替换为分配的 QoS 配置文件中的值（*no*）？仅在设置了 **new-qos-profile** 时相关。 |
| **new-vlan-priority** (*0..7*) | 已弃用，应替换为相应的 **new-qos-profile**。为向后兼容而保留。仅在 qos-hw-offloading=no 时相关。 |

以下示例根据源 MAC 地址分配 QoS 配置文件：

```ros
/interface/ethernet/switch/rule
add new-qos-profile=stream port=ether1,ether2 src-mac-address=00:01:02:00:00:00/FF:FF:FF:00:00:00 switch=switch1
add new-qos-profile=voip port=ether1,ether2 src-mac-address=04:05:06:00:00:00/FF:FF:FF:00:00:00 switch=switch1
```

## QoS 执行

### 硬件队列

每个交换机端口有八个硬件传输（Tx）队列（queue0 到 queue7）。每个队列对应一个由 [QoS 配置文件](#qos-profile) 定义的流量类别（tc0 到 tc7）。当数据包进入交换机时，它会收到一个 QoS 配置文件分配，该分配决定了流量类别，从而选择适当的出口队列进行传输。

硬件队列具有由 [传输管理器](#transmission-manager) 