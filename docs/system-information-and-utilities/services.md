# Services

> This page documents the IP/Services section in MikroTik RouterOS, detailing default services like Telnet, FTP, SSH, and WinBox along with their configuration properties such as address restrictions, ports, TLS versions, and session limits. It provides examples for managing service access control.

# Services

IP/Services lists the protocols and ports used by various MikroTik RouterOS services and containers, including those for incoming connections.

It helps to determine which MikroTik services (or containers) are listening on specific ports, and what needs to be blocked or allowed if you want to restrict or permit access to certain services.

The default services that can be configured from the IP/Services section:

| Property | Description |
| :-- | :-- |
| **telnet** | Telnet service |
| **ftp** | FTP service |
| **www** | WebFig HTTP service |
| **ssh** | SSH service |
| **www-ssl** | WebFig HTTPS service |
| **api** | API service |
| **winbox** | Responsible for WinBox tool access, as well as MikroTik smartphone app and Dude |
| **api-ssl** | API over SSL service |
| **reverse-proxy** | Reverse Proxy service |

## Properties

Note that it is not possible to add new services, only existing service modifications are allowed.

**Sub-menu:** `/ip/service`

| Property | Description |
| :-- | :-- |
| **address** (*IP address/netmask \| IPv6/0..128*; Default: ) | List of IP/IPv6 prefixes from which the service is accessible. When this parameter is set, packets are not dropped at the network level, but access to the service is denied for sources not matching the specified addresses. This option is best suited for restricting access within trusted networks.  To block access from external or untrusted networks, we recommend using a Firewall instead. |
| **certificate** (*name*; Default: **none**) | The name of the certificate used by a particular service. Applicable only for services that depend on certificates (*www-ssl, api-ssl*) |
| **name** (*name*; Default: **none**) | Service name |
| **max-sessions**(*integer: 1..1000*; Default: 20) | Max simultaneous session count for service |
| **port** (*integer: 1..65535*; Default: ) | The port a particular service listens on |
| ***tls-version*** (*any* \| *only-1.2*; Default: **any**) | Specifies which TLS versions to allow by a particular service |
| **vrf** (*name*; Default: **main**) | Specifies which VRF instance to use by a particular service |

### Read-only properties

| Property | Description |
| :-- | :-- |
| **Container** | Name of the container listening on the port |
| **Local** | Router local address used for the connection |
| **Remote** | Remote address that established the connection to the service |

### Example

For example, allow API only from a specific IP/IPv6 address range

```ros
[admin@dzeltenais_burkaans] /ip/service/set api address=10.5.101.0/24,2001:db8:fade::/64
[admin@dzeltenais_burkaans] /ip/service/print where !dynamic      
Flags: X - DISABLED, I - INVALID
Columns: NAME, PORT, PROTO, ADDRESS, CERTIFICATE, VRF, MAX-SESSIONS
 #   NAME     PORT  PROTO  ADDRESS             CERTIFICATE  VRF   MAX-SESSIONS
 0   ftp        21  tcp                                     main            20
 1   ssh        22  tcp                                     main            20
 2   telnet     23  tcp                                     main            20
 7   www        80  tcp                                     main            20
 9 X www-ssl   443  tcp                        none         main            20
13   winbox   8291  tcp                                     main            20
15   api      8728  tcp    10.5.101.0/24                    main            20
                           2001:db8:fade::/64                                 
16   api-ssl  8729  tcp                        none         main            20
```

Example that shows dynamic services that listen or have established connections to router services

```routeros
[admin@dzeltenais_burkaans] /ip/service/print where dynamic  
Flags: D - DYNAMIC; c - CONNECTION
Columns: NAME, NETNS, CONTAINER, PORT, PROTO, LOCAL, REMOTE
 #    NAME        NETNS  CONTAINER  PORT  PROTO  LOCAL         REMOTE            
 3 D  resolver                        53  tcp                                    
 4 D  resolver                        53  udp                                    
 5 D  dhcp                            67  udp                                    
 6 D  dhcpclient                      68  udp                                    
 8 D  snmp                           161  udp                                    
10 D  btest                         2000  tcp                                    
11 D  loader                        3986  tcp                                    
12 D  discover                      5678  udp                                    
14 Dc winbox                        8291  tcp    10.155.221.4  10.145.221.15:51595
17 D  pihole-FTL     16  Pi-hole      53  tcp                                    
18 D  pihole-FTL     16  Pi-hole      53  udp                                    
19 D  lighttpd       16  Pi-hole      80  tcp                                    
28 Dc lighttpd       16  Pi-hole      80  tcp    172.55.1.2    10.145.221.15:52298
29 Dc lighttpd       16  Pi-hole      80  tcp    172.55.1.2    10.145.221.15:52333
30 Dc lighttpd       16  Pi-hole      80  tcp    172.55.1.2    10.145.221.15:52339
31 Dc lighttpd       16  Pi-hole      80  tcp    172.55.1.2    10.145.221.15:52340
32 Dc lighttpd       16  Pi-hole      80  tcp    172.55.1.2    10.145.221.15:52341
33 Dc lighttpd       16  Pi-hole      80  tcp    172.55.1.2    10.145.221.15:52342
26 D  pihole-FTL     16  Pi-hole    4711  tcp
```

## Protocols and ports

The table below shows the list of protocols and ports used by RouterOS.

| Proto/Port | Description |
| :-- | :-- |
| **20/tcp** | FTP data connection |
| **21/tcp** | FTP control connection |
| **22/tcp** | Secure Shell (SSH) remote login protocol |
| **23/tcp** | Telnet protocol |
| **53/tcp 53/udp** | DNS |
| **67/udp** | Bootstrap protocol or [DHCP Server](../network-management/dhcp.md#dhcp-server) |
| **68/udp** | Bootstrap protocol or [DHCP Client](../network-management/dhcp.md#dhcp-client) |
| **80/tcp** | World Wide Web HTTP |
| **123/udp** | Network Time Protocol ([NTP](./ntp.md) |
| **161/udp** | Simple Network Management Protocol ([SNMP](../diagnostics-monitoring-and-troubleshooting/snmp.md) |
| **179/tcp** | Border Gateway Protocol ([BGP](../user-guides/routing-and-networking-protocols/unicast/bgp/index.md) |
| **443/tcp** | Secure Socket Layer (SSL) encrypted HTTP |
| **500/udp** | Internet Key Exchange (IKE) protocol |
| **520/udp 521/udp** | [RIP](../user-guides/routing-and-networking-protocols/unicast/rip.md) routing protocol |
| **546/udp** | [DHCPv6 Client](../network-management/dhcp.md) message |
| **547/udp** | [DHCPv6 Server](../network-management/dhcp.md) message |
| **646/tcp** | [LDP](../user-guides/routing-and-networking-protocols/mpls/ldp.md) transport session |
| **646/udp** | [LDP](../user-guides/routing-and-networking-protocols/mpls/ldp.md) hello protocol |
| **1080/tcp** | [SOCKS](../network-management/socks/index.md) proxy protocol |
| **1698/udp 1699/udp** | RSVP TE Tunnels |
| **1701/udp** | Layer 2 Tunnel Protocol ([L2TP](../virtual-private-networks/l2tp/index.md)) |
| **1723/tcp** | Point-To-Point Tunneling Protocol ([PPTP](../virtual-private-networks/pptp.md)) |
| **1900/udp 2828/tcp** | Universal Plug and Play ([uPnP](../firewall-and-quality-of-service/upnp.md)) |
| **1966/udp** | MME originator message traffic |
| **1966/tcp** | MME gateway protocol |
| **2000/tcp** | Bandwidth test server |
| **5246,5247/udp** | [CAPsMAN](../wireless/abgn/capsman/ap-controller-capsman.md) |
| **5350/udp** | NAT-PMP client |
| **5351/udp** | NAT-PMP server |
| **5678/udp** | Mikrotik Neighbor Discovery Protocol |
| **6343/tcp** | Default OpenFlow port |
| **8080/tcp** | HTTP Web Proxy |
| **8291/tcp** | [Winbox](../management-tools/winbox.md) |
| **8728/tcp** | [API](../developer-guides/api/index.md) |
| **8729/tcp** | API-SSL |
| **20561/udp** | MAC winbox |
| **/1** | ICMP |
| **/2** | [Multicast | IGMP](../Multicast%20Routing%20Protocols/igmp-proxy) |
| **/4** | [IPIP](../virtual-private-networks/ipip.md) encapsulation |
| **/41** | IPv6 (encapsulation) |
| **/46** | RSVP TE tunnels |
| **/47** | General Routing Encapsulation (GRE) - used for PPTP and [EoIP](../virtual-private-networks/eoip.md) tunnels |
| **/50** | Encapsulating Security Payload for IPv4 (ESP) |
| **/51** | Authentication Header for IPv4 (AH) |
| **/89** | [OSPF](../user-guides/routing-and-networking-protocols/unicast/ospf/index.md) routing protocol |
| **/103** | [Multicast | PIM](../Multicast%20Routing%20Protocols/pim-sm) |
| **/112** | [VRRP](../high-availability-solutions/vrrp.md) |

## Web server

The table below shows the list of properties that can be enabled/disabled for web services. All of properties are enabled by default and can be disabled if desired.

In this table "plain" refers to HTTP connections and "secure" to HTTPS connections.

| Property | Description |
| :-- | :-- |
| index-plain: (Default: **yes**) | Home page/login page (Can be disabled when webfig-plain and graphs-plain are disabled) |
| webfig-plain: (Default: **yes**) | WebFig interface |
| graphs-plain: (Default: **yes**) | Graph page |
| rest-plain: (Default: **yes**) | REST API support |
| crl-plain: (Default: **yes**) | CRL(Certificate Revocation List) |
| scep-plain: (Default: **yes**) | SCEP(Simple Certificate Enrollment Protocol) |
| acme-plain: (Default: **yes**) | ACME Challenge |
| index-secure: (Default: **yes**) | Home page/login page (Can be disabled when webfig-secure and graphs-secure are disabled) |
| webfig-secure: (Default: **yes**) | WebFig interface |
| graphs-secure: (Default: **yes**) | Graph page |
| rest-secure: (Default: **yes**) | REST API support |
