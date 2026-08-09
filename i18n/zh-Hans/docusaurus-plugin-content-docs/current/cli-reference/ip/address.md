# 地址

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/address

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="S" typ="slave">该地址是否属于某个作为其他主接口从属端口的接口。</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="address" typ="composite { ,  }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="network" typ="ipAddr">网络地址，由地址参数结合地址本身及子网掩码计算得出。</ArgTableRow>
<ArgTableRow arg="netmask" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="broadcast" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">指定配置IPv4地址的接口。您可以从路由器上可用的接口池中选择。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="actual-interface" typ="iface_enum">地址实际配置所在的接口。例如，如果地址配置在以太网接口上，且该以太网接口被添加到桥接中，则实际接口为桥接而非以太网。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">指示此IP地址关联的VRF。</ArgTableRow>
</ArgTable>