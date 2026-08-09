# PPPoE

> PPPoE 支持通过以太网链路在 PPP 和 MLPPP 上实现 IPv6 前缀委派，同时支持客户端到服务器及服务器到客户端的配置。其运行分为发现阶段和会话阶段，采用 LCP/CHAP 认证及 IPCP 进行 IP 地址分配。MTU 考量确保正确封装，而客户端属性（如认证方法和按需拨号）则增强了灵活性。

import DocCardList from '@theme/DocCardList';

# PPPoE

本节涵盖 PPPoE 示例，用于配置通过 PPP 和 MLPPP 在单条或多条链路上的 IPv6 前缀委派。

<DocCardList />

以太网点对点协议（PPPoE）是一种将 PPP 数据包封装到以太网帧中的方法。PPPoE 是标准点对点协议（PPP）的扩展，也是 PPPoA 的继任者。PPPoE 标准定义于 [RFC 2516](https://tools.ietf.org/html/rfc2516)。PPPoE 客户端和服务器可在路由器上的任何二层以太网接口上运行，例如无线、以太网、EoIP 等。一般来说，PPPoE 用于根据用户名（以及如果需要，还包括工作站）认证来向客户端分配 IP 地址，而非仅基于工作站的认证（后者使用静态 IP 地址或 DHCP）。出于明显的安全原因，建议不要在 PPPoE 所在的同一接口上使用静态 IP 地址或 DHCP。

## 简介

PPPoE 提供了通过简单的桥接接入设备将主机网络连接到远程接入集中器的能力。

支持的连接：

- MikroTik RouterOS PPPoE 客户端连接到任意 PPPoE 服务器。
- MikroTik RouterOS 服务器（接入集中器）为多个 PPPoE 客户端提供服务（客户端几乎适用于所有操作系统和大多数路由器）。

## PPPoE 操作

PPPoE 有两个不同的阶段（阶段）：

1. 发现阶段。
2. 会话阶段。

### 发现阶段

发现阶段包含四个步骤。完成后，双方都知道 PPPoE *SESSION\_ID* 和对端的以太网地址，这两者共同唯一地定义了 PPPoE 会话：

1. **PPPoE 主动发现初始化（PADI）-** PPPoE 客户端向广播地址发送 *PADI* 数据包。如果 PPPoE 客户端的拨号网络属性中输入了服务名称，此数据包也可以填充“service-name”字段。如果未输入服务名称，则该字段不会被填充。
2. **PPPoE 主动发现提供（PADO）-** 如果接入集中器能够处理 *PADI* 数据包中列出的“service-name”字段，则 PPPoE 服务器或接入集中器应使用 *PADO* 响应 *PADI*。如果未列出“service-name”字段，接入集中器将使用 *PADO* 数据包响应，该数据包的“service-name”字段填充了接入集中器能够提供的服务名称。*PADO* 数据包发送到 PPPoE 客户端的单播地址。
3. **PPPoE 主动发现请求（PADR）-** 当收到 *PADO* 数据包时，PPPoE 客户端使用 *PADR* 数据包响应。此数据包发送到接入集中器的单播地址。客户端可能收到多个 *PADO* 数据包，但客户端仅响应收到的第一个有效 *PADO*。如果初始的 *PADI* 数据包具有空白的“service-name”字段，客户端将使用 *PADO* 数据包中返回的第一个服务名称填充 *PADR* 数据包的“service-name”字段。
4. **PPPoE 主动发现会话确认（PADS）-** 当收到 *PADR* 时，接入集中器为点对点协议（PPP）会话生成唯一的会话标识（ID），并在 *PADS* 数据包中将此 ID 返回给 PPPoE 客户端。此数据包发送到客户端的单播地址。

### PPPoE 会话终止

- **PPPoE 主动发现终止（PADT）-** 可在会话建立后的任何时间发送，以指示 PPPoE 会话已终止。服务器或客户端均可发送。

### 会话阶段

当发现阶段完成后，双方都知道 *PPPoE 会话 ID* 和对端的 *以太网（MAC）地址*，这两者共同定义了 PPPoE 会话。PPP 帧被封装在 PPPoE 会话帧中，其以太网帧类型为 **0x8864**。
当服务器发送确认且客户端收到确认后，PPP 会话开始，包括以下阶段：

1. **LCP 协商** 阶段。
2. **认证（CHAP/PAP）** 阶段。
3. **IPCP 协商** 阶段——在此阶段为客户端分配 IP 地址。

:::warning
如果任何过程失败，LCP 协商建立阶段将重新开始。
:::

PPPoE 服务器向客户端发送 *Echo-Request* 数据包以确定会话状态，否则，当客户端在未发送 *Terminate-Request* 数据包的情况下终止会话时，服务器将无法确定会话已终止。

## MTU

通常，无需分片即可传输的最大以太网帧为 1500 字节。PPPoE 增加了 6 字节的开销，PPP 字段又增加了 2 字节，因此 IP 数据报剩余 1492 字节。因此，最大 PPPoE MRU 和 MTU 值不得大于 1492。

TCP 协议栈尽量避免分片，因此使用 MSS（最大分段大小）。默认情况下，MSS 选择为出接口的 MTU 减去 TCP 和 IP 头的通常大小（40 字节），对于以太网接口，结果为 1460 字节。不幸的是，可能存在 MTU 较低的中间链路，这会导致分片。在这种情况下，TCP 协议栈执行路径 MTU 发现。无法在不分片的情况下转发数据报的路由器应丢弃数据包并向源主机发送 *ICMP-Fragmentation-Required*。当主机收到此类 ICMP 数据包时，会尝试降低 MTU。这在理想情况下应该有效；然而，在现实世界中，许多路由器不生成需要分片的数据报；此外，许多防火墙会丢弃所有 ICMP 数据报。

此问题的解决方法是 [调整 MSS](../../firewall-and-quality-of-service/firewall/mangle.md#change-mss)（如果过大）。

## PPPoE 客户端

### 属性

| 属性 | 描述 |
| :-- | :-- |
| **ac-name** (*字符串*; 默认值: **""**) | 接入集中器名称，可留空，客户端将连接到广播域中的任意接入集中器 |
| **add-default-route** (*是\|否*; 默认值: **否**) | 启用/禁用是否自动添加默认路由 |
| **allow** (*mschap2\|mschap1\|chap\|pap*; 默认值: **mschap2,mschap1,chap,pap**) | 允许的认证方法，默认允许所有方法 |
| **default-route-distance** (*字节 [0..255]*; 默认值:**1**) | 设置应用于自动创建的默认路由的距离值，如果同时选择了 add-default-route |
| **dial-on-demand** (*是\|否*; 默认值: **否**) | 仅在生成出站流量时连接到 AC。如果选择，则在连接未建立时，将添加网关地址为 10.112.112.0/24 网络的路由。 |
| **interface** (*字符串*; 默认值: ) | 客户端运行的接口名称 |
| **keepalive-timeout** (*整数*; 默认值:**10**) | 设置保活超时时间（秒）。 |
| **max-mru** (*整数*; 默认值: **1492**) | 最大接收单元 |
| **max-mtu** (*整数*; 默认值: **1492**) | 最大传输单元 |
| **mrru** (*整数: 512..65535\|禁用*; 默认值: **禁用**) | 链路上可接收的最大数据包大小。如果数据包大于隧道 MTU，则会被拆分为多个数据包，从而允许通过隧道发送完整大小的 IP 或以太网数据包。 |
| **name** (*字符串*; 默认值: **pppoe-out[i]**) | PPPoE 接口的名称，如果未指定，则由 RouterOS 生成 |
| **password** (*字符串*; 默认值: ) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用于认证的密码 |
| **profile** (*字符串*; 默认值: **默认**) | 指定建立隧道时使用的 PPP 配置文件。 |
| **service-name** (*字符串*; 默认值: **""**) | 指定接入集中器上设置的服务名称，可留空以连接到任意 PPPoE 服务器 |
| **use-peer-dns** (*是\|否*; 默认值: **否**) | 启用/禁用从对端获取 DNS 设置 |
| **user** (*字符串*; 默认值: **""**) | 用于认证的用户名 |

### 状态

命令 `/interface/pppoe-client/monitor` 将显示当前 PPPoE 状态。

可用的只读属性：

| 属性 | 描述 |
| :-- | :-- |
| **ac-mac** (*MAC 地址*) | 客户端所连接的接入集中器（AC）的 MAC 地址 |
| **ac-name** (*字符串*) | 接入集中器的名称 |
| **active-links** (*整数*) | 绑定的 MLPPP 连接数（如果不使用 MLPPP，则为 '1'） |
| **encoding** (*字符串*) | 此连接中使用的加密和编码（如果不对称，则用 '/' 分隔） |
| **local-address** (*IP 地址*) | 分配给客户端的 IP 地址 |
| **remote-address** (*IP 地址*) | 分配给服务器的远程 IP 地址（即网关地址） |
| **mru** (*整数*) | 链路的有效 MRU |
| **mtu** (*整数*) | 链路的有效 MTU |
| **service-name** (*字符串*) | 使用的服务名称 |
| **status** (*字符串*) | 当前链路状态。可用值为：拨号中、验证密码...、已连接、已断开。 |
| **uptime** (*时间*) | 连接时间，以天、小时、分钟和秒显示 |

### 扫描器

PPPoE 扫描器允许扫描二层广播域中的所有活动 PPPoE 服务器。运行扫描器的命令如下：

```ros
/interface/pppoe-client/scan [interface]
```

#### 可用的只读属性

| 属性 | 描述 |
| :-- | :-- |
| **service** (*字符串*) | 服务器上配置的服务名称 |
| **mac-address** (*MAC*) | 检测到的服务器的 MAC 地址 |
| **ac-name** (*字符串*) | 接入集中器的名称 |

:::warning
对于 Windows，某些连接说明可能使用指定“电话号码”的形式，例如“MikroTik\_AC\mt1”，以指示“MikroTik\_AC”是接入集中器名称，“mt1”是服务名称。

**警告：** 指定 MRRU 意味着在单条链路上启用 MP（多链路 PPP）。此协议用于将大数据包拆分为较小的数据包。在 Windows 下，可以在“网络”选项卡、“设置”按钮、“为单链路连接协商多链路”中启用。Windows 上的 MRRU 硬编码为 1614。此设置有助于克服路径 MTU 发现失败。MP 设置应在两端同时启用。
:::

## PPPoE 服务器

PPPoE 服务器配置中有两种类型的接口（隧道）条目——静态用户和动态连接。为每个建立到指定服务器的隧道创建一个接口。如果需要在特定用户的防火墙规则或其他地方引用特定接口名称，则管理性地添加静态接口。当用户连接且用户名与任何现有静态条目不匹配时（或者如果条目已激活，则不能有两个同名的独立隧道接口——如果这是一个问题，请设置 *one-session-per-host* 值），动态接口会自动添加到列表中。动态接口在用户连接时出现，在用户断开时消失，因此无法在路由器配置中引用为该用户创建的隧道（例如，在防火墙中），因此如果您需要为该用户设置持久规则，请为其创建静态条目。否则，使用动态配置是安全的。

:::warning
在这两种情况下，都必须正确配置 PPP 用户——静态条目不能替代 PPP 配置。
:::

### 接入集中器

**子菜单：** `/interface/pppoe-server/server`

#### 属性

| 属性 | 描述 |
| :-- | :-- |
| **accept-untagged** (*是 \| 否*; 默认值: **是**) | 此设置控制当指定了 `pppoe-over-vlan-range` 时，PPPoE 服务器是否接受其接口上的未标记（非 VLAN）PPPoE 数据包。默认情况下，接受未标记的 PPPoE 数据包。如果您使用 `pppoe-over-vlan-range` 属性（该属性启用 802.1Q VLAN 上的 PPPoE），此选项允许您决定是否仍允许同一接口上的未标记客户端。如果您不使用 `pppoe-over-vlan-range`，此设置不会产生任何效果。 |
| **authentication** ( *mschap2 \| mschap1 \| chap \| pap*; 默认值: **"mschap2, mschap1, chap, pap"**) | 认证算法。 |
| **default-profile** (*字符串*; 默认值: **"默认"**) |  |
| **interface** (*字符串*; 默认值: **""**) | 客户端连接的接口。 |
| **keepalive-timeout** (*时间*; 默认值: **"10"，或禁用**) | 定义路由器开始每秒发送保活数据包之前的时间段（秒）。如果在该时间段内（即 2 \* keepalive-timeout）没有流量且没有保活响应，则未响应的客户端被宣告断开。**重要提示：** 在成功的 LCP 握手之后，客户端发送 LCP 回显数据包以验证 MTU 转发；如果未收到回复，则回退到备用 MTU 1480。新选项 `keepalive-timeout=disabled` 禁用发送回显数据包，从而有效关闭 MTU 测试。     |
| **max-mru** (*整数*; 默认值: **1480**) | 最大接收单元。最佳值是隧道工作的接口的 MTU 减去 20（因此，对于 1500 字节的以太网链路，将 MTU 设置为 1480 以避免数据包分片） |
| **max-mtu** (*整数*; 默认值: **1480**) | 最大传输单元。最佳值是隧道工作的接口的 MTU 减去 20（因此，对于 1500 字节的以太网链路，将 MTU 设置为 1480 以避免数据包分片） |
| **max-sessions** (*整数*; 默认值: **"0"**) | AC 可以服务的最大客户端数。'0' = 无限制。 |
| **mrru** (*整数: 512..65535 \| 禁用*; 默认值: **"禁用"**) | 链路上可接收的最大数据包大小。如果数据包大于隧道 MTU，则会被拆分为多个数据包，从而允许通过隧道发送完整大小的 IP 或以太网数据包。 |
| **one-session-per-host** (*是 \| 否*; 默认值: **"否"**) | 每个主机仅允许一个会话（由 MAC 地址确定）。如果主机尝试建立新会话，旧会话将被关闭。 |
| **pppoe-over-vlan-range** (*整数 1..4094*; 默认值: "") | 此设置允许 PPPoE 服务器在 802.1Q VLAN 上运行。默认情况下，PPPoE 服务器仅接受其接口上的未标记数据包。然而，在客户端位于不同 VLAN 的场景中，与其创建多个 802.1Q VLAN 接口并将它们桥接在一起，或为每个 VLAN 配置单独的 PPPoE 服务器，您可以直接在 PPPoE 服务器设置中指定所需的 VLAN。当您指定 VLAN ID 时，PPPoE 服务器将接受来自客户端的 802.1Q 标记数据包，并使用相同的 VLAN 进行回复。然后，您可以使用 `accept-untagged` 属性选择接受或丢弃同一接口上的未标记 PPPoE 客户端。您甚至可以在 [VLAN 接口](../../bridging-and-switching/vlan.md) 上配置带有 `pppoe-over-vlan-range` 设置的 PPPoE 服务器，从而支持 QinQ 配置。但请记住，内层 VLAN 标签应为 802.1Q。该设置支持 VLAN ID 范围以及使用逗号分隔值指定的单个 VLAN。例如：pppoe-over-vlan-range=100-115,120,122,128-130。**注意：** 避免在接口上配置带有 `pppoe-over-vlan-range` 的服务器，同时创建使用该范围内 VLAN ID 的 VLAN 接口。例如：`/interface/vlan``add interface=ether2 name=vlan15 vlan-id=15``/interface/pppoe-server/server``add disabled=no interface=ether2 pppoe-over-vlan-range=10-20` 如果您需要此类配置，请从 `pppoe-over-vlan-range` 中移除重叠的 VLAN ID，并直接在 VLAN 接口上创建单独的 PPPoE 服务器实例，如下所示：`/interface/vlan``add interface=ether2 name=vlan15 vlan-id=15``/interface/pppoe-server/server``add disabled=no interface=ether2 pppoe-over-vlan-range=10-14,16-20``add disabled=no interface=vlan15`    |
| **service-name** (*字符串*; 默认值: **""**) | PPPoE 服务名称。服务器将接受发送的 PADI 消息中服务名称与此设置匹配的客户端，或者 PADI 消息中 service-name 字段未设置的客户端。 |

PPPoE 服务器（接入集中器）支持每个接口上的多个服务器——具有不同的服务名称。接入集中器名称和 PPPoE 服务名称由客户端用于标识要注册的接入集中器。接入集中器名称与命令提示符前显示的路由器标识相同。标识可以在 *`/system/identity`* 子菜单中设置。

:::danger
不要在将要接收 PPPoE 请求的接口上分配 IP 地址。
:::

指定 MRRU 意味着在单条链路上启用 MP（多链路 PPP）。此协议用于将大数据包拆分为较小的数据包。MRRU 硬编码为 1614。此设置有助于克服路径 MTU 发现失败。MP 设置应在两端同时启用。

:::warning
默认的 *keepalive-timeout* 值 10 秒在大多数情况下是合适的。如果将其设置为 0，路由器将不会断开客户端，直到它们显式注销或路由器重启。要解决此问题，可以使用 one-session-per-host 属性。
:::

## 快速示例

![](https://manual.mikrotik.com/docs/virtual-private-networks/pppoe/img/pppoe-network-topology.jpg)

### PPPoE 客户端

要将 MikroTik RouterOS 配置为 PPPoE 客户端，只需添加一个 PPPoE 客户端，参数如下例所示：

```ros
[admin@MikroTik] > interface pppoe-client add interface=ether2 password=StrongPass service-name=pppoeservice name=PPPoE-Out disabled=no user=MT-User
[admin@MikroTik] > interface pppoe-client print
Flags: X - disabled, I - invalid, R - running 
 0  R name="PPPoE-Out" max-mtu=auto max-mru=auto mrru=disabled interface=ether2 user="MT-User" 
      password="StrongPass" profile=default keepalive-timeout=10 service-name="pppoeservice" ac-name="" 
      add-default-route=no dial-on-demand=no use-peer-dns=no allow=pap,chap,mschap1,mschap2
```

### PPPoE 服务器

要将 MikroTik RouterOS 配置为接入集中器（PPPoE 服务器）：

- 为客户端添加 IP 地址池，范围为 10.0.0.2-10.0.0.5。
- 添加 PPP 配置文件。
- 添加 PPP 密钥（用户名/密码）。
- 添加 PPPoE 服务器本身。

```ros
[admin@MikroTik] > /ip/pool
add name=pppoe-pool ranges=10.0.0.2-10.0.0.5
[admin@MikroTik] > /ppp/profile
add local-address=10.0.0.1 name=for-pppoe remote-address=pppoe-pool
[admin@MikroTik] > /ppp/secret
add name=MT-User password=StrongPass profile=for-pppoe service=pppoe
[admin@MikroTik] > /interface/pppoe-server/server
add default-profile=for-pppoe disabled=no interface=ether3 service-name=pppoeservice
```

## 备注

不建议在单台设备上使用大量的 pppoe 客户端。