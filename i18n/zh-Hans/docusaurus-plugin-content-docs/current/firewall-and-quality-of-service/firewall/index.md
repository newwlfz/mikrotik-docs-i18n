# 防火墙

> MikroTik RouterOS 防火墙提供有状态与无状态的数据包过滤、NAT 以及高级流量分类功能，以保障网络数据流安全并防止未经授权的访问。它包含 filter/raw、mangle 和 nat 模块，并预定义了链，便于高效管理规则。

# 防火墙

![防火墙基础](img/firewall-01.webp)

防火墙通过利用连接跟踪实现有状态（stateful）和无状态（stateless）的数据包过滤，从而提供安全功能，用于管理进出及通过路由器的数据流。结合网络地址转换（NAT），它既可作为防止未经授权访问直接连接的网络及路由器本身的工具，也可作为出站流量的过滤器。

网络防火墙将外部威胁阻挡在网络内部敏感数据之外。每当不同网络相互连接时，总存在外部人员侵入您局域网的风险。此类入侵可能导致私有数据被窃取和传播、有价值的数据被篡改或破坏，甚至整个硬盘被擦除。防火墙用于预防或最小化连接其他网络所固有的安全风险。正确配置的防火墙在高效且安全的网络基础设施部署中扮演着关键角色。

MikroTik RouterOS 拥有非常强大的防火墙实现，功能包括：

- 无状态数据包检查。
- 有状态数据包检查。
- 第七层协议检测。
- 点对点协议过滤。
- 流量分类依据：
  - 源 MAC 地址。
  - IP 地址（网络或列表）及地址类型（广播、本地、组播、单播）。
  - 端口或端口范围。
  - IP 协议。
  - 协议选项（ICMP 类型和代码字段、TCP 标志、IP 选项和 MSS）。
  - 数据包到达或离开的接口。
  - 内部流和连接标记。
  - DSCP 字节。
  - 数据包内容。
  - 数据包到达速率及序列号。
  - 数据包大小。
  - 数据包到达时间。

以及更多功能！

防火墙分为三个主要模块：

- **filter/raw** - 用于根据配置的策略拒绝流量。如果不需要连接跟踪，在 RAW 表中进行过滤可以节省资源。
- **mangle** - 用于标记特定连接、数据包、流，设置优先级以及执行其他任务。
- **nat** - 用于设置地址转换规则、重定向和端口转发。

## 链

防火墙过滤规则分组在链中。这允许数据包在一个链中根据一个共同标准进行匹配，然后传递到另一个链，根据其他共同标准进行处理。

例如，数据包应根据 IP 地址:端口对进行匹配。当然，可以通过向 forward 链添加尽可能多的包含 IP 地址:端口匹配的规则来实现，但更好的方式是添加一条匹配来自特定 IP 地址流量的规则。然后，可以在“**mychain**”链中添加针对各个端口进行匹配的规则，而无需指定 IP 地址。

```ros
/ip/firewall/filter 
add chain=mychain protocol=tcp dst-port=22 action=accept
add chain=mychain protocol=tcp dst-port=23 action=accept

add action=jump chain=input src-address=1.1.1.2/32 jump-target="mychain"
```

处理链时，规则按其在链中列出的顺序（从上到下）依次执行。如果数据包匹配规则的条件，则对其执行指定的动作，并且该链中不再处理更多规则（例外情况是 **passthrough** 动作和某些 [Mangle](./mangle.md) 动作）。

如果数据包未匹配链中的任何规则，则接受该数据包。

每个防火墙模块都有其预定义的链：

- **raw**：
  - prerouting
  - output
- **filter**：
  - input
  - forward
  - output
- **mangle**：
  - prerouting
  - input
  - forward
  - output
  - postrouting
- **nat**：
  - srcnat
  - dstnat
  - input
  - output

RouterOS 中更详细的数据包处理过程在 [RouterOS 中的数据包流](../packet-flow-in-routeros.md) 图中描述。