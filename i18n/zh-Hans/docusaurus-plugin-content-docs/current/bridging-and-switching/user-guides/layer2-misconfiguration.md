# Layer2 配置错误

> 本页介绍 MikroTik RouterOS 中的 Layer2 配置错误，重点关注硬件卸载和端口隔离的桥接设置不当等问题。文中解释了吞吐量低、CPU 使用率高、硬件卸载标志不正确等症状，以及针对不支持端口隔离的设备的解决方案。

# Layer2 配置错误

---

有些配置在设计上就存在重大缺陷，应尽量避免。配置错误的 Layer2 有时会导致难以检测的网络错误、随机性能下降、网络某些网段无法访问、某些网络服务故障，甚至整个网络瘫痪。本页将介绍一些常见或不常见的会导致网络问题的配置。

## 单个交换芯片上的多个桥接

---

考虑以下场景：你有一台带有内置交换芯片的设备，需要将某些端口相互隔离。为此，你创建了多个桥接并在其上启用了硬件卸载。由于每个桥接位于不同的 Layer2 域中，Layer2 帧不会在这些桥接之间转发。因此，每个桥接中的端口与不同桥接上的其他端口相互隔离。

### 配置

```ros
/interface/bridge
add name=bridge1
add name=bridge2
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge2 interface=ether3
add bridge=bridge2 interface=ether4
```

### 问题

经过简单的性能测试后，你可能会注意到一个桥接能够以线速转发流量，而第二个、第三个等桥接则无法转发与第一个桥接相同数量的数据。另一个症状可能是需要路由的数据包存在巨大延迟。经过快速检查，你可能会注意到 CPU 始终处于满负荷状态。这是因为硬件卸载并非在所有桥接上都可用，而仅在一个桥接上可用。通过检查硬件卸载状态，你会注意到只有一个桥接启用了该功能：

```ros
[admin@MikroTik] > /interface/bridge/port/print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE                                 BRIDGE                                 HW
 0   H ether1                                    bridge1                                yes
 1   H ether2                                    bridge1                                yes
 2     ether3                                    bridge2                                yes
 3     ether4                                    bridge2                                yes
```

只有一个桥接具有硬件卸载标志的原因是设备不支持端口隔离。如果不支持端口隔离，则只有一个桥接能够将流量卸载到交换芯片。

### 症状

以下是可能由这种配置错误导致的一些症状列表：

- 桥接端口缺少“H”标志。
- 吞吐量低。
- CPU 使用率高。

### 解决方案

并非所有设备都支持端口隔离。目前只有 CRS1xx/CRS2xx 系列设备支持，并且同时最多支持 7 个隔离且硬件卸载的桥接。其他设备将不得不使用 CPU 在其他桥接上转发数据包。这通常是硬件限制，可能需要更换不同的设备。桥接水平分割参数是一项软件功能，它会禁用硬件卸载；当使用桥接过滤规则时，需要将所有数据包转发到 CPU，这要求禁用硬件卸载。你可以使用 `hw=yes` 标志控制哪个桥接将被硬件卸载，并设置其他桥接为 `hw=no`，例如：

```ros
/interface/bridge/port/set [find where bridge=bridge1] hw=no
/interface/bridge/port/set [find where bridge=bridge2] hw=yes
```

有时可以通过重构网络拓扑来使用 VLAN，这是隔离 Layer2 网络的正确方法。

## 硬件卸载和 MAC 学习的数据包流

---

考虑以下场景：你设置了一个桥接并启用了硬件卸载以最大化设备吞吐量；因此，你的设备作为交换机工作，但你想使用 [Sniffer](../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md) 或 [Torch](../../diagnostics-monitoring-and-troubleshooting/torch.md) 工具进行调试，或者你可能想实现数据包日志记录。

### 配置

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 hw=yes interface=ether1 learn=yes
add bridge=bridge1 hw=yes interface=ether2 learn=yes
```

### 问题

当运行 [Sniffer](../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md) 或 [Torch](../../diagnostics-monitoring-and-troubleshooting/torch.md) 工具捕获数据包时，你可能会注意到几乎看不到任何数据包，只有一些单播数据包，但主要是广播/组播数据包被捕获，而接口报告通过某些接口的流量远大于捕获的流量。如果你将两个或更多以太网接口添加到桥接并启用 [硬件卸载](../#bridge-hardware-offloading)，则交换芯片将用于在端口之间转发数据包。要理解为什么只捕获到部分数据包，我们必须首先检查交换芯片如何与 CPU 互连。在此示例中，我们可以使用通用 5 端口以太网路由器的框图：

![交换芯片框图](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/layer2-misconfiguration-01.webp)

对于此设备，每个以太网端口都连接到交换芯片，交换芯片通过 CPU 端口（有时称为 **switch-cpu** 端口）连接到 CPU。要使数据包在 Sniffer 或 Torch 工具中可见，数据包必须从以太网端口发送到 CPU 端口，这意味着数据包必须发往 CPU 端口（数据包的目的 MAC 地址与桥接的 MAC 地址匹配）或数据包的 MAC 地址尚未学习（数据包被泛洪到所有端口），这种行为是由于 **MAC 学习** 造成的。

交换芯片维护一个称为 **主机表** 的 MAC 地址和端口列表。每当需要转发数据包时，交换芯片会根据主机表检查数据包的目的 MAC 地址，以确定应使用哪个端口转发数据包。如果交换芯片找不到目的 MAC 地址，则数据包会被泛洪到所有端口（包括 CPU 端口）。在数据包应从例如 ether1 转发到 ether2 且 ether2 后面设备的 MAC 地址已在主机表中的情况下，数据包永远不会发送到 CPU，因此 Sniffer 或 Torch 工具将无法看到它。

### 症状

以下是可能由这种配置错误导致的一些症状列表：

- Sniffer 或 Torch 工具看不到数据包。
- 过滤规则不起作用。

### 解决方案

目的 MAC 地址已被学习的数据包不会被发送到 CPU，因为这些数据包不会被泛洪到所有端口。如果确实需要将某些数据包发送到 CPU 进行数据包分析或防火墙处理，则可以使用 ACL 规则将数据包复制或重定向到 CPU。以下是如何发送发往 **4C:5E:0C:4D:12:4B** 的数据包副本的示例：

```ros
/interface/ethernet/switch/rule
add copy-to-cpu=yes dst-mac-address=4C:5E:0C:4D:12:4B/FF:FF:FF:FF:FF:FF ports=ether1 switch=switch1
```

:::warning
如果数据包被发送到 CPU，则必须由 CPU 处理；这会增加 CPU 负载。
:::

## LAG 接口和负载均衡

---

考虑以下场景：你创建了一个 LAG 接口以增加两个网络节点之间的总带宽；通常这些节点是交换机。为了测试目的以确保 LAG 接口正常工作，你连接了两台传输数据的服务器，最常用的是众所周知的网络性能测量工具 [Iperf](https://en.wikipedia.org/wiki/Iperf) 来测试此类设置。例如，你可能用两个千兆以太网端口创建了一个 LAG 接口，这为你提供了一个可以在两个接口上负载均衡流量的虚拟接口，理论上可以达到 2Gbps 的吞吐量，而服务器则使用例如 SFP+ 的 10Gbps 接口连接。

![LACP 设置](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/layer2-misconfiguration-02.webp)

### 配置

以下配置与 **SW1** 和 **SW2** 相关：

```ros
/interface/bonding
add mode=802.3ad name=bond1 slaves=ether1,ether2
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=bond1
add bridge=bridge1 interface=sfp-sfpplus1
```

### 问题

经过初步测试，你立即注意到网络吞吐量从未超过 1Gbps 限制，即使服务器和网络节点（此处为交换机）上的 CPU 负载都很低，但吞吐量仍然仅限于 1Gbps。其原因是 LACP (802.ad) 使用传输哈希策略来确定流量是否可以在多个 LAG 成员之间进行负载均衡。在这种情况下，LAG 接口并不是创建一个 2Gbps 的接口，而是一个可以在可能的情况下将流量均衡到多个从属接口的接口。对于每个数据包，都会生成一个传输哈希，这决定了数据包将通过哪个 LAG 成员发送，这是为了避免数据包乱序所必需的。有一个选项可以选择传输哈希策略，通常可以在 Layer2 (MAC)、Layer3 (IP) 和 Layer4 (端口) 之间选择。在 RouterOS 中，可以通过使用 `transmit-hash-policy` 参数来选择。在这种情况下，由于你向相同的目的 MAC 地址以及相同的 IP 地址发送数据包，并且 Iperf 也使用相同的端口，因此所有数据包生成的传输哈希都是相同的，无法在 LAG 成员之间进行负载均衡。请注意，即使目的地不同，数据包也不总是能在 LAG 成员之间均衡，这是因为标准化的传输哈希策略可能为不同的目的地生成相同的传输哈希，例如，192.168.0.1/192.168.0.2 会被均衡，但 192.168.0.2/192.168.0.4 在 `layer2-and-3` 传输哈希策略且目的 MAC 地址相同的情况下 **不会** 被均衡。

### 症状

以下是可能由这种配置错误导致的一些症状列表：

- 流量仅通过一个 LAG 成员。

### 解决方案

选择正确的传输哈希策略并正确测试网络吞吐量。测试此类设置的最简单方法是使用多个目的地，例如，不要只向一台服务器发送数据，而是向多台服务器发送数据。这将为每个数据包生成不同的传输哈希，并使跨 LAG 成员的负载均衡成为可能。对于某些设置，你可能需要更改绑定接口模式以增加总吞吐量。对于 UDP 流量，`balance-rr` 模式可能就足够了，但可能会导致 TCP 流量出现问题。你可以在此处 [阅读更多](../../high-availability-solutions/bonding.md#bonding-modes) 关于为你的设置选择正确模式的信息。

## 从属接口上的 VLAN 接口

---

考虑以下场景：你创建了一个桥接，并且希望 DHCP 服务器仅向某些带标签的 VLAN 流量分配 IP 地址。为此，你创建了一个 VLAN 接口，指定了 VLAN ID，并在其上创建了 DHCP 服务器，但由于某种原因，它无法正常工作。

### 配置

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add interface=ether1 bridge=bridge1
add interface=ether2 bridge=bridge1
/interface/vlan
add name=VLAN99 interface=ether1 vlan-id=99
/ip/pool
add name=VLAN99_POOL range=192.168.99.100-192.168.99.200
/ip/address/add address=192.168.99.1/24 interface=VLAN99
/ip/dhcp-server
add interface=VLAN99 address-pool=VLAN99_POOL disabled=no
/ip/dhcp-server/network
add address=192.168.99.0/24 gateway=192.168.99.1 dns-server=192.168.99.1
```

### 问题

当你将接口添加到桥接时，桥接成为主接口，所有桥接端口都成为从属端口。这意味着在桥接端口上接收的所有流量都被桥接接口捕获，并且所有流量都使用桥接接口而不是物理接口转发到 CPU。因此，在从属接口上创建的 VLAN 接口永远不会捕获任何流量，因为在进行任何数据包处理之前，流量会立即被转发到主接口。通常的副作用是某些 DHCP 客户端能获取 IP 地址，而有些则不能。

### 症状

以下是可能由这种配置错误导致的一些症状列表：

- DHCP 客户端/服务器无法正常工作。
- 设备无法访问。
- 桥接后面的设备无法通过带标签的流量访问。

### 解决方案

更改 VLAN 接口监听流量的接口，将其更改为主接口：

```ros
/interface/vlan/set VLAN99 interface=bridge1
```

## 桥接中的桥接上的 VLAN

---

考虑以下场景：你有一组接口（不一定是物理接口），并且希望它们都位于同一 Layer2 网段。解决方案是将它们添加到单个桥接中，但你需要来自一个端口的流量将所有流量标记到某个 VLAN。这可以通过在桥接接口之上创建 VLAN 接口，并创建一个单独的新桥接来包含这个新创建的 VLAN 接口和一个旨在为所有接收流量添加 VLAN 标签的接口来实现。网络图如下所示：

![桥接中的桥接上的 VLAN](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/layer2-misconfiguration-03.webp)

### 配置

```ros
/interface/bridge
add name=bridge1
add name=bridge2
/interface/vlan
add interface=bridge1 name=VLAN vlan-id=99
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge2 interface=VLAN
add bridge=bridge2 interface=ether3
```

### 问题

为了更好地理解潜在问题，让我们首先查看桥接主机表。

```ros
[admin@switch] /interface/bridge/host/print where !local 
Flags: X - disabled, I - invalid, D - dynamic, L - local, E - external 
 #       MAC-ADDRESS        VID ON-INTERFACE    BRIDGE
 0   D   CC:2D:E0:E4:B3:A1      ether1          bridge1
 1   D   CC:2D:E0:E4:B3:A2      ether2          bridge1
 2   D   CC:2D:E0:E4:B3:A1      VLAN            bridge2
 3   D   CC:2D:E0:E4:B3:A2      VLAN            bridge2
 4   D   CC:2D:E0:E4:B3:A3      ether3          bridge2
```

**ether1** 和 **ether2** 上的设备需要发送带有 VLAN-ID 99 的标记数据包才能到达 **ether3** 上的主机（其他数据包不会传递到 VLAN 接口并进一步与 ether3 桥接）。我们可以在主机表中看到 **bridge2** 已经学习了这些主机。从 **ether3** 到 **ether1** 的数据包将被正确地带标签发送出去，并且流量不会在 **bridge1** 中被泛洪。但是，由于 MAC 学习只能在桥接端口之间进行，而不能在桥接接口之上创建的接口上进行，因此从 **ether2** 发送到 **ether3** 的数据包将在 **bridge1** 中被泛洪。

此外，如果 **ether3** 后面的设备使用 (R)STP，那么 **ether1** 和 **ether2** 将发送带标签的 BPDU，这违反了 IEEE 802.1W 标准。由于 MAC 学习功能损坏和 (R)STP 损坏，必须避免这种设置和配置。众所周知，在某些设置中，这种配置可能会阻止你通过 MAC telnet 连接到设备。

### 症状

以下是可能由这种配置错误导致的一些症状列表：

- 端口被 RSTP 阻塞。
- 网络中出现环路。
- 端口抖动。
- 流量被泛洪到所有端口。
- MAC telnet 无法连接。
- 设备无法访问。

### 解决方案

使用桥接 VLAN 过滤。标记流量的正确方法是在流量进入桥接时分配一个 VLAN ID。通过为桥接端口指定 **PVID** 值并指定哪些端口是 **标记**（trunk）端口，哪些是 **未标记**（access）端口，可以轻松实现此行为。以下是此类设置应如何配置的示例：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3 pvid=99
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1,ether2 untagged=ether3 vlan-ids=99
```

:::danger
启用 `vlan-filtering` 将过滤发往 CPU 的流量，在启用 VLAN 过滤之前，应确保已设置 [管理端口](../#management-access-configuration)。
:::

## 带物理接口的桥接中的 VLAN

---

与 [桥接中的桥接上的 VLAN](layer2-misconfiguration.md#vlan-on-a-bridge-in-a-bridge) 的情况非常相似。最流行的用例是当你想要桥接一个物理接口和一个 VLAN（简化的 trunk/access 端口设置）时。在这种设置中，你可能希望在一侧发送带标签的流量，在另一侧发送不带标签的流量。为此，你在 trunk 端口（带标签侧）上创建一个 VLAN 接口，然后创建一个桥接，并将 VLAN 接口和物理接口（不带标签侧）都添加为桥接端口。

### 配置

```ros
/interface/vlan
add interface=ether1 name=VLAN99 vlan-id=99
/interface/bridge
add name=bridge1
/interface/bridge/port
add interface=ether2 bridge=bridge1
add interface=VLAN99 bridge=bridge1
```

### 问题

这种设置和配置在大多数情况下都能工作，但在使用 (R/M)STP 时违反了 IEEE 802.1W 标准。如果这是你的 Layer2 域中唯一的设备，那么这应该不会引起问题，但当有其他厂商的交换机时，问题就可能出现。原因是桥接接口上的 RSTP 默认是启用的，允许从每个桥接端口发送桥接协议数据单元 (BPDU)。虽然 **ether2** 正确发送不带标签的 BPDU，但 **VLAN99** 接口作为桥接端口，会通过 ether1 发送带标签的 BPDU。并非所有交换机都能理解带标签的 BPDU。在更复杂的网络中，当存在针对特定（组）VLAN 的多个网络拓扑时，应谨慎使用此配置。这与混合厂商设备环境下的 MSTP 和 PVSTP(+) 相关。在针对特定 VLAN 具有多个网络拓扑的环形拓扑中，交换机的一个端口将被阻塞，但在 MSTP 和 PVSTP(+) 中，可以为特定 VLAN 打开一条路径。在这种情况下，不支持 PVSTP(+) 的设备可能会取消 BPDU 的标签并转发 BPDU，导致交换机接收到自己的数据包，触发环路检测并阻塞端口。这也可能发生在其他协议上，但 (R)STP 是最常见的情况。如果交换机使用 BPDU 保护功能，则此类配置可能会触发该功能并导致端口被 STP 阻塞。据报道，使用 6.41 或更高版本时，此类配置可能会随着时间的推移阻止流量通过某些桥接端口转发。此类配置不仅会破坏 (R/M)STP，还可能导致环路警告。这可能是由 MNDP 数据包或任何其他直接从接口发送的数据包引起的。

### 症状

以下是可能由这种配置错误导致的一些症状列表：

- 端口被 RSTP 阻塞。
- 网络中出现环路。
- 端口抖动。
- 流量随时间推移停止转发。
- 其他启用 RSTP 的设备忽略 BPDU。

### 解决方案

为避免兼容性问题，应使用桥接 VLAN 过滤。以下示例展示了如何使用桥接 VLAN 过滤配置实现相同的流量标记效果：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2 pvid=99
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 untagged=ether2 vlan-ids=99
```

:::danger
启用 `vlan-filtering` 将过滤发往 CPU 的流量。在启用 VLAN 过滤之前，应确保已设置 [管理端口](../#management-access-configuration)。
:::

## 物理接口上的桥接 VLAN

---

与 [桥接中的桥接上的 VLAN](layer2-misconfiguration.md#vlan-on-a-bridge-in-a-bridge) 的情况非常相似：考虑以下场景。你的网络中有几台交换机，并且使用 VLAN 来隔离某些 Layer2 域，并将这些交换机连接到一台负责分配地址并将流量路由到外界的路由器。为了冗余，你将所有交换机直接连接到路由器并启用了 RSTP，但为了能够设置 DHCP 服务器，你决定为连接到交换机的每个物理接口上的每个 VLAN 创建一个 VLAN 接口，并将这些 VLAN 接口添加到一个桥接中。网络图如下所示：

![桥接 VLAN](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/layer2-misconfiguration-04.webp)

### 配置

只有路由器部分与此案例相关，只要端口是交换的，交换机配置并不重要。路由器配置如下：

```ros
/interface/bridge
add name=bridge10
add name=bridge20
/interface/vlan
add interface=ether1 name=ether1_v10 vlan-id=10
add interface=ether1 name=ether1_v20 vlan-id=20
add interface=ether2 name=ether2_v10 vlan-id=10
add interface=ether2 name=ether2_v20 vlan-id=20
/interface/bridge/port
add bridge=bridge10 interface=ether1_v10
add bridge=bridge10 interface=ether2_v10
add bridge=bridge20 interface=ether1_v20
add bridge=bridge20 interface=ether2_v20
```

### 问题

你可能会注意到网络出现奇怪的延迟，甚至网络无响应。你可能会注意到检测到环路（收到带有自己 MAC 地址的数据包），并且一些流量无缘无故地产生。问题发生的原因是，来自 **路由器** 上创建的任一 VLAN 接口的广播数据包将从物理接口发送出去，该数据包将通过物理接口、通过交换机转发，并将在不同的物理接口上被接收回来。在这种情况下，从 **ether1\_v10** 发送的广播数据包将在 **ether2** 上被接收，该数据包将被 **ether2\_v10** 捕获，而 **ether2\_v10** 与 **ether1\_v10** 桥接，并将再次通过相同的路径转发（环路）。(R)STP 可能并不总能检测到此环路，因为 (R)STP 不感知任何 VLAN。对于不带标签的流量，环路不存在，但对于带标签的流量，环路存在。在这种场景下，发现环路是相当明显的，但在更复杂的设置中，并不总是容易检测到网络设计缺陷。有时，如果你的网络不使用广播流量，这种网络设计缺陷可能会在很长一段时间内不被注意到。通常，[邻居发现协议](../../system-information-and-utilities/neighbor-discovery.md) 会从 VLAN 接口广播数据包，并且通常会在这种设置中触发环路检测。有时，捕获触发环路检测的数据包是很有用的，这可以通过使用嗅探器并分析数据包捕获文件来完成：

```ros
/tool/sniffer
set filter-mac-address=4C:5E:0C:4D:12:44/FF:FF:FF:FF:FF:FF \
filter-interface=ether1 filter-direction=rx file-name=loop_packet.pcap
```

或者使用更方便的日志记录方式：

```ros
/interface/bridge/filter
add action=log chain=forward src-mac-address=4C:5E:0C:4D:12:44/FF:FF:FF:FF:FF:FF
add action=log chain=input src-mac-address=4C:5E:0C:4D:12:44/FF:FF:FF:FF:FF:FF
```

### 症状

以下是可能由这种配置错误导致的一些症状列表：

- 端口被 (R)STP 阻塞。
- 网络中出现环路。
- 吞吐量低。
- 端口抖动。
- 网络无法访问。

### 解决方案

解决方案是使用桥接 VLAN 过滤，以使所有桥接兼容 IEEE 802.1W 和 IEEE 802.1Q。

```ros
/interface/bridge
add name=bridge vlan-filtering=yes
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
/interface/bridge/vlan
add bridge=bridge tagged=ether1,ether2,bridge vlan-ids=10
add bridge=bridge tagged=ether1,ether2,bridge vlan-ids=20
/interface/vlan
add name=vlan10 interface=bridge vlan-id=10
add name=vlan20 interface=bridge vlan-id=20
```

:::danger
启用 `vlan-filtering` 将过滤发往 CPU 的流量。在启用 VLAN 过滤之前，应确保已设置 [管理端口](../#management-access-configuration)。
:::

## 桥接 VLAN

---

这是 [物理接口上的桥接 VLAN](layer2-misconfiguration.md#bridged-vlan-on-physical-interfaces) 的一个更简化的场景，但在这种情况下，你只是简单地将两个或多个在不同物理接口上创建的 VLAN 桥接在一起。这是一种非常常见的设置类型，值得单独撰写一篇文章，因为错误配置此类设置已导致多次网络故障。这种类型的设置也用于 VLAN 转换。

### 配置

```ros
/interface/vlan
add interface=ether1 name=ether1_v10 vlan-id=10
add interface=ether2 name=ether2_v10 vlan-id=10
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1_v10
add bridge=bridge1 interface=ether2_v10
```

### 问题

你可能会注意到网络的某些部分无法访问和/或某些链路持续抖动。这是由于 (R)STP 造成的。这种类型的配置迫使设备发送可能不被其他设备（包括 RouterOS）支持的带标签的 BPDU。由于设备接收到格式错误的数据包（在运行 (R)STP 时，网络中不应存在带标签的 BPDU，这违反了 IEEE 802.1W 和 IEEE 802.1Q），设备将无法正确解释该数据包，并可能出现意外行为。

### 症状

以下是可能由这种配置错误导致的一些症状列表：

- 端口被 (R)STP 阻塞。
- 端口抖动。
- 网络无法访问。

### 解决方案

最简单的解决方案是直接在桥接上禁用 (R)STP：

```ros
/interface/bridge
set bridge1 protocol-mode=none
```

尽管如此，仍然建议重写你的配置以使用桥接 VLAN 过滤：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1,ether2 vlan-ids=10
```

:::danger
启用 `vlan-filtering` 将过滤发往 CPU 的流量。在启用 VLAN 过滤之前，应确保已设置 [管理端口](../#management-access-configuration)。
:::

## 无硬件卸载的桥接 VLAN 过滤

---

考虑以下场景：你了解了新的桥接 VLAN 过滤功能，并决定更改设备上的配置。你有一个非常简单的 trunk/access 端口设置，并且你喜欢桥接 VLAN 过滤的概念。

### 配置

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2 pvid=20
add bridge=bridge1 interface=ether3 pvid=30
add bridge=bridge1 interface=ether4 pvid=40
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 untagged=ether2 vlan-ids=20
add bridge=bridge1 tagged=ether1 untagged=ether3 vlan-ids=30
add bridge=bridge1 tagged=ether1 untagged=ether4 vlan-ids=40
```

### 问题

例如，你在 CRS1xx/CRS2xx 系列设备上使用此配置，并开始注意到 CPU 使用率非常高。当运行性能测试检查网络吞吐量时，你注意到总吞吐量仅为其应轻松达到的线速性能的一小部分。问题的原因是并非所有设备都在硬件级别支持桥接 VLAN 过滤。所有设备都可以配置桥接 VLAN 过滤，但只有少数设备能够将流量卸载到交换芯片。如果在带有内置交换芯片的设备上使用了不正确的配置方法，则将使用 CPU 来转发流量。

### 症状

以下是可能由这种配置错误导致的一些症状列表：

- 桥接端口缺少“H”标志。
- 吞吐量低。
- CPU 使用率高。

### 解决方案

在使用桥接 VLAN 过滤之前，请检查你的设备是否在硬件级别支持它。兼容性表可在 [桥接硬件卸载](../#bridge-hardware-offloading) 部分找到。目前每种类型的设备都需要不同的配置方法。以下列表说明了应在设备上使用哪种配置以利用硬件卸载的优势：

- [带有 Marvell Prestera 交换芯片的 MikroTik 设备](../index.md#bridge-vlan-filtering)
- [CRS1xx/CRS2xx 系列设备](./crs1xx-2xx-series-switches-examples.md#vlan)
- [带有交换芯片的其他设备](../switch-chip-features.md#setup-examples)

## 多交换芯片的 VLAN 过滤

---

考虑以下场景：你有一台带有两个或更多交换芯片的设备，并且你决定使用单个桥接并在硬件级别设置 VLAN 过滤（通过使用 `/interface/ethernet/switch` 菜单）以实现网络线速性能。这与 RB2011 和 RB3011 系列设备非常相关。在此示例中，假设你想要一个 trunk 端口，所有其他端口都是 access 端口，例如，**ether10** 是我们的 trunk 端口，**ether1-ether9** 是我们的 access 端口。

### 配置

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
add bridge=bridge1 interface=ether4
add bridge=bridge1 interface=ether5
add bridge=bridge1 interface=ether6
add bridge=bridge1 interface=ether7
add bridge=bridge1 interface=ether8
add bridge=bridge1 interface=ether9
add bridge=bridge1 interface=ether10
/interface/vlan
add interface=bridge1 name=VLAN10 vlan-id=10
/interface/ethernet/switch/port
set ether1,ether2,ether3,ether4,ether5,ether6,ether7,ether8,ether9 default-vlan-id=10 vlan-header=always-strip vlan-mode=secure
set ether10 vlan-header=add-if-missing vlan-mode=secure
set switch1-cpu,switch2-cpu vlan-mode=secure
/interface/ethernet/switch/vlan
add ports=ether1,ether2,ether3,ether4,ether5,switch1-cpu switch=switch1 vlan-id=10
add ports=ether6,ether7,ether8,ether9,ether10,switch2-cpu switch=switch2 vlan-id=10
```

### 问题

运行几次测试后，你可能会注意到来自 **ether6-ether10** 的数据包按预期转发，但来自 **ether1-ether5** 的数据包并不总是被正确转发（尤其是通过 trunk 端口）。最明显的问题是从 **ether1-ether5** 通过 **ether10** 的数据包被直接丢弃。这是因为这些端口位于不同的交换芯片上。这意味着无法在硬件级别进行 VLAN 过滤，因为交换芯片不知道不同交换芯片上 VLAN 表的内容。在不同交换芯片上的端口之间转发的数据包也由 CPU 处理，这意味着你无法实现线速性能。

### 症状

以下是可能由这种配置错误导致的一些症状列表：

- 数据包被丢弃。
- 吞吐量低。

### 解决方案

正确的解决方案是考虑这种硬件设计并相应地规划你的网络拓扑。要解决此问题，你必须创建两个独立的桥接并在每个交换芯片上配置 VLAN 过滤。这限制了在交换芯片之间转发数据包的可能性，但可以在两个桥接之间配置路由（如果每个交换芯片上连接的设备使用不同的网络子网）。

有一种方法可以配置设备使所有端口一起交换，同时能够在硬件级别使用 VLAN 过滤，尽管此解决方案有一些注意事项。其思想是在每个交换芯片上牺牲一个以太网端口作为 trunk 端口，用于在交换芯片之间转发数据包。这可以通过在两个交换芯片之间插入一根以太网电缆来实现。例如，让我们在 **ether5** 和 **ether6** 之间插入一根以太网电缆，然后重新配置你的设备，假设这些端口是 trunk 端口：

```ros
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
add bridge=bridge1 interface=ether4
add bridge=bridge1 interface=ether5
add bridge=bridge2 interface=ether6
add bridge=bridge2 interface=ether7
add bridge=bridge2 interface=ether8
add bridge=bridge2 interface=ether9
add bridge=bridge2 interface=ether10
/interface/ethernet/switch/port
set ether1,ether2,ether3,ether4,ether7,ether8,ether9 default-vlan-id=10 vlan-header=always-strip vlan-mode=secure
set ether5,ether6,ether10 vlan-header=add-if-missing vlan-mode=secure default-vlan-id=auto
set switch1-cpu,switch2-cpu vlan-mode=secure
/interface/ethernet/switch/vlan
add ports=ether1,ether2,ether3,ether4,ether5,switch1-cpu switch=switch1 vlan-id=10
add ports=ether6,ether7,ether8,ether9,ether10,switch2-cpu switch=switch2 vlan-id=10
```

:::warning
对于 100Mbps 交换芯片，请使用 `default-vlan-id=0` 而不是 `default-vlan-id=auto`
:::

## 使用简化桥接 VLAN 表的 VLAN 过滤

---

:::info
此问题已在 **RouterOS v7.15** 中解决。动态 VLAN 现在始终作为单独的条目创建，不再与静态配置的条目合并。
:::

你需要创建一个网络设置，其中多个客户端连接到独立的 access 端口，并通过不同的 VLAN 进行隔离。此流量应被标记并发送到适当的 trunk 端口。Access 端口使用 pvid 属性配置。由于 trunk 端口用于两个 VLAN，你决定通过添加单个桥接 VLAN 表条目并用逗号分隔 VLAN 来简化配置。当标记的 trunk 端口用于大量 VLAN 甚至某些 VLAN 范围（例如 vlan-id=100-200）时，这尤其有用。请参见下面的网络图和配置。

![交换机多个未标记端口](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/layer2-misconfiguration-05.webp)

### 配置

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3 pvid=10
add bridge=bridge1 interface=ether4 pvid=20
/interface/bridge/vlan
add bridge=bridge1 tagged=ether2 vlan-ids=10,20
```

### 问题

流量从 access 端口正确转发并标记到 trunk 端口，但你可能会注意到一些广播或组播数据包实际上在两个未标记的 access 端口之间被泛洪，尽管它们应该在不同的 VLAN 上。此外，来自标记端口的广播和组播流量也被泛洪到两个 access 端口。这可能会引起一些安全问题，因为来自不同网络的流量可以被嗅探。当你查看桥接 VLAN 表时，你注意到为 VLAN 10 和 20 创建了一个条目，并且两个未标记端口都是同一 VLAN 组的一部分。

```ros
[admin@SW1] /interface/bridge/vlan/print where tagged=ether2
Columns: BRIDGE, VLAN-IDS, CURRENT-TAGGED, CURRENT-UNTAGGED
# BRIDGE   VLAN-IDS  CURRENT-TAGGED  CURRENT-UNTAGGED
;;; port with pvid added to untagged group which might cause problems, consider adding a separate VLAN entry
0 bridge1        10  ether2          ether3          
                 20                  ether4     
```

### 症状

- 流量在不同 VLAN 之间泛洪
- 红色警告：`port with pvid added to untagged group which might cause problems, consider adding a separate VLAN entry`

### 解决方案

当使用 pvid 属性配置 access 端口时，它们会被动态添加到适当的 VLAN 条目中。创建具有多个 VLAN 或 VLAN 范围的静态 VLAN 条目