# Swos

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/swos

**Conditions:** !i386, !mmips, !powerpc, !tile, !smips
**Syscap:** swos
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address-acquisition-mode" typ="enum (dhcp-with-fallback | static | dhcp-only)"></ArgTableRow>
<ArgTableRow arg="static-ip-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="identity" typ="string"></ArgTableRow>
<ArgTableRow arg="allow-from" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="allow-from-ports" typ="ubit (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32)"></ArgTableRow>
<ArgTableRow arg="allow-from-vlan" typ="num"></ArgTableRow>
</ArgTable>

### system/swos/load-config

**Conditions:** !i386, !mmips, !powerpc, !tile, !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="file" typ="file {  }"></ArgTableRow>
</ArgTable>

### system/swos/password

**Conditions:** !i386, !mmips, !powerpc, !tile, !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="new-password" typ="string"></ArgTableRow>
<ArgTableRow arg="confirm-new-password" typ="string"></ArgTableRow>
</ArgTable>

### system/swos/reset-config

**Conditions:** !i386, !mmips, !powerpc, !tile, !smips
**Type:** Command

### system/swos/save-config

**Conditions:** !i386, !mmips, !powerpc, !tile, !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="file" typ="string"></ArgTableRow>
</ArgTable>

### system/swos/upgrade

**Conditions:** !i386, !mmips, !powerpc, !tile, !smips
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="version" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>
