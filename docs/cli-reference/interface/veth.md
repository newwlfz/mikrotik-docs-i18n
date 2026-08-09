# Veth

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/veth

**Conditions:** !smips
**Syscap:** container
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="container-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="address" typ="multi { address (flags=46/)
 }"></ArgTableRow>
<ArgTableRow arg="gateway" typ="address (flags=4)"></ArgTableRow>
<ArgTableRow arg="gateway6" typ="address (flags=6)"></ArgTableRow>
<ArgTableRow arg="dhcp" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="dhcp-address" typ="address (flags=46/)"></ArgTableRow>
</ArgTable>
