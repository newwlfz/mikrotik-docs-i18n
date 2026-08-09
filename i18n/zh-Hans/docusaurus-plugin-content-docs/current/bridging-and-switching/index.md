# 桥接与交换

---

> ---

import WideTable from '@site/src/components/WideTable';

# 桥接与交换

---

![桥接示意图](https://manual.mikrotik.com/docs/bridging-and-switching/img/index-01.webp)

类似以太网的网络（以太网、IP上的以太网、ap-bridge或bridge模式下的IEEE 802.11、WDS、VLAN）可以通过MAC桥接连接在一起。桥接功能允许连接在不同LAN（使用EoIP，如果它们之间存在任何形式的IP网络互连，地理上分布的网络也可以被桥接）上的主机进行互联，就像它们连接在同一个LAN上一样。由于桥接是透明的，它们不会出现在traceroute列表中，并且如果这些LAN被桥接，任何工具都无法区分在一个LAN中工作的主机和在另一个LAN中工作的主机。但是，根据LAN的互连方式，主机之间的延迟和数据速率可能会有所不同。

在复杂的拓扑中，网络环路可能会（有意或无意地）出现。如果不进行特殊处理，环路会阻止网络正常运行，因为它们会导致雪崩式的数据包倍增。每个桥接都运行一种算法来计算如何防止环路。(R/M)STP允许桥接之间相互通信，因此它们可以协商出一个无环拓扑。所有其他会导致环路的备用连接都将被置于待机状态，这样如果主连接发生故障，另一个连接可以接替其位置。该算法定期交换配置消息（BPDU - 桥接协议数据单元），以便所有桥接都能获得有关网络拓扑变化的最新信息。(R/M)STP会选择出一个根桥，它负责网络重配置，例如阻塞和打开其他桥接上的端口。根桥是具有最低桥ID的桥接。

## 桥接接口设置

---

要将多个网络组合成一个桥，应创建一个桥接接口。之后，所有需要的接口都应设置为其端口。默认情况下，桥接MAC地址将根据桥接端口配置自动选择。为避免不必要的MAC地址更改，建议禁用 `auto-mac` 并使用 `admin-mac` 手动指定MAC地址。

**子菜单:** `/interface/bridge`

| 属性 | 描述 |
| :-- | :-- |
| **add-dhcp-option82** (*yes* \| *no*; 默认值: **no**) | **重要提示：** 从 **RouterOS 7.23版本** 开始，此设置已被移除。现在可以使用预定义变量（如 BRIDGEMAC、HOSTNAME、INTERFACE、VID）配置自定义的Remote ID和Circuit ID值。详情请参阅下面的 `dhcp-agent-circuit-id` 和 `dhcp-agent-remote-id` 属性。如果在早期版本（7.22或更早）中启用了此设置，升级将自动将配置更新为新格式。 是否向DHCP数据包添加DHCP Option 82信息（Agent Remote ID和Agent Circuit ID）。可以与支持Option 82的DHCP服务器一起使用，以分配IP地址和实施策略。此属性仅在 `dhcp-snooping` 设置为 `yes` 时生效。 在RouterOS 7.22或更早版本中，这些值是预定义的，无法修改： 对于Agent Remote ID，RouterOS使用桥接接口MAC地址，格式为 "xx:xx:xx:xx:xx:xx"（小写，冒号分隔）。对于Agent Circuit ID，RouterOS使用接口名称和VLAN ID，用冒号分隔（interface:vlan-id），其中DHCP客户端连接。仅当在桥上启用了 <code>vlan-filtering</code> 时，才包含VLAN ID。例如（`vlan-filtering=yes`）： Agent Remote ID - cc:2d:e0:01:6a:43 Agent Circuit ID - ether2:10  |
| **admin-mac** (*MAC地址*; 默认值: **none**) | 桥接的静态MAC地址。此属性仅在 `auto-mac` 设置为 `no` 时生效。 |
| **ageing-time** (*时间*; 默认值: **00:05:00**) | 主机信息在桥接数据库中保留的时间。 |
| **arp** (*disabled* \| *enabled* \| *local-proxy-arp \| proxy-arp \| reply-only*; 默认值: **enabled**) | 地址解析协议设置<code>disabled</code> - 接口将不使用ARP<code>enabled</code> - 接口将使用ARP<code>local-proxy-arp</code> - 路由器在接口上执行代理ARP，并将回复发送到同一接口<code>proxy-arp</code> - 路由器在接口上执行代理ARP，并将回复发送到其他接口<code>reply-only</code> - 接口将仅响应来自IP/ARP表中静态条目的匹配IP地址/MAC地址组合的请求。不会自动在IP/ARP表中存储动态条目。因此，为了通信成功，必须已存在有效的静态条目。 |
| **arp-inspection** (*yes \| no*; 默认值: **no**) | 启用或禁用ARP检测。启用后，到达不受信任端口上的ARP数据包将根据DHCP Snooping绑定数据库进行验证。发送方MAC-IP对与绑定条目不匹配的数据包将被丢弃。在受信任端口上，所有ARP数据包都会在无需验证的情况下被转发。此属性仅在 `dhcp-snooping` 设置为 `yes` 时生效。 |
| **arp-timeout** (*auto \| 整数*; 默认值: **auto**) | 在从IP地址未收到数据包后，ARP记录在ARP表中保留的时间。值 `auto` 等于 `/ip/settings` 中 `arp-timeout` 的值，默认为30秒。 |
| **auto-mac** (*yes \| no*; 默认值: **yes**) | 当配置 `auto-mac=yes` 时，桥接将根据以下优先级顺序自动为桥接接口选择MAC地址： 来自桥接组成部分的以太网接口；来自桥接中的非以太网接口（例如，WiFi或隧道）；如果以上都不可用，则随机生成一个地址。 如果配置发生更改，例如，向桥接添加新端口，则仅当更高优先级的地址源可用时，桥接的MAC地址才会更新。例如，如果桥接最初使用随机生成的MAC，然后添加了以太网接口，则MAC将根据最高可用优先级（在这种情况下为以太网接口）进行更新。如果当前MAC与移动到不同桥接的端口相关联，桥接也会更新MAC地址。 当前MAC地址及其优先级级别会被保存，并在重启后重新使用。 当配置 `auto-mac=no` 时，可以使用 `admin-mac` 属性手动设置静态MAC地址。 |
| **comment** (*字符串*; 默认值: ) | 接口的简短描述。 |
| **dhcp-agent-circuit-id** (*字符串*; 默认值: **!dhcp-agent-circuit-id**) | 为通过桥接的DHCP消息指定Option 82的**Circuit ID**子选项值。字符串长度限制为255个字符。 此设置取代了现已弃用的 `add-dhcp-option82` 属性。如果在早期版本（7.22或更早）中启用了 `add-dhcp-option82`，升级将自动将配置更新为新格式：$(INTERFACE):$(VID)。通过GUI配置此设置时也会显示此格式。 支持以下变量： $(BRIDGEMAC) - 当前桥接MAC地址，格式为 "xx:xx:xx:xx:xx:xx"（小写，冒号分隔）；$(HOSTNAME) - 系统标识；$(INTERFACE) - DHCP客户端连接的接口名称；$(VID) - DHCP客户端使用的VLAN ID。如果DHCP客户端未打标签，则VID对应于端口的 <code>pvid</code>。 仅当在桥上启用了 <code>vlan-filtering</code> 时适用。 变量语法规则 变量必须用括号括起来，并以美元符号（$）开头。从终端配置时，必须使用反斜杠（\）转义美元符号，否则它将被解释为RouterOS脚本变量。示例： `/interface/bridge``add add-dhcp-option82=yes dhcp-agent-circuit-id="interface: \$(INTERFACE), vlan: \$(VID)" dhcp-snooping=yes name=bridge1 vlan-filtering=yes` 此属性仅在 `dhcp-snooping` 设置为 yes 时生效。  |
| **dhcpv6-agent-circuit-id** (*字符串*; 默认值: **!dhcpv6-agent-circuit-id**) | 为通过桥接的DHCPv6消息指定Option 18的**Interface ID**子选项值。`dhcpv6-agent-circuit-id` 属性遵循与 `dhcp-agent-circuit-id` 相同的规则。  |
| **dhcp-agent-remote-id** (*字符串*; 默认值: **!dhcp-agent-remote-id**) | 为通过桥接的DHCP消息指定Option 82的**Remote ID**子选项值。字符串长度限制为255个字符。 此设置取代了现已弃用的 `add-dhcp-option82` 属性。如果在早期版本（7.22或更早）中启用了 `add-dhcp-option82`，升级将自动将配置更新为新格式：$(BRIDGEMAC)。通过GUI配置此设置时也会显示此格式。 支持以下变量： $(BRIDGEMAC) - 当前桥接MAC地址，格式为 "xx:xx:xx:xx:xx:xx"（小写，冒号分隔）；$(HOSTNAME) - 系统标识；$(INTERFACE) - DHCP客户端连接的接口名称；$(VID) - DHCP客户端使用的VLAN ID。如果DHCP客户端未打标签，则VID对应于端口的 <code>pvid</code>。 仅当在桥上启用了 <code>vlan-filtering</code> 时适用。 变量语法规则 变量必须用括号括起来，并以美元符号（$）开头。从终端配置时，必须使用反斜杠（\）转义美元符号，否则它将被解释为RouterOS脚本变量。示例： `/interface/bridge``add add-dhcp-option82=yes dhcp-agent-remote-id="ip: 192.168.88.1, identity: \$(HOSTNAME), mac: \$(BRIDGEMAC)" dhcp-snooping=yes name=bridge1 vlan-filtering=yes` 此属性仅在 `dhcp-snooping` 设置为 yes 时生效。  |
| **dhcpv6-agent-remote-id** (*字符串*; 默认值: **!dhcpv6-agent-remote-id**) | 为通过桥接的DHCPv6消息指定Option 37的**Remote ID**子选项值。`dhcpv6-agent-remote-id` 属性遵循与 `dhcp-agent-remote-id` 相同的规则。  |
| **dhcp-snooping** (*yes \| no*; 默认值: **no**) | 在桥上启用或禁用DHCP Snooping。**注意：** 启用DHCP snooping功能将关闭桥接 [fast-path](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fast-path)，这反过来会影响 [fasttrack](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fasttrack) 通过该桥接的连接的能力。  |
| **dhcpv6-snooping**(*yes \| no*; 默认值: **no**) | 在桥上启用或禁用DHCPv6 Snooping。**注意：** 启用DHCP snooping功能将关闭桥接 [fast-path](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fast-path)，这反过来会影响 [fasttrack](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fasttrack) 通过该桥接的连接的能力。  |
| **disabled** (*yes \| no*; 默认值: **no**) | 更改桥接是否被禁用。 |
| **ether-type** (*0x9100 \| 0x8100 \| 0x88a8*; 默认值: **0x8100**) | 更改用于确定数据包是否具有VLAN标签的EtherType。具有匹配EtherType的数据包被视为带标签的数据包。此属性仅在 `vlan-filtering` 设置为 `yes` 时生效。 |
| **fast-forward** (*yes \| no*; 默认值: **yes**) | Fast Path的一种特殊且更快的情况，仅适用于具有2个接口的桥接（默认仅对新桥接启用）。更多细节可以在Fast Forward部分找到。 |
| **forward-delay** (*时间*; 默认值: **00:00:15**) | 桥接接口在初始化阶段（即路由器启动或启用接口后）在监听/学习状态中花费的时间，之后桥接将开始正常运行。 |
| **forward-reserved-addresses** (*yes \| no*: 默认值: **no**) | 是否转发位于 **01:80:C2:00:00:0x** 范围内的IEEE保留组播MAC地址。符合R/M/STP标准的桥接应避免转发这些数据包；此属性仅在 `protocol-mode` 设置为 `none` 时应用。 启用保留MAC地址的转发可能会影响依赖这些地址的某些协议。建议仅在绝对必要时启用转发，例如在透明桥接设置中（例如，扩展长链路、使用桥接作为媒体转换器或进行网络分析）。 以下是RouterOS使用的一些值得注意的MAC地址和协议： 01:80:C2:00:00:00 - 生成树协议（STP）；01:80:C2:00:00:01 - 以太网流量控制；01:80:C2:00:00:02 - 链路聚合控制协议（LACP）；01:80:C2:00:00:03 - Dot1x客户端和服务器；01:80:C2:00:00:08 - 生成树协议（用于802.1ad桥接，使用 <code>ether-type=0x88a8</code>）；01:80:C2:00:00:0D - 多VLAN注册协议（用于802.1ad桥接，使用 <code>ether-type=0x88a8</code>）；01:80:C2:00:00:0E - 链路层发现协议、多机箱链路聚合组和精确时间协议；**重要提示：** 流量控制MAC地址 01:80:C2:00:00:01 是个例外；它不会被桥接转发。  |
| **frame-types** (*admit-all \| admit-only-untagged-and-priority-tagged \| admit-only-vlan-tagged*; 默认值: **admit-all**) | 指定桥接端口上允许的帧类型。此属性仅在 `vlan-filtering` 设置为 `yes` 时生效。 |
| **igmp-snooping** (*yes \| no*; 默认值: **no**) | 启用组播组和端口学习，以防止组播流量泛洪到桥接中的所有接口。 |
| **igmp-version** (*2 \| 3*; 默认值: **2**) | 选择当桥接接口充当IGMP查询器时将生成的IGMP成员资格查询的IGMP版本。此属性仅在 `igmp-snooping` 和 `multicast-querier` 设置为 `yes` 时生效。 |
| **ingress-filtering** (*yes \| no*; 默认值: **yes**) | 启用或禁用VLAN入口过滤，该功能检查入口端口是否是桥VLAN表中接收到的VLAN ID的成员。默认情况下，桥VLAN表中不存在的VLAN在发送（出口）前被丢弃，但此属性允许您在接收（入口）时丢弃数据包。应与 `frame-types` 一起使用，以指定入口流量应该是带标签还是不带标签。此属性仅在 `vlan-filtering` 设置为 `yes` 时生效。自RouterOS v7起，此设置默认启用。 |
| **ip-source-guard** (*yes \| no*; 默认值: **no**) | 启用或禁用IP源保护。启用后，桥接将根据DHCP Snooping绑定数据库验证到达不受信任端口的IPv4数据包的源IP地址。源MAC-IP对与入口端口的绑定条目不匹配的数据包将被丢弃。在受信任端口上，所有数据包都会在无需验证的情况下被转发。此属性仅在 `dhcp-snooping` 设置为 `yes` 时生效。 |
| **l2mtu** (*只读*; 默认值: ) | L2MTU 表示此接口可以发送的不含MAC头的帧的最大大小。L2MTU值将由桥接自动设置，它将使用任何关联桥接端口的最低L2MTU值。此值不能手动更改。 |
| **last-member-interval** (*时间*; 默认值: **1s**) | 当桥接端口上的最后一个客户端取消订阅组播组并且桥接充当主动查询器时，桥接将发送一个特定于组的IGMP/MLD查询，以确保没有其他客户端仍在订阅。此设置更改这些查询的响应时间。如果在特定时间段（`last-member-interval` \* `last-member-query-count`）内未收到成员资格报告，则从组播数据库（MDB）中移除该组播组。 如果桥接端口配置了fast-leave，则立即移除组播组，而无需发送任何查询。 此属性仅在 `igmp-snooping` 和 `multicast-querier` 设置为 `yes` 时生效。 |
| **last-member-query-count** (*整数: 0..4294967295*; 默认值: **2**) | 在IGMP/MLD Snooping桥接停止转发特定组播流之前，`last-member-interval` 应经过的次数。此属性仅在 `igmp-snooping` 和 `multicast-querier` 设置为 `yes` 时生效。 |
| **max-hops** (*整数: 6..40*; 默认值: **20**) | 在MSTP启用的网络中，BPDU在被忽略之前可以在同一区域内经过的桥接计数。此属性仅在 `protocol-mode` 设置为 `mstp` 时生效。 |
| **max-learned-entries** (*整数: 0..4294967295 \| auto \| unlimited*; 默认值: **auto**) | 设置桥接接口的最大学习主机数。默认值为 `auto`，取决于安装的RAM量。可以设置高于默认值的值或选择 `unlimited` 选项，但这会增加内存不足的风险。 某些RAM大小的默认值： 64 MB 为 8192；128 MB 为 16384；256 MB 为 32768；512 MB 为 65536；1024 MB 或更高为 131072。 此限制专门适用于桥接接口，而不是交换机FDB表上的硬件限制。即使达到桥接限制，交换机也可以继续在其硬件限制内学习主机并做出正确的转发决策。但是，这些额外的主机不会显示在 `/interface/bridge/host` 表中，也无法被监控。此外，达到此限制可能会影响MLAG主机同步。 此设置自RouterOS 7.16版本起可用。 |
| **max-message-age** (*时间: 6s..40s*; 默认值: **00:00:20**) | 更改根桥发送的BPDU数据包中的Max Age值。根桥发送BPDU时，Max Age设置为 `max-message-age` 值，Message Age为0。每个后续桥接在发送其BPDU之前都会递增Message Age。一旦桥接接收到Message Age等于或大于Max Age的BPDU，该BPDU将被忽略。此属性仅在 `protocol-mode` 设置为 `stp` 或 `rstp` 时生效。 |
| **membership-interval** (*时间*; 默认值: **4m20s**) | 如果在桥接端口上未收到IGMP/MLD成员资格报告，则从组播数据库（MDB）中移除条目后的时间量。此属性仅在 `igmp-snooping` 设置为 `yes` 时生效。 |
| **mld-version** (*1 \| 2*; 默认值: **1**) | 选择当桥接接口充当MLD查询器时将生成的MLD成员资格查询的MLD版本。此属性仅在桥接具有活动IPv6地址、`igmp-snooping` 和 `multicast-querier` 设置为 `yes` 时生效。 |
| **mtu** (*整数*; 默认值: **auto**) | 最大传输单元。默认情况下，桥接将自动设置MTU，它将使用任何关联桥接端口的最低MTU值。在没有添加任何桥接端口的情况下，默认桥接MTU值为1500。可以手动设置MTU值，但不能超过桥接L2MTU或最低桥接端口L2MTU。如果添加的新桥接端口的L2MTU小于桥接的 `actual-mtu`（由 `mtu` 属性设置），则手动设置的值将被忽略，桥接将表现得如同设置了 `mtu=auto` 一样。 在桥上添加VLAN接口时，如果VLAN使用的MTU高于默认的1500，建议手动设置桥接的MTU。 |
| **multicast-querier** (*yes \| no*; 默认值: **no**) | 组播查询器生成周期性的IGMP/MLD通用成员资格查询，所有支持IGMP/MLD的设备都会以IGMP/MLD成员资格报告进行响应。通常，PIM（组播）路由器或IGMP代理会生成这些查询。 通过使用此属性，您可以使启用IGMP/MLD Snooping的桥接生成IGMP/MLD通用成员资格查询。当Layer2网络中没有活动的查询器（PIM路由器或IGMP代理）时，应使用此属性。如果没有组播查询器，组播数据库（MDB）将不会更新；学习的条目将超时，IGMP/MLD Snooping将无法正常工作。 仅生成未标记的IGMP/MLD通用成员资格查询。IGMP查询使用桥接接口自身的IPv4地址作为源地址发送（参见 `querier-uses-bridge-address`），MLD查询使用桥接接口的IPv6链路本地地址发送。如果检测到外部IGMP/MLD查询器，桥接将不会发送查询（参见监控值 `igmp-querier` 和 `mld-querier`）。 此属性仅在 `igmp-snooping` 设置为 `yes` 时生效。 |
| **multicast-router** (*disabled \| permanent \| temporary-query*; 默认值: **temporary-query**) | 组播路由器端口是连接组播路由器或查询器的端口。在此端口上，将发送未注册的组播流和IGMP/MLD成员资格报告。此设置更改桥接接口本身的组播路由器状态。此属性可用于将IGMP/MLD成员资格报告发送到桥接接口，以进行进一步的组播路由或代理。此属性仅在 `igmp-snooping` 设置为 `yes` 时生效。<code>disabled</code> - 在桥接接口上禁用组播路由器状态。无论桥接接口上配置了什么，未注册的组播和IGMP/MLD成员资格报告都不会发送到桥接接口。<code>permanent</code> - 在桥接接口上启用组播路由器状态。无论桥接接口上配置了什么，未注册的组播和IGMP/MLD成员资格报告都会发送到桥接接口本身。<code>temporary-query</code> - 使用IGMP/MLD查询自动检测桥接接口上的组播路由器状态。 |
| **name** (*文本*; 默认值: **bridgeN**) | 桥接接口的名称。 |
| **port-cost-mode** (*long \| short*; 默认值: **long**) | 更改桥接端口的路径成本和内部路径成本模式，利用基于接口速度的自动值。此设置不影响手动配置了 `path-cost` 或 `internal-path-cost` 属性的桥接端口。以下是说明特定数据速率对应的路径成本的示例（中间速率按比例计算）：  <details><summary>路径成本表</summary>数据速率长模式短模式10 Mbps2,000,000100100 Mbps200,000191 Gbps20,000410 Gbps2,000225 Gbps800140 Gbps500150 Gbps4001100 Gbps2001</details> 对于HW offloaded bond接口，应用所有bond成员端口中最高的路径成本；此值不受bonding总链路速度的影响。 对于虚拟接口（如VLAN、EoIP、VXLAN和非HW offloaded bond），以及wifi、wireless和60GHz接口，长模式分配路径成本20,000，短模式分配10。 对于动态桥接的接口（例如wifi、wireless、PPP、VPLS），路径成本默认为长模式20,000，短模式10。但是，动态添加接口到桥接的服务可以手动覆盖此值，例如，使用CAPsMAN `datapath.bridge-cost` 设置。 使用 [端口监控](index.md#bridge-port-monitoring) 观察应用的路径成本。 此属性在 `protocol-mode` 设置为 `stp`、`rstp` 或 `mstp` 时生效。 |
| **priority** (*整数: 0..65535 十进制格式 或 0x0000-0xffff 十六进制格式*; 默认值: **32768 / 0x8000**) | 桥接优先级，R/STP用于确定根桥，MSTP用于确定CIST和IST区域根桥。当 `protocol-mode` 设置为 `none` 时，此属性无效。  **有效值：** 桥接优先级必须以4096（0x1000）为步长设置。最低的12位被忽略。有效值为：0x0000, 0x1000, 0x2000, 0x3000, 0x4000, 0x5000, 0x6000, 0x7000, 0x8000, 0x9000, 0xa000, 0xb000, 0xc000, 0xd000, 0xe000, 0xf000（或其十进制等效值：0, 4096, 8192, 12288, 16384, 20480, 24576, 28672, 32768, 36864, 40960, 45056, 49152, 53248, 57344, 61440）。 |
| **protocol-mode** (*none \| rstp \| stp \| mstp*; 默认值: **rstp**) | 选择生成树协议（STP）或快速生成树协议（RSTP）以确保任何桥接LAN的无环拓扑。RSTP在拓扑更改后提供更快的生成树收敛。选择MSTP以确保跨多个VLAN的无环拓扑。 位于 **01:80:C2:00:00:0x** 范围内的保留MAC地址的转发与 `protocol-mode=none` 分离，自RouterOS v7.16起作为可控制属性 `forward-reserved-addresses` 提供。 |
| **pvid** (*整数: 1..4094*; 默认值: **1**) | 端口VLAN ID（pvid）指定未标记的入口流量分配给哪个VLAN。它适用于例如从桥接IP发送并目的地为桥接端口的帧。此属性仅在 `vlan-filtering` 设置为 `yes` 时生效。 |
| **querier-interval** (*时间*; 默认值: **4m15s**) | 更改检测到的查询器和组播路由器端口的超时时间。此属性仅在 `igmp-snooping` 设置为 `yes` 时生效。 |
| **querier-uses-bridge-address** (*yes \| no*; 默认值: **yes**) | 启用后，桥接IGMP查询器使用桥接接口自身的IPv4地址作为IGMP查询数据包的源地址，而不是默认的0.0.0.0。某些组播客户端认为来自0.0.0.0的查询无效并且不响应，这可能导致snooping表条目超时时组播流中断。此属性仅在 `igmp-snooping` 和 `multicast-querier` 设置为 `yes` 且桥接接口已分配IPv4地址时生效。此设置仅适用于IPv4（IGMP）。MLD查询始终使用桥接接口的IPv6链路本地地址。 |
| **query-interval** (*时间*; 默认值: **2m5s**) | 当桥接接口充当IGMP/MLD查询器时，更改发送IGMP/MLD通用成员资格查询的间隔。该间隔在发送最后一个启动查询后开始。此属性仅在 `igmp-snooping` 和 `multicast-querier` 设置为 `yes` 时生效。 |
| **query-response-interval** (*时间*; 默认值: **10s**) | 当桥接作为IGMP/MLD查询器活动时，此设置更改通用IGMP/MLD查询的响应时间。此属性仅在 `igmp-snooping` 和 `multicast-querier` 设置为 `yes` 时生效。 |
| **region-name** (*文本*; 默认值: ) | MSTP区域名称。此属性仅在 `protocol-mode` 设置为 `mstp` 时生效。 |
| **region-revision** (*整数: 0..65535*; 默认值: **0**) | MSTP配置修订号。此属性仅在 `protocol-mode` 设置为 `mstp` 时生效。 |
| **ra-guard** (*yes \| no*; 默认值: **no**) | RA guard - 一种安全功能，根据授权、受信任端口的列表验证传入的路由器通告。 |
| **startup-query-count** (*整数: 0..4294967295*; 默认值: **2**) | 指定当桥接接口启用或活动查询器超时时，必须发送多少次通用IGMP/MLD查询。此属性仅在 `igmp-snooping` 和 `multicast-querier` 设置为 `yes` 时生效。 |
| **startup-query-interval** (*时间*; 默认值: **31s250ms**) | 指定启动时通用IGMP/MLD查询之间的间隔。此属性仅在 `igmp-snooping` 和 `multicast-querier` 设置为 `yes` 时生效。 |
| **transmit-hold-count** (*整数: 1..10*; 默认值: **6**) | 端口发送状态机用于限制发送速率的Transmit Hold Count。 |
| **vlan-filtering** (*yes \| no*; 默认值: **no**) | 全局启用或禁用桥接的VLAN功能。 |

:::danger
更改某些属性可能导致桥接暂时禁用所有端口。在生产环境中更改此类属性时必须考虑到这一点，因为它可能导致所有数据包暂时被丢弃。此类属性包括 `vlan-filtering`、`protocol-mode`、`igmp-snooping`、`fast-forward` 等。
:::

### 示例

以下示例演示如何为简单的Layer 2交换创建和验证基本桥接接口。此配置创建一个桥接，将多个以太网端口组合到一个交换网络段中。

```ros
[admin@MikroTik] > /interface/bridge/add
[admin@MikroTik] > interface bridge print 
Flags: X - disabled, R - running 
0 R name="bridge1" mtu=auto actual-mtu=1500 l2mtu=65535 arp=enabled arp-timeout=auto mac-address=5E:D2:42:95:56:7F protocol-mode=rstp fast-forward=yes 
igmp-snooping=no auto-mac=yes ageing-time=5m priority=0x8000 max-message-age=20s forward-delay=15s transmit-hold-count=6 vlan-filtering=no 
dhcp-snooping=no 
```

### 桥接监控

要监控桥接接口的当前状态，请使用 `monitor` 命令。

**子菜单:** `/interface/bridge/monitor`

| 属性 | 描述 |
| :-- | :-- |
| **bridge-id** (*优先级.MAC地址*) | 本地桥接标识符，格式为 桥接优先级.桥接MAC地址。 |
| **current-mac-address** (*MAC地址*) | 桥接的当前MAC地址。 |
| **designated-port-count** (*整数*) | 指定桥接端口的数量。 |
| **declared-vlan-ids** (*整数 1..4094*) | 通过 [MVRP协议](./index.md#mvrp) 在桥接接口上声明的VLAN。 |
| **fast-forward** (*yes \| no*) | 桥接fast-forward是否活动。 |
| **igmp-querier** (*none* \| *接口 & IPv4地址*) | 显示检测到的IGMP查询器的桥接端口和源IP地址。仅显示检测到的外部IGMP查询器，不显示本地桥接IGMP查询器（包括IGMP代理和PIM）。仅当启用 `igmp-snooping` 时，监控值才会出现。 |
| **mld-querier** (*none* \| *接口 & IPv6地址*) | 显示检测到的MLD查询器的桥接端口和源IPv6地址。仅显示检测到的外部MLD查询器，不显示本地桥接MLD查询器。仅当启用 `igmp-snooping` 且桥接具有活动IPv6地址时，监控值才会出现。 |
| **mst-config-digest** (*整数*) | VLAN映射到MST实例ID的计算哈希值。 |
| **multicast-router** (*yes \| no*) | 显示是否在端口上检测到组播路由器。仅当启用 `igmp-snooping` 时，监控值才会出现。 |
| **port-count** (*整数*) | 桥接端口的数量。 |
| **regional-root-bridge-id** (*优先级.MAC地址*) | 区域根桥ID，格式为 桥接优先级.桥接MAC地址。仅在启用MSTP时适用。 |
| **registered-vlan-ids** (*整数 1..4094*) | 通过 [MVRP协议](./index.md#mvrp) 在桥接接口上注册的VLAN。 |
| **root-bridge** (*yes \| no*) | 显示桥接是否为生成树的根桥。 |
| **root-bridge-id** (*优先级.MAC地址*) | 根桥ID，格式为 桥接优先级.桥接MAC地址。 |
| **root-path-cost** (*整数*) | 到根桥的路径总成本。 |
| **root-port** (*名称*) | 根桥连接到的端口。 |
| **state** (*enabled \| disabled*) | 桥接的状态。 |

```ros
[admin@MikroTik] /interface/bridge/monitor bridge1
                    state: enabled                         
      current-mac-address: 2C:C8:1B:FF:92:F4               
                bridge-id: 0x1000.2C:C8:1B:FF:92:F4        
              root-bridge: yes                             
           root-bridge-id: 0x1000.2C:C8:1B:FF:92:F4        
  regional-root-bridge-id: 0x1000.2C:C8:1B:FF:92:F4        
           root-path-cost: 0                               
                root-port: none                            
               port-count: 2                               
    designated-port-count: 2                               
        mst-config-digest: d2b171a8ad95f593c241fc33d419a88c
             fast-forward: no                              
         multicast-router: no                              
             igmp-querier: none                            
              mld-querier: none                            
        declared-vlan-ids: 1                               
      registered-vlan-ids: 1                               
```

## 生成树协议

---

RouterOS桥接接口能够运行生成树协议，以确保无环且冗余的拓扑。对于只有2个桥接的小型网络，STP带来的好处不多，但对于较大的网络，正确配置STP非常关键，将STP相关值保留为默认值可能导致即使单个桥接故障，网络也完全不可达。要实现正确的无环和冗余拓扑，有必要正确设置桥接优先级、端口路径成本和端口优先级。

:::danger
在RouterOS中，可以为桥接优先级设置0到65535之间的任何值，但IEEE 802.1W标准规定桥接优先级必须以4096为步长。这可能导致不支持此类值的设备之间出现兼容性问题。为避免兼容性问题，建议仅使用以下优先级：0, 4096, 8192, 12288,