# L2TP 以太网

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/l2tp-ether

**软件包：** ppp
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="R" typ="running">运行中</ArgTableRow>
<ArgTableRow arg="u" typ="unmanaged">非托管</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="connect-to" typ="address (flags=D46v)"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="use-ipsec" typ="bool {  }">被动（传入）连接忽略此参数（对于传入连接，请使用 l2tp-server 设置）</ArgTableRow>
<ArgTableRow arg="ipsec-secret" typ="string {  }">被动（传入）连接忽略此参数（对于传入连接，请使用 l2tp-server 设置）</ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool"></ArgTableRow>
<ArgTableRow arg="l2tp-proto-version" typ="enum (l2tpv3-ip | l2tpv3-udp)">L2TPv3 封装模式（IP 或 UDP）</ArgTableRow>
<ArgTableRow arg="circuit-id" typ="string">L2TPv3 远端标识符（虚拟电路 ID）</ArgTableRow>
<ArgTableRow arg="cookie-length" typ="enum (0 | 4-bytes | 8-bytes)">被动（传入）连接忽略此参数（对于传入连接，请使用 l2tp-server 设置）</ArgTableRow>
<ArgTableRow arg="digest-hash" typ="enum (none | md5 | sha1)">被动（传入）连接忽略此参数（对于传入连接，请使用 l2tp-server 设置）</ArgTableRow>
<ArgTableRow arg="use-l2-specific-sublayer" typ="bool">启用 L2TPv3 以太网伪线第 2 层默认子层</ArgTableRow>
<ArgTableRow arg="local-address" typ="alt { ipAddr
, ip6Addr
,  }">本地 IPv4 或 IPv6 地址（非托管 L2TP 连接）</ArgTableRow>
<ArgTableRow arg="local-tunnel-id" typ="num {  }">本地隧道 ID（非托管 L2TP 连接）</ArgTableRow>
<ArgTableRow arg="local-session-id" typ="num {  }">本地会话 ID（非托管 L2TP 连接）</ArgTableRow>
<ArgTableRow arg="remote-tunnel-id" typ="num {  }">远端隧道 ID（非托管 L2TP 连接）</ArgTableRow>
<ArgTableRow arg="remote-session-id" typ="num {  }">远端会话 ID（非托管 L2TP 连接）</ArgTableRow>
<ArgTableRow arg="peer-cookie" typ="string {  }">接收数据包的 cookie 十六进制值（8 或 16 个字符，或为空）（非托管 L2TP 连接）</ArgTableRow>
<ArgTableRow arg="send-cookie" typ="string {  }">发送数据包的 cookie 十六进制值（8 或 16 个字符，或为空）（非托管 L2TP 连接）</ArgTableRow>
<ArgTableRow arg="unmanaged-mode" typ="bool {  }">启用/禁用非托管（静态）隧道模式</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="actual-mtu" typ="num"></ArgTableRow>
</ArgTable>

### interface/l2tp-ether/monitor

**软件包：** ppp
**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="circuit-id" typ="string"></ArgTableRow>
<ArgTableRow arg="cookie-length" typ="num"></ArgTableRow>
<ArgTableRow arg="header-format" typ="string"></ArgTableRow>
<ArgTableRow arg="l2-sublayer" typ="bool"></ArgTableRow>
<ArgTableRow arg="remote-sess-id" typ="num"></ArgTableRow>
<ArgTableRow arg="local-sess-id" typ="num"></ArgTableRow>
<ArgTableRow arg="control-conn-id" typ="num"></ArgTableRow>
<ArgTableRow arg="peer-address" typ="string"></ArgTableRow>
<ArgTableRow arg="encoding" typ="string"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
</ArgTable>