# RouterOS 中的数据包流

> 本页解释了数据包如何流经 MikroTik RouterOS，详细说明了桥接、路由、MPLS 决策与防火墙链之间的交互。内容包括从入口到出口点的数据包处理阶段示意图，以及路由表和防火墙链等关键组件的描述。

# RouterOS 中的数据包流

更高级的防火墙设置，或复杂的任务，例如流量优先级、路由策略，当需要利用多个 RouterOS 功能时，就需要了解：这些功能如何协同工作？何时发生什么以及为什么？

RouterOS 数据包流图和流示例将尝试回答这些问题。

用一张图来表示数据包的处理过程会非常复杂；因此，数据包流图分为三个部分：

- 总体图。
- 详细的桥接、路由和 MPLS 流图。
- 一张显示在 prerouting、input、forward、output 和 postrouting 中包含哪些功能及其顺序的图。

### 总体数据包流图

让我们看一下总体图。乍一看很复杂，但通过示例逐步分析后会变得清晰得多。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-01.svg)

图中心有 4 个框：桥接、路由、MPLS 决策和本地路由器进程。例如，如果数据包需要通过路由器进行路由，数据包将按下图所示流动。在不深入每个功能的情况下，数据包进入入接口，路由器确定其为 IP 流量并需要路由，数据包经过所有路由进程后从出接口退出。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-02.webp)让我们看另一个示例，说明当数据包的目的地是路由器本身时会发生什么。例如，入接口接收到一个 ICMP（ping）数据包，其目的地是路由器本身，因此该数据包将进入 *local-in* 处理。数据包处理完成后，路由器内部生成一个 ICMP（ping）应答（*local-out* 处理），并通过出接口发送出去。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-03.webp)在进一步举例之前，先简单解释每个框：

- **物理入接口** - 路由器接收数据包的起始点。
- **逻辑入接口** - 解封装数据包（来自隧道、IPsec 等）的起始点。
- **本地入** - 目的地为路由器本身的数据包的最后一个点。
- **接口 HTB（层级令牌桶）** - 接口队列。
- **物理出接口** - 数据包实际发送前的最后一个点。
- **逻辑出接口** - 数据包封装（到隧道、IPsec 等）前的最后一个点。
- **本地出** - 路由器生成数据包的起始点。

现在是时候更深入地了解桥接、MPLS 和路由流内部发生了什么。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-04.webp)

在进一步举例之前，先简单解释每个框：

- **路由决策** - 遍历路由表中的路由，以找到与数据包目的 IP 地址匹配的路由。找到匹配项后 - 数据包将被进一步处理，若无匹配 - 数据包将被丢弃。
- **MPLS 决策** - 根据 MPLS 转发表决定如何处理数据包。
- **桥接决策** - 桥接遍历 MAC 地址表，以找到与数据包目的 MAC 地址匹配的条目。找到匹配项后 - 数据包将被进一步处理，若无匹配 - 将创建数据包的多个副本并进行泛洪（通过所有桥接端口发送）。单个数据包副本也会到达桥接输入链，因为桥接接口本身也是众多目的地之一。当使用 `vlan-filtering=yes` 时，由于 `/interface/bridge/vlan` 表而不允许的数据包将在此阶段被丢弃。
- **use-ip-firewall** - 桥接设置中是否启用了 '*use-ip-firewall*' 选项。
- **ipsec-policy** - 数据包是否匹配任何已配置的 IPsec 策略。

#### 链

RouterOS 由几个默认链组成。这些链允许您在各种点过滤数据包：

- **PREROUTING** 链：此链中的规则适用于刚到达网络接口的数据包。此链存在于 *nat*、*mangle* 和 *raw* 表中。
- **INPUT** 链：此链中的规则适用于数据包被交给本地进程之前。此链存在于 *mangle* 和 *filter* 表中。
- **OUTPUT** 链：此链中的规则适用于数据包由进程生成之后。此链存在于 *raw*、*mangle*、nat 和 *filter* 表中。
- **FORWARD** 链：此链中的规则适用于任何通过当前主机路由的数据包。此链仅存在于 *mangle* 和 *filter* 表中。
- **POSTROUTING** 链：此链中的规则适用于数据包即将离开网络接口时。此链存在于 *nat* 和 *mangle* 表中。

prerouting、input、forward、output 和 postrouting 块中的每一个都包含更多功能，这些功能在数据包流图的第三部分中说明：

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-05.webp)

在进一步举例之前，先简单解释每个框：

- **Hotspot-in** - 允许捕获否则会被连接跟踪丢弃的流量 - 这样我们的 Hotspot 功能即使在网络设置不完整的情况下也能提供连接。
- **RAW Prerouting** - RAW 表 prerouting 链。
- **连接跟踪** - 数据包由连接跟踪处理。
- **Mangle Prerouting** - Mangle prerouting 链。
- **Mangle Input** - Mangle input 链。
- **Filter Input** - 防火墙 filter input 链。
- **HTB Global** - 队列树。
- **简单队列** - 可用于限制特定目标流量的功能。
- **TTL** - 指示路由数据包的生存时间（TTL）减 1 的确切位置。如果 TTL 变为 0，数据包将被丢弃。
- **Mangle Forward** - Mangle forward 链。
- **Filter Forward** - Filter forward 链。
- **记账** - 认证、授权和记账功能处理。
- **RAW Output** - RAW 表 output 链。
- **Mangle Output** - Mangle output 链。
- **Filter Output** - 防火墙 filter output 链。
- **路由调整** - 这是一种变通方法，允许在 mangle 链 output 中设置策略路由（routing-mark）。
- **Mangle Postrouting** - Mangle postrouting 链。
- **Src Nat** - 网络地址转换 srcnat 链。
- **Dst Nat** - 网络地址转换 dstnat 链。
- **Hotspot-out** - 撤销 hotspot-in 对返回给客户端的数据包所做的所有操作。

### 路由数据包的流

#### 转发

现在，让我们看第一个示例，其中数据包通过路由器进行路由，并更深入地了解数据包经过哪些功能：

我们已经知道数据包进入入接口，路由器确定其为 IP 数据包并需要路由，这里开始复杂的过程：

1. 数据包进入 prerouting 处理：
   1. 检查是否存在 hotspot，并修改数据包以供 hotspot 使用。
   2. 通过 RAW prerouting 链处理数据包。
   3. 将数据包发送到连接跟踪。
   4. 通过 Mangle prerouting 链处理数据包。
   5. 通过 NAT 的 dst-nat 链处理数据包。
2. 通过路由表运行数据包以做出路由决策。
3. 数据包进入 forward 过程：
   1. 检查 TTL 值。
   2. 通过 Mangle forward 链处理数据包。
   3. 通过 Filter forward 链处理数据包。
   4. 将数据包发送到记账进程。
4. 数据包进入 postrouting 过程：
   1. 通过 Mangle postrouting 链处理数据包。
   2. 通过 NAT 的 src-nat 链处理数据包。
   3. 如果存在 hotspot，则撤销在 hotspot-in 中进行的任何修改。
   4. 通过队列树（HTB Global）处理数据包。
   5. 通过简单队列处理数据包。
5. 检查是否存在 IPsec，然后通过 IPsec 策略处理。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-06.webp)

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-07.webp)

#### 输入

我们已经知道数据包进入入接口，路由器确定其为 IP 数据包并需要路由，这里开始复杂的过程：

1. 当数据包的目的地是路由器本身（路由输入）时，会发生非常相似的过程：数据包进入 prerouting 处理：
   1. - 检查是否存在 hotspot，并修改数据包以供 hotspot 使用。
   2. - 通过 RAW prerouting 链处理数据包。
   3. - 将数据包发送到连接跟踪。
   4. - 通过 Mangle prerouting 链处理数据包。
   5. - 通过 NAT 的 dst-nat 链处理数据包。
2. 通过路由表运行数据包以做出路由决策。
3. 数据包进入 input 过程：
   1. - 通过 Mangle input 链处理数据包。
   2. - 通过 Filter input 链处理数据包。
   3. - 通过队列树（HTB Global）处理数据包。
   4. - 通过简单队列处理数据包。
4. 检查是否存在 IPsec，然后通过 IPsec 策略处理。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-08.webp)

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-09.webp)

#### 输出

或者当数据包源自路由器本身（路由输出）时：

1. 数据包源自路由器本身。
   1. 数据包通过路由表以做出路由决策。
2. 数据包进入 output 过程。
   1. 通过桥接决策处理数据包。
   2. 将数据包发送到连接跟踪。
   3. 通过 Mangle output 链处理数据包。
   4. 通过 Filter output 链处理数据包。
   5. 将数据包发送到路由调整（策略路由）。
3. 数据包进入 postrouting 过程。
   1. - 通过 Mangle postrouting 链处理数据包。
   2. - 通过 NAT 的 src-nat 链处理数据包。
   3. - 如果存在 hotspot，则撤销在 hotspot-in 中进行的任何修改。
   4. - 通过队列树（HTB Global）处理数据包。
   5. - 通过简单队列处理数据包。
4. 检查是否存在 IPsec，然后通过 IPsec 策略处理。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-10.webp)![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-11.webp)

### 桥接数据包的流

下面讨论 RouterOS 中的一般桥接过程。大多数数据包将始终遵循相同的处理路径，但在某些配置中（例如启用了 VLAN 过滤、horizon、STP、DHCP 或 IGMP snooping），某些数据包可能会被区别对待。请访问桥接手册以获取更具体的信息。

#### ![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-12.webp)

#### 桥接转发

桥接转发是当数据包从一个桥接端口转发到另一个桥接端口时发生的过程，本质上是连接同一网络上的多个设备。在入接口上接收到数据包后，设备确定入接口是桥接端口，因此数据包通过桥接过程传递：

1. 数据包通过桥接 NAT dst-nat 链，在此可以更改 MAC 目的地址和优先级，此外，数据包可以被简单地接受、丢弃或标记。
2. 检查桥接设置中是否启用了 use-ip-firewall 选项。
3. 通过桥接主机表运行数据包以做出转发决策。最终被泛洪的数据包（例如广播、组播、未知单播流量）会按桥接端口进行复制，然后在桥接 forward 链中进一步处理。当使用 `vlan-filtering=yes` 时，由于 `/interface/bridge/vlan` 表而不允许的数据包将在此阶段被丢弃。
4. 数据包通过桥接 filter forward 链，在此可以更改优先级，或者数据包可以被简单地接受、丢弃或标记。
5. 检查桥接设置中是否启用了 use-ip-firewall 选项。
6. 数据包通过桥接 NAT src-nat 链，在此可以更改 MAC 源地址和优先级，此外，数据包可以被简单地接受、丢弃或标记。
7. 检查桥接设置中是否启用了 use-ip-firewall 选项。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-13.webp)

:::info
**对于 RouterOS v6：**  
当桥接 `vlan-filtering` 启用时，接收到的未标记数据包可能会在“DST-NAT”块之前被封装到 VLAN 头中，这意味着这些数据包可以使用 `mac-protocol=vlan` 和 `vlan-encap` 设置进行过滤。如果出接口的 `frame-types` 设置为 `admit-all` 或 `admit-only-untagged-and-priority-tagged`，则可能发生封装。

带标记的数据包可能会在“BRIDGING DECISION”块上被解封装，这意味着这些数据包将不再匹配 `mac-protocol=vlan` 和 `vlan-encap` 设置。如果数据包的 VLAN ID 与出端口的未标记 VLAN 成员资格匹配，则可能发生解封装。  
  
**对于 RouterOS v7 及更新版本：**

当桥接 `vlan-filtering` 启用时，接收到的未标记数据包可能会在“BRIDGING-DECISION”块上被封装到 VLAN 头中，这意味着这些数据包可以使用 `mac-protocol=vlan` 和 `vlan-encap` 设置进行过滤。如果出接口的 `frame-types` 设置为 `admit-all` 或 `admit-only-untagged-and-priority-tagged`，则可能发生封装。

带标记的数据包可能会在“BRIDGING DECISION”块上被解封装，这意味着这些数据包将不再匹配 `mac-protocol=vlan` 和 `vlan-encap` 设置。如果数据包的 VLAN ID 与出端口的未标记 VLAN 成员资格匹配，则可能发生解封装。
:::

#### 桥接输入

桥接输入是当数据包的目的地是桥接接口时发生的过程。最常见的情况是当您需要访问桥接接口上运行的某些服务（例如 DHCP 服务器）或需要将流量路由到其他网络时。最初的步骤与桥接转发过程类似 - 在入接口上接收到数据包后，设备确定入接口是桥接端口，因此它通过桥接过程传递：

1. 数据包通过桥接 NAT dst-nat 链，在此可以更改 MAC 目的地址和优先级，此外，数据包可以被简单地接受、丢弃或标记。
2. 检查桥接设置中是否启用了 use-ip-firewall 选项。
3. 通过桥接主机表运行数据包以做出转发决策。目的 MAC 地址与桥接 MAC 地址匹配的数据包将被传递到桥接 input 链。最终被泛洪的数据包（例如广播、组播、未知单播流量）也会到达桥接 input 链，因为桥接接口本身也是众多目的地之一。
4. 数据包通过桥接 filter input 链，在此可以更改优先级，或者数据包可以被简单地接受、丢弃或标记。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-14.webp)

#### 桥接输出

桥接输出是当数据包应通过一个或多个桥接端口离开设备时发生的过程。最常见的情况是当桥接接口本身尝试连接到连接到某个桥接端口的设备时（例如，当桥接接口上运行的 DHCP 服务器响应 DHCP 客户端时）。在数据包由其他更高级别的 RouterOS 进程处理后，设备最终确定输出接口是桥接，数据包通过桥接过程传递：

1. 通过桥接主机表运行数据包以做出转发决策。最终被泛洪的数据包（例如广播、组播、未知单播流量）会按桥接端口进行复制，然后在桥接 output 链中进一步处理。
2. 数据包通过桥接 filter output 链，在此可以更改优先级，或者数据包可以被简单地接受、丢弃或标记。
3. 数据包通过桥接 NAT src-nat 链，在此可以更改 MAC 源地址和优先级，此外，数据包可以被简单地接受、丢弃或标记。
4. 检查桥接设置中是否启用了 use-ip-firewall 选项。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-15.webp)

#### 启用防火墙的转发

在某些网络配置中，您可能需要对桥接流量启用路由链上的额外处理，例如，使用简单队列或 IP 防火墙。这可以在桥接设置下启用 use-ip-firewall 时完成。请注意，额外的处理将消耗更多的 CPU 资源来处理这些数据包。所有步骤已在前面讨论过；以下是回顾：

1. 数据包通过桥接 NAT dst-nat 链。
2. 启用 use-ip-firewall 选项后，数据包将在 prerouting 链中进一步处理。
3. 数据包进入 prerouting 处理。
4. 通过桥接主机表运行数据包以做出转发决策。
5. 数据包通过桥接 filter forward 链。
6. 启用 use-ip-firewall 选项后，数据包将在路由 forward 链中进一步处理。
7. 数据包进入路由 forward 处理。
8. 数据包通过桥接 NAT src-nat 链。
9. 启用 use-ip-firewall 选项后，数据包将在 postrouting 链中进一步处理。
10. 数据包进入 postrouting 处理。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-16.webp)![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-17.webp)

### 硬件卸载数据包的流

在上一主题中，我们仅讨论了需要主 CPU 处理以通过正确的桥接端口转发数据包的软件桥接。大多数 MikroTik 设备都配备了专用的交换硬件，即所谓的交换芯片或交换 ASIC。这使我们能够将一些桥接功能（如桥接端口之间的数据包转发或数据包过滤）卸载到此专用硬件芯片上，而无需消耗任何 CPU 资源。在 RouterOS 中，我们将此功能命名为桥接硬件（HW）卸载。不同的 MikroTik 设备可能具有不同的交换芯片，每个芯片具有不同的可用功能集，因此请务必访问此文章以获取更多详细信息 - [桥接硬件卸载](../bridging-and-switching/index.md#bridge-hardware-offloading)。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-18.webp)

:::warning
当出接口为硬件卸载且桥接 Fast Path 未激活时，接口 HTB 将无法正常工作。
:::

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-19.webp)

- **交换决策** - 很大程度上取决于交换机型号。此块控制所有与交换相关的任务，如主机学习、数据包转发、过滤、VLAN 标记/去标记等。某些交换机配置可以改变数据包流。
- **switch-cpu 端口** - 一种特殊用途的交换端口，用于主 CPU 和其他交换端口之间的通信。请注意，switch-cpu 端口在 RouterOS 中除了交换机菜单外不会出现在任何地方。任何与软件相关的配置（例如 interface-list）都不能应用于此端口。到达 CPU 的数据包会自动与物理入接口关联。

然而，硬件卸载并不限制设备仅使用硬件受限功能；相反，可以同时利用硬件和软件处理。这确实需要深入了解数据包如何通过交换芯片以及它们何时被传递给主 CPU。

:::info
在 `/interface/ethernet/switch` 菜单及其子菜单中找到的交换功能，如 ACL 规则、镜像、入口/出口速率限制器、QoS 和 L3HW（除 VLAN 间路由外）可能不依赖于桥接硬件卸载。因此，它们**可能**应用于未在硬件卸载桥接中配置的接口。
:::

#### 交换转发

我们将进一步讨论当桥接硬件卸载启用且数据包在单个交换芯片上的两个交换端口之间转发时的数据包流。这是最常见也是最简单的示例：

1. 交换机检查入接口是否为硬件卸载接口。
2. 交换机通过交换主机表运行数据包以做出转发决策。如果交换机找到目的 MAC 地址的匹配项，则数据包通过物理接口发送出去。最终被泛洪的数据包（例如广播、组播、未知单播流量）会被复制并发送到每个硬件卸载的交换端口。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-20.webp)

#### 交换到 CPU 输入

此过程发生在物理接口上接收到数据包且其目的地为 switch-cpu 端口以进行进一步软件处理时。有两条路径可以到达 switch-cpu。一种是根本不使用硬件卸载和交换（例如，用于路由的独立接口或故意禁用 HW 卸载的桥接接口），因此数据包只是简单地传递以进行软件处理。另一种路径是当入接口上硬件卸载处于活动状态时。这将导致数据包通过交换决策，并且交换机可能将数据包转发到 switch-cpu 端口的原因有多种：

- 数据包的目的 MAC 地址与本地 MAC 地址匹配，例如当数据包的目的地是本地桥接接口时。
- 数据包可能会泛洪到所有交换端口，包括 switch-cpu 端口，例如当接收到广播、组播或未知单播流量时。
- 交换机可能已了解到某些主机只能通过 CPU 访问（switch-cpu 端口学习将在下一节讨论），例如当桥接包含 HW 和非 HW 卸载接口时，例如无线、EoIP，甚至以太网接口。
- 数据包被有意复制到 switch-cpu，例如用于数据包检查。
- 数据包由交换机配置触发，应在软件中处理，例如 DHCP 或 IGMP snooping。

查看入接口为硬件卸载时的数据包遍历：

1. 交换机检查入接口是否为硬件卸载接口。
2. 通过交换主机表运行数据包以做出转发决策。如果上述任何一点成立，则数据包被转发到 switch-cpu 端口。
3. 数据包通过 switch-cpu 端口退出，并将由 RouterOS 数据包流进一步处理。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-21.webp)

:::warning
任何由交换芯片泛洪的接收数据包都不会被软件桥接再次泛洪到同一 HW 卸载交换组。这防止了重复数据包的形成。
:::

#### CPU 输出到交换

此过程发生在数据包退出 RouterOS 软件处理并在 switch-cpu 端口上接收时。同样，数据包可以采取两条路径。一种是根本不使用硬件卸载和交换（例如，用于路由的独立接口或故意禁用 HW 卸载的桥接接口），因此数据包只是简单地通过物理出接口发送出去。另一种路径是当出接口上硬件卸载处于活动状态时。这将导致数据包通过交换决策。与任何其他交换端口一样，交换机将从 switch-cpu 端口接收的数据包中学习源 MAC 地址。当桥接包含 HW 和非 HW 卸载接口时，这非常有用，因此交换机可以学习哪些帧应转发到 CPU。查看出接口为硬件卸载时的数据包遍历：

1. 退出 RouterOS 软件处理的数据包在 switch-cpu 端口上接收。
2. 交换机检查出接口是否为硬件卸载接口。
3. 交换机通过交换主机表运行数据包以做出转发决策。如果交换机找到目的 MAC 地址的匹配项，则数据包通过物理接口发送出去。最终被泛洪的数据包（例如广播、组播、未知单播流量）会被复制并发送到每个硬件卸载的交换端口。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-22.webp)

:::warning
通过 HW 卸载接口发送泛洪数据包的软件桥接将仅为每个 HW 卸载交换组发送单个数据包副本，而不是为每个 HW 卸载接口发送。实际的泛洪将由交换芯片完成；这防止了重复数据包的形成。
:::

### MPLS 数据包的流

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-23.webp)

#### 弹出标签

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-24.webp)

#### 交换标签

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-25.webp)

#### 压入标签

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-26.webp)

### MPLS IP VPN

在 VPNv4 设置中，到达 PE 路由器且需要转发到 CE 路由器的数据包不是典型的“转发”。

如果传入标签和目的地绑定到 VRF，则在 MPLS 标签被弹出后：

- 目的地址是路由器本地的，则数据包被移动到 LOCAL\_IN。
- 目的地址在 CE 网络中，则数据包被移动到 LOCAL\_OUT。

:::danger
从 MPLS 云转发到 CE 网络的数据包不会出现在 forward 中。
:::

例如，从 src:111.15.0.1 到 dst:111.13.0.1 的流量

```text
[admin@CCR2004_2XS] /mpls/forwarding-table> print 
Flags: L - LDP, P - VPN
Columns: LABEL, VRF, PREFIX, NEXTHOPS
#   LABEL  VRF      PREFIX         NEXTHOPS                                                                                                           
0 P    17  myVrf    111.13.0.0/24  
4 L    20  main     203.0.113.2    { label=impl-null; nh=111.11.0.1; interface=sfp-sfpplus1 }
[admin@CCR2004_2XS] /mpls/forwarding-table>                                                           
...

[admin@CCR2004_2XS] /ip/route> print detail 
Flags: D - dynamic; X - disabled, I - inactive, A - active; c - connect, s - static, r - rip, b - bgp, o - ospf, i - is-is, d - dhcp, v - vpn, m - modem, y - bgp-mpls-vpn; 
H - hw-offloaded; + - ecmp 

   DAc   dst-address=111.11.0.0/24 routing-table=main gateway=sfp-sfpplus1 immediate-gw=sfp-sfpplus1 distance=0 scope=10 suppress-hw-offload=no 
         local-address=111.11.0.2%sfp-sfpplus1 
   DAc   dst-address=203.0.113.1/32 routing-table=main gateway=lo immediate-gw=lo distance=0 scope=10 suppress-hw-offload=no local-address=203.0.113.1%lo 
   DAo   dst-address=203.0.113.2/32 routing-table=main gateway=111.11.0.1%sfp-sfpplus1 immediate-gw=111.11.0.1%sfp-sfpplus1 distance=110 scope=20 target-scope=10 
         suppress-hw-offload=no 
   DAc   dst-address=111.13.0.0/24 routing-table=myVrf gateway=sfp-sfpplus2@myVrf immediate-gw=sfp-sfpplus2 distance=0 scope=10 suppress-hw-offload=no 
         local-address=111.13.0.2%sfp-sfpplus2@myVrf 
   DAy   dst-address=111.15.0.0/24 routing-table=myVrf gateway=203.0.113.2 immediate-gw=111.11.0.1%sfp-sfpplus1 distance=200 scope=40 target-scope=30 suppress-hw-offload=no [admin@CCR2004_2XS] /ip/route>              
```

该数据包将在 output 和 postrouting 链中可见，因为它现在是一个本地发起的数据包，源 MAC 地址等于 vrfInterface：

```text
08:10:55 firewall,info output: in:(unknown 0) out:sfp-sfpplus2, connection-state:established src-mac f2:b5:e9:17:18:3b, proto ICMP (type 8, code 0), 111.15.0.1->111.13.0.1, len 56
08:10:55 firewall,info postrouting: in:myVrf out:sfp-sfpplus2, connection-state:established src-mac f2:b5:e9:17:18:3b, proto ICMP (type 8, code 0), 111.15.0.1->111.13.0.1, len 56
```

另一方面，在 CE→PE 方向上路由的数据包将在发送到 MPLS 之前像任何其他路由的 IP 流量一样出现在“forward”中：

```text
 08:10:55 firewall,info prerouting: in:sfp-sfpplus2 out:(unknown 0), connection-state:established src-mac dc:2c:6e:46:f8:93, proto ICMP (type 0, code 0), 111.13.0.1->111.15.0.1, len 56
 08:10:55 firewall,info forward: in:sfp-sfpplus2 out:sfp-sfpplus1, connection-state:established src-mac dc:2c:6e:46:f8:93, proto ICMP (type 0, code 0), 111.13.0.1->111.15.0.1, len 56
 08:10:55 firewall,info postrouting: in:sfp-sfpplus2 out:sfp-sfpplus1, connection-state:established src-mac dc:2c:6e:46:f8:93, proto ICMP (type 0, code 0), 111.13.0.1->111.15.0.1, len 56
 
```

但可能有一个例外。如果回复数据包的目的 IP 是路由器本地的，并且连接跟踪正在执行 NAT 转换，则连接跟踪将“强制”数据包通过防火墙 prerouting/forward/postrouting 链移动。

### 逻辑接口

到目前为止，我们看到的示例中入接口或出接口是实际的物理接口（以太网、无线），但如果路由器接收到隧道封装的数据包，数据包将如何流动？

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-27.webp)

让我们假设有一个 IPIP 数据包进入路由器。由于它是一个常规的 IPv4 数据包，它将通过所有与路由相关的功能进行处理（直到图中的“J”）。然后路由器将检查数据包是否需要解封装。在这种情况下，它是一个 IPIP 数据包，因此“是”，将数据包发送到解封装。之后，数据包将再次循环通过所有功能，但这次是作为解封装后的 IPv4 数据包。

这非常重要，因为数据包实际上会两次通过防火墙，因此如果有严格的防火墙，则应该有针对 IPIP 封装数据包以及解封装后的 IP 数据包的“接受”规则。

:::info
使用启用了 `vlan-filtering` 的桥接进行的数据包封装和解封装与逻辑接口无关。更多详细信息请参阅桥接部分。
:::

### IPSec 策略

让我们看看另一种隧道类型 - IPSec。这种类型的 VPN 没有逻辑接口，但以类似的方式处理。

数据包不是通过逻辑接口，而是通过 IPSec 策略处理。在路由决策（2）和 input 防火墙处理（3）之后，路由器尝试将源和目的地与 IPsec 策略匹配。当策略匹配数据包时，将其发送到解密（5）。解密后，数据包再次进入 PREROUTING 处理（6）并开始另一个处理循环，但现在是使用解封装后的数据包。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-28.webp)

封装也适用相同的过程，但顺序相反。第一个 IP 数据包通过功能处理，然后与 IPsec 策略匹配（5），封装（6），然后在第二个循环中发送到处理（7-10）。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-29.webp)

## Fast Path

从我们目前了解到的信息来看，很明显这种数据包处理会消耗大量 CPU 资源。为了加快速度，在第一个 RouterOS v6 中引入了 FastPath。它所做的是跳过 Linux 内核中的处理，基本上是用一些 RouterOS 功能换取性能。要使 FastPath 工作，需要接口驱动程序支持和特定的配置条件。

### Fast Path 的工作原理

FastPath 是一个接口驱动程序扩展，允许驱动程序直接与特定的 RouterOS 功能通信，并跳过所有其他功能。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-30.svg)

只有当至少源接口支持 fast path 时，数据包才能由 fast path 处理器转发。对于完整的快速转发，还需要目标接口支持。

目前，RouterOS 有以下 FastPath 处理器：

- IP 流量处理
- FastTrack
- 流量生成器
- MPLS
- 桥接

如果满足以下条件，则使用 FastPath 处理器：

- 未配置防火墙规则。
- 未配置 *parent=global* 的简单队列或队列树。
- 未配置 mesh 或 metarouter 接口。
- 未运行嗅探器或 torch。
- 连接跟踪未激活。
- IP 记账已禁用。
- 未配置 VRF（`/ip/vrf` 为空）。
- 未使用 hotspot（`/ip/hotspot` 没有接口）。
- 未配置 IPSec 策略。
- `/tool/mac-scan` 未在使用中。
- `/tool/ip-scan` 未在使用中。

:::warning
如果使用 FastTrack，无论是否满足上述条件，数据包都将走 FastPath 路径。
:::

如果接口支持此功能，流量生成器会自动使用 FastPath。

目前，MPLS fast-path 适用于 MPLS 交换流量（以 MPLS 形式进入路由器并且必须以 MPLS 形式离开路由器的帧）以及执行 VPLS 封装/解封装的 VPLS 端点。其他 MPLS 入口和出口将像以前一样运行。

如果满足以下条件，则使用桥接处理器：

- 没有桥接 Calea、filter、NAT 规则。
- *use-ip-firewall* 已禁用。
- 没有 mesh、MetaRouter 接口配置。
- 嗅探器、torch 和流量生成器未运行。
- 桥接 vlan-filtering 已禁用（自 RouterOS 7.2 版本起此条件已移除）。
- 桥接 dhcp-snooping 已禁用。

:::warning
vlan-filtering 桥接上的 FastPath 不支持优先级标记的数据包（带有 VLAN 头但 VLAN ID = 0 的数据包）。这些数据包将通过慢路径重定向。
:::

支持 FastPath 的接口：

| RouterBoard | 接口 |
| :-- | :-- |
| **RB6xx 系列** | ether1,2 |
| **RB800** | ether1,2 |
| **RB1100 系列** | ether1-11 |
| **所有设备** | 以太网接口 |
|  | 无线接口 |
|  | 桥接接口 |
|  | VLAN、VRRP 接口 |
|  | 绑定接口（仅 RX） |
|  | PPPoE、L2TP 接口 |
|  | EoIP、GRE、IPIP、VXLAN 接口。 |
|  | VPLS（从 v7.17 开始） |

EoIP、Gre、IPIP、VXLAN 和 L2TP 接口有一个每接口设置 *allow-fast-path*。在这些接口上允许 fast path 的副作用是绕过防火墙、连接跟踪、简单队列、parent=global 的队列树、IP 记账、IPsec、hotspot universal client、vrf 分配（对于通过 fast-path 的封装数据包）。此外，FastPath 中无法接收数据包分片。

:::info
是否正在使用 FastPath 可以通过 `/interface/print stats-detail` 验证
:::

唯一保证 FastPath 的接口队列是 only-hardware-queue。如果您需要硬件队列以外的接口队列，则数据包将不会完全走 FastPath，但对性能影响不大，因为“接口队列”是数据包流中的最后一步。

数据包可以通过从 FastPath 切换到 SlowPath 来走 Half-FastPath，但不能反过来。因此，例如，如果接收接口支持 FastPath，但出接口不支持，则路由器将尽可能通过 FastPath 处理器处理数据包，然后继续使用 SlowPath。如果接收接口不支持 FastPath 但出接口支持，则数据包将全程通过 SlowPath 处理。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-31.webp)

## FastTrack

Fasttrack 可以理解为 Fast Path + 连接跟踪。它允许将连接标记为“fast-tracked”，标记属于 fast-tracked 连接的数据包将通过 fast-path 方式发送。此类连接的连接表条目现在将具有 fast-tracked 标志。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/packet-flow-in-routeros-32.webp)

:::warning
FastTrack 数据包绕过防火墙、连接跟踪、简单队列、parent=global 的队列树、ip traffic-flow、IP 记账、IPSec、hotspot universal client、VRF 分配，因此由管理员确保 FastTrack 不与其他配置冲突！
:::

为了将连接标记为 fast-tracked，为防火墙 filter 和 mangle 实现了一个新动作 "*fasttrack-connection"*。目前，只有 TCP 和 UDP 连接可以被 fast-tracked，并且为了维护连接跟踪条目，一些随机数据包仍