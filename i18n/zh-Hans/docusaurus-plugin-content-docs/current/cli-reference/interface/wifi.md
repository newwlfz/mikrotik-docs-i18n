# Wifi

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/wifi

**软件包:** wireless-qca
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="M" typ="master">主接口</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="N" typ="network">网络</ArgTableRow>
<ArgTableRow arg="B" typ="bound">绑定</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
<ArgTableRow arg="R" typ="running">运行中</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="test.sigmadut-params" typ="string" unset="1" syscap="ww2-sigmadut"></ArgTableRow>
<ArgTableRow arg="test.sigmadut-extra-params" typ="string" unset="1" syscap="ww2-sigmadut"></ArgTableRow>
<ArgTableRow arg="configuration" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="security" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="datapath" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="channel" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="aaa" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="steering" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp)" unset="1"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { enum (auto) { auto:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="disable-running-check" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="radio-mac" typ="macAddr" unset="1"></ArgTableRow>
<ArgTableRow arg="master-interface" typ="iface_enum" unset="1"></ArgTableRow>
<ArgTableRow arg="mld-name" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="mld-interface" typ="iface_enum" unset="1"></ArgTableRow>
<ArgTableRow arg="test.dfs.ignore-radar" typ="bool" unset="1" syscap="dfstest"></ArgTableRow>
<ArgTableRow arg="test.dfs.ignore-cac" typ="bool" unset="1" syscap="dfstest"></ArgTableRow>
<ArgTableRow arg="test.dfs.duty-cycle" typ="bool" unset="1" syscap="dfstest"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (ap)" unset="1"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="hide-ssid" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="max-sta-count" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="multicast-helper" typ="enum (default | disabled | full | dhcp)" unset="1"></ArgTableRow>
<ArgTableRow arg="tx-chains" typ="ubit (0, 1, 2, 3)" unset="1"></ArgTableRow>
<ArgTableRow arg="rx-chains" typ="ubit (0, 1, 2, 3)" unset="1"></ArgTableRow>
<ArgTableRow arg="guard-interval" typ="enum (any | long)" unset="1"></ArgTableRow>
<ArgTableRow arg="country" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="installation" typ="enum (any | indoor | outdoor)" unset="1"></ArgTableRow>
<ArgTableRow arg="load-balancing-group" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="distance" typ="enum (indoors | dynamic)" unset="1"></ArgTableRow>
<ArgTableRow arg="hw-retries" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="hw-protection-mode" typ="enum (none | rts-cts | cts-to-self)" unset="1"></ArgTableRow>
<ArgTableRow arg="frame-lifetime" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="disconnect-timeout" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="keepalive-frames" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (ap | station | station-bridge | station-pseudobridge | meshpoint | invalid)" unset="1"></ArgTableRow>
<ArgTableRow arg="hide-ssid" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="beacon-interval" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="dtim-period" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="multicast-enhance" typ="enum (disabled | enabled)" unset="1"></ArgTableRow>
<ArgTableRow arg="qos-classifier" typ="enum (priority | dscp-high-3-bits)" unset="1"></ArgTableRow>
<ArgTableRow arg="station-roaming" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="max-clients" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="hw-protection-mode" typ="enum (none | rts-cts | cts-to-self)" unset="1"></ArgTableRow>
<ArgTableRow arg="country" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="chains" typ="ubit ()" unset="1"></ArgTableRow>
<ArgTableRow arg="tx-chains" typ="ubit ()" unset="1"></ArgTableRow>
<ArgTableRow arg="tx-power" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="antenna-gain" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="distance" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="installation" typ="enum (outdoor | indoor)" unset="1"></ArgTableRow>
<ArgTableRow arg="encryption" typ="ubit (tkip, ccmp, gcmp, ccmp-256, gcmp-256)" unset="1"></ArgTableRow>
<ArgTableRow arg="group-encryption" typ="enum (tkip | ccmp | gcmp | ccmp-256 | gcmp-256)" unset="1"></ArgTableRow>
<ArgTableRow arg="group-key-update" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="multi-passphrase-group" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="disable-pmkid" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="management-protection" typ="enum (disabled | allowed | required)" unset="1"></ArgTableRow>
<ArgTableRow arg="beacon-protection" typ="enum (disabled | enabled)" unset="1"></ArgTableRow>
<ArgTableRow arg="management-encryption" typ="enum (cmac | gmac | cmac-256 | gmac-256)" unset="1"></ArgTableRow>
<ArgTableRow arg="wps" typ="enum (disable | push-button)" unset="1"></ArgTableRow>
<ArgTableRow arg="dh-groups" typ="ubit (19, 20, 21)" unset="1"></ArgTableRow>
<ArgTableRow arg="sae-anti-clogging-threshold" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="sae-max-failure-rate" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="sae-pwe" typ="enum (hunting-and-pecking | hash-to-element | both)" unset="1"></ArgTableRow>
<ArgTableRow arg="owe-transition-interface" typ="iface_enum { auto:ww2::SECCFG_OWETM_IFACE_AUTO }" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-methods" typ="multi { array-id, enum (tls | ttls | peap) { tls:13, ttls:21, peap:25 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-certificate-mode" typ="enum (verify-certificate | dont-verify-certificate | no-certificates | verify-certificate-with-crl)" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-tls-certificate" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-username" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-anonymous-identity" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-password" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-accounting" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="ft" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="ft-mobility-domain" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ft-over-ds" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="ft-reassociation-deadline" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="ft-nas-identifier" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="ft-r0-key-lifetime" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="ft-preserve-vlanid" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="connect-group" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="connect-priority" typ="super { num
, /num
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="authentication-types" typ="ubit (wpa-psk, wpa2-psk, wpa2-psk-sha2, wpa-eap, wpa2-eap, wpa3-psk, wpa3-psk-gd, owe, wpa3-eap, wpa3-eap-192, dpp)" unset="1"></ArgTableRow>
<ArgTableRow arg="network-type" typ="enum (private | private-with-guest | public-chargeable | public-free | personal-device | emergency-only | test | wildcard)" unset="1"></ArgTableRow>
<ArgTableRow arg="internet" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="esr" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="uesa" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="venue" typ="enum (unspecified | disabled)" unset="1"></ArgTableRow>
<ArgTableRow arg="hessid" typ="macAddr" unset="1"></ArgTableRow>
<ArgTableRow arg="hotspot20" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="hotspot20-dgaf" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="roaming-ois" typ="multi { array-id, string
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="venue-names" typ="object { composite { ,  } { ,  }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="authentication-types" typ="object { composite { ,  } { ,  }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="ipv4-availability" typ="enum (not-available | public | port-restricted | single-nated | double-nated | port-restricted-single-nated | port-restricted-double-nated | unknown)" unset="1"></ArgTableRow>
<ArgTableRow arg="ipv6-availability" typ="enum (not-available | available | unknown)" unset="1"></ArgTableRow>
<ArgTableRow arg="realms" typ="object { composite { ,  } { ,  }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="realms-raw" typ="multi { array-id, string
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="3gpp-info" typ="object { composite { ,  } { ,  }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="3gpp-info-raw" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="domain-names" typ="multi { array-id, string
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="operator-names" typ="object { composite { ,  } { ,  }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="wan-status" typ="enum (reserved | up | down | test)" unset="1"></ArgTableRow>
<ArgTableRow arg="wan-symmetric" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="wan-at-capacity" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="wan-downlink" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="wan-uplink" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="wan-downlink-load" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="wan-uplink-load" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="wan-measurement-duration" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="connection-capabilities" typ="object { composite { ,  } { ,  }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="operational-classes" typ="multi { array-id, num
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum { none:nv::BADID }" unset="1"></ArgTableRow>
<ArgTableRow arg="bridge-cost" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bridge-horizon" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="openflow-switch" typ="enum" unset="1" syscap="openflow"></ArgTableRow>
<ArgTableRow arg="client-isolation" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="traffic-processing" typ="enum (on-cap | on-capsman | on-capsman-secure)" unset="1"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="interface-list" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="frequency" typ="object {  }" unset="1"></ArgTableRow>
<ArgTableRow arg="secondary-frequency" typ="multi { array-id, alt { enum (disabled) { disabled:ww2::CHAN_SECFREQS_DISABLED }
, num
 } { enum (disabled) { disabled:ww2::CHAN_SECFREQS_DISABLED }
, num
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="band" typ="enum ()" unset="1"></ArgTableRow>
<ArgTableRow arg="width" typ="enum ()" unset="1"></ArgTableRow>
<ArgTableRow arg="skip-dfs-channels" typ="enum (disabled | all | 10min-cac)" unset="1"></ArgTableRow>
<ArgTableRow arg="deprioritize-unii-3-4" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="reselect-interval" typ="super { time [1 .. 60*60*24*300]
, ..time [1 .. 60*60*24*300]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="reselect-time" typ="super { date
, ..date
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="preamble-puncturing" typ="alt { enum (yes | no) { yes:-1, no:0 }
,  }" unset="1"></ArgTableRow>
<ArgTableRow arg="afc" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="username-format" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="password-format" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="called-format" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="calling-format" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="mac-caching" typ="alt { enum (disabled) { disabled:0 }
, time
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="interim-update" typ="alt { enum (disabled) { disabled:0 }
, time [1 .. ]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="nas-identifier" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="neighbor-group" typ="multi { array-id, string
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="rrm" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="wnm" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="2g-probe-delay" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="transition-threshold" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="transition-threshold-time" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="transition-request-period" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="transition-request-count" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="transition-time" typ="alt { enum (unlimited | immediate) { unlimited:-1, immediate:0 }
, time
 }" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="default-name" typ="string"></ArgTableRow>
<ArgTableRow arg="cap" typ="string"></ArgTableRow>
</ArgTable>

### interface/wifi/flat-snoop

**类型:** 命令

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="M" typ="mikrotik-oui"></ArgTableRow>
<ArgTableRow arg="L" typ="locally-administered-address"></ArgTableRow>
<ArgTableRow arg="B" typ="multicast-address"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="filter-type" typ="ubit (frequency, bsss, stas)" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="num" typ="num"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (freq | bss | sta)"></ArgTableRow>
<ArgTableRow arg="address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="bss-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="frequency" typ="num"></ArgTableRow>
<ArgTableRow arg="beacon-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="rate-mbps" typ="string"></ArgTableRow>
<ArgTableRow arg="basic-rates-mbps" typ="string"></ArgTableRow>
<ArgTableRow arg="supported-rates-mbps" typ="string"></ArgTableRow>
<ArgTableRow arg="signal" typ="num"></ArgTableRow>
<ArgTableRow arg="snr" typ="num"></ArgTableRow>
<ArgTableRow arg="noise" typ="num"></ArgTableRow>
<ArgTableRow arg="seen-frame-count" typ="num"></ArgTableRow>
<ArgTableRow arg="beacon-size" typ="num"></ArgTableRow>
<ArgTableRow arg="first-beacon" typ="date"></ArgTableRow>
<ArgTableRow arg="last-seen" typ="time"></ArgTableRow>
<ArgTableRow arg="country" typ="string"></ArgTableRow>
<ArgTableRow arg="erp-info" typ="ubit (non-erp-present, use-protection, barker-preamble-mode)"></ArgTableRow>
<ArgTableRow arg="rsn-capab" typ="ubit ()"></ArgTableRow>
<ArgTableRow arg="group-data-cipher" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="group-mgmt-cipher" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="pairwise-ciphers" typ="multi { array-id, enum () {  }
 }"></ArgTableRow>
<ArgTableRow arg="rsn-akms" typ="multi { array-id, enum (802.1x | psk | ft-802.1x | ft-psk | 802.1x-256 | psk-sha256 | tdls | sae | sae | ft-sae | ft-sae | ap-peerkey | 802.1x-b-256 | 802.1x-b-192 | ft-802.1x-sha384 | fils-sha256 | fils-sha384 | ft-fils-sha256 | ft-fils-sha384 | owe | ft-psk-sha384 | psk-sha384) { 802.1x:0xfac01, psk:0xfac02, ft-802.1x:0xfac03, ft-psk:0xfac04, 802.1x-256:0xfac05, psk-sha256:0xfac06, tdls:0xfac07, sae:0xfac08, sae:0xfac18, ft-sae:0xfac09, ft-sae:0xfac19, ap-peerkey:0xfac0a, 802.1x-b-256:0xfac0b, 802.1x-b-192:0xfac0c, ft-802.1x-sha384:0xfac0d, fils-sha256:0xfac0e, fils-sha384:0xfac0f, ft-fils-sha256:0xfac10, ft-fils-sha384:0xfac11, owe:0xfac12, ft-psk-sha384:0xfac13, psk-sha384:0xfac14 }
 }"></ArgTableRow>
<ArgTableRow arg="pmkids" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="rsn" typ="string"></ArgTableRow>
<ArgTableRow arg="bss-on-time" typ="time"></ArgTableRow>
<ArgTableRow arg="sta-count" typ="num"></ArgTableRow>
<ArgTableRow arg="bss-count" typ="num"></ArgTableRow>
</ArgTable>

### interface/wifi/aaa

**软件包:** wireless-qca
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="username-format" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="password-format" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="called-format" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="calling-format" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="mac-caching" typ="alt { enum (disabled) { disabled:0 }
, time
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="interim-update" typ="alt { enum (disabled) { disabled:0 }
, time [1 .. ]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="nas-identifier" typ="string" unset="1"></ArgTableRow>
</ArgTable>

### interface/wifi/access-list

**软件包:** wireless-qca
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="mac-address" typ="macAddr" unset="1"></ArgTableRow>
<ArgTableRow arg="mac-address-mask" typ="macAddr" unset="1"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum { , any:0 }" unset="1"></ArgTableRow>
<ArgTableRow arg="signal-range" typ="composite { ,  }" unset="1"></ArgTableRow>
<ArgTableRow arg="allow-signal-out-of-range" typ="alt { enum (always) { always:0 }
, time
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="ssid-regexp" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="time" typ="super { time [0 .. 86400]
, -time [0 .. 86400]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="days" typ="ubit (sun, mon, tue, wed, thu, fri, sat)" unset="1"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (accept | reject | query-radius)" unset="1"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="multi-passphrase-group" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="radius-accounting" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="client-isolation" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="last-logged-in" typ="date" unset="1"></ArgTableRow>
<ArgTableRow arg="last-logged-out" typ="date" unset="1"></ArgTableRow>
<ArgTableRow arg="match-count" typ="num" unset="1"></ArgTableRow>
</ArgTable>

### interface/wifi/cap

**软件包:** wireless-qca
**类型:** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="discovery-interfaces" typ="multi { array-id, iface_enum { ,  } { ,  }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (request | none)" unset="1"></ArgTableRow>
<ArgTableRow arg="caps-man-addresses" typ="multi { array-id, address (flags=46iD)
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="caps-man-names" typ="multi { array-id, string
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="caps-man-certificate-common-names" typ="multi { array-id, string
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="lock-to-caps-man" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="slaves-static" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="mld-static" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="slaves-datapath" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="mld-datapath" typ="enum" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="requested-certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="locked-caps-man-common-name" typ="string"></ArgTableRow>
<ArgTableRow arg="current-caps-man-address" typ="address (flags=46mi)"></ArgTableRow>
<ArgTableRow arg="current-caps-man-identity" typ="string"></ArgTableRow>
</ArgTable>

### interface/wifi/capsman

**软件包:** wireless-qca
**类型:** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="interfaces" typ="multi { array-id, iface_enum { ,  } { ,  }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="ca-certificate" typ="enum (auto | none)" unset="1"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (auto)" unset="1"></ArgTableRow>
<ArgTableRow arg="require-peer-certificate" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="package-path" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="upgrade-policy" typ="enum (none | suggest-same-version | require-same-version)" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="generated-ca-certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="generated-certificate" typ="enum (none)"></ArgTableRow>
</ArgTable>

#### interface/wifi/capsman/remote-cap

**软件包:** wireless-qca
**类型:** 目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="address" typ="address (flags=46mi)"></ArgTableRow>
<ArgTableRow arg="identity" typ="string"></ArgTableRow>
<ArgTableRow arg="board-name" typ="string"></ArgTableRow>
<ArgTableRow arg="serial" typ="string"></ArgTableRow>
<ArgTableRow arg="version" typ="string"></ArgTableRow>
<ArgTableRow arg="base-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="common-name" typ="string"></ArgTableRow>
<ArgTableRow arg="state" typ="string"></ArgTableRow>
<ArgTableRow arg="connected-time" typ="time"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
</ArgTable>

##### interface/wifi/capsman/remote-cap/provision

**软件包:** wireless-qca
**类型:** 命令

##### interface/wifi/capsman/remote-cap/set-identity

**软件包:** wireless-qca
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
</ArgTable>

##### interface/wifi/capsman/remote-cap/upgrade

**软件包:** wireless-qca
**类型:** 命令

### interface/wifi/channel

**软件包:** wireless-qca
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="frequency" typ="object {  }" unset="1"></ArgTableRow>
<ArgTableRow arg="secondary-frequency" typ="multi { array-id, alt { enum (disabled) { disabled:ww2::CHAN_SECFREQS_DISABLED }
, num
 } { enum (disabled) { disabled:ww2::CHAN_SECFREQS_DISABLED }
, num
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="band" typ="enum ()" unset="1"></ArgTableRow>
<ArgTableRow arg="width" typ="enum ()" unset="1"></ArgTableRow>
<ArgTableRow arg="skip-dfs-channels" typ="enum (disabled | all | 10min-cac)" unset="1"></ArgTableRow>
<ArgTableRow arg="deprioritize-unii-3-4" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="reselect-interval" typ="super { time [1 .. 60*60*24*300]
, ..time [1 .. 60*60*24*300]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="reselect-time" typ="super { date
, ..date
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="preamble-puncturing" typ="alt { enum (yes | no)