# Torch

> MikroTik Torch is a real-time traffic monitoring tool that observes network flow through interfaces, allowing analysis of source/destination addresses, ports, protocols, MACs, VLAN IDs, and DSCP values for troubleshooting.

# Torch

MikroTik Torch is a real-time traffic monitoring tool used to observe traffic flow through a specific interface. It is an essential utility for troubleshooting and analyzing network load in real-time.

Watch our [video about this feature](https://youtu.be/45E2uwI3xhc).

:::warning
Traffic captured by Torch is seen before it is filtered by the Firewall. This means you will see packets that may eventually be dropped by your firewall rules.
:::

```ros
/tool/torch interface=ether1 src-address=0.0.0.0/0 dst-address=0.0.0.0/0
```

You can monitor traffic classified by:

- Source and Destination addresses (IPv4 and IPv6).
- Port and Protocol.
- MAC protocol and MAC address.
- VLAN ID.
- DSCP.

### Usage Example

To monitor HTTP and HTTPS traffic on `ether1` from a specific subnet (interface canbe unnamed parameter):

```ros
/tool/torch ether1 port=80,443 src-address=192.168.88.0/24
```

Torch displays the selected protocols along with the TX/RX data rate for each entry on the chosen interface.

:::warning
Unicast traffic between Wireless clients with client-to-client forwarding enabled will not be visible to the Torch tool. Similarly, packets processed via hardware-offloading on a bridge will not be visible (though unknown unicast, broadcast, and some multicast traffic will remain visible).
:::
