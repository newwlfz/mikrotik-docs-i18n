# IP packing

> IP Packing enables packet aggregation and compression on network links in RouterOS, requiring symmetric configuration with discovery protocol enabled. It supports different actions like simple aggregation or compression of headers and payload, with warnings about potential latency increases.

# IP packing

IP Packing provides a packet packaging service on network links. It allows simple packet aggregation into larger packets and compression of the contents of packets.

## Requirements

Packet packing is part of the system package and has to have a discovery protocol enabled on an interface.

### Configuration

**Sub-menu:** `/ip/packing`

It is required to have a configuration in two places, both routers should be set up symmetrically:

- `/ip/packing`- to enable packet aggregation and/or compression on an interface.
- `/ip/neighbor/discovery-settings` to enable discovery  protocol on the interface.

### Packing configuration

| Property | Description |
| :-- | :-- |
| aggregated-size (*20 .. 16384 default:**1500***) | size of an aggregated packet that packing will try to achieve before sending a packet over the network |
| disabled (*yes\|no*) | state of the packing rule, if a value is *yes* it will be ignored and will not be part of the active configuration |
| interface (*interface name*) | packing will try to aggregate and/or compress packets from this interface |
| packing (*simple\|compress-all\|compress-headers\|none*) | the action it should perform when a packet is leaving the interface the packing rule is configured on:<code>simple</code> - do just aggregate packets<code>compress-all</code> - do aggregation and attempt to compress headers and payload of a packet<code>compress-headers</code> - do aggregation and attempt to compress headers and leave the payload of a packet as is<code>none</code> - send packets as is |
| unpacking (*simple\|compress-all\|compress-headers\|none*) | the action that should be performed when a packet is received on the interface the packing rule is configured on:<code>simple</code> - unpack received packets from aggregated packets received from the interface<code>compress-all</code> - unpack aggregated packet and uncompress headers and payload of a packet<code>compress-headers </code>- unpack aggregated packets and decompress headers of a packet<code>none</code> - do nothing with a received packet |

:::danger
The router should be seen as a neighbor of the router over the interface you want to enable packing on. If in the neighbor list there is no entry indicating packing, packing is not working!

**Warning:** Packing may increase latency on the link it is configured on.
:::

## Example

Router-A and Router-B are connected with a cable with interface ether1 on Router-A and ether3 on Router-B. This example will aggregate packets coming from Router-A, but will leave packets from Router-B intact. On Router-A:

Make sure discovery is enabled:

```ros
 /ip/neighbor/discovery/set ether1 discover=yes 
```

Add a packing rule for the interface:

```ros
 /ip/packing/add interface=ether1 aggregated-size=1500 packing=simple unpacking=none 
```

On Router-B:

Make sure discovery is enabled:

```ros
 /ip/neighbor/discovery/set ether3 discover=yes 
```

Add a packing rule for the interface:

```ros
 /ip/packing/add interface=ether3 aggregated-size=1500 packing=none unpacking=simple
```
