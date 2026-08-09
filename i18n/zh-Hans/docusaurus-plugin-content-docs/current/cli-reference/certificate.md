# certificate

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# certificate

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="K" typ="private-key">私钥</ArgTableRow>
<ArgTableRow arg="L" typ="crl">证书吊销列表</ArgTableRow>
<ArgTableRow arg="C" typ="smart-card-key">智能卡密钥</ArgTableRow>
<ArgTableRow arg="A" typ="authority">证书颁发机构</ArgTableRow>
<ArgTableRow arg="I" typ="issued">已签发</ArgTableRow>
<ArgTableRow arg="R" typ="revoked">已吊销</ArgTableRow>
<ArgTableRow arg="E" typ="expired">已过期</ArgTableRow>
<ArgTableRow arg="T" typ="trusted">受信任</ArgTableRow>
<ArgTableRow arg="a" typ="acme-managed">ACME 管理</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
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

<ArgTable c1="只读参数" c2="类型" c3="描述">
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

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="domain-names" typ="string">逗号分隔的域名列表或通配符域名</ArgTableRow>
<ArgTableRow arg="directory-url" typ="string"></ArgTableRow>
<ArgTableRow arg="eab-kid" typ="string"></ArgTableRow>
<ArgTableRow arg="eab-key-b64" typ="string"></ArgTableRow>
</ArgTable>

## certificate/add-scep

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="ca-identity" typ="string"></ArgTableRow>
<ArgTableRow arg="template" typ="enum"></ArgTableRow>
<ArgTableRow arg="scep-url" typ="string"></ArgTableRow>
<ArgTableRow arg="challenge-password" typ="string"></ArgTableRow>
<ArgTableRow arg="on-smart-card" typ="bool">如果硬件支持，将私钥存储在智能卡上</ArgTableRow>
<ArgTableRow arg="refresh" typ="bool">检查证书有效期，如果过期则刷新</ArgTableRow>
</ArgTable>

## certificate/builtin

**类型：** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
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

<ArgTable c1="只读参数" c2="类型" c3="描述">
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

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="pin" typ="string"></ArgTableRow>
</ArgTable>

## certificate/card-verify

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="pin" typ="string"></ArgTableRow>
</ArgTable>

## certificate/create-certificate-request

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="template" typ="enum"></ArgTableRow>
<ArgTableRow arg="key-passphrase" typ="string"></ArgTableRow>
<ArgTableRow arg="challenge-passphrase" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="progress" typ="string"></ArgTableRow>
</ArgTable>

## certificate/crl

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="E" typ="expired">已过期</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="url" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
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

**类型：** 命令

### certificate/crl/flush

**类型：** 命令

## certificate/enable-ssl-certificate

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="dns-name" typ="string">SSL 证书的域名</ArgTableRow>
<ArgTableRow arg="directory-url" typ="string">ACME 目录 URL</ArgTableRow>
<ArgTableRow arg="eab-hmac-key" typ="string">Base64url 编码的 EAB HMAC 密钥</ArgTableRow>
<ArgTableRow arg="eab-kid" typ="string">EAB 账户 ID</ArgTableRow>
<ArgTableRow arg="reset-private-key" typ="bool">初始化新的私钥</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="progress" typ="string"></ArgTableRow>
</ArgTable>

## certificate/export-certificate

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="export-passphrase" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="bool"></ArgTableRow>
<ArgTableRow arg="file-name" typ="file"></ArgTableRow>
</ArgTable>

## certificate/import

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="file-name" typ="file"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string"></ArgTableRow>
<ArgTableRow arg="trusted" typ="bool">标记为受信任</ArgTableRow>
<ArgTableRow arg="trust-store" typ="alt { enum (all) { all:cerm::trust_store::All }
, ubit () {  }
 }"></ArgTableRow>
<ArgTableRow arg="no-key-export" typ="bool">禁止导出私钥</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="certificates-imported" typ="num"></ArgTableRow>
<ArgTableRow arg="private-keys-imported" typ="num"></ArgTableRow>
<ArgTableRow arg="files-imported" typ="num"></ArgTableRow>
<ArgTableRow arg="decryption-failures" typ="num"></ArgTableRow>
<ArgTableRow arg="keys-with-no-certificate" typ="num"></ArgTableRow>
<ArgTableRow arg="keys-decrypted" typ="num"></ArgTableRow>
</ArgTable>

## certificate/issued-revoke

**类型：** 命令

## certificate/scep-renew

**类型：** 命令

## certificate/scep-server

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="ca-cert" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="next-ca-cert" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="path" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="days-valid" typ="num"></ArgTableRow>
<ArgTableRow arg="request-lifetime" typ="time"></ArgTableRow>
</ArgTable>

### certificate/scep-server/otp

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="E" typ="expired">已过期</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="expires" typ="time"></ArgTableRow>
<ArgTableRow arg="used" typ="bool"></ArgTableRow>
</ArgTable>

#### certificate/scep-server/otp/generate

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="minutes-valid" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="password" typ="string"></ArgTableRow>
</ArgTable>

### certificate/scep-server/ra

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="C" typ="smart-card-key">智能卡密钥</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="server-url" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="template" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="challenge-password" typ="string"></ArgTableRow>
<ArgTableRow arg="ca-identity" typ="string"></ArgTableRow>
<ArgTableRow arg="fingerprint-algorithm" typ="enum (sha256 | sha1 | md5)"></ArgTableRow>
<ArgTableRow arg="ra-path" typ="string"></ArgTableRow>
<ArgTableRow arg="ra-transaction-lifetime" typ="time"></ArgTableRow>
<ArgTableRow arg="on-smart-card" typ="bool">将私钥存储在智能卡上</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="req-fingerprint" typ="string"></ArgTableRow>
<ArgTableRow arg="ca-fingerprint" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

#### certificate/scep-server/ra/renew

**类型：** 命令

### certificate/scep-server/requests

**类型：** 目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
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

**类型：** 命令

## certificate/settings

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="builtin-trust-store" typ="alt { enum (default | all | untrusted) { default:cerm::trust_store::Default, all:cerm::trust_store::All, untrusted:cerm::trust_store::None }
, ubit () {  }
 }">RouterOS 提供的 CA 证书</ArgTableRow>
<ArgTableRow arg="current-defaults" typ="ubit ()"></ArgTableRow>
<ArgTableRow arg="crl-download" typ="bool">自动下载和更新 CRL</ArgTableRow>
<ArgTableRow arg="crl-use" typ="bool">验证信任链时执行 CRL 检查</ArgTableRow>
<ArgTableRow arg="crl-store" typ="enum (system | ram)">CRL 存储位置</ArgTableRow>
</ArgTable>

## certificate/sign

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="ca-crl-host" typ="multi { array-id, string
 }">将 CRL URL 添加到创建的证书中</ArgTableRow>
<ArgTableRow arg="ca-on-smart-card" typ="bool">将 CA 的私钥存储在智能卡上</ArgTableRow>
<ArgTableRow arg="ca" typ="enum">签发 CA</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="progress" typ="string"></ArgTableRow>
</ArgTable>

## certificate/sign-certificate-request

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="ca" typ="enum"></ArgTableRow>
<ArgTableRow arg="file-name" typ="file"></ArgTableRow>
<ArgTableRow arg="days-valid" typ="num"></ArgTableRow>
<ArgTableRow arg="digest-algorithm" typ="enum (md5 | sha1 | sha256 | sha384 | sha512)"></ArgTableRow>
</ArgTable>