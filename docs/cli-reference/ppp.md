# ppp

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# ppp

**Package:** ppp
**Type:** Directory

## ppp/aaa

**Package:** ppp
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="use-radius" typ="bool"></ArgTableRow>
<ArgTableRow arg="accounting" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-circuit-id-in-nas-port-id" typ="bool"></ArgTableRow>
<ArgTableRow arg="interim-update" typ="time"></ArgTableRow>
<ArgTableRow arg="enable-ipv6-accounting" typ="bool"></ArgTableRow>
</ArgTable>

## ppp/active

**Package:** ppp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="R" typ="radius">radius</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="service" typ="enum (any | async | pptp | pppoe | l2tp | ovpn | sstp)"></ArgTableRow>
<ArgTableRow arg="caller-id" typ="string"></ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="encoding" typ="string"></ArgTableRow>
<ArgTableRow arg="session-id" typ="num"></ArgTableRow>
<ArgTableRow arg="limit-bytes-in" typ="num"></ArgTableRow>
<ArgTableRow arg="limit-bytes-out" typ="num"></ArgTableRow>
</ArgTable>

## ppp/l2tp-secret

**Package:** ppp
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="alt { ipPrefix
, ip6Prefix
 }"></ArgTableRow>
<ArgTableRow arg="secret" typ="string"></ArgTableRow>
</ArgTable>

## ppp/profile

**Package:** ppp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="local-address" typ="alt { enum
, ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="remote-address" typ="alt { enum
, ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="remote-ipv6-prefix-pool" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="remote-ipv6-prefix-reuse" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcpv6-pd-pool" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="dhcpv6-use-radius" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcpv6-lease-time" typ="time"></ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="bridge-port-priority" typ="num"></ArgTableRow>
<ArgTableRow arg="bridge-path-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="bridge-horizon" typ="num"></ArgTableRow>
<ArgTableRow arg="bridge-learning" typ="enum (default | no | yes)"></ArgTableRow>
<ArgTableRow arg="bridge-port-vid" typ="num"></ArgTableRow>
<ArgTableRow arg="bridge-port-trusted" typ="bool"></ArgTableRow>
<ArgTableRow arg="session-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="idle-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="use-ipv6" typ="enum (default | no | yes | required)"></ArgTableRow>
<ArgTableRow arg="use-mpls" typ="enum (default | no | yes | required)"></ArgTableRow>
<ArgTableRow arg="use-compression" typ="enum (default | no | yes)"></ArgTableRow>
<ArgTableRow arg="use-encryption" typ="enum (default | no | yes | required)"></ArgTableRow>
<ArgTableRow arg="only-one" typ="enum (default | no | yes)"></ArgTableRow>
<ArgTableRow arg="change-tcp-mss" typ="enum (default | no | yes)"></ArgTableRow>
<ArgTableRow arg="use-upnp" typ="enum (default | no | yes)"></ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string"></ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (bottom | first)"></ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="queue-type" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="incoming-filter" typ="enum"></ArgTableRow>
<ArgTableRow arg="outgoing-filter" typ="enum"></ArgTableRow>
<ArgTableRow arg="address-list" typ="multi { enum
 }"></ArgTableRow>
<ArgTableRow arg="interface-list" typ="enum"></ArgTableRow>
<ArgTableRow arg="dns-server" typ="multi { ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="wins-server" typ="multi { ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="on-up" typ="alt { , string
 }"></ArgTableRow>
<ArgTableRow arg="on-down" typ="alt { , string
 }"></ArgTableRow>
</ArgTable>

## ppp/secret

**Package:** ppp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="service" typ="enum (any | async | pptp | pppoe | l2tp | ovpn | sstp)"></ArgTableRow>
<ArgTableRow arg="caller-id" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="local-address" typ="super { ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="remote-address" typ="super { ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="routes" typ="string"></ArgTableRow>
<ArgTableRow arg="ipv6-routes" typ="string"></ArgTableRow>
<ArgTableRow arg="remote-ipv6-prefix" typ="super { ip6Prefix
 }"></ArgTableRow>
<ArgTableRow arg="limit-bytes-in" typ="num"></ArgTableRow>
<ArgTableRow arg="limit-bytes-out" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="last-logged-out" typ="date"></ArgTableRow>
<ArgTableRow arg="last-caller-id" typ="string"></ArgTableRow>
<ArgTableRow arg="last-disconnect-reason" typ="enum (peer-request | hung-up | idle-timeout | session-timeout | reset | reboot | port-error | nas-error | nas-request)"></ArgTableRow>
</ArgTable>
