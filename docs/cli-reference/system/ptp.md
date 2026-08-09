# Ptp

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/ptp

**Conditions:** !smips
**Syscap:** ptp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="priority1" typ="enum (auto)"></ArgTableRow>
<ArgTableRow arg="priority2" typ="enum (auto)"></ArgTableRow>
<ArgTableRow arg="delay-mode" typ="enum (auto | e2e | p2p)"></ArgTableRow>
<ArgTableRow arg="transport" typ="enum (auto | ipv4 | l2-non-forwardable | l2-forwardable)"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum (default | 802.1as | g8275.1 | aes67 | smpte)"></ArgTableRow>
<ArgTableRow arg="domain" typ="enum (auto)"></ArgTableRow>
</ArgTable>

### system/ptp/monitor

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="clock-id" typ="string"></ArgTableRow>
<ArgTableRow arg="priority1" typ="num"></ArgTableRow>
<ArgTableRow arg="priority2" typ="num"></ArgTableRow>
<ArgTableRow arg="i-am-gm" typ="bool"></ArgTableRow>
<ArgTableRow arg="gm-clock-id" typ="string"></ArgTableRow>
<ArgTableRow arg="gm-priority1" typ="num"></ArgTableRow>
<ArgTableRow arg="gm-priority2" typ="num"></ArgTableRow>
<ArgTableRow arg="master-clock-id" typ="string"></ArgTableRow>
<ArgTableRow arg="slave-port" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="freq-drift" typ="num"></ArgTableRow>
<ArgTableRow arg="offset" typ="num"></ArgTableRow>
<ArgTableRow arg="slave-port-delay" typ="num"></ArgTableRow>
</ArgTable>

### system/ptp/port

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ptp" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum {  }" mandatory="1"></ArgTableRow>
</ArgTable>

### system/ptp/status

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="state" typ="string"></ArgTableRow>
<ArgTableRow arg="delay" typ="num"></ArgTableRow>
<ArgTableRow arg="port-nr" typ="num"></ArgTableRow>
<ArgTableRow arg="as-capable" typ="bool"></ArgTableRow>
<ArgTableRow arg="neigh-freq-drift" typ="num"></ArgTableRow>
</ArgTable>
