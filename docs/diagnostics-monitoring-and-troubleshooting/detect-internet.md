# Detect Internet

> Detect Internet is a RouterOS tool that categorizes monitored interfaces into states like Internet, WAN, LAN, and unknown, with warnings about DHCP client installation and state transitions based on link status and cloud reachability.

# Detect Internet

Detect Internet is a tool that categorizes monitored interfaces into the following states - **Internet**, **WAN**, **LAN**, **unknown**, **slave**, and **no-link**.

:::warning
Note that Detect Internet can install DHCP clients, default routes, DNS servers and affect other facilities.
Use with caution, and after enabling the service, check how it interferes with your other configuration.
:::

### State

This submenu displays the status of all monitored interfaces defined by the *detect-interface-list* parameter:

```ros
/interface/detect-internet/state/print
```

### LAN

All layer 2 interfaces initially have this state.

### WAN

Any L3 tunnel and LTE interfaces will initially have this state. Layer 2 interfaces can obtain this state if the following conditions are met:

- An interface has an active route to 8.8.8.8 in the main routing table.
- An interface can obtain (dynamic DHCP client is created) or has obtained an address from DHCP (does not apply if the DHCP server is also running Detect Internet on the DHCP server interface).

:::warning
WAN interface can fall back to LAN state only when link status changes. LAN interfaces get locked to LAN after 1h and then change only when link status changes.
:::

### Internet

*WAN* interfaces that can reach cloud.mikrotik.com using UDP protocol port 30000 can obtain this state. Reachability is checked every 2 minutes. By default, if the cloud is not reached for 4 minutes, the state falls back to **WAN**.

## Configuration

**Sub-menu:** `/interface/detect-internet`

| Property | Description |
| :-- | :-- |
| **detect-interface-list** (*interface list*; Default: **none**) | All interfaces in the list will be monitored by Detect Internet |
| **internet-interface-list** (*interface list*; Default: **none**) | Interfaces with state Internet will be dynamically added to this list |
| **lan-interface-list** (*interface list*; Default: **none**) | Interfaces with state Lan will be dynamically added to this list |
| **wan-interface-list** (*interface list*; Default: **none**) | Interfaces with state Wan will be dynamically added to this list |
| **request-interval**(time; Default: **2m**) | Time interval between checks of interface status |

```ros
[admin@MikroTik] > /interface/detect-internet/print 
detect-interface-list: none
lan-interface-list: none
wan-interface-list: none
internet-interface-list: none
[admin@MikroTik] > /interface/detect-internet/set internet-interface-list=all wan-interface-list=all lan-interface-list=all detect-interface-list=all 
[admin@MikroTik] > /interface/detect-internet/state/print 
Columns: NAME, STATE, STATE-CHANGE-TIME, CLOUD-RTT
# NAME STATE STATE-CHANGE-TIME CLO
0 ether1 internet 2020-12-22 13:46:18 5ms
```
