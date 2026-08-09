# Isis

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/isis

**Type:** Directory

### routing/isis/instance

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="afi" typ="ubit (ip, ipv6)"></ArgTableRow>
<ArgTableRow arg="system-id" typ="string"></ArgTableRow>
<ArgTableRow arg="areas" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="areas-max" typ="num"></ArgTableRow>
<ArgTableRow arg="in-filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="metric-type" typ="enum (old | wide | both)" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.redistribute" typ="ubit ()" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.out-filter-select" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.out-filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.originate-default" typ="enum ()" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.lsp-max-size" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.lsp-max-age" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.lsp-update-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.lsp-refresh-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.redistribute" typ="ubit ()" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.out-filter-select" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.out-filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.originate-default" typ="enum ()" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.lsp-max-size" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.lsp-max-age" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.lsp-update-interval" typ="num" unset="1"></ArgTableRow>
</ArgTable>

### routing/isis/interface

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="ptp" typ="switch"></ArgTableRow>
<ArgTableRow arg="hello-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.usage" typ="ubit (l1, l2)" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.3way-state" typ="enum (down | init | up)" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.psnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.csnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.metric" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.hello-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.hello-dr-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.hello-multiplier" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.priority" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.passive" typ="switch"></ArgTableRow>
<ArgTableRow arg="l2.psnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.csnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.metric" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.hello-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.hello-dr-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.hello-multiplier" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.priority" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.passive" typ="switch"></ArgTableRow>
</ArgTable>

### routing/isis/interface-template

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="interfaces" typ="object { iface_enum {  } {  }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="levels" typ="ubit (l1, l2)"></ArgTableRow>
<ArgTableRow arg="ptp" typ="switch" unset="1"></ArgTableRow>
<ArgTableRow arg="passive" typ="switch" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.hello-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.hello-multiplier" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.hello-3way" typ="switch" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.l1.csnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.l1.psnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.l1.metric" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.l2.csnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.l2.psnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.l2.metric" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l1.hello-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l1.hello-interval-dr" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l1.hello-multiplier" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l1.priority" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l1.csnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l1.psnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l1.metric" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l2.hello-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l2.hello-interval-dr" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l2.hello-multiplier" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l2.priority" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l2.csnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l2.psnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l2.metric" typ="num" unset="1"></ArgTableRow>
</ArgTable>

### routing/isis/lsp

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="level" typ="enum (l1 | l2)"></ArgTableRow>
<ArgTableRow arg="lsp-id" typ="string"></ArgTableRow>
<ArgTableRow arg="age" typ="num"></ArgTableRow>
<ArgTableRow arg="checksum" typ="num"></ArgTableRow>
<ArgTableRow arg="sequence" typ="num"></ArgTableRow>
<ArgTableRow arg="body" typ="string" unset="1"></ArgTableRow>
</ArgTable>

### routing/isis/neighbor

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="level-type" typ="enum (l1 | l2)"></ArgTableRow>
<ArgTableRow arg="snpa" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="srcid" typ="string"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (init | up)" unset="1"></ArgTableRow>
</ArgTable>
