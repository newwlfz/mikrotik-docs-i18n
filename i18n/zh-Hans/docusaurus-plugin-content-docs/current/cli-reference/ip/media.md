# 媒体

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/media

**条件：** !smips
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="path" typ="file"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="friendly-name" typ="string"></ArgTableRow>
<ArgTableRow arg="allowed-ip" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="allowed-hostname" typ="string">仅允许此主机名的 IP 地址（由 DHCP 服务器识别）访问内容</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

### ip/media/settings

**条件：** !smips
**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="thumbnails" typ="string">以逗号分隔的文件名列表（应以 .jpg 结尾）。如果目录中的文件名与列表中的任何文件名匹配，则该文件被视为该目录中任何媒体文件的缩略图。</ArgTableRow>
</ArgTable>