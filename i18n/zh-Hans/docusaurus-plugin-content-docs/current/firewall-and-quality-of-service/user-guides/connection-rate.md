# 连接速率

> 连接速率是 MikroTik RouterOS 防火墙的一项功能，它基于连接速度来监控和过滤流量，利用 'connection-bytes' 和 'connection-rate' 来检测高速连接，以便进行优先级排序或限速。

# 连接速率

连接速率是一个防火墙匹配器，允许根据连接的当前速度来捕获流量。

## 原理

连接跟踪表中的每条记录都代表双向通信。每当一个数据包与特定记录关联时，数据包大小值（包括 IP 头部）会被添加到该记录的 "connection-bytes" 值中。（换句话说，"connection-bytes" 同时包含上传和下载流量）。

连接速率根据 "connection-bytes" 的变化来计算连接速度。连接速率每秒重新计算一次，不包含任何平均值。

"connection-bytes" 和 "connection-rate" 这两个选项仅适用于 TCP 和 UDP 流量。（您需要指定协议才能激活这些选项）。在 "connection-rate" 选项中，您可以指定想要捕获的速度范围：

```ros
ConnectionRate ::= [!]From-To
  From,To ::= 0..4294967295    (整数)
```

### 规则示例

以下规则将捕获通过路由器且连接速度低于 100kbps 的 TCP/UDP 流量：

```ros
/ip/firewall/filter
add action=accept chain=forward connection-rate=0-100k protocol=tcp
add action=accept chain=forward connection-rate=0-100k protocol=udp
```

## 应用示例 - 流量优先级

连接速率可以以多种尚未实现的方式使用，但最常见的设置是检测并降低“重连接”（长时间保持高速率的连接，如 P2P、HTTP、FTP 下载）的优先级。通过这样做，您可以优先处理所有其他流量，通常包括 VoIP、HTTP 浏览和在线游戏。

本示例中描述的方法可以与其他流量检测和优先级划分方法结合使用。由于连接速率选项不包含平均值，我们需要确定识别“重连接”的阈值。如果我们假设正常的 HTTP 浏览连接长度小于 500kB（4Mb），VoIP 所需速度不超过 200kbps，那么任何在传输前 500kB 后速度仍超过 200kbps 的连接都可以被视为“重连接”。

（在您的网络中，HTTP 浏览的 "connection-bytes" 和 VoIP 的 "connection-rate" 可能不同 - 因此，在应用此示例之前，请自行研究）

对于此示例，我们假设与 ISP 之间的上传和下载连接均为 6Mbps。

### 快速入门（适用于没有耐心的用户）

```ros
/ip/firewall/mangle
add chain=forward action=mark-connection connection-mark=!heavy_traffic_conn new-connection-mark=all_conn
add chain=forward action=mark-connection connection-bytes=500000-0 connection-mark=all_conn connection-rate=200k-100M new-connection-mark=heavy_traffic_conn protocol=tcp
add chain=forward action=mark-connection connection-bytes=500000-0 connection-mark=all_conn connection-rate=200k-100M new-connection-mark=heavy_traffic_conn protocol=udp
add chain=forward action=mark-packet connection-mark=heavy_traffic_conn new-packet-mark=heavy_traffic passthrough=no
add chain=forward action=mark-packet connection-mark=all_conn new-packet-mark=other_traffic passthrough=no

/queue/tree
add name=upload parent=public max-limit=6M
add name=other_upload parent=upload limit-at=4M max-limit=6M packet-mark=other_traffic priority=1
add name=heavy_upload parent=upload limit-at=2M max-limit=6M packet-mark=heavy_traffic priority=8
add name=download parent=local max-limit=6M
add name=other_download parent=download limit-at=4M max-limit=6M packet-mark=other_traffic priority=1
add name=heavy_download parent=download limit-at=2M max-limit=6M packet-mark=heavy_traffic priority=8
```

#### 说明

在 mangle 中，我们需要将所有连接分为两组，然后标记来自这两组的数据包。由于我们讨论的是客户端流量，最合理的标记位置是 mangle 链的 forward。

请记住，一旦“重”连接获得较低优先级并且队列达到最大限制 - 重连接的速度将会下降，连接速率也会降低。这将导致其优先级变高，连接将能够在短时间内获得更多流量，当连接速率再次上升时，又会再次导致优先级降低。为避免这种情况，我们必须确保一旦检测到“重连接”，它们将始终保持“重连接”标记。

#### IP Firewall mangle

此规则将确保“重”连接保持为重连接，并为其余连接标记默认连接标记：

```ros
/ip/firewall/mangle
add chain=forward action=mark-connection connection-mark=!heavy_traffic_conn new-connection-mark=all_conn
```

以下两条规则将根据我们的标准标记所有重连接：即任何在传输前 500kB 后速度仍超过 200kbps 的连接都可以被视为“重连接”：

```ros
add chain=forward action=mark-connection connection-bytes=500000-0 \
    connection-mark=all_conn connection-rate=200k-100M new-connection-mark=heavy_traffic_conn protocol=tcp
add chain=forward action=mark-connection connection-bytes=500000-0 \
    connection-mark=all_conn connection-rate=200k-100M new-connection-mark=heavy_traffic_conn protocol=udp
```

mangle 中的最后两条规则将简单地标记来自相应连接的所有流量：

```ros
add chain=forward action=mark-packet connection-mark=heavy_traffic_conn new-packet-mark=heavy_traffic passthrough=no
add chain=forward action=mark-packet connection-mark=all_conn new-packet-mark=other_traffic passthrough=no
```

#### 队列

这是一个简单的队列树，放置在接口 HTB 上 - "public" 是您的 ISP 连接的接口，"local" 是您的客户端所在的接口。如果您有多个 "public" 或多个 "local" 接口，您需要分别标记上传和下载流量，并将队列树放置在 global-out 中：

```ros
/queue/tree
add name=upload parent=public max-limit=6M
add name=other_upload parent=upload limit-at=4M max-limit=6M packet-mark=other_traffic priority=1
add name=heavy_upload parent=upload limit-at=2M max-limit=6M packet-mark=heavy_traffic priority=8
add name=download parent=local max-limit=6M
add name=other_download parent=download limit-at=4M max-limit=6M packet-mark=other_traffic priority=1
add name=heavy_download parent=download limit-at=2M max-limit=6M packet-mark=heavy_traffic priority=8
```