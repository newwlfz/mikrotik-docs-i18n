# Socksify

> Socksify enables routing specific traffic through a SOCKS proxy server, allowing applications without native proxy support to use one. It supports multiple services and can be configured with firewall filters for precise traffic management, including examples using TOR.

# Socksify

[*Socksify CLI Reference*](../../cli-reference/ip/socksify)

Socksify is a service that allows the router to send specific traffic through a SOCKS proxy server, even if the application itself does not natively support proxy connections.  
It intercepts network calls and redirects them through a configured SOCKS proxy.

Socksify service is used in combination with [NAT](../../firewall-and-quality-of-service/firewall/nat.md) action=`socksify`. All available firewall filters can be used to precisely select only per-application/source traffic to be redirected via socks proxy.

Multiple Socksify services can be configured simultaneously, which allows connections to multiple SOCKS servers for better traffic management.

### Property Description

**Sub-menu:** `/ip/socksify`

| Property | Description |
| :-- | :-- |
| **disabled** (*yes* \| *no*; Default: yes) | Whether the Socksify record is active. |
| **socks5-password** (*string*; Default: ) | Password for the SOCKS5 proxy server access. |
| **socks5-user**(*string*; Default: ) | Username for the SOCKS5 proxy server access. |
| **connection-timeout** (*integer:* 0..3000; Default: 60) | Time in seconds that specifies how long to wait for the SOCKS proxy or destination to respond during connection setup before aborting with an error. Setting this value to 0 disables the connection timeout. |
| **name**(*string*; Default: ) | Name of the Socksify service. |
| **socks5-port**(*integer*: 1..65535; Default: 1080) | Listening port of the SOCKS5 proxy server. |
| **socks5-server**(*IPv4;* Default: 0.0.0.0 ) | IP address of the SOCKS5 proxy server. (only IPv4 addresses are supported) |
| **port** (*integer*: 1..65535; Default: 952) | TCP port which will be used by the Socksify service. |

## Configuration examples

### Use in combination with TOR SOCKS5 proxy server

Socksify can be used in combination with TOR to achieve better privacy and anonymity for an application that does not have integrated SOCKS support.  
The configuration below will allow you to forward HTTP/s traffic through the TOR SOCKS5 proxy server.  
First you will need to configure the socksify service.

```ros
/ip/socksify 
add connection-timeout=10 disabled=no name=TOR_socksify socks5-port=9050 socks5-server=<TOR_SOCKS_proxy_IP>
```

After that you will need to configure the firewall to ensure that the correct traffic is being socksified and the socks traffic is allowed.

```ros
/ip/firewall/filter
add action=accept chain=input dst-port=952 protocol=tcp src-address=<SOCKS_client_IP> 
/ip/firewall/nat
add action=socksify chain=dstnat dst-port=80,443 protocol=tcp socksify-service=TOR_socksify src-address=<SOCKS_client_IP> 
```

### TOR container and secure DNS tutorial

Since RouterOS supports running containers, you could also set up the Tor proxy in a container. In addition to that, if you are going to be using Tor for browsing the web, you should consider protecting your DNS requests.

For detailed, step-by-step instructions watch the video [here](https://www.youtube.com/watch?v=ECRjxpb5IgE&lc=Ugy6V6EEAwyu2UC8ZJB4AaABAg).
