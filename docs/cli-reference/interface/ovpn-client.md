# Ovpn Client

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/ovpn-client

**Package:** ppp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
<ArgTableRow arg="H" typ="hw-crypto">hw-crypto</ArgTableRow>
<ArgTableRow arg="Ta" typ="tls-auth">tls-auth</ArgTableRow>
<ArgTableRow arg="Tc" typ="tls-crypt">tls-crypt</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="connect-to" typ="address (flags=D46v)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (ip | ethernet)"></ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (tcp | udp)"></ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="verify-server-certificate" typ="bool"></ArgTableRow>
<ArgTableRow arg="tls-version" typ="enum (any | only-1.2)"></ArgTableRow>
<ArgTableRow arg="auth" typ="enum (sha1 | md5 | sha256 | sha384 | sha512 | null)"></ArgTableRow>
<ArgTableRow arg="cipher" typ="enum (blowfish128 | aes128-cbc | aes192-cbc | aes256-cbc | aes128-gcm | aes192-gcm | aes256-gcm | null)"></ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="enum (no | yes | exclusively)"></ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool"></ArgTableRow>
<ArgTableRow arg="route-nopull" typ="bool">If enabled client will not use any routes pushed by server (including def1)</ArgTableRow>
<ArgTableRow arg="disconnect-notify" typ="bool {  }">Send explicit disconnect notification when using UDP mode</ArgTableRow>
</ArgTable>

### interface/ovpn-client/import-ovpn-configuration

**Package:** ppp
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="file-name" typ="file">.ovpn client configuration file</ArgTableRow>
<ArgTableRow arg="skip-cert-import" typ="bool">Ignore certificate information in ovpn file in case these are added by user manualy</ArgTableRow>
<ArgTableRow arg="key-passphrase" typ="string"></ArgTableRow>
<ArgTableRow arg="ovpn-user" typ="string"></ArgTableRow>
<ArgTableRow arg="ovpn-password" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="progress" typ="string"></ArgTableRow>
</ArgTable>

### interface/ovpn-client/monitor

**Package:** ppp
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="encoding" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="local-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="remote-address" typ="ipAddr"></ArgTableRow>
</ArgTable>
