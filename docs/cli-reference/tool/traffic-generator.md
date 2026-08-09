# Traffic Generator

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/traffic-generator

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="test-id" typ="num"></ArgTableRow>
<ArgTableRow arg="measure-out-of-order" typ="bool"></ArgTableRow>
<ArgTableRow arg="latency-distribution-max" typ="time"></ArgTableRow>
<ArgTableRow arg="stats-samples-to-keep" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="running" typ="bool"></ArgTableRow>
<ArgTableRow arg="latency-distribution-samples" typ="num"></ArgTableRow>
<ArgTableRow arg="latency-distribution-measure-interval" typ="string"></ArgTableRow>
</ArgTable>

### tool/traffic-generator/inject

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="data" typ="string"></ArgTableRow>
<ArgTableRow arg="priority" typ="num" unset="1"></ArgTableRow>
</ArgTable>

### tool/traffic-generator/inject-pcap

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="pcap-file" typ="file"></ArgTableRow>
<ArgTableRow arg="speed-multiplier" typ="num"></ArgTableRow>
<ArgTableRow arg="loop" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="iteration" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="num"></ArgTableRow>
</ArgTable>

### tool/traffic-generator/packet-template

**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="header-stack" typ="multi { enum (mac | vlan | ip | udp | raw | ipv6 | tcp) { mac:1, vlan:2, ip:3, udp:4, raw:5, ipv6:6, tcp:7 }
 }"></ArgTableRow>
<ArgTableRow arg="port" typ="enum"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="mac-src" typ="multi { array-id, array-id, composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="mac-dst" typ="multi { array-id, array-id, composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="multi { alt { enum () {  }
, num [ .. 65535]
 } { enum () {  }
, num [ .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="vlan-priority" typ="multi { num [ .. 7]
 }"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="multi { num [ .. 4095]
 }"></ArgTableRow>
<ArgTableRow arg="vlan-protocol" typ="multi { alt { enum () {  }
, num [ .. 65535]
 } { enum () {  }
, num [ .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="ip-dscp" typ="multi { num [ .. 255]
 }"></ArgTableRow>
<ArgTableRow arg="ip-id" typ="multi { num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="ip-frag-off" typ="multi { num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="ip-ttl" typ="multi { num [ .. 255]
 }"></ArgTableRow>
<ArgTableRow arg="ip-src" typ="multi { array-id, array-id, ipRange
 }"></ArgTableRow>
<ArgTableRow arg="ip-dst" typ="multi { array-id, array-id, ipRange
 }"></ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="multi { enum () {  }
 }"></ArgTableRow>
<ArgTableRow arg="ip-gateway" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="udp-src-port" typ="multi { array-id, array-id, range [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="udp-dst-port" typ="multi { array-id, array-id, range [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="udp-checksum" typ="multi { array-id, num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="raw-header" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="ipv6-src" typ="multi { array-id, array-id, ip6Prefix
 }"></ArgTableRow>
<ArgTableRow arg="ipv6-dst" typ="multi { array-id, array-id, ip6Prefix
 }"></ArgTableRow>
<ArgTableRow arg="ipv6-next-header" typ="multi { enum () {  }
 }"></ArgTableRow>
<ArgTableRow arg="ipv6-gateway" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="ipv6-traffic-class" typ="multi { num [ .. 255]
 }"></ArgTableRow>
<ArgTableRow arg="ipv6-flow-label" typ="multi { num [ .. 0xfffff]
 }"></ArgTableRow>
<ArgTableRow arg="ipv6-hop-limit" typ="multi { num [ .. 255]
 }"></ArgTableRow>
<ArgTableRow arg="tcp-src-port" typ="multi { array-id, array-id, range [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="tcp-dst-port" typ="multi { array-id, array-id, range [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="tcp-syn" typ="multi { array-id, array-id, range
 }"></ArgTableRow>
<ArgTableRow arg="tcp-ack" typ="multi { array-id, array-id, range
 }"></ArgTableRow>
<ArgTableRow arg="tcp-data-offset" typ="multi { num [ .. 15]
 }"></ArgTableRow>
<ArgTableRow arg="tcp-flags" typ="multi { ubit (fin, syn, rst, psh, ack, urg, ece, cwr, ns, res0, res1, res2) { fin, syn, rst, psh, ack, urg, ece, cwr, ns, res0, res1, res2 }
 }"></ArgTableRow>
<ArgTableRow arg="tcp-window-size" typ="multi { num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="tcp-urgent-pointer" typ="multi { num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="data" typ="enum (uninitialized | random | specific-byte | incrementing)"></ArgTableRow>
<ArgTableRow arg="data-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="random-byte-offsets-and-masks" typ="multi { array-id, array-id, composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="random-ranges" typ="object { super { num [ .. 256]
, :enum (8 | 16 | 32) { 8:8, 16:16, 32:32 }
, :range
 } { num [ .. 256]
, :enum (8 | 16 | 32) { 8:8, 16:16, 32:32 }
, :range
 }
 }"></ArgTableRow>
<ArgTableRow arg="special-footer" typ="bool"></ArgTableRow>
<ArgTableRow arg="compute-checksum-from-offset" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="assumed-port" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="assumed-interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="assumed-mac-src" typ="multi { macAddr
 }"></ArgTableRow>
<ArgTableRow arg="assumed-mac-dst" typ="multi { macAddr
 }"></ArgTableRow>
<ArgTableRow arg="assumed-mac-protocol" typ="multi { alt { enum () {  }
, num
 } { enum () {  }
, num
 }
 }"></ArgTableRow>
<ArgTableRow arg="assumed-vlan-priority" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-vlan-id" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-vlan-protocol" typ="multi { alt { enum () {  }
, num
 } { enum () {  }
, num
 }
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ip-dscp" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ip-id" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ip-frag-off" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ip-ttl" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ip-src" typ="multi { ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ip-dst" typ="multi { ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ip-protocol" typ="multi { enum () {  }
 }"></ArgTableRow>
<ArgTableRow arg="assumed-udp-src-port" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-udp-dst-port" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-udp-checksum" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-raw-header" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ipv6-src" typ="multi { ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ipv6-dst" typ="multi { ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ipv6-next-header" typ="multi { enum () {  }
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ipv6-traffic-class" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ipv6-flow-label" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ipv6-hop-limit" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-tcp-src-port" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-tcp-dst-port" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-tcp-syn" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-tcp-ack" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-tcp-data-offset" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-tcp-flags" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-tcp-window-size" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-tcp-urgent-pointer" typ="multi { num
 }"></ArgTableRow>
</ArgTable>

### tool/traffic-generator/port

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="first-header" typ="enum (mac | vlan | ip | udp | raw | ipv6 | tcp)"></ArgTableRow>
</ArgTable>

### tool/traffic-generator/quick

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="entries-to-show" typ="num"></ArgTableRow>
<ArgTableRow arg="test-id" typ="num"></ArgTableRow>
<ArgTableRow arg="measure-out-of-order" typ="bool"></ArgTableRow>
<ArgTableRow arg="cpu-core" typ="multi { array-id, array-id, range [0 .. 255]
 }"></ArgTableRow>
<ArgTableRow arg="stream" typ="multi { enum
 }"></ArgTableRow>
<ArgTableRow arg="port" typ="multi { enum
 }"></ArgTableRow>
<ArgTableRow arg="interface" typ="multi { iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="id" typ="multi { num [0 .. 255]
 }"></ArgTableRow>
<ArgTableRow arg="packet-size" typ="multi { array-id, array-id, range [1 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="pps" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="mbps" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-template" typ="multi { enum
 }"></ArgTableRow>
<ArgTableRow arg="packet-count" typ="multi { num
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="seq" typ="enum (TOT)"></ArgTableRow>
<ArgTableRow arg="id" typ="enum (TOT)"></ArgTableRow>
<ArgTableRow arg="tx-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-ooo" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bad-csum" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-ratio" typ="string"></ArgTableRow>
<ArgTableRow arg="lat-min" typ="string"></ArgTableRow>
<ArgTableRow arg="lat-avg" typ="string"></ArgTableRow>
<ArgTableRow arg="lat-max" typ="string"></ArgTableRow>
<ArgTableRow arg="jitter" typ="string"></ArgTableRow>
</ArgTable>

### tool/traffic-generator/raw-packet-template

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="port" typ="enum"></ArgTableRow>
<ArgTableRow arg="header" typ="string"></ArgTableRow>
<ArgTableRow arg="data" typ="enum (uninitialized | random | specific-byte | incrementing)"></ArgTableRow>
<ArgTableRow arg="data-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="random-byte-offsets-and-masks" typ="multi { array-id, array-id, composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="random-ranges" typ="object { super { num [ .. 256]
, :enum (8 | 16 | 32) { 8:8, 16:16, 32:32 }
, :range
 } { num [ .. 256]
, :enum (8 | 16 | 32) { 8:8, 16:16, 32:32 }
, :range
 }
 }"></ArgTableRow>
<ArgTableRow arg="ip-header-offset" typ="multi { num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="ipv6-header-offset" typ="multi { num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="udp-header-offset" typ="multi { num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="udp-compute-checksum" typ="multi { bool
 }"></ArgTableRow>
<ArgTableRow arg="tcp-header-offset" typ="multi { num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="special-footer" typ="bool"></ArgTableRow>
<ArgTableRow arg="compute-checksum-from-offset" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="header-length" typ="num"></ArgTableRow>
</ArgTable>

### tool/traffic-generator/start

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="test-id" typ="num"></ArgTableRow>
<ArgTableRow arg="measure-out-of-order" typ="bool"></ArgTableRow>
<ArgTableRow arg="cpu-core" typ="multi { array-id, array-id, range [0 .. 255]
 }"></ArgTableRow>
<ArgTableRow arg="stream" typ="multi { enum
 }"></ArgTableRow>
<ArgTableRow arg="port" typ="multi { enum
 }"></ArgTableRow>
<ArgTableRow arg="interface" typ="multi { iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="id" typ="multi { num [0 .. 255]
 }"></ArgTableRow>
<ArgTableRow arg="packet-size" typ="multi { array-id, array-id, range [1 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="pps" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="mbps" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-template" typ="multi { enum
 }"></ArgTableRow>
<ArgTableRow arg="packet-count" typ="multi { num
 }"></ArgTableRow>
</ArgTable>

### tool/traffic-generator/stats

**Type:** Directory

#### tool/traffic-generator/stats/latency-distribution

**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="stream-id" typ="num"></ArgTableRow>
<ArgTableRow arg="port" typ="enum"></ArgTableRow>
<ArgTableRow arg="seq" typ="range"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="latency" typ="string"></ArgTableRow>
<ArgTableRow arg="count" typ="num"></ArgTableRow>
<ArgTableRow arg="share" typ="num"></ArgTableRow>
<ArgTableRow arg="graph" typ="meter"></ArgTableRow>
</ArgTable>

#### tool/traffic-generator/stats/port

**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="seq" typ="enum (TOT)"></ArgTableRow>
<ArgTableRow arg="port" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="rx-unk-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-unk-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-unk-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-ooo" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bad-csum" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-ratio" typ="string"></ArgTableRow>
<ArgTableRow arg="lat-min" typ="string"></ArgTableRow>
<ArgTableRow arg="lat-avg" typ="string"></ArgTableRow>
<ArgTableRow arg="lat-max" typ="string"></ArgTableRow>
<ArgTableRow arg="jitter" typ="string"></ArgTableRow>
</ArgTable>

#### tool/traffic-generator/stats/raw

**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="seq" typ="enum (TOT)"></ArgTableRow>
<ArgTableRow arg="port" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="id" typ="enum (TOT)"></ArgTableRow>
<ArgTableRow arg="tx-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-ooo" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bad-csum" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-ratio" typ="string"></ArgTableRow>
<ArgTableRow arg="lat-min" typ="string"></ArgTableRow>
<ArgTableRow arg="lat-avg" typ="string"></ArgTableRow>
<ArgTableRow arg="lat-max" typ="string"></ArgTableRow>
<ArgTableRow arg="jitter" typ="string"></ArgTableRow>
</ArgTable>

#### tool/traffic-generator/stats/stream

**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="seq" typ="enum (TOT)"></ArgTableRow>
<ArgTableRow arg="id" typ="enum (TOT)"></ArgTableRow>
<ArgTableRow arg="tx-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-ooo" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bad-csum" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-ratio" typ="string"></ArgTableRow>
<ArgTableRow arg="lat-min" typ="string"></ArgTableRow>
<ArgTableRow arg="lat-avg" typ="string"></ArgTableRow>
<ArgTableRow arg="lat-max" typ="string"></ArgTableRow>
<ArgTableRow arg="jitter" typ="string"></ArgTableRow>
</ArgTable>

### tool/traffic-generator/stop

**Type:** Command

### tool/traffic-generator/stream

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="port" typ="enum"></ArgTableRow>
<ArgTableRow arg="id" typ="num"></ArgTableRow>
<ArgTableRow arg="packet-size" typ="range"></ArgTableRow>
<ArgTableRow arg="pps" typ="num"></ArgTableRow>
<ArgTableRow arg="mbps" typ="num"></ArgTableRow>
<ArgTableRow arg="packet-count" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-core" typ="range"></ArgTableRow>
<ArgTableRow arg="tx-template" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="default-port" typ="enum"></ArgTableRow>
</ArgTable>
