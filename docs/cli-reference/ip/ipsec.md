# Ipsec

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/ipsec

**Package:** security
**Type:** Directory

### ip/ipsec/active-peers

**Package:** security
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="R" typ="responder">responder</ArgTableRow>
<ArgTableRow arg="N" typ="natt-peer">natt-peer</ArgTableRow>
<ArgTableRow arg="P" typ="ppk">ppk</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="id" typ="string"></ArgTableRow>
<ArgTableRow arg="local-address" typ="alt { ip6Addr
, ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="remote-address" typ="alt { ip6Addr
, ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (spawning | starting | message-1-received | message-1-sent | message-2-received | message-2-sent | message-3-received | message-3-sent | message-4-received | established | expired | no-phase1 | eap | crypto | qkd)"></ArgTableRow>
<ArgTableRow arg="side" typ="bool"></ArgTableRow>
<ArgTableRow arg="dynamic-address" typ="alt { ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="last-seen" typ="time"></ArgTableRow>
<ArgTableRow arg="ph2-total" typ="num"></ArgTableRow>
<ArgTableRow arg="spii" typ="string"></ArgTableRow>
<ArgTableRow arg="spir" typ="string"></ArgTableRow>
<ArgTableRow arg="rx-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="num"></ArgTableRow>
</ArgTable>

#### ip/ipsec/active-peers/kill-connections

**Package:** security
**Type:** Command

### ip/ipsec/identity

**Package:** security
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="peer" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="auth-method" typ="enum (pre-shared-key | digital-signature | eap | eap-radius | pre-shared-key-xauth | rsa-key | rsa-signature-hybrid)"></ArgTableRow>
<ArgTableRow arg="eap-methods" typ="multi { array-id, enum (eap-tls | eap-ttls | eap-peap | eap-mschapv2) { eap-tls:ident::EAP_TLS, eap-ttls:ident::EAP_TTLS, eap-peap:ident::EAP_PEAP, eap-mschapv2:ident::EAP_MSCHAPV2 }
,  }">EAP methods</ArgTableRow>
<ArgTableRow arg="mode-config" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="notrack-chain" typ="string">Add dynamic raw notrack rules for dynamic policies</ArgTableRow>
<ArgTableRow arg="my-id" typ="alt { composite { ,  } { ,  }
, composite { ,  } { ,  }
, enum (auto | dn) { auto:ident::IDT_AUTO, dn:ident::IDT_ASN1DN }
,  }"></ArgTableRow>
<ArgTableRow arg="remote-id" typ="alt { composite { ,  } { ,  }
, composite { ,  } { ,  }
, enum (auto | ignore | dn) { auto:ident::IDT_AUTO, ignore:ident::IDT_IGNORE, dn:ident::IDT_ASN1DN }
,  }"></ArgTableRow>
<ArgTableRow arg="match-by" typ="enum (remote-id | certificate)">identity lookup method for the responder</ArgTableRow>
<ArgTableRow arg="key" typ="enum ()">key for raw RSA authentication (ike1 only)</ArgTableRow>
<ArgTableRow arg="remote-key" typ="enum ()">remote key for raw RSA authentication (ike1 only)</ArgTableRow>
<ArgTableRow arg="secret" typ="string {  }">pre-shared key secret</ArgTableRow>
<ArgTableRow arg="certificate" typ="multi { array-id, enum
,  }">local certificate</ArgTableRow>
<ArgTableRow arg="remote-certificate" typ="enum (none)">use this certificate when peer does not send one</ArgTableRow>
<ArgTableRow arg="username" typ="string {  }">EAP or XAuth user</ArgTableRow>
<ArgTableRow arg="password" typ="string {  }">EAP or XAuth password</ArgTableRow>
<ArgTableRow arg="generate-policy" typ="enum (no | port-override | port-strict)"></ArgTableRow>
<ArgTableRow arg="policy-template-group" typ="enum"></ArgTableRow>
</ArgTable>

### ip/ipsec/installed-sa

**Package:** security
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="S" typ="seen-traffic">seen-traffic</ArgTableRow>
<ArgTableRow arg="H" typ="hw-aead">hw-aead</ArgTableRow>
<ArgTableRow arg="A" typ="AH">AH</ArgTableRow>
<ArgTableRow arg="E" typ="ESP">ESP</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="spi" typ="num"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (larval | mature | dying | dead)"></ArgTableRow>
<ArgTableRow arg="auth-algorithm" typ="enum (none | md5 | sha1 | sha256 | sha512)"></ArgTableRow>
<ArgTableRow arg="enc-algorithm" typ="enum (none | des | 3des | null | aes-cbc | aes-ctr | aes-gcm | blowfish | twofish | camellia | chacha20poly1305)"></ArgTableRow>
<ArgTableRow arg="enc-key-size" typ="num"></ArgTableRow>
<ArgTableRow arg="auth-key" typ="string"></ArgTableRow>
<ArgTableRow arg="enc-key" typ="string"></ArgTableRow>
<ArgTableRow arg="addtime" typ="date"></ArgTableRow>
<ArgTableRow arg="expires-in" typ="time"></ArgTableRow>
<ArgTableRow arg="add-lifetime" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="current-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="current-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="invalid-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="replay" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="src-address" typ="super { alt { ip6Addr
, ipAddr
 } { ip6Addr
, ipAddr
 }
, :num
 }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { alt { ip6Addr
, ipAddr
 } { ip6Addr
, ipAddr
 }
, :num
 }"></ArgTableRow>
</ArgTable>

#### ip/ipsec/installed-sa/flush

**Package:** security
**Type:** Command

### ip/ipsec/key

**Package:** security
**Type:** Directory

#### ip/ipsec/key/psk

**Package:** security
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="peer" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="id" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="key" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>

##### ip/ipsec/key/psk/generate

**Package:** security
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="peer" typ="enum"></ArgTableRow>
<ArgTableRow arg="size" typ="num"></ArgTableRow>
<ArgTableRow arg="count" typ="num"></ArgTableRow>
</ArgTable>

#### ip/ipsec/key/qkd

**Package:** security
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="address" typ="string">KME device address</ArgTableRow>
<ArgTableRow arg="kme-id" typ="string">should match the KME ID in the received TLS certificate</ArgTableRow>
<ArgTableRow arg="key-size" typ="num">in bits</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)">this also specifies your SAE ID</ArgTableRow>
<ArgTableRow arg="peer-sae-id" typ="string">peer (master or slave) SAE ID</ArgTableRow>
<ArgTableRow arg="cache-size" typ="num">number of unused keys to keep in cache</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="cache-state" typ="num">number of current unused keys in cache</ArgTableRow>
<ArgTableRow arg="total-keys-received" typ="num">total number of received keys</ArgTableRow>
</ArgTable>

##### ip/ipsec/key/qkd/get-key

**Package:** security
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="additional-sae-ids" typ="multi { array-id, string
 }">additional SAEs which will also get the generated key</ArgTableRow>
<ArgTableRow arg="number" typ="num">number of keys to generate</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="keys" typ="object { super { string
, : string
 } { string
, : string
 }
 }"></ArgTableRow>
</ArgTable>

##### ip/ipsec/key/qkd/get-key-cached

**Package:** security
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="key-id" typ="string"></ArgTableRow>
<ArgTableRow arg="key" typ="string"></ArgTableRow>
</ArgTable>

##### ip/ipsec/key/qkd/get-key-with-ids

**Package:** security
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="key-ids" typ="multi { array-id, string
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="keys" typ="object { super { string
, : string
 } { string
, : string
 }
 }"></ArgTableRow>
</ArgTable>

##### ip/ipsec/key/qkd/get-status

**Package:** security
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="sae-id" typ="string">if not specified, peer-sae-id will be used</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="source-kme-id" typ="string"></ArgTableRow>
<ArgTableRow arg="target-kme-id" typ="string"></ArgTableRow>
<ArgTableRow arg="master-sae-id" typ="string"></ArgTableRow>
<ArgTableRow arg="slave-sae-id" typ="string"></ArgTableRow>
<ArgTableRow arg="key-size" typ="num"></ArgTableRow>
<ArgTableRow arg="stored-key-count" typ="num"></ArgTableRow>
<ArgTableRow arg="max-key-count" typ="num"></ArgTableRow>
<ArgTableRow arg="max-key-per-request" typ="num"></ArgTableRow>
<ArgTableRow arg="max-key-size" typ="num"></ArgTableRow>
<ArgTableRow arg="min-key-size" typ="num"></ArgTableRow>
<ArgTableRow arg="max-sae-id-count" typ="num"></ArgTableRow>
</ArgTable>

#### ip/ipsec/key/rsa

**Package:** security
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="P" typ="private-key">private-key</ArgTableRow>
<ArgTableRow arg="R" typ="rsa">rsa</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="key-size" typ="num"></ArgTableRow>
</ArgTable>

##### ip/ipsec/key/rsa/export-pub-key

**Package:** security
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="key" typ="enum"></ArgTableRow>
<ArgTableRow arg="file-name" typ="string"></ArgTableRow>
</ArgTable>

##### ip/ipsec/key/rsa/generate-key

**Package:** security
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="key-size" typ="alt { enum (2048 | 4096 | 8192) { 2048:2048, 4096:4096, 8192:8192 }
 }"></ArgTableRow>
</ArgTable>

##### ip/ipsec/key/rsa/import

**Package:** security
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="file-name" typ="file"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string"></ArgTableRow>
</ArgTable>

### ip/ipsec/mode-config

**Package:** security
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
<ArgTableRow arg="R" typ="responder">responder</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="responder" typ="bool">peer shoud request or send the config</ArgTableRow>
<ArgTableRow arg="system-dns" typ="bool {  }">send system dns servers to peer</ArgTableRow>
<ArgTableRow arg="static-dns" typ="object { alt { ipAddr
 } { ipAddr
 }
,  }">dns servers sent to peer, exclusive with system-dns</ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr {  }"></ArgTableRow>
<ArgTableRow arg="address-pool" typ="enum (none)">issue one address for peer from this pool</ArgTableRow>
<ArgTableRow arg="address-prefix-length" typ="num {  }">issued address netmask</ArgTableRow>
<ArgTableRow arg="split-include" typ="object { , alt { ipPrefix
 } { ipPrefix
 }
 }">additional protected subnets</ArgTableRow>
<ArgTableRow arg="split-dns" typ="multi { array-id, string
,  }">DNS name to be resolved using internal server</ArgTableRow>
<ArgTableRow arg="src-address-list" typ="enum ()">address list name to be added to srcnat chain for initiator</ArgTableRow>
<ArgTableRow arg="connection-mark" typ="enum ()">conection-mark to be added to srcnat chain for initiator</ArgTableRow>
<ArgTableRow arg="use-responder-dns" typ="enum (no | yes | exclusively)">if the dns servers sent should be used by the initiator</ArgTableRow>
</ArgTable>

### ip/ipsec/peer

**Package:** security
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="R" typ="responder">responder</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="address" typ="alt { ip6Prefix
, ipPrefix
, string
,  }"></ArgTableRow>
<ArgTableRow arg="local-address" typ="alt { ip6Addr
, ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="passive" typ="bool">Passive peer won't initiate connection</ArgTableRow>
<ArgTableRow arg="port" typ="num {  }">peer's port</ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="exchange-mode" typ="enum (main | base | aggressive | ike2)"></ArgTableRow>
<ArgTableRow arg="send-initial-contact" typ="bool"></ArgTableRow>
<ArgTableRow arg="ppk-secret" typ="string">static PPK secret with "static-ppk-secret" ID used when no one-time key/psk exist for this peer, ensure the key has 256 bits of entropy</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="current-address" typ="alt { ip6Addr
, ipAddr
 }"></ArgTableRow>
</ArgTable>

### ip/ipsec/policy

**Package:** security
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="T" typ="template">template</ArgTableRow>
<ArgTableRow arg="B" typ="backup">backup</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
<ArgTableRow arg="A" typ="active">active</ArgTableRow>
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="peer" typ="multi { array-id, enum
 }">auto activates peer establishes connection, use with shunt policy</ArgTableRow>
<ArgTableRow arg="tunnel" typ="bool"></ArgTableRow>
<ArgTableRow arg="group" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ip6Prefix
, ipPrefix
 }"></ArgTableRow>
<ArgTableRow arg="src-port" typ="num"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="alt { ip6Prefix
, ipPrefix
 }"></ArgTableRow>
<ArgTableRow arg="dst-port" typ="num"></ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (all)"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (encrypt | discard | none)"></ArgTableRow>
<ArgTableRow arg="level" typ="enum (require | use | unique)"></ArgTableRow>
<ArgTableRow arg="ipsec-protocols" typ="enum (ah | esp)">which ipsec protocol to use</ArgTableRow>
<ArgTableRow arg="sa-src-address" typ="alt { ip6Addr
, ipAddr
,  }">endpoint address</ArgTableRow>
<ArgTableRow arg="sa-dst-address" typ="alt { ip6Addr
, ipAddr
,  }">endpoint address</ArgTableRow>
<ArgTableRow arg="proposal" typ="enum"></ArgTableRow>
<ArgTableRow arg="template" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="ph2-count" typ="num"></ArgTableRow>
<ArgTableRow arg="ph2-state" typ="enum (spawning | starting | ready-to-send | getspi-sent | getspi-done | msg1-sent | ready-to-establish | commiting | adding-sa | established | expired | no-phase2)"></ArgTableRow>
</ArgTable>

#### ip/ipsec/policy/group

**Package:** security
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>

### ip/ipsec/profile

**Package:** security
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="hash-algorithm" typ="enum (md5 | sha1 | sha256 | sha384 | sha512)"></ArgTableRow>
<ArgTableRow arg="prf-algorithm" typ="enum (auto | sha1 | sha256 | sha384 | sha512)">IKEv2 only</ArgTableRow>
<ArgTableRow arg="enc-algorithm" typ="ubit (aes-256, aes-192, aes-128, 3des, des)"></ArgTableRow>
<ArgTableRow arg="dh-group" typ="ubit (x25519, ecp256, ecp384, ecp521, modp6144, modp4096, modp3072, modp2048, modp1536, modp1024, modp768)"></ArgTableRow>
<ArgTableRow arg="lifetime" typ="time">IKEv1 only</ArgTableRow>
<ArgTableRow arg="lifebytes" typ="num">IKEv1 only</ArgTableRow>
<ArgTableRow arg="proposal-check" typ="enum (obey | strict | claim | exact)">Lifetime check logic (IKEv1 only)</ArgTableRow>
<ArgTableRow arg="nat-traversal" typ="bool">IKEv1 only</ArgTableRow>
<ArgTableRow arg="ppk" typ="enum (no | psk | psk-ike-initial | qkd)">post-quantum preshared key (IKEv2 only)</ArgTableRow>
<ArgTableRow arg="dpd-interval" typ="alt { enum (disable-dpd) { disable-dpd:0 }
, time [ .. 3600]
 }"></ArgTableRow>
<ArgTableRow arg="dpd-maximum-failures" typ="num {  }">IKEv1 only</ArgTableRow>
</ArgTable>

### ip/ipsec/proposal

**Conditions:** IKE2_DEV
**Package:** security
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="auth-algorithms" typ="ubit (sha512, sha256, sha1, md5, null)"></ArgTableRow>
<ArgTableRow arg="enc-algorithms" typ="ubit (chacha20poly1305, aes-256-cbc, aes-256-ctr, aes-256-gcm, camellia-256, aes-192-cbc, aes-192-ctr, aes-192-gcm, camellia-192, aes-128-cbc, aes-128-ctr, aes-128-gcm, camellia-128, 3des, blowfish, twofish, des, null)"></ArgTableRow>
<ArgTableRow arg="lifetime" typ="time"></ArgTableRow>
<ArgTableRow arg="pfs-group" typ="enum (none | ecp256 | ecp384 | ecp521 | modp6144 | modp4096 | modp3072 | modp2048 | modp1536 | modp1024 | modp768)"></ArgTableRow>
</ArgTable>

### ip/ipsec/settings

**Package:** security
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="xauth-use-radius" typ="bool"></ArgTableRow>
<ArgTableRow arg="accounting" typ="bool"></ArgTableRow>
<ArgTableRow arg="interim-update" typ="time"></ArgTableRow>
<ArgTableRow arg="ddos-cookie-threshold" typ="num">DDOS cookie activation threshold</ArgTableRow>
</ArgTable>

### ip/ipsec/statistics

**Package:** security
**Type:** Settings Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="in-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="in-buffer-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="in-header-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="in-no-states" typ="num"></ArgTableRow>
<ArgTableRow arg="in-state-protocol-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="in-state-mode-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="in-state-sequence-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="in-state-expired" typ="num"></ArgTableRow>
<ArgTableRow arg="in-state-mismatches" typ="num"></ArgTableRow>
<ArgTableRow arg="in-state-invalid" typ="num"></ArgTableRow>
<ArgTableRow arg="in-template-mismatches" typ="num"></ArgTableRow>
<ArgTableRow arg="in-no-policies" typ="num"></ArgTableRow>
<ArgTableRow arg="in-policy-blocked" typ="num"></ArgTableRow>
<ArgTableRow arg="in-policy-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="out-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="out-bundle-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="out-bundle-check-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="out-no-states" typ="num"></ArgTableRow>
<ArgTableRow arg="out-state-protocol-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="out-state-mode-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="out-state-sequence-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="out-state-expired" typ="num"></ArgTableRow>
<ArgTableRow arg="out-policy-blocked" typ="num"></ArgTableRow>
<ArgTableRow arg="out-policy-dead" typ="num"></ArgTableRow>
<ArgTableRow arg="out-policy-errors" typ="num"></ArgTableRow>
</ArgTable>
