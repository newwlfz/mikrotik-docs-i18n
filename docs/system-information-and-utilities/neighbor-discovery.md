# Neighbor discovery

> Neighbor discovery protocols enable detection of devices using MNDP, CDP, or LLDP in Layer2 domains, displaying connected neighbors' IP/MAC addresses and interfaces. Configuration options include protocol selection, discovery interval adjustments, and LLDP TLVs for QoS and VLAN sharing.

# Neighbor discovery

Neighbor Discovery protocols allow us to find devices compatible with MNDP (MikroTik Neighbor Discovery Protocol), CDP (Cisco Discovery Protocol), or LLDP (Link Layer Discovery Protocol) in the Layer2 broadcast domain. They can be used to map out your network.

## Neighbor list

The neighbor list shows all discovered neighbors in the Layer2 broadcast domain. It shows to which interface the neighbor is connected, its IP/MAC addresses, and other related parameters. The list is read-only. An example of a neighbor list is provided below:

```ros
[admin@MikroTik] /ip/neighbor/print 
 # INTERFACE ADDRESS         MAC-ADDRESS       IDENTITY   VERSION    BOARD      
 0 ether13   192.168.33.2    00:0C:42:00:38:9F MikroTik   5.99       RB1100AHx2
 1 ether11   1.1.1.4         00:0C:42:40:94:25 test-host  5.8        RB1000   
 2 Local     10.0.11.203     00:02:B9:3E:AD:E0 c2611-r1   Cisco I...                    
 3 Local     10.0.11.47      00:0C:42:84:25:BA 11.47-750  5.7        RB750  
 4 Local     10.0.11.254     00:0C:42:70:04:83 tsys-sw1   5.8        RB750G    
 5 Local     10.0.11.202     00:17:5A:90:66:08 c7200      Cisco I...
```

**Sub-menu:** `/ip/neighbor`

| Property | Description |
| :-- | :-- |
| **address** (*IP*) | The highest IP address configured on a discovered device |
| **address6** (*IPv6*) | IPv6 address configured on a discovered device |
| **add-dns-entries** (*yes \| no*) | Specify whether to create dynamic DNS entry for this particular neighbor and use identity as domain name |
| **add-dns-entries-suffix** (*string*) | Suffix added to dynamic DNS entries created for each neighbor. |
| **age** (*time*) | Time interval since last discovery packet |
| **discovered-by** (*cdp\|lldp\|mndp*) | Shows the list of protocols the neighbor has been discovered by. The property is available since RouterOS version 7.7. |
| **board** (*string*) | RouterBoard model. Displayed only for devices with installed RouterOS |
| **identity** (*string*) | Configured system identity |
| **interface** (*string*) | Interface name to which the discovered device is connected |
| **interface-name** (*string*) | Interface name on the neighbor device connected to the L2 broadcast domain. Applies to CDP. |
| **ipv6** (*yes \| no*) | Shows whether the device has IPv6 enabled. |
| **mac-address** (*MAC*) | MAC address of the remote device. Can be used to connect with mac-telnet. |
| **platform** (*string*) | Name of the platform. For example "MikroTik", "cisco", etc. |
| **software-id** (*string*) | RouterOS software ID on a remote device. Applies only to devices installed with RouterOS. |
| **system-caps** (*string*) | System capabilities reported by the Link-Layer Discovery Protocol (LLDP). |
| **system-caps-enabled** (*string*) | Enabled system capabilities reported by the Link-Layer Discovery Protocol (LLDP). |
| **unpack** (*none\|simple\|uncompressed-headers\|uncompressed-all*) | Shows the discovery packet compression type. |
| **uptime** (*time*) | Uptime of remote device. Shown only for devices installed with RouterOS. |
| **version** (*string*) | Version number of installed software on a remote device |
| **running** (string array) | Reports a list of "features" running on the neighbour device. Currently lists only the "CAPsMAN" feature. |

:::warning
The number of neighbor entries is limited to (total RAM in megabytes)\*16 per interface to avoid memory exhaustion.
:::

### LLDP neighbors

LLDP-discovered neighbors are shown in a separate read-only menu under `/ip/neighbor/lldp`. This menu shows detailed LLDP type-length-values (TLVs) received from neighboring devices.

Unlike the general `/ip/neighbor` menu which aggregates neighbors from all discovery protocols (MNDP, CDP, and LLDP), `/ip/neighbor/lldp` shows only LLDP-discovered entries.

Example output:

```ros
[admin@Switch] > /ip/neighbor/lldp/print
Columns: INTERFACE, ADDRESS4, ADDRESS6, MAC-ADDRESS, LLDP-CHASSIS-ID, LLDP-PORT-ID, LLDP-PORT-DESCRIPTION, LLDP-SYSTEM-NAME, LLDP-SYSTEM-DESCRIPTION
#  INTERFACE  ADDRESS4        ADDRESS6                   MAC-ADDRESS        LLDP-CHASSIS-ID    LLDP-PORT-ID  LLDP-PORT-DESCRIPTION  LLDP-SYSTEM-NAME  LLDP-SYSTEM-DESCRIPTION                                                     
0  ether2     192.168.88.128  fe80::f61e:57ff:fe13:d794  F4:1E:57:13:D7:94  F4:1E:57:13:D7:94  ether1        ether1                 Tested_CRS812     MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CRS812-8DS-2DQ-2DDQ 
   bridge1                                                                                                                                                                                                                        
1  ether3     192.168.88.127  fe80::f61e:57ff:fe47:9255  F4:1E:57:47:92:55  F4:1E:57:47:92:55  ether1        ether1                 Tested_CRS520     MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CRS520-4XS-16XQ     
   bridge1                                                                                                                                                                                                                        
2  ether4     192.168.88.9    fe80::1afd:74ff:fe81:9a    18:FD:74:81:00:9A  18:FD:74:81:00:86  ether1        ether1                 Tester6           MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CCR2216-1G-12XS-2XQ 
   bridge1                                                                                                                                                                                                                        
3  ether5     192.168.88.132  fe80::d601:c3ff:fe43:c035  D4:01:C3:43:C0:35  D4:01:C3:43:C0:35  ether1        ether1                 Tested_L009       MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 L009UiGS            
   bridge1                                                                                                                                                                                                                        
4  ether8     192.168.88.129  fe80::f61e:57ff:fec2:8a3d  F4:1E:57:C2:8A:3D  F4:1E:57:C2:8A:2B  ether17       ether17                Tested_CRS418     MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CRS418-8P-8G-2S+    
   bridge1   
```

:::note
The `lldpRemTable` SNMP table reports only neighbors discovered through LLDP. Entries discovered exclusively by CDP or MNDP are excluded from the SNMP LLDP-MIB.
:::

## Discovery configuration

It is possible to change whether an interface participates in neighbor discovery or not using an Interface list. If the interface is included in the discovery interface list, it will send out basic information about the system and process received discovery packets broadcasted in the Layer2 network. Removing an interface from the interface list will disable both the discovery of neighbors on this interface and the possibility of discovering this device itself on that interface.

**Sub-menu:** `/ip/neighbor/discovery-settings`

| Property | Description |
| :-- | :-- |
| **discover-interface-list** (*string*; Default: **static**) | Interface list whose members the discovery protocol will run on. |
| **discover-interval** (*time: 5s..9h6m8s*; Default: **30s**) | Adjusts the frequency at which neighbor discovery packets are transmitted. It also adjusts the Time-to-Live (TTL) TLV value for CDP and LLDP packets using the formula: (`discover-interval` \* 4) + 1. The setting is available since RouterOS version 7.16. |
| **dying-gasp** (*yes \| no*; Default: **no**) | Whether to send a neighbor discovery packet with TTL=0 before a graceful reboot, shutdown, or upgrade. The dying gasp packet is not sent in case of power loss or kernel panic.  On the receiving side, a TTL=0 packet immediately removes the corresponding neighbor entry, regardless of the local `dying-gasp` setting. |
| **lldp-dcbx** (*yes \| no*; Default: **no**) | Whether to send Data Center Bridging Capabilities Exchange Protocol (DCBX) TLVs, which allows to communicate switch [QoS settings](../bridging-and-switching/quality-of-service.md) and capabilities with other neighboring devices using LLDP. Only applies to MikroTik devices with a Marvell Prestera switch (e.g. CRS3xx).  Enabled DCBX includes the following TLVs: ETS (Enhanced Transmission Selection) Configuration TLV. This TLV is used to share the switch's ETS configuration. It includes:The willingness bit, which indicates whether the device is willing to accept QoS configuration from neighboring devices. In RouterOS, the willing bit is set to disabled, meaning the switch will not accept remote configurations and instead uses its own settings.The priority assignment table, which maps priorities to specific traffic-class.The bandwidth allocation table, where RouterOS calculates the percentage of bandwidth allocated to each queue based on the <code>weight</code> property. This applies to queues using the <code>high-priority-group</code> in the <code>`/interface/ethernet/switch/qos/tx-manager/queue`</code> settings.The Transmission Selection Algorithm (TSA) table, where <code>high-priority-group</code> queues are assigned to ETS, <code>strict-priority</code> queues to Strict Priority, and <code>low-priority-group</code> or non-hardware offloaded queues to the Vendor Specific Algorithm.ETS Recommendation TLV. This provides a recommendation on how neighboring devices should configure ETS. RouterOS uses the same data as in the ETS Configuration TLV to give its recommendation.Priority-based Flow Control Configuration TLV. This TLV is used to share PFC configuration. Similar to the ETS TLV, the willingness bit is set to disabled, meaning the switch does not accept remote PFC configurations. PFC is enabled for specific priorities based on settings configured under <code>`/interface/ethernet/switch/qos/priority-flow-control`</code>, and <code>`/interface/ethernet/switch/qos/port`</code>.Application Priority TLV. This TLV is used to communicate how different applications are prioritized in the network.Application VLAN TLV. This TLV is used to share VLAN configurations for applications. RouterOS currently does not support sending values in this TLV and will send an empty VLAN table instead. |
| **lldp-mac-phy-config**(*yes \| no*; Default: **no**) | Whether to send MAC/PHY Configuration/Status TLV in LLDP, which indicates the interface capabilities, current setting of the duplex status, bit rate, and auto-negotiation. Only applies to Ethernet interfaces. While the TLV is optional in LLDP, it is mandatory when sending LLDP-MED, meaning this TLV will be included when necessary even though the property is configured as disabled. |
| **lldp-max-frame-size** (*yes \| no*; Default: **no**) | Whether to send Maximum Frame Size TLV in LLDP, which indicates the maximum frame size capability of the interface in bytes (`l2mtu` + 18). Only applies to Ethernet interfaces. |
| **lldp-med** (*yes \| no*; Default: **yes**) | Specifies whether to advertise the LLDP-MED Media Capabilities TLV. This option must be enabled when `lldp-med-net-policy-vlan` is used. The setting is available since RouterOS version 7.23. |
| **lldp-poe-power** (*yes \| no*; Default: **yes**) | Two specific TLVs facilitate Power over Ethernet (PoE) management between Power Sourcing Equipment (PSE) and Powered Devices (PD): IEEE 802.3 Organizationally Specific Power Via MDI TLVTIA-1057 (LLDP-MED) Organizationally Specific Extended Power via MDI TLV The `lldp-poe-power` attribute determines whether to transmit the IEEE 802.3 Organizationally Specific Power Via MDI TLV in LLDP messages.  The transmission of LLDP-MED Organizationally Specific Extended Power via MDI TLV is not configurable. It is automatically included in outgoing LLDP-MED packets when the remote device has transmitted the LLDP-MED capability of receiving power.  These TLVs are relevant only for Ethernet interfaces that support [PoE-Out](../hardware/poe-out.mdx). The setting is available since RouterOS version 7.15, and it replaces PoE-out port `poe-lldp-enabled` setting. |
| **lldp-med-net-policy-vlan** (*integer 0..4094*; Default: **disabled**) | Advertised VLAN ID for LLDP-MED Network Policy TLV. This allows assigning a VLAN ID for LLDP-MED capable devices, such as VoIP phones. The TLV will only be added to interfaces where LLDP-MED capable devices are discovered and `lldp-med` is enabled. Other TLV values are predefined and cannot be changed: Application Type - VoiceVLAN Type - TaggedL2 Priority - 0DSCP Priority - 0 When used together with the bridge interface, the (R/M)STP protocol should be enabled with the `protocol-mode` setting.  Additionally, other neighbor discovery protocols (e.g. CDP) should be excluded using the `protocol` setting to avoid LLDP-MED misconfiguration. |
| **lldp-vlan-info** (*yes \| no;* Default: **no**) | Whether to send IEEE 802.1 Organizationally Specific TLVs in LLDP related to VLANs.  When this setting is enabled, three TLVs are advertised: Port VLAN ID. This applies to the bridge port's <code>pvid</code> property.Port And Protocol VLAN ID. This TLV is not used and always indicates "not supported" and "not enabled".VLAN Name. This includes up to 10 active VLANs from the "<code>`/interface/bridge/vlan`</code>" table. These TLVs are relevant to interfaces that are added to a [vlan-filtering](../bridging-and-switching/index.md#bridge-vlan-filtering) bridge, and the setting is available since RouterOS version 7.16. |
| **mode** (*rx-only \| tx-only \| tx-and-rx*; Default: **tx-and-rx**) | Selects the neighbor discovery packet sending and receiving mode. The setting is available since RouterOS version 7.7. |
| **protocol** (*cdp \| lldp \| mndp*; Default: **cdp,lldp,mndp**) | List of used discovery protocols. |

Since RouterOS v6.44, neighbor discovery works on individual slave interfaces. Whenever a master interface (e.g. bonding or bridge) is included in the discovery interface list, all its slave interfaces will automatically participate in neighbor discovery. It is possible to allow neighbor discovery only on some slave interfaces. To do that, include the particular slave interface in the list and make sure that the master interface is not included.

```ros
/interface/bonding
add name=bond1 slaves=ether5,ether6
/interface/list
add name=only-ether5
/interface/list/member
add interface=ether5 list=only-ether5
/ip/neighbor/discovery-settings
set discover-interface-list=only-ether5
```

Now the neighbor list shows a master interface and an actual slave interface on which a discovery message was received.

```ros
[admin@R2] > ip neighbor print
 # INTERFACE ADDRESS                                           MAC-ADDRESS       IDENTITY   VERSION    BOARD         
 0 ether5    192.168.88.1                                      CC:2D:E0:11:22:33 R1         6.45.4 ... CCR1036-8G-2S+
   bond1    
```

## LLDP

Depending on RouterOS configuration, different type-length-values (TLVs) can be sent in the LLDP message. This includes:

- Chassis ID (MAC address).
- Port ID (interface name).
- Time To Live.
- System Name (system identity).
- System Description (platform - MikroTik, software version - RouterOS version,  hardware name - RouterBoard name).
- Management Address (all IP addresses configured on the port).
- System Capabilities (enabled system capabilities, e.g. bridge or router).
- Port Description (combined interface name like "bridge/ether1" if the sending interface is part of bridge or bond, or interface name the same as Port ID).
- IEEE 802.1 Port VLAN ID.
- IEEE 802.1 Port And Protocol VLAN ID.
- IEEE 802.1 VLAN Name.
- IEEE 802.3 MAC/PHY Configuration/Status.
- IEEE 802.3 Power Via MDI.
- IEEE 802.3 Maximum Frame Size.
- LLDP-MED Media Capabilities (list of MED capabilities).
- LLDP-MED Network Policy (assigned VLAN ID for voice traffic).
- LLDP-MED Extended Power via MDI.
- End of LLDPDU.
