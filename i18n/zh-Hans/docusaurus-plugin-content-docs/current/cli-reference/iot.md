# IoT

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## iot/bluetooth

**软件包：** iot
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="离线"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="random-static-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="antenna" typ="enum (internal | external)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="public-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="rx-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-evt" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-cmd" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-acl" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-acl" typ="num"></ArgTableRow>
</ArgTable>

### iot/bluetooth/advertisers

**软件包：** iot
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="已禁用"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="min-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="max-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="own-address-type" typ="enum (public | random-static | rpa-fallback-to-public | rpa-fallback-to-random)">AdvA 字段中使用的地址类型</ArgTableRow>
<ArgTableRow arg="channel-map" typ="ubit (37, 38, 39)"></ArgTableRow>
<ArgTableRow arg="phy" typ="enum (1M | 2M | CODED)"></ArgTableRow>
<ArgTableRow arg="legacy" typ="bool"></ArgTableRow>
<ArgTableRow arg="ad-structures" typ="multi { array-id, enum
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="device" typ="enum"></ArgTableRow>
<ArgTableRow arg="ad-size" typ="num"></ArgTableRow>
</ArgTable>

#### iot/bluetooth/advertisers/ad-structures

**软件包：** iot
**类型：** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (short-local-name | complete-local-name | service-data | manufacturer-data)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="data" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>

### iot/bluetooth/connections

**软件包：** iot
**类型：** 目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="direction" typ="enum (incoming | outgoing)"></ArgTableRow>
</ArgTable>

#### iot/bluetooth/connections/async-data

**软件包：** iot
**类型：** 目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="pdev" typ="string"></ArgTableRow>
<ArgTableRow arg="uuid" typ="string"></ArgTableRow>
<ArgTableRow arg="data-text" typ="string"></ArgTableRow>
<ArgTableRow arg="data-hex" typ="string"></ArgTableRow>
<ArgTableRow arg="data-bytes" typ="multi { array-id, num
 }"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (notification | indication)"></ArgTableRow>
<ArgTableRow arg="time" typ="date"></ArgTableRow>
</ArgTable>

##### iot/bluetooth/connections/async-data/clear

**软件包：** iot
**类型：** 命令

#### iot/bluetooth/connections/characteristics

**软件包：** iot
**类型：** 目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="uuid" typ="string"></ArgTableRow>
<ArgTableRow arg="handle" typ="num"></ArgTableRow>
<ArgTableRow arg="service-name" typ="string"></ArgTableRow>
<ArgTableRow arg="service-uuid" typ="string"></ArgTableRow>
<ArgTableRow arg="props" typ="multi { array-id, enum (bcast | read | write-no-resp | write | notify | indicate | write-signed | ext) { bcast:0x01, read:0x02, write-no-resp:0x04, write:0x08, notify:0x10, indicate:0x20, write-signed:0x40, ext:0x80 }
 }"></ArgTableRow>
<ArgTableRow arg="pdev" typ="enum"></ArgTableRow>
</ArgTable>

#### iot/bluetooth/connections/connect

**软件包：** iot
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="pdev" typ="enum"></ArgTableRow>
</ArgTable>

#### iot/bluetooth/connections/disconnect

**软件包：** iot
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="pdev" typ="enum ()"></ArgTableRow>
</ArgTable>

#### iot/bluetooth/connections/read

**软件包：** iot
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="uuid" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="pdev" typ="enum ()"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="value" typ="string"></ArgTableRow>
<ArgTableRow arg="hex" typ="string"></ArgTableRow>
<ArgTableRow arg="bytes" typ="multi { array-id, num
 }"></ArgTableRow>
</ArgTable>

#### iot/bluetooth/connections/subscribe

**软件包：** iot
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="uuid" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (notification | indication)"></ArgTableRow>
<ArgTableRow arg="pdev" typ="enum ()"></ArgTableRow>
</ArgTable>

#### iot/bluetooth/connections/unsubscribe

**软件包：** iot
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="uuid" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (notification | indication)"></ArgTableRow>
<ArgTableRow arg="pdev" typ="enum ()"></ArgTableRow>
</ArgTable>

#### iot/bluetooth/connections/write

**软件包：** iot
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="uuid" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="data-hex" typ="string"></ArgTableRow>
<ArgTableRow arg="data-str" typ="string"></ArgTableRow>
<ArgTableRow arg="data-bytes" typ="multi { array-id, num
 }"></ArgTableRow>
<ArgTableRow arg="pdev" typ="enum ()"></ArgTableRow>
</ArgTable>

#### iot/bluetooth/connections/write-no-resp

**软件包：** iot
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="uuid" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="data-hex" typ="string"></ArgTableRow>
<ArgTableRow arg="data-str" typ="string"></ArgTableRow>
<ArgTableRow arg="data-bytes" typ="multi { array-id, num
 }"></ArgTableRow>
<ArgTableRow arg="pdev" typ="enum ()"></ArgTableRow>
</ArgTable>

### iot/bluetooth/decode-ad

**软件包：** iot
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="data" typ="string"></ArgTableRow>
<ArgTableRow arg="key" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="type" typ="enum (unknown | mikrotik | ibeacon | eddystone-uid | eddystone-url | eddystone-tlm | eddystone-eid)"></ArgTableRow>
<ArgTableRow arg="version" typ="num"></ArgTableRow>
<ArgTableRow arg="encrypted" typ="bool"></ArgTableRow>
<ArgTableRow arg="acc-x" typ="num"></ArgTableRow>
<ArgTableRow arg="acc-y" typ="num"></ArgTableRow>
<ArgTableRow arg="acc-z" typ="num"></ArgTableRow>
<ArgTableRow arg="temperature" typ="num"></ArgTableRow>
<ArgTableRow arg="uptime" typ="num"></ArgTableRow>
<ArgTableRow arg="flags" typ="multi { array-id, enum (reed-switch | tilt | free-fall | impact-x | impact-y | impact-z) { reed-switch:0, tilt:1, free-fall:2, impact-x:3, impact-y:4, impact-z:5 }
 }"></ArgTableRow>
<ArgTableRow arg="battery" typ="num"></ArgTableRow>
<ArgTableRow arg="uuid" typ="string"></ArgTableRow>
<ArgTableRow arg="major" typ="num"></ArgTableRow>
<ArgTableRow arg="minor" typ="num"></ArgTableRow>
<ArgTableRow arg="rssi-at-1m" typ="num"></ArgTableRow>
<ArgTableRow arg="namespace" typ="string"></ArgTableRow>
<ArgTableRow arg="instance" typ="string"></ArgTableRow>
<ArgTableRow arg="battery-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="packet-count" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-power" typ="num"></ArgTableRow>
<ArgTableRow arg="eid" typ="string"></ArgTableRow>
</ArgTable>

### iot/bluetooth/peripheral-devices

**软件包：** iot
**类型：** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="address-type" typ="enum (public | random)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address" typ="macAddr" mandatory="1"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="persist" typ="bool"></ArgTableRow>
<ArgTableRow arg="mtik-key" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="rssi" typ="num"></ArgTableRow>
<ArgTableRow arg="last-data" typ="string">十六进制格式的广播数据</ArgTableRow>
<ArgTableRow arg="last-seen" typ="date"></ArgTableRow>
<ArgTableRow arg="beacon-types" typ="multi { array-id, enum (unknown | mikrotik | ibeacon | eddystone-uid | eddystone-url | eddystone-tlm | eddystone-eid) { unknown:0, mikrotik:1, ibeacon:2, eddystone-uid:3, eddystone-url:4, eddystone-tlm:5, eddystone-eid:6 }
 }"></ArgTableRow>
<ArgTableRow arg="mtik-version" typ="num"></ArgTableRow>
<ArgTableRow arg="mtik-encrypted" typ="bool"></ArgTableRow>
<ArgTableRow arg="mtik-acc-x" typ="num"></ArgTableRow>
<ArgTableRow arg="mtik-acc-y" typ="num"></ArgTableRow>
<ArgTableRow arg="mtik-acc-z" typ="num"></ArgTableRow>
<ArgTableRow arg="mtik-temperature" typ="num"></ArgTableRow>
<ArgTableRow arg="mtik-battery" typ="num"></ArgTableRow>
<ArgTableRow arg="mtik-uptime" typ="num"></ArgTableRow>
<ArgTableRow arg="mtik-flags" typ="multi { array-id, enum (reed-switch | tilt | free-fall | impact-x | impact-y | impact-z) { reed-switch:0, tilt:1, free-fall:2, impact-x:3, impact-y:4, impact-z:5 }
 }"></ArgTableRow>
<ArgTableRow arg="ibeacon-uuid" typ="string"></ArgTableRow>
<ArgTableRow arg="ibeacon-major" typ="num"></ArgTableRow>
<ArgTableRow arg="ibeacon-minor" typ="num"></ArgTableRow>
<ArgTableRow arg="ibeacon-rssi-at-1m" typ="num"></ArgTableRow>
<ArgTableRow arg="eddy-rssi-at-1m" typ="num"></ArgTableRow>
<ArgTableRow arg="eddy-namespace" typ="string"></ArgTableRow>
<ArgTableRow arg="eddy-instance" typ="string"></ArgTableRow>
<ArgTableRow arg="eddy-version" typ="num"></ArgTableRow>
<ArgTableRow arg="eddy-battery-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="eddy-temperature" typ="num"></ArgTableRow>
<ArgTableRow arg="eddy-packet-count" typ="num"></ArgTableRow>
<ArgTableRow arg="eddy-uptime" typ="num"></ArgTableRow>
<ArgTableRow arg="eddy-tx-power" typ="num"></ArgTableRow>
<ArgTableRow arg="eddy-eid" typ="string"></ArgTableRow>
</ArgTable>

### iot/bluetooth/reset-counters

**软件包：** iot
**类型：** 命令

### iot/bluetooth/scanners

**软件包：** iot
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="已禁用"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="type" typ="enum (passive | active)"></ArgTableRow>
<ArgTableRow arg="interval" typ="num"></ArgTableRow>
<ArgTableRow arg="window" typ="num"></ArgTableRow>
<ArgTableRow arg="own-address-type" typ="enum (public | random-static | rpa-fallback-to-public | rpa-fallback-to-random)">扫描请求中使用的地址类型</ArgTableRow>
<ArgTableRow arg="filter-policy" typ="enum (default | whitelist)"></ArgTableRow>
<ArgTableRow arg="filter-duplicates" typ="enum (off | keep-oldest | keep-newest | keep-unique)">丢弃来自同一广播者的重复广播</ArgTableRow>
<ArgTableRow arg="phy" typ="enum (1M | 2M | CODED)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="device" typ="enum"></ArgTableRow>
</ArgTable>

#### iot/bluetooth/scanners/advertisements

**软件包：** iot
**类型：** 目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="device" typ="enum"></ArgTableRow>
<ArgTableRow arg="pdu-type" typ="enum (adv-ind | adv-direct-ind | adv-scan-ind | adv-noconn-ind | scan-rsp | unknown)"></ArgTableRow>
<ArgTableRow arg="time" typ="date"></ArgTableRow>
<ArgTableRow arg="epoch" typ="num">自 Unix 纪元以来的毫秒数</ArgTableRow>
<ArgTableRow arg="address-type" typ="enum (public | random)"></ArgTableRow>
<ArgTableRow arg="address" typ="macAddr">广播者蓝牙地址</ArgTableRow>
<ArgTableRow arg="rssi" typ="num">信号强度</ArgTableRow>
<ArgTableRow arg="length" typ="num">广播数据长度</ArgTableRow>
<ArgTableRow arg="data" typ="string">十六进制格式的广播数据</ArgTableRow>
<ArgTableRow arg="phy" typ="enum (1M | 2M | CODED-S8 | CODED-S2 | NONE)">广播主 PHY</ArgTableRow>
<ArgTableRow arg="phy-secondary" typ="enum (1M | 2M | CODED-S8 | CODED-S2 | NONE)">广播次 PHY</ArgTableRow>
<ArgTableRow arg="legacy" typ="bool">广播传统兼容性</ArgTableRow>
<ArgTableRow arg="filter-comment" typ="string">匹配的白名单过滤器注释</ArgTableRow>
</ArgTable>

##### iot/bluetooth/scanners/advertisements/clear

**软件包：** iot
**类型：** 命令

### iot/bluetooth/whitelist

**软件包：** iot
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="已禁用"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address-type" typ="enum (public | random | any)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>

## iot/gpio

**系统能力：** gpio
**软件包：** iot
**类型：** 目录

### iot/gpio/analog

**软件包：** iot
**类型：** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="offset" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="value" typ="num"></ArgTableRow>
</ArgTable>

### iot/gpio/digital

**软件包：** iot
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="已禁用"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="direction" typ="enum (input | output)"></ArgTableRow>
<ArgTableRow arg="output" typ="enum (0 | 1)"></ArgTableRow>
<ArgTableRow arg="script" typ="alt { , string
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="input" typ="enum (0 | 1)"></ArgTableRow>
</ArgTable>

## iot/lora

**软件包：** iot
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="已禁用"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="gateway-id" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="servers" typ="multi { enum
 }"></ArgTableRow>
<ArgTableRow arg="tx-immediate-delay-us" typ="num"></ArgTableRow>
<ArgTableRow arg="channel-plan" typ="enum (custom | eu-868 | as-923 | kr-920 | in-865 | il-917 | us-915-1 | us-915-2 | us-915-3 | us-915-4 | us-915-5 | us-915-6 | us-915-7 | us-915-8 | au-915-1 | au-915-2 | ru-864 | ru-864-mid | 2.4-ghz)"></ArgTableRow>
<ArgTableRow arg="antenna-gain" typ="num"></ArgTableRow>
<ArgTableRow arg="forward" typ="ubit (crc-validation, dev-addr-validation, proprietary-traffic)"></ArgTableRow>
<ArgTableRow arg="network" typ="enum (public | private)"></ArgTableRow>
<ArgTableRow arg="lbt-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="listen-time" typ="num"></ArgTableRow>
<ArgTableRow arg="rssi-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="spoof-gps" typ="bool"></ArgTableRow>
<ArgTableRow arg="lat" typ="num"></ArgTableRow>
<ArgTableRow arg="long" typ="num"></ArgTableRow>
<ArgTableRow arg="alt" typ="num"></ArgTableRow>
<ArgTableRow arg="antenna" typ="enum (internal-antenna | external-antenna)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="firmware-id" typ="string"></ArgTableRow>
<ArgTableRow arg="version" typ="string"></ArgTableRow>
<ArgTableRow arg="rx-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-toa" typ="num"></ArgTableRow>
<ArgTableRow arg="band" typ="enum (unknown | 863-870 | 902-928 | 2.4-ghz)"></ArgTableRow>
</ArgTable>

### iot/lora/channels

**软件包：** iot
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="已禁用"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="radio" typ="enum (radio0 | radio1 | radio2 | radio3)"></ArgTableRow>
<ArgTableRow arg="freq-off" typ="num"></ArgTableRow>
<ArgTableRow arg="bandwidth" typ="enum (7.8_kHz | 15.6_kHz | 31.2_kHz | 62.5_kHz | 125_kHz | 250_kHz | 500_kHz | 200_kHz | 400_kHz | 800_kHz | 1600_kHz)"></ArgTableRow>
<ArgTableRow arg="spread-factor" typ="enum (SF7 | SF8 | SF9 | SF10 | SF11 | SF12 | SF5 | SF6)"></ArgTableRow>
<ArgTableRow arg="datarate" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (MSF | LoRa | FSK)"></ArgTableRow>
<ArgTableRow arg="freq" typ="num"></ArgTableRow>
</ArgTable>

### iot/lora/joineui

**软件包：** iot
**类型：** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="logging" typ="bool"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (whitelist | blacklist)"></ArgTableRow>
<ArgTableRow arg="joineuis" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
</ArgTable>

### iot/lora/netid

**软件包：** iot
**类型：** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="logging" typ="bool"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (whitelist | blacklist)"></ArgTableRow>
<ArgTableRow arg="netids" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
</ArgTable>

### iot/lora/radios

**软件包：** iot
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="已禁用"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="center-freq" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-freq-min" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-freq-max" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (SX1255 | SX1257 | SX1272 | SX1276 | SX1280 | SX1250)"></ArgTableRow>
<ArgTableRow arg="rssi-off" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-enabled" typ="bool"></ArgTableRow>
</ArgTable>

### iot/lora/reset-devices

**软件包：** iot
**类型：** 命令

### iot/lora/send

**软件包：** iot
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="device-id" typ="num">设备 ID</ArgTableRow>
<ArgTableRow arg="payload" typ="string">TX 数据包负载</ArgTableRow>
<ArgTableRow arg="power" typ="num">RF 功率，单位 dBm</ArgTableRow>
<ArgTableRow arg="frequency" typ="num">无线电 TX 频率，单位 MHz（例如 868500000）</ArgTableRow>
<ArgTableRow arg="bandwidth" typ="enum (125KHZ | 250KHZ | 500KHZ)">LoRa 带宽，单位 kHz [125, 250, 500]</ArgTableRow>
<ArgTableRow arg="spread-factor" typ="enum (SF7 | SF8 | SF9 | SF10 | SF11 | SF12 | MULTI)">扩频因子</ArgTableRow>
<ArgTableRow arg="modulation" typ="enum (MOD_CW | MOD_LORA | MOD_FSK)">调制类型</ArgTableRow>
<ArgTableRow arg="preamble" typ="num">前导码长度</ArgTableRow>
<ArgTableRow arg="inverted" typ="bool">反转极性</ArgTableRow>
</ArgTable>

### iot/lora/servers

**软件包：** iot
**类型：** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="up-port" typ="num"></ArgTableRow>
<ArgTableRow arg="down-port" typ="num"></ArgTableRow>
<ArgTableRow arg="key" typ="string"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="interval" typ="num"></ArgTableRow>
<ArgTableRow arg="ssl" typ="bool"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (UDP | LNS | CUPS)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="netid" typ="multi { enum
 }"></ArgTableRow>
<ArgTableRow arg="joineui" typ="multi { enum
 }"></ArgTableRow>
</ArgTable>

#### iot/lora/servers/reset-servers

**软件包：** iot
**类型：** 命令

### iot/lora/traffic

**软件包：** iot
**类型：** 目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="time" typ="date"></ArgTableRow>
<ArgTableRow arg="gwid" typ="string"></ArgTableRow>
<ArgTableRow arg="msgtype" typ="string"></ArgTableRow>
<ArgTableRow arg="devaddr" typ="string"></ArgTableRow>
<ArgTableRow arg="mver" typ="string"></ArgTableRow>
<ArgTableRow arg="fcnt" typ="num"></ArgTableRow>
<ArgTableRow arg="type" typ="string"></ArgTableRow>
<ArgTableRow arg="netid" typ="string"></ArgTableRow>
<ArgTableRow arg="joineui" typ="string"></ArgTableRow>
<ArgTableRow arg="deveui" typ="string"></ArgTableRow>
<ArgTableRow arg="devnonce" typ="string"></ArgTableRow>
<ArgTableRow arg="joinnonce" typ="string"></ArgTableRow>
<ArgTableRow arg="freqhz" typ="num"></ArgTableRow>
<ArgTableRow arg="mod" typ="string"></ArgTableRow>
<ArgTableRow arg="band" typ="string"></ArgTableRow>
<ArgTableRow arg="datarate" typ="string"></ArgTableRow>
<ArgTableRow arg="coderate" typ="string"></ArgTableRow>
<ArgTableRow arg="ifchain" typ="string"></ArgTableRow>
<ArgTableRow arg="crc" typ="string"></ArgTableRow>
<ArgTableRow arg="txmode" typ="string"></ArgTableRow>
<ArgTableRow arg="counter" typ="string"></ArgTableRow>
<ArgTableRow arg="rfchain" typ="string"></ArgTableRow>
<ArgTableRow arg="rssi" typ="string"></ArgTableRow>
<ArgTableRow arg="snr" typ="string"></ArgTableRow>
<ArgTableRow arg="snrmin" typ="string"></ArgTableRow>
<ArgTableRow arg="snrmax" typ="string"></ArgTableRow>
<ArgTableRow arg="rxcrc" typ="string"></ArgTableRow>
<ArgTableRow arg="rfpow" typ="string"></ArgTableRow>
<ArgTableRow arg="invertpol" typ="string"></ArgTableRow>
<ArgTableRow arg="freq" typ="string"></ArgTableRow>
<ArgTableRow arg="preamblen" typ="string"></ArgTableRow>
<ArgTableRow arg="nocrc" typ="string"></ArgTableRow>
<ArgTableRow arg="noheader" typ="string"></ArgTableRow>
<ArgTableRow arg="size" typ="string"></ArgTableRow>
<ArgTableRow arg="data" typ="string"></ArgTableRow>
</ArgTable>

#### iot/lora/traffic/clear

**软件包：** iot
**类型：** 命令

#### iot/lora/traffic/options

**软件包：** iot
**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="crc-errors" typ="bool">记录带有 CRC 错误的数据包</ArgTableRow>
<ArgTableRow arg="pckt-limit" typ="num">限制日志中的数据包数量</ArgTableRow>
</ArgTable>

## iot/modbus

**软件包：** iot
**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="disabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="hardware-port" typ="enum"></ArgTableRow>
<ArgTableRow arg="tcp-port" typ="num"></ArgTableRow>
<ArgTableRow arg="timeout" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-switch-offset" typ="num"></ArgTableRow>
<ArgTableRow arg="interframe-gap" typ="num"></ArgTableRow>
<ArgTableRow arg="disable-security-rules" typ="bool"></ArgTableRow>
</ArgTable>

### iot/modbus/read-holding-registers

**软件包：** iot
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="ip" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="timeout" typ="num"></ArgTableRow>
<ArgTableRow arg="slave-id" typ="num"></ArgTableRow>
<ArgTableRow arg="reg-addr" typ="num"></ArgTableRow>
<ArgTableRow arg="num-regs" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="values" typ="multi { array-id, num
 }"></ArgTableRow>
</ArgTable>

### iot/modbus/security-rules

**软件包：** iot
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="已禁用"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数