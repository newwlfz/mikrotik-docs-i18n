# Tftp

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/tftp

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ip-addresses" typ="object { alt { ip6Prefix
, ipRange
 } { ip6Prefix
, ipRange
 }
 }"></ArgTableRow>
<ArgTableRow arg="req-filename" typ="string"></ArgTableRow>
<ArgTableRow arg="real-filename" typ="string"></ArgTableRow>
<ArgTableRow arg="allow" typ="bool"></ArgTableRow>
<ArgTableRow arg="read-only" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow-rollover" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow-overwrite" typ="bool"></ArgTableRow>
<ArgTableRow arg="reading-window-size" typ="alt { enum (none | pipelining) { none:0, pipelining:tftpd::WINDOW_PIPELINING }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="hits" typ="num"></ArgTableRow>
</ArgTable>

### ip/tftp/settings

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="max-block-size" typ="enum (512 | 1454 | 4096 | 8192)">maximum block size allowed to negotiate</ArgTableRow>
</ArgTable>
