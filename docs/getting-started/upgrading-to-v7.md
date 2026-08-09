# Upgrading to v7

> This page outlines the steps and considerations for upgrading MikroTik RouterOS to version 7, detailing compatibility with features like BGP, OSPF, MPLS, and user manager settings. It highlights mandatory parameters for BGP connections, merged OSPF menus, and cautions about MPLS configuration backups.

# Upgrading to v7

### Introduction

This document describes the recommended steps for upgrading RouterOS to the v7 major release and the possible caveats when doing so.

Upgrading from v6 to v7 happens the same way as upgrading within v6 releases. Please follow the [Upgrade manual](./installation-and-upgrade/upgrade.md) for more detailed steps. If you are currently running RouterOS version 6 or older, we first suggest upgrading to the latest stable or long-term release in v6.

:::info
In most RouterOS setups that run fine with the aforementioned v6 versions, no extra steps are required. Upgrading to v7 will automatically convert the configuration and your device will function right away.

:::

:::note
**Note:** We do not recommend running v7 on hardware that does not have at least 64 MB of RAM.

:::

### Feature list compatibility

As previously stated, nearly all RouterOS systems can use the "Check for updates" functionality and upgrade to v7 in a few clicks, but there are some features, where extra steps may be required:

| Feature | Status |
| :-- | :-- |
| CAPsMAN | OK |
| Interfaces | OK |
| Wireless | OK |
| Bridge/Switching | OK |
| Tunnels/PPP | OK |
| IPv6 | OK |
| BGP | OK, but attention is required  [\*](#bgp)  |
| OSPF | OK, but attention is required [\*\*](#ospf) |
| MPLS | OK, but attention is required [\*\*\*](#mpls) |
| Routing filters | OK, but attention is required [\*\*\*\*](#routing-filters) |
| PIM-SM | See [notes](#notes) |
| IGMP Proxy | OK |
| Tools | OK |
| Queues | OK |
| Firewall | OK |
| HotSpot | OK |
| Static Routing | OK |
| User Manager | See [notes](#notes) |

### Notes

:::danger
The routing protocol configuration upgrade is triggered only once. This means that if a router was downgraded to ROSv6, the configuration was modified and the router got upgraded back to ROSv7, then the resulting configuration is the one that was present before the downgrade. To re-trigger v6 configuration conversion, load a ROSv6 backup with the option `force-v6-to-v7-configuration-upgrade=yes`.

:::

### **BGP**

All known configurations will upgrade from 6.x to 7.x successfully. But keep in mind that there is a complete redesign of the configuration. v7 BGP implementation provides **`connection`**, **`template`** and **`session`** menus.

**`Template`** contains all BGP protocol-related configuration options. It can be used as a template for dynamic peers and to apply a similar config to a group of peers. Most of the parameters are similar to the previous implementation except that some are grouped in the output and input sections, making the config more readable and easier to understand whether the option is applied on input or output.

The BGP **`connection`** minimal set of parameters is `remote.address`, `template, connect`, `listen` and `local.role`  
Connect and listen parameters specify whether peers will try to connect and listen to a remote address or just connect or just listen. It is possible that in setups where a peer uses the multi-hop connection `local.address` must be configured too. Peer role is now a mandatory parameter. For basic setups, you can just use ibgp, ebgp.

Now you can monitor the status of all connected and disconnected peers from `/routing/bgp/session` menu.  
Other great debugging information on all routing processes can be monitored from `/routing/stats` menu.

Networks are added to the firewall address-list and referenced in the BGP **`connection`** configuration.

### OSPF

All known configurations will upgrade from 6.x to 7.x successfully.  
OSPFv2 and OSPFv3 are now merged into one single menu `/routing/ospf`. At the moment there are no default instances and areas. To start OSPF you need to create an instance and then add an area to the instance.

RouterOSv7 uses templates to match the interface against the template and apply configuration from the matched template. OSPF menus `interface` and `neighbor` contain read-only entries for status monitoring.

### MPLS

Upgrade MPLS setups with caution, and make sure to back up the configuration before the upgrade.

### Routing filters

All supported options are upgraded without any issue, in the case of an unsupported option - an empty entry is created. The routing filter configuration is changed to a script-like configuration.

The rule now can have "if .. then" syntax to set parameters or apply actions based on conditions from the "if" statement.

Multiple rules without action are stacked in a single rule and executed in order like a firewall, the reason is that the "set" parameter order is important, and writing one "set" per line allows for an easier understanding from top to bottom on what actions were applied.

More RouterOSv7 routing filter examples are [here](../user-guides/routing-and-networking-protocols/moving-from-rosv6-to-rosv7.md#routing-filters).

### PIM-SM

Upgrading RouterOS to v7 will not preserve PIM-related configuration. After the upgrade, multicast routing configuration will be available under the `/routing/pimsm` menu and an additional "multicast" package is not required anymore. More information is available [here](../user-guides/routing-and-networking-protocols/multicast/pim-sm.md).

### User Manager

RouterOSv7 provides the new and redesigned implementation of User Manager, configuration is now integrated into RouterOS WinBox and console (WEB admin configuration interface is not available), more information is available [here](../authentication-authorization-accounting/user-manager.md). Direct migration from the older User Manager is not possible, it is possible to migrate the older database from `/user-manager/database/migrate-legacy-db`. However, it might be a good idea to start configuration from scratch.

### New features

A New Kernel is implemented in RouterOSv7, which leads to performance changes due to route cache, as well as some tasks might require higher CPU and RAM usage for different processes.

- Completely new NTP client and server implementation.
- Merged individual packages, only bundle and a few extra packages remain *(dropped support for LCD and KVM packages)*.
- New Command Line Interface (CLI) style (RouterOS v6 commands are still supported).
- Support for Let's Encrypt certificate generation.
- Support for REST API.
- Support for UEFI boot mode on x86.
- CHR FastPath support for "vmxnet3" and "virtio-net" drivers.
- Support for "Cake" and "FQ\_Codel" type queues.
- Support for IPv6 NAT.
- Support for Layer 3 hardware acceleration, QoS, and MLAG on MikroTik devices with Marvell Prestera switch.
- Support for MBIM driver with basic functionality support for all modems with MBIM mode.
- Support for VRRP grouping and connection tracking data synchronization between nodes.
- Support for Virtual eXtensible Local Area Network (VXLAN).
- Support for L2TPv3.
- Support for OpenVPN UDP transport protocol.
- Support for WireGuard.
- Support for hardware offloaded VLAN filtering on RTL8367 (RB4011, RB100AHx4) and MT7621 (hEX, hEX S, RBM33G) switches.
- Support for ZeroTier on ARM and ARM64 devices.
- Support for CPU frequency scaling for x86 devices.

### Dropped support

In RouterOS v7, support has been dropped for:

- LCD package
- KVM package
