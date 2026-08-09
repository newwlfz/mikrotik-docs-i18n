# Dhcp Server

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/dhcp-server

**Package:** dhcp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="relay" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="lease-time" typ="time"></ArgTableRow>
<ArgTableRow arg="address-pool" typ="enum (static-only)"></ArgTableRow>
<ArgTableRow arg="dynamic-lease-identifiers" typ="ubit (client-mac, client-id, opt-82)"></ArgTableRow>
<ArgTableRow arg="bootp-support" typ="enum (none | static | dynamic)"></ArgTableRow>
<ArgTableRow arg="bootp-lease-time" typ="alt { , enum (lease-time | forever) { lease-time:0, forever:0xffffffff }
, time
 }"></ArgTableRow>
<ArgTableRow arg="delay-threshold" typ="alt { enum (none) { none:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="server-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="add-arp" typ="bool"></ArgTableRow>
<ArgTableRow arg="add-dns-entries" typ="bool"></ArgTableRow>
<ArgTableRow arg="add-dns-entries-suffix" typ="string">Used only if add-dns-entries=yes. If non-empty, appends suffix to DNS entry and adds Option 15 (Domain Name) to responses.</ArgTableRow>
<ArgTableRow arg="authoritative" typ="enum (no | after-10sec-delay | after-2sec-delay | yes)"></ArgTableRow>
<ArgTableRow arg="always-broadcast" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-radius" typ="enum (no | yes | accounting)"></ArgTableRow>
<ArgTableRow arg="client-mac-limit" typ="enum (unlimited)">maximum leases one client MAC can get</ArgTableRow>
<ArgTableRow arg="conflict-detection" typ="bool">use ARP and ICMP to test for IP conflict before issuing lease</ArgTableRow>
<ArgTableRow arg="use-framed-as-classless" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-reconfigure" typ="bool"></ArgTableRow>
<ArgTableRow arg="lease-script" typ="alt { , string
 }"></ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (first | bottom)"></ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="dhcp-option-set" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="address-lists" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="allow-dual-stack-queue" typ="bool"></ArgTableRow>
<ArgTableRow arg="support-broadband-tr101" typ="bool">Pass additional Option 82 Suboptions to RADIUS server as described in RFC 4679 and The Broadband Forum TR-101</ArgTableRow>
</ArgTable>

### ip/dhcp-server/alert

**Package:** dhcp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="valid-server" typ="multi { macAddr
 }"></ArgTableRow>
<ArgTableRow arg="on-alert" typ="alt { , string
 }"></ArgTableRow>
<ArgTableRow arg="alert-timeout" typ="alt { enum (none) { none:0 }
, time
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="unknown-server" typ="multi { macAddr
 }"></ArgTableRow>
</ArgTable>

#### ip/dhcp-server/alert/reset-alert

**Package:** dhcp
**Type:** Command

### ip/dhcp-server/config

**Package:** dhcp
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="store-leases-disk" typ="alt { enum (immediately | never) { immediately:0, never:0xffffffff }
, time
 }"></ArgTableRow>
<ArgTableRow arg="accounting" typ="bool"></ArgTableRow>
<ArgTableRow arg="interim-update" typ="time"></ArgTableRow>
<ArgTableRow arg="radius-password" typ="alt { bool
, string
 }"></ArgTableRow>
</ArgTable>

### ip/dhcp-server/lease

**Package:** dhcp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="R" typ="radius">radius</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="B" typ="blocked">blocked</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="alt { ipAddr
, enum
 }"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="use-src-mac" typ="bool"></ArgTableRow>
<ArgTableRow arg="client-id" typ="string"></ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string"></ArgTableRow>
<ArgTableRow arg="routes" typ="object { composite { ,  } { ,  }
 }">Routes that appear on the server when the client is connected</ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (bottom | first)"></ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="queue-type" typ="enum"></ArgTableRow>
<ArgTableRow arg="address-lists" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="server" typ="enum (all)"></ArgTableRow>
<ArgTableRow arg="block-access" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow-dual-stack-queue" typ="bool"></ArgTableRow>
<ArgTableRow arg="lease-time" typ="time"></ArgTableRow>
<ArgTableRow arg="always-broadcast" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcp-option" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="dhcp-option-set" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="agent-circuit-id" typ="string">If non-empty, use it to match lease by Option 82 even if MAC or client-id differ</ArgTableRow>
<ArgTableRow arg="agent-remote-id" typ="string">If non-empty, use it to match lease by Option 82 even if MAC or client-id differ</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="enum (waiting | testing | declined | offered | bound | authorizing | conflict)"></ArgTableRow>
<ArgTableRow arg="expires-after" typ="time"></ArgTableRow>
<ArgTableRow arg="last-seen" typ="alt { enum (never | sometime) { never:0xffffffff, sometime:0xfffffffe }
, time
 }"></ArgTableRow>
<ArgTableRow arg="age" typ="time"></ArgTableRow>
<ArgTableRow arg="active-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="active-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="active-client-id" typ="string"></ArgTableRow>
<ArgTableRow arg="active-server" typ="enum"></ArgTableRow>
<ArgTableRow arg="active-agent-circuit-id" typ="string"></ArgTableRow>
<ArgTableRow arg="active-agent-remote-id" typ="string"></ArgTableRow>
<ArgTableRow arg="host-name" typ="string"></ArgTableRow>
<ArgTableRow arg="class-id" typ="string">DHCP option 60 from last received DHCP request</ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="reconfigure-key" typ="string"></ArgTableRow>
<ArgTableRow arg="reconfigure-last-sent" typ="string"></ArgTableRow>
<ArgTableRow arg="reconfigure-status" typ="string"></ArgTableRow>
</ArgTable>

#### ip/dhcp-server/lease/check-status

**Package:** dhcp
**Type:** Command

#### ip/dhcp-server/lease/make-static

**Package:** dhcp
**Type:** Command

#### ip/dhcp-server/lease/send-reconfigure

**Package:** dhcp
**Type:** Command

### ip/dhcp-server/matcher

**Package:** dhcp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="server" typ="enum (all)" mandatory="1">global or single server</ArgTableRow>
<ArgTableRow arg="address-pool" typ="enum (static-only)">pool used for this entry</ArgTableRow>
<ArgTableRow arg="option-set" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="code" typ="alt { num [1 .. 254]
, enum (vendor-specific) { vendor-specific:43 }
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="value" typ="string" mandatory="1">contents of option to match as string or hex with 0x prefix</ArgTableRow>
<ArgTableRow arg="matching-type" typ="enum (exact | substring)" mandatory="1"></ArgTableRow>
</ArgTable>

### ip/dhcp-server/network

**Package:** dhcp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="gateway" typ="multi { ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="netmask" typ="num"></ArgTableRow>
<ArgTableRow arg="dns-server" typ="alt { , multi { ipAddr
 } { ipAddr
 }
 }"></ArgTableRow>
<ArgTableRow arg="dns-none" typ="bool">no servers will be sent to client</ArgTableRow>
<ArgTableRow arg="wins-server" typ="multi { ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="ntp-server" typ="alt { , multi { ipAddr
 } { ipAddr
 }
 }"></ArgTableRow>
<ArgTableRow arg="ntp-none" typ="bool">no servers will be sent to client</ArgTableRow>
<ArgTableRow arg="caps-manager" typ="multi { ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="domain" typ="string"></ArgTableRow>
<ArgTableRow arg="next-server" typ="ipAddr">siaddr for next bootstrap step</ArgTableRow>
<ArgTableRow arg="boot-file-name" typ="string"></ArgTableRow>
<ArgTableRow arg="dhcp-option" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="dhcp-option-set" typ="enum (none)"></ArgTableRow>
</ArgTable>

### ip/dhcp-server/option

**Package:** dhcp
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="code" typ="alt { num [1 .. 254]
, enum (vendor-specific) { vendor-specific:43 }
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="value" typ="string">0x - exact hex value, '' - string or IP address value</ArgTableRow>
<ArgTableRow arg="force" typ="bool">always include this option in reply</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="raw-value" typ="string"></ArgTableRow>
</ArgTable>

#### ip/dhcp-server/option/sets

**Package:** dhcp
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="options" typ="multi { array-id, enum
 }" mandatory="1"></ArgTableRow>
</ArgTable>

### ip/dhcp-server/setup

**Package:** dhcp
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="network" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="gateway" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="relay" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="ippool" typ="multi { , , composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="send-dns" typ="bool"></ArgTableRow>
<ArgTableRow arg="dns-servers" typ="multi { ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="lease-time" typ="time"></ArgTableRow>
</ArgTable>
