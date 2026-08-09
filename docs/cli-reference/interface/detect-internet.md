# Detect Internet

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/detect-internet

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="detect-interface-list" typ="enum"></ArgTableRow>
<ArgTableRow arg="lan-interface-list" typ="enum"></ArgTableRow>
<ArgTableRow arg="wan-interface-list" typ="enum"></ArgTableRow>
<ArgTableRow arg="internet-interface-list" typ="enum"></ArgTableRow>
<ArgTableRow arg="request-interval" typ="time"></ArgTableRow>
</ArgTable>

### interface/detect-internet/state

**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (no-link | unknown | lan | wan | internet | slave)"></ArgTableRow>
<ArgTableRow arg="state-change-time" typ="date"></ArgTableRow>
<ArgTableRow arg="cloud-rtt" typ="time"></ArgTableRow>
</ArgTable>
