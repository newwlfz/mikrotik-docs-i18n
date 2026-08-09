# Traffic Flow

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/traffic-flow

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="interfaces" typ="multi { array-id, alt { iface_enum { local:0, all:0xFFFFFFFF } { local:0, all:0xFFFFFFFF }
, enum
 } { iface_enum { local:0, all:0xFFFFFFFF } { local:0, all:0xFFFFFFFF }
, enum
 }
 }"></ArgTableRow>
<ArgTableRow arg="cache-entries" typ="enum (1k | 2k | 4k | 8k | 16k | 32k | 64k | 128k | 256k | 512k | 1M | 2M | 4M | 8M | 16M | 32M)"></ArgTableRow>
<ArgTableRow arg="active-flow-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="inactive-flow-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="packet-sampling" typ="bool"></ArgTableRow>
<ArgTableRow arg="sampling-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="sampling-space" typ="num"></ArgTableRow>
</ArgTable>

### ip/traffic-flow/ipfix

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="nat-events" typ="bool"></ArgTableRow>
<ArgTableRow arg="first-forwarded" typ="bool"></ArgTableRow>
<ArgTableRow arg="last-forwarded" typ="bool"></ArgTableRow>
<ArgTableRow arg="sys-init-time" typ="bool"></ArgTableRow>
<ArgTableRow arg="packets" typ="bool"></ArgTableRow>
<ArgTableRow arg="bytes" typ="bool"></ArgTableRow>
<ArgTableRow arg="src-port" typ="bool"></ArgTableRow>
<ArgTableRow arg="dst-port" typ="bool"></ArgTableRow>
<ArgTableRow arg="in-interface" typ="bool"></ArgTableRow>
<ArgTableRow arg="out-interface" typ="bool"></ArgTableRow>
<ArgTableRow arg="protocol" typ="bool"></ArgTableRow>
<ArgTableRow arg="tos" typ="bool"></ArgTableRow>
<ArgTableRow arg="tcp-flags" typ="bool"></ArgTableRow>
<ArgTableRow arg="dst-mac-address" typ="bool"></ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="bool"></ArgTableRow>
<ArgTableRow arg="src-address" typ="bool"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="bool"></ArgTableRow>
<ArgTableRow arg="src-address-mask" typ="bool"></ArgTableRow>
<ArgTableRow arg="dst-address-mask" typ="bool"></ArgTableRow>
<ArgTableRow arg="gateway" typ="bool"></ArgTableRow>
<ArgTableRow arg="ttl" typ="bool"></ArgTableRow>
<ArgTableRow arg="ip-header-length" typ="bool"></ArgTableRow>
<ArgTableRow arg="is-multicast" typ="bool"></ArgTableRow>
<ArgTableRow arg="ip-total-length" typ="bool"></ArgTableRow>
<ArgTableRow arg="nat-src-address" typ="bool"></ArgTableRow>
<ArgTableRow arg="nat-dst-address" typ="bool"></ArgTableRow>
<ArgTableRow arg="nat-src-port" typ="bool"></ArgTableRow>
<ArgTableRow arg="nat-dst-port" typ="bool"></ArgTableRow>
<ArgTableRow arg="ipv6-flow-label" typ="bool"></ArgTableRow>
<ArgTableRow arg="udp-length" typ="bool"></ArgTableRow>
<ArgTableRow arg="tcp-seq-num" typ="bool"></ArgTableRow>
<ArgTableRow arg="tcp-ack-num" typ="bool"></ArgTableRow>
<ArgTableRow arg="tcp-window-size" typ="bool"></ArgTableRow>
<ArgTableRow arg="igmp-type" typ="bool"></ArgTableRow>
<ArgTableRow arg="icmp-type" typ="bool"></ArgTableRow>
<ArgTableRow arg="icmp-code" typ="bool"></ArgTableRow>
</ArgTable>

### ip/traffic-flow/monitor

**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="finished-flows" typ="num"></ArgTableRow>
<ArgTableRow arg="active-flows" typ="num"></ArgTableRow>
<ArgTableRow arg="unmanaged-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="unmanaged-bytes" typ="num"></ArgTableRow>
</ArgTable>

### ip/traffic-flow/target

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="src-address" typ="alt { ipAddr
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="alt { ipAddr
, ip6Addr
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="version" typ="enum (1 | 5 | 9 | ipfix)"></ArgTableRow>
<ArgTableRow arg="v9-template-refresh" typ="num"></ArgTableRow>
<ArgTableRow arg="v9-template-timeout" typ="time"></ArgTableRow>
</ArgTable>
