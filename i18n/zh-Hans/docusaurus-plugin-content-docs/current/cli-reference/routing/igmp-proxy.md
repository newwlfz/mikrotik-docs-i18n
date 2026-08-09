# IGMP 代理

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/igmp-proxy

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="quick-leave" typ="bool">指定对 IGMP Leave 消息的处理动作。如果启用了 quick-leave，则一旦从下游接口的第一个客户端收到 Leave 消息，就会立即向上游发送 IGMP Leave 消息。仅在代理后面只有一个订阅者时使用 `yes`。</ArgTableRow>
<ArgTableRow arg="query-interval" typ="time">通过下游接口发送 IGMP Query 消息的频率。</ArgTableRow>
<ArgTableRow arg="query-response-interval" typ="time">等待 IGMP Query 消息响应的最长时间。</ArgTableRow>
</ArgTable>

### routing/igmp-proxy/interface

**类型：** 目录

配置哪些接口将作为路由器上的 IGMP 代理接口参与。如果某个接口未配置为 IGMP 代理接口，则在该接口上接收到的所有 IGMP 流量都将被忽略。

可以使用 `print status` 命令获取每个接口的详细状态信息。

```ros
[admin@MikroTik] /routing/igmp-proxy/interface/print status 
Flags: X - disabled, I - inactive, D - dynamic; U - upstream 
 0  U interface=ether2 threshold=1 alternative-subnets="" upstream=yes source-ip-address=192.168.10.10 rx-bytes=3018487500 rx-packets=2012325 tx-bytes=0 tx-packets=0 

 1    interface=ether3 threshold=1 alternative-subnets="" upstream=no querier=yes source-ip-address=192.168.20.10 rx-bytes=0 rx-packets=0 tx-bytes=2973486000 tx-packets=1982324 

 2    interface=ether4 threshold=1 alternative-subnets="" upstream=no querier=yes source-ip-address=192.168.30.10 rx-bytes=0 rx-packets=0 tx-bytes=152019000 tx-packets=101346 
```

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="U" typ="upstream">上游</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum { all:0 }">接口名称。</ArgTableRow>
<ArgTableRow arg="threshold" typ="num">最小 TTL 值。接收到的 TTL 值低于此值的数据包将被忽略。</ArgTableRow>
<ArgTableRow arg="alternative-subnets" typ="multi { , , super { ipAddr
, /num
 } { ipAddr
, /num
 }
 }">默认情况下，仅接受来自直接连接子网的数据包。此参数可用于指定备选的有效数据包源子网列表，适用于数据和 IGMP 数据包。仅对上游接口有效。当组播数据源通常位于不同 IP 网络中时应使用此参数。</ArgTableRow>
<ArgTableRow arg="upstream" typ="bool">如果接口朝向组播树的根方向，则称为“上游”接口。IGMP 转发路由器必须且只能配置一个上游接口。上游接口用于发送 IGMP 成员资格请求。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="querier" typ="bool">该接口是否充当 IGMP 查询器。</ArgTableRow>
<ArgTableRow arg="source-ip-address" typ="ipAddr">检测到的接口源 IP 地址。</ArgTableRow>
<ArgTableRow arg="rx-bytes" typ="num">接口上接收到的组播流量总量。</ArgTableRow>
<ArgTableRow arg="rx-packets" typ="num">接口上接收到的组播数据包总量。</ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="num">接口上发送的组播流量总量。</ArgTableRow>
<ArgTableRow arg="tx-packets" typ="num">接口上发送的组播数据包总量。</ArgTableRow>
</ArgTable>

### routing/igmp-proxy/mfc

**类型：** 目录

组播转发缓存（MFC）状态。

RouterOS 支持 IGMP 代理的静态组播转发规则。如果添加了静态规则，则该组的所有动态规则将被忽略。这些规则仅在配置了 IGMP 代理接口（应设置上游和下游接口）时才会生效，否则这些规则将不会激活。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="A" typ="active">已激活</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="group" typ="ipAddr" mandatory="1">此规则适用的组播组地址。</ArgTableRow>
<ArgTableRow arg="source" typ="ipAddr" mandatory="1">组播数据源地址。</ArgTableRow>
<ArgTableRow arg="upstream-interface" typ="iface_enum" mandatory="1">接收流数据的接口。</ArgTableRow>
<ArgTableRow arg="downstream-interfaces" typ="multi { iface_enum
 }">接收到的流将仅发送到列出的接口。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="active-downstream-interfaces" typ="multi { iface_enum
 }">数据流通过此接口从路由器发出。</ArgTableRow>
<ArgTableRow arg="bytes" typ="num">接收到的组播流量总量。</ArgTableRow>
<ArgTableRow arg="packets" typ="num">接收到的组播数据包总量。</ArgTableRow>
<ArgTableRow arg="wrong-packets" typ="num">在错误接口上接收到的组播数据包总量，例如，在某个下游接口上接收到组播流，而不是在上游接口上接收到。</ArgTableRow>
</ArgTable>