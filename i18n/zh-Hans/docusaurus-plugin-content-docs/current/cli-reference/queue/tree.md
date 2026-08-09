# 树

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## queue/tree

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="parent" typ="enum (global)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="packet-mark" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="limit-at" typ="num"></ArgTableRow>
<ArgTableRow arg="queue" typ="enum"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="max-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="burst-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="burst-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="burst-time" typ="time"></ArgTableRow>
<ArgTableRow arg="bucket-size" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="packets" typ="num"></ArgTableRow>
<ArgTableRow arg="dropped" typ="num"></ArgTableRow>
<ArgTableRow arg="rate" typ="num"></ArgTableRow>
<ArgTableRow arg="packet-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="queued-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="queued-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="pcq-queues" typ="num"></ArgTableRow>
</ArgTable>

### queue/tree/reset-counters

**类型：** 命令

### queue/tree/reset-counters-all

**类型：** 命令