# Smb

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/smb

**Conditions:** !smips
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="enum (no | auto | yes)"></ArgTableRow>
<ArgTableRow arg="domain" typ="string"></ArgTableRow>
<ArgTableRow arg="comment" typ="string"></ArgTableRow>
<ArgTableRow arg="interfaces" typ="multi { array-id, iface_enum { all:0 } { all:0 }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

### ip/smb/shares

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
<ArgTableRow arg="r" typ="read-only">read-only</ArgTableRow>
<ArgTableRow arg="c" typ="require-encryption">require-encryption</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="directory" typ="file"></ArgTableRow>
<ArgTableRow arg="read-only" typ="bool"></ArgTableRow>
<ArgTableRow arg="require-encryption" typ="bool"></ArgTableRow>
<ArgTableRow arg="valid-users" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="invalid-users" typ="multi { array-id, enum
 }"></ArgTableRow>
</ArgTable>

### ip/smb/users

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
<ArgTableRow arg="r" typ="read-only">read-only</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="read-only" typ="bool"></ArgTableRow>
</ArgTable>
