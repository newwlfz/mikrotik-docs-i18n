# Reverse Proxy

> Reverse proxy service on MikroTik RouterOS allows routing HTTPS traffic to servers or apps using a simple URL instead of NAT rules, with configurable IP/port and SNI settings, but requires disabling default www-ssl service on port 443.

# Reverse Proxy

Reverse proxy is a service that allows the router to send HTTPS traffic to servers or to RouterOS containers/apps when "use-https" parameter is enabled in app settings, behind the router using a simple URL, instead of an IP address and creating a separate destination NAT rule.

:::danger
Please note that by default, the reverse-proxy service uses HTTPS port 443, same as the default www-ssl service port. For reverse-proxy to function correctly you need to ensure that www-ssl service is disabled or uses a different TCP port. ([/ip/service documentation](../../system-information-and-utilities/services.md)
:::

### Property Description

**Sub-menu:** `/ip/reverse-proxy`

| Property | Description |
| :-- | :-- |
| **disabled** (*yes* \| *no*; Default: **yes**) | Whether the reverse proxy record is active. |
| **ip-address**(IPv4/IPv6; Default: **0.0.0.0** ) | IP address of the server, connection to which should be proxied. |
| **port**(integer: 0..65535; Default: **0**) | Listening port of the server. |
| **sni** (string; Default: ) | Server Name Indication of the server. |
| **certificate**(certificate; Default: **none**) | The name of the [certificate](../../authentication-authorization-accounting/certificates.md) used by a particular reverse-proxy instance. When set to **none**, the reverse-proxy instance will use the certificate from the reverse-proxy service set in the `/ip/service` menu. |
| **vrf** (name; Default:main ) | The Virtual Routing and Forwarding instance to be used. |
| **comment**(string; Default: ) | Descriptive name of an item. |
