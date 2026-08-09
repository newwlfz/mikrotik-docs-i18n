# Bgp

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/bgp

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="routing-table" typ="enum" unset="1">Name of the routing table, to install routes in. Overrides the instance parameter.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1">Name of the VRF BGP connections operate on. By default uses the "main" routing table.</ArgTableRow>
<ArgTableRow arg="templates" typ="multi { enum
 }" unset="1">List of template names that will be used to inherit parameter values from. Useful feature, to easily configure groups with overlapping configuration options.</ArgTableRow>
<ArgTableRow arg="as" typ="as" unset="1">A 32-bit BGP autonomous system number. The value accepts AS-Plain or AS-Dot formats. Override the instance ASN and configure BGP confederation using the following format: _`confederation_as/as`_. For example, if your AS is 34 and your confederation AS is 43, set `as=43/34`.</ArgTableRow>
<ArgTableRow arg="nexthop-choice" typ="enum (default | force-self | propagate)" unset="1">Affect outgoing **NEXT\_HOP** attribute selection. Next-hops set in filters always take precedence and are not changed on route reflection except when set in a filter.   default - select the next-hop as described in [`RFC 4271`](https://tools.ietf.org/html/rfc4271)   force-self - use the local address of the interface that connects to the peer as the next-hop   propagate - propagate received next-hop; if the route has a BGP **NEXT\_HOP** attribute, use it as the next-hop; otherwise, fall back to the default case</ArgTableRow>
<ArgTableRow arg="multihop" typ="bool" unset="1">Enable when the remote peer is more than one hop away.This option affects outgoing next-hop selection as described in [`RFC 4271`](https://tools.ietf.org/html/rfc4271) (for eBGP only, excluding iBGP peers local to the confederation). It also affects:Whether to accept connections from peers not in the same network (the remote address of the connection is used for this check)Whether to accept incoming routes with a NEXT\_HOP attribute not in the same network as the address used to establish the connectionThe target scope of routes installed from this peer; routes from multi-hop or iBGP peers resolve their next-hops through IGP routes by default</ArgTableRow>
<ArgTableRow arg="hold-time" typ="alt { enum (infinity) { infinity:0 }
, time [3 .. 65535]
 }" unset="1">Specifies the BGP Hold Time value to be used when negotiating with peers.According to the BGP specification, if the router does not receive successive **KEEPALIVE** and/or **UPDATE** and/or **NOTIFICATION** messages within the period specified in the Hold Time field of the **OPEN** message, then the BGP connection to the peer will be closed.The minimal `hold-time` value of both peers will be used (note that the special value 0 or 'infinity' is lower than any other value)*   infinity \- never expire the connection and never send keepalive messages.</ArgTableRow>
<ArgTableRow arg="keepalive-time" typ="time" unset="1">The interval between keepalive messages, if not set then by default keepalive is 1/3 of the `hold-time`.</ArgTableRow>
<ArgTableRow arg="afi" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6, evpn)" unset="1">List of address families this peer can exchange routing information. The remote peer must support BGP capabilities optional parameter (they usually do) to negotiate any other address families than IP.</ArgTableRow>
<ArgTableRow arg="cisco-vpls-nlri-len-fmt" typ="enum (auto-bits | auto-bytes | bits | bytes)" unset="1">VPLS NLRI length format type. Used for compatibility with Cisco VPLS. \[\[Read more>>\]\].</ArgTableRow>
<ArgTableRow arg="output.remove-private-as" typ="bool" unset="1">If set, then the BGP **AS-PATH** attribute is removed before sending out route updates if the attribute contains only private AS numbers.The removal process happens before routing filters are applied and before the local, AS number is prepended to the AS path.</ArgTableRow>
<ArgTableRow arg="output.as-override" typ="bool" unset="1">If set, then all instances of the remote peer's AS number in the BGP **AS-PATH** attribute are replaced with the local AS number before sending a route update to that peer. Happens before routing filters and prepend.</ArgTableRow>
<ArgTableRow arg="use-bfd" typ="bool" unset="1">Whether to use the BFD protocol for faster connection state detection.</ArgTableRow>
<ArgTableRow arg="save-to" typ="string" unset="1">Filename to save BGP protocol-specific packet content (Exported PDU) into pcap format. This method allows much simpler peer-specific packet capturing for debugging purposes.</ArgTableRow>
<ArgTableRow arg="output.add-path" typ="ubit (ip, ipv6)" unset="1">Enable sending of additional paths for specified address families (BGP Addpath).</ArgTableRow>
<ArgTableRow arg="output.affinity" typ="enum (main | alone | remote-as | instance | afi | vrf | input)" unset="1">Configure output multicore processing. Read more in [Routing Protocol Multi-core Support](../../user-guides/routing-and-networking-protocols/routing-protocol-multi-core-support.md) article.   **alone** - input and output of each session is processed in its own process, the most likely best option when there are a lot of cores and a lot of peers   **afi, instance, vrf, remote-as** - try to run input/output of new session in process with similar parameters   **main** - run input/output in the main process (could potentially increase performance on single-core even possibly on multicore devices with small amount of cores)   **input** - run output in the same process as input (can be set only for output affinity)</ArgTableRow>
<ArgTableRow arg="output.redistribute" typ="ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, bgp-mpls-vpn, slaac)" unset="1">Enable redistribution of specified route types.</ArgTableRow>
<ArgTableRow arg="output.filter-select" typ="enum" unset="1">Name of the routing select chain to be used for prefix selection. If not specified, then default selection is used.</ArgTableRow>
<ArgTableRow arg="output.filter-chain" typ="enum" unset="1">Name of the routing filter chain to be used on the output prefixes. If the chain is not specified, then BGP by default accepts everything.</ArgTableRow>
<ArgTableRow arg="output.network" typ="enum" unset="1">Name of the address list used to send local networks. The network is sent only if a matching IGP route exists in the routing table and its **ORIGIN** attribute is set to IGP, other distribution methods have **ORIGIN** attribute set to INCOMPLETE.</ArgTableRow>
<ArgTableRow arg="output.network-blackhole" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="output.default-originate" typ="enum (never | if-installed | always)" unset="1">Specifies default route (0.0.0.0/0) distribution method. 'if-installed' option can be used to distribute default route only if corresponding IGP route present in the routing table.</ArgTableRow>
<ArgTableRow arg="output.default-prepend" typ="num" unset="1">How many times to prepend local ASN.</ArgTableRow>
<ArgTableRow arg="output.no-client-to-client-reflection" typ="bool" unset="1">Disable client-to-client route reflection in Route Reflector setups.</ArgTableRow>
<ArgTableRow arg="output.no-early-cut" typ="bool" unset="1">The early cut is the mechanism, to guess (based on default RFC behavior) what would happen with the sent NLRI when received by the remote peer. If the algorithm determines that the NLRI is going to be dropped, a peer will not even try to send it. However such behavior may not be desired in specific scenarios, then this option should be used to disable the early cut feature. Early cut works with eBGP sessions.</ArgTableRow>
<ArgTableRow arg="output.keep-sent-attributes" typ="bool" unset="1">Store in memory sent prefix attributes, required for `dump-saved-advertisements` command to work. By default, sent-out prefixes are not stored to preserve the router's memory. An option should be enabled only for debugging purposes when necessary to see currently advertised prefixes.</ArgTableRow>
<ArgTableRow arg="input.add-path" typ="ubit (ip, ipv6)" unset="1">Accept received additional paths (BGP Addpath) for specified address families.</ArgTableRow>
<ArgTableRow arg="input.attr-error-handling" typ="enum (default | revised)"></ArgTableRow>
<ArgTableRow arg="input.affinity" typ="enum (main | alone | remote-as | instance | afi | vrf)" unset="1">
Configure input multi-core processing. Read more in [Routing Protocol Multi-core Support](../../user-guides/routing-and-networking-protocols/routing-protocol-multi-core-support.md) article.
- **alone** - input and output of each session are processed in its own process, most likely the best option when there are a lot of cores and a lot of peers.
- **afi, instance, vrf, remote-as** - try to run input/output of new session in process with similar parameters.
- **main** - run input/output in the main process (could potentially increase performance on single-core even possibly on multi-core devices with a small amount of cores).
</ArgTableRow>
<ArgTableRow arg="input.filter" typ="enum" unset="1">Name of the routing filter chain to be used on input prefixes. This happens after NLRIs are processed. If the chain is not specified, then BGP by default accepts everything.</ArgTableRow>
<ArgTableRow arg="input.filter-nlri" typ="enum" unset="1">Name of the filter chain that will filter incoming IPv4/IPv6 NLRIs directly before they are  stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session restart.</ArgTableRow>
<ArgTableRow arg="input.allow-as" typ="num" unset="1">Indicates how many times to allow your own AS number in AS-PATH, before discarding a prefix.</ArgTableRow>
<ArgTableRow arg="input.accept-nlri" typ="enum" unset="1">Name of the ipv4/6 address-list. A quick way to filter incoming updates with specific NLRIs. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session restart.</ArgTableRow>
<ArgTableRow arg="input.filter-communities" typ="enum" unset="1">A quick way to filter incoming updates with specific communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.</ArgTableRow>
<ArgTableRow arg="input.filter-ext-communities" typ="enum" unset="1">A quick way to filter incoming updates with specific extended communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.</ArgTableRow>
<ArgTableRow arg="input.filter-large-communities" typ="enum" unset="1">A quick way to filter incoming updates with specific large communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.</ArgTableRow>
<ArgTableRow arg="input.accept-communities" typ="enum" unset="1">A quick way to filter incoming updates with specific communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.</ArgTableRow>
<ArgTableRow arg="input.accept-ext-communities" typ="enum" unset="1">A quick way to filter incoming updates with specific extended communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.</ArgTableRow>
<ArgTableRow arg="input.accept-large-communities" typ="enum" unset="1">A quick way to filter incoming updates with specific large communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.</ArgTableRow>
<ArgTableRow arg="input.filter-unknown" typ="enum" unset="1">A quick way to filter incoming updates with specific "unknown" attributes. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.</ArgTableRow>
<ArgTableRow arg="input.limit-process-routes-ipv4" typ="enum (10 | 100 | 1000 | 10000 | 100000 | 1000000 | 10000000)" unset="1">Try to limit the amount of received IPv4 routes to the specified number. This number does not represent the exact number of routes going to be installed in the routing table by the peer. [BGP session "clear"](#routingbgpsessionclear) command must be used to reset the flag if the limit is reached.</ArgTableRow>
<ArgTableRow arg="input.limit-process-routes-ipv6" typ="enum (10 | 100 | 1000 | 10000 | 100000 | 1000000 | 10000000)" unset="1">Try to limit the amount of received IPv6 routes to the specified number. This number does not represent the exact number of routes going to be installed in the routing table by the peer. BGP session "clear" command must be used to reset the flag if the limit is reached.</ArgTableRow>
</ArgTable>

### routing/bgp/advertisements

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="peer" typ="enum"></ArgTableRow>
<ArgTableRow arg="dst" typ="address (flags=46/R)"></ArgTableRow>
<ArgTableRow arg="afi" typ="enum (ip | ipv6 | l2vpn | l2vpn-cisco | vpnv4 | vpnv6)"></ArgTableRow>
<ArgTableRow arg="local-pref" typ="num"></ArgTableRow>
<ArgTableRow arg="med" typ="num"></ArgTableRow>
<ArgTableRow arg="nexthop" typ="multi { address (flags=46)
 }"></ArgTableRow>
<ArgTableRow arg="nlri" typ="multi { address (flags=46i/SR)
 }"></ArgTableRow>
<ArgTableRow arg="withdrawn" typ="multi { address (flags=46i/SR)
 }"></ArgTableRow>
<ArgTableRow arg="origin" typ="num"></ArgTableRow>
<ArgTableRow arg="as-path" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="as4-path" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="communities" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="ext-communities" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="large-communities" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="atomic-aggregate" typ="bool"></ArgTableRow>
<ArgTableRow arg="aggregator" typ="string"></ArgTableRow>
<ArgTableRow arg="as4-aggregator" typ="string"></ArgTableRow>
<ArgTableRow arg="originator-id" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="cluster-list" typ="multi { ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="igp-metric" typ="num"></ArgTableRow>
<ArgTableRow arg="otc" typ="num"></ArgTableRow>
</ArgTable>

### routing/bgp/connection

**Conditions:** !smips
**Type:** Directory

A list of all connection-specific parameters can be seen in the table below.

In addition to connection-specific parameters, template-specific parameters are also directly exposed in this menu, for easier configuration in simple scenarios (when templates are not necessary).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="instance" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="remote.address" typ="address (flags=46i/+:)" unset="1">Remote address used to connect and/or listen to.</ArgTableRow>
<ArgTableRow arg="remote.port" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="remote.as" typ="super { as
, [ /as]
 }" unset="1">Remote AS number. If not specified BGP will determine remote AS automatically from the OPEN message.</ArgTableRow>
<ArgTableRow arg="remote.ttl" typ="num">Acceptable minimum Time To Live, the hop limit for this TCP connection. For example, if 'ttl=255' then only single-hop neighbors will be able to establish the connection. This property only affects EBGP peers.</ArgTableRow>
<ArgTableRow arg="remote.allowed-as" typ="enum" unset="1">Name of the num-list containing remote AS numbers that will be allowed to connect. Useful for dynamic peer configuration.</ArgTableRow>
<ArgTableRow arg="local.address" typ="address (flags=46i:)" unset="1"></ArgTableRow>
<ArgTableRow arg="local.port" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="local.ttl" typ="num">Time To Live (hop limit) that will be recorded in sent TCP packets.</ArgTableRow>
<ArgTableRow arg="local.role" typ="enum (ibgp | ibgp-rr | ebgp | ebgp-provider | ebgp-rs | ebgp-rs-client | ebgp-customer | ebgp-peer)" mandatory="1">BGP role. In most scenarios, set to iBGP or eBGP. For more information on BGP roles, see the corresponding [RFC 9234](https://tools.ietf.org/html/rfc9234).</ArgTableRow>
<ArgTableRow arg="tcp-md5-key" typ="string" unset="1">Key used to authenticate the connection with TCP MD5 signature as described in [RFC 2385](https://tools.ietf.org/html/rfc2385). Leave empty to disable authentication.</ArgTableRow>
<ArgTableRow arg="connect" typ="bool">Whether to allow the router to initiate the connection.</ArgTableRow>
<ArgTableRow arg="listen" typ="bool">Enable listening for incoming connections. If `remote.address` is a host address and listening is enabled, close the listening socket after the first successful accept. If `remote.address` is a subnet and listening is enabled, the listening socket remains open after the first successful accept with a hard-coded limit of 256 open connections.</ArgTableRow>
<ArgTableRow arg="routing-table" typ="enum" unset="1">Name of the routing table, to install routes in. Overrides the instance parameter.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1">Name of the VRF BGP connections operate on. By default uses the "main" routing table.</ArgTableRow>
<ArgTableRow arg="templates" typ="multi { enum
 }" unset="1">List of template names that will be used to inherit parameter values from. Useful feature, to easily configure groups with overlapping configuration options.</ArgTableRow>
<ArgTableRow arg="as" typ="as" unset="1">A 32-bit BGP autonomous system number. The value accepts AS-Plain or AS-Dot formats. Override the instance ASN and configure BGP confederation using the following format: _`confederation_as/as`_. For example, if your AS is 34 and your confederation AS is 43, set `as=43/34`.</ArgTableRow>
<ArgTableRow arg="nexthop-choice" typ="enum (default | force-self | propagate)" unset="1">Affect outgoing **NEXT\_HOP** attribute selection. Next-hops set in filters always take precedence and are not changed on route reflection except when set in a filter.   default - select the next-hop as described in [`RFC 4271`](https://tools.ietf.org/html/rfc4271)   force-self - use the local address of the interface that connects to the peer as the next-hop   propagate - propagate received next-hop; if the route has a BGP **NEXT\_HOP** attribute, use it as the next-hop; otherwise, fall back to the default case</ArgTableRow>
<ArgTableRow arg="multihop" typ="bool" unset="1">Enable when the remote peer is more than one hop away.This option affects outgoing next-hop selection as described in [`RFC 4271`](https://tools.ietf.org/html/rfc4271) (for eBGP only, excluding iBGP peers local to the confederation). It also affects:Whether to accept connections from peers not in the same network (the remote address of the connection is used for this check)Whether to accept incoming routes with a NEXT\_HOP attribute not in the same network as the address used to establish the connectionThe target scope of routes installed from this peer; routes from multi-hop or iBGP peers resolve their next-hops through IGP routes by default</ArgTableRow>
<ArgTableRow arg="hold-time" typ="alt { enum (infinity) { infinity:0 }
, time [3 .. 65535]
 }" unset="1">Specifies the BGP Hold Time value to be used when negotiating with peers.According to the BGP specification, if the router does not receive successive **KEEPALIVE** and/or **UPDATE** and/or **NOTIFICATION** messages within the period specified in the Hold Time field of the **OPEN** message, then the BGP connection to the peer will be closed.The minimal `hold-time` value of both peers will be used (note that the special value 0 or 'infinity' is lower than any other value)*   infinity \- never expire the connection and never send keepalive messages.</ArgTableRow>
<ArgTableRow arg="keepalive-time" typ="time" unset="1">The interval between keepalive messages, if not set then by default keepalive is 1/3 of the `hold-time`.</ArgTableRow>
<ArgTableRow arg="afi" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6, evpn)" unset="1">List of address families this peer can exchange routing information. The remote peer must support BGP capabilities optional parameter (they usually do) to negotiate any other address families than IP.</ArgTableRow>
<ArgTableRow arg="cisco-vpls-nlri-len-fmt" typ="enum (auto-bits | auto-bytes | bits | bytes)" unset="1">VPLS NLRI length format type. Used for compatibility with Cisco VPLS. \[\[Read more>>\]\].</ArgTableRow>
<ArgTableRow arg="output.remove-private-as" typ="bool" unset="1">If set, then the BGP **AS-PATH** attribute is removed before sending out route updates if the attribute contains only private AS numbers.The removal process happens before routing filters are applied and before the local, AS number is prepended to the AS path.</ArgTableRow>
<ArgTableRow arg="output.as-override" typ="bool" unset="1">If set, then all instances of the remote peer's AS number in the BGP **AS-PATH** attribute are replaced with the local AS number before sending a route update to that peer. Happens before routing filters and prepend.</ArgTableRow>
<ArgTableRow arg="use-bfd" typ="bool" unset="1">Whether to use the BFD protocol for faster connection state detection.</ArgTableRow>
<ArgTableRow arg="save-to" typ="string" unset="1">Filename to save BGP protocol-specific packet content (Exported PDU) into pcap format. This method allows much simpler peer-specific packet capturing for debugging purposes.</ArgTableRow>
<ArgTableRow arg="output.add-path" typ="ubit (ip, ipv6)" unset="1">Enable sending of additional paths for specified address families (BGP Addpath).</ArgTableRow>
<ArgTableRow arg="output.affinity" typ="enum (main | alone | remote-as | instance | afi | vrf | input)" unset="1">Configure output multicore processing. Read more in [Routing Protocol Multi-core Support](../../user-guides/routing-and-networking-protocols/routing-protocol-multi-core-support.md) article.   **alone** - input and output of each session is processed in its own process, the most likely best option when there are a lot of cores and a lot of peers   **afi, instance, vrf, remote-as** - try to run input/output of new session in process with similar parameters   **main** - run input/output in the main process (could potentially increase performance on single-core even possibly on multicore devices with small amount of cores)   **input** - run output in the same process as input (can be set only for output affinity)</ArgTableRow>
<ArgTableRow arg="output.redistribute" typ="ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, bgp-mpls-vpn, slaac)" unset="1">Enable redistribution of specified route types.</ArgTableRow>
<ArgTableRow arg="output.filter-select" typ="enum" unset="1">Name of the routing select chain to be used for prefix selection. If not specified, then default selection is used.</ArgTableRow>
<ArgTableRow arg="output.filter-chain" typ="enum" unset="1">Name of the routing filter chain to be used on the output prefixes. If the chain is not specified, then BGP by default accepts everything.</ArgTableRow>
<ArgTableRow arg="output.network" typ="enum" unset="1">Name of the address list used to send local networks. The network is sent only if a matching IGP route exists in the routing table and its **ORIGIN** attribute is set to IGP, other distribution methods have **ORIGIN** attribute set to INCOMPLETE.</ArgTableRow>
<ArgTableRow arg="output.network-blackhole" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="output.default-originate" typ="enum (never | if-installed | always)" unset="1">Specifies default route (0.0.0.0/0) distribution method. 'if-installed' option can be used to distribute default route only if corresponding IGP route present in the routing table.</ArgTableRow>
<ArgTableRow arg="output.default-prepend" typ="num" unset="1">How many times to prepend local ASN.</ArgTableRow>
<ArgTableRow arg="output.no-client-to-client-reflection" typ="bool" unset="1">Disable client-to-client route reflection in Route Reflector setups.</ArgTableRow>
<ArgTableRow arg="output.no-early-cut" typ="bool" unset="1">The early cut is the mechanism, to guess (based on default RFC behavior) what would happen with the sent NLRI when received by the remote peer. If the algorithm determines that the NLRI is going to be dropped, a peer will not even try to send it. However such behavior may not be desired in specific scenarios, then this option should be used to disable the early cut feature. Early cut works with eBGP sessions.</ArgTableRow>
<ArgTableRow arg="output.keep-sent-attributes" typ="bool" unset="1">Store in memory sent prefix attributes, required for `dump-saved-advertisements` command to work. By default, sent-out prefixes are not stored to preserve the router's memory. An option should be enabled only for debugging purposes when necessary to see currently advertised prefixes.</ArgTableRow>
<ArgTableRow arg="input.add-path" typ="ubit (ip, ipv6)" unset="1">Accept received additional paths (BGP Addpath) for specified address families.</ArgTableRow>
<ArgTableRow arg="input.attr-error-handling" typ="enum (default | revised)"></ArgTableRow>
<ArgTableRow arg="input.affinity" typ="enum (main | alone | remote-as | instance | afi | vrf)" unset="1">
Configure input multi-core processing. Read more in [Routing Protocol Multi-core Support](../../user-guides/routing-and-networking-protocols/routing-protocol-multi-core-support.md) article.
- **alone** - input and output of each session are processed in its own process, most likely the best option when there are a lot of cores and a lot of peers.
- **afi, instance, vrf, remote-as** - try to run input/output of new session in process with similar parameters.
- **main** - run input/output in the main process (could potentially increase performance on single-core even possibly on multi-core devices with a small amount of cores).
</ArgTableRow>
<ArgTableRow arg="input.filter" typ="enum" unset="1">Name of the routing filter chain to be used on input prefixes. This happens after NLRIs are processed. If the chain is not specified, then BGP by default accepts everything.</ArgTableRow>
<ArgTableRow arg="input.filter-nlri" typ="enum" unset="1">Name of the filter chain that will filter incoming IPv4/IPv6 NLRIs directly before they are  stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session restart.</ArgTableRow>
<ArgTableRow arg="input.allow-as" typ="num" unset="1">Indicates how many times to allow your own AS number in AS-PATH, before discarding a prefix.</ArgTableRow>
<ArgTableRow arg="input.accept-nlri" typ="enum" unset="1">Name of the ipv4/6 address-list. A quick way to filter incoming updates with specific NLRIs. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session restart.</ArgTableRow>
<ArgTableRow arg="input.filter-communities" typ="enum" unset="1">A quick way to filter incoming updates with specific communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.</ArgTableRow>
<ArgTableRow arg="input.filter-ext-communities" typ="enum" unset="1">A quick way to filter incoming updates with specific extended communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.</ArgTableRow>
<ArgTableRow arg="input.filter-large-communities" typ="enum" unset="1">A quick way to filter incoming updates with specific large communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.</ArgTableRow>
<ArgTableRow arg="input.accept-communities" typ="enum" unset="1">A quick way to filter incoming updates with specific communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.</ArgTableRow>
<ArgTableRow arg="input.accept-ext-communities" typ="enum" unset="1">A quick way to filter incoming updates with specific extended communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.</ArgTableRow>
<ArgTableRow arg="input.accept-large-communities" typ="enum" unset="1">A quick way to filter incoming updates with specific large communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.</ArgTableRow>
<ArgTableRow arg="input.filter-unknown" typ="enum" unset="1">A quick way to filter incoming updates with specific "unknown" attributes. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.</ArgTableRow>
<ArgTableRow arg="input.limit-process-routes-ipv4" typ="enum (10 | 100 | 1000 | 10000 | 100000 | 1000000 | 10000000)" unset="1">Try to limit the amount of received IPv4 routes to the specified number. This number does not represent the exact number of routes going to be installed in the routing table by the peer. [BGP session "clear"](#routingbgpsessionclear) command must be used to reset the flag if the limit is reached.</ArgTableRow>
<ArgTableRow arg="input.limit-process-routes-ipv6" typ="enum (10 | 100 | 1000 | 10000 | 100000 | 1000000 | 10000000)" unset="1">Try to limit the amount of received IPv6 routes to the specified number. This number does not represent the exact number of routes going to be installed in the routing table by the peer. BGP session "clear" command must be used to reset the flag if the limit is reached.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="local.default-address" typ="address (flags=46i:)"></ArgTableRow>
</ArgTable>

### routing/bgp/evpn

**Conditions:** !smips
**Type:** Directory

See EVPN documentation.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="instance" typ="enum" mandatory="1">BGP instance this EVPN is assigned to.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1">Name of the VRF table that this EVPN instance will use.</ArgTableRow>
<ArgTableRow arg="rd" typ="address (flags=R)" unset="1">Specifies the value that gets attached to route so that receiving routers can distinguish advertisements that may otherwise look the same. Used to distinguish between tenants using overlapping IP ranges. Also can be used to simplify convergence and redundancy within Virtual Network. RDs from MLAG pairs should be unique, too.</ArgTableRow>
<ArgTableRow arg="vni" typ="object { range
 }" unset="1">Range of Virtual Network Identifiers.</ArgTableRow>
<ArgTableRow arg="import.route-targets" typ="object { address (flags=R)
 }" unset="1">List of route targets that will be used to import EVPN routes.</ArgTableRow>
<ArgTableRow arg="export.route-targets" typ="object { address (flags=R)
 }" unset="1">List of route targets that will be added to EVPN routes when exporting.</ArgTableRow>
</ArgTable>

### routing/bgp/instance

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="routing-table" typ="enum" unset="1">Name of the routing table, to install routes in.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1">Name of the VRF BGP connections operate on. By default always uses the "main" routing table.</ArgTableRow>
<ArgTableRow arg="router-id" typ="alt { ipAddr
, enum
 }" unset="1">BGP Router ID to be used. Use the ID from the `/routing/router-id` configuration by specifying the reference name, or set the ID directly by specifying IP.Equal router-ids are also used to group peers into one instance.</ArgTableRow>
<ArgTableRow arg="as" typ="super { as
, [ /as]
 }" unset="1">32-bit BGP autonomous system number. Enter the value in AS-Plain or AS-Dot formats. Configure BGP confederation using the following format: _`confederation_as/as`_. For example, if your AS is 34 and your confederation AS is 43, set `as=43/34`.</ArgTableRow>
<ArgTableRow arg="cluster-id" typ="ipAddr" unset="1">For route reflector instances, specify the cluster ID of the route reflector cluster. This attribute identifies routing updates from other route reflectors in the cluster to avoid routing information loops. Typically, only one route reflector exists per cluster; in this case, do not configure 'cluster-id' and BGP router ID is used instead.</ArgTableRow>
<ArgTableRow arg="ignore-as-path-len" typ="bool" unset="1">Ignore the **AS_PATH** attribute in the BGP route selection algorithm. Applies to input.</ArgTableRow>
<ArgTableRow arg="multipath" typ="num" unset="1">Install the specified number of ECMP routes received by add-path or selected by [best path selection](../../user-guides/routing-and-networking-protocols/unicast/bgp/understanding-bgp.md#best-path-selection).</ArgTableRow>
</ArgTable>

### routing/bgp/session

**Conditions:** !smips
**Type:** Directory

List of BGP already established, not yet connected or disconnected sessions.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="E" typ="established">established</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="remote.address" typ="address (flags=46iv+:)"></ArgTableRow>
<ArgTableRow arg="remote.port" typ="num"></ArgTableRow>
<ArgTableRow arg="remote.as" typ="super { as
, [ /as]
 }"></ArgTableRow>
<ArgTableRow arg="remote.id" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="remote.refused-cap-opt" typ="bool"></ArgTableRow>
<ArgTableRow arg="remote.capabilities" typ="ubit (mp, rr, orf, enhe, em, sec, ml, role, gr, as4, dyn, ms, ap, err, llgr, fqdn)">Remote peer's advertised/supported capabilities.</ArgTableRow>
<ArgTableRow arg="remote.afi" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6, evpn)">Remote peer's advertised/supported address families.</ArgTableRow>
<ArgTableRow arg="remote.hold-time" typ="alt { enum (infinity) { infinity:0 }
, time [3 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="remote.messages" typ="num">Number of BGP messages received from remote peer.</ArgTableRow>
<ArgTableRow arg="remote.bytes" typ="num">Total number of bytes received from remote peer.</ArgTableRow>
<ArgTableRow arg="remote.gr-restart" typ="bool"></ArgTableRow>
<ArgTableRow arg="remote.gr-time" typ="num"></ArgTableRow>
<ArgTableRow arg="remote.gr-afi" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6)"></ArgTableRow>
<ArgTableRow arg="remote.gr-afi-fwp" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6)"></ArgTableRow>
<ArgTableRow arg="remote.eor" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6, evpn)">List of address families that received end-of-rib from remote peer.</ArgTableRow>
<ArgTableRow arg="remote.role" typ="enum (provider | route-server | route-server-client | customer | peer)"></ArgTableRow>
<ArgTableRow arg="local.role" typ="enum (ibgp | ibgp-rr | ebgp | ebgp-provider | ebgp-rs | ebgp-rs-client | ebgp-customer | ebgp-peer)"></ArgTableRow>
<ArgTableRow arg="local.address" typ="address (flags=46iv:)"></ArgTableRow>
<ArgTableRow arg="local.port" typ="num"></ArgTableRow>
<ArgTableRow arg="local.as" typ="super { as
, [ /as]
 }"></ArgTableRow>
<ArgTableRow arg="local.id" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="local.cluster-id" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="local.capabilities" typ="ubit (mp, rr, enhe, role, gr, as4, ap)"></ArgTableRow>
<ArgTableRow arg="local.afi" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6, evpn)"></ArgTableRow>
<ArgTableRow arg="local.messages" typ="num"></ArgTableRow>
<ArgTableRow arg="local.bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="local.eor" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4)"></ArgTableRow>
<ArgTableRow arg="output.affinity" typ="enum (main | alone | remote-as | instance | afi | vrf | input)"></ArgTableRow>
<ArgTableRow arg="output.procid" typ="num"></ArgTableRow>
<ArgTableRow arg="output.filter-select" typ="enum"></ArgTableRow>
<ArgTableRow arg="output.filter-chain" typ="enum"></ArgTableRow>
<ArgTableRow arg="output.network" typ="enum"></ArgTableRow>
<ArgTableRow arg="output.add-path" typ="ubit (ip, ipv6)"></ArgTableRow>
<ArgTableRow arg="output.remove-private-as" typ="bool"></ArgTableRow>
<ArgTableRow arg="output.default-originate" typ="enum (never | if-installed | always)"></ArgTableRow>
<ArgTableRow arg="output.default-prepend" typ="num"></ArgTableRow>
<ArgTableRow arg="output.no-client-to-client-reflection" typ="bool"></ArgTableRow>
<ArgTableRow arg="output.no-early-cut" typ="bool"></ArgTableRow>
<ArgTableRow arg="output.keep-sent-attributes" typ="bool"></ArgTableRow>
<ArgTableRow arg="output.last-notification" typ="string">Content of last sent notification message.</ArgTableRow>
<ArgTableRow arg="input.affinity" typ="enum (main | alone | remote-as | instance | afi | vrf)"></ArgTableRow>
<ArgTableRow arg="input.procid" typ="num">Shows which routing process the session is tied to.</ArgTableRow>
<ArgTableRow arg="input.filter" typ="enum"></ArgTableRow>
<ArgTableRow arg="input.allow-as" typ="num"></ArgTableRow>
<ArgTableRow arg="input.as-override" typ="bool"></ArgTableRow>
<ArgTableRow arg="input.ignore-as-path-len" typ="bool"></ArgTableRow>
<ArgTableRow arg="input.limit-process-routes" typ="num"></ArgTableRow>
<ArgTableRow arg="input.add-path" typ="ubit (ip, ipv6)"></ArgTableRow>
<ArgTableRow arg="input.last-notification" typ="string">Content of last received notification message.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="ibgp" typ="switch">Indicates if the session is iBGP.</ArgTableRow>
<ArgTableRow arg="ebgp" typ="switch">Indicates if the session is eBGP.</ArgTableRow>
<ArgTableRow arg="limit-exceeded" typ="switch">Indicates if received prefix count exceeds configured prefix limit by `input.limit-process-routes-ipv4` and/or `input.limit-process-routes-ipv6`.</ArgTableRow>
<ArgTableRow arg="stopped" typ="switch">Indicates whether session is administratively stopped.</ArgTableRow>
<ArgTableRow arg="routing-table" typ="enum"></ArgTableRow>
<ArgTableRow arg="nexthop-choice" typ="enum (default | force-self | propagate)"></ArgTableRow>
<ArgTableRow arg="cisco-vpls-nlri-len-fmt" typ="enum (auto-bits | auto-bytes | bits | bytes)"></ArgTableRow>
<ArgTableRow arg="multihop" typ="bool"></ArgTableRow>
<ArgTableRow arg="hold-time" typ="alt { enum (infinity) { infinity:0 }
, time [3 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="keepalive-time" typ="time"></ArgTableRow>
<ArgTableRow arg="use-bfd" typ="bool"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time">Uptime of established session.</ArgTableRow>
<ArgTableRow arg="last-started" typ="date"></ArgTableRow>
<ArgTableRow arg="last-stopped" typ="date"></ArgTableRow>
<ArgTableRow arg="save-to" typ="string"></ArgTableRow>
<ArgTableRow arg="prefix-count" typ="num"></ArgTableRow>
<ArgTableRow arg="keepalive-timer" typ="time"></ArgTableRow>
<ArgTableRow arg="restart-timer" typ="time"></ArgTableRow>
</ArgTable>

#### routing/bgp/session/clear

**Conditions:** !smips
**Type:** Command

Clear the session flags. For example, to be able to re-establish a session after the prefix limit is reached "limit-exceeded" flag must be cleared. It can be done by specifying `flag` parameter, which is able to take the following values:

* input-last-notification  
* limit-exceeded  
* output-last-notification  
* refused-cap-opt  
* stopped

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="flag" typ="enum (refused-cap-opt | stopped | limit-exceeded | input-last-notification | output-last-notification)">A flag to be cleared from BGP session.</ArgTableRow>
</ArgTable>

#### routing/bgp/session/dump-saved-advertisements

**Conditions:** !smips
**Type:** Command

 Dump saved advertisements from specified BGP session in the \*.pcap file.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="save-to" typ="string">The filename where to store the PCAP data.</ArgTableRow>
</ArgTable>

#### routing/bgp/session/refresh

**Conditions:** !smips
**Type:** Command

Send route refresh to a specified BGP session. Is used to trigger re-sending all the routes from the remote peer.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="afi" typ="enum (ip | ipv6 | l2vpn | vpnv4)">Specifies for which address family to send route refresh.</ArgTableRow>
</ArgTable>

#### routing/bgp/session/resend

**Conditions:** !smips
**Type:** Command

Resend prefixes to a specified BGP session. The command takes two arguments:

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="afi" typ="enum (ip | ipv6 | l2vpn | vpnv4)">Specifies for which address families to resend prefixes.</ArgTableRow>
<ArgTableRow arg="save-to" typ="string">The name of the pcap file where to dump resent messages, can be used for debugging purposes.</ArgTableRow>
</ArgTable>

#### routing/bgp/session/stop

**Conditions:** !smips
**Type:** Command

### routing/bgp/template

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="routing-table" typ="enum" unset="1">Name of the routing table, to install routes in. Overrides the instance parameter.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1">Name of the VRF BGP connections operate on. By default uses the "main" routing table.</ArgTableRow>
<ArgTableRow arg="templates" typ="multi { enum
 }" unset="1">List of template names that will be used to inherit parameter values from. Useful feature, to easily configure groups with overlapping configuration options.</ArgTableRow>
<ArgTableRow arg="as" typ="as" unset="1">A 32-bit BGP autonomous system number. The value accepts AS-Plain or AS-Dot formats. Override the instance ASN and configure BGP confederation using the following format: _`confederation_as/as`_. For example, if your AS is 34 and your confederation AS is 43, set `as=43/34`.</ArgTableRow>
<ArgTableRow arg="nexthop-choice" typ="enum (default | force-self | propagate)" unset="1">Affect outgoing **NEXT\_HOP** attribute selection. Next-hops set in filters always take precedence and are not changed on route reflection except when set in a filter.   default - select the next-hop as described in [`RFC 4271`](https://tools.ietf.org/html/rfc4271)   force-self - use the local address of the interface that connects to the peer as the next-hop   propagate - propagate received next-hop; if the route has a BGP **NEXT\_HOP** attribute, use it as the next-hop; otherwise, fall back to the default case</ArgTableRow>
<ArgTableRow arg="multihop" typ="bool" unset="1">Enable when the remote peer is more than one hop away.This option affects outgoing next-hop selection as described in [`RFC 4271`](https://tools.ietf.org/html/rfc4271) (for eBGP only, excluding iBGP peers local to the confederation). It also affects:Whether to accept connections from peers not in the same network (the remote address of the connection is used for this check)Whether to accept incoming routes with a NEXT\_HOP attribute not in the same network as the address used to establish the connectionThe target scope of routes installed from this peer; routes from multi-hop or iBGP peers resolve their next-hops through IGP routes by default</ArgTableRow>
<ArgTableRow arg="hold-time" typ="alt { enum (infinity) { infinity:0 }
, time [3 .. 65535]
 }" unset="1">Specifies the BGP Hold Time value to be used when negotiating with peers.According to the BGP specification, if the router does not receive successive **KEEPALIVE** and/or **UPDATE** and/or **NOTIFICATION** messages within the period specified in the Hold Time field of the **OPEN** message, then the BGP connection to the peer will be closed.The minimal `hold-time` value of both peers will be used (note that the special value 0 or 'infinity' is lower than any other value)*   infinity \- never expire the connection and never send keepalive messages.</ArgTableRow>
<ArgTableRow arg="keepalive-time" typ="time" unset="1">The interval between keepalive messages, if not set then by default keepalive is 1/3 of the `hold-time`.</ArgTableRow>
<ArgTableRow arg="afi" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6, evpn)" unset="1">List of address families this peer can exchange routing information. The remote peer must support BGP capabilities optional parameter (they usually do) to negotiate any other address families than IP.</ArgTableRow>
<ArgTableRow arg="cisco-vpls-nlri-len-fmt" typ="enum (auto-bits | auto-bytes | bits | bytes)" unset="1">VPLS NLRI length format type. Used for compatibility with Cisco VPLS. \[\[Read more>>\]\].</ArgTableRow>
<ArgTableRow arg="output.remove-private-as" typ="bool" unset="1">If set, then the BGP **AS-PATH** attribute is removed before sending out route updates if the attribute contains only private AS numbers.The removal process happens before routing filters are applied and before the local, AS number is prepended to the AS path.</ArgTableRow>
<ArgTableRow arg="output.as-override" typ="bool" unset="1">If set, then all instances of the remote peer's AS number in the BGP **AS-PATH** attribute are replaced with the local AS number before sending a route update to that peer. Happens before routing filters and prepend.</ArgTableRow>
<ArgTableRow arg="use-bfd" typ="bool" unset="1">Whether to use the BFD protocol for faster connection state detection.</ArgTableRow>
<ArgTableRow arg="save-to" typ="string" unset="1">Filename to save BGP protocol-specific packet content (Exported PDU) into pcap format. This method allows much simpler peer-specific packet capturing for debugging purposes.</ArgTableRow>
<ArgTableRow arg="output.add-path" typ="ubit (ip, ipv6)" unset="1">Enable sending of additional paths for specified address families (BGP Addpath).</ArgTableRow>
<ArgTableRow arg="output.affinity" typ="enum (main | alone | remote-as | instance | afi | vrf | input)" unset="1">Configure output multicore processing. Read more in [Routing Protocol Multi-core Support](../../user-guides/routing-and-networking-protocols/routing-protocol-multi-core-support.md) article.   **alone** - input and output of each session is processed in its own process, the most likely best option when there are a lot of cores and a lot of peers   **afi, instance, vrf, remote-as** - try to run input/output of new session in process with similar parameters   **main** - run input/output in the main process (could potentially increase performance on single-core even possibly on multicore devices with small amount of cores)   **input** - run output in the same process as input (can be set only for output affinity)</ArgTableRow>
<ArgTableRow arg="output.redistribute" typ="ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, bgp-mpls-vpn, slaac)" unset="1">Enable redistribution of specified route types.</ArgTableRow>
<ArgTableRow arg="output.filter-select" typ="enum" unset="1">Name of the routing select chain to be used for prefix selection. If not specified, then default selection is used.</ArgTableRow>
<ArgTableRow arg="output.filter-chain" typ="enum" unset="1">Name of the routing filter chain to be used on the output prefixes. If the chain is not specified, then BGP by default accepts everything.</ArgTableRow>
<ArgTableRow arg="output.network" typ="enum" unset="1">Name of the address list used to send local networks. The network is sent only if a matching IGP route exists in the routing table and its **ORIGIN** attribute is set to IGP, other distribution methods have **ORIGIN** attribute set to INCOMPLETE.</ArgTableRow>
<ArgTableRow arg="output.network-blackhole" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="output.default-originate" typ="enum (never | if-installed | always)" unset="1">Specifies default route (0.0.0.0/0) distribution method. 'if-installed' option can be used to distribute default route only if corresponding IGP route present in the routing table.</ArgTableRow>
<ArgTableRow arg="output.default-prepend" typ="num" unset="1">How many times to prepend local ASN.</ArgTableRow>
<ArgTableRow arg="output.no-client-to-client-reflection" typ="bool" unset="1">Disable client-to-client route reflection in Route Reflector setups.</ArgTableRow>
<ArgTableRow arg="output.no-early-cut" typ="bool" unset="1">The early cut is the mechanism, to guess (based on default RFC behavior) what would happen with the sent NLRI when received by the remote peer. If the algorithm determines that the NLRI is going to be dropped, a peer will not even try to send it. However such behavior may not be desired in specific scenarios, then this option should be used to disable the early cut feature. Early cut works with eBGP sessions.</ArgTableRow>
<ArgTableRow arg="output.keep-sent-attributes" typ="bool" unset="1">Store in memory sent prefix attributes, required for `dump-saved-advertisements` command to work. By default, sent-out prefixes are not stored to preserve the router's memory. An option should be enabled only for debugging purposes when necessary to see currently advertised prefixes.</ArgTableRow>
<ArgTableRow arg="input.add-path" typ="ubit (ip, ipv6)" unset="1">Accept received additional paths (BGP Addpath) for specified address families.</ArgTableRow>
<ArgTableRow arg="input.attr-error-handling" typ="enum (default | revised)"></ArgTableRow>
<ArgTableRow arg="input.affinity" typ="enum (main | alone | remote-as | instance | afi | vrf)" unset="1">
Configure input multi-core processing. Read more in [Routing Protocol Multi-core Support](../../user-guides/routing-and-networking-protocols/routing-protocol-multi-core-support.md) article.
- **alone** - input and output of each session are processed in its own process, most likely the best option when there are a lot of cores and a lot of peers.
- **afi, instance, vrf, remote-as** - try to run input/output of new session in process with similar parameters.
- **main** - run input/output in the main process (could potentially increase performance on single-core even possibly on multi-core devices with a small amount of cores).
</ArgTableRow>
<ArgTableRow arg="input.filter" typ="enum" unset="1">Name of the routing filter chain to be used on input prefixes. This happens after NLRIs are processed. If the chain is not specified, then BGP by default accepts everything.</ArgTableRow>
<ArgTableRow arg="input.filter-nlri" typ="enum" unset="1">Name of the filter chain that will filter incoming IPv4/IPv6 NLRIs directly before they are  stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session restart.</ArgTableRow>
<ArgTableRow arg="input.allow-as" typ="num" unset="1">Indicates how many times to allow your own AS number in AS-PATH, before discarding a prefix.</ArgTableRow>
<ArgTableRow arg="input.accept-nlri" typ="enum" unset="1">Name of the ipv4/6 address-list. A quick way to filter incoming updates with specific NLRIs. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session restart.</ArgTableRow>
<ArgTableRow arg="input.filter-communities" typ="enum" unset="1">A quick way to filter incoming updates with specific communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.</ArgTableRow>
<ArgTableRow arg="input.filter-ext-communities" typ="enum" unset="1">A quick way to filter incoming updates with specific extended communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.</ArgTableRow>
<ArgTableRow arg="input.filter-large-communities" typ="enum" unset="1">A quick way to filter incoming updates with specific large communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.</ArgTableRow>
<ArgTableRow arg="input.accept-communities" typ="enum" unset="1">A quick way to filter incoming updates with specific communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.</ArgTableRow>
<ArgTableRow arg="input.accept-ext-communities" typ="enum" unset="1">A quick way to filter incoming updates with specific extended communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.</ArgTableRow>
<ArgTableRow arg="input.accept-large-communities" typ="enum" unset="1">A quick way to filter incoming updates with specific large communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.</ArgTableRow>
<ArgTableRow arg="input.filter-unknown" typ="enum" unset="1">A quick way to filter incoming updates with specific "unknown" attributes. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.</ArgTableRow>
<ArgTableRow arg="input.limit-process-routes-ipv4" typ="enum (10 | 100 | 1000 | 10000 | 100000 | 1000000 | 10000000)" unset="1">Try to limit the amount of received IPv4 routes to the specified number. This number does not represent the exact number of routes going to be installed in the routing table by the peer. [BGP session "clear"](#routingbgpsessionclear) command must be used to reset the flag if the limit is reached.</ArgTableRow>
<ArgTableRow arg="input.limit-process-routes-ipv6" typ="enum (10 | 100 | 1000 | 10000 | 100000 | 1000000 | 10000000)" unset="1">Try to limit the amount of received IPv6 routes to the specified number. This number does not represent the exact number of routes going to be installed in the routing table by the peer. BGP session "clear" command must be used to reset the flag if the limit is reached.</ArgTableRow>
</ArgTable>

### routing/bgp/vpls

**Conditions:** !smips
**Type:** Directory

This menu lists all the configured BGP-based VPLS instances. These instances allow the router to advertise VPLS BGP NLRI and indicate that the router belongs to a specific customer VPLS network.

MP-BGP-based autodiscovery and signaling (RFC 4761).

Cisco VPLS BGP-based auto-discovery (draft-ietf-l2vpn-signaling-08).

Support for multiple import/export route target extended communities for BGP-based VPLS (both, RFC 4761 and draft-ietf-l2vpn-signaling-08).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="rd" typ="address (flags=R)" unset="1">Specifies the value that gets attached to VPLS NLRI so that receiving routers can distinguish advertisements that may otherwise look the same. This implies that a unique route-distinguisher for every VPLS must be used. It is not necessary to use the same route distinguisher for some VPLS on all routers forming that VPLS as distinguisher is not used for determining if some BGP NLRI is related to a particular VPLS (Route Target attribute is used for this), but it is mandatory to have different distinguishers for different VPLSes. Accepts 3 types of formats. [Read more>>](../../user-guides/routing-and-networking-protocols/route-distinguisher-and-route-target.md)</ArgTableRow>
<ArgTableRow arg="site-id" typ="num" unset="1">Unique site identifier. Each site must have a unique site-id. A parameter must be set for&nbsp;RFC 4761 style VPLS signaling.</ArgTableRow>
<ArgTableRow arg="cisco-id" typ="address" unset="1">Unique identifier. A parameter must be set for cisco-style VPLS signaling. In most cases this should not be used, any modern software supports RFC 4761 style signaling (see site-id parameter). Parameter is a merge of l2-router-id and RD, for example: 10.155.155.1&amp;6550:123</ArgTableRow>
<ArgTableRow arg="import-route-targets" typ="multi { array-id, address (flags=R)
 }" unset="1">The setting is used to determine if BGP NLRI is related to a particular VPLS, by comparing route targets received from BGP NLRI.</ArgTableRow>
<ArgTableRow arg="export-route-targets" typ="multi { array-id, address (flags=R)
 }" unset="1">The setting is used to tag BGP NLRI with one or more route targets which on the remote side is used by `import-route-targets`.</ArgTableRow>
<ArgTableRow arg="local-pref" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="interface-list" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="pw-type" typ="enum (tagged-ethernet | raw-ethernet | vpls)" unset="1">Pseudowire type (RFC 4447 Section 5.2). By default, `raw-ethernet` is used.</ArgTableRow>
<ArgTableRow arg="pw-l2mtu" typ="num" unset="1">L2MTU value advertised to a remote peer (RFC 4447 Section 5.2).</ArgTableRow>
<ArgTableRow arg="pw-control-word" typ="enum (default | enabled | disabled)" unset="1">Enables or disables Control Word usage (RFC 4623 Section 4). Default values for regular and Cisco-style VPLS tunnels differ. Cisco-style by default has Control Word usage disabled. Read more in the [VPLS Control Word](../../user-guides/routing-and-networking-protocols/mpls/vpls/control-word.md) article.</ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum" unset="1">[Bridge](../interface/bridge.md) the VPLS interface belongs to.</ArgTableRow>
<ArgTableRow arg="bridge-cost" typ="num" unset="1">Cost of the [bridge port](../interface/bridge.md#path-cost).</ArgTableRow>
<ArgTableRow arg="bridge-horizon" typ="num" unset="1">When set to `none`, [bridge horizon](../interface/bridge.md#horizon) is not used.</ArgTableRow>
<ArgTableRow arg="bridge-pvid" typ="num" unset="1">Port VLAN ID (pvid) assigned to a dynamically bridged interface. Applies only when [bridge `vlan-filtering`](../interface/bridge.md#vlan-filtering) is set to `yes`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="current-peers" typ="string"></ArgTableRow>
</ArgTable>

### routing/bgp/vpn

**Conditions:** !smips
**Type:** Directory

L3VPN VPNv4/VPNv6 instance configuration

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="instance" typ="enum" mandatory="1">Name of the instance this VPN is assigned to.</ArgTableRow>
<ArgTableRow arg="route-distinguisher" typ="string" mandatory="1">Specifies the value that gets attached to route so that receiving routers can distinguish advertisements that may otherwise look the same. Used to distinguish between tenants using overlapping IP ranges. Also can be used to simplify convergence and redundancy within Virtual Network. RDs from MLAG pairs should be unique, too.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" mandatory="1">Name of the VRF table that this VPN instance will use.</ArgTableRow>
<ArgTableRow arg="label-allocation-policy" typ="enum (per-vrf | per-prefix)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="import.route-targets" typ="object { address (flags=R)
 }" unset="1">List of route targets that will be used to import VPNv4 routes. The accepted RT format is similar to the one for Route Distinguishers.</ArgTableRow>
<ArgTableRow arg="export.route-targets" typ="object { address (flags=R)
 }" unset="1">List of route targets added when exporting VPNv4 routes. The accepted RT format is similar to the one for Route Distinguishers.</ArgTableRow>
<ArgTableRow arg="import.filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="export.filter-select" typ="enum" unset="1">The name of the `routing/filter/select-chain` that is used to select prefixes to be exported.</ArgTableRow>
<ArgTableRow arg="export.filter-chain" typ="enum" unset="1">The name of the `routing/filter/chain` that is used to filter prefixes before exporting.</ArgTableRow>
<ArgTableRow arg="export.redistribute" typ="ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, slaac)" unset="1">Enable redistribution of specified route types from a VRF to VPNv4.</ArgTableRow>
</ArgTable>
