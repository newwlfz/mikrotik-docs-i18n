# Macsec

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/macsec

**条件：** !smips
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="R" typ="running">运行中</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">硬件卸载</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="cak" typ="string"></ArgTableRow>
<ArgTableRow arg="ckn" typ="string"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="tx-untagged" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-untagged" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-too-long" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-no-tag" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bad-tag" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-unknown-sci" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-no-sci" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-overrun" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-sc-protected-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-sc-protected-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-sc-encrypted-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-sc-encrypted-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-validated-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-decrypted-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-unchecked" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-delayed" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-ok" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-invalid" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-late" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-not-valid" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-not-using-sa" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-unused-sa" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sa-ok" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sa-invalid" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sa-not-valid" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sa-not-using-sa" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sa-unused-sa" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-sa-protected" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-sa-encrypted" typ="multi { num
 }"></ArgTableRow>
</ArgTable>

### interface/macsec/monitor

**条件：** !smips
**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="key-server" typ="bool"></ArgTableRow>
<ArgTableRow arg="cipher-suite" typ="enum (aes-gcm-128 | aes-gcm-xpn-128)"></ArgTableRow>
</ArgTable>

### interface/macsec/profile

**条件：** !smips
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="ciphers" typ="multi { enum (aes-gcm-128 | aes-gcm-xpn-128) { aes-gcm-128:mka::CIPHER_AES_GCM_128, aes-gcm-xpn-128:mka::CIPHER_AES_GCM_XPN_128 }
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="server-priority" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="default-name" typ="string"></ArgTableRow>
</ArgTable>