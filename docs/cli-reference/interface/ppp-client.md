# Ppp Client

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/ppp-client

**Package:** ppp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
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

**Package:** ppp
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="input" typ="string">sends command to modem and waits for any output before returning</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="output" typ="string"></ArgTableRow>
</ArgTable>

### interface/ppp-client/firmware-upgrade

**Package:** ppp
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="upgrade" typ="bool">perform the upgrade or just check</ArgTableRow>
<ArgTableRow arg="firmware-file" typ="file">path or url for the upgrade image</ArgTableRow>
<ArgTableRow arg="update-channel" typ="enum (stable | testing)">firmware update channel</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="installed" typ="string"></ArgTableRow>
<ArgTableRow arg="latest" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="note" typ="string"></ArgTableRow>
</ArgTable>

### interface/ppp-client/info

**Package:** ppp
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="user-command" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
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

**Package:** ppp
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
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

**Package:** ppp
**Type:** Command

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="C" typ="current">current</ArgTableRow>
<ArgTableRow arg="A" typ="available">available</ArgTableRow>
<ArgTableRow arg="F" typ="forbidden">forbidden</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="operator" typ="string"></ArgTableRow>
<ArgTableRow arg="mcc-mnc" typ="num"></ArgTableRow>
<ArgTableRow arg="access-technology" typ="string"></ArgTableRow>
<ArgTableRow arg="signal-strength" typ="num"></ArgTableRow>
</ArgTable>
