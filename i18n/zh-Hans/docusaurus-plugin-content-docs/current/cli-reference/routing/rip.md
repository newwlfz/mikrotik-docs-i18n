# RIP

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/rip

**类型：** 目录

### routing/rip/instance

**类型：** 目录

RIP 路由的最大度量值为 15。度量值大于 15 被视为“无穷大”，具有此类度量值的路由被视为不可达。因此，RIP 不能用于任意两台路由器之间跳数超过 15 的网络，并且使用大于 1 的重分发度量值会进一步减小此最大跳数。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string">实例的名称。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">用于连接的 VRF 名称。</ArgTableRow>
<ArgTableRow arg="afi" typ="enum (ip | ipv6)"></ArgTableRow>
<ArgTableRow arg="in-filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="out-filter-select" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="out-filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="redistribute" typ="ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, bgp-mpls-vpn, slaac)" unset="1"></ArgTableRow>
<ArgTableRow arg="originate-default" typ="enum (never | always | if-installed)" unset="1">是否生成默认路由。</ArgTableRow>
<ArgTableRow arg="route-timeout" typ="num">指定路由被视为无效的时间间隔。</ArgTableRow>
<ArgTableRow arg="route-gc-timeout" typ="num"></ArgTableRow>
<ArgTableRow arg="update-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="routing-table" typ="enum" unset="1">路由将被安装到的路由表名称。</ArgTableRow>
</ArgTable>

### routing/rip/interface

**类型：** 目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="bfd" typ="bool"></ArgTableRow>
</ArgTable>

### routing/rip/interface-template

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="instance" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="interfaces" typ="object { iface_enum {  } {  }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="source-addresses" typ="object { address (flags=46)
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="cost" typ="num"></ArgTableRow>
<ArgTableRow arg="split-horizon" typ="bool"></ArgTableRow>
<ArgTableRow arg="poison-reverse" typ="bool"></ArgTableRow>
<ArgTableRow arg="key-chain" typ="enum" unset="1">包含 MD5 密钥的密钥链名称。仅在需要 MD5 认证时设置。</ArgTableRow>
<ArgTableRow arg="password" typ="string" unset="1">明文认证的密码。仅在需要明文认证时设置。</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (passive | strict)" unset="1"></ArgTableRow>
<ArgTableRow arg="use-bfd" typ="bool" unset="1"></ArgTableRow>
</ArgTable>

### routing/rip/keys

**类型：** 目录

MD5 认证密钥链。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="chain" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="key-id" typ="num" mandatory="1">密钥标识符。此编号包含在 MD5 认证的 RIP 消息中，并决定使用哪个密钥来验证特定消息的认证。</ArgTableRow>
<ArgTableRow arg="key" typ="string" mandatory="1">认证密钥。最大长度为 16 个字符。</ArgTableRow>
<ArgTableRow arg="valid-from" typ="date">密钥自此日期和时间起有效。</ArgTableRow>
<ArgTableRow arg="valid-till" typ="date">密钥有效至该日期和时间。</ArgTableRow>
</ArgTable>

### routing/rip/neighbor

**类型：** 目录

此子菜单用于定义交换路由信息的邻居路由器。通常，如果网络内组播工作正常，则无需添加邻居。如果交换路由信息时出现问题，可以将邻居路由器添加到列表中。这将强制路由器使用常规单播数据包与邻居交换路由信息。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="routes" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-total" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-bad" typ="num"></ArgTableRow>
<ArgTableRow arg="entries-bad" typ="num"></ArgTableRow>
<ArgTableRow arg="last-update" typ="time">距上次更新的时间。</ArgTableRow>
</ArgTable>

### routing/rip/static-neighbor

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)"></ArgTableRow>
</ArgTable>