# Vrrp

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/vrrp

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
<ArgTableRow arg="G" typ="grp-authority">grp-authority</ArgTableRow>
<ArgTableRow arg="g" typ="grp-member">grp-member</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
<ArgTableRow arg="M" typ="master">master</ArgTableRow>
<ArgTableRow arg="B" typ="backup">backup</ArgTableRow>
<ArgTableRow arg="F" typ="failure">failure</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp)"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { enum (auto) { auto:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="group-master" typ="iface_enum { :0, none:0, self:vrrp::LOOPBACK_ID }">deprecated</ArgTableRow>
<ArgTableRow arg="group-authority" typ="iface_enum { :0, none:0, self:vrrp::LOOPBACK_ID }">VRRP interface-authority that controls the entire group</ArgTableRow>
<ArgTableRow arg="vrid" typ="num"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="interval" typ="time"></ArgTableRow>
<ArgTableRow arg="preemption-mode" typ="bool"></ArgTableRow>
<ArgTableRow arg="authentication" typ="enum (none | simple | ah)"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="on-backup" typ="alt { , string
 }"></ArgTableRow>
<ArgTableRow arg="on-master" typ="alt { , string
 }"></ArgTableRow>
<ArgTableRow arg="on-fail" typ="alt { , string
 }"></ArgTableRow>
<ArgTableRow arg="version" typ="enum (2 | 3)"></ArgTableRow>
<ArgTableRow arg="v3-protocol" typ="enum (ipv4 | ipv6)"></ArgTableRow>
<ArgTableRow arg="sync-connection-tracking" typ="bool">Connection tracking data exchange between master and backup</ArgTableRow>
<ArgTableRow arg="remote-address" typ="ipAddr {  }">Forces address of the sender or receiver of Conntrack data</ArgTableRow>
<ArgTableRow arg="connection-tracking-mode" typ="enum (passive-active | active-active)"></ArgTableRow>
<ArgTableRow arg="connection-tracking-port" typ="num {  }">Port used for Conntrack data sync</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
</ArgTable>
