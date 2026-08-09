# Wireless

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/wireless

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="R" typ="running"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
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

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="default-name" typ="string"></ArgTableRow>
<ArgTableRow arg="interface-type" typ="enum (virtual | Atheros AR5212 | Atheros AR5211 | Atheros AR5210 | Prism | Atheros AR5213 | Atheros AR5413 | Atheros 11N | Atheros AR9271 | Atheros AR9300 | Atheros AR92xx | Atheros AR9888 | IPQ4019 | QCA9984 | QCA9888)"></ArgTableRow>
<ArgTableRow arg="pci-info" typ="string"></ArgTableRow>
</ArgTable>

### interface/wireless/access-list

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
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

**Package:** wireless-rep
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
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

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="A" typ="access-point"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
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

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="test-value" typ="num"></ArgTableRow>
</ArgTable>

### interface/wireless/cap

**Package:** wireless-rep
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
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

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="requested-certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="locked-caps-man-common-name" typ="string"></ArgTableRow>
</ArgTable>

### interface/wireless/channels

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="list" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="frequency" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="width" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="band" typ="enum (2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="extension-channel" typ="enum (disabled | Ce | eC | Ceee | eCee | eeCe | eeeC)"></ArgTableRow>
</ArgTable>

### interface/wireless/connect-list

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
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

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="freq" typ="num"></ArgTableRow>
<ArgTableRow arg="use" typ="num"></ArgTableRow>
<ArgTableRow arg="nf" typ="num"></ArgTableRow>
</ArgTable>

### interface/wireless/info

**Package:** wireless-rep
**Type:** Directory

#### interface/wireless/info/allowed-channels

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="frequency-mode" typ="enum"></ArgTableRow>
<ArgTableRow arg="country" typ="enum"></ArgTableRow>
<ArgTableRow arg="band" typ="enum (2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac)"></ArgTableRow>
<ArgTableRow arg="channel-width" typ="enum (20mhz | 40mhz-turbo | 10mhz | 5mhz | 20/40mhz-Ce | 20/40mhz-eC | 20/40/80mhz-Ceee | 20/40/80mhz-eCee | 20/40/80mhz-eeCe | 20/40/80mhz-eeeC)"></ArgTableRow>
<ArgTableRow arg="antenna-gain" typ="num"></ArgTableRow>
<ArgTableRow arg="dfs-mode" typ="enum (none | no-radar-detect | radar-detect)"></ArgTableRow>
<ArgTableRow arg="installation" typ="enum (any | indoor | outdoor)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="channels" typ="multi { array-id, string
 }"></ArgTableRow>
</ArgTable>

#### interface/wireless/info/country-info

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="country" typ="enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="ranges" typ="multi { array-id, string
 }"></ArgTableRow>
</ArgTable>

#### interface/wireless/info/country-list

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="countries" typ="multi { array-id, string
 }"></ArgTableRow>
</ArgTable>

#### interface/wireless/info/default-scan-list

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="frequency-mode" typ="enum"></ArgTableRow>
<ArgTableRow arg="country" typ="enum"></ArgTableRow>
<ArgTableRow arg="band" typ="enum (2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac)"></ArgTableRow>
<ArgTableRow arg="channel-width" typ="enum (20mhz | 40mhz-turbo | 10mhz | 5mhz | 20/40mhz-Ce | 20/40mhz-eC | 20/40/80mhz-Ceee | 20/40/80mhz-eCee | 20/40/80mhz-eeCe | 20/40/80mhz-eeeC)"></ArgTableRow>
<ArgTableRow arg="antenna-gain" typ="num"></ArgTableRow>
<ArgTableRow arg="dfs-mode" typ="enum (none | no-radar-detect | radar-detect)"></ArgTableRow>
<ArgTableRow arg="installation" typ="enum (any | indoor | outdoor)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="channels" typ="multi { array-id, string
 }"></ArgTableRow>
</ArgTable>

#### interface/wireless/info/hw-info

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="ranges" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="tx-chains" typ="ubit (0, 1, 2, 3)"></ArgTableRow>
<ArgTableRow arg="rx-chains" typ="ubit (0, 1, 2, 3)"></ArgTableRow>
<ArgTableRow arg="extra-info" typ="string"></ArgTableRow>
<ArgTableRow arg="locked-countries" typ="multi { array-id, enum
 }"></ArgTableRow>
</ArgTable>

#### interface/wireless/info/scan-list

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="frequency-mode" typ="enum"></ArgTableRow>
<ArgTableRow arg="country" typ="enum"></ArgTableRow>
<ArgTableRow arg="band" typ="enum (2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac)"></ArgTableRow>
<ArgTableRow arg="channel-width" typ="enum (20mhz | 40mhz-turbo | 10mhz | 5mhz | 20/40mhz-Ce | 20/40mhz-eC | 20/40/80mhz-Ceee | 20/40/80mhz-eCee | 20/40/80mhz-eeCe | 20/40/80mhz-eeeC)"></ArgTableRow>
<ArgTableRow arg="antenna-gain" typ="num"></ArgTableRow>
<ArgTableRow arg="dfs-mode" typ="enum (none | no-radar-detect | radar-detect)"></ArgTableRow>
<ArgTableRow arg="installation" typ="enum (any | indoor | outdoor)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="channels" typ="multi { array-id, string
 }"></ArgTableRow>
</ArgTable>

### interface/wireless/interworking-profiles

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
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
<ArgTableRow arg="ipv4-availability" typ="enum (not-available | public | port-restricted | single-nated | double-nated | port-restricted-single-nated | port-restricted-double-nated | unknown)"></ArgTableRow>
<ArgTableRow arg="ipv6-availability" typ="enum (not-available | available | unknown)"></ArgTableRow>
<ArgTableRow arg="realms" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="realms-raw" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="3gpp-raw" typ="string"></ArgTableRow>
<ArgTableRow arg="3gpp-info" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="domain-names" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="operator-names" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="wan-status" typ="enum (reserved | up | down | test)"></ArgTableRow>
<ArgTableRow arg="wan-symmetric" typ="bool"></ArgTableRow>
<ArgTableRow arg="wan-at-capacity" typ="bool"></ArgTableRow>
<ArgTableRow arg="wan-downlink" typ="num"></ArgTableRow>
<ArgTableRow arg="wan-uplink" typ="num"></ArgTableRow>
<ArgTableRow arg="wan-downlink-load" typ="num"></ArgTableRow>
<ArgTableRow arg="wan-uplink-load" typ="num"></ArgTableRow>
<ArgTableRow arg="wan-measurement-duration" typ="num"></ArgTableRow>
<ArgTableRow arg="connection-capabilities" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="operational-classes" typ="multi { array-id, num
 }"></ArgTableRow>
</ArgTable>

### interface/wireless/manual-tx-power-table

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="manual-tx-powers" typ="multi { array-id, array-id, composite { ,  } { ,  }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
</ArgTable>

### interface/wireless/monitor

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="enum (disabled | searching-for-network | connected-to-ess | initializing | searching-for-frequency | radar-detecting | running-ap | tkip-countermeasures | nstreme-dual-slave)"></ArgTableRow>
<ArgTableRow arg="status-reason" typ="string"></ArgTableRow>
<ArgTableRow arg="channel" typ="string"></ArgTableRow>
<ArgTableRow arg="wireless-protocol" typ="enum (802.11 | nstreme | nv2)"></ArgTableRow>
<ArgTableRow arg="nstreme-status" typ="bool"></ArgTableRow>
<ArgTableRow arg="tx-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="rx-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="bssid" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="radio-name" typ="string"></ArgTableRow>
<ArgTableRow arg="signal-strength" typ="num"></ArgTableRow>
<ArgTableRow arg="signal-strength-ch0" typ="num"></ArgTableRow>
<ArgTableRow arg="signal-strength-ch1" typ="num"></ArgTableRow>
<ArgTableRow arg="signal-strength-ch2" typ="num"></ArgTableRow>
<ArgTableRow arg="signal-strength-ch3" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength-ch0" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength-ch1" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength-ch2" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength-ch3" typ="num"></ArgTableRow>
<ArgTableRow arg="noise-floor" typ="num"></ArgTableRow>
<ArgTableRow arg="signal-to-noise" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-ccq" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-ccq" typ="num"></ArgTableRow>
<ArgTableRow arg="p-throughput" typ="num"></ArgTableRow>
<ArgTableRow arg="overall-tx-ccq" typ="num"></ArgTableRow>
<ArgTableRow arg="registered-clients" typ="num"></ArgTableRow>
<ArgTableRow arg="authenticated-clients" typ="num"></ArgTableRow>
<ArgTableRow arg="current-ack-timeout" typ="num"></ArgTableRow>
<ArgTableRow arg="current-distance" typ="num"></ArgTableRow>
<ArgTableRow arg="wds-link" typ="bool"></ArgTableRow>
<ArgTableRow arg="bridge" typ="bool"></ArgTableRow>
<ArgTableRow arg="nstreme" typ="bool"></ArgTableRow>
<ArgTableRow arg="polling" typ="bool"></ArgTableRow>
<ArgTableRow arg="csma-disabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="framing-mode" typ="enum (none | best-fit | exact-size)"></ArgTableRow>
<ArgTableRow arg="framing-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="framing-current-size" typ="num"></ArgTableRow>
<ArgTableRow arg="routeros-version" typ="string"></ArgTableRow>
<ArgTableRow arg="last-ip" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="802.1x-port-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="authentication-type" typ="enum (wpa-psk | wpa2-psk | wpa-eap | wpa2-eap)"></ArgTableRow>
<ArgTableRow arg="encryption" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="group-encryption" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="management-protection" typ="bool"></ArgTableRow>
<ArgTableRow arg="compression" typ="bool"></ArgTableRow>
<ArgTableRow arg="wmm-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="nv2-sync-state" typ="enum (searching | syncing | synced)"></ArgTableRow>
<ArgTableRow arg="nv2-sync-master" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="nv2-sync-distance" typ="num"></ArgTableRow>
<ArgTableRow arg="nv2-sync-period-size" typ="num"></ArgTableRow>
<ArgTableRow arg="nv2-sync-downlink-ratio" typ="num"></ArgTableRow>
<ArgTableRow arg="current-tx-powers" typ="multi { , , , , super { enum () {  }
, :num
, (num
, num
 } { enum () {  }
, :num
, (num
, num
 }
 }"></ArgTableRow>
<ArgTableRow arg="current-ofdm-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="current-cck-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="1s-frames" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="1s-compressed-frames" typ="num"></ArgTableRow>
<ArgTableRow arg="1s-bytes" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="1s-length-of-orig" typ="num"></ArgTableRow>
<ArgTableRow arg="total-frames" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="total-compressed-frames" typ="num"></ArgTableRow>
<ArgTableRow arg="total-bytes" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="total-length-of-orig" typ="num"></ArgTableRow>
<ArgTableRow arg="notify-external-fdb" typ="bool"></ArgTableRow>
<ArgTableRow arg="cloned-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="searching-for-address-to-clone" typ="bool"></ArgTableRow>
</ArgTable>

### interface/wireless/nstreme

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enable-nstreme" typ="bool"></ArgTableRow>
<ArgTableRow arg="enable-polling" typ="bool"></ArgTableRow>
<ArgTableRow arg="disable-csma" typ="bool"></ArgTableRow>
<ArgTableRow arg="framer-policy" typ="enum (none | best-fit | exact-size | dynamic-size)"></ArgTableRow>
<ArgTableRow arg="framer-limit" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
</ArgTable>

### interface/wireless/nstreme-dual

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="R" typ="running"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp)"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { enum (auto) { auto:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="disable-running-check" typ="bool"></ArgTableRow>
<ArgTableRow arg="tx-radio" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="rx-radio" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="remote-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="tx-band" typ="enum (2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n)"></ArgTableRow>
<ArgTableRow arg="tx-channel-width" typ="enum (20mhz | 40mhz | 10mhz | 5mhz)"></ArgTableRow>
<ArgTableRow arg="tx-frequency" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-band" typ="enum (2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n)"></ArgTableRow>
<ArgTableRow arg="rx-channel-width" typ="enum (20mhz | 40mhz | 10mhz | 5mhz)"></ArgTableRow>
<ArgTableRow arg="rx-frequency" typ="num"></ArgTableRow>
<ArgTableRow arg="disable-csma" typ="bool"></ArgTableRow>
<ArgTableRow arg="rates-b" typ="ubit (1Mbps, 2Mbps, 5.5Mbps, 11Mbps)"></ArgTableRow>
<ArgTableRow arg="rates-a/g" typ="ubit (6Mbps, 9Mbps, 12Mbps, 18Mbps, 24Mbps, 36Mbps, 48Mbps, 54Mbps)"></ArgTableRow>
<ArgTableRow arg="ht-rates" typ="ubit (1, 2, 3, 4, 5, 6, 7, 8)"></ArgTableRow>
<ArgTableRow arg="ht-guard-interval" typ="enum (long | short | both)"></ArgTableRow>
<ArgTableRow arg="ht-channel-width" typ="enum (20mhz | 40mhz | 2040mhz)"></ArgTableRow>
<ArgTableRow arg="ht-streams" typ="enum (single | double | both)"></ArgTableRow>
<ArgTableRow arg="framer-policy" typ="enum (none | best-fit | exact-size)"></ArgTableRow>
<ArgTableRow arg="framer-limit" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
</ArgTable>

#### interface/wireless/nstreme-dual/monitor

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="rx-signal-strength" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="tx-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="connected" typ="bool"></ArgTableRow>
<ArgTableRow arg="packets" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="bytes" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="frames" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="frame-bytes" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="hw-frames" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="hw-frame-bytes" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="tx-retries-timeout" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-retries-lost" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bad-seqs" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-duplicates" typ="num"></ArgTableRow>
</ArgTable>

#### interface/wireless/nstreme-dual/reset-counters

**Package:** wireless-rep
**Type:** Command

### interface/wireless/registration-table

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
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
<ArgTableRow arg="signal-strength-ch3" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength-ch0" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength-ch1" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength-ch2" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength-ch3" typ="num"></ArgTableRow>
<ArgTableRow arg="evm-ch0" typ="num"></ArgTableRow>
<ArgTableRow arg="evm-ch1" typ="num"></ArgTableRow>
<ArgTableRow arg="evm-ch2" typ="num"></ArgTableRow>
<ArgTableRow arg="evm-ch3" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-evm-ch0" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-evm-ch1" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-evm-ch2" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-evm-ch3" typ="num"></ArgTableRow>
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
<ArgTableRow arg="nstreme-plus" typ="bool"></ArgTableRow>
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
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="tdma-timing-offset" typ="num"></ArgTableRow>
<ArgTableRow arg="tdma-tx-size" typ="num"></ArgTableRow>
<ArgTableRow arg="tdma-rx-size" typ="num"></ArgTableRow>
<ArgTableRow arg="tdma-retx" typ="num"></ArgTableRow>
<ArgTableRow arg="tdma-winfull" typ="num"></ArgTableRow>
<ArgTableRow arg="eap-identity" typ="string"></ArgTableRow>
</ArgTable>

#### interface/wireless/registration-table/reset-counters

**Package:** wireless-rep
**Type:** Command

### interface/wireless/reset-configuration

**Package:** wireless-rep
**Type:** Command

### interface/wireless/reset-mac-address

**Package:** wireless-rep
**Type:** Command

### interface/wireless/scan

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="A" typ="active"></ArgTableRow>
<ArgTableRow arg="P" typ="privacy"></ArgTableRow>
<ArgTableRow arg="R" typ="routeros-network"></ArgTableRow>
<ArgTableRow arg="N" typ="nstreme"></ArgTableRow>
<ArgTableRow arg="T" typ="tdma"></ArgTableRow>
<ArgTableRow arg="W" typ="wds"></ArgTableRow>
<ArgTableRow arg="B" typ="bridge"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="background" typ="bool"></ArgTableRow>
<ArgTableRow arg="save-file" typ="string"></ArgTableRow>
<ArgTableRow arg="rounds" typ="num"></ArgTableRow>
<ArgTableRow arg="passive" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="channel" typ="string"></ArgTableRow>
<ArgTableRow arg="sig" typ="num"></ArgTableRow>
<ArgTableRow arg="nf" typ="num"></ArgTableRow>
<ArgTableRow arg="snr" typ="num"></ArgTableRow>
<ArgTableRow arg="radio-name" typ="string"></ArgTableRow>
<ArgTableRow arg="routeros-version" typ="string"></ArgTableRow>
</ArgTable>

### interface/wireless/security-profiles

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (none | static-keys-optional | static-keys-required | dynamic-keys)"></ArgTableRow>
<ArgTableRow arg="authentication-types" typ="ubit (wpa-psk, wpa2-psk, wpa-eap, wpa2-eap)"></ArgTableRow>
<ArgTableRow arg="unicast-ciphers" typ="ubit (tkip, aes-ccm)"></ArgTableRow>
<ArgTableRow arg="group-ciphers" typ="ubit (tkip, aes-ccm)"></ArgTableRow>
<ArgTableRow arg="wpa-pre-shared-key" typ="string"></ArgTableRow>
<ArgTableRow arg="wpa2-pre-shared-key" typ="string"></ArgTableRow>
<ArgTableRow arg="supplicant-identity" typ="string"></ArgTableRow>
<ArgTableRow arg="eap-methods" typ="multi { array-id, enum (eap-tls | eap-ttls-mschapv2 | peap | passthrough) { eap-tls:13, eap-ttls-mschapv2:21, peap:25, passthrough:0xffffffff }
 }"></ArgTableRow>
<ArgTableRow arg="tls-mode" typ="enum (verify-certificate | dont-verify-certificate | no-certificates | verify-certificate-with-crl)"></ArgTableRow>
<ArgTableRow arg="tls-certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="mschapv2-username" typ="string"></ArgTableRow>
<ArgTableRow arg="mschapv2-password" typ="string"></ArgTableRow>
<ArgTableRow arg="disable-pmkid" typ="bool"></ArgTableRow>
<ArgTableRow arg="static-algo-0" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="static-key-0" typ="string"></ArgTableRow>
<ArgTableRow arg="static-algo-1" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="static-key-1" typ="string"></ArgTableRow>
<ArgTableRow arg="static-algo-2" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="static-key-2" typ="string"></ArgTableRow>
<ArgTableRow arg="static-algo-3" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="static-key-3" typ="string"></ArgTableRow>
<ArgTableRow arg="static-transmit-key" typ="enum (key-0 | key-1 | key-2 | key-3)"></ArgTableRow>
<ArgTableRow arg="static-sta-private-algo" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="static-sta-private-key" typ="string"></ArgTableRow>
<ArgTableRow arg="radius-mac-authentication" typ="bool"></ArgTableRow>
<ArgTableRow arg="radius-mac-accounting" typ="bool"></ArgTableRow>
<ArgTableRow arg="radius-eap-accounting" typ="bool"></ArgTableRow>
<ArgTableRow arg="interim-update" typ="time"></ArgTableRow>
<ArgTableRow arg="radius-mac-format" typ="enum (XX:XX:XX:XX:XX:XX | XXXX:XXXX:XXXX | XXXXXX:XXXXXX | XX-XX-XX-XX-XX-XX | XXXXXX-XXXXXX | XXXXXXXXXXXX | XX XX XX XX XX XX | xx:xx:xx:xx:xx:xx | xxxx:xxxx:xxxx | xxxxxx:xxxxxx | xx-xx-xx-xx-xx-xx | xxxxxx-xxxxxx | xxxxxxxxxxxx | xx xx xx xx xx xx)"></ArgTableRow>
<ArgTableRow arg="radius-mac-mode" typ="enum (as-username | as-username-and-password)"></ArgTableRow>
<ArgTableRow arg="radius-called-format" typ="enum (mac:ssid | mac | ssid)"></ArgTableRow>
<ArgTableRow arg="radius-mac-caching" typ="alt { enum (disabled) { disabled:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="group-key-update" typ="time"></ArgTableRow>
<ArgTableRow arg="management-protection" typ="enum (allowed | required | disabled)"></ArgTableRow>
<ArgTableRow arg="management-protection-key" typ="string"></ArgTableRow>
</ArgTable>

### interface/wireless/setup-repeater

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string"></ArgTableRow>
<ArgTableRow arg="country" typ="enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

### interface/wireless/sniffer

**Package:** wireless-rep
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="multiple-channels" typ="bool"></ArgTableRow>
<ArgTableRow arg="channel-time" typ="time"></ArgTableRow>
<ArgTableRow arg="only-headers" typ="bool"></ArgTableRow>
<ArgTableRow arg="receive-errors" typ="bool"></ArgTableRow>
<ArgTableRow arg="memory-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="file-name" typ="string"></ArgTableRow>
<ArgTableRow arg="file-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="streaming-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="streaming-server" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="streaming-max-rate" typ="num"></ArgTableRow>
</ArgTable>

#### interface/wireless/sniffer/packet

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="E" typ="crc-error"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="time" typ="num"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="channel" typ="string"></ArgTableRow>
<ArgTableRow arg="signal-at-rate" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="dst" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="src" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (assoc-req | assoc-resp | reassoc-req | reassoc-resp | probe-req | probe-resp | beacon | atim | disassoc | auth | deauth | ps-poll | rts | cts | ack | cf-end | cf-endack | data | d-cfack | d-cfpoll | d-cfackpoll | data-null | nd-cfack | nd-cfpoll | nd-cfackpoll)"></ArgTableRow>
</ArgTable>

#### interface/wireless/sniffer/save

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="file-name" typ="string"></ArgTableRow>
</ArgTable>

#### interface/wireless/sniffer/sniff

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="processed-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="file-size" typ="num"></ArgTableRow>
<ArgTableRow arg="file-saved-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="file-over-limit-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="memory-size" typ="num"></ArgTableRow>
<ArgTableRow arg="memory-saved-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="memory-over-limit-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="stream-dropped-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="stream-sent-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="real-file-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="real-memory-limit" typ="num"></ArgTableRow>
</ArgTable>

### interface/wireless/snooper

**Package:** wireless-rep
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="multiple-channels" typ="bool"></ArgTableRow>
<ArgTableRow arg="channel-time" typ="time"></ArgTableRow>
<ArgTableRow arg="receive-errors" typ="bool"></ArgTableRow>
</ArgTable>

#### interface/wireless/snooper/flat-snoop

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="type" typ="enum (frequency | network | station)"></ArgTableRow>
<ArgTableRow arg="channel" typ="string"></ArgTableRow>
<ArgTableRow arg="use" typ="num"></ArgTableRow>
<ArgTableRow arg="bitrate" typ="alt { num
, num
, num
 }"></ArgTableRow>
<ArgTableRow arg="frequency-network-count" typ="num"></ArgTableRow>
<ArgTableRow arg="noise-floor" typ="num"></ArgTableRow>
<ArgTableRow arg="frequency-station-count" typ="num"></ArgTableRow>
<ArgTableRow arg="active" typ="alt { bool
, bool
 }"></ArgTableRow>
<ArgTableRow arg="frequency-known" typ="bool"></ArgTableRow>
<ArgTableRow arg="beacon-seen" typ="bool"></ArgTableRow>
<ArgTableRow arg="address" typ="alt { macAddr
, macAddr
 }"></ArgTableRow>
<ArgTableRow arg="network-ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="beacon-hides-ssid" typ="bool"></ArgTableRow>
<ArgTableRow arg="beacon-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="beacon-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="last-beacon" typ="time"></ArgTableRow>
<ArgTableRow arg="beacon-strength" typ="num"></ArgTableRow>
<ArgTableRow arg="signal-to-noise" typ="alt { num
, num
 }"></ArgTableRow>
<ArgTableRow arg="ssid-source" typ="enum (none | association-discussion | probe-response | beacon)"></ArgTableRow>
<ArgTableRow arg="supported-rates" typ="multi { array-id, enum () {  }
 }"></ArgTableRow>
<ArgTableRow arg="basic-rates" typ="multi { array-id, enum () {  }
 }"></ArgTableRow>
<ArgTableRow arg="network-capabilities" typ="multi { array-id, enum () {  }
 }"></ArgTableRow>
<ArgTableRow arg="mt-network" typ="bool"></ArgTableRow>
<ArgTableRow arg="mt-info" typ="multi { array-id, enum (nstreme | doing-wds | without-polling | dynamic-packing-size) { nstreme:0, doing-wds:2, without-polling:3, dynamic-packing-size:4 }
 }"></ArgTableRow>
<ArgTableRow arg="mt-name" typ="alt { string
, string
 }"></ArgTableRow>
<ArgTableRow arg="mt-routeros-version" typ="alt { string
, string
 }"></ArgTableRow>
<ArgTableRow arg="mt-mru" typ="alt { num
, num
 }"></ArgTableRow>
<ArgTableRow arg="mt-framing-mode" typ="enum (none | best-fit | exact-size)"></ArgTableRow>
<ArgTableRow arg="network-station-count" typ="num"></ArgTableRow>
<ArgTableRow arg="use-of-freq" typ="alt { num
, num
 }"></ArgTableRow>
<ArgTableRow arg="use-of-traffic" typ="alt { num
, num
 }"></ArgTableRow>
<ArgTableRow arg="freq-source" typ="enum (seen-frame-on-freq | network-on-freq)"></ArgTableRow>
<ArgTableRow arg="last-seen" typ="time"></ArgTableRow>
<ArgTableRow arg="signal-strength" typ="num"></ArgTableRow>
<ArgTableRow arg="network-source" typ="enum (none | seen-data-frame | seen-successful-auth | seen-successful-assoc | forms-network)"></ArgTableRow>
<ArgTableRow arg="seen-wep" typ="bool"></ArgTableRow>
<ArgTableRow arg="station-rates" typ="multi { array-id, enum () {  }
 }"></ArgTableRow>
<ArgTableRow arg="station-capabilities" typ="multi { array-id, enum () {  }
 }"></ArgTableRow>
<ArgTableRow arg="mt-station" typ="bool"></ArgTableRow>
<ArgTableRow arg="assoc-capabilities" typ="multi { array-id, enum () {  }
 }"></ArgTableRow>
<ArgTableRow arg="assoc-id" typ="num"></ArgTableRow>
<ArgTableRow arg="assoc-mt-info" typ="multi { array-id, enum (nstreme | doing-wds | without-polling | dynamic-packing-size) { nstreme:0, doing-wds:2, without-polling:3, dynamic-packing-size:4 }
 }"></ArgTableRow>
<ArgTableRow arg="assoc-mt-ap-tx-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="assoc-mt-client-tx-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="assoc-mt-framing-mode" typ="enum (none | best-fit | exact-size)"></ArgTableRow>
<ArgTableRow arg="assoc-mt-framing-limit" typ="num"></ArgTableRow>
</ArgTable>

### interface/wireless/spectral-scan

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="range" typ="alt { range [ .. 7000]
, enum (2.4ghz | 5ghz | current-channel) { 2.4ghz:1, 5ghz:2, current-channel:3 }
 }"></ArgTableRow>
<ArgTableRow arg="show-interference" typ="bool"></ArgTableRow>
<ArgTableRow arg="samples" typ="num"></ArgTableRow>
<ArgTableRow arg="buckets" typ="num"></ArgTableRow>
<ArgTableRow arg="peak-hold-time" typ="time"></ArgTableRow>
<ArgTableRow arg="save-file-name" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="freq" typ="num"></ArgTableRow>
<ArgTableRow arg="interference" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="dbm" typ="num"></ArgTableRow>
<ArgTableRow arg="graph" typ="meter"></ArgTableRow>
</ArgTable>

### interface/wireless/wds

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="R" typ="running"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp)"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { enum (auto) { auto:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="disable-running-check" typ="bool"></ArgTableRow>
<ArgTableRow arg="master-interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="wds-address" typ="macAddr"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
</ArgTable>

#### interface/wireless/wds/monitor

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="active" typ="bool"></ArgTableRow>
</ArgTable>

### interface/wireless/wps-client

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="create-profile" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string"></ArgTableRow>
<ArgTableRow arg="authentication" typ="string"></ArgTableRow>
<ArgTableRow arg="encryption" typ="string"></ArgTableRow>
</ArgTable>

### interface/wireless/wps-push-button

**Package:** wireless-rep
**Type:** Command
