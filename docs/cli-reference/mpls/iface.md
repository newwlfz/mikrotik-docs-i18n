# Iface

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## mpls/interface

**Conditions:** !smips
**Type:** Directory

Configuration of MPLS MTU (path MTU + MPLS tag size) is useful in cases when there is a large variety of possible MTUs along the path. Configuring MPLS MTU to a minimum value that can pass all the hops will ensure that the MPLS packet will not be silently dropped on the devices that do not support a big enough MTU.

```ros
[admin@rack1_b35_CCR1036] /mpls/interface> print 
Flags: X - disabled; * - builtin 
 0    ;;; router-test
      interface=ether1 mpls-mtu=1580 input=yes 

 1    ;;; router-test
      interface=ether2 mpls-mtu=1580 input=yes 

 2    interface=all mpls-mtu=1500  
```

If interface is not matched by any entry in the list, then mpls MTU will be equal to interface's L2MTU.

:::info
Listed entries are ordered, and the first entry (iterating from the top to the bottom) that matches the interface will be used.
:::

The order of the entries is important due to the possibility that different interface lists can contain the same interface and in addition, that interface can be referenced directly.

Selection of the MPLS MTU happens in the following manner:

- If the interface matches the entry from this table, then try to use the configured MPLS MTU value.
- If the interface does not match any entry then consider MPLS MTU equal to L2MTU.
- If the interface does not support L2MTU, then consider MPLS MTU equal to L3 MTU.

On the MPLS ingress path, MTU is chosen by min(MPLS MTU - tagsize, l3mtu). This means that on interfaces that do not support L2MTU and the default L3 MTU is set to 1500, max path MTU will be 1500 - tag size (the interface will not be able to pass a full IP frame without fragmentation). In such scenarios, L3MTU must be increased by the max observed tag size.

Read more on MTUs in the [MTU in RouterOS](../../hardware/mtu-in-routeros.md) article.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="*" typ="builtin"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="enum ()" mandatory="1">Name of the interface or interface-list to match.</ArgTableRow>
<ArgTableRow arg="mpls-mtu" typ="num" unset="1">The option represents how big packets can be carried over the interface with added MPLS labels</ArgTableRow>
<ArgTableRow arg="input" typ="bool" unset="1">Whether to allow MPLS input on the interface.</ArgTableRow>
</ArgTable>
