# IPIP

> IPIP (IP-in-IP) is a tunneling protocol in RouterOS for secure point-to-point connections over IP networks, supporting IPv4 encapsulation and interoperability with other platforms. It offers basic configuration options like MTU, keepalive, and DSCP settings, with warnings about lack of encryption.

# IPIP

IPIP (IP-in-IP) is a simple tunneling protocol defined in RFC 2003 that encapsulates IP packets within another IP header to transport traffic between two endpoints. In RouterOS, IPIP can be used to create point-to-point tunnels between routers across intermediate IP networks.

An IPIP tunnel interface is represented as a virtual interface in the interface list and can be configured similarly to other logical interfaces. The protocol is supported by various networking platforms, including RouterOS, Linux, and Cisco devices, enabling interoperability between different vendors.

IPIP is commonly used to connect remote networks over public or private IP infrastructure without requiring direct Layer 2 connectivity. The protocol supports encapsulation of IPv4 traffic and is often used as a lightweight tunneling mechanism where encryption is not required.

Typical use cases for IPIP include tunneling private networks over the internet, establishing routed links between remote sites, and providing an alternative to source routing in network designs. Because IPIP does not provide encryption, authentication, or traffic integrity protection, it is commonly combined with IPsec when secure transport is required.

**Sub-menu:** `/interface/ipip`

## Properties

| Property | Description |
| :-- | :-- |
| **clamp-tcp-mss** (*yes \| no*; Default: **yes**) | Controls whether to change the MSS size for received TCP SYN packets. When enabled, a router will change the MSS size for received TCP SYN packets if the current MSS size exceeds the tunnel interface MTU (taking into account the TCP/IP overhead). The received encapsulated packet will still contain the original MSS, and only after decapsulation the MSS is changed. |
| **dont-fragment** (*inherit \| no*; Default: **no**) | Whether to include the DF bit in related packets:  *no* - fragment if needed, *inherit* - use the Don't Fragment flag of the original packet.  (Without Don't Fragment: inherit - packet may be fragmented). |
| **dscp** (*inherit \| integer [0-63]*; Default: ) | Set the dscp value in the IPIP header to a fixed value or inherit the dscp value taken from tunnelled traffic. |
| **ipsec-secret** (*string*; Default: ) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | When secret is specified, the router adds a dynamic ipsec peer to remote-address with a pre-shared key and a policy with default values (by default phase2 uses sha1/aes128cbc). |
| **local-address** (*IP*; Default: ) | IP address on a router that will be used by the IPIP tunnel. |
| **mtu** (*integer*; Default: **1480**) | Layer3 Maximum transmission unit. |
| **keepalive** (*integer[/time],integer 0..4294967295*; Default: **10s,10**) | The keepalive parameter sets the time interval in which the tunnel running flag will remain set even if the remote end of the tunnel goes down. If the configured time and retries fail, the interface running flag is removed. Parameters are written in the following format: `KeepaliveInterval,KeepaliveRetries` where KeepaliveInterval is the time interval and KeepaliveRetries - the number of retry attempts. By default, keepalive is set to 10 seconds and 10 retries. To disable, set `/interface/ipip/set ipip1 keepalive=no`. |
| **name** (*string*; Default: ) | Interface name. |
| **remote-address** (*IP*; Default: ) | IP address of the remote end of IPIP tunnel. |

:::warning
There is no authentication or 'state' for this interface. The bandwidth usage of the interface may be monitored with the monitor feature from the interface menu.
:::

## Example

 Suppose we want to add an IPIP tunnel between routers R1 and R2:

![](/docs/virtual-private-networks/img/ipip-01.webp)

At first, we need to configure IPIP interfaces and then add IP addresses to them.
  
The configuration for router **R1** is as follows:

```ros
[admin@MikroTik] /interface/ipip> add
local-address: 10.0.0.1
remote-address: 22.63.11.6
[admin@MikroTik] /interface/ipip> print
Flags: X - disabled, R - running
# NAME MTU LOCAL-ADDRESS REMOTE-ADDRESS
0 X ipip1 1480 10.0.0.1 22.63.11.6

[admin@MikroTik] /interface/ipip> en 0
[admin@MikroTik] /interface/ipip> /ip/address/add address=1.1.1.1/24 interface=ipip1
```

The configuration of the **R2** is shown below:

```ros
[admin@MikroTik] /interface/ipip> add local-address=22.63.11.6 remote-address=10.
0.0.1
[admin@MikroTik] /interface/ipip> print
Flags: X - disabled, R - running
# NAME MTU LOCAL-ADDRESS REMOTE-ADDRESS
0 X ipip1 1480 22.63.11.6 10.0.0.1

[admin@MikroTik] /interface/ipip> enable 0
[admin@MikroTik] /interface/ipip> /ip/address/add address=1.1.1.2/24 interface=ipip1
```

Now both routers can ping each other:

```ros
[admin@MikroTik] /interface/ipip> /ping 1.1.1.2
1.1.1.2 64 byte ping: ttl=64 time=24 ms
1.1.1.2 64 byte ping: ttl=64 time=19 ms
1.1.1.2 64 byte ping: ttl=64 time=20 ms
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 19/21.0/24 ms
[admin@MikroTik] /interface/ipip>
```
