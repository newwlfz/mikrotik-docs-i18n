# DNS

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/dns

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="servers" typ="multi { address (flags=46v)
 }"></ArgTableRow>
<ArgTableRow arg="use-doh-server" typ="string"></ArgTableRow>
<ArgTableRow arg="verify-doh-cert" typ="bool"></ArgTableRow>
<ArgTableRow arg="doh-max-server-connections" typ="num"></ArgTableRow>
<ArgTableRow arg="doh-max-concurrent-queries" typ="num"></ArgTableRow>
<ArgTableRow arg="doh-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="allow-remote-requests" typ="bool"></ArgTableRow>
<ArgTableRow arg="max-udp-packet-size" typ="num"></ArgTableRow>
<ArgTableRow arg="query-server-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="query-total-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="max-concurrent-queries" typ="num"></ArgTableRow>
<ArgTableRow arg="max-concurrent-tcp-sessions" typ="num"></ArgTableRow>
<ArgTableRow arg="cache-size" typ="num"></ArgTableRow>
<ArgTableRow arg="cache-max-ttl" typ="time"></ArgTableRow>
<ArgTableRow arg="address-list-extra-time" typ="time"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="mdns-repeat-ifaces" typ="multi { iface_enum
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="dynamic-servers" typ="multi { address (flags=46v)
 }"></ArgTableRow>
<ArgTableRow arg="cache-used" typ="num"></ArgTableRow>
</ArgTable>

### ip/dns/adlist

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="file" typ="file {  }"></ArgTableRow>
<ArgTableRow arg="url" typ="string"></ArgTableRow>
<ArgTableRow arg="ssl-verify" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="match-count" typ="num"></ArgTableRow>
<ArgTableRow arg="name-count" typ="num"></ArgTableRow>
</ArgTable>

#### ip/dns/adlist/pause

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="duration" typ="time"></ArgTableRow>
</ArgTable>

#### ip/dns/adlist/reload

**类型：** 命令

### ip/dns/cache

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="S" typ="static">静态</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="type" typ="enum (A | NS | CNAME | MX | TXT | AAAA | SRV)"></ArgTableRow>
<ArgTableRow arg="data" typ="alt { ipAddr
, string
, composite { ,  } { ,  }
, composite { ,  } { ,  }
, composite { ,  } { ,  }
, string
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="ttl" typ="time"></ArgTableRow>
</ArgTable>

#### ip/dns/cache/all

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="S" typ="static">静态</ArgTableRow>
<ArgTableRow arg="N" typ="negative">否定</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (A | NS | MD | MF | CNAME | SOA | MB | MG | MR | NULL | WKS | PTR | HINFO | MINFO | MX | TXT | AAAA | SRV)"></ArgTableRow>
<ArgTableRow arg="data" typ="alt { ipAddr
, string
, composite { ,  } { ,  }
, composite { ,  } { ,  }
, composite { ,  } { ,  }
, string
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="ttl" typ="time"></ArgTableRow>
<ArgTableRow arg="responsible" typ="string"></ArgTableRow>
<ArgTableRow arg="serial" typ="num"></ArgTableRow>
<ArgTableRow arg="refresh" typ="num"></ArgTableRow>
<ArgTableRow arg="retry" typ="num"></ArgTableRow>
<ArgTableRow arg="expire" typ="num"></ArgTableRow>
<ArgTableRow arg="minimum" typ="num"></ArgTableRow>
</ArgTable>

#### ip/dns/cache/flush

**类型：** 命令

### ip/dns/forwarders

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="dns-servers" typ="multi { address (flags=46D)
 }"></ArgTableRow>
<ArgTableRow arg="doh-servers" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="verify-doh-cert" typ="bool"></ArgTableRow>
</ArgTable>

### ip/dns/static

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="regexp" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (NXDOMAIN | A | NS | CNAME | MX | TXT | AAAA | SRV | FWD)"></ArgTableRow>
<ArgTableRow arg="forward-to" typ="alt { enum
, ipAddr
, ip6Addr
, string
 }"></ArgTableRow>
<ArgTableRow arg="address" typ="alt { ipAddr
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="mx-preference" typ="num"></ArgTableRow>
<ArgTableRow arg="mx-exchange" typ="string"></ArgTableRow>
<ArgTableRow arg="cname" typ="string"></ArgTableRow>
<ArgTableRow arg="text" typ="string"></ArgTableRow>
<ArgTableRow arg="ns" typ="string"></ArgTableRow>
<ArgTableRow arg="srv-priority" typ="num"></ArgTableRow>
<ArgTableRow arg="srv-weight" typ="num"></ArgTableRow>
<ArgTableRow arg="srv-port" typ="num"></ArgTableRow>
<ArgTableRow arg="srv-target" typ="string"></ArgTableRow>
<ArgTableRow arg="ttl" typ="time"></ArgTableRow>
<ArgTableRow arg="match-subdomain" typ="bool"></ArgTableRow>
<ArgTableRow arg="address-list" typ="string"></ArgTableRow>
</ArgTable>