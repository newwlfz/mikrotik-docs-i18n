# 证书

> 本文档介绍 MikroTik RouterOS 中的证书管理菜单，涵盖证书模板创建、密钥大小和用途等配置属性，以及包括 ACME 客户端集成在内的证书管理。

# 证书

## 概述

**子菜单：** `/certificate`

该通用菜单用于管理证书、添加模板、签发证书以及管理 CRL 和 SCEP 客户端。

### 证书模板

证书模板用于准备所需的证书以供签名。

证书模板在证书签名或执行证书请求命令后立即被删除。

```ros
/certificate
add name=CA-Template common-name=CAtemp key-usage=key-cert-sign,crl-sign
add name=Server common-name=server
add name=Client common-name=client
```

打印证书列表：

```ros
[admin@4k11] /certificate> print detail 
Flags: K - private-key; L - crl; C - smart-card-key; A - authority; I - issued, R - revoked; E - expired; T - trusted 
 0         name="CA-Template" key-type=rsa common-name="CAtemp" key-size=2048 subject-alt-name="" days-valid=365 key-usage=key-cert-sign,crl-sign 

 1         name="Server" key-type=rsa common-name="server" key-size=2048 subject-alt-name="" days-valid=365 
           key-usage=digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign,tls-server,tls-client 

 2         name="Client" key-type=rsa common-name="client" key-size=2048 subject-alt-name="" days-valid=365 
           key-usage=digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign,tls-server,tls-client 
```

#### 证书模板属性

在证书模板创建过程中，可以定义和配置多个参数以满足特定需求。

| 属性 | 描述 |
| :-- | :-- |
| **common-name** (*字符串*) | 证书通用名称 |
| **copy-from**(*名称*) | 从中复制常规设置的证书名称 |
| **country** (*字符串*) | 证书颁发者国家 |
| **days-valid** (*天数* 默认值：**365**) | 证书签名后的有效天数 |
| **digest-algorithm** (*md5 \| sha1 \| sha256 \| sha384 \| sha512* 默认值：**sha256**) | 用于签署证书的哈希算法。 |
| **key-size** (*1024* \| *1536* \| *2048* \| *4096* \| *8192* \| *prime256v1* \| *secp384r1* \| *secp521r1* 默认值：**2048**) | 证书公钥大小 |
| **key-usage** (*code-sign* \| *crl-sign* \| *decipher-only* \| *dvcs* \| *encipher-only* \| *key-cert-sign* \| *ocsp-sign* \| *tls-client* \| *content-commitment* \| *data-encipherment* \| *digital-signature* \| *email-protect* \| *key-agreement* \| *key-encipherment* \| *timestamp* \| *tls-server* 默认值：**digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign,tls-server,tls-client**) | 证书用途 |
| **locality** (*字符串*) | 证书颁发者所在地 |
| **name** (*字符串*) | 证书名称 |
| **organization** (*字符串*) | 证书颁发者组织 |
| **state** (*字符串*) | 证书颁发者州/省 |
| **subject-alt-name** (*DNS: \| IP: \| email:*) | 证书主题备用名称 |
| **trusted** (*no \| yes*) | 是否信任证书。如果为 *yes*，证书将用于主机证书验证。 |
| **trust-store**(*all* \| *capsman* \| *dns* \| *email* \| *ipsec* \| *mqtt* \| *openflow* \| *radius* \| *sstp* \| *userman* \| *www* \| *api* \| *container* \| *dot1x* \| *fetch* \| *lora* \| *netwatch* \| *ovpn* \| *tr069* \| *wpa-eap* \| *wiliot* \| *logging* 默认值：**all**) | 指定可以使用特定证书进行证书验证或信任链创建的服务（www、sstp）。 |
| **unit** (*字符串*) | 证书颁发者组织单位 |

### 证书属性

对于已签名的证书，大多数属性是只读的，但 *name、trusted* 和 *trust-store* 除外。

| 属性 | 描述 |
| :-- | :-- |
| **acme-status** *(字符串)* | ACME 客户端状态 |
| **common-name** (*字符串*) | 证书通用名称 |
| **copy-from**(*名称*) | 从中复制常规设置的证书名称 |
| **country** (*字符串*) | 证书颁发者国家 |
| **days-valid** (*天数*) | 证书签名后的有效天数 |
| **digest-algorithm** (*md5 \| sha1 \| sha256 \| sha384 \| sha512*) | 用于签署证书的哈希算法 |
| **directory-url** *(字符串)* | ACME 客户端目录 URL |
| **domain-names** *(字符串)* | ACME 客户端使用的域名 |
| **key-size** (*1024* \| *1536* \| *2048* \| *4096* \| *8192* \| *prime256v1* \| *secp384r1* \| *secp521r1*) | 证书公钥大小 |
| **key-usage** (*code-sign* \| *crl-sign* \| *decipher-only* \| *dvcs* \| *encipher-only* \| *key-cert-sign* \| *ocsp-sign* \| *tls-client* \| *content-commitment* \| *data-encipherment* \| *digital-signature* \| *email-protect* \| *key-agreement* \| *key-encipherment* \| *timestamp* \| *tls-server*) | 证书用途 |
| **locality** (*字符串*) | 证书颁发者所在地 |
| **organization** (*字符串*) | 证书颁发者组织 |
| **revoked** *(日期)* | 证书吊销时间（仅适用于在特定设备上签名并吊销的证书） |
| **state** (*字符串*) | 证书颁发者州/省 |
| **subject-alt-name** (*DNS \| IP \| email*) | 证书主题备用名称 |
| **trusted** (*no \| yes*) | 是否信任证书。如果为 *yes*，证书将用于主机证书验证。 |
| **trust-store**(*all* \| *capsman* \| *dns* \| *email* \| *ipsec* \| *mqtt* \| *openflow* \| *radius* \| *sstp* \| *userman* \| *www* \| *api* \| *container* \| *dot1x* \| *fetch* \| *lora* \| *netwatch* \| *ovpn* \| *tr069* \| *wpa-eap* \| *wiliot* \| *logging*) | 指定可以使用特定证书进行证书验证或信任链创建的服务（www、sstp）。 |
| **unit** (*字符串*) | 证书颁发者组织单位 |
| **serial-number** (*字符串*) | 证书序列号 |
| **fingerprint** (*字符串*) | 证书指纹 |
| **akid** (*字符串*) | 证书颁发机构 ID |
| **skid** (*字符串*) | 证书主题 ID |
| **issuer** (*字符串*) | 证书颁发机构 |
| **invalid-before** *(日期)* | 证书生效前的日期和时间（有效期开始日期）。 |
| **invalid-after** *(日期)* | 证书失效后的日期和时间（到期日期）。 |
| **expires-after** *(时间)* | 到期前剩余时间 |
| **key-type** (*字符串*) | 私钥类型 |
| **ca** *(字符串)* | CA 证书名称（仅显示在特定设备上签名的证书） |

:::warning
如果 CA 证书被移除，证书链中的所有已签发证书也将被移除。
:::

### 签署证书

证书需要被签署。在以下示例中，我们将签署证书并为服务器证书添加 CRL URL：

```ros
/certificate 
sign CA-Template 
sign Client      
sign Server ca-crl-host=192.168.88.1 name=ServerCA

```

让我们检查证书是否已签署：

```ros
[admin@MikroTik] /certificate> print
Flags: K - private-key; L - crl; A - authority; T - trusted
Columns: NAME, COMMON-name, FINGERPRINT
#        NAME         COMMON  FINGERPRINT                                                     
0  K AT  CA-Template  CAtemp  0c7aaa7607a4dde1bbf33deaae6be7bac9fe4064ba47d64e8a73dcefad6cfc38
1  K AT  Client       client  b3ff25ecb166ea41e15733a7493003f3ea66310c10390c33e98fe32364c3659f
2  KLAT  ServerCA     server  152b88c9d81f4b765a59e2302e01efd1fbf11ceeed6e59f4974e87787a5bb980

```

视频示例请点击 [此处。](http://youtube.com/watch?v=i2A3YIQKfwY)

:::warning
密钥签名过程的时间取决于特定证书的密钥大小。对于 4k 及以上的值，在 CPU 性能较低的设备上签署此特定证书可能需要相当长的时间。
:::

### 导出证书

可以以 PEM 或 PKCS12 两种格式导出带密钥的客户端证书和 CA 证书。

| 属性 | 描述 |
| :-- | :-- |
| **export-passphrase** (*字符串* 默认值：**none**) *[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用于导出证书私钥加密的密码短语。 |
| **file-name** (*字符串* 默认值：**cert\_export\_[证书名称].crt/key/pkcs12**) | 导出的证书文件名。 |
| **type** (*pem \| pkcs12* 默认值：**pem**) | 导出的证书类型。 如果是 PEM，证书将以 CRT 扩展名导出，如果指定了 export-passphrase，还将导出一个加密的私钥 KEY 文件。 如果是 PKCS12，证书将以 P12 扩展名导出，如果指定了 export-passphrase，导出的证书将包含加密的私钥。PKCS12 文件使用 AES 加密。 |

```ros
/certificate 
export-certificate CA-Template 
export-certificate ServerCA export-passphrase=yourpassphrase
export-certificate Client export-passphrase=yourpassphrase
```

导出的证书可在 */file* 部分下找到：

```ros
[admin@MikroTik] > file print
Columns: NAME, TYPE, SIZE, CREATION-TIME
#  NAME                         TYPE        SIZE  CREATION-TIME       
0  skins                        directory         2019-01-19 00:00:04
1  flash                        directory         2019-01-19 01:00:00
2  pub                          directory         2019-01-19 02:42:16
3  cert_export_CA-Template.crt  .crt file   1119  2019-01-19 04:15:21
4  cert_export_ServerCA.crt     .crt file   1229  2019-01-19 04:15:42
5  cert_export_ServerCA.key     .key file   1858  2019-01-19 04:15:42
6  cert_export_Client.crt       .crt file   1164  2019-01-19 04:15:55
7  cert_export_Client.key       .key file   1858  2019-01-19 04:15:55
```

:::warning
导出证书需要“敏感”用户策略。
:::

### 导入证书

要导入证书，必须使用其中一种文件上传方法将证书上传到设备。

证书必须作为文件导入。

支持 PEM、DER、CRT、PKCS12 格式。PKCS12 导入支持 AES 和 3DES 解密。

| 属性 | 描述 |
| :-- | :-- |
| **name** (*字符串* 默认值：**file-name\_number**) | 将在证书管理器中显示的证书名称 |
| **file-name** (*字符串*) | 将要导入的文件名 |
| **passphrase** (*字符串* 默认值：**none**) *[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 文件密码短语（如果有） |
| **trusted** (*yes \| no* 默认值：yes) | 为导入的证书添加 *trusted* 标志 |
| **trust-store**(*all* \| *capsman* \| *dns* \| *email* \| *ipsec* \| *mqtt* \| *openflow* \| *radius* \| *sstp* \| *userman* \| *www* \| *api* \| *container* \| *dot1x* \| *fetch* \| *lora* \| *netwatch* \| *ovpn* \| *tr069* \| *wpa-eap* \| *wiliot* \| *logging* 默认值：**all**) | 指定可以使用特定证书进行证书验证或信任链创建的服务（www、sstp）。 |

```ros
[admin@MikroTik] > /certificate/import file-name=certificate_file_name name=name_example passphrase=file_passphrase
     certificates-imported: 2
     private-keys-imported: 1
            files-imported: 1
       decryption-failures: 0
  keys-with-no-certificate: 0

[admin@MikroTik] > /certificate/print 
Flags: K - PRIVATE-KEY; T - TRUSTED
Columns: NAME, COMMON-NAME
#    NAME            COMMON-NAME                                                  
0 KT name_example    cert    
1  T name_example_1  ca   
```

### CRL

RouterOS 支持证书吊销列表（CRL）检查。

默认情况下，不使用 CRL，也不验证证书的吊销状态。

在 [证书设置](#settings) 中启用 `crl-use=yes` 以使系统根据其 CRL 验证链中的每个证书，并设置 `crl-download=yes` 让 RouterOS 自动下载和更新 CRL。

可以通过提供 CRL URL 手动添加 CRL，也可以在导入包含 CRL 分发点的证书时动态添加。

| 属性 | 描述 |
| :-- | :-- |
| **akid** (*字符串*) | CRL 颁发机构 ID |
| **cert**(*字符串*) | 从中添加 CRL 分发点的证书（来自证书库） |
| **dynamic** (*标志*) | CRL 是否为动态添加 |
| **expired** (*标志*) | CRL 是否已过期 |
| **fingerprint** (*字符串*) | CRL 指纹 |
| **Invalid** (*标志*) | CRL 是否无效（未更新） |
| **last-update** (*日期*) | 上次 CRL 更新的日期和时间 |
| **next-update** (*日期*) | 下次 CRL 更新的日期和时间 |
| **num** (*整数*) | CRL 编号 |
| **removed** (*整数*) | 已吊销证书的数量 |
| **signature** (*字符串*) | CRL 签名 |
| **url** (*字符串*) | CRL URL |
| **num** (*整数*) | CRL 编号 |

### 设置

`/certificate/settings` 允许配置 [证书吊销列表](#crl) 和 [内置信任库](#内置信任库颁发机构) 设置。

| 属性 | 描述 |
| :-- | :-- |
| **builtin-trust-store** (*all* \| *default* \| *capsman* \| *dns* \| *email* \| *ipsec* \| *mqtt* \| *openflow* \| *radius* \| *sstp* \| *userman* \| *www* \| *api* \| *container* \| *dot1x* \| *fetch* \| *lora* \| *netwatch* \| *ovpn* \| *tr069* \| *wpa-eap* \| *wiliot* \| *logging* \| *untrusted* 默认值：**default**) | 可以使用 [内置信任库颁发机构](#内置信任库颁发机构) 进行证书验证的服务。 当前默认值：fetchmqttemailnetwatchcontainerloradnswwwreverse-proxy |
| **crl-download** (*yes \| no* 默认值：**no**) | 是否自动下载/更新 CRL |
| **crl-store** (*ram \| system* 默认值：**ram**) | 存储下载的 CRL 信息的位置。 对于具有“trusted=yes”的证书，CRL 将每小时使用 http 协议自动更新（目前不支持 ldap 和 ftp） |
| **crl-use** (*yes \| no* 默认值：**no**) | 是否使用 CRL |

:::warning
如果 `/certificate/settings/set crl-use` 设置为 *`yes`*，RouterOS 将检查证书链中每个证书的 CRL，因此，应将整个证书链安装到设备中——从根 CA 开始，包括中间 CA（如果有），以及用于特定服务的证书。
:::

关于导入根证书的 [示例](http://youtube.com/watch?v=q9oMO3_jvBU)。

## ACME 客户端

ACME 客户端通过 ACME 自动获取和续订多个 TLS 证书。

要通过 CLI 添加新的 ACME 客户端，请使用命令 `/certificate/add-acme`。

现有的 ACME 客户端会出现在证书视图中，并标记有 `a`（acme-manage）标志。

域名必须解析到路由器，并且 TCP 端口 80 必须可从 WAN 访问（使用 HTTP-01 质询）。对于 IP Cloud `<id>.sn.mynetname.net` 域名，则使用 DNS-01 质询。

当证书有效期过去 80% 时，证书会自动续订。

如果在初始设置期间未获取证书，则必须添加新的 ACME 客户端。

### 属性

| 属性 | 描述 |
| :-- | :-- |
| **directory-url** (*字符串*) | ACME 目录 URL |
| **domain-names** (*字符串*) | 逗号分隔的域名列表 |
| **eab-hmac-key** (*字符串*) | 用于 ACME 外部账户绑定的 HMAC 密钥 |
| **eab-kid** (*字符串*) | 密钥标识符 |
| **name** (*字符串*) | ACME 客户端名称 |

### 手动 ACME 续订

要手动触发 ACME 证书续订：

```ros
/certificate/acme-renew [name]
```

例如：

```ros
/certificate/acme-renew numbers=0
```

### Let's Encrypt 证书

要获取具有自动证书续订功能的 Let's Encrypt 证书，您必须使用 `domain-names` 参数手动提供域名：

```ros
/certificate/add-acme domain-names=router.example.com
```

要为 [IP Cloud](/docs/network-management/cloud#ddns) 名称（例如，`example.sn.mynetname.net`）生成 Let's Encrypt 证书，请将 `/ip/cloud` 菜单中的 `dns-name` 作为域名提供，或使用 `[/ip/cloud/get dns-name]` 内联读取：

```ros
/certificate/add-acme domain-names=[/ip/cloud/get dns-name]
```

:::info
如果未提供 `directory-url`，则使用 Let's Encrypt 目录。
:::

## SCEP

SCEP 使用 HTTP 协议和 base64 编码的 GET 请求。大多数请求没有身份验证和加密，但是，重要的请求可以在必要时受到保护（使用收到的公钥进行加密或签名）。

RouterOS 中的 SCEP 客户端将：

- 从 CA 服务器或 RA（如果使用）获取 CA 证书。
- 用户应比较 CA 证书的指纹，或确认其来自正确的服务器。
- 使用临时密钥生成自签名证书。
- 向服务器发送证书请求。
- 如果服务器响应状态为 x，则客户端持续请求，直到服务器发送错误或批准。

SCEP 服务器仅支持签发一张证书。RouterOS 还支持 renew 和 next-ca 选项：

- renew - 使用相同的 CA 自动续订旧证书的可能性。
- next-ca - 将当前 CA 证书更换为新证书的可能性。

客户端轮询服务器以获取任何更改，如果服务器通告 next-ca 可用，则客户端可以请求下一个 CA，或等待 CA 即将过期然后请求 next-ca。

默认情况下，如果服务器通告支持，RouterOS 客户端将尝试使用 POST、AES 和 SHA256。如果不支持上述算法，则客户端将尝试使用 3DES、DES 和 SHA1、MD5。

SCEP 证书在其有效期的 3/4 过去后自动续订。

## 内置信任库颁发机构

RouterOS 包含一个内置根证书颁发机构列表，特定服务可以使用这些颁发机构进行主机证书验证。

SMIPS 设备具有 [精简的内置 CA 信任库](#smips-内置-ca)。

可以使用内置根证书颁发机构的服务列表可在 [设置](#settings) 部分找到。

可以在无需手动导入相关根证书的情况下，使用带证书验证的 [DoH](../network-management/dns.md)。

内置根证书颁发机构列表可在 系统 → 证书 → 内置 CA 中访问，或通过 `/certificate/builtin/` 访问。

### 内置 CA 列表

以下内置 CA 列表适用于除 SMIPS 之外的所有架构。

| 组织 | 通用名称 | 主题 ID |
| :-- | :-- | :-- |
| Amazon | Amazon Root CA 1 | `8418CC8534ECBC0C94942E08599CC7B2104E0A08` |
| DigiCert Inc | DigiCert Assured ID Root CA | `45EBA2AFF492CB82312D518BA7A7219DF36DC80F` |
| DigiCert Inc | DigiCert Assured ID Root G2 | `CEC34AB99955F2B8DB60BFA97EBD56B59736A7D6` |
| DigiCert Inc | DigiCert Assured ID Root G3 | `CBD0BDA9E1980551A14D37A28379CE8D1D2AE484` |
| DigiCert Inc | DigiCert Global Root CA | `03DE503556D14CBB66F0A3E21B1BC397B23DD155` |
| DigiCert Inc | DigiCert Global Root G2 | `4E2254201895E6E36EE60FFAFAB912ED06178F39` |
| DigiCert Inc | DigiCert Global Root G3 | `B3DB48A4F9A1C5D8AE3641CC1163696229BC4BC6` |
| DigiCert Inc | DigiCert High Assurance EV Root CA | `B13EC36903F8BF4701D498261A0802EF63642BC3` |
| DigiCert, Inc. | DigiCert TLS ECC P384 Root G5 | `C151455059AB3EE72C5AFA2022120780887C116A` |
| DigiCert, Inc. | DigiCert TLS RSA4096 Root G5 | `51331CED3640AF17D325CD6968F2AF4E233EB341` |
| DigiCert Inc | DigiCert Trusted Root G4 | `ECD7E382D2715D644CDF2E673FE7BA98AE1C0F4F` |
| GlobalSign | GlobalSign | `3DE629489BEA07CA21444A26DE6EDED283D09F59` |
| GlobalSign nv-sa | GlobalSign Root CA | `607B661A450D97CA89502F7D04CD34A8FFFCFD4B` |
| GlobalSign | GlobalSign | `8FF04B7FA82E4524AE4D50FA639A8BDEE2DD1BBC` |
| GlobalSign | GlobalSign | `AE6C05A39313E2A2E7E2D71CD6C7F07FC86753A0` |
| GlobalSign nv-sa | GlobalSign Root E46 | `310A908FB6C69DD2444B80B5A2E61FB1124F1B95` |
| GlobalSign nv-sa | GlobalSign Root R46 | `035CAB738187A8CCB0A6D594E2369649FF05992C` |
| The Go Daddy Group, Inc. | | `D2C4B0D291D44C1171B361CB3DA1FEDDA86AD4E3` |
| GoDaddy.com, Inc. | Go Daddy Root Certificate Authority - G2 | `3A9A8507106728B6EFF6BD05416E20C194DA0FDE` |
| Sectigo Limited | Sectigo Public Server Authentication Root E46 | `D122DA4C59F14B5F2638AA9DD6EEEB0DC3FBA961` |
| Sectigo Limited | Sectigo Public Server Authentication Root R46 | `5673586495F9921AB0122A046279A14015882149` |
| The USERTRUST Network | USERTrust ECC Certification Authority | `3AE10986D4CF19C29676744976DCE035C663639A` |
| The USERTRUST Network | USERTrust RSA Certification Authority | `5379BF5AAA2B4ACF5480E1D89BC09DF2B20366CB` |
| Internet Security Research Group | ISRG Root X1 | `79B459E67BB6E5E40173800888C81A58F6E99B6E` |
| Internet Security Research Group | ISRG Root X2 | `7C4296AEDE4B483BFA92F89E8CCF6D8BA9723795` |
| ISRG | Root YE | `A3C8265A8EA14CD03563FC9B23C83AAE56F34F56` |
| ISRG | Root YR | `DEE75B60D0226D40287D3F0D01FEA4B552B45194` |

### SMIPS 内置 CA

SMIPS 设备具有精简的内置 CA 信任库：

| 组织 | 通用名称 | 主题 ID |
| :-- | :-- | :-- |
| DigiCert Inc | DigiCert Global Root G2 | `4E2254201895E6E36EE60FFAFAB912ED06178F39` |
| Internet Security Research Group | ISRG Root X1 | `79B459E67BB6E5E40173800888C81A58F6E99B6E` |
| Internet Security Research Group | ISRG Root X2 | `7C4296AEDE4B483BFA92F89E8CCF6D8BA9723795` |
| ISRG | Root YE | `A3C8265A8EA14CD03563FC9B23C83AAE56F34F56` |
| ISRG | Root YR | `DEE75B60D0226D40287D3F0D01FEA4B552B45194` |