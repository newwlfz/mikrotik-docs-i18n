# Pool（地址池）

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/pool

**类型：** 目录

IP 地址池用于定义一系列 IP 地址，可供 RouterOS 的各种功能使用，例如 DHCP 服务器、点对点服务器等。IPv4 和 IPv6 分别有独立的列表。在可能的情况下，系统会为每个客户端（OWNER/INFO 对）分配相同的 IP 地址。

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string">地址池的名称。</ArgTableRow>
<ArgTableRow arg="ranges" typ="multi { , , ipRange
 }" mandatory="1">不重叠的 IP 地址范围列表，格式为：`from1-to1,from2-to2,...,fromN-toN`。例如，`10.0.0.1-10.0.0.27,10.0.0.32-10.0.0.47`。</ArgTableRow>
<ArgTableRow arg="next-pool" typ="enum (none)">当从某个地址池获取 IP 地址时，如果该地址池没有空闲地址，且设置了 next-pool 属性，则会从下一个地址池中获取 IP 地址。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="total" typ="num"></ArgTableRow>
<ArgTableRow arg="used" typ="num"></ArgTableRow>
<ArgTableRow arg="available" typ="num"></ArgTableRow>
</ArgTable>

### ip/pool/used

**类型：** 目录

该菜单列出了所有从 IP 地址池中已使用的 IP 地址。

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="pool" typ="enum">IP 地址池的名称。</ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr">从地址池中分配给客户端的 IP 地址。</ArgTableRow>
<ArgTableRow arg="owner" typ="string">获取该 IP 地址的服务名称。</ArgTableRow>
<ArgTableRow arg="info" typ="string">附加信息，例如，对于 DHCP - 来自租约菜单的 MAC 地址；对于 PPP - PPP 类型客户端的连接用户名。</ArgTableRow>
</ArgTable>