# OVPN 客户端

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/ovpn-client

**软件包：** ppp
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="R" typ="running">运行中</ArgTableRow>
<ArgTableRow arg="H" typ="hw-crypto">硬件加密</ArgTableRow>
<ArgTableRow arg="Ta" typ="tls-auth">TLS 认证</ArgTableRow>
<ArgTableRow arg="Tc" typ="tls-crypt">TLS 加密</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="connect-to" typ="address (flags=D46v)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (ip | ethernet)"></ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (tcp | udp)"></ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="verify-server-certificate" typ="bool"></ArgTableRow>
<ArgTableRow arg="tls-version" typ="enum (any | only-1.2)"></ArgTableRow>
<ArgTableRow arg="auth" typ="enum (sha1 | md5 | sha256 | sha384 | sha512 | null)"></ArgTableRow>
<ArgTableRow arg="cipher" typ="enum (blowfish128 | aes128-cbc | aes192-cbc | aes256-cbc | aes128-gcm | aes192-gcm | aes256-gcm | null)"></ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="enum (no | yes | exclusively)"></ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool"></ArgTableRow>
<ArgTableRow arg="route-nopull" typ="bool">如果启用，客户端将不会使用服务器推送的任何路由（包括 def1）</ArgTableRow>
<ArgTableRow arg="disconnect-notify" typ="bool {  }">在使用 UDP 模式时发送显式断开通知</ArgTableRow>
</ArgTable>

### interface/ovpn-client/import-ovpn-configuration

**软件包：** ppp
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="file-name" typ="file">.ovpn 客户端配置文件</ArgTableRow>
<ArgTableRow arg="skip-cert-import" typ="bool">忽略 ovpn 文件中的证书信息，以防这些信息由用户手动添加</ArgTableRow>
<ArgTableRow arg="key-passphrase" typ="string"></ArgTableRow>
<ArgTableRow arg="ovpn-user" typ="string"></ArgTableRow>
<ArgTableRow arg="ovpn-password" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="progress" typ="string"></ArgTableRow>
</ArgTable>

### interface/ovpn-client/monitor

**软件包：** ppp
**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="encoding" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="local-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="remote-address" typ="ipAddr"></ArgTableRow>
</ArgTable>