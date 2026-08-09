# Upnp

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/upnp

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow-disable-external-interface" typ="bool"></ArgTableRow>
<ArgTableRow arg="show-dummy-rule" typ="bool"></ArgTableRow>
</ArgTable>

### ip/upnp/interfaces

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (external | internal)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="forced-ip" typ="super { ipAddr
 }"></ArgTableRow>
</ArgTable>
