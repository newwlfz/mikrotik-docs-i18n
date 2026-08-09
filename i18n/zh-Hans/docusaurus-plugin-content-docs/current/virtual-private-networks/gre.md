# GRE

> 通用路由封装（GRE）是一种隧道协议，用于在IP网络上封装各种网络协议，在RouterOS中作为虚拟接口实现，并支持可选的keepalive机制以及MTU、MSS钳制和DSCP设置等属性，以确保可靠的流量转发。

# GRE

通用路由封装（GRE）是一种最初由Cisco开发的隧道协议，用于在IP网络上封装多种网络层协议。它在隧道端点之间创建虚拟点对点链路，允许不同协议的流量穿越路由基础设施。

GRE作为无状态隧道运行，其行为类似于IPIP和EoIP。由于端点之间不维护会话状态，即使远程端点不可达，流量也可能继续向其转发，这可能导致流量黑洞，直到路由重新收敛或隧道状态发生变化。

在RouterOS中，GRE接口作为虚拟接口实现，可根据所需拓扑用于路由或桥接网络设计中。

为改进故障检测，RouterOS为GRE隧道提供了可选的keepalive机制。Keepalive监控远程端点的可达性，当对端停止响应时，可自动禁用隧道接口，从而降低流量被发送到不活动隧道中的风险。

:::tip
GRE隧道增加24字节开销（4字节GRE头 + 20字节IP头）。GRE隧道仅能转发IP和IPv6数据包（以太网类型800和86dd）。当GRE隧道用作路由网关时，请勿使用“Check gateway”选项中的“arp”。
:::
**子菜单：** `/interface/gre`

## 属性

| 属性 | 描述 |
| :-- | :-- |
| **allow-fast-path** (*yes \| no*; 默认：**yes**) | 是否允许FastPath处理。若使用IPsec隧道，则必须禁用。 |
| **clamp-tcp-mss** (*yes \| no*; 默认：**yes**) | 控制是否修改接收到的TCP SYN报文中的MSS大小。启用时，若当前MSS大小超过隧道接口MTU（考虑TCP/IP开销），路由器将修改接收到的TCP SYN报文中的MSS大小。接收到的封装报文仍包含原始MSS，仅在解封装后才修改MSS。 |
| **comment** (*string*; 默认：) | 隧道的简短描述。 |
| **disabled** (*yes \| no*; 默认：**no**) | 启用/禁用隧道。 |
| **dont-fragment** (*inherit \| no*; 默认：**no**) | 是否在相关数据包中包含DF位：*no* - 需要时进行分片，*inherit* - 使用原始数据包的“不分片”标志。（若未设置“不分片”：inherit - 数据包可能被分片）。 |
| **dscp** (*inherit \| integer [0-63]*; 默认：) | 将GRE头中的dscp值设置为固定值，或从隧道流量中继承dscp值。 |
| **ipsec-secret** (*string*; 默认：) *[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 指定密钥后，路由器会向remote-address添加动态IPsec对端，使用预共享密钥和策略（默认phase2使用sha1/aes128cbc）。 |
| **keepalive** (*integer[/time],integer 0..4294967295*; 默认：**10s,10**) | 隧道keepalive参数设置隧道运行标志在远程端断开后仍保持的时间间隔。若配置的时间和重试次数均失败，则移除接口运行标志。参数格式为：`KeepaliveInterval,KeepaliveRetries`，其中KeepaliveInterval为时间间隔，KeepaliveRetries为重试次数。默认keepalive设置为10秒和10次重试。 |
| **l2mtu** (*integer [0..65536]*; 默认：**65535**) | 二层最大传输单元。 |
| **local-address** (*IP*; 默认：**0.0.0.0**) | 用于本地隧道端的IP地址。若设置为0.0.0.0，则使用出接口的IP地址。 |
| **mtu** (*integer [0..65536]*; 默认：**1476**) | 三层最大传输单元。 |
| **name** (*string*; 默认：) | 隧道名称。 |
| **remote-address** (*IP*; 默认：) | 远程隧道端的IP地址。 |

## 配置示例

本示例的目标是通过互联网在两个远程站点之间建立三层连接。

![](https://manual.mikrotik.com/docs/virtual-private-networks/img/gre-01.webp)

我们有两个站点，**Site1**本地网络范围为10.1.101.0/24，**Site2**本地网络范围为10.1.202.0/24。

第一步是创建GRE隧道。站点1上的路由器：

```ros
/interface/gre/add name=myGre remote-address=192.168.90.1 local-address=192.168.80.1
```

站点2上的路由器：

```ros
/interface/gre/add name=myGre remote-address=192.168.80.1 local-address=192.168.90.1
```

如您所见，隧道配置非常简单。

:::warning
在此示例中未配置keepalive，因此即使远程隧道端不可达，隧道接口仍将具有**运行**标志。
:::

现在只需设置隧道地址和相应的路由。站点1上的路由器：

```ros
/ip/address/add address=172.16.1.1/30 interface=myGre
/ip/route/add dst-address=10.1.202.0/24 gateway=172.16.1.2
```

站点2上的路由器：

```ros
/ip/address/add address=172.16.1.2/30 interface=myGre
/ip/route/add dst-address=10.1.101.0/24 gateway=172.16.1.1
```

此时，两个站点已通过GRE隧道建立三层连接。