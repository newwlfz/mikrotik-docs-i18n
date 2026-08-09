# Pool

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/pool

**Type:** Directory

IP pools are used to define a range of IP addresses that can be used by various RouterOS utilities, for example, DHCP server, Point-to-Point servers and more. Separate lists for IPv4 and IPv6 are available. Whenever possible, the same IP address is given out to each client (OWNER/INFO pair).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the pool.</ArgTableRow>
<ArgTableRow arg="ranges" typ="multi { , , ipRange
 }" mandatory="1">IP address list of non-overlapping IP address ranges in the form of: `from1-to1,from2-to2,...,fromN-toN`. For example, `10.0.0.1-10.0.0.27,10.0.0.32-10.0.0.47`.</ArgTableRow>
<ArgTableRow arg="next-pool" typ="enum (none)">When IP address acquisition is performed from a pool that has no free addresses, and the next-pool property is set, then an IP address will be acquired from the next pool.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="total" typ="num"></ArgTableRow>
<ArgTableRow arg="used" typ="num"></ArgTableRow>
<ArgTableRow arg="available" typ="num"></ArgTableRow>
</ArgTable>

### ip/pool/used

**Type:** Directory

Menu lists all used IP addresses from IP pools.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="pool" typ="enum">Name of the IP pool.</ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr">IP address that is assigned to a client from the pool.</ArgTableRow>
<ArgTableRow arg="owner" typ="string">Name of the service which acquired this IP address.</ArgTableRow>
<ArgTableRow arg="info" typ="string">Additional info, for example, for DHCP - MAC address from the leases menu and for PPP - connections username of a PPP type client.</ArgTableRow>
</ArgTable>
