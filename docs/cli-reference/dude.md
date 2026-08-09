# dude

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# dude

**Package:** dude
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="data-directory" typ="file"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

## dude/agent

**Package:** dude
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>

## dude/device

**Package:** dude
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>

## dude/device-type

**Package:** dude
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>

## dude/export-db

**Package:** dude
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="backup-file" typ="file"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

## dude/import-db

**Package:** dude
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="backup-file" typ="file"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

## dude/notification

**Package:** dude
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>

## dude/probe

**Package:** dude
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>

## dude/ros

**Package:** dude
**Type:** Directory

### dude/ros/address

**Package:** dude
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address" typ="composite { ,  }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="network" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="netmask" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="broadcast" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="interface" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="actual-interface" typ="enum"></ArgTableRow>
</ArgTable>

### dude/ros/arp

**Package:** dude
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="H" typ="DHCP"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="P" typ="published"></ArgTableRow>
<ArgTableRow arg="C" typ="complete"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="interface" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="published" typ="bool"></ArgTableRow>
</ArgTable>

### dude/ros/health

**Package:** dude
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="fan-mode" typ="enum (manual | auto)"></ArgTableRow>
<ArgTableRow arg="use-fan" typ="enum (auxiliary | main)"></ArgTableRow>
<ArgTableRow arg="use-fan2" typ="enum (auxiliary | main)"></ArgTableRow>
<ArgTableRow arg="fan-switch" typ="enum (auto | on | off)"></ArgTableRow>
<ArgTableRow arg="fan-on-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-overtemp-check" typ="bool"></ArgTableRow>
<ArgTableRow arg="cpu-overtemp-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-overtemp-startup-delay" typ="time"></ArgTableRow>
<ArgTableRow arg="psu1-state" typ="enum (ok | fail)"></ArgTableRow>
<ArgTableRow arg="psu2-state" typ="enum (ok | fail)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="active-fan" typ="enum (auxiliary | main | none)"></ArgTableRow>
<ArgTableRow arg="active-fan2" typ="enum (auxiliary | main | none)"></ArgTableRow>
<ArgTableRow arg="voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="battery" typ="num"></ArgTableRow>
<ArgTableRow arg="current" typ="num"></ArgTableRow>
<ArgTableRow arg="fan-speed" typ="num"></ArgTableRow>
<ArgTableRow arg="fan-speed2" typ="num"></ArgTableRow>
<ArgTableRow arg="temperature" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-temperature" typ="num"></ArgTableRow>
<ArgTableRow arg="power-consumption" typ="num"></ArgTableRow>
<ArgTableRow arg="board-temperature1" typ="num"></ArgTableRow>
<ArgTableRow arg="board-temperature2" typ="num"></ArgTableRow>
<ArgTableRow arg="board-temperature3" typ="num"></ArgTableRow>
<ArgTableRow arg="psu1-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="psu2-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="psu1-current" typ="num"></ArgTableRow>
<ArgTableRow arg="psu2-current" typ="num"></ArgTableRow>
<ArgTableRow arg="fan1-speed" typ="num"></ArgTableRow>
<ArgTableRow arg="fan2-speed" typ="num"></ArgTableRow>
<ArgTableRow arg="fan3-speed" typ="num"></ArgTableRow>
<ArgTableRow arg="fan4-speed" typ="num"></ArgTableRow>
<ArgTableRow arg="fan5-speed" typ="num"></ArgTableRow>
<ArgTableRow arg="fan6-speed" typ="num"></ArgTableRow>
</ArgTable>

### dude/ros/interface

**Package:** dude
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="R" typ="running"></ArgTableRow>
<ArgTableRow arg="S" typ="slave"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="default-name" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="string"></ArgTableRow>
<ArgTableRow arg="actual-mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="max-l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="fast-path" typ="bool"></ArgTableRow>
<ArgTableRow arg="last-link-down-time" typ="date"></ArgTableRow>
<ArgTableRow arg="last-link-up-time" typ="date"></ArgTableRow>
<ArgTableRow arg="link-downs" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-drop" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-drop" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-error" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-error" typ="num"></ArgTableRow>
<ArgTableRow arg="fp-rx-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="fp-tx-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="fp-rx-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="fp-tx-packet" typ="num"></ArgTableRow>
</ArgTable>

### dude/ros/lease

**Package:** dude
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="R" typ="radius"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="B" typ="blocked"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address" typ="alt { ipAddr
, ip6Addr
, enum
 }"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="use-src-mac" typ="bool"></ArgTableRow>
<ArgTableRow arg="client-id" typ="string"></ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string"></ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="super { enum (bottom | first) { bottom:0xffffffff, first:0 }
 }"></ArgTableRow>
<ArgTableRow arg="address-lists" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="server" typ="enum (all)"></ArgTableRow>
<ArgTableRow arg="block-access" typ="bool"></ArgTableRow>
<ArgTableRow arg="lease-time" typ="time"></ArgTableRow>
<ArgTableRow arg="always-broadcast" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcp-option" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="dhcp-option-set" typ="enum (none)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="enum (waiting | testing | busy | offered | bound | authorizing)"></ArgTableRow>
<ArgTableRow arg="expires-after" typ="time"></ArgTableRow>
<ArgTableRow arg="last-seen" typ="alt { enum (never | sometime) { never:0xffffffff, sometime:0xfffffffe }
, time
 }"></ArgTableRow>
<ArgTableRow arg="active-address" typ="alt { ipAddr
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="active-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="active-client-id" typ="string"></ArgTableRow>
<ArgTableRow arg="active-server" typ="enum"></ArgTableRow>
<ArgTableRow arg="host-name" typ="string"></ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="agent-circuit-id" typ="string"></ArgTableRow>
<ArgTableRow arg="agent-remote-id" typ="string"></ArgTableRow>
</ArgTable>

### dude/ros/neighbor

**Package:** dude
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="enum"></ArgTableRow>
<ArgTableRow arg="address" typ="alt { ipAddr
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="address4" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="address6" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="identity" typ="string"></ArgTableRow>
<ArgTableRow arg="platform" typ="string"></ArgTableRow>
<ArgTableRow arg="version" typ="string"></ArgTableRow>
<ArgTableRow arg="unpack" typ="enum (none | simple | uncompress-headers | uncompress-all)"></ArgTableRow>
<ArgTableRow arg="age" typ="time"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="software-id" typ="string"></ArgTableRow>
<ArgTableRow arg="board" typ="string"></ArgTableRow>
<ArgTableRow arg="ipv6" typ="bool"></ArgTableRow>
<ArgTableRow arg="interface-name" typ="string"></ArgTableRow>
</ArgTable>

### dude/ros/queue

**Package:** dude
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="target" typ="object { alt { alt { ipPrefix
, ip6Prefix
 } { ipPrefix
, ip6Prefix
 }
, enum
 } { alt { ipPrefix
, ip6Prefix
 } { ipPrefix
, ip6Prefix
 }
, enum
 }
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="dst" typ="alt { ipPrefix
, ip6Prefix
, enum
 }"></ArgTableRow>
<ArgTableRow arg="parent" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="packet-marks" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="priority" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="queue" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="limit-at" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="max-limit" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="burst-limit" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="burst-threshold" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="burst-time" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="bucket-size" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="total-priority" typ="num"></ArgTableRow>
<ArgTableRow arg="total-queue" typ="enum"></ArgTableRow>
<ArgTableRow arg="total-limit-at" typ="num"></ArgTableRow>
<ArgTableRow arg="total-max-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="total-burst-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="total-burst-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="total-burst-time" typ="time"></ArgTableRow>
<ArgTableRow arg="total-bucket-size" typ="num"></ArgTableRow>
<ArgTableRow arg="time" typ="super { time
, -time
, ,ubit (sun, mon, tue, wed, thu, fri, sat) { sun, mon, tue, wed, thu, fri, sat }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="bytes" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="total-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="packets" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="total-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="dropped" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="total-dropped" typ="num"></ArgTableRow>
<ArgTableRow arg="rate" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="total-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="packet-rate" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="total-packet-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="queued-packets" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="total-queued-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="queued-bytes" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="total-queued-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="pcq-queues" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="total-pcq-queues" typ="num"></ArgTableRow>
</ArgTable>

### dude/ros/registration-table

**Package:** dude
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="enum"></ArgTableRow>
<ArgTableRow arg="radio-name" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="ap" typ="bool"></ArgTableRow>
<ArgTableRow arg="wds" typ="bool"></ArgTableRow>
<ArgTableRow arg="bridge" typ="bool"></ArgTableRow>
<ArgTableRow arg="rx-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="tx-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="packets" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="bytes" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="frames" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="frame-bytes" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="hw-frames" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="hw-frame-bytes" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="packed-frames" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="packed-bytes" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="tx-frames-timed-out" typ="num"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="last-activity" typ="time"></ArgTableRow>
<ArgTableRow arg="signal-strength" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="signal-to-noise" typ="num"></ArgTableRow>
<ArgTableRow arg="signal-strength-ch0" typ="num"></ArgTableRow>
<ArgTableRow arg="signal-strength-ch1" typ="num"></ArgTableRow>
<ArgTableRow arg="signal-strength-ch2" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength-ch0" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength-ch1" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength-ch2" typ="num"></ArgTableRow>
<ArgTableRow arg="evm-ch0" typ="num"></ArgTableRow>
<ArgTableRow arg="evm-ch1" typ="num"></ArgTableRow>
<ArgTableRow arg="evm-ch2" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-evm-ch0" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-evm-ch1" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-evm-ch2" typ="num"></ArgTableRow>
<ArgTableRow arg="strength-at-rates" typ="multi { , , , super { num
, @enum () {  }
,  time
 } { num
, @enum () {  }
,  time
 }
 }"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-ccq" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-ccq" typ="num"></ArgTableRow>
<ArgTableRow arg="p-throughput" typ="num"></ArgTableRow>
<ArgTableRow arg="ack-timeout" typ="num"></ArgTableRow>
<ArgTableRow arg="distance" typ="num"></ArgTableRow>
<ArgTableRow arg="nstreme" typ="bool"></ArgTableRow>
<ArgTableRow arg="framing-mode" typ="enum (none | best-fit | exact-size)"></ArgTableRow>
<ArgTableRow arg="framing-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="framing-current-size" typ="num"></ArgTableRow>
<ArgTableRow arg="routeros-version" typ="string"></ArgTableRow>
<ArgTableRow arg="last-ip" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="ap-tx-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="client-tx-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="802.1x-port-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="authentication-type" typ="enum (wpa-psk | wpa2-psk | wpa-eap | wpa2-eap)"></ArgTableRow>
<ArgTableRow arg="encryption" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="group-encryption" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="management-protection" typ="bool"></ArgTableRow>
<ArgTableRow arg="compression" typ="bool"></ArgTableRow>
<ArgTableRow arg="wmm-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="wmm-ps-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="tx-rate-set" typ="string"></ArgTableRow>
<ArgTableRow arg="tdma-timing-offset" typ="num"></ArgTableRow>
<ArgTableRow arg="tdma-tx-size" typ="num"></ArgTableRow>
<ArgTableRow arg="tdma-rx-size" typ="num"></ArgTableRow>
<ArgTableRow arg="tdma-retx" typ="num"></ArgTableRow>
<ArgTableRow arg="tdma-winfull" typ="num"></ArgTableRow>
</ArgTable>

### dude/ros/resource

**Package:** dude
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="version" typ="string"></ArgTableRow>
<ArgTableRow arg="build-time" typ="string"></ArgTableRow>
<ArgTableRow arg="free-memory" typ="num"></ArgTableRow>
<ArgTableRow arg="total-memory" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu" typ="string"></ArgTableRow>
<ArgTableRow arg="cpu-count" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-frequency" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-load" typ="num"></ArgTableRow>
<ArgTableRow arg="free-hdd-space" typ="num"></ArgTableRow>
<ArgTableRow arg="total-hdd-space" typ="num"></ArgTableRow>
<ArgTableRow arg="write-sect-since-reboot" typ="num"></ArgTableRow>
<ArgTableRow arg="write-sect-total" typ="num"></ArgTableRow>
<ArgTableRow arg="bad-blocks" typ="num"></ArgTableRow>
<ArgTableRow arg="architecture-name" typ="string"></ArgTableRow>
<ArgTableRow arg="board-name" typ="string"></ArgTableRow>
<ArgTableRow arg="platform" typ="string"></ArgTableRow>
</ArgTable>

### dude/ros/route

**Package:** dude
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="A" typ="active"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="C" typ="connect"></ArgTableRow>
<ArgTableRow arg="S" typ="static"></ArgTableRow>
<ArgTableRow arg="r" typ="rip"></ArgTableRow>
<ArgTableRow arg="b" typ="bgp"></ArgTableRow>
<ArgTableRow arg="o" typ="ospf"></ArgTableRow>
<ArgTableRow arg="m" typ="mme"></ArgTableRow>
<ArgTableRow arg="B" typ="blackhole"></ArgTableRow>
<ArgTableRow arg="U" typ="unreachable"></ArgTableRow>
<ArgTableRow arg="P" typ="prohibit"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="ipPrefix"></ArgTableRow>
<ArgTableRow arg="pref-src" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="gateway" typ="object { alt { composite { ,  } { ,  }
, enum
, super { ipAddr
, [ @enum (main) { main:254 }]
 } { ipAddr
, [ @enum (main) { main:254 }]
 }
 } { composite { ,  } { ,  }
, enum
, super { ipAddr
, [ @enum (main) { main:254 }]
 } { ipAddr
, [ @enum (main) { main:254 }]
 }
 }
 }"></ArgTableRow>
<ArgTableRow arg="check-gateway" typ="enum (arp | ping)"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (unicast | blackhole | unreachable | prohibit)"></ArgTableRow>
<ArgTableRow arg="distance" typ="num"></ArgTableRow>
<ArgTableRow arg="scope" typ="num"></ArgTableRow>
<ArgTableRow arg="target-scope" typ="num"></ArgTableRow>
<ArgTableRow arg="routing-mark" typ="string"></ArgTableRow>
<ArgTableRow arg="vrf-interface" typ="enum"></ArgTableRow>
<ArgTableRow arg="bgp-as-path" typ="string"></ArgTableRow>
<ArgTableRow arg="bgp-local-pref" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp-prepend" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp-med" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp-atomic-aggregate" typ="bool"></ArgTableRow>
<ArgTableRow arg="bgp-origin" typ="enum (igp | egp | incomplete)"></ArgTableRow>
<ArgTableRow arg="bgp-communities" typ="multi { , , alt { enum (no-export | no-advertise | local-as) { no-export:0xFFFFFF01, no-advertise:0xFFFFFF02, local-as:0xFFFFFF03 }
, super { num [ .. 0xffff]
, :num [ .. 0xffff]
 } { num [ .. 0xffff]
, :num [ .. 0xffff]
 }
 } { enum (no-export | no-advertise | local-as) { no-export:0xFFFFFF01, no-advertise:0xFFFFFF02, local-as:0xFFFFFF03 }
, super { num [ .. 0xffff]
, :num [ .. 0xffff]
 } { num [ .. 0xffff]
, :num [ .. 0xffff]
 }
 }
 }"></ArgTableRow>
<ArgTableRow arg="route-tag" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="gateway-status" typ="object { super { alt { enum
, ipAddr
 } { enum
, ipAddr
 }
, [  on string]
, [  enum (unreachable | reachable | recursive | inactive) { unreachable:0, reachable:1, recursive:2, inactive:3 }]
, [  via multi { array-id, ipAddr
 } { array-id, ipAddr
 }]
, [  multi { array-id, enum
 } { array-id, enum
 }]
 } { alt { enum
, ipAddr
 } { enum
, ipAddr
 }
, [  on string]
, [  enum (unreachable | reachable | recursive | inactive) { unreachable:0, reachable:1, recursive:2, inactive:3 }]
, [  via multi { array-id, ipAddr
 } { array-id, ipAddr
 }]
, [  multi { array-id, enum
 } { array-id, enum
 }]
 }
 }"></ArgTableRow>
<ArgTableRow arg="bgp-weight" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp-ext-communities" typ="string"></ArgTableRow>
<ArgTableRow arg="received-from" typ="enum"></ArgTableRow>
<ArgTableRow arg="ospf-metric" typ="num"></ArgTableRow>
<ArgTableRow arg="ospf-type" typ="enum (intra-area | inter-area | external-type-1 | external-type-2 | nssa-external-type-1 | nssa-external-type-2)"></ArgTableRow>
</ArgTable>

### dude/ros/routerboard

**Package:** dude
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="routerboard" typ="bool"></ArgTableRow>
<ArgTableRow arg="model" typ="string"></ArgTableRow>
<ArgTableRow arg="serial-number" typ="string"></ArgTableRow>
<ArgTableRow arg="firmware-type" typ="string"></ArgTableRow>
<ArgTableRow arg="factory-firmware" typ="string"></ArgTableRow>
<ArgTableRow arg="current-firmware" typ="string"></ArgTableRow>
<ArgTableRow arg="upgrade-firmware" typ="string"></ArgTableRow>
</ArgTable>

## dude/service

**Package:** dude
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>

## dude/settings

**Package:** dude
**Type:** Settings Directory

## dude/vacuum-db

**Package:** dude
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>
