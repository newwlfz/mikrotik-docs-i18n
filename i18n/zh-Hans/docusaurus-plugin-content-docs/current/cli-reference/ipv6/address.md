# 地址

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ipv6/address

**软件包：** ipv6
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="G" typ="global">全局</ArgTableRow>
<ArgTableRow arg="L" typ="link-local">链路本地</ArgTableRow>
<ArgTableRow arg="S" typ="slave">地址是否属于某个作为其他主接口从属端口的接口。</ArgTableRow>
<ArgTableRow arg="d" typ="deprecated">已弃用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="address" typ="composite { ,  }">
IPv6 地址。如果指定了 `from-pool` 参数，地址也可以从地址池中构建。
例如，如果地址设置为 `::1/64`，则地址将按如下方式构建 `<prefix_from_pool>::1/64`
</ArgTableRow>
<ArgTableRow arg="from-pool" typ="enum">地址池的名称，将从该池中获取前缀，以构建 IPv6 地址，地址的最后部分取自 address 属性。</ArgTableRow>
<ArgTableRow arg="from-pool-policy" typ="enum (recommended | strict | without-acquire)">
指定如何从地址池获取前缀，如果设置了 `from-pool` 参数。

- `recommended` 选项将使用 `address` 作为后缀，并在提供 subnet-id 时使用 **subnet-id**。
- `strict` 将使用 **address** 作为严格后缀。
- `without-acquire` 将不会从地址池分配前缀，并允许其他服务使用完全相同的前缀。`without-acquire` 选项主要应用于在路由器上创建 SLAAC 地址，同时该路由器也作为 DHCPv6 服务器，从同一子网向客户端提供地址。
</ArgTableRow>

<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">指定配置 IPv6 地址的接口。您可以从路由器上可用的接口池中选择。</ArgTableRow>
<ArgTableRow arg="eui-64" typ="bool">是否计算 EUI-64 地址并将其用作 IPv6 地址的最后 64 位。</ArgTableRow>
<ArgTableRow arg="advertise" typ="bool">是否启用无状态地址配置。该地址的前缀会自动通过 ICMPv6 协议向主机通告三次。对于前缀长度为 64 的地址，此选项默认设置。如果地址被移除或更改，则旧前缀将通过 ICMPv6 协议自动向主机通告三次，且生命周期设置为 `0s`，从而使旧前缀被弃用。</ArgTableRow>
<ArgTableRow arg="no-dad" typ="bool">如果启用（是）- 禁用接口上 IPv6 地址的重复地址检测（DAD）。这在您希望为设备分配静态 IPv6 地址并避免 DAD 造成的延迟时非常有用。</ArgTableRow>
<ArgTableRow arg="auto-link-local" typ="bool">如果您想手动向接口添加链路本地地址，此设置允许您覆盖自动生成的 IPv6 链路本地地址。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="actual-interface" typ="iface_enum">地址实际配置所在的接口。例如，如果地址配置在以太网接口上，且该以太网接口已添加到桥接中，则实际接口是桥接而非以太网。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">指示此 IP 地址关联到哪个 VRF。</ArgTableRow>
<ArgTableRow arg="valid" typ="alt { enum (forever) { forever:-1 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="preferred" typ="alt { enum (forever) { forever:-1 }
, time
 }"></ArgTableRow>
</ArgTable>