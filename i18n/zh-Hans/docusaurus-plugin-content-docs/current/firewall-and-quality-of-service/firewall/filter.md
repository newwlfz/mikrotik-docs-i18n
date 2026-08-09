# 过滤器

> MikroTik RouterOS 中的防火墙过滤器通过预定义的链（input、forward、output）控制数据包流，允许或阻止流量，并可选择接受特定服务或丢弃恶意数据包。IPv4 配置通过 `/ip/firewall/filter` 完成，IPv6 通过 `/ipv6/firewall/filter` 完成，本文提供了保护路由器和局域网设备的示例。

# 过滤器

防火墙过滤器用于允许或阻止特定数据包，这些数据包可能被转发到您的本地网络、源自您的路由器，或目的地为路由器。

设置过滤有两种方法：

- 允许特定流量并丢弃所有其他流量。
- 仅丢弃恶意流量，允许所有其他流量。

两种方法各有利弊。例如，从安全角度来看，第一种方法更为安全，但每当需要接受新服务的流量时，都需要管理员介入。这种策略能很好地控制流量，并因服务配置错误而降低被入侵的可能性。

另一方面，在保护客户网络时，接受用户可能使用的所有服务将是一场管理噩梦。因此，在高级设置中，仔细规划防火墙至关重要。

防火墙过滤器由三个无法删除的预定义链组成：

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/firewall/img/filter-01.webp)

- **input** - 用于处理**进入路由器**的数据包，这些数据包通过某个接口进入，目标 IP 地址为路由器的地址之一。经过路由器的数据包不会根据 input 链的规则进行处理。
- **forward** - 用于处理**经过路由器**的数据包。
- **output** - 用于处理**源自路由器**并通过某个接口离开的数据包。经过路由器的数据包不会根据 output 链的规则进行处理。

防火墙过滤器配置可通过 IPv4 的 `/ip/firewall/filter` 菜单和 IPv6 的 `/ipv6/firewall/filter` 菜单访问。

## 防火墙示例

让我们看一个基本的防火墙示例，以保护路由器本身及其后面的客户端，涵盖 IPv4 和 IPv6 协议。

### IPv4 防火墙

#### 保护路由器本身

设置防火墙时遵循的经验法则：

- 使用 `new` 连接来减少路由器负载。
- 接受您需要的流量。
- `drop` 所有其他流量，可设置 `log=yes` 记录攻击者，但请注意，在遭受高强度攻击时，这可能会增加 CPU 负载。

我们总是从接受已知且已接受的连接开始，因此第一条规则应接受 "established" 和 "related" 连接。

```ros
/ip/firewall/filter
add action=accept chain=input comment="默认配置" connection-state=established,related
```

现在我们可以继续接受一些新连接。在我们的示例中，我们希望允许从任何地址访问 ICMP 协议，而其他所有内容仅允许从 192.168.88.2-192.168.88.254 地址范围访问。为此，我们创建一个地址列表和两条防火墙规则。

```ros
/ip/firewall/address-list
add address=192.168.88.2-192.168.88.254 list=allowed_to_router
/ip/firewall/filter
add action=accept chain=input src-address-list=allowed_to_router
add action=accept chain=input protocol=icmp

```

最后，我们丢弃所有其他流量：

```ros
add action=drop chain=input
```

刚创建的完整规则集：

```ros
/ip/firewall/filter
add action=accept chain=input comment="默认配置" connection-state=established,related
add action=accept chain=input src-address-list=allowed_to_router
add action=accept chain=input protocol=icmp
add action=drop chain=input
/ip/firewall/address-list
add address=192.168.88.2-192.168.88.254 list=allowed_to_router
```

#### 保护局域网设备

保护用户的概念非常相似，只是在这种情况下，我们阻止不需要的流量并接受所有其他流量。

首先，我们将创建一个名为 "not\_in\_internet" 的 `address-list`，用于防火墙过滤规则：

```ros
/ip/firewall/address-list
add address=0.0.0.0/8 comment=RFC6890 list=not_in_internet
add address=172.16.0.0/12 comment=RFC6890 list=not_in_internet
add address=192.168.0.0/16 comment=RFC6890 list=not_in_internet
add address=10.0.0.0/8 comment=RFC6890 list=not_in_internet
add address=169.254.0.0/16 comment=RFC6890 list=not_in_internet
add address=127.0.0.0/8 comment=RFC6890 list=not_in_internet
add address=224.0.0.0/4 comment=组播 list=not_in_internet
add address=198.18.0.0/15 comment=RFC6890 list=not_in_internet
add address=192.0.0.0/24 comment=RFC6890 list=not_in_internet
add address=192.0.2.0/24 comment=RFC6890 list=not_in_internet
add address=198.51.100.0/24 comment=RFC6890 list=not_in_internet
add address=203.0.113.0/24 comment=RFC6890 list=not_in_internet
add address=100.64.0.0/10 comment=RFC6890 list=not_in_internet
add address=240.0.0.0/4 comment=RFC6890 list=not_in_internet
```

简要防火墙过滤规则说明：

- 具有 *connection-state=established,related* 的数据包被添加到 FastTrack 以实现更快的数据吞吐量，防火墙将仅处理新连接。
- 丢弃 *invalid* 连接，并使用前缀 "invalid" 记录日志。
- 丢弃从本地网络尝试访问非公共地址的数据包，事先应用 *address-list=not\_in\_internet*，"bridge" 是本地网络接口，使用前缀 "!public\_from\_LAN" 记录尝试日志。
- 丢弃未经过 NAT 的传入数据包，ether1 是公共接口，使用 "!NAT" 前缀记录尝试日志。
- 跳转到 ICMP 链以丢弃不需要的 ICMP 消息。
- 丢弃来自互联网的非公共 IP 地址的传入数据包，ether1 是公共接口，使用前缀 "!public" 记录尝试日志。
- 丢弃来自局域网但没有局域网 IP 的数据包，192.168.88.0/24 是本地网络子网。

```ros
/ip/firewall/filter
add action=fasttrack-connection chain=forward comment=FastTrack connection-state=established,related
add action=accept chain=forward comment="已建立、相关" connection-state=established,related
add action=drop chain=forward comment="丢弃无效" connection-state=invalid log=yes log-prefix=invalid
add action=drop chain=forward comment="丢弃从局域网尝试访问非公共地址的数据包" dst-address-list=not_in_internet in-interface=bridge log=yes log-prefix=!public_from_LAN out-interface=!bridge
add action=drop chain=forward comment="丢弃未经过 NAT 的传入数据包" connection-nat-state=!dstnat connection-state=new in-interface=ether1 log=yes log-prefix=!NAT
add action=jump chain=forward protocol=icmp jump-target=icmp comment="跳转到 ICMP 过滤器"
add action=drop chain=forward comment="丢弃来自互联网的非公共 IP 地址的传入数据包" in-interface=ether1 log=yes log-prefix=!public src-address-list=not_in_internet
add action=drop chain=forward comment="丢弃来自局域网但没有局域网 IP 的数据包" in-interface=bridge log=yes log-prefix=LAN_!LAN src-address=!192.168.88.0/24
```

在 "icmp" 链中仅允许需要的 ICMP 代码：

```ros
/ip/firewall/filter
  add chain=icmp protocol=icmp icmp-options=0:0 action=accept \
    comment="回显应答"
  add chain=icmp protocol=icmp icmp-options=3:0 action=accept \
    comment="网络不可达"
  add chain=icmp protocol=icmp icmp-options=3:1 action=accept \
    comment="主机不可达"
  add chain=icmp protocol=icmp icmp-options=3:4 action=accept \
    comment="主机不可达，需要分片"
  add chain=icmp protocol=icmp icmp-options=8:0 action=accept \
    comment="允许回显请求"
  add chain=icmp protocol=icmp icmp-options=11:0 action=accept \
    comment="允许超时"
  add chain=icmp protocol=icmp icmp-options=12:0 action=accept \
    comment="允许参数错误"
  add chain=icmp action=drop comment="拒绝所有其他类型"
```

### IPv6 防火墙

#### 保护路由器本身

与 IPv4 设置非常相似，不同之处在于我们必须处理更多 IPv6 正常运行所需的协议。

首先，我们创建一个 `address-list`，允许从该列表中的地址访问设备：

```ros
/ipv6/firewall/address-list/add address=fd12:672e:6f65:8899::/64 list=allowed
```

简要 IPv6 防火墙过滤规则说明：

- 使用 *new* 数据包，接受 *established/related* 数据包。
- 从互联网（公共）接口/接口列表中丢弃 *link-local* 地址。
- 接受来自 *link-local* 地址对路由器的访问，接受 *multicast* 地址用于管理目的，接受您的源 *address-list* 以访问路由器。
- 丢弃所有其他内容。

```ros
/ipv6/firewall/filter
add action=accept chain=input comment="允许已建立和相关连接" connection-state=established,related
add chain=input action=accept protocol=icmpv6 comment="接受 ICMPv6"
add chain=input action=accept protocol=udp port=33434-33534 comment="defconf: 接受 UDP traceroute"
add chain=input action=accept protocol=udp dst-port=546 src-address=fe80::/10 comment="接受 DHCPv6-Client 前缀委派。"
add action=drop chain=input in-interface=in_interface_name log=yes log-prefix=dropLL_from_public src-address=fe80::/10
add action=accept chain=input comment="允许允许的地址" src-address-list=allowed
add action=drop chain=input
/ipv6/firewall/address-list
add address=fe80::/10 list=allowed
add address=xxxx::/48 list=allowed
add address=ff02::/16 comment=组播 list=allowed
```

:::warning
在某些使用 DHCPv6 中继的设置中，数据包的源地址可能不在 link-local 范围内。在这种情况下，必须移除或调整规则 #4 的 src-address 参数，以接受中继地址。
:::

#### 保护局域网设备

这一步比 IPv4 更为重要。在 IPv4 设置中，客户端通常拥有本地地址范围内的地址，并通过 NAT 转换为公共 IP，这样它们就无法从公共网络直接访问。

IPv6 则不同。在大多数常见设置中，启用 IPv6 会使您的客户端可从公共网络访问，因此必须使用适当的防火墙过滤规则来保护您的客户。

简而言之，非常基本的局域网保护应：

- 接受 *established/related* 并使用 *new* 数据包。
- 丢弃 *invalid* 数据包。
- 接受 ICMPv6 数据包。
- 仅接受从您的客户端发起到公共网络的 *new* 连接。
- 丢弃所有其他内容。

```ros
/ipv6/firewall/filter
add action=accept chain=forward comment=established,related connection-state=established,related
add action=drop chain=forward comment=invalid connection-state=invalid log=yes log-prefix=ipv6,invalid
add action=accept chain=forward comment=icmpv6 in-interface=!in_interface_name protocol=icmpv6
add action=accept chain=forward comment="本地网络" in-interface=!in_interface_name src-address-list=allowed
add action=drop chain=forward log-prefix=IPV6
```

## RAW 过滤

防火墙 RAW 表允许在连接跟踪之前有选择地绕过或丢弃数据包，从而显著降低 CPU 负载。该工具对于缓解 DoS/DDoS 攻击非常有用。

RAW 过滤器配置可通过 IPv4 的 `/ip/firewall/raw` 菜单和 IPv6 的 `/ipv6/firewall/raw` 菜单访问。

RAW 表没有依赖于连接跟踪的匹配器（如 connection-state、layer7 等）。
如果数据包被标记为绕过连接跟踪，则不会进行数据包去分片。

此外，RAW 防火墙只能有两个链中的规则：

- **prerouting** - 用于处理进入路由器的任何数据包。
- **output** - 用于处理源自路由器并通过某个接口离开的数据包。经过路由器的数据包不会根据 output 链的规则进行处理。

### 基本 RAW 示例

假设我们有 OSPF 配置，但由于连接跟踪，OSPF 存在邻接问题。我们可以使用 RAW 规则来解决此问题，通过不将 OSPF 数据包发送到连接跟踪。

```ros
/ip/firewall/raw
add chain=prerouting protocol=ospf action=notrack
add chain=output protocol=ospf action=notrack
```

## 了解更多

- [构建高级防火墙](../user-guides/building-advanced-firewall.md)
- [连接速率](../user-guides/connection-rate.md)
- [SSH 暴力破解防护](../user-guides/bruteforce-prevention.md)
- [Syn/DoS 防护](../user-guides/ddos-protection.md)