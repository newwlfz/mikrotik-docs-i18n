# Iot

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## iot/bluetooth

**Package:** iot
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="offline"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="random-static-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="antenna" typ="enum (internal | external)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
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

**Package:** iot
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="min-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="max-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="own-address-type" typ="enum (public | random-static | rpa-fallback-to-public | rpa-fallback-to-random)">Address type used in AdvA field</ArgTableRow>
<ArgTableRow arg="channel-map" typ="ubit (37, 38, 39)"></ArgTableRow>
<ArgTableRow arg="phy" typ="enum (1M | 2M | CODED)"></ArgTableRow>
<ArgTableRow arg="legacy" typ="bool"></ArgTableRow>
<ArgTableRow arg="ad-structures" typ="multi { array-id, enum
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum"></ArgTableRow>
<ArgTableRow arg="ad-size" typ="num"></ArgTableRow>
</ArgTable>

#### iot/bluetooth/advertisers/ad-structures

**Package:** iot
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (short-local-name | complete-local-name | service-data | manufacturer-data)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="data" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>

### iot/bluetooth/connections

**Package:** iot
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="direction" typ="enum (incoming | outgoing)"></ArgTableRow>
</ArgTable>

#### iot/bluetooth/connections/async-data

**Package:** iot
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
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

**Package:** iot
**Type:** Command

#### iot/bluetooth/connections/characteristics

**Package:** iot
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
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

**Package:** iot
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="pdev" typ="enum"></ArgTableRow>
</ArgTable>

#### iot/bluetooth/connections/disconnect

**Package:** iot
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="pdev" typ="enum ()"></ArgTableRow>
</ArgTable>

#### iot/bluetooth/connections/read

**Package:** iot
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="uuid" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="pdev" typ="enum ()"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="value" typ="string"></ArgTableRow>
<ArgTableRow arg="hex" typ="string"></ArgTableRow>
<ArgTableRow arg="bytes" typ="multi { array-id, num
 }"></ArgTableRow>
</ArgTable>

#### iot/bluetooth/connections/subscribe

**Package:** iot
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="uuid" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (notification | indication)"></ArgTableRow>
<ArgTableRow arg="pdev" typ="enum ()"></ArgTableRow>
</ArgTable>

#### iot/bluetooth/connections/unsubscribe

**Package:** iot
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="uuid" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (notification | indication)"></ArgTableRow>
<ArgTableRow arg="pdev" typ="enum ()"></ArgTableRow>
</ArgTable>

#### iot/bluetooth/connections/write

**Package:** iot
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="uuid" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="data-hex" typ="string"></ArgTableRow>
<ArgTableRow arg="data-str" typ="string"></ArgTableRow>
<ArgTableRow arg="data-bytes" typ="multi { array-id, num
 }"></ArgTableRow>
<ArgTableRow arg="pdev" typ="enum ()"></ArgTableRow>
</ArgTable>

#### iot/bluetooth/connections/write-no-resp

**Package:** iot
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="uuid" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="data-hex" typ="string"></ArgTableRow>
<ArgTableRow arg="data-str" typ="string"></ArgTableRow>
<ArgTableRow arg="data-bytes" typ="multi { array-id, num
 }"></ArgTableRow>
<ArgTableRow arg="pdev" typ="enum ()"></ArgTableRow>
</ArgTable>

### iot/bluetooth/decode-ad

**Package:** iot
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="data" typ="string"></ArgTableRow>
<ArgTableRow arg="key" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
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

**Package:** iot
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address-type" typ="enum (public | random)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address" typ="macAddr" mandatory="1"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="persist" typ="bool"></ArgTableRow>
<ArgTableRow arg="mtik-key" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="rssi" typ="num"></ArgTableRow>
<ArgTableRow arg="last-data" typ="string">Advertisement data in hex format</ArgTableRow>
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

**Package:** iot
**Type:** Command

### iot/bluetooth/scanners

**Package:** iot
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="type" typ="enum (passive | active)"></ArgTableRow>
<ArgTableRow arg="interval" typ="num"></ArgTableRow>
<ArgTableRow arg="window" typ="num"></ArgTableRow>
<ArgTableRow arg="own-address-type" typ="enum (public | random-static | rpa-fallback-to-public | rpa-fallback-to-random)">Address type used in scan requests</ArgTableRow>
<ArgTableRow arg="filter-policy" typ="enum (default | whitelist)"></ArgTableRow>
<ArgTableRow arg="filter-duplicates" typ="enum (off | keep-oldest | keep-newest | keep-unique)">Discard duplicate advertisements from the same advertiser</ArgTableRow>
<ArgTableRow arg="phy" typ="enum (1M | 2M | CODED)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum"></ArgTableRow>
</ArgTable>

#### iot/bluetooth/scanners/advertisements

**Package:** iot
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum"></ArgTableRow>
<ArgTableRow arg="pdu-type" typ="enum (adv-ind | adv-direct-ind | adv-scan-ind | adv-noconn-ind | scan-rsp | unknown)"></ArgTableRow>
<ArgTableRow arg="time" typ="date"></ArgTableRow>
<ArgTableRow arg="epoch" typ="num">Milliseconds since Unix Epoch</ArgTableRow>
<ArgTableRow arg="address-type" typ="enum (public | random)"></ArgTableRow>
<ArgTableRow arg="address" typ="macAddr">Advertiser Bluetooth address</ArgTableRow>
<ArgTableRow arg="rssi" typ="num">Signal strength</ArgTableRow>
<ArgTableRow arg="length" typ="num">Advertisement data length</ArgTableRow>
<ArgTableRow arg="data" typ="string">Advertisement data in hex format</ArgTableRow>
<ArgTableRow arg="phy" typ="enum (1M | 2M | CODED-S8 | CODED-S2 | NONE)">Advertisement primary PHY</ArgTableRow>
<ArgTableRow arg="phy-secondary" typ="enum (1M | 2M | CODED-S8 | CODED-S2 | NONE)">Advertisement secondary PHY</ArgTableRow>
<ArgTableRow arg="legacy" typ="bool">Advertisement legacy compatibility</ArgTableRow>
<ArgTableRow arg="filter-comment" typ="string">Comment of the matching whitelist filter</ArgTableRow>
</ArgTable>

##### iot/bluetooth/scanners/advertisements/clear

**Package:** iot
**Type:** Command

### iot/bluetooth/whitelist

**Package:** iot
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address-type" typ="enum (public | random | any)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>

## iot/gpio

**Syscap:** gpio
**Package:** iot
**Type:** Directory

### iot/gpio/analog

**Package:** iot
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="offset" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="value" typ="num"></ArgTableRow>
</ArgTable>

### iot/gpio/digital

**Package:** iot
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="direction" typ="enum (input | output)"></ArgTableRow>
<ArgTableRow arg="output" typ="enum (0 | 1)"></ArgTableRow>
<ArgTableRow arg="script" typ="alt { , string
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="input" typ="enum (0 | 1)"></ArgTableRow>
</ArgTable>

## iot/lora

**Package:** iot
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
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

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="firmware-id" typ="string"></ArgTableRow>
<ArgTableRow arg="version" typ="string"></ArgTableRow>
<ArgTableRow arg="rx-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-toa" typ="num"></ArgTableRow>
<ArgTableRow arg="band" typ="enum (unknown | 863-870 | 902-928 | 2.4-ghz)"></ArgTableRow>
</ArgTable>

### iot/lora/channels

**Package:** iot
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="radio" typ="enum (radio0 | radio1 | radio2 | radio3)"></ArgTableRow>
<ArgTableRow arg="freq-off" typ="num"></ArgTableRow>
<ArgTableRow arg="bandwidth" typ="enum (7.8_kHz | 15.6_kHz | 31.2_kHz | 62.5_kHz | 125_kHz | 250_kHz | 500_kHz | 200_kHz | 400_kHz | 800_kHz | 1600_kHz)"></ArgTableRow>
<ArgTableRow arg="spread-factor" typ="enum (SF7 | SF8 | SF9 | SF10 | SF11 | SF12 | SF5 | SF6)"></ArgTableRow>
<ArgTableRow arg="datarate" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (MSF | LoRa | FSK)"></ArgTableRow>
<ArgTableRow arg="freq" typ="num"></ArgTableRow>
</ArgTable>

### iot/lora/joineui

**Package:** iot
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="logging" typ="bool"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (whitelist | blacklist)"></ArgTableRow>
<ArgTableRow arg="joineuis" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
</ArgTable>

### iot/lora/netid

**Package:** iot
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="logging" typ="bool"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (whitelist | blacklist)"></ArgTableRow>
<ArgTableRow arg="netids" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
</ArgTable>

### iot/lora/radios

**Package:** iot
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="center-freq" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-freq-min" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-freq-max" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (SX1255 | SX1257 | SX1272 | SX1276 | SX1280 | SX1250)"></ArgTableRow>
<ArgTableRow arg="rssi-off" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-enabled" typ="bool"></ArgTableRow>
</ArgTable>

### iot/lora/reset-devices

**Package:** iot
**Type:** Command

### iot/lora/send

**Package:** iot
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device-id" typ="num">device id</ArgTableRow>
<ArgTableRow arg="payload" typ="string">TX packet payload</ArgTableRow>
<ArgTableRow arg="power" typ="num">RF power in dBm</ArgTableRow>
<ArgTableRow arg="frequency" typ="num">Radio TX frequency in MHz (e.g.868500000)</ArgTableRow>
<ArgTableRow arg="bandwidth" typ="enum (125KHZ | 250KHZ | 500KHZ)">LoRa bandwidth in khz [125, 250, 500]</ArgTableRow>
<ArgTableRow arg="spread-factor" typ="enum (SF7 | SF8 | SF9 | SF10 | SF11 | SF12 | MULTI)">Spread Factor</ArgTableRow>
<ArgTableRow arg="modulation" typ="enum (MOD_CW | MOD_LORA | MOD_FSK)">modulation type</ArgTableRow>
<ArgTableRow arg="preamble" typ="num">preamble length</ArgTableRow>
<ArgTableRow arg="inverted" typ="bool">invert polarity</ArgTableRow>
</ArgTable>

### iot/lora/servers

**Package:** iot
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
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

**Package:** iot
**Type:** Command

### iot/lora/traffic

**Package:** iot
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
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

**Package:** iot
**Type:** Command

#### iot/lora/traffic/options

**Package:** iot
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="crc-errors" typ="bool">log packets with CRC errors</ArgTableRow>
<ArgTableRow arg="pckt-limit" typ="num">limit packets in log</ArgTableRow>
</ArgTable>

## iot/modbus

**Package:** iot
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="disabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="hardware-port" typ="enum"></ArgTableRow>
<ArgTableRow arg="tcp-port" typ="num"></ArgTableRow>
<ArgTableRow arg="timeout" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-switch-offset" typ="num"></ArgTableRow>
<ArgTableRow arg="interframe-gap" typ="num"></ArgTableRow>
<ArgTableRow arg="disable-security-rules" typ="bool"></ArgTableRow>
</ArgTable>

### iot/modbus/read-holding-registers

**Package:** iot
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ip" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="timeout" typ="num"></ArgTableRow>
<ArgTableRow arg="slave-id" typ="num"></ArgTableRow>
<ArgTableRow arg="reg-addr" typ="num"></ArgTableRow>
<ArgTableRow arg="num-regs" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="values" typ="multi { array-id, num
 }"></ArgTableRow>
</ArgTable>

### iot/modbus/security-rules

**Package:** iot
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ip-range" typ="ipRange" mandatory="1"></ArgTableRow>
<ArgTableRow arg="allowed-function-codes" typ="multi { array-id, num
 }" mandatory="1"></ArgTableRow>
</ArgTable>

### iot/modbus/transceive

**Package:** iot
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="num"></ArgTableRow>
<ArgTableRow arg="function" typ="num"></ArgTableRow>
<ArgTableRow arg="data" typ="string"></ArgTableRow>
<ArgTableRow arg="values" typ="multi { array-id, num
 }"></ArgTableRow>
<ArgTableRow arg="rx-switch-offset" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="num"></ArgTableRow>
<ArgTableRow arg="function" typ="num"></ArgTableRow>
<ArgTableRow arg="data" typ="string"></ArgTableRow>
<ArgTableRow arg="values" typ="multi { array-id, num
 }"></ArgTableRow>
<ArgTableRow arg="time" typ="date"></ArgTableRow>
<ArgTableRow arg="status" typ="enum (ok | error)"></ArgTableRow>
<ArgTableRow arg="error" typ="num"></ArgTableRow>
<ArgTableRow arg="error-description" typ="string"></ArgTableRow>
</ArgTable>

## iot/mqtt

**Package:** iot
**Type:** Settings Directory

### iot/mqtt/brokers

**Package:** iot
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="W" typ="Will message enabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="ssl" typ="bool"></ArgTableRow>
<ArgTableRow arg="client-id" typ="string"></ArgTableRow>
<ArgTableRow arg="username" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="will-topic" typ="string"></ArgTableRow>
<ArgTableRow arg="will-message" typ="string"></ArgTableRow>
<ArgTableRow arg="will-qos" typ="num"></ArgTableRow>
<ArgTableRow arg="will-retain" typ="bool"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="auto-connect" typ="bool"></ArgTableRow>
<ArgTableRow arg="keep-alive" typ="num"></ArgTableRow>
<ArgTableRow arg="parallel-scripts-limit" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="connected" typ="bool"></ArgTableRow>
</ArgTable>

### iot/mqtt/connect

**Package:** iot
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="broker" typ="enum ()"></ArgTableRow>
</ArgTable>

### iot/mqtt/disconnect

**Package:** iot
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="broker" typ="enum ()"></ArgTableRow>
</ArgTable>

### iot/mqtt/publish

**Package:** iot
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="broker" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="topic" typ="string"></ArgTableRow>
<ArgTableRow arg="message" typ="string"></ArgTableRow>
<ArgTableRow arg="qos" typ="num"></ArgTableRow>
<ArgTableRow arg="retain" typ="bool"></ArgTableRow>
<ArgTableRow arg="disconnect-after" typ="bool"></ArgTableRow>
<ArgTableRow arg="force" typ="bool"></ArgTableRow>
</ArgTable>

### iot/mqtt/subscribe

**Package:** iot
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="broker" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="topic" typ="string"></ArgTableRow>
<ArgTableRow arg="qos" typ="num"></ArgTableRow>
<ArgTableRow arg="force" typ="bool"></ArgTableRow>
</ArgTable>

### iot/mqtt/subscriptions

**Package:** iot
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="broker" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="topic" typ="string"></ArgTableRow>
<ArgTableRow arg="qos" typ="num"></ArgTableRow>
<ArgTableRow arg="on-message" typ="string"></ArgTableRow>
</ArgTable>

#### iot/mqtt/subscriptions/monitor-data

**Package:** iot
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="data" typ="string"></ArgTableRow>
<ArgTableRow arg="time" typ="date"></ArgTableRow>
<ArgTableRow arg="topic" typ="string"></ArgTableRow>
<ArgTableRow arg="broker" typ="enum ()"></ArgTableRow>
</ArgTable>

#### iot/mqtt/subscriptions/recv

**Package:** iot
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="broker" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="topic" typ="string"></ArgTableRow>
<ArgTableRow arg="data" typ="string"></ArgTableRow>
<ArgTableRow arg="time" typ="date"></ArgTableRow>
</ArgTable>

##### iot/mqtt/subscriptions/recv/clear

**Package:** iot
**Type:** Command

### iot/mqtt/unsubscribe

**Package:** iot
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="broker" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="topic" typ="enum ()"></ArgTableRow>
</ArgTable>

## iot/wiliot

**Package:** iot
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="spoof-gps" typ="bool"></ArgTableRow>
<ArgTableRow arg="lat" typ="num"></ArgTableRow>
<ArgTableRow arg="long" typ="num"></ArgTableRow>
<ArgTableRow arg="server" typ="enum (none)">Used MQTT server</ArgTableRow>
<ArgTableRow arg="scanner" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="advertiser" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="wi-fi" typ="iface_enum { , none:nv::BADID }"></ArgTableRow>
<ArgTableRow arg="features" typ="ubit (gateway, bridge)">supported Wiliot features</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="gateway-id" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="string"></ArgTableRow>
<ArgTableRow arg="owner" typ="string"></ArgTableRow>
</ArgTable>

### iot/wiliot/bluetooth-traffic

**Package:** iot
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="time" typ="date"></ArgTableRow>
<ArgTableRow arg="address" typ="macAddr">Advertiser Bluetooth address</ArgTableRow>
<ArgTableRow arg="rssi" typ="num">Signal strength</ArgTableRow>
<ArgTableRow arg="payload" typ="string">Payload</ArgTableRow>
</ArgTable>

#### iot/wiliot/bluetooth-traffic/clear

**Package:** iot
**Type:** Command

### iot/wiliot/clear

**Package:** iot
**Type:** Command

### iot/wiliot/disable

**Package:** iot
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

### iot/wiliot/enable

**Package:** iot
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

### iot/wiliot/mqtt-traffic

**Package:** iot
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="time" typ="date"></ArgTableRow>
<ArgTableRow arg="topic" typ="string"></ArgTableRow>
<ArgTableRow arg="data" typ="string"></ArgTableRow>
</ArgTable>

#### iot/wiliot/mqtt-traffic/clear

**Package:** iot
**Type:** Command

### iot/wiliot/options

**Package:** iot
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="token-refresh-handicap" typ="num">handicap for refreshing token</ArgTableRow>
<ArgTableRow arg="pckt-limit" typ="num">mqtt log packet limit</ArgTableRow>
</ArgTable>

### iot/wiliot/servers

**Package:** iot
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="ssl" typ="bool"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)"></ArgTableRow>
</ArgTable>

#### iot/wiliot/servers/defaults

**Package:** iot
**Type:** Command
