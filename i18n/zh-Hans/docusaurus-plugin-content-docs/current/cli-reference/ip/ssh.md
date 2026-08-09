# SSH

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/ssh

**软件包：** security
**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="ciphers" typ="multi { array-id, enum (aes-gcm | aes-ctr | aes-cbc | 3des-cbc | null | auto) { aes-gcm:ssh::config::CIPHER_AES_GCM, aes-ctr:ssh::config::CIPHER_AES_CTR, aes-cbc:ssh::config::CIPHER_AES_CBC, 3des-cbc:ssh::config::CIPHER_3DES_CBC, null:ssh::config::CIPHER_NULL, auto:ssh::config::CIPHER_AUTO }
 }">允许的加密算法列表</ArgTableRow>
<ArgTableRow arg="forwarding-enabled" typ="enum (no | local | remote | both)">控制允许的转发类型</ArgTableRow>
<ArgTableRow arg="password-authentication" typ="enum (yes | no | yes-if-no-key)"></ArgTableRow>
<ArgTableRow arg="publickey-authentication-options" typ="enum (none | touch-required | verify-required)"></ArgTableRow>
<ArgTableRow arg="strong-crypto" typ="bool">使用更强的加密、HMAC算法，使用更大的DH素数并禁用较弱的算法</ArgTableRow>
<ArgTableRow arg="host-key-size" typ="enum (1024 | 1536 | 2048 | 4096 | 8192)">重新生成主机密钥时的RSA密钥大小</ArgTableRow>
<ArgTableRow arg="host-key-type" typ="enum (rsa | ed25519)"></ArgTableRow>
</ArgTable>

### ip/ssh/export-host-key

**软件包：** security
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="key-file-prefix" typ="string"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string"></ArgTableRow>
</ArgTable>

### ip/ssh/import-host-key

**软件包：** security
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="private-key-file" typ="file"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string"></ArgTableRow>
</ArgTable>

### ip/ssh/regenerate-host-key

**软件包：** security
**类型：** 命令