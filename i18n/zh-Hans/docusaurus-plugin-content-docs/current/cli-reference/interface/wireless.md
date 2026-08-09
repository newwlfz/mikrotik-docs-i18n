# 无线

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/wireless

**软件包:** wireless-rep
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="禁用"></ArgTableRow>
<ArgTableRow arg="R" typ="运行中"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp)"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { enum (auto) { auto:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="disable-running-check" typ="bool"></ArgTableRow>
<ArgTableRow arg="prism-cardtype" typ="enum (200mW | 100mW | 30mW)"></ArgTableRow>
<ArgTableRow arg="master-interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="radio-name" typ="string"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (station | station-wds | ap-bridge | bridge | alignment-only | nstreme-dual-slave | wds-slave | station-pseudobridge | station-pseudobridge-clone | station-bridge)"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="area" typ="string"></ArgTableRow>
<ArgTableRow arg="frequency-mode" typ="enum"></ArgTableRow>
<ArgTableRow arg="country" typ="enum"></ArgTableRow>
<ArgTableRow arg="installation" typ="enum (any | indoor | outdoor)"></ArgTableRow>
<ArgTableRow arg="antenna-gain" typ="num"></ArgTableRow>
<ArgTableRow arg="frequency" typ="alt { num
, enum (auto) { auto:0 }
 }"></ArgTableRow>
<ArgTableRow arg="band" typ="enum (2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac)"></ArgTableRow>
<ArgTableRow arg="channel-width" typ="enum (20mhz | 40mhz-turbo | 10mhz | 5mhz | 20/40mhz-Ce | 20/40mhz-eC | 20/40/80mhz-Ceee | 20/40/80mhz-eCee | 20/40/80mhz-eeCe | 20/40/80mhz-eeeC | 20/40/80/160mhz-Ceeeeeee | 20/40/80/160mhz-eCeeeeee | 20/40/80/160mhz-eeCeeeee | 20/40/80/160mhz-eeeCeeee | 20/40/80/160mhz-eeeeCeee | 20/40/80/160mhz-eeeeeCee | 20/40/80/160mhz-eeeeeeCe | 20/40/80/160mhz-eeeeeeeC | 20/40mhz-XX | 20/40/80mhz-XXXX | 20/40/80/160mhz-XXXXXXXX)"></ArgTableRow>
<ArgTableRow arg="secondary-frequency" typ="multi { array-id, enum (auto) { auto:0xffffffff }
 }"></ArgTableRow>
<ArgTableRow arg="scan-list" typ="object { alt { enum (default) { default:0 }
, super { num
, -num
, [ :num]
 } { num
, -num
, [ :num]
 }
, enum () { ,  }
 } { enum (default) { default:0 }
, super { num
, -num
, [ :num]
 } { num
, -num
, [ :num]
 }
, enum () { ,  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="wireless-protocol" typ="enum (unspecified | any | 802.11 | nstreme | nv2 | nv2-nstreme-802.11 | nv2-nstreme)"></ArgTableRow>
<ArgTableRow arg="rate-set" typ="enum (default | configured)"></ArgTableRow>
<ArgTableRow arg="supported-rates-b" typ="ubit (1Mbps, 2Mbps, 5.5Mbps, 11Mbps)"></ArgTableRow>
<ArgTableRow arg="supported-rates-a/g" typ="ubit (6Mbps, 9Mbps, 12Mbps, 18Mbps, 24Mbps, 36Mbps, 48Mbps, 54Mbps)"></ArgTableRow>
<ArgTableRow arg="basic-rates-b" typ="ubit (1Mbps, 2Mbps, 5.5Mbps, 11Mbps)"></ArgTableRow>
<ArgTableRow arg="basic-rates-a/g" typ="ubit (6Mbps, 9Mbps, 12Mbps, 18Mbps, 24Mbps, 36Mbps, 48Mbps, 54Mbps)"></ArgTableRow>
<ArgTableRow arg="max-station-count" typ="num"></ArgTableRow>
<ArgTableRow arg="distance" typ="enum (indoors | dynamic)"></ArgTableRow>
<ArgTableRow arg="tx-power" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="tx-power-mode" typ="enum (default | all-rates-fixed | card-rates | manual-table)"></ArgTableRow>
<ArgTableRow arg="noise-floor-threshold" typ="alt { enum (default) { default:5555 }
, num [-128 .. 127]
 }"></ArgTableRow>
<ArgTableRow arg="nv2-noise-floor-offset" typ="alt { enum (default) { default:5555 }
, num [0 .. 20]
 }"></ArgTableRow>
<ArgTableRow arg="burst-time" typ="enum (disabled)"></ArgTableRow>
<ArgTableRow arg="dfs-test-mode" typ="ubit (only-detect, duty-cycle, short-search)" syscap="dfstest"></ArgTableRow>
<ArgTableRow arg="antenna-mode" typ="enum (ant-a | ant-b | txa-rxb | rxa-txb)"></ArgTableRow>
<ArgTableRow arg="vlan-mode" typ="enum (no-tag | use-tag | use-service-tag)"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="wds-mode" typ="enum (disabled | static | dynamic | static-mesh | dynamic-mesh)"></ArgTableRow>
<ArgTableRow arg="wds-default-bridge" typ="iface_enum { none:0xffffffff }"></ArgTableRow>
<ArgTableRow arg="wds-default-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="wds-cost-range" typ="range"></ArgTableRow>
<ArgTableRow arg="wds-ignore-ssid" typ="bool"></ArgTableRow>
<ArgTableRow arg="update-stats-interval" typ="alt { enum (disabled) { disabled:0 }
, time [10 .. 18000]
 }"></ArgTableRow>
<ArgTableRow arg="bridge-mode" typ="enum (enabled | disabled)"></ArgTableRow>
<ArgTableRow arg="default-authentication" typ="bool"></ArgTableRow>
<ArgTableRow arg="default-forwarding" typ="bool"></ArgTableRow>
<ArgTableRow arg="default-ap-tx-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="default-client-tx-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="wmm-support" typ="enum (disabled | enabled | required)"></ArgTableRow>
<ArgTableRow arg="hide-ssid" typ="bool"></ArgTableRow>
<ArgTableRow arg="security-profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="interworking-profile" typ="enum (disabled)"></ArgTableRow>
<ArgTableRow arg="wps-mode" typ="enum (disabled | push-button | push-button-virtual-only | push-button-5s)"></ArgTableRow>
<ArgTableRow arg="station-roaming" typ="enum (disabled | enabled)"></ArgTableRow>
<ArgTableRow arg="disconnect-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="on-fail-retry-time" typ="time"></ArgTableRow>
<ArgTableRow arg="preamble-mode" typ="enum (long | short | both)"></ArgTableRow>
<ArgTableRow arg="compression" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow-sharedkey" typ="bool"></ArgTableRow>
<ArgTableRow arg="station-bridge-clone-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="ampdu-priorities" typ="ubit (0, 1, 2, 3, 4, 5, 6, 7)"></ArgTableRow>
<ArgTableRow arg="guard-interval" typ="enum (any | long)"></ArgTableRow>
<ArgTableRow arg="ht-supported-mcs" typ="ubit (mcs-0, mcs-1, mcs-2, mcs-3, mcs-4, mcs-5, mcs-6, mcs-7, mcs-8, mcs-9, mcs-10, mcs-11, mcs-12, mcs-13, mcs-14, mcs-15, mcs-16, mcs-17, mcs-18, mcs-19, mcs-20, mcs-21, mcs-22, mcs-23, mcs-24, mcs-25, mcs-26, mcs-27, mcs-28, mcs-29, mcs-30, mcs-31)"></ArgTableRow>
<ArgTableRow arg="ht-basic-mcs" typ="ubit (mcs-0, mcs-1, mcs-2, mcs-3, mcs-4, mcs-5, mcs-6, mcs-7, mcs-8, mcs-9, mcs-10, mcs-11, mcs-12, mcs-13, mcs-14, mcs-15, mcs-16, mcs-17, mcs-18, mcs-19, mcs-20, mcs-21, mcs-22, mcs-23, mcs-24, mcs-25, mcs-26, mcs-27, mcs-28, mcs-29, mcs-30, mcs-31)"></ArgTableRow>
<ArgTableRow arg="vht-supported-mcs" typ="multi { array-id, enum (none | mcs0-7 | mcs0-8 | mcs0-9) { none:0, mcs0-7:1, mcs0-8:2, mcs0-9:3 }
 }"></ArgTableRow>
<ArgTableRow arg="vht-basic-mcs" typ="multi { array-id, enum (none | mcs0-7 | mcs0-8 | mcs0-9) { none:0, mcs0-7:1, mcs0-8:2, mcs0-9:3 }
 }"></ArgTableRow>
<ArgTableRow arg="tx-chains" typ="ubit (0, 1, 2, 3)"></ArgTableRow>
<ArgTableRow arg="rx-chains" typ="ubit (0, 1, 2, 3)"></ArgTableRow>
<ArgTableRow arg="amsdu-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="amsdu-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="tdma-period-size" typ="enum (auto | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10)"></ArgTableRow>
<ArgTableRow arg="nv2-queue-count" typ="num"></ArgTableRow>
<ArgTableRow arg="nv2-qos" typ="enum (default | frame-priority)"></ArgTableRow>
<ArgTableRow arg="nv2-cell-radius" typ="num"></ArgTableRow>
<ArgTableRow arg="nv2-security" typ="enum (disabled | enabled)"></ArgTableRow>
<ArgTableRow arg="nv2-preshared-key" typ="string"></ArgTableRow>
<ArgTableRow arg="nv2-mode" typ="enum (dynamic-downlink | fixed-downlink | sync-master | sync-slave)"></ArgTableRow>
<ArgTableRow arg="nv2-downlink-ratio" typ="num"></ArgTableRow>
<ArgTableRow arg="nv2-sync-secret" typ="string"></ArgTableRow>
<ArgTableRow arg="hw-retries" typ="num"></ArgTableRow>
<ArgTableRow arg="frame-lifetime" typ="num"></ArgTableRow>
<ArgTableRow arg="adaptive-noise-immunity" typ="enum (none | client-mode | ap-and-client-mode)"></ArgTableRow>
<ArgTableRow arg="hw-fragmentation-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="hw-protection-mode" typ="enum (none | rts-cts | cts-to-self)"></ArgTableRow>
<ArgTableRow arg="hw-protection-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="frequency-offset" typ="num"></ArgTableRow>
<ArgTableRow arg="rate-selection" typ="enum (advanced)"></ArgTableRow>
<ArgTableRow arg="multicast-helper" typ="enum (default | disabled | full | dhcp)"></ArgTableRow>
<ArgTableRow arg="multicast-buffering" typ="bool"></ArgTableRow>
<ArgTableRow arg="keepalive-frames" typ="bool"></ArgTableRow>
<ArgTableRow arg="skip-dfs-channels" typ="enum (disabled | all | 10min-cac)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="default-name" typ="string"></ArgTableRow>
<ArgTableRow arg="interface-type" typ="enum (virtual | Atheros AR5212 | Atheros AR5211 | Atheros AR5210 | Prism | Atheros AR5213 | Atheros AR5413 | Atheros 11N | Atheros AR9271 | Atheros AR9300 | Atheros AR92xx | Atheros AR9888 | IPQ4019 | QCA9984 | QCA9888)"></ArgTableRow>
<ArgTableRow arg="pci-info" typ="string"></ArgTableRow>
</ArgTable>

### interface/wireless/access-list

**软件包:** wireless-rep
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="禁用"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum { , any:0 }"></ArgTableRow>
<ArgTableRow arg="signal-range" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="allow-signal-out-of-range" typ="alt { enum (always) { always:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="authentication" typ="bool"></ArgTableRow>
<ArgTableRow arg="forwarding" typ="bool"></ArgTableRow>
<ArgTableRow arg="ap-tx-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="client-tx-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="private-algo" typ="enum (none | 40bit-wep | 104bit-wep | aes-ccm | tkip)"></ArgTableRow>
<ArgTableRow arg="private-key" typ="string"></ArgTableRow>
<ArgTableRow arg="private-pre-shared-key" typ="string"></ArgTableRow>
<ArgTableRow arg="time" typ="super { time [0 .. 86400]
, -time [0 .. 86400]
, ,ubit (sun, mon, tue, wed, thu, fri, sat) { sun, mon, tue, wed, thu, fri, sat }
 }"></ArgTableRow>
<ArgTableRow arg="management-protection-key" typ="string"></ArgTableRow>
<ArgTableRow arg="vlan-mode" typ="enum (default | no-tag | use-tag | use-service-tag)"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
</ArgTable>

### interface/wireless/align

**软件包:** wireless-rep
**类型:** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="frame-size" typ="num"></ArgTableRow>
<ArgTableRow arg="active-mode" typ="bool"></ArgTableRow>
<ArgTableRow arg="receive-all" typ="bool"></ArgTableRow>
<ArgTableRow arg="audio-monitor" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="filter-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="ssid-all" typ="bool"></ArgTableRow>
<ArgTableRow arg="frames-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="audio-min" typ="num"></ArgTableRow>
<ArgTableRow arg="audio-max" typ="num"></ArgTableRow>
</ArgTable>

#### interface/wireless/align/monitor

**软件包:** wireless-rep
**类型:** 命令

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="A" typ="接入点"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="rxq" typ="num"></ArgTableRow>
<ArgTableRow arg="avg-rxq" typ="num"></ArgTableRow>
<ArgTableRow arg="last-rx" typ="num"></ArgTableRow>
<ArgTableRow arg="txq" typ="num"></ArgTableRow>
<ArgTableRow arg="last-tx" typ="num"></ArgTableRow>
<ArgTableRow arg="correct" typ="num"></ArgTableRow>
</ArgTable>

#### interface/wireless/align/test-audio

**软件包:** wireless-rep
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="test-value" typ="num"></ArgTableRow>
</ArgTable>

### interface/wireless/cap

**软件包:** wireless-rep
**类型:** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="interfaces" typ="multi { array-id, iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (request | none)"></ArgTableRow>
<ArgTableRow arg="lock-to-caps-man" typ="bool"></ArgTableRow>
<ArgTableRow arg="discovery-interfaces" typ="multi { array-id, iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="caps-man-addresses" typ="multi { array-id, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="caps-man-names" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="caps-man-certificate-common-names" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum { none:0xffffffff }"></ArgTableRow>
<ArgTableRow arg="static-virtual" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="requested-certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="locked-caps-man-common-name" typ="string"></ArgTableRow>
</ArgTable>

### interface/wireless/channels

**软件包:** wireless-rep
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="禁用"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="list" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="frequency" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="width" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="band" typ="enum (2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="extension-channel" typ="enum (disabled | Ce | eC | Ceee | eCee | eeCe | eeeC)"></ArgTableRow>
</ArgTable>

### interface/wireless/connect-list

**软件包:** wireless-rep
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="禁用"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="connect" typ="bool"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="signal-range" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="allow-signal-out-of-range" typ="alt { enum (always) { always:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="area-prefix" typ="string"></ArgTableRow>
<ArgTableRow arg="security-profile" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="wireless-protocol" typ="enum (any | 802.11 | nstreme | tdma)"></ArgTableRow>
<ArgTableRow arg="interworking" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="iw-network-type" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="iw-venue" typ="enum (any | assembly | business | educational | industrial | institutional | mercantile | residential | storage | utility | vehicular | outdoor)"></ArgTableRow>
<ArgTableRow arg="iw-hessid" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="iw-internet" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="iw-asra" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="iw-esr" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="iw-uesa" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="iw-hotspot20" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="iw-hotspot20-dgaf" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="iw-roaming-ois" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="iw-authentication-types" typ="object { enum (terms-and-conditions | online-enrollment | https-redirection | dns-redirection) { terms-and-conditions:0, online-enrollment:1, https-redirection:2, dns-redirection:3 }
 }"></ArgTableRow>
<ArgTableRow arg="iw-ipv4-availability" typ="enum (any | not-available | public | port-restricted | single-nated | double-nated | port-restricted-single-nated | port-restricted-double-nated | unknown)"></ArgTableRow>
<ArgTableRow arg="iw-ipv6-availability" typ="enum (any | not-available | available | unknown)"></ArgTableRow>
<ArgTableRow arg="iw-realms" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="3gpp" typ="string"></ArgTableRow>
<ArgTableRow arg="iw-connection-capabilities" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
</ArgTable>

### interface/wireless/frequency-monitor

**软件包:** wireless-rep
**类型:** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="freq" typ="num"></ArgTableRow>
<ArgTableRow arg="use" typ="num"></ArgTableRow>
<ArgTableRow arg="nf" typ="num"></ArgTableRow>
</ArgTable>

### interface/wireless/info

**软件包:** wireless-rep
**类型:** 目录

#### interface/wireless/info/allowed-channels

**软件包:** wireless-rep
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="frequency-mode" typ="enum"></ArgTableRow>
<ArgTableRow arg="country" typ="enum"></ArgTableRow>
<ArgTableRow arg="band" typ="enum (2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac)"></ArgTableRow>
<ArgTableRow arg="channel-width" typ="enum (20mhz | 40mhz-turbo | 10mhz | 5mhz | 20/40mhz-Ce | 20/40mhz-eC | 20/40/80mhz-Ceee | 20/40/80mhz-eCee | 20/40/80mhz-eeCe | 20/40/80mhz-eeeC)"></ArgTableRow>
<ArgTableRow arg="antenna-gain" typ="num"></ArgTableRow>
<ArgTableRow arg="dfs-mode" typ="enum (none | no-radar-detect | radar-detect)"></ArgTableRow>
<ArgTableRow arg="installation" typ="enum (any | indoor | outdoor)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="channels" typ="multi { array-id, string
 }"></ArgTableRow>
</ArgTable>

#### interface/wireless/info/country-info

**软件包:** wireless-rep
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="country" typ="enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="ranges" typ="multi { array-id, string
 }"></ArgTableRow>
</ArgTable>

#### interface/wireless/info/country-list

**软件包:** wireless-rep
**类型:** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="countries" typ="multi { array-id, string
 }"></ArgTableRow>
</ArgTable>

#### interface/wireless/info/default-scan-list

**软件包:** wireless-rep
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="frequency-mode" typ="enum"></ArgTableRow>
<ArgTableRow arg="country" typ="enum"></ArgTableRow>
<ArgTableRow arg="band" typ="enum (2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac)"></ArgTableRow>
<ArgTableRow arg="channel-width" typ="enum (20mhz | 40mhz-turbo | 10mhz | 5mhz | 20/40mhz-Ce | 20/40mhz-eC | 20/40/80mhz-Ceee | 20/40/80mhz-eCee | 20/40/80mhz-eeCe | 20/40/80mhz-eeeC)"></ArgTableRow>
<ArgTableRow arg="antenna-gain" typ="num"></ArgTableRow>
<ArgTableRow arg="dfs-mode" typ="enum (none | no-radar-detect | radar-detect)"></ArgTableRow>
<ArgTableRow arg="installation" typ="enum (any | indoor | outdoor)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="channels" typ="multi { array-id, string
 }"></ArgTableRow>
</ArgTable>

#### interface/wireless/info/hw-info

**软件包:** wireless-rep
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="ranges" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="tx-chains" typ="ubit (0, 1, 2, 3)"></ArgTableRow>
<ArgTableRow arg="rx-chains" typ="ubit (0, 1, 2, 3)"></ArgTableRow>
<ArgTableRow arg="extra-info" typ="string"></ArgTableRow>
<ArgTableRow arg="locked-countries" typ="multi { array-id, enum
 }"></ArgTableRow>
</ArgTable>

#### interface/wireless/info/scan-list

**软件包:** wireless-rep
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="frequency-mode" typ="enum"></ArgTableRow>
<ArgTableRow arg="country" typ="enum"></ArgTableRow>
<ArgTableRow arg="band" typ="enum (2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac)"></ArgTableRow>
<ArgTableRow arg="channel-width" typ="enum (20mhz | 40mhz-turbo | 10mhz | 5mhz | 20/40mhz-Ce | 20/40mhz-eC | 20/40/80mhz-Ceee | 20/40/80mhz-eCee | 20/40/80mhz-eeCe | 20/40/80mhz-eeeC)"></ArgTableRow>
<ArgTableRow arg="antenna-gain" typ="num"></ArgTableRow>
<ArgTableRow arg="dfs-mode" typ="enum (none | no-radar-detect | radar-detect)"></ArgTableRow>
<ArgTableRow arg="installation" typ="enum (any | indoor | outdoor)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="channels" typ="multi { array-id, string
 }"></ArgTableRow>
</ArgTable>

### interface/wireless/interworking-profiles

**软件包:** wireless-rep
**类型:** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="network-type" typ="enum (private | private-with-guest | public-chargeable | public-free | personal-device | emergency-only | test | wildcard)"></ArgTableRow>
<ArgTableRow arg="internet" typ="bool"></ArgTableRow>
<ArgTableRow arg="asra" typ="bool"></ArgTableRow>
<ArgTableRow arg="esr" typ="bool"></ArgTableRow>
<ArgTableRow arg="uesa" typ="bool"></ArgTableRow>
<ArgTableRow arg="venue" typ="enum (unspecified | disabled)"></ArgTableRow>
<ArgTableRow arg="hessid" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="hotspot20" typ="bool"></ArgTableRow>
<ArgTableRow arg="hotspot20-dgaf" typ="bool"></ArgTableRow>
<ArgTableRow arg="roaming-ois" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="venue-names" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="authentication-types" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="ipv4-availability" typ="enum (not-available | public | port-restricted | single-nated | double-nated | port-restricted-single-nated | port-restricted-double-n