# IP Scan

> The IP Scan tool in RouterOS scans networks for active devices, collecting IP addresses, MAC addresses, response times, DNS names, SNMP strings, and NET-BIOS names. It can scan by IPv4 prefix or interface listening, with warnings against conflicting settings.

# IP Scan

IP Scan tool allows a user to scan networks based on some network prefix or by setting an interface to listen on. Either way, the tool collects certain data from the network:

- address - IP address of a network device.
- mac-address - MAC address of a network device.
- time - response time of the seen network device when found.
- DNS - DNS name of a network device.
- SNMP - SNMP name of the device.
- NET-BIOS  - NET-BIOS name of the device if advertised by the device.

When using the IP scan tool the user must choose what they want to scan for:

- A certain IPv4 prefix - the tool will attempt to scan all the IP addresses or addresses set.
- The interface of the router - the tool will attempt to listen for packets that are "passing by" and attempt to compile results when something is found.

:::danger
There is a possibility to set both but then results may be inconclusive!
:::

## Quick Example

The `/tool/ip-scan` utility is an essential diagnostic tool for users to discover active hosts within a specific IP range. It is particularly useful for identifying unauthorized devices, verifying IP address assignments, or mapping out a network segment when documentation is missing. By sending ICMP and ARP requests, it provides a real-time overview of reachable addresses, their associated MAC addresses, and even SNMP identity strings for compatible devices.

This tool is frequently utilized during initial site audits or when troubleshooting connectivity issues in a dynamic DHCP environment. By running a scan across a local subnet, you can quickly correlate physical hardware with logical IP addresses to detect IP conflicts or rogue access points. This visibility is crucial for maintaining network integrity and ensuring that all connected infrastructure matches the intended deployment topology.

In the following example, we will scan the devices on 10.155.126.0/24 network:

```ros
[admin@MikroTik] > /tool/ip-scan address-range=10.155.126.1-10.155.126.255
Columns: ADDRESS, MAC-ADDRESS, TIMe, SNMP
  ADDRESS         MAC-ADDRESS        TIM  SNMP     
  10.155.126.1    E4:8D:8C:1C:D3:18  2ms  CCR1036-8G-2S+
  10.155.126.251                     2ms           
  10.155.126.151  E4:8D:8C:49:49:DB  1ms           
  10.155.126.153  6C:3B:6B:48:0E:8B  1ms  750Gr3         
  10.155.126.249  CC:2D:E0:8D:01:88  0ms  CRS328-24P-4S+   
  10.155.126.250  B8:69:F4:B3:1B:D2  0ms           
  10.155.126.252  6C:3B:6B:ED:83:69  0ms           
  10.155.126.253  6C:3B:6B:ED:81:83  0ms
```
