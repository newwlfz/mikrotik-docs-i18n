# 前缀

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### ipv6/nd/prefix

**软件包：** ipv6
**类型：** 目录

用于无状态地址自动配置的路由器通告（RA）消息中发送的前缀信息（[RFC 4862](https://tools.ietf.org/html/rfc4862)）。默认情况下，自动配置仅适用于主机，不适用于路由器。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="prefix" typ="alt { enum (none) { none:0 }
, ip6Prefix
 }">用于无状态地址自动配置的前缀。如果选择“none”选项，RouterOS 仅通告选项，不包含特定前缀。</ArgTableRow>
<ArgTableRow arg="6to4-interface" typ="iface_enum { none:0xffffffff }">如果设置，RouterOS 将此前缀与接口的 IPv4 地址组合，以生成有效的 6to4 前缀。RouterOS 将前 16 位替换为 2002，并将接下来的 32 位替换为接口配置的 IPv4 地址。其余 80 位（包括 SLA ID）按配置进行通告。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">运行无状态自动配置的接口。</ArgTableRow>
<ArgTableRow arg="on-link" typ="bool">设置后，表示 RouterOS 可以将此前缀视为在链路上。未设置时，RA 消息不对前缀的在链路或离链路状态作任何声明。此前缀仍可能用于地址配置，而前缀中的某些地址保持离链路状态。</ArgTableRow>
<ArgTableRow arg="autonomous" typ="bool">设置后，表示 RouterOS 可以使用此前缀进行自主地址配置。否则，RouterOS 将忽略此前缀信息。</ArgTableRow>
<ArgTableRow arg="dhcp6-pd-preferred" typ="bool">表示客户端应根据 [RFC 9762](https://datatracker.ietf.org/doc/rfc9762/) 使用 DHCPv6 前缀委派。</ArgTableRow>
<ArgTableRow arg="valid-lifetime" typ="alt { enum (infinity) { infinity:0xffffffff }
, time
 }">数据包发送后地址保持有效的时间长度。有效生命周期必须大于或等于首选生命周期。[`了解更多 >>`](../../../getting-started/networking-fundamentals/ipv6-neighbor-discovery.md#address-states)</ArgTableRow>
<ArgTableRow arg="preferred-lifetime" typ="alt { enum (infinity) { infinity:0xffffffff }
, time
 }">数据包发送后生成的地址变为弃用的时间。弃用地址仅用于现有连接，并保持可用直到有效生命周期到期。[`了解更多 >>`](../../../getting-started/networking-fundamentals/ipv6-neighbor-discovery.md#address-states)</ArgTableRow>
</ArgTable>

#### ipv6/nd/prefix/default

**软件包：** ipv6
**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="autonomous" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcp6-pd-preferred" typ="bool"></ArgTableRow>
<ArgTableRow arg="valid-lifetime" typ="alt { enum (infinity) { infinity:0xffffffff }
, time
 }"></ArgTableRow>
<ArgTableRow arg="preferred-lifetime" typ="alt { enum (infinity) { infinity:0xffffffff }
, time
 }"></ArgTableRow>
</ArgTable>