# port

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# port

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="baud-rate" typ="enum (auto | 50 | 75 | 110 | 134 | 150 | 200 | 300 | 600 | 1200 | 1800 | 2400 | 4800 | 9600 | 19200 | 38400 | 57600 | 115200 | 230400 | 460800 | 500000 | 576000 | 921600 | 1000000 | 1152000 | 1500000 | 2000000 | 2500000 | 3000000 | 3500000 | 4000000)"></ArgTableRow>
<ArgTableRow arg="data-bits" typ="enum (7 | 8)"></ArgTableRow>
<ArgTableRow arg="parity" typ="enum (none | odd | even)"></ArgTableRow>
<ArgTableRow arg="stop-bits" typ="enum (1 | 2)"></ArgTableRow>
<ArgTableRow arg="flow-control" typ="enum (xon-xoff | hardware | none)"></ArgTableRow>
<ArgTableRow arg="rts" typ="bool"></ArgTableRow>
<ArgTableRow arg="dtr" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="used-by" typ="string"></ArgTableRow>
<ArgTableRow arg="device" typ="string"></ArgTableRow>
<ArgTableRow arg="channels" typ="num"></ArgTableRow>
<ArgTableRow arg="line-state" typ="multi { array-id, enum (dtr | rts | cts | dcd | ri | dsr) { dtr:1, rts:2, cts:5, dcd:6, ri:7, dsr:8 }
 }"></ArgTableRow>
</ArgTable>

## port/remote-access

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="A" typ="active">active</ArgTableRow>
<ArgTableRow arg="B" typ="busy">busy</ArgTableRow>
<ArgTableRow arg="L" typ="logging-active">logging-active</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="port" typ="enum"></ArgTableRow>
<ArgTableRow arg="channel" typ="num"></ArgTableRow>
<ArgTableRow arg="remote-addresses" typ="object { super { address (flags=46/)
, [ -address (flags=46)]
, [ @num]
 } { address (flags=46/)
, [ -address (flags=46)]
, [ @num]
 }
 }"></ArgTableRow>
<ArgTableRow arg="local-address" typ="alt { ipAddr
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="ip-port" typ="num"></ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (tcp-server | rfc2217 | tcp-client | udp)"></ArgTableRow>
<ArgTableRow arg="log-file" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="active-peer" typ="ip6Addr {  }"></ArgTableRow>
<ArgTableRow arg="active-peer-port" typ="num {  }"></ArgTableRow>
</ArgTable>
