# snmp

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# snmp

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="contact" typ="string"></ArgTableRow>
<ArgTableRow arg="location" typ="string"></ArgTableRow>
<ArgTableRow arg="engine-id-suffix" typ="string"></ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ipAddr
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="trap-target" typ="object { alt { ip6Addr
, ipAddr
 } { ip6Addr
, ipAddr
 }
 }"></ArgTableRow>
<ArgTableRow arg="trap-community" typ="enum"></ArgTableRow>
<ArgTableRow arg="trap-version" typ="enum (1 | 2 | 3)"></ArgTableRow>
<ArgTableRow arg="trap-generators" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="trap-interfaces" typ="object { iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="engine-id" typ="string"></ArgTableRow>
</ArgTable>

## snmp/community

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="addresses" typ="object { alt { ip6Prefix
, ipPrefix
 } { ip6Prefix
, ipPrefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="security" typ="enum (none | authorized | private)"></ArgTableRow>
<ArgTableRow arg="read-access" typ="bool"></ArgTableRow>
<ArgTableRow arg="write-access" typ="bool"></ArgTableRow>
<ArgTableRow arg="authentication-protocol" typ="enum (MD5 | SHA1)"></ArgTableRow>
<ArgTableRow arg="encryption-protocol" typ="enum (DES | AES)"></ArgTableRow>
<ArgTableRow arg="authentication-password" typ="string"></ArgTableRow>
<ArgTableRow arg="encryption-password" typ="string"></ArgTableRow>
</ArgTable>

## snmp/send-trap

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="oid" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (integer | string | nullobj | obj-id | ip-address | counter32 | timeticks | unsigned)"></ArgTableRow>
<ArgTableRow arg="value" typ="string"></ArgTableRow>
</ArgTable>
