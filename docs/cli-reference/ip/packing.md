# Packing

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/packing

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="packing" typ="enum (none | simple | compress-headers | compress-all)"></ArgTableRow>
<ArgTableRow arg="unpacking" typ="enum (none | simple | compress-headers | compress-all)"></ArgTableRow>
<ArgTableRow arg="aggregated-size" typ="num"></ArgTableRow>
</ArgTable>
