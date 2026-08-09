# 过滤器

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/filter

**类型：** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="community" typ="alt { super { num [ .. 0xffff]
, :num [ .. 0xffff]
 } { num [ .. 0xffff]
, :num [ .. 0xffff]
 }
, enum (internet | graceful-shutdown | accept-own | route-filter-xlate-4 | route-filter-4 | route-filter-xlate-6 | route-filter-6 | llgr-stale | no-llgr | accept-own-nh | blackhole | no-export | no-advertise | no-export-subconfed | no-peer) { internet:r5fc1::WK_INTERNET, graceful-shutdown:r5fc1::WK_GRACEFUL_SHUTDOWN, accept-own:r5fc1::WK_ACCEPT_OWN, route-filter-xlate-4:r5fc1::WK_ROUTE_FILTER_XLATE_4, route-filter-4:r5fc1::WK_ROUTE_FILTER_4, route-filter-xlate-6:r5fc1::WK_ROUTE_FILTER_XLATE_6, route-filter-6:r5fc1::WK_ROUTE_FILTER_6, llgr-stale:r5fc1::WK_LLGR_STALE, no-llgr:r5fc1::WK_NO_LLGR, accept-own-nh:r5fc1::WK_ACCEPT_OWN_NH, blackhole:r5fc1::WK_BLACKHOLE, no-export:r5fc1::WK_NO_EXPORT, no-advertise:r5fc1::WK_NO_ADVERTISE, no-export-subconfed:r5fc1::WK_NO_EXPORT_SUBCONFED, no-peer:r5fc1::WK_NOPEER }
 }"></ArgTableRow>
<ArgTableRow arg="community" typ="alt { super { enum (rt | soo) { rt:r5fc2::VALUE_TYPE_RT, soo:r5fc2::VALUE_TYPE_SOO }
, :address (flags=R)
 } { enum (rt | soo) { rt:r5fc2::VALUE_TYPE_RT, soo:r5fc2::VALUE_TYPE_SOO }
, :address (flags=R)
 }
, num
 }"></ArgTableRow>
<ArgTableRow arg="community" typ="super { num
, :num
, :num
 }"></ArgTableRow>
</ArgTable>

### routing/filter/chain

**类型：** 目录

可在 BGP/OSPF 或其他路由协议配置中引用的过滤器规则链的动态列表。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="I" typ="inactive">非活动</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
</ArgTable>

### routing/filter/community-ext-list

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="list" typ="enum" mandatory="1">引用名称。</ArgTableRow>
<ArgTableRow arg="communities" typ="object {  }">
以**原始**整数值或类型化格式表示的扩展团体列表：`type:value`，其中 type 可以是：
- `rt` - 路由目标（route-target）
- `soo` - 源站点（site of origin）。

值取决于类型。
</ArgTableRow>
<ArgTableRow arg="regexp" typ="string">用于匹配团体的正则表达式匹配器。仅包含 regexp 参数的团体集不能用于追加/删除团体。</ArgTableRow>
</ArgTable>

### routing/filter/community-large-list

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="list" typ="enum" mandatory="1">引用名称。</ArgTableRow>
<ArgTableRow arg="communities" typ="object {  }">以以下格式表示的大型团体列表：`admin:value1:value2`，其中每个部分可以是整数 [0..4294967295]。</ArgTableRow>
<ArgTableRow arg="regexp" typ="string">用于匹配团体的正则表达式匹配器。仅包含 regexp 参数的团体集不能用于追加/删除团体。</ArgTableRow>
</ArgTable>

### routing/filter/community-list

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="list" typ="enum" mandatory="1">引用名称。</ArgTableRow>
<ArgTableRow arg="communities" typ="object {  }">
以**公认**名称或以下格式表示的团体列表：`as:number`，其中每个部分可以是整数 [0..65535]。
接受的**公认**名称：
- `accept-own`
- `graceful-shutdown`
- `no-advertise`
- `no-llgr`
- `route-filter-6`
- `accept-own-nh`
- `internet`
- `no-export`
- `no-peer`
- `route-filter-xlate-4`
- `blackhole`
- `llgr-stale`
- `local-as`
- `route-filter-4`
- `route-filter-xlate-6`
</ArgTableRow>
<ArgTableRow arg="regexp" typ="string">用于匹配团体的正则表达式匹配器。仅包含 regexp 参数的团体集不能用于追加/删除团体。</ArgTableRow>
</ArgTable>

### routing/filter/filter-wizard

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="chain" typ="enum"></ArgTableRow>
<ArgTableRow arg="dst" typ="super { !
, alt { enum
, address (flags=46/+)
 } { enum
, address (flags=46/+)
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="dst-len" typ="super { !
, range [ .. 128]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="gateway" typ="super { !
, alt { enum
, address (flags=46/+)
 } { enum
, address (flags=46/+)
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="match-chain" typ="super { !
, enum
 }" unset="1">如果提供的链未拒绝，则返回 true</ArgTableRow>
<ArgTableRow arg="routing-table" typ="super { !
, enum
 }" unset="1">路由被导入时所在路由表的名称</ArgTableRow>
<ArgTableRow arg="afi" typ="super { !
, ubit (ip, ipv6, l2vpn, vpnv4, vpnv6, l2vpn-cisco) { ip, ipv6, l2vpn, vpnv4, vpnv6, l2vpn-cisco }
 }" unset="1">路由的地址族</ArgTableRow>
<ArgTableRow arg="protocol" typ="super { !
, ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, slaac, bgp-mpls-vpn) { connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, slaac, bgp-mpls-vpn }
 }" unset="1">路由被导入时所用的协议类型</ArgTableRow>
<ArgTableRow arg="bgp-atomic-aggregate" typ="bool"></ArgTableRow>
<ArgTableRow arg="bgp-local-origin" typ="bool">如果前缀是本地起源的，例如 BGP network，则返回 true</ArgTableRow>
<ArgTableRow arg="suppress-hw-offload" typ="bool" syscap="crs_prestera"></ArgTableRow>
<ArgTableRow arg="use-te-nexthop" typ="bool"></ArgTableRow>
<ArgTableRow arg="blackhole" typ="bool">匹配黑洞路由</ArgTableRow>
<ArgTableRow arg="ospf-type" typ="super { !
, enum (intra | inter | ext1 | ext2 | nssa1 | nssa2) { intra:0, inter:1, ext1:2, ext2:3, nssa1:7, nssa2:8 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="rpki" typ="super { !
, enum (unknown | valid | invalid) { unknown:r5r::RPKI_UNKNOWN, valid:r5r::RPKI_VALID, invalid:r5r::RPKI_INVALID }
 }" unset="1">前缀的 RPKI 验证状态</ArgTableRow>
<ArgTableRow arg="bgp-origin" typ="super { !
, ubit (igp, egp, incomplete) { igp, egp, incomplete }
 }" unset="1">匹配 BGP Origin 属性</ArgTableRow>
<ArgTableRow arg="bgp-as-path" typ="string">匹配 BGP AS-Path 属性的正则表达式，详见文档</ArgTableRow>
<ArgTableRow arg="bgp-communities-match" typ="super { !
, enum () {  }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-communities" typ="object {  }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-communities-list-name" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-ext-communities-match" typ="super { !
, enum () {  }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-ext-communities" typ="object {  }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-ext-communities-list-name" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-large-communities-match" typ="super { !
, enum () {  }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-large-communities" typ="object {  }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-large-communities-list-name" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="distance" typ="super { !
, alt { enum
, range [ .. 255]
 } { enum
, range [ .. 255]
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="scope" typ="super { !
, alt { enum
, range [ .. 255]
 } { enum
, range [ .. 255]
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="scope-target" typ="super { !
, alt { enum
, range [ .. 255]
 } { enum
, range [ .. 255]
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-weight" typ="super { !
, alt { enum
, range [ .. 65535]
 } { enum
, range [ .. 65535]
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-local-pref" typ="super { !
, alt { enum
, range
 } { enum
, range
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-med" typ="super { !
, alt { enum
, range
 } { enum
, range
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-out-med" typ="super { !
, alt { enum
, range
 } { enum
, range
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-as-path-length" typ="super { !
, alt { enum
, range
 } { enum
, range
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="ospf-metric" typ="super { !
, alt { enum
, range
 } { enum
, range
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="set-distance" typ="alt { enum () {  }
, num [1 .. 255]
, composite { ,  } { ,  }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="set-scope" typ="alt { enum () {  }
, num [1 .. 255]
, composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="set-scope-target" typ="alt { enum () {  }
, num [1 .. 255]
, composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="set-bgp-weight" typ="alt { enum () {  }
, num [ .. 65535]
, composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="set-bgp-local-pref" typ="alt { enum () {  }
, num
, composite { ,  } { ,  }
 }">设置 BGP Local-Pref 属性的值</ArgTableRow>
<ArgTableRow arg="set-bgp-med" typ="alt { enum () {  }
, num
, composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="set-bgp-out-med" typ="alt { enum () {  }
, num
, composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="set-suppress-hw-offload" typ="bool" syscap="crs_prestera"></ArgTableRow>
<ArgTableRow arg="set-use-te-nexthop" typ="bool"></ArgTableRow>
<ArgTableRow arg="set-blackhole" typ="bool"></ArgTableRow>
<ArgTableRow arg="set-gw-check" typ="enum (none | arp | ping | bfd)">设置网关检查</ArgTableRow>
<ArgTableRow arg="set-gateway" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="set-comment" typ="string"></ArgTableRow>
<ArgTableRow arg="set-bgp-communities" typ="object {  }">设置 BGP Communities 属性的值</ArgTableRow>
<ArgTableRow arg="set-bgp-communities-list" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="set-bgp-ext-communities" typ="object {  }"></ArgTableRow>
<ArgTableRow arg="set-bgp-large-communities" typ="object {  }"></ArgTableRow>
<ArgTableRow arg="action" typ="enum ()" unset="1"></ArgTableRow>
<ArgTableRow arg="jump-target-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="rpki-verify" typ="enum" unset="1">在指定 RPKI 组的当前链中启用 RPKI 验证</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="result" typ="string"></ArgTableRow>
</ArgTable>

### routing/filter/num-list

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="list" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="range" typ="range"></ArgTableRow>
</ArgTable>

### routing/filter/rule

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">非活动</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="chain" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="rule" typ="remote"></ArgTableRow>
</ArgTable>

### routing/filter/select-rule

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="chain" typ="enum" unset="1" mandatory="1"></ArgTableRow>
<ArgTableRow arg="do-where" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="do-group-num" typ="super { enum () {  }
, >enum
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="do-group-prfx" typ="super { enum () {  }
, >enum
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="do-select-num" typ="super { enum () {  }
, >enum (largest-none-best | largest-none-worst | smallest-none-best | smallest-none-worst) { largest-none-best:r5srl::SELECT_CMP_LB, largest-none-worst:r5srl::SELECT_CMP_LW, smallest-none-best:r5srl::SELECT_CMP_SB, smallest-none-worst:r5srl::SELECT_CMP_SW }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="do-select-prfx" typ="super { enum () {  }
, >enum (largest-none-best | largest-none-worst | smallest-none-best | smallest-none-worst) { largest-none-best:r5srl::SELECT_CMP_LB, largest-none-worst:r5srl::SELECT_CMP_LW, smallest-none-best:r5srl::SELECT_CMP_SB, smallest-none-worst:r5srl::SELECT_CMP_SW }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="do-take" typ="num"></ArgTableRow>
<ArgTableRow arg="do-jump" typ="enum"></ArgTableRow>
</ArgTable>

### routing/filter/sync

**类型：** 命令

### routing/filter/test-as-path-regexp

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="regexp" typ="string"></ArgTableRow>
<ArgTableRow arg="as-path" typ="object { num
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="result" typ="string"></ArgTableRow>
</ArgTable>