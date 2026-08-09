# user

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# user

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="E" typ="expired">expired</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="group" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="password" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="inactivity-timeout" typ="time">period after which inactivity policy is applied</ArgTableRow>
<ArgTableRow arg="inactivity-policy" typ="enum (none | logout | lockscreen)">specify action taken after inactivity timeout</ArgTableRow>
<ArgTableRow arg="address" typ="object { alt { ipPrefix
, ip6Prefix
 } { ipPrefix
, ip6Prefix
 }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="last-logged-in" typ="date"></ArgTableRow>
</ArgTable>

## user/aaa

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="use-radius" typ="bool"></ArgTableRow>
<ArgTableRow arg="accounting" typ="bool"></ArgTableRow>
<ArgTableRow arg="interim-update" typ="time"></ArgTableRow>
<ArgTableRow arg="default-group" typ="enum"></ArgTableRow>
<ArgTableRow arg="exclude-groups" typ="multi { , enum
 }"></ArgTableRow>
</ArgTable>

## user/active

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="R" typ="radius">radius</ArgTableRow>
<ArgTableRow arg="M" typ="by-romon">by-romon</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="when" typ="date"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="address" typ="alt { ipAddr
, ip6Addr
, macAddr
 }"></ArgTableRow>
<ArgTableRow arg="by-romon" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="via" typ="enum (unknown | winbox | console | telnet | ftp | web | ssh | mac-telnet | bandwidth-test | api | romon | rest-api)"></ArgTableRow>
<ArgTableRow arg="group" typ="enum"></ArgTableRow>
</ArgTable>

## user/expire-password

**Type:** Command

## user/group

**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="policy" typ="multi { array-id, array-id, super { !
, enum
 } { !
, enum
 }
 }"></ArgTableRow>
<ArgTableRow arg="skin" typ="enum"></ArgTableRow>
</ArgTable>

## user/settings

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="minimum-password-length" typ="num"></ArgTableRow>
<ArgTableRow arg="minimum-categories" typ="num"></ArgTableRow>
</ArgTable>

## user/ssh-keys

**Package:** security
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="user" typ="enum"></ArgTableRow>
<ArgTableRow arg="key" typ="string">only for adding new keys</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="key-type" typ="enum (rsa | ed25519 | ed25519-sk)"></ArgTableRow>
<ArgTableRow arg="bits" typ="num"></ArgTableRow>
<ArgTableRow arg="info" typ="string"></ArgTableRow>
<ArgTableRow arg="fingerprint" typ="string"></ArgTableRow>
</ArgTable>

### user/ssh-keys/import

**Package:** security
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="public-key-file" typ="file"></ArgTableRow>
<ArgTableRow arg="user" typ="enum"></ArgTableRow>
<ArgTableRow arg="info" typ="string"></ArgTableRow>
</ArgTable>

### user/ssh-keys/private

**Package:** security
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="user" typ="enum"></ArgTableRow>
<ArgTableRow arg="key-type" typ="enum (rsa | ed25519)"></ArgTableRow>
<ArgTableRow arg="bits" typ="num"></ArgTableRow>
<ArgTableRow arg="info" typ="string"></ArgTableRow>
</ArgTable>

#### user/ssh-keys/private/import

**Package:** security
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="private-key-file" typ="file"></ArgTableRow>
<ArgTableRow arg="user" typ="enum"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string"></ArgTableRow>
<ArgTableRow arg="info" typ="string"></ArgTableRow>
</ArgTable>
