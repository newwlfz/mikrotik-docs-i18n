# Clock

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/clock

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="time" typ="date"></ArgTableRow>
<ArgTableRow arg="date" typ="date"></ArgTableRow>
<ArgTableRow arg="time-zone-autodetect" typ="bool"></ArgTableRow>
<ArgTableRow arg="time-zone-name" typ="enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="gmt-offset" typ="timezone"></ArgTableRow>
<ArgTableRow arg="dst-active" typ="bool"></ArgTableRow>
</ArgTable>

### system/clock/manual

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="time-zone" typ="timezone"></ArgTableRow>
<ArgTableRow arg="dst-delta" typ="timezone"></ArgTableRow>
<ArgTableRow arg="dst-start" typ="date"></ArgTableRow>
<ArgTableRow arg="dst-end" typ="date"></ArgTableRow>
</ArgTable>
