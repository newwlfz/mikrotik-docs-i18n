# Ntp

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/ntp

**Type:** Directory

### system/ntp/client

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (unicast | broadcast | multicast | manycast)"></ArgTableRow>
<ArgTableRow arg="servers" typ="multi { address (flags=46D)
 }"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="freq-drift" typ="num"></ArgTableRow>
<ArgTableRow arg="status" typ="enum (stopped | waiting | synchronized | using-local-clock)"></ArgTableRow>
<ArgTableRow arg="synced-server" typ="address (flags=46D)"></ArgTableRow>
<ArgTableRow arg="synced-stratum" typ="num"></ArgTableRow>
<ArgTableRow arg="system-offset" typ="num"></ArgTableRow>
</ArgTable>

#### system/ntp/client/reset-freq-drift

**Type:** Command

#### system/ntp/client/servers

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="address (flags=46D)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="min-poll" typ="num"></ArgTableRow>
<ArgTableRow arg="max-poll" typ="num"></ArgTableRow>
<ArgTableRow arg="iburst" typ="bool"></ArgTableRow>
<ArgTableRow arg="auth-key" typ="enum (none)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="resolved-address" typ="address (flags=46)"></ArgTableRow>
</ArgTable>

### system/ntp/key

**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="key-id" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="key-val" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>

### system/ntp/monitor-peers

**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="type" typ="string"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="refid" typ="string"></ArgTableRow>
<ArgTableRow arg="stratum" typ="num"></ArgTableRow>
<ArgTableRow arg="hpoll" typ="num"></ArgTableRow>
<ArgTableRow arg="ppoll" typ="num"></ArgTableRow>
<ArgTableRow arg="root-delay" typ="num"></ArgTableRow>
<ArgTableRow arg="root-disp" typ="num"></ArgTableRow>
<ArgTableRow arg="offset" typ="num"></ArgTableRow>
<ArgTableRow arg="delay" typ="num"></ArgTableRow>
<ArgTableRow arg="disp" typ="num"></ArgTableRow>
<ArgTableRow arg="jitter" typ="num"></ArgTableRow>
</ArgTable>

### system/ntp/server

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="broadcast" typ="bool"></ArgTableRow>
<ArgTableRow arg="multicast" typ="bool"></ArgTableRow>
<ArgTableRow arg="manycast" typ="bool"></ArgTableRow>
<ArgTableRow arg="broadcast-addresses" typ="multi { ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="use-local-clock" typ="bool"></ArgTableRow>
<ArgTableRow arg="local-clock-stratum" typ="num"></ArgTableRow>
<ArgTableRow arg="auth-key" typ="enum (none)"></ArgTableRow>
</ArgTable>
