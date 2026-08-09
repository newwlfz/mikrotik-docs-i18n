# 跟踪

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

#### ip/firewall/connection/tracking

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="enabled" typ="枚举 (auto | yes | no)"></ArgTableRow>
<ArgTableRow arg="tcp-syn-sent-timeout" typ="时间"></ArgTableRow>
<ArgTableRow arg="tcp-syn-received-timeout" typ="时间"></ArgTableRow>
<ArgTableRow arg="tcp-established-timeout" typ="时间"></ArgTableRow>
<ArgTableRow arg="tcp-fin-wait-timeout" typ="时间"></ArgTableRow>
<ArgTableRow arg="tcp-close-wait-timeout" typ="时间"></ArgTableRow>
<ArgTableRow arg="tcp-last-ack-timeout" typ="时间"></ArgTableRow>
<ArgTableRow arg="tcp-time-wait-timeout" typ="时间"></ArgTableRow>
<ArgTableRow arg="tcp-close-timeout" typ="时间"></ArgTableRow>
<ArgTableRow arg="tcp-max-retrans-timeout" typ="时间"></ArgTableRow>
<ArgTableRow arg="tcp-unacked-timeout" typ="时间"></ArgTableRow>
<ArgTableRow arg="loose-tcp-tracking" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="liberal-tcp-tracking" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="udp-timeout" typ="时间"></ArgTableRow>
<ArgTableRow arg="udp-stream-timeout" typ="时间"></ArgTableRow>
<ArgTableRow arg="icmp-timeout" typ="时间"></ArgTableRow>
<ArgTableRow arg="generic-timeout" typ="时间"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="active-ipv4" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="active-ipv6" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="max-entries" typ="数值"></ArgTableRow>
<ArgTableRow arg="total-entries" typ="数值"></ArgTableRow>
<ArgTableRow arg="total-ip4-entries" typ="数值"></ArgTableRow>
<ArgTableRow arg="total-ip6-entries" typ="数值"></ArgTableRow>
</ArgTable>