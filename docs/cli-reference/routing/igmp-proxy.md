# Igmp Proxy

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/igmp-proxy

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="quick-leave" typ="bool">Specifies the action on IGMP Leave message. If quick-leave is on, then an IGMP Leave message is sent upstream as soon as a leave message is received from the first client on the downstream interface. Use `yes` only in case there is only one subscriber behind the proxy.</ArgTableRow>
<ArgTableRow arg="query-interval" typ="time">How often to send out IGMP Query messages over downstream interfaces.</ArgTableRow>
<ArgTableRow arg="query-response-interval" typ="time">How long to wait for responses to an IGMP Query message.</ArgTableRow>
</ArgTable>

### routing/igmp-proxy/interface

**Type:** Directory

Configure what interfaces will participate as IGMP proxy interfaces on the router. If an interface is not configured as an IGMP proxy interface, then all IGMP traffic received on it will be ignored.

It is possible to get detailed status information for each interface using the `print status` command.

```ros
[admin@MikroTik] /routing/igmp-proxy/interface/print status 
Flags: X - disabled, I - inactive, D - dynamic; U - upstream 
 0  U interface=ether2 threshold=1 alternative-subnets="" upstream=yes source-ip-address=192.168.10.10 rx-bytes=3018487500 rx-packets=2012325 tx-bytes=0 tx-packets=0 

 1    interface=ether3 threshold=1 alternative-subnets="" upstream=no querier=yes source-ip-address=192.168.20.10 rx-bytes=0 rx-packets=0 tx-bytes=2973486000 tx-packets=1982324 

 2    interface=ether4 threshold=1 alternative-subnets="" upstream=no querier=yes source-ip-address=192.168.30.10 rx-bytes=0 rx-packets=0 tx-bytes=152019000 tx-packets=101346 
```

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="U" typ="upstream">upstream</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum { all:0 }">Name of the interface.</ArgTableRow>
<ArgTableRow arg="threshold" typ="num">Minimal TTL. Packets received with a lower TTL value are ignored</ArgTableRow>
<ArgTableRow arg="alternative-subnets" typ="multi { , , super { ipAddr
, /num
 } { ipAddr
, /num
 }
 }">By default, only packets from directly attached subnets are accepted. This parameter can be used to specify a list of alternative valid packet source subnets, both for data and IGMP packets. Has an effect only on the upstream interface. Should be used when the source of multicast data often is in a different IP network.</ArgTableRow>
<ArgTableRow arg="upstream" typ="bool">The interface is called "upstream" if it's in the direction of the root of the multicast tree. An IGMP forwarding router must have exactly one upstream interface configured. The upstream interface is used to send out IGMP membership requests.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="querier" typ="bool">Whether the interface is acting as an IGMP querier.</ArgTableRow>
<ArgTableRow arg="source-ip-address" typ="ipAddr">The detected source IP for the interface.</ArgTableRow>
<ArgTableRow arg="rx-bytes" typ="num">The total amount of received multicast traffic on the interface.</ArgTableRow>
<ArgTableRow arg="rx-packets" typ="num">The total amount of received multicast packets on the interface.</ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="num">The total amount of transmitted multicast traffic on the interface.</ArgTableRow>
<ArgTableRow arg="tx-packets" typ="num">The total amount of transmitted multicast packets on the interface.</ArgTableRow>
</ArgTable>

### routing/igmp-proxy/mfc

**Type:** Directory

Multicast forwarding cache (MFC) status.

RouterOS supports static multicast forwarding rules for IGMP proxy. If a static rule is added, all dynamic rules for that group will be ignored. These rules will take effect only if IGMP-proxy interfaces are configured (upstream and downstream interfaces should be set) otherwise these rules won't be active.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="A" typ="active">active</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="group" typ="ipAddr" mandatory="1">The multicast group address this rule applies to.</ArgTableRow>
<ArgTableRow arg="source" typ="ipAddr" mandatory="1">The multicast data originator address.</ArgTableRow>
<ArgTableRow arg="upstream-interface" typ="iface_enum" mandatory="1">The interface that is receiving stream data.</ArgTableRow>
<ArgTableRow arg="downstream-interfaces" typ="multi { iface_enum
 }">The received stream will be sent out to the listed interfaces only.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="active-downstream-interfaces" typ="multi { iface_enum
 }">The packet stream is going out of the router through this interface.</ArgTableRow>
<ArgTableRow arg="bytes" typ="num">The total amount of received multicast traffic.</ArgTableRow>
<ArgTableRow arg="packets" typ="num">The total amount of received multicast packets.</ArgTableRow>
<ArgTableRow arg="wrong-packets" typ="num">The total amount of received multicast packets that arrived on a wrong interface, for example, a multicast stream that is received on a downstream interface instead of an upstream interface.</ArgTableRow>
</ArgTable>
