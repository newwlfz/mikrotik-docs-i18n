# IPIP

> IPIP（IP-in-IP）是 RouterOS 中的一种隧道协议，用于通过 IP 网络建立安全的点对点连接，支持 IPv4 封装，并可与其它平台实现互操作。它提供诸如 MTU、keepalive 和 DSCP 等基本配置选项，但需注意其缺乏加密机制。

# IPIP

IPIP（IP-in-IP）是一种简单的隧道协议，定义于 RFC 2003 中，它将 IP 数据包封装在另一个 IP 报头内，以在两个端点之间传输流量。在 RouterOS 中，IPIP 可用于在中间 IP 网络之上创建路由器之间的点对点隧道。

IPIP 隧道接口在接口列表中表现为一个虚拟接口，其配置方式与其它逻辑接口类似。该协议受到多种网络平台的支持，包括 RouterOS、Linux 和 Cisco 设备，从而实现了不同厂商设备之间的互操作性。

IPIP 通常用于通过公共或私有 IP 基础设施连接远程网络，而无需直接的二层连接。该协议支持 IPv4 流量的封装，常被用作无需加密的轻量级隧道机制。

IPIP 的典型应用场景包括：通过互联网隧道传输私有网络、在远程站点之间建立路由链路，以及在网络设计中替代源路由。由于 IPIP 不提供加密、认证或流量完整性保护，在需要安全传输时，通常与 IPsec 结合使用。

**子菜单：** `/interface/ipip`

## 属性

| 属性 | 说明 |
| :-- | :-- |
| **clamp-tcp-mss** (*yes \| no*；默认值：**yes**) | 控制是否更改接收到的 TCP SYN 报文的 MSS 大小。启用时，如果当前 MSS 大小超过隧道接口的 MTU（考虑 TCP/IP 开销），路由器将更改接收到的 TCP SYN 报文的 MSS 大小。接收到的封装报文仍包含原始 MSS，仅在解封装后才更改 MSS。 |
| **dont-fragment** (*inherit \| no*；默认值：**no**) | 是否在相关数据包中包含 DF 位：*no* - 按需分片，*inherit* - 使用原始数据包的“不分片”标志。（若未设置“不分片”：inherit - 数据包可能被分片）。 |
| **dscp** (*inherit \| integer [0-63]*；默认值：) | 将 IPIP 报头中的 DSCP 值设置为固定值，或继承来自隧道流量的 DSCP 值。 |
| **ipsec-secret** (*string*；默认值：) *[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 当指定密钥时，路由器会向 remote-address 添加一个使用预共享密钥的动态 IPsec 对等体，并采用默认值的策略（默认情况下，阶段 2 使用 sha1/aes128cbc）。 |
| **local-address** (*IP*；默认值：) | 路由器上用于 IPIP 隧道的 IP 地址。 |
| **mtu** (*integer*；默认值：**1480**) | 三层最大传输单元。 |
| **keepalive** (*integer[/time],integer 0..4294967295*；默认值：**10s,10**) | keepalive 参数设置隧道运行标志保持置位的时间间隔，即使隧道远端已断开。如果配置的时间和重试次数均失败，则移除接口运行标志。参数格式如下：`KeepaliveInterval,KeepaliveRetries`，其中 KeepaliveInterval 为时间间隔，KeepaliveRetries 为重试次数。默认情况下，keepalive 设置为 10 秒和 10 次重试。要禁用，请设置 `/interface/ipip/set ipip1 keepalive=no`。 |
| **name** (*string*；默认值：) | 接口名称。 |
| **remote-address** (*IP*；默认值：) | IPIP 隧道远端的 IP 地址。 |

:::warning
此接口没有认证或“状态”机制。接口的带宽使用情况可通过接口菜单中的监控功能进行查看。
:::

## 示例

假设我们想在路由器 R1 和 R2 之间添加一条 IPIP 隧道：

![](https://manual.mikrotik.com/docs/virtual-private-networks/img/ipip-01.webp)

首先，我们需要配置 IPIP 接口，然后为其添加 IP 地址。

路由器 **R1** 的配置如下：

```ros
[admin@MikroTik] /interface/ipip> add
local-address: 10.0.0.1
remote-address: 22.63.11.6
[admin@MikroTik] /interface/ipip> print
Flags: X - disabled, R - running
# NAME MTU LOCAL-ADDRESS REMOTE-ADDRESS
0 X ipip1 1480 10.0.0.1 22.63.11.6

[admin@MikroTik] /interface/ipip> en 0
[admin@MikroTik] /interface/ipip> /ip/address/add address=1.1.1.1/24 interface=ipip1
```

路由器 **R2** 的配置如下所示：

```ros
[admin@MikroTik] /interface/ipip> add local-address=22.63.11.6 remote-address=10.
0.0.1
[admin@MikroTik] /interface/ipip> print
Flags: X - disabled, R - running
# NAME MTU LOCAL-ADDRESS REMOTE-ADDRESS
0 X ipip1 1480 22.63.11.6 10.0.0.1

[admin@MikroTik] /interface/ipip> enable 0
[admin@MikroTik] /interface/ipip> /ip/address/add address=1.1.1.2/24 interface=ipip1
```

现在两台路由器可以互相 ping 通：

```ros
[admin@MikroTik] /interface/ipip> /ping 1.1.1.2
1.1.1.2 64 byte ping: ttl=64 time=24 ms
1.1.1.2 64 byte ping: ttl=64 time=19 ms
1.1.1.2 64 byte ping: ttl=64 time=20 ms
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 19/21.0/24 ms
[admin@MikroTik] /interface/ipip>
```