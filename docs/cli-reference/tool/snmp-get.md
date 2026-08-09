# Snmp Get

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/snmp-get

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="oid" typ="object { string
 }"></ArgTableRow>
<ArgTableRow arg="next" typ="bool"></ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="tries" typ="num"></ArgTableRow>
<ArgTableRow arg="try-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="version" typ="enum (1 | 2c | 3)"></ArgTableRow>
<ArgTableRow arg="community" typ="string"></ArgTableRow>
<ArgTableRow arg="security" typ="enum (none | authorized | private)"></ArgTableRow>
<ArgTableRow arg="authentication-password" typ="string"></ArgTableRow>
<ArgTableRow arg="authentication-protocol" typ="enum (MD5 | SHA1)"></ArgTableRow>
<ArgTableRow arg="encryption-password" typ="string"></ArgTableRow>
<ArgTableRow arg="encryption-protocol" typ="enum (DES | AES)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="oid" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (null | integer | counter | gauge | timeticks | unsigned-integer | octet-string | opaque | object-id | ip-address | counter-64bit | no-such-object | no-such-instance | end-of-mib-view)"></ArgTableRow>
<ArgTableRow arg="value" typ="string"></ArgTableRow>
</ArgTable>
