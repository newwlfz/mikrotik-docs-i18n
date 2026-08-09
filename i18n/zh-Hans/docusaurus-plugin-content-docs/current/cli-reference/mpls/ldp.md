# Ldp

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## mpls/ldp

**条件：** !smips
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="lsr-id" typ="ipAddr" unset="1">唯一的标签交换路由器ID。</ArgTableRow>
<ArgTableRow arg="path-vector-limit" typ="num" unset="1">用于环路检测的最大路径向量限制。与 `loop-detect` 属性配合使用。</ArgTableRow>
<ArgTableRow arg="hop-limit" typ="num" unset="1">用于环路检测的最大跳数限制。与 `loop-detect` 属性配合使用。</ArgTableRow>
<ArgTableRow arg="loop-detect" typ="bool" unset="1">定义是否运行LSP环路检测。如果未在所有LSR上启用，则无法正常工作。应仅用于非TTL网络，如ATM网络。</ArgTableRow>
<ArgTableRow arg="use-explicit-null" typ="bool" unset="1">是否分发显式空标签绑定。</ArgTableRow>
<ArgTableRow arg="distribute-for-default" typ="bool" unset="1">定义是否为默认路由映射标签。</ArgTableRow>
<ArgTableRow arg="transport-addresses" typ="multi { array-id, address (flags=46)
 }" unset="1">指定LDP会话连接的源地址，并将这些地址作为传输地址通告给LDP邻居。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1">此实例将操作的VRF表名称。</ArgTableRow>
<ArgTableRow arg="afi" typ="ubit (ip, ipv6)" unset="1">确定实例支持的地址族。</ArgTableRow>
<ArgTableRow arg="preferred-afi" typ="enum (ip | ipv6)" unset="1">确定首选哪个地址族连接。该值也会在双栈元素中设置（如果使用）。</ArgTableRow>
</ArgTable>

### mpls/ldp/accept-filter

**条件：** !smips
**类型：** 目录

应从LDP邻居接受的标签绑定列表。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="vrf" typ="enum (any)" unset="1"></ArgTableRow>
<ArgTableRow arg="prefix" typ="address (flags=46/)" unset="1">要匹配的前缀。</ArgTableRow>
<ArgTableRow arg="neighbor" typ="address (flags=46/)" unset="1">此过滤器适用的邻居。</ArgTableRow>
<ArgTableRow arg="accept" typ="bool" unset="1">是否接受来自邻居针对指定前缀的标签绑定。如果未设置参数，则匹配的前缀不被接受。</ArgTableRow>
</ArgTable>

### mpls/ldp/advertise-filter

**条件：** !smips
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="vrf" typ="enum (any)" unset="1"></ArgTableRow>
<ArgTableRow arg="prefix" typ="address (flags=46/)" unset="1">要匹配的前缀。</ArgTableRow>
<ArgTableRow arg="neighbor" typ="address (flags=46/)" unset="1">此过滤器适用的邻居。</ArgTableRow>
<ArgTableRow arg="advertise" typ="bool" unset="1">是否向邻居通告针对指定前缀的标签绑定。如果未设置参数，则匹配的前缀不被通告。</ArgTableRow>
</ArgTable>

### mpls/ldp/interface

**条件：** !smips
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="enum ()" mandatory="1">LDP将监听的接口或接口列表的名称。</ArgTableRow>
<ArgTableRow arg="hello-interval" typ="time" unset="1">路由器在指定接口上发送hello数据包的间隔。默认值为5秒。</ArgTableRow>
<ArgTableRow arg="hold-time" typ="time" unset="1">指定在接口上发现的邻居被声明为不可达的间隔。默认值为15秒。</ArgTableRow>
<ArgTableRow arg="transport-addresses" typ="multi { array-id, address (flags=46)
 }" unset="1">如果与LDP实例设置不同，则使用传输地址。</ArgTableRow>
<ArgTableRow arg="accept-dynamic-neighbors" typ="bool" unset="1">定义是动态发现邻居，还是仅使用LDP邻居菜单中静态配置的邻居。</ArgTableRow>
<ArgTableRow arg="afi" typ="ubit (ip, ipv6)" unset="1">确定接口地址族。仅考虑实例配置为支持的AFI。如果未明确指定值，则视为与实例支持的AFI相同。</ArgTableRow>
</ArgTable>

### mpls/ldp/local-mapping

**条件：** !smips
**类型：** 目录

此子菜单显示路由器本地绑定到路由的标签。如果无意动态使用LDP，也可以在此菜单中配置静态映射。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">绑定是否处于活动状态，并可被选为转发的候选。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">条目是否为动态添加。</ArgTableRow>
<ArgTableRow arg="E" typ="egress">出口</ArgTableRow>
<ArgTableRow arg="G" typ="gateway">目的地是否可通过网关到达。</ArgTableRow>
<ArgTableRow arg="L" typ="local">目的地是否在路由器本地可达。</ArgTableRow>
<ArgTableRow arg="V" typ="vpls">VPLS</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="vrf" typ="enum" unset="1">此映射所属的VRF表名称。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="address (flags=46/)" unset="1" mandatory="1">分配标签的目的前缀。</ArgTableRow>
<ArgTableRow arg="label" typ="alt { enum (expl-null | alert | expl-null6 | impl-null) { expl-null:0, alert:1, expl-null6:2, impl-null:3 }
, num [16 .. 1048576]
 }" mandatory="1">分配给目的地的标签编号。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="adv-path" typ="string"></ArgTableRow>
<ArgTableRow arg="peers" typ="object { composite { ,  } { ,  }
 }">此条目被通告到的对等体的IP地址和标签空间。</ArgTableRow>
<ArgTableRow arg="pw-fec" typ="string"></ArgTableRow>
</ArgTable>

### mpls/ldp/neighbor

**条件：** !smips
**类型：** 目录

已发现和静态配置的LDP邻居列表。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
<ArgTableRow arg="O" typ="operational">指示对等体是否处于可操作状态。</ArgTableRow>
<ArgTableRow arg="C" typ="active-connect">指示已选择主动角色，路由器正在尝试建立会话。</ArgTableRow>
<ArgTableRow arg="W" typ="passive-wait">指示对等体是否处于被动角色，当前正在等待会话初始化。</ArgTableRow>
<ArgTableRow arg="T" typ="throttled">指示会话是否处于节流状态。初始化失败后会话被节流，最大节流时间为120秒。</ArgTableRow>
<ArgTableRow arg="t" typ="sending-targeted-hello">是否正在向邻居发送定向hello。</ArgTableRow>
<ArgTableRow arg="v" typ="vpls">邻居是否被LDP信令的VPLS隧道使用。</ArgTableRow>
<ArgTableRow arg="p" typ="passive">指示对等体是否处于被动角色。</ArgTableRow>
<ArgTableRow arg="d" typ="on-demand">下游按需标签分发。</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="transport" typ="address (flags=46vi)" mandatory="1">远程传输地址。</ArgTableRow>
<ArgTableRow arg="send-targeted" typ="bool" unset="1">指定是否尝试发送定向hello，用于定向（非直连）LDP会话。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="peer" typ="object { composite { ,  } { ,  }
 }">邻居的LSR-ID和标签空间。</ArgTableRow>
<ArgTableRow arg="local-transport" typ="address (flags=46)">选定的本地传输地址。</ArgTableRow>
<ArgTableRow arg="addresses" typ="multi { array-id, address (flags=46)
 }">在邻居上发现的地址列表。</ArgTableRow>
<ArgTableRow arg="path-vector-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="on-demand" typ="bool">下游按需标签分发。</ArgTableRow>
<ArgTableRow arg="used-afi" typ="ubit (ip, ipv6)">使用的传输AFI。</ArgTableRow>
</ArgTable>

### mpls/ldp/remote-mapping

**条件：** !smips
**类型：** 目录

此子菜单显示从其他路由器接收的路由的标签绑定。如果无意动态使用LDP，可以配置静态映射。此表用于构建转发表。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">绑定是否处于活动状态，并可被选为转发的候选。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">条目是否为动态添加。</ArgTableRow>
<ArgTableRow arg="V" typ="vpls">VPLS</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="vrf" typ="enum" unset="1">此映射所属的VRF表名称。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="address (flags=46/)" mandatory="1">分配标签的目的前缀。</ArgTableRow>
<ArgTableRow arg="label" typ="alt { enum (expl-null | alert | expl-null6 | impl-null) { expl-null:0, alert:1, expl-null6:2, impl-null:3 }
, num [16 .. 1048576]
 }" mandatory="1">分配给目的地的标签编号。</ArgTableRow>
<ArgTableRow arg="nexthop" typ="address (flags=46i)" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="peer" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="path" typ="string"></ArgTableRow>
<ArgTableRow arg="pw-fec" typ="string"></ArgTableRow>
</ArgTable>