# Gmp

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/gmp

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interfaces" typ="object { iface_enum {  } {  }
 }">接口名称，支持多个接口和接口列表。</ArgTableRow>
<ArgTableRow arg="groups" typ="object { address (flags=46)
 }">接口使用的组播组地址，支持多个组地址。</ArgTableRow>
<ArgTableRow arg="exclude" typ="switch">当设置 `exclude` 时，接口预期拒绝来自配置的 `sources` 的组播数据。当未使用此选项时，接口将为配置的 `sources` 发出特定源加入请求。</ArgTableRow>
<ArgTableRow arg="sources" typ="object { address (flags=46)
 }" unset="1">接口使用的源地址列表，支持多个源地址。此设置仅在 IGMPv3 或 MLDv2 协议激活时生效。</ArgTableRow>
</ArgTable>