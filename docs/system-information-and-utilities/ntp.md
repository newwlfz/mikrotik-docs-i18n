# NTP

> RouterOS documentation for NTP covers client and server configurations including enabled modes, server lists with IPv4/IPv6 support, VRF settings, authentication keys, and status monitoring like frequency drift and synced stratum. It also warns about using local clock for precision timing and lists NTP log messages.

# NTP

The RouterOS main package includes Network Time Protocol (NTP) client and server functionality, which is based on RFC5905.

### NTP Client properties

Client configuration is located in `/system/ntp/client`

| Property | Description |
| :-- | :-- |
| **enabled** (*yes, no default: no*) | Enable NTP client for time synchronization |
| **mode** (*broadcast, manycast, multicast, unicast*) | Mode that the NTP client will operate in |
| **NTP servers** | The list of NTP servers. It is possible to add static entries.  The following formats are accepted:  - FQDN ("Resolved Address" will appear in the "Servers" window in an appropriate column if the address is resolved) or IP address can be used. If DHCP-Client property **use-peer-ntp=yes** - the dynamic entries advertised by [DHCP](../network-management/dhcp.md)  - *ipv4*  - *ipv4*`@`*vrf*  - *ipv6*  - *ipv6*`@`*vrf*  - *ipv6-linklocal*`%`*interface* |
| **vrf** (*default: main*) | Virtual Routing and Forwarding |
| **Servers** (*Button/Section*) | A detailed table of dynamically and statically added NTP servers (Address, Resolved address, Min Poll, Max Poll, iBurst, Auth. Key)  To set the NTP server using its FQDN. The domain name will be resolved each time an NTP request is sent. The Router has to have *`/ip/dns`* configured. |
| **Peers** | Current parameter values  `[admin@ntp-example_v7] > /system/ntp/monitor-peers``type="ucast-client" address=x.x.x.x refid="y.y.y.y" stratum=3 hpoll=10 ppoll=10 root-delay=28.869 ms root-disp=50.994 ms``offset=-0.973 ms delay=0.522 ms disp=15.032 ms jitter=0.521 ms``-- [Q quit  D dump  C-z pause]` |
| **Keys** | NTP symmetric keys, used for authentication between the NTP client and server. Key Identifier (Key ID) - an integer identifying the cryptographic key used to generate the message-authentication code.  |

#### Status

- **synchronized, stopped, waiting, using-local-clock** - Current status of the NTP client.
- **Frequency drift** - The fractional frequency drift per unit time.
- **synced-server** - The IP address of the NTP Server.
- **synced-stratum** - The accuracy of each server is defined by a number called the stratum, with the topmost level (primary servers) assigned as one and each level downwards (secondary servers) in the hierarchy assigned as one greater than the preceding level.
- **system-offset** - This is a signed, fixed-point number indicating the offset of the NTP server's clock relative to the local clock, in seconds.

### NTP Client Servers properties

Client configuration is located in `/system/ntp/client/servers`

| Property | Description |
| :-- | :-- |
| **enabled** (*yes \| no; Default: yes*) | Enables the NTP client server. |
| **comment** (*string;* Default: ) | Descriptive name of an item. |
| **address** (IPv4 address [IPv4]*, IPv6 address [IPv6],* Domain name; Default: ) | IP address or domain name of the NTP server. |
| **resolved-address** (IPv4 address [IPv4]*, IPv6 address [IPv6]; Default:* ) | Actual IP address of the NTP server, obtained after domain name resolution. |
| **min-poll** (*integer:* 3..17; Default: 6) | Determines the shortest interval (powers of 2, in seconds) between NTP queries. More detailed information can be found in [RFC5905](https://www.rfc-editor.org/rfc/rfc5905.html). |
| **max-poll** (*integer*: 3..17; Default: 10) | Determines the longest interval (powers of 2, in seconds) between NTP queries. More detailed information can be found in [RFC5905](https://www.rfc-editor.org/rfc/rfc5905.html). |
| **iburst**(*yes \| no; Default: yes*) | Determines if initial burst is disabled or enabled. IBurst tells the NTP client to send a rapid burst of packets only at startup. More detailed information can be found in [RFC5905](https://www.rfc-editor.org/rfc/rfc5905.html). |
| **auth-key** (default value: *none*) | NTP symmetric key, used for authentication between the NTP client and server. Key Identifier (Key ID) - an integer identifying the cryptographic key used to generate the message-authentication code. |

### NTP Server settings

Server configuration is located in `/system/ntp/server`

| Property | Description |
| :-- | :-- |
| **enabled** (*yes* or *no*; default value: *no*) | Enable NTP server |
| **broadcast** (*yes* or *no*; default value: *no*) | Enable a certain NTP server mode, for this mode to work you have to set up the broadcast-addresses field |
| **multicast** (*yes* or *no*; default value: *no*) | Enable a certain NTP server mode |
| **manycast** (*yes* or *no*; default value: *no*) | Enable a certain NTP server mode |
| **broadcast-addresses** (*IP address*; default value: ) | Set the broadcast address to use for NTP server broadcast mode |
| **vrf** (*default: main*) | Virtual Routing and Forwarding |
| **use-local-clock** (*yes* or *no*; default value: *no*) | The server will supply its local system time as valid if others are not available. |
| **local-clock-stratum** | Manually set the stratum if **use-local-clock=yes** |
| **auth-key** (default value: *none*) | NTP symmetric key, used for authentication between the NTP client and server. Key Identifier (Key ID) - an integer identifying the cryptographic key used to generate the message-authentication code. |

:::danger
If you use use-local-clock, then be aware that the router's internal CPU clock is not a reliable time source for precise timing operations, as its frequency may vary due to power management, thermal conditions, and hardware differences, even between identical models. This variation is expected and does not affect normal router performance. For accurate timekeeping, it is recommended to use network-based time synchronisation, such as NTP (Network Time Protocol).
:::

### Log messages

The SNTP client can produce the following log messages. See the article "[log](../diagnostics-monitoring-and-troubleshooting/log/index.md)" on how to set up logging and how to inspect logs.

- **ntp**,**debug** Gradually adjust by *OFFS*.
- **ntp**,**debug** Instantly adjust by *OFFS*.
- **ntp**,**debug** Wait for *N* seconds before sending the next message.
- **ntp**,**debug** Wait for *N* seconds before restarting.
- **ntp**,**debug**,**packet** Packet received an error, restarting.
- **ntp**,**debug**,**packet** Received *PKT*.
- **ntp**,**debug**,**packet** Ignoring received *PKT*.
- **ntp**,**debug**,**packet** Error sending to *IP*, restarting.
- **ntp**,**debug**,**packet** Sending to *IP* *PKT*.

#### Explanation of log message fields

- *OFFS* - Difference of two NTP timestamp values, in hexadecimal.
- *PKT* - Dump of an NTP packet. If the packet is shorter than the minimum 48 bytes, it is dumped as a hexadecimal string. Otherwise, the packet is dumped as a list of field names and values, one per log line. Names of fields follow RFC4330.
- *IP* - Remote IP address.

**NOTE**: The above logging rules work only with the built-in SNTP client; the separate NTP package doesn't have any logging facilities.
