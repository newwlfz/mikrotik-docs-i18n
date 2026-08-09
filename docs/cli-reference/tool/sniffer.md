# Sniffer

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/sniffer

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="only-headers" typ="bool"></ArgTableRow>
<ArgTableRow arg="memory-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="memory-scroll" typ="bool"></ArgTableRow>
<ArgTableRow arg="file-name" typ="file"></ArgTableRow>
<ArgTableRow arg="file-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="streaming-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="streaming-server" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="max-packet-size" typ="num"></ArgTableRow>
<ArgTableRow arg="filter-stream" typ="bool"></ArgTableRow>
<ArgTableRow arg="filter-interface" typ="object { iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="filter-mac-address" typ="object { super { !
, composite { ,  } { ,  }
 } { !
, composite { ,  } { ,  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="filter-src-mac-address" typ="object { super { !
, composite { ,  } { ,  }
 } { !
, composite { ,  } { ,  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="filter-dst-mac-address" typ="object { super { !
, composite { ,  } { ,  }
 } { !
, composite { ,  } { ,  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="filter-mac-protocol" typ="object { super { !
, alt { enum () {  }
, num [ .. 65535]
 } { enum () {  }
, num [ .. 65535]
 }
 } { !
, alt { enum () {  }
, num [ .. 65535]
 } { enum () {  }
, num [ .. 65535]
 }
 }
 }"></ArgTableRow>
<ArgTableRow arg="filter-ip-address" typ="object { super { !
, composite { ,  } { ,  }
 } { !
, composite { ,  } { ,  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="filter-src-ip-address" typ="object { super { !
, composite { ,  } { ,  }
 } { !
, composite { ,  } { ,  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="filter-dst-ip-address" typ="object { super { !
, composite { ,  } { ,  }
 } { !
, composite { ,  } { ,  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="filter-ipv6-address" typ="object { super { !
, ip6Prefix
 } { !
, ip6Prefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="filter-src-ipv6-address" typ="object { super { !
, ip6Prefix
 } { !
, ip6Prefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="filter-dst-ipv6-address" typ="object { super { !
, ip6Prefix
 } { !
, ip6Prefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="filter-ip-protocol" typ="object { super { !
, enum () {  }
 } { !
, enum () {  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="filter-port" typ="object { super { !
, enum () {  }
 } { !
, enum () {  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="filter-src-port" typ="object { super { !
, enum () {  }
 } { !
, enum () {  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="filter-dst-port" typ="object { super { !
, enum () {  }
 } { !
, enum () {  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="filter-vlan" typ="object { super { !
, num [ .. 4095]
 } { !
, num [ .. 4095]
 }
 }"></ArgTableRow>
<ArgTableRow arg="filter-cpu" typ="object { super { !
, num
 } { !
, num
 }
 }"></ArgTableRow>
<ArgTableRow arg="filter-size" typ="object { super { !
, range [0 .. 65535]
 } { !
, range [0 .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="filter-direction" typ="enum (any | tx | rx)"></ArgTableRow>
<ArgTableRow arg="filter-operator-between-entries" typ="enum (or | and)"></ArgTableRow>
<ArgTableRow arg="quick-rows" typ="num"></ArgTableRow>
<ArgTableRow arg="quick-show-frame" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="running" typ="bool"></ArgTableRow>
</ArgTable>

### tool/sniffer/connection

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="A" typ="active">active</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="src-address" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="bytes" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="resends" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="mss" typ="composite { ,  }"></ArgTableRow>
</ArgTable>

### tool/sniffer/host

**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="rate" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="peak-rate" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="total" typ="composite { ,  }"></ArgTableRow>
</ArgTable>

### tool/sniffer/packet

**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="time" typ="num"></ArgTableRow>
<ArgTableRow arg="num" typ="num"></ArgTableRow>
<ArgTableRow arg="direction" typ="enum (rx | tx)"></ArgTableRow>
<ArgTableRow arg="src-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="dst-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="vlan" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="src-address" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="protocol" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="enum (ip)"></ArgTableRow>
<ArgTableRow arg="size" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu" typ="num"></ArgTableRow>
<ArgTableRow arg="ip-packet-size" typ="num"></ArgTableRow>
<ArgTableRow arg="ip-header-size" typ="num"></ArgTableRow>
<ArgTableRow arg="dscp" typ="num"></ArgTableRow>
<ArgTableRow arg="ecn" typ="num"></ArgTableRow>
<ArgTableRow arg="identification" typ="num"></ArgTableRow>
<ArgTableRow arg="fragment-offset" typ="num"></ArgTableRow>
<ArgTableRow arg="ttl" typ="num"></ArgTableRow>
<ArgTableRow arg="tcp-flags" typ="multi { array-id, enum (fin | syn | rst | psh | ack | urg | ece | cwr) { fin:0, syn:1, rst:2, psh:3, ack:4, urg:5, ece:6, cwr:7 }
 }"></ArgTableRow>
<ArgTableRow arg="data" typ="string"></ArgTableRow>
</ArgTable>

### tool/sniffer/protocol

**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="protocol" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="enum (ip)"></ArgTableRow>
<ArgTableRow arg="port" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="packets" typ="num"></ArgTableRow>
<ArgTableRow arg="bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="share" typ="num"></ArgTableRow>
</ArgTable>

### tool/sniffer/quick

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="rows" typ="num"></ArgTableRow>
<ArgTableRow arg="show-frame" typ="bool"></ArgTableRow>
<ArgTableRow arg="interface" typ="object { iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="object { super { !
, composite { ,  } { ,  }
 } { !
, composite { ,  } { ,  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="object { super { !
, composite { ,  } { ,  }
 } { !
, composite { ,  } { ,  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="dst-mac-address" typ="object { super { !
, composite { ,  } { ,  }
 } { !
, composite { ,  } { ,  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="object { super { !
, alt { enum () {  }
, num [ .. 65535]
 } { enum () {  }
, num [ .. 65535]
 }
 } { !
, alt { enum () {  }
, num [ .. 65535]
 } { enum () {  }
, num [ .. 65535]
 }
 }
 }"></ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="object { super { !
, enum () {  }
 } { !
, enum () {  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="ip-address" typ="object { super { !
, composite { ,  } { ,  }
 } { !
, composite { ,  } { ,  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="src-ip-address" typ="object { super { !
, composite { ,  } { ,  }
 } { !
, composite { ,  } { ,  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="dst-ip-address" typ="object { super { !
, composite { ,  } { ,  }
 } { !
, composite { ,  } { ,  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="ipv6-address" typ="object { super { !
, ip6Prefix
 } { !
, ip6Prefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="src-ipv6-address" typ="object { super { !
, ip6Prefix
 } { !
, ip6Prefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="dst-ipv6-address" typ="object { super { !
, ip6Prefix
 } { !
, ip6Prefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="port" typ="object { super { !
, enum () {  }
 } { !
, enum () {  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="src-port" typ="object { super { !
, enum () {  }
 } { !
, enum () {  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="dst-port" typ="object { super { !
, enum () {  }
 } { !
, enum () {  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="object { super { !
, num [ .. 4095]
 } { !
, num [ .. 4095]
 }
 }"></ArgTableRow>
<ArgTableRow arg="direction" typ="enum (any | tx | rx)"></ArgTableRow>
<ArgTableRow arg="operator-between-entries" typ="enum (or | and)"></ArgTableRow>
<ArgTableRow arg="cpu" typ="object { super { !
, num
 } { !
, num
 }
 }"></ArgTableRow>
<ArgTableRow arg="size" typ="object { super { !
, range [0 .. 65535]
 } { !
, range [0 .. 65535]
 }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="time" typ="num"></ArgTableRow>
<ArgTableRow arg="num" typ="num"></ArgTableRow>
<ArgTableRow arg="dir" typ="enum (<- | ->)"></ArgTableRow>
<ArgTableRow arg="src-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="dst-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="vlan" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="src-address" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="protocol" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="size" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu" typ="num"></ArgTableRow>
<ArgTableRow arg="fp" typ="bool"></ArgTableRow>
<ArgTableRow arg="raw" typ="string"></ArgTableRow>
<ArgTableRow arg="dscp" typ="num"></ArgTableRow>
<ArgTableRow arg="ecn" typ="num"></ArgTableRow>
<ArgTableRow arg="fragment-offset" typ="num"></ArgTableRow>
<ArgTableRow arg="identification" typ="num"></ArgTableRow>
<ArgTableRow arg="ip-header-size" typ="num"></ArgTableRow>
<ArgTableRow arg="ip-packet-size" typ="num"></ArgTableRow>
<ArgTableRow arg="tcp-flags" typ="super { multi { array-id, enum (fin | syn | rst | psh | ack | urg | ece | cwr) { fin:0, syn:1, rst:2, psh:3, ack:4, urg:5, ece:6, cwr:7 }
 } { array-id, enum (fin | syn | rst | psh | ack | urg | ece | cwr) { fin:0, syn:1, rst:2, psh:3, ack:4, urg:5, ece:6, cwr:7 }
 }
 }"></ArgTableRow>
<ArgTableRow arg="ttl" typ="num"></ArgTableRow>
</ArgTable>

### tool/sniffer/save

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="file-name" typ="file"></ArgTableRow>
</ArgTable>

### tool/sniffer/start

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="object { iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="object { super { !
, composite { ,  } { ,  }
 } { !
, composite { ,  } { ,  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="object { super { !
, composite { ,  } { ,  }
 } { !
, composite { ,  } { ,  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="dst-mac-address" typ="object { super { !
, composite { ,  } { ,  }
 } { !
, composite { ,  } { ,  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="object { super { !
, alt { enum () {  }
, num [ .. 65535]
 } { enum () {  }
, num [ .. 65535]
 }
 } { !
, alt { enum () {  }
, num [ .. 65535]
 } { enum () {  }
, num [ .. 65535]
 }
 }
 }"></ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="object { super { !
, enum () {  }
 } { !
, enum () {  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="ip-address" typ="object { super { !
, composite { ,  } { ,  }
 } { !
, composite { ,  } { ,  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="src-ip-address" typ="object { super { !
, composite { ,  } { ,  }
 } { !
, composite { ,  } { ,  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="dst-ip-address" typ="object { super { !
, composite { ,  } { ,  }
 } { !
, composite { ,  } { ,  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="ipv6-address" typ="object { super { !
, ip6Prefix
 } { !
, ip6Prefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="src-ipv6-address" typ="object { super { !
, ip6Prefix
 } { !
, ip6Prefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="dst-ipv6-address" typ="object { super { !
, ip6Prefix
 } { !
, ip6Prefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="port" typ="object { super { !
, enum () {  }
 } { !
, enum () {  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="src-port" typ="object { super { !
, enum () {  }
 } { !
, enum () {  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="dst-port" typ="object { super { !
, enum () {  }
 } { !
, enum () {  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="object { super { !
, num [ .. 4095]
 } { !
, num [ .. 4095]
 }
 }"></ArgTableRow>
<ArgTableRow arg="direction" typ="enum (any | tx | rx)"></ArgTableRow>
<ArgTableRow arg="operator-between-entries" typ="enum (or | and)"></ArgTableRow>
<ArgTableRow arg="cpu" typ="object { super { !
, num
 } { !
, num
 }
 }"></ArgTableRow>
<ArgTableRow arg="size" typ="object { super { !
, range [0 .. 65535]
 } { !
, range [0 .. 65535]
 }
 }"></ArgTableRow>
</ArgTable>

### tool/sniffer/stop

**Type:** Command
