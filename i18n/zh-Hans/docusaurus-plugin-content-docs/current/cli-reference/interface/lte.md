# LTE

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/lte

**条件：** !smips
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="R" typ="running">运行中</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="pin" typ="string"></ArgTableRow>
<ArgTableRow arg="apn-profiles" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="modem-init" typ="string">调制解调器初始化时发送的字符串</ArgTableRow>
<ArgTableRow arg="operator" typ="string">运营商锁定，使用数值：mccmnc</ArgTableRow>
<ArgTableRow arg="allow-roaming" typ="bool"></ArgTableRow>
<ArgTableRow arg="sms-read" typ="bool">如果在 /tool/sms 中启用了任何接口，则忽略此设置</ArgTableRow>
<ArgTableRow arg="sms-protocol" typ="enum (mbim | at | auto)"></ArgTableRow>
<ArgTableRow arg="network-mode" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="band" typ="multi { array-id, enum
 }">LTE 频段</ArgTableRow>
<ArgTableRow arg="nr-band" typ="multi { array-id, enum
 }">NR 频段</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="default-name" typ="string"></ArgTableRow>
<ArgTableRow arg="master" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="advertised-mtu" typ="num"></ArgTableRow>
</ArgTable>

### interface/lte/apn

**条件：** !smips
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="apn" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-network-apn" typ="bool">在 LTE 模式下使用网络提供的 APN</ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool"></ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="ip-type" typ="enum (ipv4 | ipv6 | auto)">请求的 PDN 类型</ArgTableRow>
<ArgTableRow arg="authentication" typ="enum (none | pap | chap)"></ArgTableRow>
<ArgTableRow arg="user" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="password" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="passthrough-interface" typ="iface_enum { none:0 }"></ArgTableRow>
<ArgTableRow arg="passthrough-mac" typ="alt { , bool
, macAddr
 }">自动将从第一个数据包中学习 MAC 地址</ArgTableRow>
<ArgTableRow arg="passthrough-subnet-size" typ="alt { enum (auto | 32) { auto:0, 32:32 }
, num [16 .. 32]
 }"></ArgTableRow>
<ArgTableRow arg="ipv6-interface" typ="iface_enum { none:0 }">用于通告 IPv6 前缀的接口</ArgTableRow>
</ArgTable>

### interface/lte/at-chat

**条件：** !smips
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="input" typ="string">向调制解调器发送命令，并在返回前等待任何输出</ArgTableRow>
<ArgTableRow arg="wait" typ="alt { enum (no | yes) { no:0, yes:3 }
, time [ .. 255]
 }">始终等待 3 秒</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="output" typ="string"></ArgTableRow>
</ArgTable>

### interface/lte/cell-monitor

**条件：** !smips
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="max-age" typ="time"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
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

**条件：** !smips
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="A" typ="active">激活</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="nickname" typ="string"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="spn" typ="string"></ArgTableRow>
<ArgTableRow arg="iccid" typ="string"></ArgTableRow>
</ArgTable>

#### interface/lte/esim/activate

**条件：** !smips
**类型：** 命令

#### interface/lte/esim/deactivate

**条件：** !smips
**类型：** 命令

#### interface/lte/esim/delete

**条件：** !smips
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="force-delete" typ="bool">在删除配置文件之前将其禁用，默认值：no</ArgTableRow>
</ArgTable>

#### interface/lte/esim/esim-id

**条件：** !smips
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="eid" typ="string"></ArgTableRow>
</ArgTable>

#### interface/lte/esim/provision

**条件：** !smips
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="activation-code" typ="string">配置文件激活码。示例：LPA:1$server.example.io$ABCD10EFGHI5KL6M</ArgTableRow>
<ArgTableRow arg="activate" typ="bool">配置完成后激活新创建的配置文件（默认值：yes）</ArgTableRow>
<ArgTableRow arg="sm-dp-plus" typ="string">SM-DP+ 服务器主机名。示例：sm-dp-plus=server.example.io</ArgTableRow>
<ArgTableRow arg="matching-id" typ="string">激活码令牌。示例：matching-id=ABCD10EFGHI5KL6M</ArgTableRow>
<ArgTableRow arg="confirmation-code" typ="string">运营商提供的可选代码</ArgTableRow>
<ArgTableRow arg="sm-dp-plus-oid" typ="string">运营商提供的可选 SM-DP+</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="iccid" typ="string"></ArgTableRow>
<ArgTableRow arg="spn" typ="string"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

#### interface/lte/esim/refresh-profile-list

**条件：** !smips
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
</ArgTable>

#### interface/lte/esim/send-notifications

**条件：** !smips
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
</ArgTable>

#### interface/lte/esim/set-nickname

**条件：** !smips
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="nickname" typ="string"></ArgTableRow>
</ArgTable>

### interface/lte/firmware-upgrade

**条件：** !smips
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="upgrade" typ="bool">执行升级或仅检查</ArgTableRow>
<ArgTableRow arg="firmware-file" typ="file">升级镜像的路径或 URL</ArgTableRow>
<ArgTableRow arg="update-channel" typ="enum (stable | testing)">固件更新通道</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="installed" typ="string"></ArgTableRow>
<ArgTableRow arg="latest" typ="string"></ArgTableRow>
<ArgTableRow arg="note" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

### interface/lte/monitor

**条件：** !smips
**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
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

**条件：** !smips
**类型：** 命令

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="C" typ="current">当前</ArgTableRow>
<ArgTableRow arg="A" typ="available">可用</ArgTableRow>
<ArgTableRow arg="F" typ="forbidden">禁止</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="operator" typ="string"></ArgTableRow>
<ArgTableRow arg="mcc-mnc" typ="string"></ArgTableRow>
<ArgTableRow arg="access-technology" typ="string"></ArgTableRow>
<ArgTableRow arg="rssi" typ="num"></ArgTableRow>
<ArgTableRow arg="rsrp" typ="num"></ArgTableRow>
<ArgTableRow arg="rsrq" typ="num"></ArgTableRow>
</ArgTable>

### interface/lte/settings

**条件：** !smips, !i386, !mips, !powerpc
**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="mode" typ="enum (auto | serial | mbim | user | qmi)"></ArgTableRow>
<ArgTableRow arg="esim-channel" typ="enum (auto | at | qmi | mbim)"></ArgTableRow>
<ArgTableRow arg="firmware-path" typ="string"></ArgTableRow>
<ArgTableRow arg="log-dir" typ="string" syscap="modemlog"></ArgTableRow>
<ArgTableRow arg="info-polling-interval" typ="num" syscap="tr069-client">信息轮询间隔（秒）</ArgTableRow>
<ArgTableRow arg="link-recovery-timer" typ="num">以秒为单位</ArgTableRow>
<ArgTableRow arg="sim-slot" typ="enum" syscap="sim-slot"></ArgTableRow>
<ArgTableRow arg="sim-link" typ="enum" syscap="sim-link"></ArgTableRow>
<ArgTableRow arg="external-antenna" typ="enum (auto | main | div | both | none)" syscap="modem-antenna-switch"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="external-antenna-selected" typ="enum (main | div | both | none | none)" syscap="modem-antenna-switch"></ArgTableRow>
</ArgTable>

### interface/lte/show-capabilities

**条件：** !smips
**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
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