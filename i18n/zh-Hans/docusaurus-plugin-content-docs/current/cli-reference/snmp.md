# snmp

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# snmp

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
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

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="engine-id" typ="string"></ArgTableRow>
</ArgTable>

## snmp/community

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
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

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="oid" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (integer | string | nullobj | obj-id | ip-address | counter32 | timeticks | unsigned)"></ArgTableRow>
<ArgTableRow arg="value" typ="string"></ArgTableRow>
</ArgTable>