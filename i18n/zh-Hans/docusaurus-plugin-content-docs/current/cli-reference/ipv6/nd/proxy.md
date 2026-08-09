# 代理

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### ipv6/nd/proxy

**软件包：** ipv6
**类型：** 目录

IPv6 邻居发现代理允许路由器或主机代表另一节点响应邻居发现（[RFC 4861](https://tools.ietf.org/html/rfc4861)）消息。这使得不同网络段之间的通信如同在同一链路上进行。在 RouterOS 中，代理可为单个 IPv6 地址启用，并按接口工作。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="address" typ="ip6Addr">代理所拥有的 IPv6 地址。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">代理针对此 IPv6 地址操作的接口。</ArgTableRow>
</ArgTable>