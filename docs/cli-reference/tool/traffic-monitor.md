# Traffic Monitor

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/traffic-monitor

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="traffic" typ="enum (transmitted | received)"></ArgTableRow>
<ArgTableRow arg="trigger" typ="enum (above | below | always)"></ArgTableRow>
<ArgTableRow arg="threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="on-event" typ="alt { , string
 }"></ArgTableRow>
</ArgTable>
