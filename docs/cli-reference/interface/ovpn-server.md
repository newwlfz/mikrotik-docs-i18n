# Ovpn Server

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/ovpn-server

**Package:** ppp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
<ArgTableRow arg="H" typ="hw-crypto">hw-crypto</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="client-address" typ="string"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="encoding" typ="string"></ArgTableRow>
</ArgTable>

### interface/ovpn-server/monitor

**Package:** ppp
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="caller-id" typ="string"></ArgTableRow>
<ArgTableRow arg="encoding" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="local-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="remote-address" typ="ipAddr"></ArgTableRow>
</ArgTable>

### interface/ovpn-server/server

**Package:** ppp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (ip | ethernet)"></ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (tcp | udp)"></ArgTableRow>
<ArgTableRow arg="netmask" typ="num"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled)"></ArgTableRow>
<ArgTableRow arg="default-profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum"></ArgTableRow>
<ArgTableRow arg="require-client-certificate" typ="bool"></ArgTableRow>
<ArgTableRow arg="tls-version" typ="enum (any | only-1.2)"></ArgTableRow>
<ArgTableRow arg="auth" typ="ubit (sha1, md5, sha256, sha384, sha512, null)"></ArgTableRow>
<ArgTableRow arg="cipher" typ="ubit (blowfish128, aes128-cbc, aes192-cbc, aes256-cbc, aes128-gcm, aes192-gcm, aes256-gcm, null)"></ArgTableRow>
<ArgTableRow arg="reneg-sec" typ="num">Encryption key re-negotiation interval (0 - disabled)</ArgTableRow>
<ArgTableRow arg="redirect-gateway" typ="ubit (disabled, def1, ipv6)">Push 'redirect-gateway def1 ipv6' options to VPN clients</ArgTableRow>
<ArgTableRow arg="push-routes" typ="string"></ArgTableRow>
<ArgTableRow arg="push-routes-ipv6" typ="string"></ArgTableRow>
<ArgTableRow arg="enable-tun-ipv6" typ="bool">Enable ipv6 inside ovpn tunnel</ArgTableRow>
<ArgTableRow arg="tun-server-ipv6" typ="ip6Addr">Server ipv6 address</ArgTableRow>
<ArgTableRow arg="ipv6-prefix-len" typ="num">Prefix length used for tunneled ipv6</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="user-auth-method" typ="enum (pap | mschap2)"></ArgTableRow>
</ArgTable>

#### interface/ovpn-server/server/export-client-configuration

**Package:** ppp
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="server" typ="enum"></ArgTableRow>
<ArgTableRow arg="server-address" typ="string">Public ip address or dns name clients will use to connect to this vpn server</ArgTableRow>
<ArgTableRow arg="ca-certificate" typ="file">CA certificate used by client ovpn configuration</ArgTableRow>
<ArgTableRow arg="client-certificate" typ="file">Client certificate used by client ovpn configuration</ArgTableRow>
<ArgTableRow arg="client-cert-key" typ="file">Client private key used by client ovpn configuration</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="progress" typ="string"></ArgTableRow>
</ArgTable>
