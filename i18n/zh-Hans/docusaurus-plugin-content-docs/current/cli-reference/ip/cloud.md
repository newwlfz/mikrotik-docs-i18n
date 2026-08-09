# Cloud

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/cloud

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="ddns-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="ddns-update-interval" typ="alt { enum (none) { none:0 }
, time [1m .. ]
 }"></ArgTableRow>
<ArgTableRow arg="update-time" typ="bool"></ArgTableRow>
<ArgTableRow arg="back-to-home-vpn" typ="enum (revoked-and-disabled | enabled)" syscap="cloud-vpn"></ArgTableRow>
<ArgTableRow arg="vpn-prefer-relay-code" typ="string" syscap="cloud-vpn"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="public-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="public-address-ipv6" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="dns-name" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="vpn-dns-name" typ="string" syscap="cloud-vpn"></ArgTableRow>
<ArgTableRow arg="vpn-port" typ="num" syscap="cloud-vpn"></ArgTableRow>
<ArgTableRow arg="vpn-status" typ="string" syscap="cloud-vpn"></ArgTableRow>
<ArgTableRow arg="vpn-relay-rtts" typ="multi { string
 }" syscap="cloud-vpn"></ArgTableRow>
<ArgTableRow arg="vpn-relay-ipv4-status" typ="string" syscap="cloud-vpn"></ArgTableRow>
<ArgTableRow arg="vpn-relay-ipv6-status" typ="string" syscap="cloud-vpn"></ArgTableRow>
<ArgTableRow arg="vpn-relay-regions" typ="multi { string
 }" syscap="cloud-vpn"></ArgTableRow>
<ArgTableRow arg="vpn-relay-addressess" typ="multi { ipAddr
 }" syscap="cloud-vpn"></ArgTableRow>
<ArgTableRow arg="vpn-relay-addressess-ipv6" typ="multi { ip6Addr
 }" syscap="cloud-vpn"></ArgTableRow>
<ArgTableRow arg="vpn-private-key" typ="string" syscap="cloud-vpn"></ArgTableRow>
<ArgTableRow arg="vpn-public-key" typ="string" syscap="cloud-vpn"></ArgTableRow>
<ArgTableRow arg="vpn-peer-private-key" typ="string" syscap="cloud-vpn"></ArgTableRow>
<ArgTableRow arg="vpn-peer-public-key" typ="string" syscap="cloud-vpn"></ArgTableRow>
<ArgTableRow arg="vpn-interface" typ="iface_enum" syscap="cloud-vpn"></ArgTableRow>
<ArgTableRow arg="vpn-wireguard-client-config" typ="string" syscap="cloud-vpn"></ArgTableRow>
<ArgTableRow arg="vpn-wireguard-client-config-qrcode" typ="pic" syscap="cloud-vpn"></ArgTableRow>
<ArgTableRow arg="warning" typ="string"></ArgTableRow>
</ArgTable>

### ip/cloud/advanced

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="use-local-address" typ="bool"></ArgTableRow>
</ArgTable>

#### ip/cloud/app/update

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="ip4-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="ip6-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="ip4" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="ip6" typ="ip6Addr"></ArgTableRow>
</ArgTable>

### ip/cloud/back-to-home-file

**系统能力：** cloud-vpn
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="path" typ="file"></ArgTableRow>
<ArgTableRow arg="allow-uploads" typ="bool"></ArgTableRow>
<ArgTableRow arg="expires" typ="alt { enum (never) { never:0xFFFFFFFF }
, time
, date
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="key" typ="string"></ArgTableRow>
<ArgTableRow arg="url" typ="string"></ArgTableRow>
<ArgTableRow arg="direct-url" typ="string"></ArgTableRow>
<ArgTableRow arg="downloads" typ="num"></ArgTableRow>
</ArgTable>

#### ip/cloud/back-to-home-file/settings

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="prefer-relay-code" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="dns-name" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="relay-rtts" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="relay-ipv4-status" typ="string"></ArgTableRow>
<ArgTableRow arg="relay-ipv6-status" typ="string"></ArgTableRow>
<ArgTableRow arg="relay-regions" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="relay-addressess" typ="multi { ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="relay-addressess-ipv6" typ="multi { ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)"></ArgTableRow>
</ArgTable>

### ip/cloud/back-to-home-user

**系统能力：** cloud-vpn
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="A" typ="active">活动</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="expires" typ="alt { enum (never) { never:0xFFFFFFFF }
, time
, date
 }"></ArgTableRow>
<ArgTableRow arg="allow-lan" typ="bool"></ArgTableRow>
<ArgTableRow arg="private-key" typ="string"></ArgTableRow>
<ArgTableRow arg="public-key" typ="string"></ArgTableRow>
<ArgTableRow arg="file-access" typ="enum (disabled | read-only | full)"></ArgTableRow>
<ArgTableRow arg="file-access-path" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="client-address" typ="multi { address (flags=46/)
 }"></ArgTableRow>
<ArgTableRow arg="file-access-token" typ="string"></ArgTableRow>
</ArgTable>

#### ip/cloud/back-to-home-user/show-client-config

**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="conf" typ="string"></ArgTableRow>
<ArgTableRow arg="qr" typ="pic"></ArgTableRow>
</ArgTable>

### ip/cloud/force-update

**类型：** 命令