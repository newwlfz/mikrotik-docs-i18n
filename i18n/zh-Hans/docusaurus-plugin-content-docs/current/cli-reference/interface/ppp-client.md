# PPP 客户端

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/ppp-client

**软件包：** ppp
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="R" typ="running">运行中</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="max-mru" typ="num"></ArgTableRow>
<ArgTableRow arg="mrru" typ="num"></ArgTableRow>
<ArgTableRow arg="port" typ="enum"></ArgTableRow>
<ArgTableRow arg="data-channel" typ="num"></ArgTableRow>
<ArgTableRow arg="info-channel" typ="num"></ArgTableRow>
<ArgTableRow arg="network-mode" typ="enum (lte-m | nb-iot | auto)"></ArgTableRow>
<ArgTableRow arg="apn" typ="string"></ArgTableRow>
<ArgTableRow arg="pin" typ="string"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="remote-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="phone" typ="string"></ArgTableRow>
<ArgTableRow arg="dial-command" typ="string"></ArgTableRow>
<ArgTableRow arg="modem-init" typ="string"></ArgTableRow>
<ArgTableRow arg="null-modem" typ="bool"></ArgTableRow>
<ArgTableRow arg="dial-on-demand" typ="bool"></ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool"></ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="bool"></ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="num"></ArgTableRow>
<ArgTableRow arg="allow" typ="ubit (pap, chap, mschap1, mschap2)"></ArgTableRow>
</ArgTable>

### interface/ppp-client/at-chat

**软件包：** ppp
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="input" typ="string">向调制解调器发送命令，并在返回前等待任何输出</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="output" typ="string"></ArgTableRow>
</ArgTable>

### interface/ppp-client/firmware-upgrade

**软件包：** ppp
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="upgrade" typ="bool">执行升级或仅进行检查</ArgTableRow>
<ArgTableRow arg="firmware-file" typ="file">升级镜像的路径或 URL</ArgTableRow>
<ArgTableRow arg="update-channel" typ="enum (stable | testing)">固件更新通道</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="installed" typ="string"></ArgTableRow>
<ArgTableRow arg="latest" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="note" typ="string"></ArgTableRow>
</ArgTable>

### interface/ppp-client/info

**软件包：** ppp
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="user-command" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="modem-status" typ="string"></ArgTableRow>
<ArgTableRow arg="pin-status" typ="string"></ArgTableRow>
<ArgTableRow arg="functionality" typ="string"></ArgTableRow>
<ArgTableRow arg="manufacturer" typ="string"></ArgTableRow>
<ArgTableRow arg="model" typ="string"></ArgTableRow>
<ArgTableRow arg="revision" typ="string"></ArgTableRow>
<ArgTableRow arg="serial-number" typ="string"></ArgTableRow>
<ArgTableRow arg="current-operator" typ="string"></ArgTableRow>
<ArgTableRow arg="phy-cellid" typ="num"></ArgTableRow>
<ArgTableRow arg="current-cellid" typ="num"></ArgTableRow>
<ArgTableRow arg="access-technology" typ="string"></ArgTableRow>
<ArgTableRow arg="imsi" typ="string"></ArgTableRow>
<ArgTableRow arg="signal-strength" typ="string"></ArgTableRow>
<ArgTableRow arg="frame-error-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="user-command" typ="string"></ArgTableRow>
<ArgTableRow arg="rsrp" typ="num"></ArgTableRow>
<ArgTableRow arg="rsrq" typ="num"></ArgTableRow>
<ArgTableRow arg="sinr" typ="num"></ArgTableRow>
<ArgTableRow arg="earfcn" typ="num"></ArgTableRow>
</ArgTable>

### interface/ppp-client/monitor

**软件包：** ppp
**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="encoding" typ="string"></ArgTableRow>
<ArgTableRow arg="connect-speed" typ="num"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="mru" typ="num"></ArgTableRow>
<ArgTableRow arg="local-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="remote-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="local-ipv6-address" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="remote-ipv6-address" typ="ip6Addr"></ArgTableRow>
</ArgTable>

### interface/ppp-client/scan

**软件包：** ppp
**类型：** 命令

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="C" typ="current">当前</ArgTableRow>
<ArgTableRow arg="A" typ="available">可用</ArgTableRow>
<ArgTableRow arg="F" typ="forbidden">禁止</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="operator" typ="string"></ArgTableRow>
<ArgTableRow arg="mcc-mnc" typ="num"></ArgTableRow>
<ArgTableRow arg="access-technology" typ="string"></ArgTableRow>
<ArgTableRow arg="signal-strength" typ="num"></ArgTableRow>
</ArgTable>