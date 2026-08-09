# Pwr Link

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### interface/pwr-link/pwr-line

**Syscap:** pwrlink
**类型:** 目录

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
<ArgTableRow arg="tx-flow-control" typ="enum (off | on | auto)"></ArgTableRow>
<ArgTableRow arg="rx-flow-control" typ="enum (off | on | auto)"></ArgTableRow>
<ArgTableRow arg="bandwidth" typ="composite { ,  }" syscap="switch"></ArgTableRow>
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

#### interface/pwr-link/pwr-line/blink

**类型:** 命令

#### interface/pwr-link/pwr-line/configure

**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="network-key" typ="string"></ArgTableRow>
<ArgTableRow arg="network-password" typ="string"></ArgTableRow>
<ArgTableRow arg="plc-cco-selection-mode" typ="enum (auto | never | always)"></ArgTableRow>
</ArgTable>

#### interface/pwr-link/pwr-line/join

**类型:** 命令

#### interface/pwr-link/pwr-line/leave

**类型:** 命令

#### interface/pwr-link/pwr-line/monitor

**类型:** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="connection-to-plc" typ="enum (ok | no-link)"></ArgTableRow>
<ArgTableRow arg="tx-flow-control" typ="bool"></ArgTableRow>
<ArgTableRow arg="rx-flow-control" typ="bool"></ArgTableRow>
<ArgTableRow arg="phy-regs" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="plc-actual-network-key" typ="string"></ArgTableRow>
<ArgTableRow arg="plc-hw-platform" typ="string"></ArgTableRow>
<ArgTableRow arg="plc-sw-platform" typ="string"></ArgTableRow>
<ArgTableRow arg="plc-fw-version" typ="string"></ArgTableRow>
<ArgTableRow arg="plc-line-freq" typ="enum (unknown | 50Hz | 60Hz)"></ArgTableRow>
<ArgTableRow arg="plc-zero-crossing" typ="enum (not-yet-detected | detected | missing)"></ArgTableRow>
<ArgTableRow arg="plc-role" typ="enum (station | proxy-coordinator | central-coordinator)"></ArgTableRow>
<ArgTableRow arg="plc-station-count" typ="num"></ArgTableRow>
<ArgTableRow arg="plc-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="plc-cco-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="plc-station-info" typ="string"></ArgTableRow>
</ArgTable>

#### interface/pwr-link/pwr-line/reset-counters

**类型:** 命令

#### interface/pwr-link/pwr-line/reset-mac-address

**类型:** 命令

#### interface/pwr-link/pwr-line/upgrade-firmware

**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="firmware-file" typ="file"></ArgTableRow>
<ArgTableRow arg="pib-file" typ="file"></ArgTableRow>
</ArgTable>