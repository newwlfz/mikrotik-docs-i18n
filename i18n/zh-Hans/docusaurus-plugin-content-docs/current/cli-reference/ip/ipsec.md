# Ipsec

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/ipsec

**软件包:** security
**类型:** 目录

### ip/ipsec/active-peers

**软件包:** security
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="R" typ="responder">响应方</ArgTableRow>
<ArgTableRow arg="N" typ="natt-peer">NAT-T 对等体</ArgTableRow>
<ArgTableRow arg="P" typ="ppk">PPK</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
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

**软件包:** security
**类型:** 命令

### ip/ipsec/identity

**软件包:** security
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="peer" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="auth-method" typ="enum (pre-shared-key | digital-signature | eap | eap-radius | pre-shared-key-xauth | rsa-key | rsa-signature-hybrid)"></ArgTableRow>
<ArgTableRow arg="eap-methods" typ="multi { array-id, enum (eap-tls | eap-ttls | eap-peap | eap-mschapv2) { eap-tls:ident::EAP_TLS, eap-ttls:ident::EAP_TTLS, eap-peap:ident::EAP_PEAP, eap-mschapv2:ident::EAP_MSCHAPV2 }
,  }">EAP 方法</ArgTableRow>
<ArgTableRow arg="mode-config" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="notrack-chain" typ="string">为动态策略添加动态原始 notrack 规则</ArgTableRow>
<ArgTableRow arg="my-id" typ="alt { composite { ,  } { ,  }
, composite { ,  } { ,  }
, enum (auto | dn) { auto:ident::IDT_AUTO, dn:ident::IDT_ASN1DN }
,  }"></ArgTableRow>
<ArgTableRow arg="remote-id" typ="alt { composite { ,  } { ,  }
, composite { ,  } { ,  }
, enum (auto | ignore | dn) { auto:ident::IDT_AUTO, ignore:ident::IDT_IGNORE, dn:ident::IDT_ASN1DN }
,  }"></ArgTableRow>
<ArgTableRow arg="match-by" typ="enum (remote-id | certificate)">响应方的身份查找方法</ArgTableRow>
<ArgTableRow arg="key" typ="enum ()">用于原始 RSA 认证的密钥（仅 IKE1）</ArgTableRow>
<ArgTableRow arg="remote-key" typ="enum ()">用于原始 RSA 认证的远程密钥（仅 IKE1）</ArgTableRow>
<ArgTableRow arg="secret" typ="string {  }">预共享密钥</ArgTableRow>
<ArgTableRow arg="certificate" typ="multi { array-id, enum
,  }">本地证书</ArgTableRow>
<ArgTableRow arg="remote-certificate" typ="enum (none)">当对等体未发送证书时使用此证书</ArgTableRow>
<ArgTableRow arg="username" typ="string {  }">EAP 或 XAuth 用户</ArgTableRow>
<ArgTableRow arg="password" typ="string {  }">EAP 或 XAuth 密码</ArgTableRow>
<ArgTableRow arg="generate-policy" typ="enum (no | port-override | port-strict)"></ArgTableRow>
<ArgTableRow arg="policy-template-group" typ="enum"></ArgTableRow>
</ArgTable>

### ip/ipsec/installed-sa

**软件包:** security
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="S" typ="seen-traffic">已见流量</ArgTableRow>
<ArgTableRow arg="H" typ="hw-aead">硬件 AEAD</ArgTableRow>
<ArgTableRow arg="A" typ="AH">AH</ArgTableRow>
<ArgTableRow arg="E" typ="ESP">ESP</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
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

<ArgTable c1="只读参数" c2="类型" c3="描述">
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

**软件包:** security
**类型:** 命令

### ip/ipsec/key

**软件包:** security
**类型:** 目录

#### ip/ipsec/key/psk

**软件包:** security
**类型:** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="peer" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="id" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="key" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>

##### ip/ipsec/key/psk/generate

**软件包:** security
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="peer" typ="enum"></ArgTableRow>
<ArgTableRow arg="size" typ="num"></ArgTableRow>
<ArgTableRow arg="count" typ="num"></ArgTableRow>
</ArgTable>

#### ip/ipsec/key/qkd

**软件包:** security
**类型:** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="address" typ="string">KME 设备地址</ArgTableRow>
<ArgTableRow arg="kme-id" typ="string">应与接收到的 TLS 证书中的 KME ID 匹配</ArgTableRow>
<ArgTableRow arg="key-size" typ="num">以位为单位</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)">此证书同时指定您的 SAE ID</ArgTableRow>
<ArgTableRow arg="peer-sae-id" typ="string">对等体（主或从）SAE ID</ArgTableRow>
<ArgTableRow arg="cache-size" typ="num">缓存中保留的未使用密钥数量</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="cache-state" typ="num">缓存中当前未使用的密钥数量</ArgTableRow>
<ArgTableRow arg="total-keys-received" typ="num">接收到的密钥总数</ArgTableRow>
</ArgTable>

##### ip/ipsec/key/qkd/get-key

**软件包:** security
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="additional-sae-ids" typ="multi { array-id, string
 }">也将获得生成密钥的其他 SAE</ArgTableRow>
<ArgTableRow arg="number" typ="num">要生成的密钥数量</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="keys" typ="object { super { string
, : string
 } { string
, : string
 }
 }"></ArgTableRow>
</ArgTable>

##### ip/ipsec/key/qkd/get-key-cached

**软件包:** security
**类型:** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="key-id" typ="string"></ArgTableRow>
<ArgTableRow arg="key" typ="string"></ArgTableRow>
</ArgTable>

##### ip/ipsec/key/qkd/get-key-with-ids

**软件包:** security
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="key-ids" typ="multi { array-id, string
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="keys" typ="object { super { string
, : string
 } { string
, : string
 }
 }"></ArgTableRow>
</ArgTable>

##### ip/ipsec/key/qkd/get-status

**软件包:** security
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="sae-id" typ="string">如果未指定，将使用 peer-sae-id</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
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

**软件包:** security
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="P" typ="private-key">私钥</ArgTableRow>
<ArgTableRow arg="R" typ="rsa">RSA</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="key-size" typ="num"></ArgTableRow>
</ArgTable>

##### ip/ipsec/key/rsa/export-pub-key

**软件包:** security
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="key" typ="enum"></ArgTableRow>
<ArgTableRow arg="file-name" typ="string"></ArgTableRow>
</ArgTable>

##### ip/ipsec/key/rsa/generate-key

**软件包:** security
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="key-size" typ="alt { enum (2048 | 4096 | 8192) { 2048:2048, 4096:4096, 8192:8192 }
 }"></ArgTableRow>
</ArgTable>

##### ip/ipsec/key/rsa/import

**软件包:** security
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="file-name" typ="file"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string"></ArgTableRow>
</ArgTable>

### ip/ipsec/mode-config

**软件包:** security
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
<ArgTableRow arg="R" typ="responder">响应方</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="responder" typ="bool">对等体应请求或发送配置</ArgTableRow>
<ArgTableRow arg="system-dns" typ="bool {  }">向对等体发送系统 DNS 服务器</ArgTableRow>
<ArgTableRow arg="static-dns" typ="object { alt { ipAddr
 } { ipAddr
 }
,  }">发送给对等体的 DNS 服务器，与 system-dns 互斥</ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr {  }"></ArgTableRow>
<ArgTableRow arg="address-pool" typ="enum (none)">从此地址池为对等体分配一个地址</ArgTableRow>
<ArgTableRow arg="address-prefix-length" typ="num {  }">分配地址的子网掩码</ArgTableRow>
<ArgTableRow arg="split-include" typ="object { , alt { ipPrefix
 } { ipPrefix
 }
 }">额外的受保护子网</ArgTableRow>
<ArgTableRow arg="split-dns" typ="multi { array-id, string
,  }">使用内部服务器解析的 DNS 名称</ArgTableRow>
<ArgTableRow arg="src-address-list" typ="enum ()">要添加到发起方 srcnat 链的地址列表名称</ArgTableRow>
<ArgTableRow arg="connection-mark" typ="enum ()">要添加到发起方 srcnat 链的连接标记</ArgTableRow>
<ArgTableRow arg="use-responder-dns" typ="enum (no | yes | exclusively)">发起方是否应使用发送的 DNS 服务器</ArgTableRow>
</ArgTable>

### ip/ipsec/peer

**软件包:** security
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="R" typ="responder">响应方</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="address" typ="alt { ip6Prefix
, ipPrefix
, string
,  }"></ArgTableRow>
<ArgTableRow arg="local-address" typ="alt { ip6Addr
, ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="passive" typ="bool">被动对等体不会发起连接</ArgTableRow>
<ArgTableRow arg="port" typ="num {  }">对等体的端口</ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="exchange-mode" typ="enum (main | base | aggressive | ike2)"></ArgTableRow>
<ArgTableRow arg="send-initial-contact" typ="bool"></ArgTableRow>
<ArgTableRow arg="ppk-secret" typ="string">使用 "static-ppk-secret" ID 的静态 PPK 密钥，当该对等体不存在一次性密钥/PSK 时使用，确保密钥具有 256 位熵</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="current-address" typ="alt { ip6Addr
, ipAddr
 }"></ArgTableRow>
</ArgTable>

### ip/ipsec/policy

**软件包:** security
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="T" typ="template">模板</ArgTableRow>
<ArgTableRow arg="B" typ="backup">备份</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
<ArgTableRow arg="A" typ="active">活动</ArgTableRow>
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="peer" typ="multi { array-id, enum
 }">自动激活对等体建立连接，与分流策略一起使用</ArgTableRow>
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
<ArgTableRow arg="ipsec-protocols" typ="enum (ah | esp)">要使用的 IPsec 协议</ArgTableRow>
<ArgTableRow arg="sa-src-address" typ="alt { ip6Addr
, ipAddr
,  }">端点地址</ArgTableRow>
<ArgTableRow arg="sa-dst-address" typ="alt { ip6Addr
, ipAddr
,  }">端点地址</ArgTableRow>
<ArgTableRow arg="proposal" typ="enum"></ArgTableRow>
<ArgTableRow arg="template" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="ph2-count" typ="num"></ArgTableRow>
<ArgTableRow arg="ph2-state" typ="enum (spawning | starting | ready-to-send | getspi-sent | getspi-done | msg1-sent | ready-to-establish | commiting | adding-sa | established | expired | no-phase2)"></ArgTableRow>
</ArgTable>

#### ip/ipsec/policy/group

**软件包:** security
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>

### ip/ipsec/profile

**软件包:** security
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="hash-algorithm" typ="enum (md5 | sha1 | sha256 | sha384 | sha512)"></ArgTableRow>
<ArgTableRow arg="prf-algorithm" typ="enum (auto | sha1 | sha256 | sha384 | sha512)">仅 IKEv2</ArgTableRow>
<ArgTableRow arg="enc-algorithm" typ="ubit (aes-256, aes-192, aes-128, 3des, des)"></ArgTableRow>
<ArgTableRow arg="dh-group" typ="ubit (x25519, ecp256, ecp384, ecp521, modp6144, modp4096, modp3072, modp2048, modp1536, modp1024, modp768)"></ArgTableRow>
<ArgTableRow arg="lifetime" typ="time">仅 IKEv1</ArgTableRow>
<ArgTableRow arg="lifebytes" typ="num">仅 IKEv1</ArgTableRow>
<ArgTableRow arg="proposal-check" typ="enum (obey | strict | claim | exact)">生命周期检查逻辑（仅 IKEv1）</ArgTableRow>
<ArgTableRow arg="nat-traversal" typ="bool">仅 IKEv1</ArgTableRow>
<ArgTableRow arg="ppk" typ="enum (no | psk | psk-ike-initial | qkd)">后量子预共享密钥（仅 IKEv2）</ArgTableRow>
<ArgTableRow arg="dpd-interval" typ="alt { enum (disable-dpd) { disable-dpd:0 }
, time [ .. 3600]
 }"></ArgTableRow>
<ArgTableRow arg="dpd-maximum-failures" typ="num {  }">仅 IKEv1</ArgTableRow>
</ArgTable>

### ip/ipsec/proposal

**条件:** IKE2_DEV
**软件包:** security
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="auth-algorithms" typ="ubit (sha512, sha256, sha1, md5, null)"></ArgTableRow>
<ArgTableRow arg="enc-algorithms" typ="ubit (chacha20poly1305, aes-256-cbc, aes-256-ctr, aes-256-gcm, camellia-256, aes-192-cbc, aes-192-ctr, aes-192-gcm, camellia-192, aes-128-cbc, aes-128-ctr, aes-128-gcm, camellia-128, 3des, blowfish, twofish, des, null)"></ArgTableRow>
<ArgTableRow arg="lifetime" typ="time"></ArgTableRow>
<ArgTableRow arg="pfs-group" typ="enum (none | ecp256 | ecp384 | ecp521 | modp6144 | modp4096 | modp3072 | modp2048 | modp1536 | modp1024 | modp768)"></ArgTableRow>
</ArgTable>

### ip/ipsec/settings

**软件包:** security
**类型:** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="xauth-use-radius" typ="bool"></ArgTableRow>
<ArgTableRow arg="accounting" typ="bool"></ArgTableRow>
<ArgTableRow arg="interim-update" typ="time"></ArgTableRow>
<ArgTableRow arg="ddos-cookie-threshold" typ="num">DDOS Cookie 激活阈值</ArgTableRow>
</ArgTable>

### ip/ipsec/statistics

**软件包:** security
**类型:** 设置目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
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