# Speed Test 速度测试

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/speed-test

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="address" typ="address (flags=46viD)"></ArgTableRow>
<ArgTableRow arg="connection-count" typ="num"></ArgTableRow>
<ArgTableRow arg="test-duration" typ="time"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
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