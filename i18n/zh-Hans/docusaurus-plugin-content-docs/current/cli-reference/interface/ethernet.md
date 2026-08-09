# 以太网

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/ethernet

**适用条件：** i386
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="R" typ="running">运行中</ArgTableRow>
<ArgTableRow arg="S" typ="slave">从属</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="orig-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="disable-running-check" typ="bool" syscap="uefi"></ArgTableRow>
<ArgTableRow arg="auto-negotiation" typ="bool"></ArgTableRow>
<ArgTableRow arg="advertise" typ="multi { , array-id,  }"></ArgTableRow>
<ArgTableRow arg="tx-flow-control" typ="enum (off | on | auto)"></ArgTableRow>
<ArgTableRow arg="rx-flow-control" typ="enum (off | on | auto)"></ArgTableRow>
<ArgTableRow arg="cable-settings" typ="enum (short | standard | default)"></ArgTableRow>
<ArgTableRow arg="mdix-enable" typ="bool"></ArgTableRow>
<ArgTableRow arg="speed" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="bandwidth" typ="composite { ,  }" syscap="switch"></ArgTableRow>
<ArgTableRow arg="poe-out" typ="enum (off | auto-on | forced-on | forced-on-a | forced-on-bt)" syscap="poe"></ArgTableRow>
<ArgTableRow arg="poe-voltage" typ="enum (auto | low | high)" syscap="poe"></ArgTableRow>
<ArgTableRow arg="poe-priority" typ="num" syscap="poe"></ArgTableRow>
<ArgTableRow arg="power-cycle-ping-enabled" typ="bool" syscap="poe"></ArgTableRow>
<ArgTableRow arg="power-cycle-ping-address" typ="alt { ipAddr
, ip6Addr
, macAddr
 }" syscap="poe"></ArgTableRow>
<ArgTableRow arg="power-cycle-ping-timeout" typ="time" syscap="poe"></ArgTableRow>
<ArgTableRow arg="power-cycle-interval" typ="alt { enum (none) { none:0 }
, time
 }" syscap="poe"></ArgTableRow>
<ArgTableRow arg="sfp-rate-select" typ="bool"></ArgTableRow>
<ArgTableRow arg="sfp-ignore-rx-los" typ="bool"></ArgTableRow>
<ArgTableRow arg="combo-mode" typ="enum (auto | copper | sfp)"></ArgTableRow>
<ArgTableRow arg="fec-mode" typ="enum (off | auto | fec74 | fec91)"></ArgTableRow>
<ArgTableRow arg="sfp-shutdown-temperature" typ="num"></ArgTableRow>
<ArgTableRow arg="passthrough-interface" typ="iface_enum { none:0 }" syscap="pcie_passthrough"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp)"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { enum (auto) { auto:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="loop-protect" typ="enum (default | off | on)"></ArgTableRow>
<ArgTableRow arg="loop-protect-send-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="loop-protect-disable-time" typ="time"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="default-name" typ="string"></ArgTableRow>
<ArgTableRow arg="switch" typ="enum" syscap="switch"></ArgTableRow>
<ArgTableRow arg="loop-protect-status" typ="enum (off | on | disabled)"></ArgTableRow>
</ArgTable>

### interface/ethernet/switch

**适用条件：** !smips
**系统能力：** multiswitch
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mirror-source" typ="iface_enum { none:0 }" syscap="switch-mirror1"></ArgTableRow>
<ArgTableRow arg="mirror-target" typ="iface_enum { none:0, cpu:0xffffffff }" syscap="switch-mirror-prestera"></ArgTableRow>
<ArgTableRow arg="mirror-egress-target" typ="enum (none)" syscap="switch-mv88e6xxx"></ArgTableRow>
<ArgTableRow arg="rspan" typ="bool" syscap="switch-mirror-prestera"></ArgTableRow>
<ArgTableRow arg="rspan-ingress-vlan-id" typ="num" syscap="switch-mirror-prestera"></ArgTableRow>
<ArgTableRow arg="rspan-egress-vlan-id" typ="num" syscap="switch-mirror-prestera"></ArgTableRow>
<ArgTableRow arg="switch-all-ports" typ="bool"></ArgTableRow>
<ArgTableRow arg="cpu-flow-control" typ="bool" syscap="switch-mv88e6xxx"></ArgTableRow>
<ArgTableRow arg="l3-hw-offloading" typ="bool" syscap="crs_prestera">三层硬件卸载</ArgTableRow>
<ArgTableRow arg="qos-hw-offloading" typ="bool" syscap="crs_prestera">服务质量硬件卸载</ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="bridge-type" typ="enum (customer-vid-used-as-lookup-vid | service-vid-used-as-lookup-vid)"></ArgTableRow>
<ArgTableRow arg="drop-if-no-vlan-assignment-on-ports" typ="multi { array-id,  }"></ArgTableRow>
<ArgTableRow arg="drop-if-invalid-or-src-port-not-member-of-vlan-on-ports" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="unknown-vlan-lookup-mode" typ="bool"></ArgTableRow>
<ArgTableRow arg="forward-unknown-vlan" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-svid-in-one2one-vlan-lookup" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-cvid-in-one2one-vlan-lookup" typ="bool"></ArgTableRow>
<ArgTableRow arg="mac-level-isolation" typ="bool"></ArgTableRow>
<ArgTableRow arg="multicast-lookup-mode" typ="enum (dst-mac-and-vid-always | dst-ip-and-vid-for-ipv4)"></ArgTableRow>
<ArgTableRow arg="override-existing-when-ufdb-full" typ="bool"></ArgTableRow>
<ArgTableRow arg="unicast-fdb-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="ingress-mirror0" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="ingress-mirror1" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="ingress-mirror-ratio" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="egress-mirror0" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="egress-mirror1" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="egress-mirror-ratio" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="fdb-uses" typ="enum (mirror0 | mirror1)"></ArgTableRow>
<ArgTableRow arg="vlan-uses" typ="enum (mirror0 | mirror1)"></ArgTableRow>
<ArgTableRow arg="mirror-egress-if-ingress-mirrored" typ="bool"></ArgTableRow>
<ArgTableRow arg="mirror-tx-on-mirror-port" typ="bool"></ArgTableRow>
<ArgTableRow arg="mirrored-packet-qos-priority" typ="num"></ArgTableRow>
<ArgTableRow arg="mirrored-packet-drop-precedence" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="bypass-vlan-ingress-filter-for" typ="ubit ()"></ArgTableRow>
<ArgTableRow arg="bypass-ingress-port-policing-for" typ="ubit ()"></ArgTableRow>
<ArgTableRow arg="bypass-l2-security-check-filter-for" typ="ubit ()"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="type" typ="enum (ADMtek | IC-Plus-175C | IC-Plus-178C | IC-Plus-175D | Atheros-8316 | Atheros-7240 | Atheros-8227 | Atheros-8327 | Atheros-8236 | QCA-8513L | Atheros-8327N | QCA-8519 | QCA-8511 | QCA-8337 | MediaTek-MT7621 | Realtek-RTL8367 | Marvell-98DX3236 | Marvell-98DX8216 | Marvell-98DX8208 | Marvell-98DX8332 | Marvell-98DX8212 | Marvell-98DX3257 | IPQ-PPE | Marvell-98DX8525 | Marvell-98PX1012 | Marvell-98DX4310 | Marvell-98DX224S | Marvell-98DX226S | Marvell-88E6393X | Marvell-98DX3255 | Marvell-88E6191X | Marvell-98DX2528 | Marvell-98CX8410 | Marvell-88E6341 | MediaTek-MT7531 | Marvell-88E6190 | Marvell-98DX7335 | Marvell-98DX3510 | Marvell-98DX3550 | MediaTek-MT7531AE | Marvell-98DX1508M | Alder | Marvell-98DX3530 | Marvell-98DX4550 | QCA-8386 | EN7523 | Marvell-98DX2521 | Marvell-98DX2556 | Marvell-98DX2588)"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (QCA-8513L | QCA-8519 | QCA-8511)"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/qos

**系统能力：** crs_prestera
**类型：** 目录

##### interface/ethernet/switch/qos/profile

**系统能力：** crs_prestera
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">硬件卸载</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">QoS 配置文件名称</ArgTableRow>
<ArgTableRow arg="pcp" typ="num"></ArgTableRow>
<ArgTableRow arg="dscp" typ="num"></ArgTableRow>
<ArgTableRow arg="traffic-class" typ="num"></ArgTableRow>
<ArgTableRow arg="automap" typ="bool">是否应自动将 DSCP 和 PCP 值映射到配置文件？</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="hw-id" typ="num"></ArgTableRow>
</ArgTable>

##### interface/ethernet/switch/qos/map

**系统能力：** crs_prestera
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">硬件卸载</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">QoS 映射名称</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="hw-id" typ="num"></ArgTableRow>
</ArgTable>

###### interface/ethernet/switch/qos/map/vlan

**系统能力：** crs_prestera
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">硬件卸载</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="map" typ="enum"></ArgTableRow>
<ArgTableRow arg="pcp" typ="multi { , , range [0 .. 7]
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="dei-only" typ="bool">仅在 DEI/CFI 位已设置时进行映射</ArgTableRow>
<ArgTableRow arg="profile" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>

###### interface/ethernet/switch/qos/map/ip

**系统能力：** crs_prestera
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">硬件卸载</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="map" typ="enum"></ArgTableRow>
<ArgTableRow arg="dscp" typ="multi { , , range [0 .. 63]
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>

##### interface/ethernet/switch/qos/priority-flow-control

**系统能力：** !prestera-ac3
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">硬件卸载</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">PFC 配置文件名称</ArgTableRow>
<ArgTableRow arg="traffic-class" typ="multi { array-id, num [ .. 7]
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="rx" typ="bool">接收（并遵守）PFC 帧</ArgTableRow>
<ArgTableRow arg="tx" typ="bool">发送 PFC 帧</ArgTableRow>
<ArgTableRow arg="pause-threshold" typ="alt { , num [ .. 100]
, num [1536 .. ]
 }">当排队数据包的总大小达到此阈值时，发送暂停帧（XOFF）</ArgTableRow>
<ArgTableRow arg="resume-threshold" typ="alt { , num [ .. 100]
, num [256 .. ]
 }">当排队数据包的总大小降至此阈值时，发送恢复帧（XON）</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="hw-id" typ="num"></ArgTableRow>
</ArgTable>

##### interface/ethernet/switch/qos/tx-manager

**系统能力：** crs_prestera
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">硬件卸载</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">Tx 管理器名称</ArgTableRow>
<ArgTableRow arg="queue-buffers" typ="alt { num [ .. 100]
, num [1536 .. 67108864]
 }">为 Tx 管理器独占保留的字节数（或百分比）。该值将分配到所分配端口的活动队列上。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="hw-id" typ="num"></ArgTableRow>
</ArgTable>

###### interface/ethernet/switch/qos/tx-manager/queue

**系统能力：** crs_prestera
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">硬件卸载</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="schedule" typ="enum (strict-priority | low-priority-group | high-priority-group)">按流量类别的严格优先级或组内轮询调度 Tx</ArgTableRow>
<ArgTableRow arg="weight" typ="num">优先级组的权重值</ArgTableRow>
<ArgTableRow arg="queue-buffers" typ="alt { num [ .. 100]
, num [1536 .. 67108864]
 }" syscap="!prestera-cpss">每队列保留缓冲区。为队列独占保留的字节数（或 tx-manager 的百分比）。</ArgTableRow>
<ArgTableRow arg="use-shared-buffers" typ="bool" syscap="!prestera-cpss">当端口或队列缓冲区已满时，允许使用共享缓冲区池</ArgTableRow>
<ArgTableRow arg="wred" typ="bool" syscap="!prestera-ac3">加权随机早期检测</ArgTableRow>
<ArgTableRow arg="ecn" typ="bool" syscap="!prestera-ac3">显式拥塞通知 - ECN 标记</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="tx-manager" typ="enum"></ArgTableRow>
<ArgTableRow arg="traffic-class" typ="num"></ArgTableRow>
<ArgTableRow arg="wred-actual" typ="bool" syscap="!prestera-ac3">实际 WRED 值</ArgTableRow>
<ArgTableRow arg="ecn-actual" typ="bool" syscap="!prestera-ac3">实际 ECN 值</ArgTableRow>
</ArgTable>

##### interface/ethernet/switch/qos/settings

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="multicast-buffers" typ="num">用于组播流量的最大数据包缓冲区数量（占总缓冲区内存的百分比）</ArgTableRow>
<ArgTableRow arg="mirror-buffers" typ="num" syscap="!prestera-cpss">用于镜像流量的最大数据包缓冲区数量（占总缓冲区内存的百分比）</ArgTableRow>
<ArgTableRow arg="mirror-profile" typ="enum">应用于镜像数据包的 QoS 配置文件</ArgTableRow>
<ArgTableRow arg="shared-buffers" typ="num">端口之间共享的数据包缓冲区数量（占总缓冲区内存的百分比）</ArgTableRow>
<ArgTableRow arg="lossless-buffers" typ="num" syscap="!prestera-ac3">无损共享池的大小（占共享缓冲区的百分比）</ArgTableRow>
<ArgTableRow arg="lossless-traffic-class" typ="multi { array-id, num [ .. 7]
 }" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="wred-threshold" typ="enum (low | medium | high)" syscap="!prestera-ac3">开始随机尾部丢弃或 ECN 标记的相对队列填充级别</ArgTableRow>
<ArgTableRow arg="total-desc" typ="num" syscap="(option and !prestera-cpss)"></ArgTableRow>
<ArgTableRow arg="total-buff" typ="num" syscap="(option and !prestera-cpss)"></ArgTableRow>
</ArgTable>

##### interface/ethernet/switch/qos/monitor

**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="total-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="total-packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="total-byte-cap" typ="num"></ArgTableRow>
<ArgTableRow arg="total-byte-use" typ="num"></ArgTableRow>
<ArgTableRow arg="multicast-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="multicast-packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="multicast-byte-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="multicast-byte-use" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="mirror-ingress-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="mirror-ingress-packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="mirror-ingress-byte-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="mirror-ingress-byte-use" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="mirror-egress-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="mirror-egress-packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="mirror-egress-byte-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="mirror-egress-byte-use" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="shared-packet-cap" typ="num" syscap="prestera-ac3"></ArgTableRow>
<ArgTableRow arg="shared-packet-use" typ="num" syscap="prestera-ac3"></ArgTableRow>
<ArgTableRow arg="shared-byte-cap" typ="num" syscap="prestera-ac3"></ArgTableRow>
<ArgTableRow arg="shared-byte-use" typ="num" syscap="prestera-ac3"></ArgTableRow>
<ArgTableRow arg="lossy-pool-packet-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="lossy-pool-packet-use" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="lossless-pool-packet-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="lossless-pool-packet-use" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="lossy-pool-byte-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="lossy-pool-byte-use" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="lossless-pool-byte-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="lossless-pool-byte-use" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="wred-packet-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="wred-byte-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
</ArgTable>

##### interface/ethernet/switch/qos/port

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
<ArgTableRow arg="R" typ="running">运行中</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="profile" typ="enum" syscap="crs_prestera">默认分配给入站数据包的 QoS 配置文件</ArgTableRow>
<ArgTableRow arg="map" typ="enum" syscap="crs_prestera">QoS 数据包到配置文件映射</ArgTableRow>
<ArgTableRow arg="trust-l2" typ="enum (ignore | trust | keep)" syscap="crs_prestera">信任二层头部（PCP）用于 QoS 映射</ArgTableRow>
<ArgTableRow arg="trust-l3" typ="enum (ignore | trust | keep)" syscap="crs_prestera">信任三层头部（DSCP）用于 QoS 映射</ArgTableRow>
<ArgTableRow arg="tx-manager" typ="enum" syscap="crs_prestera">此端口出站流量的 QoS Tx 管理器</ArgTableRow>
<ArgTableRow arg="pfc" typ="enum" syscap="!prestera-ac3">此端口入站流量的优先级流控制配置文件</ArgTableRow>
<ArgTableRow arg="egress-rate-queue0" typ="num" syscap="switch-rate"></ArgTableRow>
<ArgTableRow arg="egress-rate-queue1" typ="num" syscap="switch-rate"></ArgTableRow>
<ArgTableRow arg="egress-rate-queue2" typ="num" syscap="switch-rate"></ArgTableRow>
<ArgTableRow arg="egress-rate-queue3" typ="num" syscap="switch-rate"></ArgTableRow>
<ArgTableRow arg="egress-rate-queue4" typ="num" syscap="switch-rate"></ArgTableRow>
<ArgTableRow arg="egress-rate-queue5" typ="num" syscap="switch-rate"></ArgTableRow>
<ArgTableRow arg="egress-rate-queue6" typ="num" syscap="switch-rate"></ArgTableRow>
<ArgTableRow arg="egress-rate-queue7" typ="num" syscap="switch-rate"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="switch" typ="enum"></ArgTableRow>
<ArgTableRow arg="tx-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="byte-use" typ="num"></ArgTableRow>
<ArgTableRow arg="queue0-shared-packet-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="queue1-shared-packet-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="queue2-shared-packet-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="queue3-shared-packet-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="queue4-shared-packet-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="queue5-shared-packet-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="queue6-shared-packet-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="queue7-shared-packet-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="queue0-shared-byte-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue1-shared-byte-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue2-shared-byte-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue3-shared-byte-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue4-shared-byte-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue5-shared-byte-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue6-shared-byte-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue7-shared-byte-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue0-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue1-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue2-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue3-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue4-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue5-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue6-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue7-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue0-byte-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue1-byte-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue2-byte-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue3-byte-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue4-byte-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue5-byte-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue6-byte-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue7-byte-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue0-packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue1-packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue2-packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue3-packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue4-packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue5-packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue6-packet-use" typ="num" syscap="!prestera-cpss"></Arg