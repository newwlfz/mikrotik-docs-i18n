# 类型

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## queue/type

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="kind" typ="enum (bfifo | pfifo | red | sfq | pcq | mq-pfifo | none | codel | fq-codel | cake)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="bfifo-limit" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="pfifo-limit" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="red-limit" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="red-min-threshold" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="red-max-threshold" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="red-burst" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="red-avg-packet" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="sfq-perturb" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="sfq-allot" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="pcq-rate" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="pcq-limit" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="pcq-classifier" typ="ubit (src-address, dst-address, src-port, dst-port)"></ArgTableRow>
<ArgTableRow arg="pcq-total-limit" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="pcq-burst-rate" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="pcq-burst-threshold" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="pcq-burst-time" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="pcq-src-address-mask" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="pcq-dst-address-mask" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="pcq-src-address6-mask" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="pcq-dst-address6-mask" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="mq-pfifo-limit" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="codel-limit" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="codel-interval" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="codel-target" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="codel-ecn" typ="bool {  }"></ArgTableRow>
<ArgTableRow arg="codel-ce-threshold" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="fq-codel-limit" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="fq-codel-interval" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="fq-codel-target" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="fq-codel-ecn" typ="bool {  }"></ArgTableRow>
<ArgTableRow arg="fq-codel-ce-threshold" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="fq-codel-flows" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="fq-codel-memlimit" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="fq-codel-quantum" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="cake-bandwidth" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="cake-autorate-ingress" typ="bool {  }"></ArgTableRow>
<ArgTableRow arg="cake-overhead" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="cake-mpu" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="cake-atm" typ="enum (none | atm | ptm)"></ArgTableRow>
<ArgTableRow arg="cake-overhead-scheme" typ="multi { , enum (raw | convervative | ipoa-vcmux | ipoa-llcsnap | bridged-vcmux | bridged-llcsnap | pppoa-vcmux | pppoa-llc | pppoe-vcmux | pppoe-llcsnap | pppoe-ptm | bridged-ptm | via-ethernet | ethernet | ether-vlan | docsis) { raw:1, convervative:2, ipoa-vcmux:3, ipoa-llcsnap:4, bridged-vcmux:5, bridged-llcsnap:6, pppoa-vcmux:7, pppoa-llc:8, pppoe-vcmux:9, pppoe-llcsnap:10, pppoe-ptm:11, bridged-ptm:12, via-ethernet:13, ethernet:14, ether-vlan:15, docsis:16 }
 }"></ArgTableRow>
<ArgTableRow arg="cake-rtt" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="cake-rtt-scheme" typ="enum (none | datacentre | lan | metro | regional | internet | oceanic | satellite | interplanetary)"></ArgTableRow>
<ArgTableRow arg="cake-diffserv" typ="enum (diffserv3 | diffserv4 | diffserv8 | besteffort | precedence)"></ArgTableRow>
<ArgTableRow arg="cake-flowmode" typ="enum (flowblind | srchost | dsthost | hosts | flows | dual-srchost | dual-dsthost | triple-isolate)"></ArgTableRow>
<ArgTableRow arg="cake-nat" typ="bool {  }"></ArgTableRow>
<ArgTableRow arg="cake-wash" typ="bool {  }"></ArgTableRow>
<ArgTableRow arg="cake-ack-filter" typ="enum (none | filter | aggressive)"></ArgTableRow>
<ArgTableRow arg="cake-memlimit" typ="num {  }"></ArgTableRow>
</ArgTable>