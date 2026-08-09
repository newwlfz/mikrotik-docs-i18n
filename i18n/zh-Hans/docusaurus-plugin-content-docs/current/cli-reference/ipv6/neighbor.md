# 邻居

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ipv6/neighbor

**软件包：** ipv6
**类型：** 目录

通过 IPv6 [邻居发现](https://tools.ietf.org/html/rfc4861) 协议发现的所有节点列表，或通过配置手动添加的节点。

邻居条目的默认最大数量取决于已安装的内存大小。可通过 `/ipv6/settings/set max-neighbor-entries=x` 进行调整。详见 [IPv6 设置](./settings.md)。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="R" typ="router">路由器</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="address" typ="ip6Addr">邻居的 IPv6 地址。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">该邻居所连接到的接口名称。</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">要添加设备的 MAC 地址。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="string">
缓存条目的状态：
- **noarp** - 邻居条目有效。RouterOS 不验证此条目，但可在其生命周期到期时将其移除。
- **incomplete** - 地址解析正在进行中，邻居的链路层地址尚未确定。
- **reachable** - 邻居在最近（几十秒内）可达。
- **stale** - 不再确认邻居可达。在尝试可达性验证之前，将继续向该邻居发送流量。
- **delay** - 不再确认邻居可达，且最近已向该邻居发送流量。RouterOS 会短暂延迟探测，以允许上层协议确认可达性。
- **probe** - 不再确认邻居可达，正在发送单播邻居请求探测以验证可达性。
- **failed** - RouterOS 无法通过邻居发现协议解析邻居的 MAC 地址。
</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">指示与此邻居条目关联的 VRF。</ArgTableRow>
</ArgTable>