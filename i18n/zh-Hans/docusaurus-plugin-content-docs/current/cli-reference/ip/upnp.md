# UPnP

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/upnp

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow-disable-external-interface" typ="bool"></ArgTableRow>
<ArgTableRow arg="show-dummy-rule" typ="bool"></ArgTableRow>
</ArgTable>

### ip/upnp/interfaces

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (external | internal)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="forced-ip" typ="super { ipAddr
 }"></ArgTableRow>
</ArgTable>