# Profile

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/profile

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="cpu" typ="enum (all | total)" syscap="smp"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="cpu" typ="num" syscap="smp"></ArgTableRow>
<ArgTableRow arg="usage" typ="num"></ArgTableRow>
</ArgTable>
