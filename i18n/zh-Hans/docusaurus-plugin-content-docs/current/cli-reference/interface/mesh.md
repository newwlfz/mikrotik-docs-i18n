# Mesh（网状网络）

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/mesh

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="R" typ="running">运行中</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string">名称</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">最大传输单元</ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp)">地址解析协议</ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { enum (auto) { auto:0 }
, time
 }">ARP 超时时间</ArgTableRow>
<ArgTableRow arg="auto-mac" typ="bool">自动 MAC 地址</ArgTableRow>
<ArgTableRow arg="admin-mac" typ="macAddr">管理 MAC 地址</ArgTableRow>
<ArgTableRow arg="mesh-portal" typ="bool">网状网络门户</ArgTableRow>
<ArgTableRow arg="hwmp-default-hoplimit" typ="num">HWMP 默认跳数限制</ArgTableRow>
<ArgTableRow arg="hwmp-preq-waiting-time" typ="time">HWMP PREQ 等待时间</ArgTableRow>
<ArgTableRow arg="hwmp-preq-retries" typ="num">HWMP PREQ 重试次数</ArgTableRow>
<ArgTableRow arg="hwmp-preq-destination-only" typ="bool">HWMP PREQ 仅限目的地</ArgTableRow>
<ArgTableRow arg="hwmp-preq-reply-and-forward" typ="bool">HWMP PREQ 回复并转发</ArgTableRow>
<ArgTableRow arg="hwmp-prep-lifetime" typ="time">HWMP PREP 生存时间</ArgTableRow>
<ArgTableRow arg="hwmp-rann-interval" typ="time">HWMP RANN 间隔</ArgTableRow>
<ArgTableRow arg="hwmp-rann-propagation-delay" typ="num">HWMP RANN 传播延迟</ArgTableRow>
<ArgTableRow arg="hwmp-rann-lifetime" typ="time">HWMP RANN 生存时间</ArgTableRow>
<ArgTableRow arg="reoptimize-paths" typ="bool">重新优化路径</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="mac-address" typ="macAddr">MAC 地址</ArgTableRow>
</ArgTable>

### interface/mesh/fdb

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="A" typ="active">活动</ArgTableRow>
<ArgTableRow arg="R" typ="root">根</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="mesh" typ="iface_enum">网状网络接口</ArgTableRow>
<ArgTableRow arg="type" typ="enum (local | outsider | direct | mesh | neighbor | larval | unknown)">类型</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">MAC 地址</ArgTableRow>
<ArgTableRow arg="on-interface" typ="iface_enum">所在接口</ArgTableRow>
<ArgTableRow arg="lifetime" typ="time">生存时间</ArgTableRow>
<ArgTableRow arg="age" typ="time">老化时间</ArgTableRow>
<ArgTableRow arg="metric" typ="num">度量值</ArgTableRow>
<ArgTableRow arg="seq-number" typ="num">序列号</ArgTableRow>
</ArgTable>

### interface/mesh/port

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">不活动</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">接口</ArgTableRow>
<ArgTableRow arg="mesh" typ="iface_enum" mandatory="1">网状网络接口</ArgTableRow>
<ArgTableRow arg="path-cost" typ="num">路径开销</ArgTableRow>
<ArgTableRow arg="hello-interval" typ="time">Hello 间隔</ArgTableRow>
<ArgTableRow arg="port-type" typ="enum (auto | WDS | wireless | ethernet)">端口类型</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="active-port-type" typ="enum (wireless | WDS | ethernet-mesh | ethernet-bridge | ethernet-mixed)">活动端口类型</ArgTableRow>
<ArgTableRow arg="dr-address" typ="macAddr">指定路由器地址</ArgTableRow>
</ArgTable>

### interface/mesh/traceroute

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="mesh" typ="iface_enum">网状网络接口</ArgTableRow>
<ArgTableRow arg="address" typ="macAddr">MAC 地址</ArgTableRow>
<ArgTableRow arg="hoplimit" typ="num">跳数限制</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="address" typ="macAddr">MAC 地址</ArgTableRow>
<ArgTableRow arg="time" typ="num">时间</ArgTableRow>
<ArgTableRow arg="status" typ="enum (success | ttl-exceeded | no-route | timeout)">状态</ArgTableRow>
</ArgTable>