# 连接跟踪（Connection Tracking）

> MikroTik RouterOS 中的连接跟踪通过监控逻辑网络连接来实现有状态防火墙功能，支持 NAT 及多种防火墙特性。它将数据包分配到诸如 new、established、related、invalid 或 untracked 等状态，并通过 FastTrack 优化 TCP/UDP 数据包转发。

# 连接跟踪

连接跟踪允许内核跟踪所有逻辑网络连接或会话，从而关联构成该连接的所有数据包。

NAT 依赖此信息以相同方式转换所有相关数据包。

借助连接跟踪，即使对于 UDP 等无状态协议，您也可以使用有状态防火墙功能。

### 受连接跟踪影响的防火墙功能

- NAT
- 防火墙：
  - connection-bytes
  - connection-mark
  - connection-type
  - connection-state
  - connection-limit
  - connection-rate
  - layer7-protocol
  - new-connection-mark
  - tarpit

已跟踪连接的列表可在 IPv4 的 `/ip/firewall/connection` 和 IPv6 的 `/ipv6/firewall/connection` 中查看。

```text
      [admin@3C22-atombumba] /ip/firewall/connection> print
      Flags: S - seen-reply, A - assured
      #    PR.. SRC-ADDRESS           DST-ADDRESS           TCP-STATE   TIMEOUT
      0    udp  10.5.8.176:5678       255.255.255.255:5678              0s
      1    udp  10.5.101.3:646        224.0.0.2:646                     5s
      2    ospf 10.5.101.161          224.0.0.5                         9m58s
      3    udp  10.5.8.140:5678       255.255.255.255:5678              8s
      4 SA tcp  10.5.101.147:48984    10.5.101.1:8291       established 4m59s

```

```text
      [admin@3C22-atombumba] /ipv6/firewall/connection> print
      Flags: S - seen reply, A - assured
      #    PRO.. SRC-ADDRESS                 DST-ADDRESS                 TCP-STATE
      0    udp   fe80::d6ca:6dff:fe77:3698   ff02::1
      1    udp   fe80::d6ca:6dff:fe98:7c28   ff02::1
      2    ospf  fe80::d6ca:6dff:fe73:9822   ff02::5

```

## 连接状态

根据连接表条目，到达的数据包可以被分配为以下连接状态之一：**new、invalid、established、related** 或 **untracked**。

数据包被视为 **new** 有两种不同的情况。第一种情况是针对无状态连接（如 UDP），即连接表中没有对应的连接条目。另一种情况是针对有状态协议（TCP）。在这种情况下，启动新连接的新数据包始终是带有 *SYN* 标志的 TCP 数据包。

如果数据包不是 new，则它可能属于 ***established*** 或 ***related*** 连接，或者不属于任何连接，从而使其成为 ***invalid***。具有 ***established*** 状态的数据包，正如大多数人已经猜到的那样，属于连接跟踪表中已存在的连接。***related*** 状态非常相似，不同之处在于该数据包属于与某个现有连接相关的连接，例如，ICMP 错误数据包或 FTP 数据连接数据包。

连接状态 **untracked** 是一种特殊情况，当使用 **RAW** 防火墙规则将连接从连接跟踪中排除时使用。此规则将使所有转发的流量绕过连接跟踪，从而提高数据包通过设备的处理速度。

任何其他数据包都被视为 ***invalid***，在大多数情况下应被丢弃。

基于此信息，我们可以设置一组基本的过滤规则，通过接受 *established/related* 数据包、丢弃 *invalid* 数据包，并且仅对 *new* 数据包进行更详细的过滤，来加速数据包过滤并减少 CPU 负载。

```ros
/ip/firewall/filter
add chain=input connection-state=invalid action=drop comment="丢弃无效连接"
add chain=input connection-state=established,related,untracked action=accept comment="允许已建立/相关/未跟踪连接"
```

:::danger
此类规则集不得应用于非对称路由的路由器，因为非对称路由的数据包可能被视为无效而被丢弃。
:::

## FastTrack

IPv4 FastTrack 是一种特殊的处理器，它绕过 Linux 机制，允许更快的数据包转发。该处理器用于标记了 `fasttrack-connection` 操作的 **TCP** 和 **UDP** 连接。IPv4 FastTrack 处理器支持 NAT（SNAT、DNAT 或两者）。

请注意，并非连接的所有数据包都能被 FastTrack 处理，因此即使连接被标记为 FastTrack，您也可能会看到一些数据包走慢速路径。这就是为什么 **fasttrack-connection** 通常后面会跟一条相同的 `action=accept` 规则。

FastTrack 处理的数据包会绕过：

- 防火墙。
- 连接跟踪。
- 简单队列（Simple queues）。
- 父级为 *global* 的队列树（Queue tree）。
- IP 记账（IP accounting）。
- IPSec。
- Hotspot 通用客户端。
- VRF 分配。

由管理员负责确保 FastTrack 不会干扰其他配置。

### 要求

如果满足以下条件，则 IPv4 FastTrack 处于活动状态：

- 没有 mesh、metarouter 接口配置。
- Sniffer、torch 或流量生成器未运行。
- *`/tool/mac-scan`* 未被主动使用。
- *`/tool/ip-scan`* 未被主动使用。
- 在 *IP/Settings* 下启用了 FastPath 和 Route cache。

### 示例

例如，对于具有出厂默认配置的 SOHO 路由器，您可以使用放置在防火墙过滤器顶部的一条规则来 FastTrack 所有 LAN 流量。需要相同的配置接受规则：

```ros
/ip/firewall/filter/add chain=forward action=fasttrack-connection connection-state=established,related
/ip/firewall/filter/add chain=forward action=accept connection-state=established,related
```

:::tip

- 连接在关闭、超时或路由器重启之前一直保持 FastTrack 状态。
- 只有在 FastTrack 防火墙规则被删除/禁用并且路由器重启后，Dummy 规则才会消失。
- 当设备上同时启用 FastPath 和 FastTrack 时，同一时间只能有一个处于活动状态。

**警告：** 队列（除非是父级为接口的队列树）、防火墙过滤器和 mangle 规则将不会应用于 FastTrack 处理的流量。
:::

## 连接跟踪设置

连接跟踪设置通过 `/ip/firewall/connection/tracking` 菜单进行管理。

#### 属性

| 属性 | 描述 |
| :-- | :-- |
| **enabled** (*yes \| no \| auto*; 默认值：**auto**) | 允许禁用或启用连接跟踪。禁用连接跟踪后，上述防火墙功能将停止工作。如果设置为 "auto"，则在添加至少一条防火墙规则之前，连接跟踪处于禁用状态。 |
| **liberal-tcp-tracking** (*yes \| no*; 默认值：**no**) | 通过切换内核参数 `nf_conntrack_tcp_be_liberal` 来启用或禁用宽松的 TCP 连接跟踪。当设置为 **yes** 时，系统仅将窗口外的 RST 段标记为 INVALID。**注意：** 启用此设置可能允许原本会被防火墙的 `connection-state` 匹配器视为 `invalid` 的畸形数据包通过。这可能会增加对某些规避技术的暴露。仅在排查问题或处理已知问题时才应启用此属性。 |
| **loose-tcp-tracking** (*yes \| no*; 默认值：**yes**) | 当 loose-tcp-tracking=yes 时，握手过程中未看到第一个初始 SYN 的第 2 部分（SYN,ACK）和第 3 部分（ACK）将被视为 ESTABLISHED。当 loose-tcp-tracking=no 时，未看到第一个初始 SYN 的第 2 部分（SYN,ACK）和第 3 部分（ACK）将被视为 INVALID。 |
| **tcp-syn-sent-timeout** (*time*; 默认值：**5s**) | TCP SYN 超时时间。 |
| **tcp-syn-received-timeout** (*time*; 默认值：**5s**) | TCP SYN 超时时间。 |
| **tcp-established-timeout** (*time*; 默认值：**1d**) | 已建立的 TCP 连接超时的时间。 |
| **tcp-fin-wait-timeout** (*time*; 默认值：**10s**) |  |
| **tcp-close-wait-timeout** (*time*; 默认值：**10s**) |  |
| **tcp-last-ack-timeout** (*time*; 默认值：**10s**) |  |
| **tcp-time-wait-timeout** (*time*; 默认值：**10s**) |  |
| **tcp-close-timeout** (*time*; 默认值：**10s**) |  |
| **udp-timeout** (*time*; 默认值：**30s**) | 指定仅在一个方向上看到数据包的 UDP 连接的超时时间。 |
| **udp-stream-timeout** (*time*; 默认值：**3m**) | 指定在两个方向上看到数据包的 UDP 连接的超时时间。 |
| **icmp-timeout** (*time*; 默认值：**10s**) | ICMP 连接超时时间。 |
| **generic-timeout** (*time*; 默认值：**10m**) | 所有其他连接条目的超时时间。 |
| tcp-max-retrans-timeout  | |
| tcp-unacked-timeout  | |

**只读属性**

| 属性 | 描述 |
| :-- | :-- |
| **max-entries** (*integer*) | 连接跟踪表可以容纳的最大条目数。此值取决于安装的 RAM 数量。请注意，系统启动时不会创建最大尺寸的连接跟踪表；如果情况需要且系统仍有空闲 RAM，它可能会增加，但大小不会超过 1048576。 |
| **total-entries** (*integer*) | 连接表当前持有的连接数。 |
| active-ipv4  | |
| active-ipv6  | |
| total-ip4-entries  | |
| total-ip6-entries  | |

## 连接列表

已跟踪连接的列表可在 IPv4 的 `/ip/firewall/connection` 和 IPv6 的 `/ipv6/firewall/connection` 中查看。

### 属性

连接列表中的所有属性均为只读。

| 属性 | 描述 |
| :-- | :-- |
| **assured** (*yes \| no*) | 指示此连接是确定的，并且如果达到最大可跟踪连接数，它不会被清除。 |
| **confirmed** (*yes \| no*) | 连接已确认，并且数据包已从设备发送出去。 |
| **connection-mark** (*string*) | 由 mangle 规则设置的连接标记。 |
| **connection-type** (*pptp \| ftp*) | 连接类型，如果连接跟踪无法确定预定义的连接类型，则此属性为空。 |
| **dst-address** (*ip*) | 目标地址。 |
| **dst-port**(*integer*) | 目标端口。 |
| **dstnat** (*yes \| no*) | 连接已通过 DST-NAT（例如，端口转发）。 |
| **dying** (*yes \| no*) | 连接因连接超时而正在消亡。 |
| **expected** (*yes \| no*) | 连接是使用连接助手（预定义的服务规则）设置的。 |
| **fasttrack** (*yes \| no*) | 连接是否被 FastTrack 处理。 |
| **gre-key** (*integer*) | GRE 键字段的内容。 |
| **gre-protocol** (*string*) | 封装负载的协议。 |
| **gre-version** (*string*) | 连接中使用的 GRE 协议版本。 |
| **hw-offload**(*yes \| no*) | 硬件卸载的连接。 |
| **icmp-code** (*string*) | ICMP 代码字段。 |
| **icmp-id** (*integer*) | 包含 ICMP ID。 |
| **icmp-type** (*integer*) | ICMP 类型编号。 |
| **orig-bytes** (*integer*) | 使用特定连接从源地址发送出的字节数。 |
| **orig-fasttrack-bytes** (*integer*) | 使用特定连接从源地址发送出的 FastTrack 字节数。 |
| **orig-fasttrack-packets** (*integer*) | 使用特定连接从源地址发送出的 FastTrack 数据包数。 |
| **orig-packets** (*integer*) | 使用特定连接从源地址发送出的数据包数。 |
| **orig-rate** (*integer*) | 使用特定连接从源地址发送数据包的数据速率。 |
| **protocol** (*string*) | IP 协议类型。 |
| **repl-bytes** (*integer*) | 使用特定连接从目标地址接收到的字节数。 |
| **repl-fasttrack-bytes** (*integer*) | 使用特定连接从目标地址接收到的 FastTrack 字节数。 |
| **repl-fasttrack-packets** (*integer*) | 使用特定连接从目标地址接收到的 FastTrack 数据包数。 |
| **repl-packets** (*integer*) | 使用特定连接从目标地址接收到的数据包数。 |
| **repl-rate** (*string*) | 使用特定连接从目标地址接收数据包的数据速率。 |
| **reply-dst-address** (*ip*) | 预期用于返回数据包的目标地址。 |
| **reply-dst-port**(*integer*) | 预期用于返回数据包的目标端口。 |
| **reply-src-address** (*ip*) | 预期用于返回数据包的源地址。 |
| **reply-src-port** (*integer*) | 预期用于返回数据包的源端口。 |
| **seen-reply** (*yes \| no*) | 目标地址已回复源地址。 |
| **src-address** (*ip*) | 源地址。 |
| **src-port**(*integer*) | 源端口。 |
| **srcnat** (*yes \| no*) | 连接正在通过 SRC-NAT，包括通过 NAT 进行伪装的数据包。 |
| **tcp-state** (*string*) | TCP 连接的当前状态："established""time-wait""close""syn-sent""syn-recv""fin-wait""close-wait""last-ack""listen" |
| **timeout** (*time*) | 连接将从连接列表中移除的时间。 |
| **uses-helper**(*yes \| no*) | "IP/Firewall/Service Port" 助手已应用于特定连接。 |