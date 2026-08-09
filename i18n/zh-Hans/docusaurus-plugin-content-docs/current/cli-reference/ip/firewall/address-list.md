# 地址列表

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### ip/firewall/address-list

**类型：** 目录

防火墙地址列表允许用户创建一组IP地址，并将其归并到一个共同的名称下。防火墙过滤、mangle 和 NAT 功能随后可以使用这些地址列表来匹配数据包。

地址列表记录也可以通过 NAT、Mangle 和 Filter 功能中的 `action=add-src-to-address-list` 或 `action=add-dst-to-address-list` 项目动态更新。

带有 `add-src-to-address-list` 或 `add-dst-to-address-list` 操作的防火墙规则以透传模式工作，这意味着匹配的数据包将被传递给后续的防火墙规则。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="list" typ="enum" mandatory="1">IP地址将被添加到的地址列表的名称。</ArgTableRow>
<ArgTableRow arg="address" typ="alt { ipRange
, string
 }">要添加到地址列表的单个IP地址或IP范围，或一个DNS名称。例如，您可以输入 `192.168.0.0-192.168.1.255`，保存时它会自动将输入条目修改为 192.168.0.0/23。IP-IP范围仅支持IPv4地址。</ArgTableRow>
<ArgTableRow arg="timeout" typ="time">地址将从地址列表中移除的时间。如果未指定超时时间，地址将永久存储在地址列表中；否则，地址将存储在RAM中，并在系统重启后被移除。</ArgTableRow>
<ArgTableRow arg="dynamic" typ="bool">该条目是否为动态创建。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="creation-time" typ="date">条目创建的时间。</ArgTableRow>
</ArgTable>