# Openflow

> RouterOS supports OpenFlow protocols 1.0 and 1.3 for SDN integration, enabling centralized traffic management via controller applications that access switch data paths. It includes basic statistics support and requires careful configuration to avoid disrupting regular networking when using OpenFlow-enabled interfaces.

# Openflow

RouterOS supports OpenFlow [1.0](https://opennetworking.org/wp-content/uploads/2013/04/openflow-spec-v1.0.0.pdf) and [1.3](https://opennetworking.org/wp-content/uploads/2014/10/openflow-spec-v1.3.0.pdf) which allows communication between the OpenFlow controller and the OpenFlow agent.

OpenFlow is used to centralize management of network equipment in Software Defined Networks (SDNs).

Applications on the OpenFlow controller have access to the switch's data-path and can perform custom tasks, like flow steering, traffic monitoring etc.

Controller sends flows to be added in the agent's flow table. Packet lookup, modification and forwarding are done based on the flow table on the agent.

RouterOS supports OpenFlow fastpath in simple setups where " goto table" flows are not used.

OpenFlow feature overrides regular packet processing functionality - packets that are received on interfaces that are OpenFlow switch ports will not pass through the regular networking stack unless OpenFlow controller sets up flows that enable this. Due to this, care must be taken to not disable access to the device when configuring OpenFlow.

OpenFlow support is available as a standalone openflow package.

### Currently supported basic capabilities

- OFPC\_FLOW\_STATS
- OFPC\_TABLE\_STATS
- OFPC\_PORT\_STATS
- OFPC\_GROUP\_STATS

### Currently unsupported basic capabilities

- OFPC\_IP\_REASM
- OFPC\_QUEUE\_STATS
- OFPC\_PORT\_BLOCKED

### Currently not supported configuration parameters and actions (version 1)

- OFPAT\_SET\_NW\_SRC
- OFPAT\_SET\_NW\_DST
- OFPAT\_SET\_NW\_TOS
- OFPAT\_SET\_TP\_SRC
- OFPAT\_SET\_TP\_DST
- OFPAT\_ENQUEUE
- OFPAT\_VENDOR

### Currently not supported configuration parameters and actions (version 1.3)

- OFPT\_SET\_ASYNC
- OFPAT\_SET\_NW\_TTL
- OFPAT\_DEC\_NW\_TTL
- OFPAT\_COPY\_TTL\_OUT
- OFPAT\_COPY\_TTL\_IN

## Configuration Example

The example demonstrates very basic L2 untagged packet forwarding between sfp-sfplus1-2 ports. Faucet is used as a controller.

```routeros
/openflow
add controllers=tcp/10.155.101.182/6653 datapath-id=1/DC:2C:6E:A4:B4:2E disabled=no name=faucet

/openflow/port
add disabled=no interface=sfp-sfpplus1 port-id=1 switch=faucet
add disabled=no interface=sfp-sfpplus2 port-id=2 switch=faucet
```

:::info
If you intend to also use Gauge, then add Gauge's IP and port  in the controllers list. Example, where 6654 is the Gauge port: `controllers=tcp/10.155.101.182/6653,tcp/10.155.101.182/6654`
:::

Faucet configuration. dp\_id must be the same as datapath-id from ROS configuration in hex format ( 1/DC:2C:6E:A4:B4:2E →  0x0001dc2c6ea4b42e ):

```routeros
---
vlans:
    100:
        description: "untagged"

acls:
    1:
        - rule:
            actions:
                allow: 1

dps:
    test_switch:
        dp_id: 0x0001dc2c6ea4b42e
        hardware: "Generic"
        drop_broadcast_source_address: false
        drop_spoofed_faucet_mac: false
        interfaces:
            1:
                name: "h1"
                description: "host1 container"
                native_vlan: 100
                acl_in: 1
            2:
                name: "h2"
                description: "host2 container"
                native_vlan: 100
                acl_in: 1

```

Faucet installed flows can be seen from the `/openflow/flow` menu:

```routeros
[admin@CCR2004_2XS_111] /openflow/flow>  print detail 
Flags: I - inactive 
 0   switch=faucet version=4 match=" [ { ethdst_m=01000cccccccffffffffffff } ]" actions=" []" 
     info="priority 8240, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 1   switch=faucet version=4 match=" [ { ethdst_m=01000ccccccdffffffffffff } ]" actions=" []" 
     info="priority 8240, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 2   switch=faucet version=4 match=" [ { ethdst_m=ffffffffffffffffffffffff }; { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1; max_len=0 } }; { output={ port=2; max_len=0 } } ] 
        } ]" 
     info="priority 8240, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 3   switch=faucet version=4 match=" [ { ethdst_m=0180c2000000fffffffffff0 } ]" actions=" []" 
     info="priority 8236, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 4   switch=faucet version=4 match=" [ { ethdst_m=0180c2000000ffffff000000 }; { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1; max_len=0 } }; { output={ port=2; max_len=0 } } ] 
        } ]" 
     info="priority 8216, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 5   switch=faucet version=4 match=" [ { ethdst_m=01005e000000ffffff000000 }; { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1; max_len=0 } }; { output={ port=2; max_len=0 } } ] 
        } ]" 
     info="priority 8216, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 6   switch=faucet version=4 match=" [ { ethdst_m=333300000000ffff00000000 }; { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1; max_len=0 } }; { output={ port=2; max_len=0 } } ] 
        } ]" 
     info="priority 8208, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 7   switch=faucet version=4 match=" [ { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1; max_len=0 } }; { output={ port=2; max_len=0 } } ] 
        } ]" 
     info="priority 8192, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 8   switch=faucet version=4 match=" []" actions=" []" 
     info="priority 0, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 9   switch=faucet version=4 match=" []" actions=" [ { goto=4 } ]" 
     info="priority 0, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=3 

10   switch=faucet version=4 match=" [ { ethtype=9000 } ]" actions=" []" 
     info="priority 20490, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=2 

11   switch=faucet version=4 match=" [ { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { output={ port=4294967293; max_len=96 } } ] }; { goto=3 } ]" 
     info="priority 4096, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=2 

12   switch=faucet version=4 match=" []" actions=" [ { goto=3 } ]" 
     info="priority 0, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=2 

13   switch=faucet version=4 match=" [ { inport=00000001 }; { vlanvid=0000 } ]" 
     actions=" [ { apply-actions= [ { pushvlan={ ethertype=33024 } }; { setfield={ vlanvid=1064 } } ] }; { goto=2 } ]" 
     info="priority 4096, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=1 

14   switch=faucet version=4 match=" [ { inport=00000002 }; { vlanvid=0000 } ]" 
     actions=" [ { apply-actions= [ { pushvlan={ ethertype=33024 } }; { setfield={ vlanvid=1064 } } ] }; { goto=2 } ]" 
     info="priority 4096, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=1 

15   switch=faucet version=4 match=" []" actions=" []" 
     info="priority 0, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=1 

16   switch=faucet version=4 match=" [ { inport=00000001 } ]" actions=" [ { goto=1 } ]" 
     info="priority 20480, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=0 

17   switch=faucet version=4 match=" [ { inport=00000002 } ]" actions=" [ { goto=1 } ]" 
     info="priority 20480, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=0 

18   switch=faucet version=4 match=" []" actions=" []" 
     info="priority 0, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=0 

19   switch=faucet version=4 match=" [ { ethdst=dc2c6ec5a7ff }; { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1; max_len=0 } } ] } ]" 
     info="priority 8192, idletimeout 413, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=3 

20   switch=faucet version=4 match=" [ { inport=00000001 }; { ethsrc=dc2c6ec5a7ff }; { vlanvid=1064 } ]" 
     actions=" [ { goto=3 } ]" info="priority 8191, idletimeout 0, hardtimeout 263, cookie 1524372928, removenotify 0" 
     table-id=2 

21   switch=faucet version=4 match=" [ { ethdst=dc2c6e46f893 }; { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=2; max_len=0 } } ] } ]" 
     info="priority 8192, idletimeout 417, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=3 

22   switch=faucet version=4 match=" [ { inport=00000002 }; { ethsrc=dc2c6e46f893 }; { vlanvid=1064 } ]" 
     actions=" [ { goto=3 } ]" info="priority 8191, idletimeout 0, hardtimeout 267, cookie 1524372928, removenotify 0" 
     table-id=2 

```

Statistics of the flows can be seen with the **`stats`** parameter:

```routeros
[admin@CCR2004_2XS_111] /openflow/flow>  print stats 
Columns: SWITCH, MATCH, BYTES, PACKETS, DURATION
 # SWITCH  MATCH                                                                BYTES  PACKETS  DURATION  
 0 faucet   [ { ethdst_m=01000cccccccffffffffffff } ]                            3590       25  6m26s890ms
 1 faucet   [ { ethdst_m=01000ccccccdffffffffffff } ]                               0        0  6m26s890ms
 2 faucet   [ { ethdst_m=ffffffffffffffffffffffff }; { vlanvid=1064 } ]          5552       26  6m26s890ms
 3 faucet   [ { ethdst_m=0180c2000000fffffffffff0 } ]                            4917       25  6m26s890ms
 4 faucet   [ { ethdst_m=0180c2000000ffffff000000 }; { vlanvid=1064 } ]             0        0  6m26s890ms
 5 faucet   [ { ethdst_m=01005e000000ffffff000000 }; { vlanvid=1064 } ]             0        0  6m26s890ms
 6 faucet   [ { ethdst_m=333300000000ffff00000000 }; { vlanvid=1064 } ]          5992       25  6m26s890ms
 7 faucet   [ { vlanvid=1064 } ]                                                  340        5  6m26s890ms
 8 faucet   []                                                                      0        0  6m26s890ms
 9 faucet   []                                                                  20391      106  6m26s890ms
10 faucet   [ { ethtype=9000 } ]                                                    0        0  6m26s890ms
11 faucet   [ { vlanvid=1064 } ]                                                  530        8  6m26s890ms
12 faucet   []                                                                      0        0  6m26s890ms
13 faucet   [ { inport=00000001 }; { vlanvid=0000 } ]                           39135      463  6m26s890ms
14 faucet   [ { inport=00000002 }; { vlanvid=0000 } ]                           37936      459  6m26s890ms
15 faucet   []                                                                  17941      100  6m26s890ms
16 faucet   [ { inport=00000001 } ]                                             48664      515  6m26s890ms
17 faucet   [ { inport=00000002 } ]                                             46348      507  6m26s890ms
18 faucet   []                                                                      0        0  6m26s890ms
19 faucet   [ { ethdst=dc2c6ec5a7ff }; { vlanvid=1064 } ]                       28340      408  6m26s780ms
20 faucet   [ { ethdst=dc2c6e46f893 }; { vlanvid=1064 } ]                       28340      408  6m26s780ms
21 faucet   [ { inport=00000001 }; { ethsrc=dc2c6ec5a7ff }; { vlanvid=1064 } ]  12020      142  2m660ms   
22 faucet   [ { inport=00000002 }; { ethsrc=dc2c6e46f893 }; { vlanvid=1064 } ]  10769      133  1m55s660ms
```

## Statistics

Fastpath statistics can be seen from `/openflow/print fast-path`. We can see that in this example fast path is not functional due to the complexity of flows Faucet is installing.

```routeros
[admin@CCR2004_2XS_111] /openflow> print fast-path 
  openflow-fast-path-packets: 0 0
    openflow-fast-path-bytes: 0 0
```

Port statistics can be seen from the `/openflow/port` menu

```routeros
[admin@CCR2004_2XS_111] /openflow/port> print stats
Columns: INTERFACE, PORT-ID, RX-BYTES, TX-BYTES, RX-PACKETS, TX-PACKETS
# INTERFACE     PORT-ID  RX-BYTES  TX-BYTES  RX-PACKETS  TX-PACKETS
0 sfp-sfpplus1        1    115668     81180        1223        1035
1 sfp-sfpplus2        2    112200     82188        1215        1037
```

## Reference

### General

**Sub-menu:** `/openflow`

This menu lists the configuration of OpenFlow clients.

| Property | Description |
| :-- | :-- |
| **certificate** (*name*) | [Certificate from certificate store](../authentication-authorization-accounting/certificates.md). Used together with the `verify-peer` parameter. |
| **controllers** (*list of [protocol/address/port]*) | Configuration of the connection to the controller. Supported protocols are **tcp** and **tls**. Example: tcp/1.2.3.4/6654 |
| **datapath-id** (*number/mac*) | Datapath ID consisting of two parts (integer number [0..65535] and MAC address) separated by a slash. |
| **name** (*string*) | Reference name of the entry |
| ****passive-port**** (*disabled \| integer [1..65535]*) |  |
| **verify-peer** (*if-cert-present \| none \| required*) | Verify peer's identity against the router’s [certificate store](../authentication-authorization-accounting/certificates.md). |
| ****version**** (*1 \| 1.3 \| default*) | Version of the OpenFlow standard to be used. |

#### Read-Only Parameters

| Property | Description |
| :-- | :-- |
| **openflow-fast-path-bytes** (*integer*) | Number of bytes set to fastpath |
| **openflow-fast-path-packets** (*integer*) | Number of packets sent to fastpath |

### Flows

**Sub-menu:** `/openflow/flow`

This menu lists installed flows responsible for packet forwarding between openflow ports.

| Property | Description |
| :-- | :-- |
| **actions** (*string*) | Action string |
| **bytes** (*integer*) | Number of bytes matched by the rule |
| **duration** (*time*) |  |
| **inactive** (*yes \| no*) |  |
| **info** (*string*) | Info string |
| **match** (*string*) | Matcher rule string |
| **packets** (*integer*) | Number of packets matched by the rule |
| **switch** (*name*) | Controller name that installed the rule |
| **table-id** (*integer*) | ID of the table where the rule is located |
| **version** (*integer*) |  |

### Groups

**Sub-menu:** `/openflow/group`

| Property | Description |
| :-- | :-- |
| **bucket-count** () |  |
| **bucket-stats** () |  |
| **buckets** () |  |
| **bytes** (*integer*) |  |
| **duration** (*time*) |  |
| **flow-count** (*integer*) |  |
| **id** (*integer*) |  |
| **inactive** (*yes \| no*) |  |
| **packets** (*integer*) |  |
| **switch** (*name*) |  |
| **type** () |  |

### Meter

**Sub-menu:** `/openflow/meter`

 The sub-menu displays installed traffic meters by the controller. Meters allow the rate-monitoring before the output and apply action instructions.

| Property | Description |
| :-- | :-- |
| **band-count** () |  |
| **bands** () |  |
| **bytes** (*integer*) | Number of accounted bytes |
| **duration** (*time*) |  |
| **id** (*integer*) |  |
| **inactive** (*yes \| no*) |  |
| **packets** (*integer*) | Number of accounted packets |
| **switch** (*name*) | Controller name that installed the rule |

### Ports

**Sub-menu:** `/openflow/port`

This menu lists the ports controlled by OpenFlow.

| Property | Description |
| :-- | :-- |
| **interface** (*name*) | Name of the interface to be controlled by OpenFlow |
| **port-id** (*integer*) | Port ID used to identify the interface in flow rules |
| **switch** (*name*) | Name of the switch that will be able to control the port. |

#### Read-Only Parameters

| Property | Description |
| :-- | :-- |
| **rx-bytes** (*integer*) | Amount of bytes received on the interface |
| **rx-packets** (*integer*) | Number of packets received on the interface |
| **tx-bytes** (*integer*) | Amount of bytes transmitted on the interface |
| **tx-packets** (*integer*) | Number of packets transmitted on the interface |
