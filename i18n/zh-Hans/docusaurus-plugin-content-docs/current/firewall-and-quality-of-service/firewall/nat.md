# NAT

> MikroTik RouterOS 中的 NAT 功能支持私有网络与公共网络之间的 IPv4 地址转换，既支持用于隐藏内部 IP 的源 NAT（伪装），也支持用于将外部流量重定向到特定内部设备的目标 NAT。本文档说明了配置规则、NAT 类型以及连接跟踪问题的故障排除技巧。

# NAT

网络地址转换（Network Address Translation）是一种互联网标准，它允许局域网中的主机使用一组 IP 地址进行内部通信，而使用另一组 IP 地址进行外部通信。使用 NAT 的局域网被称为 *natted* 网络。要使 NAT 发挥作用，每个 *natted* 网络中都必须有一个 NAT 网关。NAT 网关（NAT 路由器）在数据包进出局域网时执行 IP 地址重写。RouterOS 支持 IPv4 的 NAT，但不支持 NAT64。

NAT 仅匹配连接的第一个数据包，连接跟踪会记住该操作，并对属于同一连接的所有其他数据包执行该操作。

:::danger
每当 NAT 规则被更改或添加时，应清除连接跟踪表；否则，在连接条目过期之前，NAT 规则可能看起来无法正常工作。
:::

## NAT 类型

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/firewall/img/nat-01.webp)

NAT 有两种类型：

- **源 NAT 或 srcnat。** 此类型的 NAT 对源自 natted 网络的数据包执行。当 IP 数据包通过路由器时，NAT 路由器会将数据包的私有源地址替换为新的公共 IP 地址。对反向传输的回复数据包执行相反的操作。
- **目标 NAT 或 dstnat。** 此类型的 NAT 对发往 natted 网络的数据包执行。它最常用于使私有网络上的主机可以从互联网访问。执行 dstnat 的 NAT 路由器在数据包通过路由器发往私有网络时，会替换数据包的目标 IP 地址。

从 RouterOS v7 开始，防火墙 NAT 新增了两个 *INPUT* 和 *OUTPUT* 链，用于处理发往和来自本地机器上运行的应用程序的数据包：

- **input** - 用于处理通过某个接口进入路由器，且目标 IP 地址为路由器自身地址之一的数据包。通过路由器的数据包不经过 input 链规则的检查。
- **output** - 用于处理源自路由器本身并通过某个接口离开的数据包。通过路由器的数据包不经过 output 链规则的检查。

### 目标 NAT

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/firewall/img/nat-02.webp)

网络地址转换通过修改数据包 IP 头中的网络地址信息来工作。让我们看一个常见的设置，其中网络管理员希望从互联网访问办公室服务器。

我们想要允许从互联网连接到本地 IP 为 10.0.0.3 的办公室服务器。在这种情况下，我们必须在办公室网关路由器上配置目标地址转换规则：

```ros
/ip/firewall/nat/add chain=dstnat action=dst-nat dst-address=172.16.16.1 dst-port=22 to-addresses=10.0.0.3 protocol=tcp
```

上述规则的含义是：当传入连接请求目标地址为 172.16.16.1 的 TCP 端口 22 时，使用 *dst-nat* 操作并将数据包重定向到本地 IP 地址为 10.0.0.3 且端口为 22 的设备。

:::tip
为了只允许从家里的 PC 访问，我们可以通过添加 *"src-address=192.168.88.1"* 来改进我们的 *dst-nat* 规则，这是（在此示例中）家庭 PC 的公共 IP 地址。这也被认为更安全！
:::

### 源 NAT

如果您想将本地设备隐藏在从 ISP 获取的公共 IP 地址后面，您应该配置 MikroTik 路由器的源网络地址转换（伪装）功能。
假设您想将办公室计算机和服务器都隐藏在公共 IP 172.16.16.1 后面。规则将如下所示：

```ros
/ip/firewall/nat/add chain=srcnat src-address=10.0.0.0/24 action=src-nat to-addresses=172.16.16.1 out-interface=WAN
```

现在，您的 ISP 将看到所有请求都来自 IP 172.16.16.1，而不会看到您局域网内的 IP 地址。

#### 伪装

防火墙 NAT `action=masquerade` 是 `action=srcnat` 的一个独特变体。它专为公共 IP 可能随机变化的情况而设计，例如 DHCP 服务器更改分配的 IP，或者 PPPoE 隧道在断开后获得不同的 IP，简而言之——**当公共 IP 是动态的时候**。

```ros
/ip/firewall/nat/add chain=srcnat src-address=10.0.0.0/24 action=masquerade out-interface=WAN
```

每次接口断开和/或其 IP 地址更改时，路由器将清除与该接口相关的所有已伪装的连接跟踪条目，从而在公共 IP 更改后加快系统恢复时间。如果使用 `srcnat` 而不是 `masquerade`，连接跟踪条目会保留，连接可以在链路故障后简单地恢复。

不幸的是，当主链路断开后连接被路由到不同链路时，这可能导致不稳定链路出现一些问题。在这种情况下，可能发生以下情况：

- 断开连接时，所有相关的连接跟踪条目被清除。
- 来自每个被清除（先前已伪装）连接的下一个数据包将作为 *新* 连接进入防火墙，如果主接口未恢复，数据包将通过备用路由（如果有）路由出去，从而创建新的伪装连接。
- 主链路恢复，路由恢复到主链路，因此属于现有连接的数据包通过主接口发送而无需伪装，从而将本地 IP 泄漏到公共网络。

为了解决这种情况，可以创建一条 **黑洞** 路由，作为可能因断开而消失的路由的替代方案。

NAT 路由器后面的主机没有真正的端到端连接。因此，某些互联网协议在 NAT 场景下可能无法工作。需要从私有网络外部发起 TCP 连接的服务或无状态协议（如 UDP）可能会中断。

为了克服这些限制，RouterOS 包含了许多所谓的 NAT 助手，为各种协议启用 NAT 穿越。

:::tip
尽管源 NAT 和伪装执行相同的基本功能：将一个地址空间映射到另一个地址空间，但细节略有不同。最明显的是，伪装为出站数据包选择的源 IP 地址是绑定到数据包将退出的接口的 IP 地址。
:::

#### CGNAT (NAT444)

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/firewall/img/nat-03.webp)

为了应对 IPv4 地址耗尽，RFC 6598 被部署。其思想是在运营商网络内部使用共享的 100.64.0.0/10 地址空间，并在运营商的边缘路由器上执行 NAT，将其转换为单个公共 IP 或公共 IP 范围。

由于这种设置的性质，它也被称为 NAT444，相对于“普通” NAT 环境的 NAT44 网络。涉及三个不同的 IPv4 地址空间。

RouterOS 上的 CGNAT 配置与任何其他常规源 NAT 配置没有区别：

```ros
/ip/firewall/nat
 add chain=srcnat action=src-nat src-address=100.64.0.0/10 to-address=2.2.2.2 out-interface=<public_if>
```

其中：

- 2.2.2.2 - 公共 IP 地址。
- public\_if - 提供商边缘路由器上连接到互联网的接口。

NAT444 的优势显而易见：使用更少的公共 IPv4 地址。但这项技术也有重大缺点：

- 执行 CGNAT 的服务提供商路由器需要为所有地址转换维护状态表：这需要大量的内存和 CPU 资源。
- 主机游戏问题。当两个使用相同外部公共 IPv4 地址的用户尝试相互连接时，某些游戏会失败。
- 出于法律原因跟踪用户意味着额外的日志记录，因为多个家庭共享一个公共地址。
- 任何需要传入连接的功能都会中断。虽然普通 NAT 已经存在这种情况，但最终用户通常仍然可以在其 NAT 路由器上设置端口转发。CGNAT 使这变得不可能。这意味着无法托管 Web 服务器，IP 电话默认也无法接听来电。
- 某些 Web 服务器只允许来自同一公共 IP 地址的最大连接数，以此作为对抗 SYN 洪水等 DoS 攻击的手段。使用 CGNAT，此限制更容易达到，某些服务的质量可能会变差。
- 6to4 需要全局可达的地址，并且在采用拓扑范围受限地址的网络中无法工作。

具有共享地址空间源地址或目标地址的数据包不得跨服务提供商边界转发。服务提供商必须在入口链路上过滤此类数据包。在 RouterOS 中，这可以通过边缘路由器上的防火墙过滤器轻松完成：

```ros
/ip/firewall/filter
 add chain=input src-address=100.64.0.0/10 action=drop in-interface=<public_if>
 add chain=output dst-address=100.64.0.0/10 action=drop out-interface=<public_if>
 add chain=forward src-address=100.64.0.0/10 action=drop in-interface=<public_if>
 add chain=forward src-address=100.64.0.0/10 action=drop out-interface=<public_if>
 add chain=forward dst-address=100.64.0.0/10 action=drop out-interface=<public_if>
```

服务提供商可能需要记录映射地址，在一个大型 CGN 部署网络中这可能是一个问题。幸运的是，RFC 7422 提出了一种管理 CGN 转换的方法，可以显著减少所需的日志记录量，同时为滥用响应提供可追溯性。

RFC 指出，CGN 可以确定性将客户私有地址（在 CGN 面向客户的接口上接收，也称为内部侧）映射到扩展了端口范围的公共地址，而不是记录每个连接。

这意味着必须添加单独的 NAT 规则来实现单独的映射，如下例所示：

|  |  |
| :-- | :-- |
| **内部 IP** | **外部 IP/端口范围** |
| 100.64.0.1 | 2.2.2.2:5000-5199 |
| 100.64.0.2 | 2.2.2.2:5200-5399 |
| 100.64.0.3 | 2.2.2.2:5400-5599 |
| 100.64.0.4 | 2.2.2.2:5600-5799 |
| 100.64.0.5 | 2.2.2.2:5800-5999 |

建议使用脚本而不是手动编写规则。以下示例可以根据您设置的任何要求进行调整。

```ros
{
######## 可调整值 #########
:local StartingAddress 100.64.0.1
:local ClientCount 5
:local AddressesPerClient 2
:local PublicAddress 2.2.2.2
:local StartingPort 5000
:local PortsPerAddress 200
####################################

# 所有客户端链跳转
/ip/firewall/nat/add chain=srcnat action=jump jump-target=clients \
    src-address="$StartingAddress-$($StartingAddress + ($ClientCount * $AddressesPerClient) - 1)"

:local currentPort $StartingPort

:for c from=1 to=$ClientCount do={
    # 特定客户端链跳转
    :if ($AddressesPerClient > 1) do={
      /ip/firewall/nat/add chain=clients action=jump jump-target="client-$c" \
      src-address="$($StartingAddress + ($AddressesPerClient * ($c - 1)))-$($StartingAddress + ($AddressesPerClient * $c -1))"
    } else={
      /ip/firewall/nat/add chain=clients action=jump jump-target="client-$c" \
      src-address="$($StartingAddress + ($AddressesPerClient * ($c - 1)))"
    }

    # 转换规则
    :for a from=1 to=$AddressesPerClient do={
      /ip/firewall/nat/add chain="client-$c" action=src-nat protocol=tcp \
      src-address="$($StartingAddress + (($c -1) * $AddressesPerClient) + $a - 1)" to-address=$PublicAddress to-ports="$currentPort-$($currentPort + $PortsPerAddress - 1)"
      /ip/firewall/nat/add chain="client-$c" action=src-nat protocol=udp \
      src-address="$($StartingAddress + (($c -1) * $AddressesPerClient) + $a - 1)" to-address=$PublicAddress to-ports="$currentPort-$($currentPort + $PortsPerAddress - 1)"
      :set currentPort ($currentPort + $PortsPerAddress)
    }
}
}
```

六个局部值可以调整，脚本可以简单地粘贴到终端中，也可以存储在系统脚本部分，以备日后需要重新生成配置。

执行后，您应该得到一组规则：

```ros
[admin@MikroTik] > ip firewall nat print
Flags: X - disabled, I - invalid; D - dynamic
 0    chain=srcnat action=jump jump-target=clients
      src-address=100.64.0.1-100.64.0.10

 1    chain=clients action=jump jump-target=client-1
      src-address=100.64.0.1-100.64.0.2

 2    chain=client-1 action=src-nat to-addresses=2.2.2.2 to-ports=5000-5199
      protocol=tcp src-address=100.64.0.1

 3    chain=client-1 action=src-nat to-addresses=2.2.2.2 to-ports=5000-5199
      protocol=udp src-address=100.64.0.1

 4    chain=client-1 action=src-nat to-addresses=2.2.2.2 to-ports=5200-5399
      protocol=tcp src-address=100.64.0.2

 5    chain=client-1 action=src-nat to-addresses=2.2.2.2 to-ports=5200-5399
      protocol=udp src-address=100.64.0.2

 6    chain=clients action=jump jump-target=client-2
      src-address=100.64.0.3-100.64.0.4

 7    chain=client-2 action=src-nat to-addresses=2.2.2.2 to-ports=5400-5599
      protocol=tcp src-address=100.64.0.3

 8    chain=client-2 action=src-nat to-addresses=2.2.2.2 to-ports=5400-5599
      protocol=udp src-address=100.64.0.3

 9    chain=client-2 action=src-nat to-addresses=2.2.2.2 to-ports=5600-5799
      protocol=tcp src-address=100.64.0.4

10    chain=client-2 action=src-nat to-addresses=2.2.2.2 to-ports=5600-5799
      protocol=udp src-address=100.64.0.4

11    chain=clients action=jump jump-target=client-3
      src-address=100.64.0.5-100.64.0.6

12    chain=client-3 action=src-nat to-addresses=2.2.2.2 to-ports=5800-5999
      protocol=tcp src-address=100.64.0.5

13    chain=client-3 action=src-nat to-addresses=2.2.2.2 to-ports=5800-5999
      protocol=udp src-address=100.64.0.5

14    chain=client-3 action=src-nat to-addresses=2.2.2.2 to-ports=6000-6199
      protocol=tcp src-address=100.64.0.6

15    chain=client-3 action=src-nat to-addresses=2.2.2.2 to-ports=6000-6199
      protocol=udp src-address=100.64.0.6

[...]
```

#### 发夹 NAT

发夹网络地址转换（*NAT 回环*）是指局域网中的设备可以通过网关路由器的公共 IP 地址访问局域网中的另一台机器。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/firewall/img/nat-02.webp)

在上面的例子中，网关路由器有以下 `dst-nat` 配置规则：

```ros
/ip/firewall/nat/add chain=dstnat action=dst-nat dst-address=172.16.16.1 dst-port=443 to-addresses=10.0.0.3 to-ports=443 protocol=tcp
```

当来自家里 PC 的用户与 Web 服务器建立连接时，路由器按配置执行 DST NAT：

1. 客户端发送一个源 IP 地址为 192.168.88.1、目标 IP 地址为 172.16.16.1 且端口为 443 的数据包，以请求一些 Web 资源。
2. 路由器对数据包执行目标 NAT，将其转换为 10.0.0.3，并相应地替换数据包中的目标 IP 地址。源 IP 地址保持不变：192.168.88.1。
3. 服务器回复客户端的请求，回复数据包的源 IP 地址为 10.0.0.3，目标 IP 地址为 192.168.88.1。
4. 路由器确定该数据包是先前连接的一部分，撤销目标 NAT，并将原始目标 IP 地址放入源 IP 地址字段。目标 IP 地址为 192.168.88.1，源 IP 地址为 172.16.16.1。
5. 客户端收到预期的回复数据包，连接建立。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/firewall/img/nat-04.webp)

但是，当与 Web 服务器位于同一网络的客户端请求连接到 Web 服务器的**公共** IP 地址时，会出现**问题**：

1. 客户端发送一个源 IP 地址为 10.0.0.2、目标 IP 地址为 172.16.16.1 且端口为 443 的数据包，以请求一些 Web 资源。
2. 路由器对数据包执行目标 NAT，将其转换为 10.0.0.3，并相应地替换数据包中的目标 IP 地址。源 IP 地址保持不变：10.0.0.2。
3. 服务器回复客户端的请求。但是，请求的源 IP 地址与 Web 服务器位于同一子网。Web 服务器不会将回复发送回路由器，而是直接发送回 10.0.0.2，回复中的源 IP 地址为 10.0.0.3。
4. 客户端收到回复数据包，但将其丢弃，因为它期望从 172.16.16.1 而不是 10.0.0.3 收到数据包。

为了解决此问题，我们将配置一个新的 *src-nat* 规则（发夹 NAT 规则），如下所示：

```ros
/ip/firewall/nat
add action=masquerade chain=srcnat dst-address=10.0.0.3 out-interface=LAN protocol=tcp src-address=10.0.0.0/24
```

配置上述规则后：

1. 客户端发送一个源 IP 地址为 10.0.0.2、目标 IP 地址为 172.16.16.1 且端口为 443 的数据包，以请求一些 Web 资源。
2. 路由器对数据包执行目标 NAT，将其转换为 10.0.0.3，并相应地替换数据包中的目标 IP 地址。它还对数据包执行源 NAT，并将数据包中的源 IP 地址替换为其 LAN 接口上的 IP 地址。目标 IP 地址为 10.0.0.3，源 IP 地址为 10.0.0.1。
3. Web 服务器回复请求，并将源 IP 地址为 10.0.0.3 的回复发送回路由器的 LAN 接口 IP 地址 10.0.0.1。
4. 路由器确定该数据包是先前连接的一部分，撤销源和目标 NAT，并将原始目标 IP 地址 172.16.16.1 放入源 IP 地址字段，将原始源 IP 地址 10.0.0.2 放入目标 IP 地址字段。

### 端点无关 NAT

端点无关 NAT 在源 NAT 中创建一个映射，并对具有相同源 IP 和端口的所有后续数据包使用相同的映射。此映射通过以下规则创建：

```ros
/ip/firewall/nat
add action=endpoint-independent-nat chain=srcnat out-interface=WAN protocol=udp
```

此映射允许运行源无关过滤，从而允许将来自 WAN 的任何源的数据包转发到映射的内部 IP 和端口。以下规则启用过滤：

```ros
/ip/firewall/nat
add action=endpoint-independent-nat chain=dstnat in-interface=WAN protocol=udp
```

:::danger
端点无关 NAT 仅适用于 UDP 协议。
:::

此外，endpoint-independent-nat 可以接受其他一些参数：

- `randomize-port` - 随机化公共端口连接将被映射到的端口。

更多信息请参见 [RFC 5128](https://www.ietf.org/rfc/rfc5128.txt) 第 2.2.3 和 2.2.5 节

## NAT 助手

NAT 路由器后面的主机没有真正的端到端连接。因此，某些互联网协议在 NAT 场景下可能无法工作。为了克服这些限制，RouterOS 包含了许多 NAT 助手，为各种协议启用 NAT 穿越。

NAT 助手可以在 `/ip/firewall/service-ports` 菜单中管理。

可用 NAT 助手列表：

| 助手 | 描述 |
| :-- | :-- |
| **FTP** | FTP 服务助手 |
| **H323** | H323 服务助手 |
| **IRC** | IRC 服务助手 |
| **PPTP** | PPTP (GRE) 隧道助手 |
| **UDPLITE** | UDP-Lite 服务助手 |
| **DCCP** | DCCP 服务助手 |
| **SCTP** | SCTP 服务助手 |
| **SIP** | SIP 助手。附加选项：`sip-direct-media` 允许将 RTP 媒体流重定向为直接从主叫方到被叫方。默认值为 `yes`。`sip-timeout` 允许调整 SIP UDP 连接的 TTL。默认值：1 小时。在某些设置中，您可能需要减小此值。 |
| **TFTP** | TFTP 服务助手 |
| **RTSP** | RTSP 服务助手 |

:::warning
如果未启用连接跟踪，则防火墙服务端口将显示为非活动状态

**警告：** **udplite**、**dccp** 和 **sctp** 是连接跟踪的内置服务。由于这些不是单独加载的模块，因此不能单独禁用；它们会与连接跟踪一起被禁用。
:::