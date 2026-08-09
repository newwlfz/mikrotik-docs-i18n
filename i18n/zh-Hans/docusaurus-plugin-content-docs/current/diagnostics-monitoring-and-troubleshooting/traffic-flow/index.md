# 流量流

> MikroTik Traffic-Flow 提供网络监控与统计功能，通过收集经过路由器的数据包统计信息，支持 NetFlow 版本 1、5、9 及 IPFIX，以实现灵活的流量分析。它允许配置接口、缓存条目、超时时间、数据包采样以及用于流量数据传输的目标主机。

import DocCardList from '@theme/DocCardList';

# 流量流

MikroTik Traffic-Flow 是一个系统，用于提供经过路由器的数据包的统计信息。除了网络监控和统计外，系统管理员还可以识别网络中可能出现的各种问题。借助 Traffic-Flow，可以分析和优化整体网络性能。由于 Traffic-Flow 与 Cisco NetFlow 兼容，因此可以与各种为 Cisco NetFlow 设计的工具配合使用。

Traffic Flow 只能处理由路由器 CPU 处理的流量，因此硬件卸载的流量将不会出现在 Traffic Flow 流中（例如，硬件卸载的桥接流量）。

Traffic-Flow 支持以下 NetFlow 格式：

- **版本 1** - 这是 NetFlow 使用的原始格式。它提供有关流经路由器的 IP 数据包的基本信息，但缺乏对高级功能的支持，例如不同类型的协议和服务类型（ToS）。
- **版本 5** - 作为版本 1 的增强版，此格式支持附加功能，例如服务类型（ToS）、TCP 标志和自治系统号。除版本 1 的功能外，版本 5 还可以包含 BGP AS 和流序列号信息。目前，RouterOS 不包含 BGP AS 号。
- **版本 9** - 此版本引入了基于模板的导出格式，允许可扩展性并支持以前版本无法处理的新记录类型。它可以根据定义的模板导出数据，并且能够导出 IPv4 和 IPv6 流信息。
- **IPFIX** - 由 IETF 标准化，此协议基于 NetFlow 版本 9。它进一步扩展了功能，允许更可定制和灵活的流记录。IPFIX 支持 NetFlow 未涉及的新技术，例如组播。

## 常规

**子菜单：** `/ip/traffic-flow`

本节列出了 Traffic-Flow 的配置属性。

| 属性 | 描述 |
| :-- | :-- |
| **interfaces** (*string \| all*; 默认值：**all**) | 将使用这些接口的名称来收集流量流的统计数据。要指定多个接口，请用逗号分隔。 |
| **cache-entries** (*128k \| 16k \| 1k \| 256k \| 2k \| ...* ; 默认值：**4k**) | 可以同时存在于路由器内存中的流数量。 |
| **active-flow-timeout** (*time*; 默认值：**30m**) | 流的最大生命周期。 |
| **inactive-flow-timeout** (*time*; 默认值：**15s**) | 如果流处于空闲状态，保持其活跃的时间。如果在此超时时间内连接未看到任何数据包，则流量流将作为新流发送数据包。如果此超时时间过小，可能会产生大量流并使缓冲区溢出。 |
| **packet-sampling** (*no \| yes*; 默认值：**no**) | 启用或禁用数据包采样功能。 |
| **sampling-interval** (*integer*; 默认值：**0**) | 连续采样的数据包数量。 |
| **sampling-space** (*integer*; 默认值：**0**) | 连续忽略的数据包数量。 |

:::warning
信息

数据包采样在 RouterOS **v7** 中可用。
:::

在以下示例中：

```ros
/ip/traffic-flow/set packet-sampling=yes sampling-interval=2222 sampling-space=1111
```

将连续采样 2222 个数据包，然后忽略 1111 个数据包。然后采样周期以这种方式重复。

## 目标

**子菜单：** `/ip/traffic-flow/target`

通过 Traffic-Flow 目标，我们指定那些将从路由器收集 Traffic-Flow 信息的主机。

| 属性 | 描述 |
| :-- | :-- |
| **src-address** *(IP ; 默认值： )* | 发送 Traffic-Flow 统计数据时用作源地址的 IP 地址 |
| **dst-address** (*IP*; 默认值： ) | 从路由器接收 Traffic-Flow 统计数据包的主机的 IP 地址。 |
| **port** *(Port; 默认值：2055)* | 从路由器接收 Traffic-Flow 统计数据包的主机的端口（UDP）。 |
| **v9-template-refresh** (*integer*; 默认值：**20**) | 发送模板到接收主机之前的数据包数量（仅适用于 NetFlow 版本 9 和 IPFIX） |
| **v9-template-timeout** (*time*; 默认值： ) | 如果模板尚未发送，多久后发送。（仅适用于 NetFlow 版本 9 和 IPFIX） |
| **version** (*1 \| 5 \| 9 \| IPFIX*; 默认值： ) | 使用哪种 NetFlow 版本格式 |

## IPFIX

**子菜单：** `/ip/traffic-flow/ipfix`

允许自定义流记录

| 属性 | 描述 |
| :-- | :-- |
| **bytes** | 流中处理的总字节数。 |
| **ip-total-length** | IP 数据包的长度（以字节为单位）。 |
| **src-address** | 流的源 IP 地址。 |
| **dst-address** | 流的目的 IP 地址。 |
| **ipv6-flow-label** | IPv6 头中的标签字段，用于对流进行分类。 |
| **src-address-mask** | 源地址的网络掩码，有助于汇总数据。 |
| **dst-address-mask** | 目的地址的网络掩码。 |
| **is-multicast** | 指示流是否为组播流。 |
| **src-mac-address** | 源 MAC 地址。 |
| **dst-mac-address** | 目的 MAC 地址。 |
| **last-forwarded** | 流中最后一个转发数据包的时间戳。 |
| **src-port** | 源端口号。 |
| **dst-port** | 目的端口号。 |
| **nat-dst-address** | 由 NAT 转换后的目的 IP 地址。 |
| **sys-init-time** | 系统初始化时间，可用于时序分析。 |
| **first-forwarded** | 流中第一个转发数据包的时间戳。 |
| **nat-dst-port** | 由 NAT 转换后的目的端口号。 |
| **tcp-ack-num** | TCP 连接中的确认号。 |
| **gateway** | 流经其路由的网关 IP 地址。 |
| **nat-events** | 与该流的网络地址转换相关的事件。 |
| **tcp-flags** | TCP 头中的标志（例如，SYN、ACK）。 |
| **icmp-code** | 用于错误消息和操作信息的 ICMP 代码。 |
| **nat-src-address** | 由 NAT 转换后的源 IP 地址。 |
| **icmp-type** | ICMP 消息的类型，对于诊断消息很重要。 |
| **nat-src-port** | 由 NAT 转换后的源端口号。 |
| **tcp-seq-num** | TCP 连接中的序列号。 |
| **tcp-window-size** | TCP 连接中的窗口大小，指示接收数据缓冲的规模。 |
| **igmp-type** | 互联网组管理协议操作的类型。 |
| **out-interface** | 流的数据包通过其发送出去的接口。 |
| **in-interface** | 流的数据包通过其接收的接口。 |
| **packets** | 流中处理的数据包数量。 |
| **ip-header-length** | IP 头的长度。 |
| **protocol** | 协议号（例如，TCP、UDP、ICMP）。 |
| **tos** | IP 头中的服务类型字段，指示数据包的优先级和处理方式。 |
| **ttl** | 数据包的生存时间，每经过一个路由器减一，以防止无限循环。 |
| **udp-length** | UDP 负载的长度。 |

## 注意事项

通过查看[数据包流图](../../firewall-and-quality-of-service/packet-flow-in-routeros.md)，您可以看到流量流位于输入、转发和输出链栈的末端。这意味着流量流只会统计到达这些链之一的流量。

例如，您在交换机上设置了一个镜像端口，将镜像端口连接到路由器，并设置流量流来统计镜像数据包。不幸的是，这种设置将无法工作，因为镜像数据包在到达输入链之前就被丢弃了。

如果流量通过其他接口和监控接口，则报告中会出现其他接口。

## 示例

此示例演示如何在路由器上配置 Traffic-Flow

在路由器上启用 Traffic-Flow：

```ros
[admin@MikroTik] /ip/traffic-flow> set enabled=yes
[admin@MikroTik] /ip/traffic-flow> print
                enabled: yes
             interfaces: all
          cache-entries: 4k
    active-flow-timeout: 30m
  inactive-flow-timeout: 15s
[admin@MikroTik] /ip/traffic-flow>
```

指定将接收 Traffic-Flow 数据包的主机的 IP 地址和端口：

```ros
[admin@MikroTik] /ip/traffic-flow/target> add dst-address=192.168.0.2 port=2055 version=9
[admin@MikroTik] /ip/traffic-flow/target> print
Flags: X - disabled 
 #   SRC-ADDRESS       DST-ADDRESS        PORT     VERSION
 0   0.0.0.0           192.168.0.2        2055     9  
[admin@MikroTik] /ip/traffic-flow/target>
```

现在，路由器开始发送带有 Traffic-Flow 信息的数据包。

:::info
要将 ntop-ng 与 MikroTik 结合使用，您需要使用 Nprobe，这是一个付费软件。
:::

### 查看更多

- [NetFlow 基础](https://etutorials.org/Networking/network+management/Part+II+Implementations+on+the+Cisco+Devices/Chapter+7.+NetFlow/Fundamentals+of+NetFlow/)
- [在 MikroTik 上使用 Ntop 的流量流](https://github.com/ntop/ntopng/issues/1575)

## 相关主题

<DocCardList />