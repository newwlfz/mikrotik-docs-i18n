# 设置

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### ipv6/nd/settings

**软件包：** ipv6
**类型：** 设置目录

IPv6 ND 菜单下有一个子菜单“设置”，用于修改全局邻居发现设置。

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="router-advertisement-route-distance" typ="num">指定安装 SLAAC 默认路由时必须使用的距离。</ArgTableRow>
<ArgTableRow arg="router-advertisement-ignored-options" typ="ubit (dns, mtu)">允许您忽略特定的接收到的 ND 选项，如 DNS 和 MTU。如果 RA 包含此类选项，且在此列表中选中，则这些选项将被忽略。</ArgTableRow>
</ArgTable>