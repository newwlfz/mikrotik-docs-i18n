# Fantasy

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/fantasy

**类型：** 目录

Fantasy 菜单是一种用于测试目的而生成大量路由的便捷方式。与脚本相比，这种方法的主要优势在于生成速度快且简单。只需禁用 fantasy 规则，即可轻松移除所有由 fantasy 生成的路由。

Fantasy 使用基于哈希路由序列号、种子及其他参数的随机生成器。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="address (flags=46it/)">将从中生成路由的前缀。</ArgTableRow>
<ArgTableRow arg="prefix-length" typ="range">生成路由的前缀长度（可指定为整数范围）。例如 `dst-address=192.168.0.0/16` 和 `prefix-length=24` 将从 `192.168.0.0/16` 子网生成 /24 路由。</ArgTableRow>
<ArgTableRow arg="gateway" typ="address (flags=46iv/)"></ArgTableRow>
<ArgTableRow arg="scope" typ="range">要设置的 scope；可设置为范围。</ArgTableRow>
<ArgTableRow arg="target-scope" typ="range">要设置的 target-scope；可设置为范围。</ArgTableRow>
<ArgTableRow arg="instance-id" typ="range"></ArgTableRow>
<ArgTableRow arg="dealer-id" typ="range"></ArgTableRow>
<ArgTableRow arg="seed" typ="string">随机生成器种子。</ArgTableRow>
<ArgTableRow arg="count" typ="num"></ArgTableRow>
<ArgTableRow arg="offset" typ="num">路由序列号偏移量。</ArgTableRow>
<ArgTableRow arg="priv-offs" typ="range"></ArgTableRow>
<ArgTableRow arg="priv-size" typ="range"></ArgTableRow>
<ArgTableRow arg="use-hold" typ="bool"></ArgTableRow>
</ArgTable>