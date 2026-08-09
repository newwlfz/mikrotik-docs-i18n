# certificate

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# certificate

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="K" typ="private-key">private-key</ArgTableRow>
<ArgTableRow arg="L" typ="crl">crl</ArgTableRow>
<ArgTableRow arg="C" typ="smart-card-key">smart-card-key</ArgTableRow>
<ArgTableRow arg="A" typ="authority">authority</ArgTableRow>
<ArgTableRow arg="I" typ="issued">issued</ArgTableRow>
<ArgTableRow arg="R" typ="revoked">revoked</ArgTableRow>
<ArgTableRow arg="E" typ="expired">expired</ArgTableRow>
<ArgTableRow arg="T" typ="trusted">trusted</ArgTableRow>
<ArgTableRow arg="a" typ="acme-managed">acme-managed</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="active" typ="switch"></ArgTableRow>
<ArgTableRow arg="inactive" typ="switch"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="trust-store" typ="alt { enum (all) { all:cerm::trust_store::All }
, ubit () {  }
 }"></ArgTableRow>
<ArgTableRow arg="digest-algorithm" typ="enum (md5 | sha1 | sha256 | sha384 | sha512)"></ArgTableRow>
<ArgTableRow arg="trusted" typ="bool"></ArgTableRow>
<ArgTableRow arg="common-name" typ="string"></ArgTableRow>
<ArgTableRow arg="organization" typ="string"></ArgTableRow>
<ArgTableRow arg="unit" typ="string"></ArgTableRow>
<ArgTableRow arg="locality" typ="string"></ArgTableRow>
<ArgTableRow arg="state" typ="string"></ArgTableRow>
<ArgTableRow arg="country" typ="string"></ArgTableRow>
<ArgTableRow arg="subject-alt-name" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="key-size" typ="enum (prime256v1 | secp384r1 | secp521r1 | 1024 | 1536 | 2048 | 4096 | 8192)"></ArgTableRow>
<ArgTableRow arg="key-usage" typ="ubit (digital-signature, content-commitment, key-encipherment, data-encipherment, key-agreement, key-cert-sign, crl-sign, encipher-only, decipher-only, tls-server, tls-client, code-sign, email-protect, timestamp, ocsp-sign, dvcs)"></ArgTableRow>
<ArgTableRow arg="days-valid" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="ca-crl-host" typ="string"></ArgTableRow>
<ArgTableRow arg="ca" typ="enum"></ArgTableRow>
<ArgTableRow arg="scep-url" typ="string"></ArgTableRow>
<ArgTableRow arg="fingerprint" typ="string"></ArgTableRow>
<ArgTableRow arg="req-fingerprint" typ="string"></ArgTableRow>
<ArgTableRow arg="ca-fingerprint" typ="string"></ArgTableRow>
<ArgTableRow arg="expires-after" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="challenge-password" typ="string"></ArgTableRow>
<ArgTableRow arg="domain-names" typ="string"></ArgTableRow>
<ArgTableRow arg="directory-url" typ="string"></ArgTableRow>
<ArgTableRow arg="acme-status" typ="string"></ArgTableRow>
<ArgTableRow arg="revoked" typ="date"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="issuer" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="key-type" typ="enum (rsa | dsa | ec)"></ArgTableRow>
<ArgTableRow arg="invalid-before" typ="date"></ArgTableRow>
<ArgTableRow arg="invalid-after" typ="date"></ArgTableRow>
<ArgTableRow arg="serial-number" typ="string"></ArgTableRow>
<ArgTableRow arg="akid" typ="string"></ArgTableRow>
<ArgTableRow arg="skid" typ="string"></ArgTableRow>
</ArgTable>

## certificate/add-acme

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="domain-names" typ="string">comma separated list of domain names or a wildcard domain</ArgTableRow>
<ArgTableRow arg="directory-url" typ="string"></ArgTableRow>
<ArgTableRow arg="eab-kid" typ="string"></ArgTableRow>
<ArgTableRow arg="eab-key-b64" typ="string"></ArgTableRow>
</ArgTable>

## certificate/add-scep

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="ca-identity" typ="string"></ArgTableRow>
<ArgTableRow arg="template" typ="enum"></ArgTableRow>
<ArgTableRow arg="scep-url" typ="string"></ArgTableRow>
<ArgTableRow arg="challenge-password" typ="string"></ArgTableRow>
<ArgTableRow arg="on-smart-card" typ="bool">stores private key on smart card if hardware supports it</ArgTableRow>
<ArgTableRow arg="refresh" typ="bool">check certificate expiry and refresh it if expired</ArgTableRow>
</ArgTable>

## certificate/builtin

**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="common-name" typ="string"></ArgTableRow>
<ArgTableRow arg="organization" typ="string"></ArgTableRow>
<ArgTableRow arg="unit" typ="string"></ArgTableRow>
<ArgTableRow arg="locality" typ="string"></ArgTableRow>
<ArgTableRow arg="state" typ="string"></ArgTableRow>
<ArgTableRow arg="country" typ="string"></ArgTableRow>
<ArgTableRow arg="subject-alt-name" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="key-size" typ="enum (prime256v1 | secp384r1 | secp521r1 | 1024 | 1536 | 2048 | 4096 | 8192)"></ArgTableRow>
<ArgTableRow arg="key-usage" typ="ubit (digital-signature, content-commitment, key-encipherment, data-encipherment, key-agreement, key-cert-sign, crl-sign, encipher-only, decipher-only, tls-server, tls-client, code-sign, email-protect, timestamp, ocsp-sign, dvcs)"></ArgTableRow>
<ArgTableRow arg="days-valid" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="issuer" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="key-type" typ="enum (rsa | dsa | ec)"></ArgTableRow>
<ArgTableRow arg="invalid-before" typ="date"></ArgTableRow>
<ArgTableRow arg="invalid-after" typ="date"></ArgTableRow>
<ArgTableRow arg="serial-number" typ="string"></ArgTableRow>
<ArgTableRow arg="akid" typ="string"></ArgTableRow>
<ArgTableRow arg="skid" typ="string"></ArgTableRow>
</ArgTable>

## certificate/card-reinstall

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="pin" typ="string"></ArgTableRow>
</ArgTable>

## certificate/card-verify

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="pin" typ="string"></ArgTableRow>
</ArgTable>

## certificate/create-certificate-request

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="template" typ="enum"></ArgTableRow>
<ArgTableRow arg="key-passphrase" typ="string"></ArgTableRow>
<ArgTableRow arg="challenge-passphrase" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="progress" typ="string"></ArgTableRow>
</ArgTable>

## certificate/crl

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="E" typ="expired">expired</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="url" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="cert" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="trust-store" typ="alt { enum (all) { all:cerm::trust_store::All }
, ubit () {  }
 }"></ArgTableRow>
<ArgTableRow arg="num" typ="num"></ArgTableRow>
<ArgTableRow arg="revoked" typ="num"></ArgTableRow>
<ArgTableRow arg="next-update" typ="date"></ArgTableRow>
<ArgTableRow arg="last-update" typ="date"></ArgTableRow>
<ArgTableRow arg="akid" typ="string"></ArgTableRow>
<ArgTableRow arg="fingerprint" typ="string"></ArgTableRow>
<ArgTableRow arg="signature" typ="string"></ArgTableRow>
</ArgTable>

### certificate/crl/download

**Type:** Command

### certificate/crl/flush

**Type:** Command

## certificate/enable-ssl-certificate

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="dns-name" typ="string">domain name for SSL certificate</ArgTableRow>
<ArgTableRow arg="directory-url" typ="string">ACME directory url</ArgTableRow>
<ArgTableRow arg="eab-hmac-key" typ="string">base64url encoded EAB hmac key</ArgTableRow>
<ArgTableRow arg="eab-kid" typ="string">EAB account id</ArgTableRow>
<ArgTableRow arg="reset-private-key" typ="bool">initialize new private key</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="progress" typ="string"></ArgTableRow>
</ArgTable>

## certificate/export-certificate

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="export-passphrase" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="bool"></ArgTableRow>
<ArgTableRow arg="file-name" typ="file"></ArgTableRow>
</ArgTable>

## certificate/import

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="file-name" typ="file"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string"></ArgTableRow>
<ArgTableRow arg="trusted" typ="bool">mark as trusted</ArgTableRow>
<ArgTableRow arg="trust-store" typ="alt { enum (all) { all:cerm::trust_store::All }
, ubit () {  }
 }"></ArgTableRow>
<ArgTableRow arg="no-key-export" typ="bool">disallow private key export</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="certificates-imported" typ="num"></ArgTableRow>
<ArgTableRow arg="private-keys-imported" typ="num"></ArgTableRow>
<ArgTableRow arg="files-imported" typ="num"></ArgTableRow>
<ArgTableRow arg="decryption-failures" typ="num"></ArgTableRow>
<ArgTableRow arg="keys-with-no-certificate" typ="num"></ArgTableRow>
<ArgTableRow arg="keys-decrypted" typ="num"></ArgTableRow>
</ArgTable>

## certificate/issued-revoke

**Type:** Command

## certificate/scep-renew

**Type:** Command

## certificate/scep-server

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ca-cert" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="next-ca-cert" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="path" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="days-valid" typ="num"></ArgTableRow>
<ArgTableRow arg="request-lifetime" typ="time"></ArgTableRow>
</ArgTable>

### certificate/scep-server/otp

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="E" typ="expired">expired</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="expires" typ="time"></ArgTableRow>
<ArgTableRow arg="used" typ="bool"></ArgTableRow>
</ArgTable>

#### certificate/scep-server/otp/generate

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="minutes-valid" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="password" typ="string"></ArgTableRow>
</ArgTable>

### certificate/scep-server/ra

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="C" typ="smart-card-key">smart-card-key</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="server-url" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="template" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="challenge-password" typ="string"></ArgTableRow>
<ArgTableRow arg="ca-identity" typ="string"></ArgTableRow>
<ArgTableRow arg="fingerprint-algorithm" typ="enum (sha256 | sha1 | md5)"></ArgTableRow>
<ArgTableRow arg="ra-path" typ="string"></ArgTableRow>
<ArgTableRow arg="ra-transaction-lifetime" typ="time"></ArgTableRow>
<ArgTableRow arg="on-smart-card" typ="bool">stores private key on smart card</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="req-fingerprint" typ="string"></ArgTableRow>
<ArgTableRow arg="ca-fingerprint" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

#### certificate/scep-server/ra/renew

**Type:** Command

### certificate/scep-server/requests

**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="authority" typ="alt { enum
, enum
 }"></ArgTableRow>
<ArgTableRow arg="status" typ="enum (pending | granted | denied | authorized | waiting | failed | issued | invalid)"></ArgTableRow>
<ArgTableRow arg="created" typ="date"></ArgTableRow>
<ArgTableRow arg="transaction-id" typ="string"></ArgTableRow>
<ArgTableRow arg="req-fingerprint" typ="string"></ArgTableRow>
<ArgTableRow arg="country" typ="string"></ArgTableRow>
<ArgTableRow arg="state" typ="string"></ArgTableRow>
<ArgTableRow arg="locality" typ="string"></ArgTableRow>
<ArgTableRow arg="organization" typ="string"></ArgTableRow>
<ArgTableRow arg="unit" typ="string"></ArgTableRow>
<ArgTableRow arg="common-name" typ="string"></ArgTableRow>
<ArgTableRow arg="serial-number" typ="string"></ArgTableRow>
<ArgTableRow arg="subject-alt-name" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
</ArgTable>

#### certificate/scep-server/requests/grant

**Type:** Command

## certificate/settings

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="builtin-trust-store" typ="alt { enum (default | all | untrusted) { default:cerm::trust_store::Default, all:cerm::trust_store::All, untrusted:cerm::trust_store::None }
, ubit () {  }
 }">RouterOS provided CA certificates</ArgTableRow>
<ArgTableRow arg="current-defaults" typ="ubit ()"></ArgTableRow>
<ArgTableRow arg="crl-download" typ="bool">auto CRL download and update</ArgTableRow>
<ArgTableRow arg="crl-use" typ="bool">perform CRL checking when validating trust chain</ArgTableRow>
<ArgTableRow arg="crl-store" typ="enum (system | ram)">CRL storage location</ArgTableRow>
</ArgTable>

## certificate/sign

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="ca-crl-host" typ="multi { array-id, string
 }">adds CRL URL to created certificate</ArgTableRow>
<ArgTableRow arg="ca-on-smart-card" typ="bool">stores CA's private key on smart card</ArgTableRow>
<ArgTableRow arg="ca" typ="enum">issuer CA</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="progress" typ="string"></ArgTableRow>
</ArgTable>

## certificate/sign-certificate-request

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ca" typ="enum"></ArgTableRow>
<ArgTableRow arg="file-name" typ="file"></ArgTableRow>
<ArgTableRow arg="days-valid" typ="num"></ArgTableRow>
<ArgTableRow arg="digest-algorithm" typ="enum (md5 | sha1 | sha256 | sha384 | sha512)"></ArgTableRow>
</ArgTable>
