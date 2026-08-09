# Dot1x

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/dot1x

**Conditions:** !smips
**Type:** Directory

### interface/dot1x/client

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="eap-methods" typ="multi { enum (eap-tls | eap-ttls | eap-peap | eap-mschapv2) { eap-tls:13, eap-ttls:21, eap-peap:25, eap-mschapv2:26 }
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="identity" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="anon-identity" typ="string"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

### interface/dot1x/server

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum {  }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="accounting" typ="bool"></ArgTableRow>
<ArgTableRow arg="interim-update" typ="time"></ArgTableRow>
<ArgTableRow arg="auth-types" typ="ubit (dot1x, mac-auth)"></ArgTableRow>
<ArgTableRow arg="mac-auth-mode" typ="enum (mac-as-username | mac-as-username-and-password)"></ArgTableRow>
<ArgTableRow arg="radius-mac-format" typ="enum (XX:XX:XX:XX:XX:XX | XX-XX-XX-XX-XX-XX | XXXXXXXXXXXX | xx:xx:xx:xx:xx:xx | xx-xx-xx-xx-xx-xx | xxxxxxxxxxxx)"></ArgTableRow>
<ArgTableRow arg="reauth-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="auth-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="retrans-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="reject-vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="guest-vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="server-fail-vlan-id" typ="num"></ArgTableRow>
</ArgTable>

#### interface/dot1x/server/active

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="username" typ="string"></ArgTableRow>
<ArgTableRow arg="client-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="session-id" typ="string"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="auth-info" typ="string"></ArgTableRow>
</ArgTable>

#### interface/dot1x/server/state

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>
