# Dhcp Client

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ipv6/dhcp-client

**Package:** dhcp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="request" typ="ubit (info, address, prefix)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="accept-prefix-without-address" typ="bool">accept prefix even if no address was offered (applied only if both address and prefix were requested)</ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool">Defines whether to add the default route to the DHCP server (or immediate relay if response was relayed)</ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="default-route-tables" typ="object { alt { composite { ,  } { ,  }
, alt { enum (default) { default:0xffffffff }
, enum
 } { enum (default) { default:0xffffffff }
, enum
 }
 } { composite { ,  } { ,  }
, alt { enum (default) { default:0xffffffff }
, enum
 } { enum (default) { default:0xffffffff }
, enum
 }
 }
 }"></ArgTableRow>
<ArgTableRow arg="check-gateway" typ="enum (none | arp | ping | bfd)"></ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="bool">Whether to accept the DNS settings advertised by DHCP server</ArgTableRow>
<ArgTableRow arg="use-interface-duid" typ="bool">use DUID generated from current interface MAC</ArgTableRow>
<ArgTableRow arg="custom-duid" typ="string">used as client DUID, overrides use-interface-duid</ArgTableRow>
<ArgTableRow arg="validate-server-duid" typ="bool"></ArgTableRow>
<ArgTableRow arg="rapid-commit" typ="bool">use Rapid Commit if possible</ArgTableRow>
<ArgTableRow arg="allow-reconfigure" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcp-options" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="pool-name" typ="string">name of the pool that is created from the received prefix (applied only if prefix was requested)</ArgTableRow>
<ArgTableRow arg="pool-prefix-length" typ="num">prefix length of the pool created from the received prefix (applied only if prefix was requested); if unset, prefix length is determined automatically</ArgTableRow>
<ArgTableRow arg="prefix-hint" typ="ip6Prefix"></ArgTableRow>
<ArgTableRow arg="prefix-address-lists" typ="multi { array-id, string
 }">address lists to which the received prefix will be added (applied only if prefix was requested)</ArgTableRow>
<ArgTableRow arg="script" typ="alt { , string
 }"></ArgTableRow>
<ArgTableRow arg="custom-iapd-id" typ="num"></ArgTableRow>
<ArgTableRow arg="custom-iana-id" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="enum (stopped | searching... | requesting... | bound | renewing... | rebinding... | stopping... | declining... | error | idle | requesting-info... | confirming...)"></ArgTableRow>
<ArgTableRow arg="duid" typ="string"></ArgTableRow>
<ArgTableRow arg="dhcp-server-v6" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="prefix" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="address" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="reconfigure-key" typ="string"></ArgTableRow>
<ArgTableRow arg="reconfigure-last-counter" typ="string"></ArgTableRow>
</ArgTable>

### ipv6/dhcp-client/option

**Package:** dhcp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="code" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="value" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="raw-value" typ="string"></ArgTableRow>
</ArgTable>

### ipv6/dhcp-client/release

**Package:** dhcp
**Type:** Command

### ipv6/dhcp-client/renew

**Package:** dhcp
**Type:** Command
