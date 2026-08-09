# openflow

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# openflow

**Package:** openflow
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="datapath-id" typ="super { num [0 .. 65535]
, /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="version" typ="enum (default | 1 | 1.3)"></ArgTableRow>
<ArgTableRow arg="passive-port" typ="num"></ArgTableRow>
<ArgTableRow arg="controllers" typ="object { super { enum (tcp | tls) { tcp:openflow::PROTOCOL_TCP, tls:openflow::PROTOCOL_TLS }
, /ip6Addr
, /num [1 .. 65535]
 } { enum (tcp | tls) { tcp:openflow::PROTOCOL_TCP, tls:openflow::PROTOCOL_TLS }
, /ip6Addr
, /num [1 .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)" unset="1"></ArgTableRow>
<ArgTableRow arg="verify-peer" typ="enum (required | none | if-cert-present)" unset="1"></ArgTableRow>
<ArgTableRow arg="isolate-controllers" typ="bool" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="openflow-fast-path-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="openflow-fast-path-bytes" typ="num"></ArgTableRow>
</ArgTable>

## openflow/flow

**Package:** openflow
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum"></ArgTableRow>
<ArgTableRow arg="version" typ="num"></ArgTableRow>
<ArgTableRow arg="match" typ="string"></ArgTableRow>
<ArgTableRow arg="actions" typ="string"></ArgTableRow>
<ArgTableRow arg="info" typ="string"></ArgTableRow>
<ArgTableRow arg="table-id" typ="num"></ArgTableRow>
<ArgTableRow arg="bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="packets" typ="num"></ArgTableRow>
<ArgTableRow arg="duration" typ="time"></ArgTableRow>
</ArgTable>

## openflow/group

**Package:** openflow
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum"></ArgTableRow>
<ArgTableRow arg="id" typ="num"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (all | select | indirect | ff)"></ArgTableRow>
<ArgTableRow arg="bucket-count" typ="num"></ArgTableRow>
<ArgTableRow arg="flow-count" typ="num"></ArgTableRow>
<ArgTableRow arg="buckets" typ="string"></ArgTableRow>
<ArgTableRow arg="bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="packets" typ="num"></ArgTableRow>
<ArgTableRow arg="duration" typ="time"></ArgTableRow>
<ArgTableRow arg="bucket-stats" typ="string"></ArgTableRow>
</ArgTable>

## openflow/meter

**Package:** openflow
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum"></ArgTableRow>
<ArgTableRow arg="id" typ="num"></ArgTableRow>
<ArgTableRow arg="band-count" typ="num"></ArgTableRow>
<ArgTableRow arg="bands" typ="string"></ArgTableRow>
<ArgTableRow arg="bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="packets" typ="num"></ArgTableRow>
<ArgTableRow arg="duration" typ="time"></ArgTableRow>
</ArgTable>

## openflow/port

**Package:** openflow
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="enum ()" mandatory="1"></ArgTableRow>
<ArgTableRow arg="switch" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="port-id" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="tx-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-packets" typ="num"></ArgTableRow>
</ArgTable>
