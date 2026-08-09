# Lte

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/lte

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="pin" typ="string"></ArgTableRow>
<ArgTableRow arg="apn-profiles" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="modem-init" typ="string">string to send upon modem initialization</ArgTableRow>
<ArgTableRow arg="operator" typ="string">operator locking, use numeric value: mccmnc</ArgTableRow>
<ArgTableRow arg="allow-roaming" typ="bool"></ArgTableRow>
<ArgTableRow arg="sms-read" typ="bool">This setting is ignored if any interface is enabled in /tool/sms</ArgTableRow>
<ArgTableRow arg="sms-protocol" typ="enum (mbim | at | auto)"></ArgTableRow>
<ArgTableRow arg="network-mode" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="band" typ="multi { array-id, enum
 }">LTE band</ArgTableRow>
<ArgTableRow arg="nr-band" typ="multi { array-id, enum
 }">NR band</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="default-name" typ="string"></ArgTableRow>
<ArgTableRow arg="master" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="advertised-mtu" typ="num"></ArgTableRow>
</ArgTable>

### interface/lte/apn

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="apn" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-network-apn" typ="bool">in LTE mode use APN provided by the network</ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool"></ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="ip-type" typ="enum (ipv4 | ipv6 | auto)">requested PDN type</ArgTableRow>
<ArgTableRow arg="authentication" typ="enum (none | pap | chap)"></ArgTableRow>
<ArgTableRow arg="user" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="password" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="passthrough-interface" typ="iface_enum { none:0 }"></ArgTableRow>
<ArgTableRow arg="passthrough-mac" typ="alt { , bool
, macAddr
 }">auto will learn MAC from first packet</ArgTableRow>
<ArgTableRow arg="passthrough-subnet-size" typ="alt { enum (auto | 32) { auto:0, 32:32 }
, num [16 .. 32]
 }"></ArgTableRow>
<ArgTableRow arg="ipv6-interface" typ="iface_enum { none:0 }">interface on which to advertise IPv6 prefix</ArgTableRow>
</ArgTable>

### interface/lte/at-chat

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="input" typ="string">sends command to modem and waits for any output before returning</ArgTableRow>
<ArgTableRow arg="wait" typ="alt { enum (no | yes) { no:0, yes:3 }
, time [ .. 255]
 }">always wait 3s</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="output" typ="string"></ArgTableRow>
</ArgTable>

### interface/lte/cell-monitor

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="max-age" typ="time"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="phy-cellid" typ="num"></ArgTableRow>
<ArgTableRow arg="band" typ="string"></ArgTableRow>
<ArgTableRow arg="psc" typ="num"></ArgTableRow>
<ArgTableRow arg="earfcn" typ="string"></ArgTableRow>
<ArgTableRow arg="rsrp" typ="num"></ArgTableRow>
<ArgTableRow arg="rsrq" typ="num"></ArgTableRow>
<ArgTableRow arg="rssi" typ="num"></ArgTableRow>
<ArgTableRow arg="sinr" typ="num"></ArgTableRow>
<ArgTableRow arg="rscp" typ="num"></ArgTableRow>
<ArgTableRow arg="age" typ="time"></ArgTableRow>
</ArgTable>

### interface/lte/esim

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="A" typ="active">active</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="nickname" typ="string"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="spn" typ="string"></ArgTableRow>
<ArgTableRow arg="iccid" typ="string"></ArgTableRow>
</ArgTable>

#### interface/lte/esim/activate

**Conditions:** !smips
**Type:** Command

#### interface/lte/esim/deactivate

**Conditions:** !smips
**Type:** Command

#### interface/lte/esim/delete

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="force-delete" typ="bool">disables profile before deleting it, default: no</ArgTableRow>
</ArgTable>

#### interface/lte/esim/esim-id

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="eid" typ="string"></ArgTableRow>
</ArgTable>

#### interface/lte/esim/provision

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="activation-code" typ="string">Profile activation code. Example: LPA:1$server.example.io$ABCD10EFGHI5KL6M</ArgTableRow>
<ArgTableRow arg="activate" typ="bool">Activate newly created profile after it is provisioned (default: yes)</ArgTableRow>
<ArgTableRow arg="sm-dp-plus" typ="string">SM-DP+ server hostname. Example: sm-dp-plus=server.example.io</ArgTableRow>
<ArgTableRow arg="matching-id" typ="string">An activation code token. Example: matching-id=ABCD10EFGHI5KL6M</ArgTableRow>
<ArgTableRow arg="confirmation-code" typ="string">An optional code supplied by the operator</ArgTableRow>
<ArgTableRow arg="sm-dp-plus-oid" typ="string">An optional SM-DP+ supplied by the operator</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="iccid" typ="string"></ArgTableRow>
<ArgTableRow arg="spn" typ="string"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

#### interface/lte/esim/refresh-profile-list

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
</ArgTable>

#### interface/lte/esim/send-notifications

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
</ArgTable>

#### interface/lte/esim/set-nickname

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="nickname" typ="string"></ArgTableRow>
</ArgTable>

### interface/lte/firmware-upgrade

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="upgrade" typ="bool">perform the upgrade or just check</ArgTableRow>
<ArgTableRow arg="firmware-file" typ="file">path or url for the upgrade image</ArgTableRow>
<ArgTableRow arg="update-channel" typ="enum (stable | testing)">firmware update channel</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="installed" typ="string"></ArgTableRow>
<ArgTableRow arg="latest" typ="string"></ArgTableRow>
<ArgTableRow arg="note" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

### interface/lte/monitor

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="pin-status" typ="string"></ArgTableRow>
<ArgTableRow arg="registration-status" typ="string"></ArgTableRow>
<ArgTableRow arg="functionality" typ="enum (minimum | full | tx rf circuit disabled | rx rf circuit disabled | tx and rx rf circuit disabled | tx and rx rf circuit disabled)"></ArgTableRow>
<ArgTableRow arg="manufacturer" typ="string"></ArgTableRow>
<ArgTableRow arg="model" typ="string"></ArgTableRow>
<ArgTableRow arg="revision" typ="string"></ArgTableRow>
<ArgTableRow arg="current-operator" typ="string"></ArgTableRow>
<ArgTableRow arg="roaming" typ="bool"></ArgTableRow>
<ArgTableRow arg="psc" typ="num"></ArgTableRow>
<ArgTableRow arg="lac" typ="num"></ArgTableRow>
<ArgTableRow arg="current-cellid" typ="num"></ArgTableRow>
<ArgTableRow arg="enb-id" typ="num"></ArgTableRow>
<ArgTableRow arg="sector-id" typ="num"></ArgTableRow>
<ArgTableRow arg="phy-cellid" typ="num"></ArgTableRow>
<ArgTableRow arg="access-technology" typ="string"></ArgTableRow>
<ArgTableRow arg="data-class" typ="string"></ArgTableRow>
<ArgTableRow arg="session-uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="imei" typ="string"></ArgTableRow>
<ArgTableRow arg="imsi" typ="string"></ArgTableRow>
<ArgTableRow arg="iccid" typ="string"></ArgTableRow>
<ArgTableRow arg="subscriber-number" typ="string"></ArgTableRow>
<ArgTableRow arg="primary-band" typ="string"></ArgTableRow>
<ArgTableRow arg="ca-band" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="ul-ca-band" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="frame-error-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="dl-modulation" typ="string"></ArgTableRow>
<ArgTableRow arg="dl-mimo" typ="num"></ArgTableRow>
<ArgTableRow arg="cqi" typ="num"></ArgTableRow>
<ArgTableRow arg="ri" typ="num"></ArgTableRow>
<ArgTableRow arg="mcs" typ="num"></ArgTableRow>
<ArgTableRow arg="ecio" typ="num"></ArgTableRow>
<ArgTableRow arg="rscp" typ="num"></ArgTableRow>
<ArgTableRow arg="rssi" typ="num"></ArgTableRow>
<ArgTableRow arg="rsrp" typ="num"></ArgTableRow>
<ArgTableRow arg="rsrq" typ="num"></ArgTableRow>
<ArgTableRow arg="sinr" typ="num"></ArgTableRow>
<ArgTableRow arg="nr-dl-modulation" typ="string"></ArgTableRow>
<ArgTableRow arg="nr-rsrp" typ="num"></ArgTableRow>
<ArgTableRow arg="nr-rsrq" typ="num"></ArgTableRow>
<ArgTableRow arg="nr-sinr" typ="num"></ArgTableRow>
</ArgTable>

### interface/lte/scan

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="C" typ="current">current</ArgTableRow>
<ArgTableRow arg="A" typ="available">available</ArgTableRow>
<ArgTableRow arg="F" typ="forbidden">forbidden</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="operator" typ="string"></ArgTableRow>
<ArgTableRow arg="mcc-mnc" typ="string"></ArgTableRow>
<ArgTableRow arg="access-technology" typ="string"></ArgTableRow>
<ArgTableRow arg="rssi" typ="num"></ArgTableRow>
<ArgTableRow arg="rsrp" typ="num"></ArgTableRow>
<ArgTableRow arg="rsrq" typ="num"></ArgTableRow>
</ArgTable>

### interface/lte/settings

**Conditions:** !smips, !i386, !mips, !powerpc
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="mode" typ="enum (auto | serial | mbim | user | qmi)"></ArgTableRow>
<ArgTableRow arg="esim-channel" typ="enum (auto | at | qmi | mbim)"></ArgTableRow>
<ArgTableRow arg="firmware-path" typ="string"></ArgTableRow>
<ArgTableRow arg="log-dir" typ="string" syscap="modemlog"></ArgTableRow>
<ArgTableRow arg="info-polling-interval" typ="num" syscap="tr069-client">info polling interval in seconds</ArgTableRow>
<ArgTableRow arg="link-recovery-timer" typ="num">in seconds</ArgTableRow>
<ArgTableRow arg="sim-slot" typ="enum" syscap="sim-slot"></ArgTableRow>
<ArgTableRow arg="sim-link" typ="enum" syscap="sim-link"></ArgTableRow>
<ArgTableRow arg="external-antenna" typ="enum (auto | main | div | both | none)" syscap="modem-antenna-switch"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="external-antenna-selected" typ="enum (main | div | both | none | none)" syscap="modem-antenna-switch"></ArgTableRow>
</ArgTable>

### interface/lte/show-capabilities

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="modem-bus-location" typ="string"></ArgTableRow>
<ArgTableRow arg="cell-scan" typ="bool"></ArgTableRow>
<ArgTableRow arg="network-scan" typ="bool"></ArgTableRow>
<ArgTableRow arg="roaming-barring" typ="bool"></ArgTableRow>
<ArgTableRow arg="apn-address-family" typ="string"></ArgTableRow>
<ArgTableRow arg="max-apn-count" typ="num"></ArgTableRow>
<ArgTableRow arg="rat-modes" typ="string"></ArgTableRow>
<ArgTableRow arg="band-selection" typ="bool"></ArgTableRow>
<ArgTableRow arg="lte-bands" typ="string"></ArgTableRow>
<ArgTableRow arg="nr-bands" typ="string"></ArgTableRow>
<ArgTableRow arg="passthrough" typ="bool"></ArgTableRow>
<ArgTableRow arg="esim-detected" typ="bool"></ArgTableRow>
<ArgTableRow arg="firmware-update" typ="bool"></ArgTableRow>
<ArgTableRow arg="lte-attach-config" typ="bool"></ArgTableRow>
<ArgTableRow arg="at-chat" typ="bool"></ArgTableRow>
<ArgTableRow arg="framed-route-apn" typ="string"></ArgTableRow>
</ArgTable>
