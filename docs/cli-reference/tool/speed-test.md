# Speed Test

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/speed-test

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="address (flags=46viD)"></ArgTableRow>
<ArgTableRow arg="connection-count" typ="num"></ArgTableRow>
<ArgTableRow arg="test-duration" typ="time"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="time-remaining" typ="time"></ArgTableRow>
<ArgTableRow arg="ping-min-avg-max" typ="string"></ArgTableRow>
<ArgTableRow arg="jitter-min-avg-max" typ="string"></ArgTableRow>
<ArgTableRow arg="loss" typ="string"></ArgTableRow>
<ArgTableRow arg="tcp-download" typ="string"></ArgTableRow>
<ArgTableRow arg="tcp-upload" typ="string"></ArgTableRow>
<ArgTableRow arg="udp-download" typ="string"></ArgTableRow>
<ArgTableRow arg="udp-upload" typ="string"></ArgTableRow>
</ArgTable>
