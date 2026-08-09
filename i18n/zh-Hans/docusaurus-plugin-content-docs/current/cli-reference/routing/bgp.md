# BGP

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/bgp

**条件：** !smips
**类型：** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="routing-table" typ="enum" unset="1">用于安装路由的路由表名称。覆盖实例参数。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1">BGP 连接所操作的 VRF 名称。默认使用 "main" 路由表。</ArgTableRow>
<ArgTableRow arg="templates" typ="multi { enum
 }" unset="1">用于继承参数值的模板名称列表。此功能便于轻松配置具有重叠配置选项的组。</ArgTableRow>
<ArgTableRow arg="as" typ="as" unset="1">32 位 BGP 自治系统编号。该值接受 AS-Plain 或 AS-Dot 格式。覆盖实例 ASN，并使用以下格式配置 BGP 联盟：_`confederation_as/as`_。例如，如果您的 AS 是 34，联盟 AS 是 43，请设置 `as=43/34`。</ArgTableRow>
<ArgTableRow arg="nexthop-choice" typ="enum (default | force-self | propagate)" unset="1">影响出站 **NEXT\_HOP** 属性的选择。在过滤器中设置的下一跳始终优先，并且在路由反射时不会被更改，除非在过滤器中设置。   default - 按照 [`RFC 4271`](https://tools.ietf.org/html/rfc4271) 中的描述选择下一跳   force-self - 使用连接到对等体的接口的本地地址作为下一跳   propagate - 传播接收到的下一跳；如果路由具有 BGP **NEXT\_HOP** 属性，则将其用作下一跳；否则，回退到默认情况</ArgTableRow>
<ArgTableRow arg="multihop" typ="bool" unset="1">当远程对等体距离超过一跳时启用。此选项影响出站下一跳的选择，如 [`RFC 4271`](https://tools.ietf.org/html/rfc4271) 中所述（仅适用于 eBGP，不包括联盟本地的 iBGP 对等体）。它还会影响：是否接受来自不在同一网络中的对等体的连接（使用连接的远程地址进行检查）是否接受具有不在用于建立连接的地址同一网络中的 NEXT\_HOP 属性的入站路由从此对等体安装的路由的目标范围；来自多跳或 iBGP 对等体的路由默认通过 IGP 路由解析其下一跳</ArgTableRow>
<ArgTableRow arg="hold-time" typ="alt { enum (infinity) { infinity:0 }
, time [3 .. 65535]
 }" unset="1">指定与对等体协商时使用的 BGP 保持时间值。根据 BGP 规范，如果路由器在 OPEN 消息的保持时间字段指定的时间内未收到连续的 **KEEPALIVE** 和/或 **UPDATE** 和/或 **NOTIFICATION** 消息，则到对等体的 BGP 连接将被关闭。将使用两个对等体中的最小 `hold-time` 值（请注意，特殊值 0 或 'infinity' 低于任何其他值）*   infinity \- 永不过期连接且从不发送 keepalive 消息。</ArgTableRow>
<ArgTableRow arg="keepalive-time" typ="time" unset="1">keepalive 消息之间的间隔，如果未设置，则默认 keepalive 为 `hold-time` 的 1/3。</ArgTableRow>
<ArgTableRow arg="afi" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6, evpn)" unset="1">此对等体可以交换路由信息的地址族列表。远程对等体必须支持 BGP capabilities 可选参数（通常都支持）才能协商除 IP 之外的任何其他地址族。</ArgTableRow>
<ArgTableRow arg="cisco-vpls-nlri-len-fmt" typ="enum (auto-bits | auto-bytes | bits | bytes)" unset="1">VPLS NLRI 长度格式类型。用于与 Cisco VPLS 兼容。\[\[了解更多>>\]\]。</ArgTableRow>
<ArgTableRow arg="output.remove-private-as" typ="bool" unset="1">如果设置，则在发送出站路由更新之前，如果 BGP **AS-PATH** 属性仅包含私有 AS 编号，则移除该属性。移除过程发生在应用路由过滤器之前以及本地 AS 编号被前置到 AS 路径之前。</ArgTableRow>
<ArgTableRow arg="output.as-override" typ="bool" unset="1">如果设置，则在向该对等体发送路由更新之前，BGP **AS-PATH** 属性中远程对等体 AS 编号的所有实例都将替换为本地 AS 编号。发生在路由过滤和前置之前。</ArgTableRow>
<ArgTableRow arg="use-bfd" typ="bool" unset="1">是否使用 BFD 协议以加快连接状态检测。</ArgTableRow>
<ArgTableRow arg="save-to" typ="string" unset="1">将 BGP 协议特定的数据包内容（导出的 PDU）保存为 pcap 格式的文件名。此方法允许更简单地对特定对等体进行数据包捕获以进行调试。</ArgTableRow>
<ArgTableRow arg="output.add-path" typ="ubit (ip, ipv6)" unset="1">为指定的地址族启用发送附加路径（BGP Addpath）。</ArgTableRow>
<ArgTableRow arg="output.affinity" typ="enum (main | alone | remote-as | instance | afi | vrf | input)" unset="1">配置输出多核处理。在 [路由协议多核支持](../../user-guides/routing-and-networking-protocols/routing-protocol-multi-core-support.md) 文章中了解更多信息。   **alone** - 每个会话的输入和输出在其自己的进程中处理，当有大量核心和大量对等体时，这很可能是最佳选择   **afi, instance, vrf, remote-as** - 尝试在具有相似参数的进程中运行新会话的输入/输出   **main** - 在主进程中运行输入/输出（在单核甚至核心数量较少的多核设备上可能提高性能）   **input** - 在与输入相同的进程中运行输出（只能为输出亲和性设置）</ArgTableRow>
<ArgTableRow arg="output.redistribute" typ="ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, bgp-mpls-vpn, slaac)" unset="1">启用指定路由类型的重分发。</ArgTableRow>
<ArgTableRow arg="output.filter-select" typ="enum" unset="1">用于前缀选择的 routing select 链名称。如果未指定，则使用默认选择。</ArgTableRow>
<ArgTableRow arg="output.filter-chain" typ="enum" unset="1">用于输出前缀的路由过滤器链名称。如果未指定链，则 BGP 默认接受所有内容。</ArgTableRow>
<ArgTableRow arg="output.network" typ="enum" unset="1">用于发送本地网络的地址列表名称。仅当路由表中存在匹配的 IGP 路由且其 **ORIGIN** 属性设置为 IGP 时，才会发送该网络，其他分发方法的 **ORIGIN** 属性设置为 INCOMPLETE。</ArgTableRow>
<ArgTableRow arg="output.network-blackhole" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="output.default-originate" typ="enum (never | if-installed | always)" unset="1">指定默认路由（0.0.0.0/0）的分发方法。'if-installed' 选项可用于仅在路由表中存在相应的 IGP 路由时分发默认路由。</ArgTableRow>
<ArgTableRow arg="output.default-prepend" typ="num" unset="1">前置本地 ASN 的次数。</ArgTableRow>
<ArgTableRow arg="output.no-client-to-client-reflection" typ="bool" unset="1">在路由反射器设置中禁用客户端到客户端的路由反射。</ArgTableRow>
<ArgTableRow arg="output.no-early-cut" typ="bool" unset="1">early cut 是一种机制，用于（基于默认 RFC 行为）猜测发送的 NLRI 在远程对等体接收时会发生什么。如果算法确定 NLRI 将被丢弃，则对等体甚至不会尝试发送它。然而，在特定场景中可能不希望出现这种行为，此时应使用此选项禁用 early cut 功能。Early cut 适用于 eBGP 会话。</ArgTableRow>
<ArgTableRow arg="output.keep-sent-attributes" typ="bool" unset="1">在内存中存储已发送的前缀属性，这是 `dump-saved-advertisements` 命令工作所必需的。默认情况下，不存储已发送的前缀以节省路由器内存。仅在调试需要查看当前通告的前缀时才应启用此选项。</ArgTableRow>
<ArgTableRow arg="input.add-path" typ="ubit (ip, ipv6)" unset="1">接受指定地址族接收到的附加路径（BGP Addpath）。</ArgTableRow>
<ArgTableRow arg="input.attr-error-handling" typ="enum (default | revised)"></ArgTableRow>
<ArgTableRow arg="input.affinity" typ="enum (main | alone | remote-as | instance | afi | vrf)" unset="1">
配置输入多核处理。在 [路由协议多核支持](../../user-guides/routing-and-networking-protocols/routing-protocol-multi-core-support.md) 文章中了解更多信息。
- **alone** - 每个会话的输入和输出在其自己的进程中处理，当有大量核心和大量对等体时，这很可能是最佳选择。
- **afi, instance, vrf, remote-as** - 尝试在具有相似参数的进程中运行新会话的输入/输出。
- **main** - 在主进程中运行输入/输出（在单核甚至核心数量较少的多核设备上可能提高性能）。
</ArgTableRow>
<ArgTableRow arg="input.filter" typ="enum" unset="1">用于输入前缀的路由过滤器链名称。这发生在 NLRIs 被处理之后。如果未指定链，则 BGP 默认接受所有内容。</ArgTableRow>
<ArgTableRow arg="input.filter-nlri" typ="enum" unset="1">过滤器链的名称，用于在传入的 IPv4/IPv6 NLRIs 存储到内存之前直接过滤它们，从而显著减少内存使用。常规输入过滤器链只能拒绝前缀，这意味着它仍会占用内存，并将在 /routing route 表中显示为 "not active, filtered"。更改需要重启会话才能生效。</ArgTableRow>
<ArgTableRow arg="input.allow-as" typ="num" unset="1">指示在丢弃前缀之前，允许在 AS-PATH 中出现多少次您自己的 AS 编号。</ArgTableRow>
<ArgTableRow arg="input.accept-nlri" typ="enum" unset="1">ipv4/6 地址列表的名称。一种快速过滤具有特定 NLRIs 的传入更新的方法。它允许在传入消息被解析并存储到内存之前直接过滤它们，从而显著减少内存使用。常规输入过滤器链只能拒绝前缀，这意味着它仍会占用内存，并将在 /routing route 表中显示为 "not active, filtered"。更改需要重启会话才能生效。</ArgTableRow>
<ArgTableRow arg="input.filter-communities" typ="enum" unset="1">一种快速过滤具有特定 communities 的传入更新的方法。它允许在传入消息被解析并存储到内存之前直接过滤它们，从而显著减少内存使用。常规输入过滤器链只能拒绝前缀，这意味着它仍会占用内存，并将在 /routing route 表中显示为 "not active, filtered"。更改需要刷新会话才能生效。</ArgTableRow>
<ArgTableRow arg="input.filter-ext-communities" typ="enum" unset="1">一种快速过滤具有特定扩展 communities 的传入更新的方法。它允许在传入消息被解析并存储到内存之前直接过滤它们，从而显著减少内存使用。常规输入过滤器链只能拒绝前缀，这意味着它仍会占用内存，并将在 /routing route 表中显示为 "not active, filtered"。更改需要刷新会话才能生效。</ArgTableRow>
<ArgTableRow arg="input.filter-large-communities" typ="enum" unset="1">一种快速过滤具有特定大型 communities 的传入更新的方法。它允许在传入消息被解析并存储到内存之前直接过滤它们，从而显著减少内存使用。常规输入过滤器链只能拒绝前缀，这意味着它仍会占用内存，并将在 /routing route 表中显示为 "not active, filtered"。更改需要刷新会话才能生效。</ArgTableRow>
<ArgTableRow arg="input.accept-communities" typ="enum" unset="1">一种快速过滤具有特定 communities 的传入更新的方法。它允许在传入消息被解析并存储到内存之前直接过滤它们，从而显著减少内存使用。常规输入过滤器链只能拒绝前缀，这意味着它仍会占用内存，并将在 /routing route 表中显示为 "not active, filtered"。更改需要刷新会话才能生效。</ArgTableRow>
<ArgTableRow arg="input.accept-ext-communities" typ="enum" unset="1">一种快速过滤具有特定扩展 communities 的传入更新的方法。它允许在传入消息被解析并存储到内存之前直接过滤它们，从而显著减少内存使用。常规输入过滤器链只能拒绝前缀，这意味着它仍会占用内存，并将在 /routing route 表中显示为 "not active, filtered"。更改需要刷新会话才能生效。</ArgTableRow>
<ArgTableRow arg="input.accept-large-communities" typ="enum" unset="1">一种快速过滤具有特定大型 communities 的传入更新的方法。它允许在传入消息被解析并存储到内存之前直接过滤它们，从而显著减少内存使用。常规输入过滤器链只能拒绝前缀，这意味着它仍会占用内存，并将在 /routing route 表中显示为 "not active, filtered"。更改需要刷新会话才能生效。</ArgTableRow>
<ArgTableRow arg="input.filter-unknown" typ="enum" unset="1">一种快速过滤具有特定 "unknown" 属性的传入更新的方法。它允许在传入消息被解析并存储到内存之前直接过滤它们，从而显著减少内存使用。常规输入过滤器链只能拒绝前缀，这意味着它仍会占用内存，并将在 /routing route 表中显示为 "not active, filtered"。更改需要刷新会话才能生效。</ArgTableRow>
<ArgTableRow arg="input.limit-process-routes-ipv4" typ="enum (10 | 100 | 1000 | 10000 | 100000 | 1000000 | 10000000)" unset="1">尝试将接收到的 IPv4 路由数量限制为指定数量。此数字并不代表对等体将要在路由表中安装的确切路由数量。如果达到限制，必须使用 [BGP 会话 "clear"](#routingbgpsessionclear) 命令来重置标志。</ArgTableRow>
<ArgTableRow arg="input.limit-process-routes-ipv6" typ="enum (10 | 100 | 1000 | 10000 | 100000 | 1000000 | 10000000)" unset="1">尝试将接收到的 IPv6 路由数量限制为指定数量。此数字并不代表对等体将要在路由表中安装的确切路由数量。如果达到限制，必须使用 BGP 会话 "clear" 命令来重置标志。</ArgTableRow>
</ArgTable>

### routing/bgp/advertisements

**条件：** !smips
**类型：** 目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="peer" typ="enum"></ArgTableRow>
<ArgTableRow arg="dst" typ="address (flags=46/R)"></ArgTableRow>
<ArgTableRow arg="afi" typ="enum (ip | ipv6 | l2vpn | l2vpn-cisco | vpnv4 | vpnv6)"></ArgTableRow>
<ArgTableRow arg="local-pref" typ="num"></ArgTableRow>
<ArgTableRow arg="med" typ="num"></ArgTableRow>
<ArgTableRow arg="nexthop" typ="multi { address (flags=46)
 }"></ArgTableRow>
<ArgTableRow arg="nlri" typ="multi { address (flags=46i/SR)
 }"></ArgTableRow>
<ArgTableRow arg="withdrawn" typ="multi { address (flags=46i/SR)
 }"></ArgTableRow>
<ArgTableRow arg="origin" typ="num"></ArgTableRow>
<ArgTableRow arg="as-path" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="as4-path" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="communities" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="ext-communities" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="large-communities" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="atomic-aggregate" typ="bool"></ArgTableRow>
<ArgTableRow arg="aggregator" typ="string"></ArgTableRow>
<ArgTableRow arg="as4-aggregator" typ="string"></ArgTableRow>
<ArgTableRow arg="originator-id" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="cluster-list" typ="multi { ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="igp-metric" typ="num"></ArgTableRow>
<ArgTableRow arg="otc" typ="num"></ArgTableRow>
</ArgTable>

### routing/bgp/connection

**条件：** !smips
**类型：** 目录

所有连接特定参数的列表可以在下表中看到。

除了连接特定参数外，模板特定参数也直接在此菜单中公开，以便在简单场景（不需要模板时）更容易配置。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">非活动</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="instance" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="remote.address" typ="address (flags=46i/+:)" unset="1">用于连接和/或监听的远程地址。</ArgTableRow>
<ArgTableRow arg="remote.port" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="remote.as" typ="super { as
, [ /as]
 }" unset="1">远程 AS 编号。如果未指定，BGP 将自动从 OPEN 消息中确定远程 AS。</ArgTableRow>
<ArgTableRow arg="remote.ttl" typ="num">可接受的最小生存时间（TTL），即此 TCP 连接的跳数限制。例如，如果 'ttl=255'，则只有单跳邻居才能建立连接。此属性仅影响 EBGP 对等体。</ArgTableRow>
<ArgTableRow arg="remote.allowed-as" typ="enum" unset="1">包含允许连接的远程 AS 编号的 num-list 名称。对于动态对等体配置很有用。</ArgTableRow>
<ArgTableRow arg="local.address" typ="address (flags=46i:)" unset="1"></ArgTableRow>
<ArgTableRow arg="local.port" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="local.ttl" typ="num">将在发送的 TCP 数据包中记录的生存时间（跳数限制）。</ArgTableRow>
<ArgTableRow arg="local.role" typ="enum (ibgp | ibgp-rr | ebgp | ebgp-provider | ebgp-rs | ebgp-rs-client | ebgp-customer | ebgp-peer)" mandatory="1">BGP 角色。在大多数场景中，设置为 iBGP 或 eBGP。有关 BGP 角色的更多信息，请参见相应的 [RFC 9234](https://tools.ietf.org/html/rfc9234)。</ArgTableRow>
<ArgTableRow arg="tcp-md5-key" typ="string" unset="1">用于使用 TCP MD5 签名验证连接身份的密钥，如 [RFC 2385](https://tools.ietf.org/html/rfc2385) 中所述。留空以禁用身份验证。</ArgTableRow>
<ArgTableRow arg="connect" typ="bool">是否允许路由器发起连接。</ArgTableRow>
<ArgTableRow arg="listen" typ="bool">启用对传入连接的监听。如果 `remote.address` 是主机地址且启用了监听，则在第一次成功接受后关闭监听套接字。如果 `remote.address` 是子网且启用了监听，则在第一次成功接受后监听套接字保持打开状态，并带有 256 个打开连接的硬编码限制。</ArgTableRow>
<ArgTableRow arg="routing-table" typ="enum" unset="1">用于安装路由的路由表名称。覆盖实例参数。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1">BGP 连接所操作的 VRF 名称。默认使用 "main" 路由表。</ArgTableRow>
<ArgTableRow arg="templates" typ="multi { enum
 }" unset="1">用于继承参数值的模板名称列表。此功能便于轻松配置具有重叠配置选项的组。</ArgTableRow>
<ArgTableRow arg="as" typ="as" unset="1">32 位 BGP 自治系统编号。该值接受 AS-Plain 或 AS-Dot 格式。覆盖实例 ASN，并使用以下格式配置 BGP 联盟：_`confederation_as/as`_。例如，如果您的 AS 是 34，联盟 AS 是 43，请设置 `as=43/34`。</ArgTableRow>
<ArgTableRow arg="nexthop-choice" typ="enum (default | force-self | propagate)" unset="1">影响出站 **NEXT\_HOP** 属性的选择。在过滤器中设置的下一跳始终优先，并且在路由反射时不会被更改，除非在过滤器中设置。   default - 按照 [`RFC 4271`](https://tools.ietf.org/html/rfc4271) 中的描述选择下一跳   force-self - 使用连接到对等体的接口的本地地址作为下一跳   propagate - 传播接收到的下一跳；如果路由具有 BGP **NEXT\_HOP** 属性，则将其用作下一跳；否则，回退到默认情况</ArgTableRow>
<ArgTableRow arg="multihop" typ="bool" unset="1">当远程对等体距离超过一跳时启用。此选项影响出站下一跳的选择，如 [`RFC 4271`](https://tools.ietf.org/html/rfc4271) 中所述（仅适用于 eBGP，不包括联盟本地的 iBGP 对等体）。它还会影响：是否接受来自不在同一网络中的对等体的连接（使用连接的远程地址进行检查）是否接受具有不在用于建立连接的地址同一网络中的 NEXT\_HOP 属性的入站路由从此对等体安装的路由的目标范围；来自多跳或 iBGP 对等体的路由默认通过 IGP 路由解析其下一跳</ArgTableRow>
<ArgTableRow arg="hold-time" typ="alt { enum (infinity) { infinity:0 }
, time [3 .. 65535]
 }" unset="1">指定与对等体协商时使用的 BGP 保持时间值。根据 BGP 规范，如果路由器在 OPEN 消息的保持时间字段指定的时间内未收到连续的 **KEEPALIVE** 和/或 **UPDATE** 和/或 **NOTIFICATION** 消息，则到对等体的 BGP 连接将被关闭。将使用两个对等体中的最小 `hold-time` 值（请注意，特殊值 0 或 'infinity' 低于任何其他值）*   infinity \- 永不过期连接且从不发送 keepalive 消息。</ArgTableRow>
<ArgTableRow arg="keepalive-time" typ="time" unset="1">keepalive 消息之间的间隔，如果未设置，则默认 keepalive 为 `hold-time` 的 1/3。</ArgTableRow>
<ArgTableRow arg="afi" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6, evpn)" unset="1">此对等体可以交换路由信息的地址族列表。远程对等体必须支持 BGP capabilities 可选参数（通常都支持）才能协商除 IP 之外的任何其他地址族。</ArgTableRow>
<ArgTableRow arg="cisco-vpls-nlri-len-fmt" typ="enum (auto-bits | auto-bytes | bits | bytes)" unset="1">VPLS NLRI 长度格式类型。用于与 Cisco VPLS 兼容。\[\[了解更多>>\]\]。</ArgTableRow>
<ArgTableRow arg="output.remove-private-as" typ="bool" unset="1">如果设置，则在发送出站路由更新之前，如果 BGP **AS-PATH** 属性仅包含私有 AS 编号，则移除该属性。移除过程发生在应用路由过滤器之前以及本地 AS 编号被前置到 AS 路径之前。</ArgTableRow>
<ArgTableRow arg="output.as-override" typ="bool" unset="1">如果设置，则在向该对等体发送路由更新之前，BGP **AS-PATH** 属性中远程对等体 AS 编号的所有实例都将替换为本地 AS 编号。发生在路由过滤和前置之前。</ArgTableRow>
<ArgTableRow arg="use-bfd" typ="bool" unset="1">是否使用 BFD 协议以加快连接状态检测。</ArgTableRow>
<ArgTableRow arg="save-to" typ="string" unset="1">将 BGP 协议特定的数据包内容（导出的 PDU）保存为 pcap 格式的文件名。此方法允许更简单地对特定对等体进行数据包捕获以进行调试。</ArgTableRow>
<ArgTableRow arg="output.add-path" typ="ubit (ip, ipv6)" unset="1">为指定的地址族启用发送附加路径（BGP Addpath）。</ArgTableRow>
<ArgTableRow arg="output.affinity" typ="enum (main | alone | remote-as | instance | afi | vrf | input)" unset="1">配置输出多核处理。在 [路由协议多核支持](../../user-guides/routing-and-networking-protocols/routing-protocol-multi-core-support.md) 文章中了解更多信息。   **alone** - 每个会话的输入和输出在其自己的进程中处理，当有大量核心和大量对等体时，这很可能是最佳选择   **afi, instance, vrf, remote-as** - 尝试在具有相似参数的进程中运行新会话的输入/输出   **main** - 在主进程中运行输入/输出（在单核甚至核心数量较少的多核设备上可能提高性能）   **input** - 在与输入相同的进程中运行输出（只能为输出亲和性设置）</ArgTableRow>
<ArgTableRow arg="output.redistribute" typ="ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, bgp-mpls-vpn, slaac)" unset="1">启用指定路由类型的重分发。</ArgTableRow>
<ArgTableRow arg="output.filter-select" typ="enum" unset="1">用于前缀选择的 routing select 链名称。如果未指定，则使用默认选择。</ArgTableRow>
<ArgTableRow arg="output.filter-chain" typ="enum" unset="1">用于输出前缀的路由过滤器链名称。如果未指定链，则 BGP 默认接受所有内容。</ArgTableRow>
<ArgTableRow arg="output.network" typ="enum" unset="1">用于发送本地网络的地址列表名称。仅当路由表中存在匹配的 IGP 路由且其 **ORIGIN** 属性设置为 IGP 时，才会发送该网络，其他分发方法的 **ORIGIN** 属性设置为 INCOMPLETE。</ArgTableRow>
<ArgTableRow arg="output.network-blackhole" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="output.default-originate" typ="enum (never | if-installed | always)" unset="1">指定默认路由（0.0.0.0/0）的分发方法。'if-installed' 选项可用于仅在路由表中存在相应的 IGP 路由时分发默认路由。</ArgTableRow>
<ArgTableRow arg="output.default-prepend" typ="num" unset="1">前置本地 ASN 的次数。</ArgTableRow>
<ArgTableRow arg="output.no-client-to-client-reflection" typ="bool" unset="1">在路由反射器设置中禁用客户端到客户端的路由反射。</ArgTableRow>
<ArgTableRow arg="output.no-early-cut" typ="bool" unset="1">early cut 是一种机制，用于（基于默认 RFC 行为）猜测发送的 NLRI 在远程对等体接收时会发生什么。如果算法确定 NLRI 将被丢弃，则对等体甚至不会尝试发送它。然而，在特定场景中可能不希望出现这种行为，此时应使用此选项禁用 early cut 功能。Early cut 适用于 eBGP 会话。</ArgTableRow>
<ArgTableRow arg="output.keep-sent-attributes" typ="bool" unset="1">在内存中存储已发送的前缀属性，这是 `dump-saved-advertisements` 命令工作所必需的。默认情况下，不存储已发送的前缀以节省路由器内存。仅在调试需要查看当前通告的前缀时才应启用此选项。</ArgTableRow>
<ArgTableRow arg="input.add-path" typ="ubit (ip, ipv6)" unset="1">接受指定地址族接收到的附加路径（BGP Addpath）。</ArgTableRow>
<ArgTableRow arg="input.attr-error-handling" typ="enum (default | revised)"></ArgTableRow>
<ArgTableRow arg="input.affinity" typ="enum (main | alone | remote-as | instance | afi | vrf)" unset="1">
配置输入多核处理。在 [路由协议多核支持](../../user-guides/routing-and-networking-protocols/routing-protocol-multi-core-support.md) 文章中了解更多信息。
- **alone** - 每个会话的输入和输出在其自己的进程中处理，当有大量核心和大量对等体时，这很可能是最佳选择。
- **afi, instance, vrf, remote-as** - 尝试在具有相似参数的进程中运行新会话的输入/输出。
- **main** - 在主进程中运行输入/输出（在单核甚至核心数量较少的多核设备上可能提高性能）。
</ArgTableRow>
<ArgTableRow arg="input.filter" typ="enum" unset="1">用于输入前缀的路由过滤器链名称。这发生在 NLRIs 被处理之后。如果未指定链，则 BGP 默认接受所有内容。</ArgTableRow>
<ArgTableRow arg="input.filter-nlri" typ="enum" unset="1">过滤器链的名称，用于在传入的 IPv4/IPv6 NLRIs 存储到内存之前直接过滤它们，从而显著减少内存使用。常规输入过滤器链只能拒绝前缀，这意味着它仍会占用内存，并将在 /routing route 表中显示为 "not active, filtered"。更改需要重启会话才能生效。</ArgTableRow>
<ArgTableRow arg="input.allow-as" typ="num" unset="1">指示在丢弃前缀之前，允许在 AS-PATH 中出现多少次您自己的 AS 编号。</ArgTableRow>
<ArgTableRow arg="input.accept-nlri" typ="enum" unset="1">ipv4/6 地址列表的名称。一种快速过滤具有特定 NLRIs 的传入更新的方法。它允许在传入消息被解析并存储到内存之前直接过滤它们，从而显著减少内存使用。常规输入过滤器链只能拒绝前缀，这意味着它仍会占用内存，并将在 /routing route 表中显示为 "not active, filtered"。更改需要重启会话才能生效。</ArgTableRow>
<ArgTableRow arg="input.filter-communities" typ="enum" unset="1">一种快速过滤具有特定 communities 的传入更新的方法。它允许在传入消息被解析并存储到内存之前直接过滤它们，从而显著减少内存使用。常规输入过滤器链只能拒绝前缀，这意味着它仍会占用内存，并将在 /routing route 表中显示为 "not active, filtered"。更改需要刷新会话才能生效。</ArgTableRow>
<ArgTableRow arg="input.filter-ext-communities" typ="enum" unset="1">一种快速过滤具有特定扩展 communities 的传入更新的方法。它允许在传入消息被解析并存储到内存之前直接过滤它们，从而显著减少内存使用。常规输入过滤器链只能拒绝前缀，这意味着它仍会占用内存，并将在 /routing route 表中显示为 "not active, filtered"。更改需要刷新会话才能生效。</ArgTableRow>
<ArgTableRow arg="input.filter-large-communities" typ="enum" unset="1">一种快速过滤具有特定大型 communities 的传入更新的方法。它允许在传入消息被解析并存储到内存之前直接过滤它们，从而显著减少内存使用。常规输入过滤器链只能拒绝前缀，这意味着它仍会占用内存，并将在 /routing route 表中显示为 "not active, filtered"。更改需要刷新会话才能生效。</ArgTableRow>
<ArgTableRow arg="input.accept-communities" typ="enum" unset="1">一种快速过滤具有特定 communities 的传入更新的方法。它允许在传入消息被解析并存储到内存之前直接过滤它们，从而显著减少内存使用。常规输入过滤器链只能拒绝前缀，这意味着它仍会占用内存，并将在 /routing route 表中显示为 "not active, filtered"。更改需要刷新会话才能生效。</ArgTableRow>
<ArgTableRow arg="input.accept-ext-communities" typ="enum" unset="1">一种快速过滤具有特定扩展 communities 的传入更新的方法。它允许在传入消息被解析并存储到内存之前直接过滤它们，从而显著减少内存使用。常规输入过滤器链只能拒绝前缀，这意味着它仍会占用内存，并将在 /routing route 表中显示为 "not active, filtered"。更改需要刷新会话才能生效。</ArgTableRow>
<ArgTableRow arg="input.accept-large-communities" typ="enum" unset="1">一种快速过滤具有特定大型 communities 的传入更新的方法。它允许在传入消息被解析并存储到内存之前直接过滤它们，从而显著减少内存使用。常规输入过滤器链只能拒绝前缀，这意味着它仍会占用内存，并将在 /routing route 表中显示为 "not active, filtered"。更改需要刷新会话才能生效。</ArgTableRow>
<ArgTableRow arg="input.filter-unknown" typ="enum" unset="1">一种快速过滤具有特定 "unknown" 属性的传入更新的方法。它允许在传入消息被解析并存储到内存之前直接过滤它们，从而显著减少内存使用。常规输入过滤器链只能拒绝前缀，这意味着它仍会占用内存，并将在 /routing route 表中显示为 "not active, filtered"。更改需要刷新会话才能生效。</ArgTableRow>
<ArgTableRow arg="input.limit-process-routes-ipv4" typ="enum (10 | 100 | 1000 | 10000 | 100000 | 1000000 | 10000000)" unset="1">尝试将接收到的 IPv4 路由数量限制为指定数量。此数字并不代表对等体将要在路由表中安装的确切路由数量。如果达到限制，必须使用 [BGP 会话 "clear"](#routingbgpsessionclear) 命令来重置标志。</ArgTableRow>
<ArgTableRow arg="input.limit-process-routes-ipv6" typ="enum (10 | 100 | 1000 | 10000 | 100000 | 