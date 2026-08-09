# Socksify

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/socksify

**类型：** 目录

完整文档请参阅 [Socksify](../../network-management/socks/socksify)。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">disabled（默认设置）</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string">Socksify 服务的名称</ArgTableRow>
<ArgTableRow arg="connection-timeout" typ="num">在连接建立期间，等待 SOCKS 代理或目标主机响应的秒数，超时后中止并报错。设置为 0 可禁用超时（默认值：**60秒**）</ArgTableRow>
<ArgTableRow arg="port" typ="num">Socksify 服务使用的 TCP 端口（默认值：**952**）</ArgTableRow>
<ArgTableRow arg="socks5-server" typ="ipAddr">SOCKS5 代理服务器的 IP 地址，仅支持 IPv4（默认值：**0.0.0.0**）</ArgTableRow>
<ArgTableRow arg="socks5-port" typ="num">SOCKS5 代理服务器的监听端口（默认值：**1080**）</ArgTableRow>
<ArgTableRow arg="socks5-user" typ="string">访问 SOCKS5 代理服务器的用户名</ArgTableRow>
<ArgTableRow arg="socks5-password" typ="string">访问 SOCKS5 代理服务器的密码</ArgTableRow>
</ArgTable>