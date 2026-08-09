# License

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/license

**Type:** Settings Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="software-id" typ="string" syscap="nochr"></ArgTableRow>
<ArgTableRow arg="old-software-id" typ="string" syscap="nochr"></ArgTableRow>
<ArgTableRow arg="nlevel" typ="num" syscap="nochr"></ArgTableRow>
<ArgTableRow arg="features" typ="ubit (AP, synchronous, radiolan, wireless, extra-channels, , , )" syscap="nochr"></ArgTableRow>
<ArgTableRow arg="expires-in" typ="time" syscap="nochr"></ArgTableRow>
<ArgTableRow arg="system-id" typ="string" syscap="chr"></ArgTableRow>
<ArgTableRow arg="level" typ="enum (free | p1 | p10 | p-unlimited)" syscap="chr"></ArgTableRow>
<ArgTableRow arg="limited-upgrades" typ="bool" syscap="chr"></ArgTableRow>
<ArgTableRow arg="next-renewal-at" typ="date" syscap="chr"></ArgTableRow>
<ArgTableRow arg="deadline-at" typ="date" syscap="chr"></ArgTableRow>
</ArgTable>

### system/license/generate-new-id

**Syscap:** chr
**Type:** Command

### system/license/output

**Syscap:** nochr
**Type:** Command

### system/license/renew

**Syscap:** chr
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="account" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="level" typ="enum (p1 | p10 | p-unlimited)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>
