# RPKI

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/rpki

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="group" typ="enum">分配给数据库的组。</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46)">RTR 服务器地址。</ArgTableRow>
<ArgTableRow arg="port" typ="num">RTR 服务器端口。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1">用于绑定连接的 VRF 表。</ArgTableRow>
<ArgTableRow arg="preference" typ="num" unset="1">当存在多个 RTR 源时，数值越高表示优先级越高。如果未配置优先级，RouterOS 优先选择组内最低的远程 IP。如果远程 IP 相同，RouterOS 优先选择最低的远程端口。</ArgTableRow>
<ArgTableRow arg="refresh-interval" typ="num" unset="1">轮询验证器以获取最新数据的间隔（秒）。</ArgTableRow>
<ArgTableRow arg="retry-interval" typ="num" unset="1">从验证器获取数据失败后重试的间隔（秒）。</ArgTableRow>
<ArgTableRow arg="expire-interval" typ="num" unset="1">当未从验证器收到有效更新时，已轮询数据保持有效的间隔（秒）。</ArgTableRow>
</ArgTable>

### routing/rpki/rpki-check

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="prefix" typ="address (flags=46/)"></ArgTableRow>
<ArgTableRow arg="group" typ="enum"></ArgTableRow>
<ArgTableRow arg="origin-as" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="result" typ="string"></ArgTableRow>
</ArgTable>

### routing/rpki/rpki-query

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="group" typ="enum"></ArgTableRow>
<ArgTableRow arg="prefix" typ="address (flags=46/)"></ArgTableRow>
<ArgTableRow arg="exact" typ="switch"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="results" typ="string"></ArgTableRow>
</ArgTable>

### routing/rpki/session

**类型：** 目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="group" typ="enum"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (idle | connecting | prepare | loading | sync | error)"></ArgTableRow>
<ArgTableRow arg="version" typ="num"></ArgTableRow>
<ArgTableRow arg="session" typ="num"></ArgTableRow>
<ArgTableRow arg="serial" typ="num"></ArgTableRow>
<ArgTableRow arg="expires" typ="time"></ArgTableRow>
</ArgTable>