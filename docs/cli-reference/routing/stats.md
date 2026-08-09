# Stats

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/stats

**Conditions:** !smips
**Type:** Directory

### routing/stats/memory

**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="procid" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="used" typ="num"></ArgTableRow>
<ArgTableRow arg="unused" typ="num"></ArgTableRow>
<ArgTableRow arg="object-size" typ="num"></ArgTableRow>
<ArgTableRow arg="objects" typ="num"></ArgTableRow>
<ArgTableRow arg="unused-objects" typ="num"></ArgTableRow>
<ArgTableRow arg="pages" typ="num"></ArgTableRow>
<ArgTableRow arg="page-slack" typ="num"></ArgTableRow>
<ArgTableRow arg="page-cell-count" typ="num"></ArgTableRow>
</ArgTable>

### routing/stats/origin

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="Y" typ="synthetic">synthetic</ArgTableRow>
<ArgTableRow arg="Z" typ="terminal">terminal</ArgTableRow>
<ArgTableRow arg="X" typ="stopping">stopping</ArgTableRow>
<ArgTableRow arg="A" typ="abandoned">abandoned</ArgTableRow>
<ArgTableRow arg="H" typ="hold">hold</ArgTableRow>
<ArgTableRow arg="U" typ="attrs-updated">attrs-updated</ArgTableRow>
<ArgTableRow arg="M" typ="attrs-merge">attrs-merge</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="string"></ArgTableRow>
<ArgTableRow arg="instance-id" typ="num"></ArgTableRow>
<ArgTableRow arg="dealer-id" typ="num"></ArgTableRow>
<ArgTableRow arg="publisher-idx" typ="num"></ArgTableRow>
<ArgTableRow arg="route-type" typ="string"></ArgTableRow>
<ArgTableRow arg="pid" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="route-count" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="in-policy" typ="num"></ArgTableRow>
<ArgTableRow arg="update.in-policy" typ="num"></ArgTableRow>
<ArgTableRow arg="total-route-count" typ="num"></ArgTableRow>
</ArgTable>

### routing/stats/pcap

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="file" typ="string"></ArgTableRow>
<ArgTableRow arg="timestamp" typ="time"></ArgTableRow>
<ArgTableRow arg="src" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="dst" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="protocol" typ="string"></ArgTableRow>
<ArgTableRow arg="data" typ="string"></ArgTableRow>
<ArgTableRow arg="bgp.type" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp.notification.code" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp.notification.subcode" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp.route-refresh.afi" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp.route-refresh.safi" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp.route-refresh.subtype" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp.update.local-pref" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp.update.med" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp.update.nexthop" typ="multi { address (flags=46)
 }"></ArgTableRow>
<ArgTableRow arg="bgp.update.nlri" typ="multi { address (flags=46i/SR)
 }"></ArgTableRow>
<ArgTableRow arg="bgp.update.withdrawn" typ="multi { address (flags=46i/SR)
 }"></ArgTableRow>
<ArgTableRow arg="bgp.update.origin" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp.update.as-path" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="bgp.update.as4-path" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="bgp.update.communities" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="bgp.update.ext-communities" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="bgp.update.large-communities" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="bgp.update.atomic-aggregate" typ="bool"></ArgTableRow>
<ArgTableRow arg="bgp.update.aggregator" typ="string"></ArgTableRow>
<ArgTableRow arg="bgp.update.as4-aggregator" typ="string"></ArgTableRow>
<ArgTableRow arg="bgp.update.originator-id" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="bgp.update.cluster-list" typ="multi { ipAddr
 }"></ArgTableRow>
</ArgTable>

### routing/stats/process

**Type:** Directory

This menu allows you to monitor debugging information of all the routing processes.

```ros
[admin@rack1_b35_CCR1036] /routing/stats/process> print interval=1
Columns: TASKS, PRIVATE-MEM-BLOCKS, SHARED-MEM-BLOCKS, PSS, RSS, VMS, RETIRED, ID, PID, RPID, PROCESS-TIME, KERNEL-TIME, CUR-BUSY, MAX-BUSY, CUR-CALC, MAX-CALC
 # TASKS                         PRIVATE-  SHARED-ME  PSS        RSS     VMS      RETIRED  ID       PID  RPID  PROCESS  KERNEL-TIME  CUR-BUSY  MAX-BUSY  CUR-CALC  MAX-CALC
 0 routing tables                768.0KiB  1792.0KiB  2399.0KiB  6.4MiB  22.1MiB       34  main     317     0  2s260ms  1s940ms      10ms      170ms     20ms      1s210ms 
   rib                                                                                                                                                                     
 1 fib                           0         0          2263.0KiB  6.2MiB  22.3MiB           fib      351     1  250ms    1s720ms                1s210ms             1s210ms 
 2 ospf                          256.0KiB  256.0KiB   2559.0KiB  6.6MiB  22.3MiB           ospf     384     1  4s710ms  5s210ms                20ms                20ms    
 3 pimsm                         256.0KiB  0          2252.0KiB  5.8MiB  22.3MiB           pim      386     1  200ms    450ms                  10ms                10ms    
 4 fantasy                       0         0          2031.0KiB  5.1MiB  22.3MiB           fantasy  388     1  270ms    390ms                  10ms                10ms    
 5 configuration and reporting   0         512.0KiB   2351.0KiB  6.4MiB  22.3MiB           static   389     1  310ms    430ms                  10ms                10ms    
 6 ldp                           256.0KiB  256.0KiB   2455.0KiB  6.4MiB  22.3MiB           mpls     387     1  340ms    350ms                  40ms                40ms    
   Copy                                                                                                                                                                    
 7 rip                           256.0KiB  0          2230.0KiB  5.7MiB  22.3MiB           rip      377     1  230ms    380ms                  10ms                10ms    
 8 routing policy configuration  512.0KiB  512.0KiB   2355.0KiB  5.6MiB  22.3MiB           policy   358     1  240ms    390ms                  10ms                10ms    
 9 BGP service                   512.0KiB  0          2592.0KiB  6.3MiB  22.3MiB           bgp      364     1  360ms    600ms                  10ms                10ms    
10 BFD service                   256.0KiB  0          2206.0KiB  5.7MiB  22.3MiB           12       371     1  230ms    370ms                  10ms                10ms    
11 BGP Input 111.11.0.1          512.0KiB  512.0KiB   2560.0KiB  6.4MiB  22.3MiB        1  22       679     1  140ms    350ms                  10ms                10ms    
   BGP Output 111.11.0.1                                                                                                                                                   
12 Global memory                           256.0KiB                                        global     0     0  
```

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="A" typ="abandoned">abandoned</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="tasks" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="private-mem-blocks" typ="num"></ArgTableRow>
<ArgTableRow arg="shared-mem-blocks" typ="num"></ArgTableRow>
<ArgTableRow arg="pss" typ="num"></ArgTableRow>
<ArgTableRow arg="rss" typ="num"></ArgTableRow>
<ArgTableRow arg="vms" typ="num"></ArgTableRow>
<ArgTableRow arg="retired" typ="num"></ArgTableRow>
<ArgTableRow arg="id" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="pid" typ="num"></ArgTableRow>
<ArgTableRow arg="rpid" typ="num"></ArgTableRow>
<ArgTableRow arg="task-count" typ="num"></ArgTableRow>
<ArgTableRow arg="process-time" typ="time"></ArgTableRow>
<ArgTableRow arg="kernel-time" typ="time"></ArgTableRow>
<ArgTableRow arg="in-rpc-queue" typ="num"></ArgTableRow>
<ArgTableRow arg="out-rpc-queue" typ="num"></ArgTableRow>
<ArgTableRow arg="cur-busy" typ="time"></ArgTableRow>
<ArgTableRow arg="max-busy" typ="time"></ArgTableRow>
<ArgTableRow arg="cur-calc" typ="time"></ArgTableRow>
<ArgTableRow arg="max-calc" typ="time"></ArgTableRow>
</ArgTable>

#### routing/stats/process/kill

**Type:** Command

### routing/stats/step

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="context" typ="string"></ArgTableRow>
<ArgTableRow arg="pid" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="order" typ="num"></ArgTableRow>
<ArgTableRow arg="runs" typ="num"></ArgTableRow>
<ArgTableRow arg="targets" typ="num"></ArgTableRow>
<ArgTableRow arg="max-time" typ="time"></ArgTableRow>
<ArgTableRow arg="cur-time" typ="time"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (off | on | once)"></ArgTableRow>
<ArgTableRow arg="sched" typ="time"></ArgTableRow>
</ArgTable>
