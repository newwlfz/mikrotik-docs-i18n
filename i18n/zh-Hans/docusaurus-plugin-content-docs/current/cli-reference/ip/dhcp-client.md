# DHCP 客户端

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/dhcp-client

**软件包：** dhcp
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="add-default-route" typ="enum (no | yes | special-classless)"></ArgTableRow>
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
<ArgTableRow arg="use-peer-dns" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-peer-ntp" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow-reconfigure" typ="bool"></ArgTableRow>
<ArgTableRow arg="vlan-priority" typ="num">出站数据包的优先级；仅适用于 VLAN 接口</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">出站数据包的 DSCP</ArgTableRow>
<ArgTableRow arg="use-broadcast" typ="enum (always | never | both)">控制 DHCPDISCOVER 和 DHCPREQUEST（仅在请求和重新绑定阶段）消息的 BROADCAST 标志</ArgTableRow>
<ArgTableRow arg="dhcp-options" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="script" typ="alt { , string
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="custom-source-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="custom-hostname-suffix" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="enum (stopped | searching... | requesting... | bound | renewing... | rebinding... | error)"></ArgTableRow>
<ArgTableRow arg="address" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="netmask" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="gateway" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="dhcp-server" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="primary-dns" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="secondary-dns" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="primary-ntp" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="secondary-ntp" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="caps-managers" typ="multi { , ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="reconfigure-key" typ="string"></ArgTableRow>
<ArgTableRow arg="reconfigure-last-counter" typ="string"></ArgTableRow>
<ArgTableRow arg="expires-after" typ="time"></ArgTableRow>
</ArgTable>

### ip/dhcp-client/option

**软件包：** dhcp
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="code" typ="alt { num [1 .. 254]
, enum (hostname | vendor-specific | vendor-class-id | client-id) { hostname:12, vendor-specific:43, vendor-class-id:60, client-id:61 }
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="value" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="raw-value" typ="string"></ArgTableRow>
</ArgTable>

### ip/dhcp-client/release

**软件包：** dhcp
**类型：** 命令

### ip/dhcp-client/renew

**软件包：** dhcp
**类型：** 命令