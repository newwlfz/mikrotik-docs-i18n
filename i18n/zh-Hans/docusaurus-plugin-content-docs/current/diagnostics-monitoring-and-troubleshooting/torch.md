# Torch

> MikroTik Torch 是一款实时流量监控工具，用于观察通过接口的网络流量，支持分析源/目的地址、端口、协议、MAC、VLAN ID 和 DSCP 值，便于故障排查。

# Torch

MikroTik Torch 是一款实时流量监控工具，用于观察通过特定接口的流量。它是实时排查网络负载和进行故障分析的重要实用工具。

观看我们的[关于此功能的视频](https://youtu.be/45E2uwI3xhc)。

:::warning
Torch 捕获的流量是在防火墙过滤之前可见的。这意味着您会看到可能最终被防火墙规则丢弃的数据包。
:::

```ros
/tool/torch interface=ether1 src-address=0.0.0.0/0 dst-address=0.0.0.0/0
```

您可以按以下分类监控流量：

- 源地址和目的地址（IPv4 和 IPv6）。
- 端口和协议。
- MAC 协议和 MAC 地址。
- VLAN ID。
- DSCP。

### 使用示例

要监控 `ether1` 上来自特定子网的 HTTP 和 HTTPS 流量（接口可作为未命名参数）：

```ros
/tool/torch ether1 port=80,443 src-address=192.168.88.0/24
```

Torch 会显示所选协议以及所选接口上每个条目的 TX/RX 数据速率。

:::warning
在启用了客户端间转发功能的无线客户端之间传输的单播流量，Torch 工具将无法看到。同样，通过桥接硬件卸载处理的数据包也不可见（但未知单播、广播以及部分组播流量仍将保持可见）。
:::