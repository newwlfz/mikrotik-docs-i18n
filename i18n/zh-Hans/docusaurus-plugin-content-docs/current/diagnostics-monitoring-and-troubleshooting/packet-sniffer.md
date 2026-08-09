# 数据包嗅探器

> Packet Sniffer 是 MikroTik RouterOS 中的一个工具，用于捕获和分析网络数据包，以诊断问题或检测安全威胁。它支持按 IP、MAC、端口、协议等进行过滤，并可将数据包保存为 PCAPNG 格式或流式传输到 PC 进行分析。

# 数据包嗅探器

数据包嗅探器是一种能够捕获和分析进入、离开或经过路由器的数据包的工具。在诊断网络问题或防范网络安全攻击时，数据包嗅探功能非常有用。

:::warning
启用客户端间转发（client-to-client forwarding）的 Wireless 客户端之间的单播流量对嗅探工具不可见。

**警告：** 在 Bridge 上启用了硬件卸载（hardware offloading）处理的数据包将不可见（泛洪数据包，如未知单播、广播和多播流量可能可见）。

**提示：** 嗅探器在数据包进入防火墙之前（direction=rx）或离开防火墙之后（direction=tx）捕获数据包。
:::

## 数据包嗅探器配置

RouterOS 内置嗅探器允许您根据各种协议捕获数据包。

在以下示例中，我们将配置嗅探器以匹配通过 ether1 接口的数据包：

```ros
[admin@MikroTik] > /tool/sniffer/start interface=ether1           
[admin@MikroTik] > /tool/sniffer/stop                             
[admin@MikroTik] > /tool/sniffer/save file-name=/flash/test.pcap            
MikroTik] > /file/print where name~"test" 
Columns: NAME, TYPE, SIZE, CREATION-TIME
#  NAME        TYPE  SIZE  CREATION-TIME       
9  flash/test.pcap  file  3696  2019-12-04 10:48:16
```

您可以从文件部分下载捕获的数据包。然后，您可以使用诸如 [Wireshark](https://www.wireshark.org/) 之类的数据包分析器来分析文件：

![](https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/img/packet-sniffer-01.webp)

如果您使用数据包流式传输到 PC 并使用 Wireshark，为确保只查看流式传输的数据，您需要应用一个匹配嗅探器所用端口的过滤器；默认使用 37008 端口。此外，我们建议使用 `filter-stream=yes`。

![](https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/img/packet-sniffer-timestamp.png)

:::warning
请注意，嗅探到的数据包仅在 10 分钟内可用。如果您需要永久保存，请设置 "file-name" 直接保存，或按前述说明发出 "save" 命令。

**重要提示：** 从 RouterOS 7.20 开始，嗅探工具以 PCAPNG 格式保存捕获的数据包。[traffic-generator inject-pcap](./traffic-generator.md) 功能从 RouterOS 7.21 开始支持 PCAPNG 格式。
:::

**子菜单：** `/tool/sniffer`

| 属性 | 描述 |
| :-- | :-- |
| **file-limit** (*整数 10..4294967295[KiB]*; 默认值：**1000KiB**) | 文件大小限制。达到限制时嗅探器将停止。 |
| **file-name** (*字符串*; 默认值：) | 保存嗅探数据包的文件名。 |
| **filter-cpu** (*整数*; 默认值：) | 用作过滤器的 CPU 核心。 |
| **filter-ip-address** (*ip/mask[,ip/mask]（最多 16 项）*; 默认值：) | 最多 16 个用作过滤器的 IP 地址。 |
| **filter-dst-ip-address** (*ip/mask[,ip/mask]（最多 16 项）*; 默认值：) | 最多 16 个用作过滤器的 IP 目的地址。 |
| **filter-src-ip-address** (*ip/mask[,ip/mask]（最多 16 项）*; 默认值：) | 最多 16 个用作过滤器的 IP 源地址。 |
| **filter-ipv6-address** (*ipv6/mask[,ipv6/mask]（最多 16 项）*; 默认值：) | 最多 16 个用作过滤器的 IPv6 地址。 |
| **filter-dst-ipv6-address** (*ipv6/mask[,ipv6/mask]（最多 16 项）*; 默认值：) | 最多 16 个用作过滤器的 IPv6 目的地址。 |
| **filter-src-ipv6-address** (*ipv6/mask[,ipv6/mask]（最多 16 项）*; 默认值：) | 最多 16 个用作过滤器的 IPv6 源地址。 |
| **filter-mac-address** (*mac/mask[,mac/mask]（最多 16 项）*; 默认值：) | 最多 16 个用作过滤器的 MAC 地址和 MAC 地址掩码。 |
| **filter-dst-mac-address** (*mac/mask[,mac/mask]（最多 16 项）*; 默认值：) | 最多 16 个用作过滤器的 MAC 目的地址和 MAC 地址掩码。 |
| **filter-src-mac-address** (*mac/mask[,mac/mask]（最多 16 项）*; 默认值：) | 最多 16 个用作过滤器的 MAC 源地址和 MAC 地址掩码。 |
| **filter-port** (*[!]port[,port]（最多 16 项）*; 默认值：) | 最多 16 个用作过滤器的逗号分隔端口。也可使用预定义端口名称列表，如 ssh 和 telnet。 |
| **filter-dst-port** (*[!]port[,port]（最多 16 项）*; 默认值：) | 最多 16 个用作过滤器的逗号分隔目的端口。也可使用预定义端口名称列表，如 ssh 和 telnet。 |
| **filter-src-port** (*[!]port[,port]（最多 16 项）*; 默认值：) | 最多 16 个用作过滤器的逗号分隔源端口。也可使用预定义端口名称列表，如 ssh 和 telnet。 |
| **filter-ip-protocol** (*[!]protocol[,protocol]（最多 16 项）*; 默认值：) | 最多 16 个用作过滤器的逗号分隔 IP/IPv6 协议。IP 协议（可使用协议编号代替协议名称）：ipsec-ah - IPsec AH 协议ipsec-esp - IPsec ESP 协议ddp - 数据报交付协议egp - 外部网关协议ggp - 网关-网关协议gre - 通用路由封装hmp - 主机监控协议idpr-cmtp - IDPR 控制消息传输icmp - 互联网控制消息协议icmpv6 - 互联网控制消息协议 v6igmp - 互联网组管理协议ipencap - IP 封装于 IP 中ipip - IP 封装encap - IP 封装iso-tp4 - ISO 传输协议类 4ospf - 开放最短路径优先pup - PARC 通用数据包协议pim - 协议无关组播rspf - 无线最短路径优先rdp - 可靠数据报协议st - ST 数据报模式tcp - 传输控制协议udp - 用户数据报协议vmtp - 通用消息传输协议vrrp - 虚拟路由器冗余协议xns-idp - Xerox XNS IDPxtp - Xpress 传输协议 |
| **filter-mac-protocol**(*[!]protocol[,protocol]（最多 16 项）*; 默认值：) | 最多 16 个用作过滤器的逗号分隔条目。MAC 协议（可使用协议编号代替协议名称）：802.2 - 802.2 帧 (0x0004)arp - 地址解析协议 (0x0806)capsman - CAPsMAN 到 CAP MAC 层连接 (0x88BB)dot1x - EAPoL IEEE 802.1X (0x888E)homeplug-av - HomePlug AV MME (0x88E1)ip - 互联网协议版本 4 (0x0800)ipv6 - 互联网协议版本 6 (0x86DD)ipx - 互联网分组交换 (0x8137)lacp - 链路聚合控制协议 (0x8809)lldp - 链路层发现协议 (0x88CC)loop-protect - 环路保护协议 (0x9003)macsec - MAC 安全 IEEE 802.1AE (0x88E5)mpls-multicast - MPLS 组播 (0x8848)mpls-unicast - MPLS 单播 (0x8847)mvrp - 多 VLAN 注册协议 (0x88F5)packing-compr - 带压缩 IP 打包的封装数据包 (0x9001)packing-simple - 带简单 IP 打包的封装数据包 (0x9000)pppoe - PPPoE 会话阶段 (0x8864)pppoe-discovery - PPPoE 发现阶段 (0x8863)rarp - 反向地址解析协议 (0x8035)romon - 路由器管理覆盖网络 RoMON (0x88BF)service-vlan - 运营商桥接 (IEEE 802.1ad) 和最短路径桥接 IEEE 802.1aq (0x88A8)vlan - VLAN 标记帧 (IEEE 802.1Q) 和带 NNI 兼容性的最短路径桥接 IEEE 802.1aq (0x8100) |
| **filter-stream** (*yes \| no*; 默认值：**yes**) | 忽略发往嗅探服务器的嗅探数据包。 |
| **filter-size** (*integer[-integer]:0..65535*; 默认值：) | 按指定大小或大小范围（字节）过滤数据包。 |
| **filter-direction**(*any \| rx \| tx*; 默认值：) | 指定过滤应用的方向。 |
| **filter-interface** (*all \| name*; 默认值：**all**) | 嗅探器运行的接口名称。**all** 表示嗅探器将在所有接口上嗅探数据包。 |
| **filter-operator-between-entries** (*and \| or*; 默认值：**or**) | 更改具有多个条目的过滤器的逻辑。 |
| **filter-vlan** (*integer[,integer]:0..4095*; 默认值：) | 最多 16 个用作过滤器的 VLAN ID。 |
| **memory-limit**(*整数 10..4294967295[KiB]*; 默认值：**100KiB**) | 用于存储嗅探数据的内存量。 |
| **memory-scroll** (*yes \| no*; 默认值：**yes**) | 当达到内存限制时是否覆盖旧的嗅探数据。 |
| **only-headers**(*yes \| no*; 默认值：**no**) | 仅将数据包头保存到内存中，而非整个数据包。 |
| **show-frame (*yes \| no*; 默认值：no)** | 在命令行中运行快速嗅探时是否查看帧内容。 |
| **streaming-enabled** (*yes \| no*; 默认值：**no**) | 定义是否将嗅探数据包发送到流服务器。 |
| **streaming-server** (*IP*; 默认值：**0.0.0.0**) | Tazmen 嗅探协议 (TZSP) 流接收器。 |
| **streaming-port** (*port*; 默认值：**37008** ) | 将 TZSP 数据包流式传输到的端口。 |

:::danger
`file-size` 限制不应配置为超过可用空闲内存！
:::

### 数据包嗅探器快速模式

快速模式将使用有限大小的数据包缓冲区显示过滤出的结果。可以设置多个过滤属性。如果未设置任何属性，将使用当前配置。

```ros
[admin@MikroTik] > /tool/sniffer/quick ip-protocol=icmp
Columns: INTERFace, TIME, NUm, DIr, SRC-MAC, DST-MAC, SRC-ADDRESS, DST-ADDRESS, PROTOCOl, SIze, Cpu, FP
INTERF  TIME    NU  DI  SRC-MAC            DST-MAC            SRC-ADDRESS     DST-ADDRESS     PROTOCO  SI  C  FP
ether7  35.472  79  <-  6C:3B:6B:ED:83:69  6C:3B:6B:ED:81:83  10.155.126.252  10.155.126.253  ip:icmp  70  7  no
ether7  35.472  80  ->  6C:3B:6B:ED:81:83  6C:3B:6B:ED:83:69  10.155.126.253  10.155.126.252  ip:icmp  70  7  no
ether1  35.595  81  <-  6C:3B:6B:ED:83:63  6C:3B:6B:ED:81:7D  172.24.24.2     172.24.24.1     ip:icmp  70  4  no
ether1  35.595  82  ->  6C:3B:6B:ED:81:7D  6C:3B:6B:ED:83:63  172.24.24.1     172.24.24.2     ip:icmp  70  4  no
ether7  36.457  83  <-  6C:3B:6B:ED:83:69  6C:3B:6B:ED:81:83  10.155.126.252  10.155.126.253  ip:icmp  70  7  no
ether7  36.457  84  ->  6C:3B:6B:ED:81:83  6C:3B:6B:ED:83:69  10.155.126.253  10.155.126.252  ip:icmp  70  7  no
ether1  36.6    85  <-  6C:3B:6B:ED:83:63  6C:3B:6B:ED:81:7D  172.24.24.2     172.24.24.1     ip:icmp  70  4  no
ether1  36.6    86  ->  6C:3B:6B:ED:81:7D  6C:3B:6B:ED:83:63  172.24.24.1     172.24.24.2     ip:icmp  70  4  no
```

:::warning
除非设置了 *fast-path* 参数，否则在同一接口上使用数据包嗅探器将无法看到流量生成器（Traffic-Generator）的数据包。
:::

### 数据包嗅探器协议

在此子菜单中，您可以查看所有嗅探到的协议及其在总嗅探量中所占的份额。

```ros
[admin@MikroTik] /tool/sniffer/protocol> print 
 # PROTOCOL IP-PROTOCOL PORT                                     PACKETS      BYTES        SHARE
 0 802.2                                                              1         60        0.05%
 1 ip                                                               215     100377       99.04%
 2 arp                                                                2        120        0.11%
 3 ipv6                                                               6        788        0.77%
 4 ip       tcp                                                     210      99981       98.65%
 5 ip       udp                                                       3        228        0.22%
 6 ip       ospf                                                      2        168        0.16%
 7 ip       tcp         8291 (winbox)                               210      99981       98.65%
 8 ip       tcp         36771                                       210      99981       98.65%
 9 ip       udp         646                                           3        228        0.22%
```

### 数据包嗅探器主机

该子菜单显示参与您所嗅探数据交换的主机列表。

```ros
[admin@MikroTik] /tool/sniffer/host> print 
 # ADDRESS         RATE                PEEK-RATE           TOTAL            
 0 10.5.101.3      0bps/0bps           0bps/720bps         0/90             
 1 10.5.101.10     0bps/0bps           175.0kbps/19.7kbps  61231/7011       
 2 10.5.101.13     0bps/0bps           0bps/608bps         0/76             
 3 10.5.101.14     0bps/0bps           0bps/976bps         0/212            
 4 10.5.101.15     0bps/0bps           19.7kbps/175.0kbps  7011/61231       
 5 224.0.0.2       0bps/0bps           608bps/0bps         76/0             
 6 224.0.0.5       0bps/0bps           1440bps/0bps        302/0 
```

### 数据包嗅探器连接

在此您可以获取在嗅探期间监视的连接列表。

```ros
[admin@MikroTik] /tool/sniffer/connection> print
Flags: A - active
  #   SRC-ADDRESS       DST-ADDRESS             BYTES     RESENDS   MSS
  0 A 10.0.0.241:1839   10.0.0.181:23 (telnet)  6/42      60/0      0/0
  1 A 10.0.0.144:2265   10.0.0.181:22 (ssh)     504/252   504/0     0/0
```