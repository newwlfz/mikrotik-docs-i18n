# Dynamic DNS

> Dynamic DNS Update Tool enables secure updates to domain name records for dynamic IP addresses using RFC-compliant algorithms, supporting only hmac-md5. It requires BIND DNS server and works with specified properties like IP, DNS server, key, and TTL.

# Dynamic DNS

**Sub-menu:** `/tool/dns-update`

**Standards:** `RFC 2136, RFC 3007`

Dynamic DNS Update Tool gives a way to keep the domain name pointing to a dynamic IP address. It works by sending domain name system update requests to the name server, which has a zone to be updated. Secure DNS updates are also supported.

The DNS update tool supports only one algorithm - **hmac-md5**. It's the only proposed algorithm for signing DNS messages.

:::warning
DNS update tool works only with the BIND server; it will not work with DynDNS, EveryDNS, or any other similar service.
:::

## Properties

| Property | Description |
| :-- | :-- |
| **address** (*IP*; Default: ) | Defines the IP address associated with the domain name. |
| **dns-server** (*IP*; Default: ) | DNS server to send updates to. |
| **key** (*string*; Default: ) | Authorization key to access the server. |
| **key-name** (*string*; Default: ) | Authorization key name (like a username) to access the server. |
| **name** (*string*; Default: ) | Name to attach to the IP address. |
| **ttl** (*integer*; Default: ) | Time to live for the item (in seconds). |
| **zone** (*string*; Default: ) | DNS zone where to update the domain name. |

:::warning
The system clock time on your router can't differ from the DNS server's time by more than 5 minutes. Otherwise, the DNS server will ignore this request.
:::

## Example

To tell the 23.34.45.56 DNS server to (re)associate the mydomain name in the myzone.com zone with the 68.42.14.4 IP address specifying that the name of the key is dns-update-key and the actual key updates:

```ros
[admin@MikroTik] tool> dns-update dns-server=23.34.45.56 name=mydomain \
\... zone=myzone.com address=68.42.14.4 key-name=dns-update-key key=update
```
