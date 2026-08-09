# CAKE

> CAKE（Common Applications Kept Enhanced）是 RouterOS 中一种先进的队列管理算法，通过带宽整形、流隔离和基于 RTT 的拥塞控制来优化网络流量处理。它支持 Diffserv 优先级处理、ACK 过滤、NAT 处理以及针对不同链路技术的各种开销补偿方案。

CAKE（Common Applications Kept Enhanced）是一种支持整形的队列规则，它结合了 COBALT 主动队列管理、赤字模式整形器、DRR++ 流隔离、简化 DiffServ 处理以及链路层开销补偿。

CAKE 旨在通过实用的默认设置和少量调优来维持公平性并最小化缓冲膨胀（bufferbloat）。

## 何时使用 CAKE

在共享瓶颈链路上使用 CAKE，当批量传输增加延迟或单个主机可能占用可用容量时。典型示例包括多个客户端共享的互联网连接、慢速上行链路或非对称连接。

CAKE 可以：

- 在链路繁忙时保持低延迟。
- 在主机之间及其各自连接之间共享容量。
- 针对链路层开销进行整形。
- 应用简单的 DiffServ 策略。
- 在高度非对称链路上过滤冗余的 TCP 确认包。

CAKE 只能控制通过其队列的流量。它无法纠正 Wi-Fi 干扰、路由器 CPU 不足或网络中其他位置的队列，除非其整形器配置在该瓶颈速率之下。

当您需要每流公平性和主动队列管理且 CPU 占用较低时，请使用 FQ-CoDel。当您还需要每主机公平性、带链路层补偿的集成整形器、DiffServ 处理或 ACK 过滤时，请使用 CAKE。

## 基本配置

CAKE 是一种队列类型，而不是完整的流量匹配规则。在 `/queue/type` 下创建 CAKE 条目定义了一个可重用的队列配置文件，但其本身不处理任何流量。将该配置文件分配给 Simple Queue、Queue Tree 或 Interface Queue。有关属性和可接受值的完整列表，请参阅生成的 [`/queue/type` CLI 参考](../../../cli-reference/queue/type)。

以下示例将相同的 CAKE 配置文件应用于 Simple Queue 的两个方向。HTB 提供上行和下行限制，因此 CAKE 的内部整形器保持无限制：

```ros
/queue/type
add name=cake-default kind=cake cake-bandwidth=0 cake-nat=yes

/queue/simple
add name=internet-cake target=192.168.88.0/24 max-limit=20M/100M queue=cake-default/cake-default
```

在 `max-limit=20M/100M` 和 `queue=cake-default/cake-default` 中，第一个值是上行，第二个值是下行。请将目标地址和速率替换为适合网络环境的值。FastTracked 流量会绕过此 Simple Queue，因此请为队列必须处理的流量禁用 FastTrack。

:::note
仅在 `kind=cake` 的队列类型上设置 `cake-bandwidth`。它控制 CAKE qdisc 内置的整形器。

Simple Queue 和 Queue Tree 条目使用 HTB。它们的 `limit-at`（CIR）和 `max-limit`（MIR）参数控制 HTB 层的速率。当您将 CAKE 队列类型分配给这些条目之一时，CAKE 作为 HTB 下的叶子 qdisc 运行。

当 HTB 应控制流量速率时，请保留 `cake-bandwidth=0`。此值使 CAKE 的整形器无限制，但 CAKE 继续提供主动队列管理、流隔离和 DiffServ 处理。当 CAKE 也应整形流量时，请设置 `cake-bandwidth`。如果您同时配置了 `cake-bandwidth` 和 HTB 速率限制，流量将通过两个整形器。
:::

## 推荐的起始配置

| 使用场景 | 推荐的起始配置 |
| :-- | :-- |
| Simple Queue 或 Queue Tree 提供速率限制 | 保留 `cake-bandwidth=0` 并设置 HTB `max-limit`。CAKE 提供主动队列管理和公平性，而无需添加第二个整形器。 |
| CAKE 提供速率限制 | 将 `cake-bandwidth` 设置为低于实际瓶颈速率，并配置正确的链路层开销。除非两个整形层都是有意为之，否则避免第二个 HTB 速率限制。 |
| 路由器执行 NAT | 设置 `cake-nat=yes` 并保持默认的 `triple-isolate` 流模式。这允许一个 CAKE 实例在内部主机之间及其流之间平衡流量。 |
| 下载/上传比率大于约 10:1 | 仅在较慢方向的传输队列上设置 `cake-ack-filter=filter`。 |
| 入站 DSCP 标记不受信任 | 设置 `cake-diffserv=besteffort` 以忽略它们，或设置 `cake-wash=yes` 以在 CAKE 应用其优先级决策后清除它们。 |

### 方向和队列放置

CAKE 实例仅处理通过其附加队列的数据包。它不会自动处理反向流量。

- **Interface Queue：** 接口队列处理该接口传输的数据包。对于转发的客户端流量，面向 WAN 的传输接口上的 CAKE 处理上行流量，而面向 LAN 的传输接口上的 CAKE 处理下行流量。这是两个独立的 CAKE 实例。接口队列不处理该接口接收的数据包。
- **Simple Queue：** RouterOS 相对于配置的目标地址确定上行和下行。`queue` 属性按顺序选择上行和下行队列类型。将 CAKE 队列类型分配给两个位置以处理两个方向。
- **Queue Tree：** 每个 Queue Tree 是单向的。其父级和数据包选择决定哪些流量通过其 CAKE 叶子队列。

当上行和下行速率或选项不同时，请为每个方向配置单独的 CAKE 队列类型。如果 LAN 使用多个出接口，仅附加到其中一个接口的 Interface Queue 不会处理其他接口传输的流量。单个 CAKE 实例可以平衡通过它的许多主机和流。仅当您需要明确的每客户端速率限制或 HTB 保证时，才创建单独的每客户端队列。

`cake-autorate-ingress` 名称指的是 CAKE 的容量估计模式。它不会使 Interface Queue 处理接口接收的数据包，也不会创建反向队列。Linux 示例中将 WAN 入站重定向到 Intermediate Functional Block（IFB）会创建一个单独的传输排队点；它们不是 RouterOS Interface Queue 配置说明。

### 选择整形速率

整形器必须成为瓶颈才能控制队列延迟。从低于稳定测量吞吐量的值开始，而不是广告服务速率。入站整形通常需要更多的余量，因为上游发送方和 ISP 队列不在路由器的控制范围内。通过正确的开销补偿，出站整形可以更接近测量的链路速率运行。

在测量延迟的同时，在上传和下载负载同时进行的情况下验证速率。仅限吞吐量的速度测试无法显示交互式流量、语音或其他主机是否保持响应。当 CAKE 在主机和流之间共享容量时，单个流吞吐量降低可能是预期结果。

:::warning
整形的 CAKE 实例不会将其数据包处理分配到多个 CPU 核心。CPU 耗尽会降低吞吐量并增加延迟，即使其他核心空闲。请在目标设备上测试所需的整形速率。无限制的 CAKE 所需的处理量远少于整形的 CAKE。
:::

:::note
FastTracked 流量会绕过 Simple Queues 和 `parent=global` 的 Queue Trees。直接父级为接口的 Queue Trees 可以处理 FastTracked 流量。请参阅 [FastTrack](../../connection-tracking#fasttrack)。
:::

## 开销补偿

CAKE 必须知道每个数据包在瓶颈链路上占用多少时间。CAKE 可见的数据包大小可能不包括帧、封装或数据包间开销。如果没有补偿，配置的整形器可能比实际链路发送得稍快，并允许队列在其他地方堆积。

优先选择与瓶颈技术匹配的 `cake-overhead-scheme`。方案会设置相关的开销、最小数据包单元（MPU）以及 ATM 或 PTM 补偿。仅在封装已知且没有预设匹配时使用手动值。

| 方案 | 行为 |
| :-- | :-- |
| `raw` | 禁用开销补偿。当 CAKE 可见的数据包大小已经代表瓶颈使用的单元时使用。 |
| `convervative` | 故意高估未知开销。相当于 48 字节开销并带有 ATM 补偿。RouterOS 对此值使用拼写 `convervative`。 |
| `ethernet` | 计入以太网前导码、帧间间隙和帧校验序列。相当于 38 字节开销、84 字节 MPU，且无 ATM 或 PTM 补偿。 |
| `via-ethernet` | 当 CAKE 接收完整的以太网帧而不是原始 IP 数据包时，调整另一个方案。仅作为修饰符与适用的基础方案一起使用。 |
| `ether-vlan` | 为 IEEE 802.1Q VLAN 头添加 4 字节。与适用的基础方案结合使用。 |
| `docsis` | 匹配 DOCSIS 头端整形和计量使用的以太网帧大小。相当于 18 字节开销、64 字节 MPU，且无 ATM 或 PTM 补偿。 |
| ADSL 方案 | 选择 `ipoa-vcmux`、`ipoa-llcsnap`、`bridged-vcmux`、`bridged-llcsnap`、`pppoa-vcmux`、`pppoa-llc`、`pppoe-vcmux` 或 `pppoe-llcsnap` 以匹配封装。这些方案包含 ATM 信元补偿。 |
| `pppoe-ptm` 或 `bridged-ptm` | 选择匹配的 VDSL2 封装。这些方案包含 PTM 补偿。 |

对于手动配置，`cake-overhead` 接受 -64 到 256 字节的值。`cake-mpu` 接受 0 到 256 字节的值，且不能为负数。设置 `cake-atm=atm` 用于 ATM 信元帧，或 `cake-atm=ptm` 用于 PTM 编码。

## RTT 方案

CAKE 队列规则使用往返时间（RTT）来调整其主动队列管理参数。除非已知典型流量 RTT，否则保持默认的 `internet` 方案。较短的方案反应更快，但低于实际路径 RTT 的值会降低长生命周期流的吞吐量，尤其是在低速率链路上。该设置不需要与每个流完全匹配；实际 RTT 在大约一个数量级内通常都能正常工作。

对于大多数本地网络，使用 `metro` 而不是 `lan`。`lan` 的激进时间常数可能会过早发出拥塞信号，降低吞吐量，并为公平性逻辑留下过少的排队流量。仅将其保留用于受控的纯以太网网络；在整形互联网接入链路时不要使用它。

以下是您可以使用的 RTT 设置、它们的含义以及可能的使用场景：

1. `cake-rtt`：手动指定 RTT，例如 `cake-rtt=100ms`。
2. `cake-rtt-scheme=datacentre`：假设 RTT 为 100 微秒。仅用于极高性能的数据中心网络。
3. `cake-rtt-scheme=lan`：假设 RTT 为 1 毫秒。仅用于受控的纯以太网网络，不用于互联网接入链路。
4. `cake-rtt-scheme=metro`：假设 RTT 为 10 毫秒。用于大多数本地网络或单个城市内的流量。
5. `cake-rtt-scheme=regional`：假设 RTT 为 30 毫秒。用于区域或国家内的流量。
6. `cake-rtt-scheme=internet`：假设 RTT 为 100 毫秒。适用于典型的互联网流量。
7. `cake-rtt-scheme=oceanic`：假设 RTT 为 300 毫秒。用于延迟持续高于平均水平的互联网流量。
8. `cake-rtt-scheme=satellite`：假设 RTT 为 1000 毫秒。用于地球静止卫星路径。
9. `cake-rtt-scheme=interplanetary`：假设 RTT 为 3600 秒，几乎完全禁用主动队列管理（AQM）操作。不适用于普通网络配置。

对于卫星和其他高延迟链路，当预设与路径不匹配时，请设置测量的 RTT。预设是起点而非测量值。

## 流隔离

CAKE 通过源地址和目标地址、传输协议以及源端口和目标端口来识别流。它将流放入单独的队列并公平调度。当批量流使用同一链路时，稀疏、低速率流可以保持响应。

- `cake-flowmode=triple-isolate`：在源主机、目标主机和单个流之间应用公平性。这是默认设置，也是典型网关的推荐起点。
- `cake-flowmode=dual-srchost`：先在源主机之间应用公平性，然后在每个主机的流之间应用。当源地址标识需要平衡的订阅者或设备时使用。
- `cake-flowmode=dual-dsthost`：先在目标主机之间应用公平性，然后在每个主机的流之间应用。当目标地址标识需要平衡的订阅者或设备时使用。
- `cake-flowmode=srchost`：仅在源地址之间应用公平性。
- `cake-flowmode=dsthost`：仅在目标地址之间应用公平性。
- `cake-flowmode=hosts`：在源主机和目标主机对之间应用公平性。
- `cake-flowmode=flows`：仅在完整的五元组流之间应用公平性。
- `cake-flowmode=flowblind`：禁用流隔离，并将每个 tin 的所有流量放入一个队列。

当路由器执行 NAT 时，设置 `cake-nat=yes`，以便 CAKE 可以隔离内部地址和端口。除非拓扑需要特定的方向模式，否则保持 `triple-isolate`。常见的组合——上行使用 `dual-srchost`、下行使用 `dual-dsthost`——主要仅在 CAKE 无需 NAT 查找即可看到所需主机地址时有用。当另一台设备执行 NAT 或硬件卸载流量绕过 CAKE 时，NAT 查找无效。

## ACK 过滤器

ACK 过滤会在冗余的 TCP 确认包消耗窄带传输链路容量之前将其移除。从 `cake-ack-filter=filter` 开始；仅在测试表明额外过滤不会降低 TCP 性能后，才使用 `cake-ack-filter=aggressive`。设置 `cake-ack-filter=none` 以禁用它。

仅在高度非对称连接的较慢一侧的传输队列上启用 ACK 过滤。当下载/上传比率超过约 10:1 时，它变得相关。不要在接收队列上启用它：ACK 包通常不会在那里累积，而且过滤器会消耗额外的 CPU。

ACK 过滤无法检查加密流量（如 WireGuard 或 IPsec 隧道）内的 ACK 包。请在明文 TCP ACK 包可见的位置应用它。

## DiffServ

区分服务（DiffServ）根据数据包的区分服务代码点（DSCP）对其进行分类，并将其放入称为 tins 的 CAKE 流量类中。CAKE 在 tins 之间应用软优先级：每个 tin 都获得服务，并且可以借用未使用的容量。百分比阈值不是固定的带宽限制。例如，当其他 tins 空闲时，Best Effort 可以使用 100% 的链路容量。

- `cake-diffserv=diffserv3`（默认）：提供 Bulk（CS1 和 LE）、Best Effort（一般流量）和 Voice（CS7、CS6、EF、VA 和 TOS4）tins。它们的阈值分别为 6.25%、100% 和 25%。Voice 使用较短的 CoDel 间隔。
- `cake-diffserv=diffserv4`：提供 Bulk（CS1 和 LE）、Best Effort（一般流量）、Video（AF4x、AF3x、CS3、AF2x、CS2、TOS4 和 TOS1）以及 Voice（CS7、CS6、EF、VA、CS5 和 CS4）tins。它们的阈值分别为 6.25%、100%、50% 和 25%。
- `cake-diffserv=diffserv8`：为具有明确、详细 DSCP 策略的网络提供八个 tins。
- `cake-diffserv=besteffort`：禁用优先级排队，并将所有流量放入一个 tin。当 DSCP 标记不存在或不得影响调度时使用。
- `cake-diffserv=precedence`：使用传统的 IP 优先级解释。在新配置中避免此模式。

CAKE 本身不会创建可信的分类。仅当您信任接收到的 DSCP 标记或通过一致的本地策略设置它们时，才使用 DiffServ 模式。不正确的高优先级标记可能会给流量带来意外的服务。

## Wash

`cake-wash=yes` 选项在 CAKE 使用 DSCP 标记进行优先级决策后清除它们。它不会清除显式拥塞通知（ECN）位。

在 DiffServ 域边界启用 `cake-wash=yes`，当下一网络不得继承现有 DSCP 策略时。如果入站标记不受信任且不应影响调度，请使用 `cake-diffserv=besteffort`；添加 `cake-wash=yes` 也会在转发数据包之前清除这些标记。

## Autorate ingress

`cake-autorate-ingress` 选项根据入站数据包的到达时间估计容量，并调整 CAKE 的内部整形器。可选的 `cake-bandwidth` 值提供其初始估计。

估计器仅观察到达此 CAKE 实例的流量。它无法测量更下游的瓶颈，并且必须接收足够的流量才能增加其估计值。容量变化大或快的链路（如 LTE 和 5G）因此可能产生不稳定或意外低的速率。

:::warning
在生产使用前，请在真实链路上测试 `cake-autorate-ingress`。它是 CAKE 的内置估计器，不同于持续测量延迟并更新整形器的外部自适应速率实现。当可预测的延迟和吞吐量比跟随每次容量变化更重要时，请使用低于可靠链路容量的固定速率。
:::

当 HTB 旨在控制速率时，不要启用 `cake-autorate-ingress`。该选项更改 CAKE 的整形器，而不是 HTB `max-limit`。