# ARP

> 本文档介绍了 MikroTik RouterOS 中的 ARP（地址解析协议）功能，解释了 IP 地址如何映射到 MAC 地址。内容包括 ARP 表属性、只读标志、VRF 关联以及 ARP 模式（禁用、启用、代理 ARP），并提供了静态条目和接口特定设置的配置示例。

# ARP

**子菜单:** `/ip/arp`

尽管 IP 数据包使用 IP 地址进行寻址，但数据传输时必须使用硬件地址。地址解析协议（ARP）用于将 OSI 第三层 IP 地址映射到 OSI 第二层 MAC 地址。路由器维护一个当前使用的 ARP 条目表。通常该表是动态构建的，但为了增强网络安全性，可以通过添加静态条目来部分或完全静态构建。

## 属性

本节介绍 ARP 表的配置选项。

| 属性 | 描述 |
| :-- | :-- |
| **address** (*IP*; 默认值: ) | 需要映射的 IP 地址 |
| **interface** (*字符串*; 默认值: ) | IP 地址所分配到的接口名称 |
| **mac-address** (*MAC*; 默认值: **00:00:00:00:00:00**) | 需要映射到的 MAC 地址 |
| **published** (*是 \| 否*; 默认值: **否**) | 针对单个 IP 地址的静态代理 ARP 条目。当收到针对特定 IP 地址的 ARP 查询时，设备将使用自身的 MAC 地址进行响应。无需在接口上设置代理 ARP 即可代理所有 MAC 地址。接口仅在设备具有指向目标的有效路由时才会响应 ARP 请求 |

**只读属性:**

| 属性 | 描述 |
| :-- | :-- |
| **complete** (*是 \| 否*) | 当 ARP `status` 为永久、可达、过期、探测或延迟时，ARP 条目中包含完成标志 |
| **dhcp**(*是 \| 否*) | ARP 条目是否由 DHCP 服务器添加 |
| **disabled**(*是 \| 否*) | ARP 条目是否被禁用 |
| **dynamic** (*是 \| 否*) | 条目是否为动态创建 |
| **invalid** (*是 \| 否*) | 条目是否无效 |
| **status**(*延迟 \| 失败 \| 不完整 \| 永久 \| 探测 \| 可达 \| 过期*) | 显示 ARP 条目的状态：<code>延迟</code> - 邻居条目验证当前被延迟<code>失败</code> - ARP 解析失败，系统无法获取给定 IP 地址的 MAC 地址<code>不完整</code> - 系统没有该 IP 地址的 MAC 地址信息，尚未解析<code>永久</code> - ARP 条目被视为永久条目，即使未被主动使用也不会从表中移除。此状态用于手动配置的 ARP 条目<code>探测</code> - 正在探测邻居<code>可达</code> - ARP 解析成功，且与 IP 地址关联的 MAC 地址已知，条目在可达性超时到期前有效<code>过期</code> - 条目仍然有效，但已老化。这意味着系统最近未与该 IP 地址关联的设备通信。 |
| **VRF** (字符串) | 指示此 ARP 条目关联的 VRF。 |

:::warning
默认的最大 ARP 条目数取决于已安装的内存大小。可通过命令 "`/ip/settings/set max-neighbor-entries=`x" 进行调整，更多详情请参阅 [IPv4 设置](../cli-reference/ip/settings.md)。
:::

## ARP 模式

可以在接口配置上设置多种 ARP 模式：

- `disabled` - 接口将不使用 ARP。
- `enabled` - 接口将使用 ARP。
- `local-proxy-arp` - 路由器在接口上执行代理 ARP，并将回复发送到同一接口。
- `proxy-arp` - 路由器在接口上执行代理 ARP，并将回复发送到其他接口。
- `reply-only` - 接口仅回复来自 IP/ARP 表中静态条目的匹配 IP 地址/MAC 地址组合的请求。不会自动在 IP/ARP 表中存储动态条目。因此，为了通信成功，必须已存在有效的静态条目。

### 禁用

如果在接口上关闭 ARP 功能，即使用 `arp=disabled`，路由器将不会响应客户端的 ARP 请求。因此，也需要在客户端添加静态 ARP 条目。例如，应使用 arp 命令将路由器的 IP 和 MAC 地址添加到 Windows 工作站：

```text
C:\> arp -s 10.5.8.254  00-aa-00-62-c6-09
```

### 启用

此模式在所有接口上默认启用。ARP 将自动发现，新的动态条目将添加到 ARP 表中。

### 代理 ARP

配置了正确代理 ARP 功能的路由器在不同网络之间充当透明的 ARP 代理。

此行为可能很有用，例如，如果您想为拨号（ppp、pppoe、pptp）客户端分配与所连接 LAN 相同地址空间的 IP 地址。

可以在每个接口上单独启用代理 ARP，使用命令 `arp=proxy-arp`：

#### 设置代理 ARP

```ros
 [admin@MikroTik] /interface/ethernet> set 1 arp=proxy-arp

 [admin@MikroTik] /interface/ethernet> print

 Flags: X - disabled, R - running
   #    NAME                 MTU   MAC-ADDRESS         ARP
   0  R ether1              1500  00:30:4F:0B:7B:C1 enabled
   1  R ether2              1500  00:30:4F:06:62:12 proxy-arp
```

### 仅回复

如果接口上的 ARP 属性设置为 `reply-only`，则路由器仅回复 ARP 请求。邻居 MAC 地址将仅使用 `/ip/arp` 菜单中静态配置的条目进行解析，但无需像 ARP 禁用时那样将路由器的 MAC 地址添加到其他主机的 ARP 表中。

### 本地代理 ARP

如果接口上的 ARP 属性设置为 `local-proxy-arp`，则路由器仅对此接口执行代理 ARP，即针对从同一接口进入和离开的流量。在普通 LAN 中，默认行为是两个网络主机直接相互通信，而不涉及路由器。

启用 `local-proxy-arp` 后，路由器将使用自身的接口 MAC 地址响应所有客户端主机，而不是其他主机的 MAC 地址。

例如，如果主机 A（192.168.88.2/24）查询主机 B（192.168.88.3/24）的 MAC 地址，路由器将使用自身的 MAC 地址进行响应。换句话说，如果启用了 `local-proxy-arp`，路由器将承担转发主机 A 192.168.88.2 和主机 B 192.168.88.3 之间流量的责任。主机 A 和 B 上的所有 ARP 缓存条目将引用路由器的 MAC 地址。在这种情况下，路由器正在对整个子网 192.168.88.0/24 执行 `local-proxy-arp`。

RouterOS `local-proxy-arp` 的一个示例可以是带有 DHCP 服务器和隔离桥接端口的桥接设置，其中同一子网的主机只能通过桥接 IP 在第三层相互访问。

```ros
/interface/bridge
add arp=local-proxy-arp name=bridge1
/interface/bridge/port
add bridge=bridge1 horizon=1 interface=ether2
add bridge=bridge1 horizon=1 interface=ether3
add bridge=bridge1 horizon=1 interface=ether4
```

## 免费 ARP

可以在 RouterOS 中创建免费 ARP 请求。为此，您必须使用流量生成器工具。以下是一个生成免费 ARP 请求以更新远程设备上 ARP 表的示例：

```ros
/tool/traffic-generator/inject interface=ether2 \
data="ffffffffffff4c5e0c14ef78080600010800060400014c5e0c14ef780a057a01ffffffffffff0a057a01000000000000000000000000000000000000"
```

您必须将 MAC 地址（4c5e0c14ef78）和 IP 地址（0a057a01）更改为您路由器的地址。IP 地址和 MAC 地址必须来自请求 ARP 表更新的设备。您还需要指定要通过哪个接口（ether2）发送免费 ARP 请求。确保接收设备支持免费 ARP 请求。