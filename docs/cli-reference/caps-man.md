# Caps Man

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## caps-man/aaa

**Package:** wireless-rep
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="mac-format" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-mode" typ="enum (as-username | as-username-and-password)"></ArgTableRow>
<ArgTableRow arg="mac-caching" typ="alt { enum (disabled) { disabled:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="interim-update" typ="alt { enum (disabled) { disabled:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="called-format" typ="enum (mac:ssid | mac | ssid)"></ArgTableRow>
</ArgTable>

### caps-man/acl/access-list

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
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
, ,ubit (sun, mon, tue, wed, thu, fri, sat) { sun, mon, tue, wed, thu, fri, sat }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (accept | reject | query-radius)" unset="1"></ArgTableRow>
<ArgTableRow arg="ap-tx-limit" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="client-tx-limit" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="private-passphrase" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="radius-accounting" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="client-to-client-forwarding" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="vlan-mode" typ="enum (no-tag | use-tag | use-service-tag)" unset="1"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" unset="1"></ArgTableRow>
</ArgTable>

### caps-man/cfg/configuration

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="security" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="datapath" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="channel" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="rates" typ="enum" unset="1"></ArgTableRow>
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
<ArgTableRow arg="authentication-types" typ="ubit (wpa-psk, wpa2-psk, wpa-eap, wpa2-eap)" unset="1"></ArgTableRow>
<ArgTableRow arg="encryption" typ="ubit (aes-ccm, tkip)" unset="1"></ArgTableRow>
<ArgTableRow arg="group-encryption" typ="enum (aes-ccm | tkip)" unset="1"></ArgTableRow>
<ArgTableRow arg="group-key-update" typ="time"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-methods" typ="multi { array-id, enum (eap-tls | passthrough) { eap-tls:13, passthrough:0xffffffff }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-radius-accounting" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="tls-mode" typ="enum (verify-certificate | dont-verify-certificate | no-certificates | verify-certificate-with-crl)"></ArgTableRow>
<ArgTableRow arg="tls-certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="disable-pmkid" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp)"></ArgTableRow>
<ArgTableRow arg="client-to-client-forwarding" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum" unset="1"></ArgTableRow>
<ArgTableRow arg="bridge-cost" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bridge-horizon" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="openflow-switch" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="local-forwarding" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="vlan-mode" typ="enum (no-tag | use-tag | use-service-tag)" unset="1"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="interface-list" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="frequency" typ="multi { array-id, num
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="secondary-frequency" typ="multi { array-id, alt { enum (disabled) { disabled:wlc::CHANCFG_SECFREQS_DISABLED }
, num
 } { enum (disabled) { disabled:wlc::CHANCFG_SECFREQS_DISABLED }
, num
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="control-channel-width" typ="enum (5mhz | 10mhz | 20mhz | 40mhz-turbo)" unset="1"></ArgTableRow>
<ArgTableRow arg="band" typ="enum (2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac)" unset="1"></ArgTableRow>
<ArgTableRow arg="extension-channel" typ="enum (disabled | Ce | eC | Ceee | eCee | eeCe | eeeC | XX | XXXX | Ceeeeeee | eCeeeeee | eeCeeeee | eeeCeeee | eeeeCeee | eeeeeCee | eeeeeeCe | eeeeeeeC | XXXXXXXX)" unset="1"></ArgTableRow>
<ArgTableRow arg="tx-power" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="save-selected" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="reselect-interval" typ="super { time [1 .. 60*60*24*300]
, ..time [1 .. 60*60*24*300]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="skip-dfs-channels" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="basic" typ="ubit (1Mbps, 2Mbps, 5.5Mbps, 11Mbps, 6Mbps, 9Mbps, 12Mbps, 18Mbps, 24Mbps, 36Mbps, 48Mbps, 54Mbps)" unset="1"></ArgTableRow>
<ArgTableRow arg="supported" typ="ubit (1Mbps, 2Mbps, 5.5Mbps, 11Mbps, 6Mbps, 9Mbps, 12Mbps, 18Mbps, 24Mbps, 36Mbps, 48Mbps, 54Mbps)" unset="1"></ArgTableRow>
<ArgTableRow arg="ht-basic-mcs" typ="ubit (mcs-0, mcs-1, mcs-2, mcs-3, mcs-4, mcs-5, mcs-6, mcs-7, mcs-8, mcs-9, mcs-10, mcs-11, mcs-12, mcs-13, mcs-14, mcs-15, mcs-16, mcs-17, mcs-18, mcs-19, mcs-20, mcs-21, mcs-22, mcs-23)" unset="1"></ArgTableRow>
<ArgTableRow arg="ht-supported-mcs" typ="ubit (mcs-0, mcs-1, mcs-2, mcs-3, mcs-4, mcs-5, mcs-6, mcs-7, mcs-8, mcs-9, mcs-10, mcs-11, mcs-12, mcs-13, mcs-14, mcs-15, mcs-16, mcs-17, mcs-18, mcs-19, mcs-20, mcs-21, mcs-22, mcs-23)" unset="1"></ArgTableRow>
<ArgTableRow arg="vht-basic-mcs" typ="multi { array-id, enum (none | mcs0-7 | mcs0-8 | mcs0-9) { none:0, mcs0-7:1, mcs0-8:2, mcs0-9:3 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="vht-supported-mcs" typ="multi { array-id, enum (none | mcs0-7 | mcs0-8 | mcs0-9) { none:0, mcs0-7:1, mcs0-8:2, mcs0-9:3 }
 }" unset="1"></ArgTableRow>
</ArgTable>

### caps-man/chancfg/channel

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="frequency" typ="multi { array-id, num
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="secondary-frequency" typ="multi { array-id, alt { enum (disabled) { disabled:wlc::CHANCFG_SECFREQS_DISABLED }
, num
 } { enum (disabled) { disabled:wlc::CHANCFG_SECFREQS_DISABLED }
, num
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="control-channel-width" typ="enum (5mhz | 10mhz | 20mhz | 40mhz-turbo)" unset="1"></ArgTableRow>
<ArgTableRow arg="band" typ="enum (2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac)" unset="1"></ArgTableRow>
<ArgTableRow arg="extension-channel" typ="enum (disabled | Ce | eC | Ceee | eCee | eeCe | eeeC | XX | XXXX | Ceeeeeee | eCeeeeee | eeCeeeee | eeeCeeee | eeeeCeee | eeeeeCee | eeeeeeCe | eeeeeeeC | XXXXXXXX)" unset="1"></ArgTableRow>
<ArgTableRow arg="tx-power" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="save-selected" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="reselect-interval" typ="super { time [1 .. 60*60*24*300]
, ..time [1 .. 60*60*24*300]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="skip-dfs-channels" typ="bool" unset="1"></ArgTableRow>
</ArgTable>

### caps-man/controller/manager

**Package:** wireless-rep
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none | auto)"></ArgTableRow>
<ArgTableRow arg="ca-certificate" typ="enum (none | auto)"></ArgTableRow>
<ArgTableRow arg="package-path" typ="string"></ArgTableRow>
<ArgTableRow arg="upgrade-policy" typ="enum (none | suggest-same-version | require-same-version)"></ArgTableRow>
<ArgTableRow arg="require-peer-certificate" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="generated-certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="generated-ca-certificate" typ="enum (none)"></ArgTableRow>
</ArgTable>

#### caps-man/controller/manager/interface

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum { all:nv::BADID }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="forbid" typ="bool"></ArgTableRow>
</ArgTable>

### caps-man/dpathcfg/datapath

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp)"></ArgTableRow>
<ArgTableRow arg="client-to-client-forwarding" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum" unset="1"></ArgTableRow>
<ArgTableRow arg="bridge-cost" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bridge-horizon" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="openflow-switch" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="local-forwarding" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="vlan-mode" typ="enum (no-tag | use-tag | use-service-tag)" unset="1"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="interface-list" typ="enum" unset="1"></ArgTableRow>
</ArgTable>

### caps-man/ifaceactual/actual-interface-configuration

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="M" typ="master"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="B" typ="bound"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="R" typ="running"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { enum (auto) { auto:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="disable-running-check" typ="bool"></ArgTableRow>
<ArgTableRow arg="radio-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="master-interface" typ="iface_enum { none:nv::BADID }"></ArgTableRow>
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
<ArgTableRow arg="authentication-types" typ="ubit (wpa-psk, wpa2-psk, wpa-eap, wpa2-eap)" unset="1"></ArgTableRow>
<ArgTableRow arg="encryption" typ="ubit (aes-ccm, tkip)" unset="1"></ArgTableRow>
<ArgTableRow arg="group-encryption" typ="enum (aes-ccm | tkip)" unset="1"></ArgTableRow>
<ArgTableRow arg="group-key-update" typ="time"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-methods" typ="multi { array-id, enum (eap-tls | passthrough) { eap-tls:13, passthrough:0xffffffff }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-radius-accounting" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="tls-mode" typ="enum (verify-certificate | dont-verify-certificate | no-certificates | verify-certificate-with-crl)"></ArgTableRow>
<ArgTableRow arg="tls-certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="disable-pmkid" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp)"></ArgTableRow>
<ArgTableRow arg="client-to-client-forwarding" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum" unset="1"></ArgTableRow>
<ArgTableRow arg="bridge-cost" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bridge-horizon" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="openflow-switch" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="local-forwarding" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="vlan-mode" typ="enum (no-tag | use-tag | use-service-tag)" unset="1"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="interface-list" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="frequency" typ="multi { array-id, num
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="secondary-frequency" typ="multi { array-id, alt { enum (disabled) { disabled:wlc::CHANCFG_SECFREQS_DISABLED }
, num
 } { enum (disabled) { disabled:wlc::CHANCFG_SECFREQS_DISABLED }
, num
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="control-channel-width" typ="enum (5mhz | 10mhz | 20mhz | 40mhz-turbo)" unset="1"></ArgTableRow>
<ArgTableRow arg="band" typ="enum (2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac)" unset="1"></ArgTableRow>
<ArgTableRow arg="extension-channel" typ="enum (disabled | Ce | eC | Ceee | eCee | eeCe | eeeC | XX | XXXX | Ceeeeeee | eCeeeeee | eeCeeeee | eeeCeeee | eeeeCeee | eeeeeCee | eeeeeeCe | eeeeeeeC | XXXXXXXX)" unset="1"></ArgTableRow>
<ArgTableRow arg="tx-power" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="save-selected" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="reselect-interval" typ="super { time [1 .. 60*60*24*300]
, ..time [1 .. 60*60*24*300]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="skip-dfs-channels" typ="bool" unset="1"></ArgTableRow>
</ArgTable>

## caps-man/interface

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="M" typ="master"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="B" typ="bound"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="R" typ="running"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { enum (auto) { auto:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="disable-running-check" typ="bool"></ArgTableRow>
<ArgTableRow arg="radio-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="master-interface" typ="iface_enum { none:nv::BADID }"></ArgTableRow>
<ArgTableRow arg="radio-name" typ="string"></ArgTableRow>
<ArgTableRow arg="configuration" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="security" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="datapath" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="channel" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="rates" typ="enum" unset="1"></ArgTableRow>
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
<ArgTableRow arg="authentication-types" typ="ubit (wpa-psk, wpa2-psk, wpa-eap, wpa2-eap)" unset="1"></ArgTableRow>
<ArgTableRow arg="encryption" typ="ubit (aes-ccm, tkip)" unset="1"></ArgTableRow>
<ArgTableRow arg="group-encryption" typ="enum (aes-ccm | tkip)" unset="1"></ArgTableRow>
<ArgTableRow arg="group-key-update" typ="time"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-methods" typ="multi { array-id, enum (eap-tls | passthrough) { eap-tls:13, passthrough:0xffffffff }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-radius-accounting" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="tls-mode" typ="enum (verify-certificate | dont-verify-certificate | no-certificates | verify-certificate-with-crl)"></ArgTableRow>
<ArgTableRow arg="tls-certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="disable-pmkid" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp)"></ArgTableRow>
<ArgTableRow arg="client-to-client-forwarding" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum" unset="1"></ArgTableRow>
<ArgTableRow arg="bridge-cost" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bridge-horizon" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="openflow-switch" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="local-forwarding" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="vlan-mode" typ="enum (no-tag | use-tag | use-service-tag)" unset="1"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="interface-list" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="frequency" typ="multi { array-id, num
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="secondary-frequency" typ="multi { array-id, alt { enum (disabled) { disabled:wlc::CHANCFG_SECFREQS_DISABLED }
, num
 } { enum (disabled) { disabled:wlc::CHANCFG_SECFREQS_DISABLED }
, num
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="control-channel-width" typ="enum (5mhz | 10mhz | 20mhz | 40mhz-turbo)" unset="1"></ArgTableRow>
<ArgTableRow arg="band" typ="enum (2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac)" unset="1"></ArgTableRow>
<ArgTableRow arg="extension-channel" typ="enum (disabled | Ce | eC | Ceee | eCee | eeCe | eeeC | XX | XXXX | Ceeeeeee | eCeeeeee | eeCeeeee | eeeCeeee | eeeeCeee | eeeeeCee | eeeeeeCe | eeeeeeeC | XXXXXXXX)" unset="1"></ArgTableRow>
<ArgTableRow arg="tx-power" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="save-selected" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="reselect-interval" typ="super { time [1 .. 60*60*24*300]
, ..time [1 .. 60*60*24*300]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="skip-dfs-channels" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="basic" typ="ubit (1Mbps, 2Mbps, 5.5Mbps, 11Mbps, 6Mbps, 9Mbps, 12Mbps, 18Mbps, 24Mbps, 36Mbps, 48Mbps, 54Mbps)" unset="1"></ArgTableRow>
<ArgTableRow arg="supported" typ="ubit (1Mbps, 2Mbps, 5.5Mbps, 11Mbps, 6Mbps, 9Mbps, 12Mbps, 18Mbps, 24Mbps, 36Mbps, 48Mbps, 54Mbps)" unset="1"></ArgTableRow>
<ArgTableRow arg="ht-basic-mcs" typ="ubit (mcs-0, mcs-1, mcs-2, mcs-3, mcs-4, mcs-5, mcs-6, mcs-7, mcs-8, mcs-9, mcs-10, mcs-11, mcs-12, mcs-13, mcs-14, mcs-15, mcs-16, mcs-17, mcs-18, mcs-19, mcs-20, mcs-21, mcs-22, mcs-23)" unset="1"></ArgTableRow>
<ArgTableRow arg="ht-supported-mcs" typ="ubit (mcs-0, mcs-1, mcs-2, mcs-3, mcs-4, mcs-5, mcs-6, mcs-7, mcs-8, mcs-9, mcs-10, mcs-11, mcs-12, mcs-13, mcs-14, mcs-15, mcs-16, mcs-17, mcs-18, mcs-19, mcs-20, mcs-21, mcs-22, mcs-23)" unset="1"></ArgTableRow>
<ArgTableRow arg="vht-basic-mcs" typ="multi { array-id, enum (none | mcs0-7 | mcs0-8 | mcs0-9) { none:0, mcs0-7:1, mcs0-8:2, mcs0-9:3 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="vht-supported-mcs" typ="multi { array-id, enum (none | mcs0-7 | mcs0-8 | mcs0-9) { none:0, mcs0-7:1, mcs0-8:2, mcs0-9:3 }
 }" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="current-state" typ="string"></ArgTableRow>
<ArgTableRow arg="current-channel" typ="string"></ArgTableRow>
<ArgTableRow arg="current-rate-set" typ="string"></ArgTableRow>
<ArgTableRow arg="current-basic-rate-set" typ="string"></ArgTableRow>
<ArgTableRow arg="current-registered-clients" typ="num"></ArgTableRow>
<ArgTableRow arg="current-authorized-clients" typ="num"></ArgTableRow>
</ArgTable>

### caps-man/interface/hw-info

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
<ArgTableRow arg="antenna-gain" typ="num"></ArgTableRow>
<ArgTableRow arg="locked-countries" typ="multi { array-id, enum
 }"></ArgTableRow>
</ArgTable>

### caps-man/interface/possible-channels

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="channels" typ="multi { array-id, string
 }"></ArgTableRow>
</ArgTable>

### caps-man/interface/reselect-channel

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
</ArgTable>

### caps-man/interface/scan

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
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="save-file" typ="string"></ArgTableRow>
<ArgTableRow arg="rounds" typ="num"></ArgTableRow>
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

## caps-man/radio

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="L" typ="local"></ArgTableRow>
<ArgTableRow arg="P" typ="provisioned"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="radio-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="remote-cap-name" typ="string"></ArgTableRow>
<ArgTableRow arg="remote-cap-identity" typ="string"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
</ArgTable>

### caps-man/radio/hw-info

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="ranges" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="tx-chains" typ="ubit (0, 1, 2, 3)"></ArgTableRow>
<ArgTableRow arg="rx-chains" typ="ubit (0, 1, 2, 3)"></ArgTableRow>
<ArgTableRow arg="antenna-gain" typ="num"></ArgTableRow>
<ArgTableRow arg="locked-countries" typ="multi { array-id, enum
 }"></ArgTableRow>
</ArgTable>

### caps-man/radio/provision

**Package:** wireless-rep
**Type:** Command

### caps-man/ratescfg/rates

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="basic" typ="ubit (1Mbps, 2Mbps, 5.5Mbps, 11Mbps, 6Mbps, 9Mbps, 12Mbps, 18Mbps, 24Mbps, 36Mbps, 48Mbps, 54Mbps)" unset="1"></ArgTableRow>
<ArgTableRow arg="supported" typ="ubit (1Mbps, 2Mbps, 5.5Mbps, 11Mbps, 6Mbps, 9Mbps, 12Mbps, 18Mbps, 24Mbps, 36Mbps, 48Mbps, 54Mbps)" unset="1"></ArgTableRow>
<ArgTableRow arg="ht-basic-mcs" typ="ubit (mcs-0, mcs-1, mcs-2, mcs-3, mcs-4, mcs-5, mcs-6, mcs-7, mcs-8, mcs-9, mcs-10, mcs-11, mcs-12, mcs-13, mcs-14, mcs-15, mcs-16, mcs-17, mcs-18, mcs-19, mcs-20, mcs-21, mcs-22, mcs-23)" unset="1"></ArgTableRow>
<ArgTableRow arg="ht-supported-mcs" typ="ubit (mcs-0, mcs-1, mcs-2, mcs-3, mcs-4, mcs-5, mcs-6, mcs-7, mcs-8, mcs-9, mcs-10, mcs-11, mcs-12, mcs-13, mcs-14, mcs-15, mcs-16, mcs-17, mcs-18, mcs-19, mcs-20, mcs-21, mcs-22, mcs-23)" unset="1"></ArgTableRow>
<ArgTableRow arg="vht-basic-mcs" typ="multi { array-id, enum (none | mcs0-7 | mcs0-8 | mcs0-9) { none:0, mcs0-7:1, mcs0-8:2, mcs0-9:3 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="vht-supported-mcs" typ="multi { array-id, enum (none | mcs0-7 | mcs0-8 | mcs0-9) { none:0, mcs0-7:1, mcs0-8:2, mcs0-9:3 }
 }" unset="1"></ArgTableRow>
</ArgTable>

### caps-man/remoteap/remote-cap

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="state" typ="string"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="radios" typ="num"></ArgTableRow>
<ArgTableRow arg="address" typ="super { alt { ip6Addr
, macAddr
 } { ip6Addr
, macAddr
 }
, /num
 }"></ArgTableRow>
<ArgTableRow arg="board" typ="string"></ArgTableRow>
<ArgTableRow arg="serial" typ="string"></ArgTableRow>
<ArgTableRow arg="base-mac" typ="string"></ArgTableRow>
<ArgTableRow arg="version" typ="string"></ArgTableRow>
<ArgTableRow arg="identity" typ="string"></ArgTableRow>
</ArgTable>

#### caps-man/remoteap/remote-cap/provision

**Package:** wireless-rep
**Type:** Command

#### caps-man/remoteap/remote-cap/set-identity

**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="identity" typ="string"></ArgTableRow>
</ArgTable>

#### caps-man/remoteap/remote-cap/upgrade

**Package:** wireless-rep
**Type:** Command

### caps-man/rule/provisioning

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="radio-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="hw-supported-modes" typ="multi { array-id, enum (a | a-turbo | an | ac | b | g | g-turbo | gn) { a:1, a-turbo:2, an:3, ac:5, b:0x11, g:0x12, g-turbo:0x13, gn:0x14 }
 }"></ArgTableRow>
<ArgTableRow arg="identity-regexp" typ="string"></ArgTableRow>
<ArgTableRow arg="common-name-regexp" typ="string"></ArgTableRow>
<ArgTableRow arg="ip-address-ranges" typ="multi { , , ipRange
 }"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (none | create-enabled | create-disabled | create-dynamic-enabled)"></ArgTableRow>
<ArgTableRow arg="master-configuration" typ="enum"></ArgTableRow>
<ArgTableRow arg="slave-configurations" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="name-format" typ="enum (cap | prefix | identity | prefix-identity)"></ArgTableRow>
<ArgTableRow arg="name-prefix" typ="string"></ArgTableRow>
</ArgTable>

### caps-man/seccfg/security

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="authentication-types" typ="ubit (wpa-psk, wpa2-psk, wpa-eap, wpa2-eap)" unset="1"></ArgTableRow>
<ArgTableRow arg="encryption" typ="ubit (aes-ccm, tkip)" unset="1"></ArgTableRow>
<ArgTableRow arg="group-encryption" typ="enum (aes-ccm | tkip)" unset="1"></ArgTableRow>
<ArgTableRow arg="group-key-update" typ="time"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-methods" typ="multi { array-id, enum (eap-tls | passthrough) { eap-tls:13, passthrough:0xffffffff }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-radius-accounting" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="tls-mode" typ="enum (verify-certificate | dont-verify-certificate | no-certificates | verify-certificate-with-crl)"></ArgTableRow>
<ArgTableRow arg="tls-certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="disable-pmkid" typ="bool" unset="1"></ArgTableRow>
</ArgTable>

### caps-man/sta/registration-table

**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="radio-name" typ="string"></ArgTableRow>
<ArgTableRow arg="tx-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="rx-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="tx-signal" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-signal" typ="num"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="packets" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="bytes" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="tx-rate-set" typ="string"></ArgTableRow>
<ArgTableRow arg="eap-identity" typ="string"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="last-ip" typ="ipAddr"></ArgTableRow>
</ArgTable>
