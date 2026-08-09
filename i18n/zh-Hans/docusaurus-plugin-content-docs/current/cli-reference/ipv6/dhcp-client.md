# DHCP 客户端

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ipv6/dhcp-client

**软件包：** dhcp
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="request" typ="ubit (info, address, prefix)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="accept-prefix-without-address" typ="bool">即使未提供地址也接受前缀（仅当同时请求地址和前缀时适用）</ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool">定义是否向 DHCP 服务器（或响应被中继时的直接中继）添加默认路由</ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="default-route-tables" typ="object { alt { composite { ,  } { ,  }
, alt { enum (default) { default:0xffffffff }
, enum
 } { enum (default) { default:0xffffffff }
, enum
 }
 } { composite { ,  } { ,  }
, alt { enum (default) { default:0xffffffff }
, enum
 } { enum (default) { default:0xffffffff }
, enum
 }
 }
 }"></ArgTableRow>
<ArgTableRow arg="check-gateway" typ="enum (none | arp | ping | bfd)"></ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="bool">是否接受 DHCP 服务器通告的 DNS 设置</ArgTableRow>
<ArgTableRow arg="use-interface-duid" typ="bool">使用根据当前接口 MAC 生成的 DUID</ArgTableRow>
<ArgTableRow arg="custom-duid" typ="string">用作客户端 DUID，覆盖 use-interface-duid</ArgTableRow>
<ArgTableRow arg="validate-server-duid" typ="bool"></ArgTableRow>
<ArgTableRow arg="rapid-commit" typ="bool">尽可能使用快速提交（Rapid Commit）</ArgTableRow>
<ArgTableRow arg="allow-reconfigure" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcp-options" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="pool-name" typ="string">从接收到的前缀创建的地址池名称（仅当请求前缀时适用）</ArgTableRow>
<ArgTableRow arg="pool-prefix-length" typ="num">从接收到的前缀创建的地址池前缀长度（仅当请求前缀时适用）；若未设置，则自动确定前缀长度</ArgTableRow>
<ArgTableRow arg="prefix-hint" typ="ip6Prefix"></ArgTableRow>
<ArgTableRow arg="prefix-address-lists" typ="multi { array-id, string
 }">接收到的前缀将被添加到的地址列表（仅当请求前缀时适用）</ArgTableRow>
<ArgTableRow arg="script" typ="alt { , string
 }"></ArgTableRow>
<ArgTableRow arg="custom-iapd-id" typ="num"></ArgTableRow>
<ArgTableRow arg="custom-iana-id" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="enum (stopped | searching... | requesting... | bound | renewing... | rebinding... | stopping... | declining... | error | idle | requesting-info... | confirming...)"></ArgTableRow>
<ArgTableRow arg="duid" typ="string"></ArgTableRow>
<ArgTableRow arg="dhcp-server-v6" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="prefix" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="address" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="reconfigure-key" typ="string"></ArgTableRow>
<ArgTableRow arg="reconfigure-last-counter" typ="string"></ArgTableRow>
</ArgTable>

### ipv6/dhcp-client/option

**软件包：** dhcp
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="code" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="value" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="raw-value" typ="string"></ArgTableRow>
</ArgTable>

### ipv6/dhcp-client/release

**软件包：** dhcp
**类型：** 命令

### ipv6/dhcp-client/renew

**软件包：** dhcp
**类型：** 命令