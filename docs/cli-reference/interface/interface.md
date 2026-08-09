# interface

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# interface

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="R" typ="running"></ArgTableRow>
<ArgTableRow arg="S" typ="slave"></ArgTableRow>
<ArgTableRow arg="P" typ="passthrough"></ArgTableRow>
<ArgTableRow arg="w" typ="power-limited"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="default-name" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="string"></ArgTableRow>
<ArgTableRow arg="actual-mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="max-l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="last-link-down-time" typ="date"></ArgTableRow>
<ArgTableRow arg="last-link-up-time" typ="date"></ArgTableRow>
<ArgTableRow arg="link-downs" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-drop" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-drop" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-queue-drop" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-error" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-error" typ="num"></ArgTableRow>
<ArgTableRow arg="fp-rx-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="fp-tx-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="fp-rx-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="fp-tx-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="fp-rps-drop" typ="num"></ArgTableRow>
</ArgTable>

## interface/blink

**Type:** Command

## interface/monitor-traffic

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="multi { array-id, iface_enum { aggregate:0 } { aggregate:0 }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="rx-packets-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bits-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="fp-rx-packets-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="fp-rx-bits-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-drops-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-errors-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-packets-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-bits-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="fp-tx-packets-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="fp-tx-bits-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-drops-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-queue-drops-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-errors-per-second" typ="num"></ArgTableRow>
</ArgTable>

## interface/reset-counters

**Type:** Command
