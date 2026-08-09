# Ssh

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/ssh

**Package:** security
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ciphers" typ="multi { array-id, enum (aes-gcm | aes-ctr | aes-cbc | 3des-cbc | null | auto) { aes-gcm:ssh::config::CIPHER_AES_GCM, aes-ctr:ssh::config::CIPHER_AES_CTR, aes-cbc:ssh::config::CIPHER_AES_CBC, 3des-cbc:ssh::config::CIPHER_3DES_CBC, null:ssh::config::CIPHER_NULL, auto:ssh::config::CIPHER_AUTO }
 }">allowed cipher list</ArgTableRow>
<ArgTableRow arg="forwarding-enabled" typ="enum (no | local | remote | both)">control which forwarding is allowed</ArgTableRow>
<ArgTableRow arg="password-authentication" typ="enum (yes | no | yes-if-no-key)"></ArgTableRow>
<ArgTableRow arg="publickey-authentication-options" typ="enum (none | touch-required | verify-required)"></ArgTableRow>
<ArgTableRow arg="strong-crypto" typ="bool">use stronger encryption, HMAC algorithms, use bigger DH primes and disallow weaker ones</ArgTableRow>
<ArgTableRow arg="host-key-size" typ="enum (1024 | 1536 | 2048 | 4096 | 8192)">RSA key size when host key is regenerated</ArgTableRow>
<ArgTableRow arg="host-key-type" typ="enum (rsa | ed25519)"></ArgTableRow>
</ArgTable>

### ip/ssh/export-host-key

**Package:** security
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="key-file-prefix" typ="string"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string"></ArgTableRow>
</ArgTable>

### ip/ssh/import-host-key

**Package:** security
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="private-key-file" typ="file"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string"></ArgTableRow>
</ArgTable>

### ip/ssh/regenerate-host-key

**Package:** security
**Type:** Command
