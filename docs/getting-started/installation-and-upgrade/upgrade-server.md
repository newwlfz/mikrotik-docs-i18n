# Upgrade Server

> Learn how RouterOS connects to the MikroTik upgrade server to check for and download new versions, and how to troubleshoot connectivity issues.

When you check for updates, RouterOS contacts `upgrade.mikrotik.com` to determine the latest available version for your device and license tier. If the server cannot be reached or the DNS name does not resolve, the upgrade check fails or returns outdated information.

## How the Upgrade Check Works

The RouterOS package update mechanism performs the following steps:

1. The device sends a request to `upgrade.mikrotik.com`, including the current RouterOS version, architecture, and license level.
2. The server matches this information against the release chain you have selected (Long term, Stable, Testing, or Development) and returns the latest compatible version.
3. If a newer version is available, the device downloads the corresponding `.npk` packages directly from the same server.

## Troubleshooting

If the device does not detect an available upgrade, verify that it can resolve and reach the upgrade server.

### Check DNS resolution

Run the following command to verify that the device resolves the server address:

```ros
:put [:resolve upgrade.mikrotik.com]
```

The result should be `159.148.147.251`. If the address does not resolve or resolves to a different IP, review your DNS settings. See the [DNS](../../network-management/dns.md) article for more information.

### Check server reachability

Once DNS resolution is confirmed, verify that the device can reach the server:

```ros
/tool/ping address=159.148.147.251
```

If the ping fails, check your firewall rules, routing, or upstream connectivity. The device must be able to reach the server on port 443 (HTTPS) to download packages.
