# Apptraffic

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### tool/apptraffic/stats

**Conditions:** !mmips, !powerpc, !smips, !mipsel
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="application" typ="string"></ArgTableRow>
<ArgTableRow arg="category" typ="string"></ArgTableRow>
<ArgTableRow arg="bytes-out" typ="num"></ArgTableRow>
<ArgTableRow arg="bytes-in" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-out" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-in" typ="num"></ArgTableRow>
<ArgTableRow arg="percent-out" typ="num"></ArgTableRow>
<ArgTableRow arg="percent-in" typ="num"></ArgTableRow>
</ArgTable>

#### tool/apptraffic/stats/categories

**Conditions:** !mmips, !powerpc, !smips, !mipsel
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="category" typ="string"></ArgTableRow>
<ArgTableRow arg="bytes-out" typ="num"></ArgTableRow>
<ArgTableRow arg="bytes-in" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-out" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-in" typ="num"></ArgTableRow>
<ArgTableRow arg="percent-out" typ="num"></ArgTableRow>
<ArgTableRow arg="percent-in" typ="num"></ArgTableRow>
</ArgTable>

#### tool/apptraffic/stats/clear

**Conditions:** !mmips, !powerpc, !smips, !mipsel
**Type:** Command
