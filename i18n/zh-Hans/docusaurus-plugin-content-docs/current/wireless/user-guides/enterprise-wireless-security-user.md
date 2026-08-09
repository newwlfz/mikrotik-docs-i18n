# 使用 User Manager v5 实现企业级无线安全

> 本指南介绍如何将 MikroTik RouterOS User Manager v5 配置为企业无线网络的认证服务器，涵盖安装、用于 PEAP 和 EAP-TLS 等安全 EAP 方法的 TLS 证书生成，以及基于证书认证的接入点设置。

# 使用 User Manager v5 实现企业级无线安全

User Manager 版本 5（适用于 RouterOS v7）支持通过可扩展认证协议（EAP）进行用户认证。

本指南将说明将 User Manager v5 配置为 MikroTik 无线接入点认证服务器所需的步骤，为用户提供 PEAP 和 EAP-TLS 认证方法。

本指南假设一台独立设备运行 User Manager，网络地址为 10.0.0.10，并有两个接入点——一个位于 10.0.0.11，另一个位于 10.0.0.12。

## 安装 User Manager

User Manager v5 可在 [RouterOS v7 最新版本](https://mikrotik.com/download) 的“Extra packages”归档中找到。

下载适合相应 CPU 架构的归档文件，解压后将 User Manager 包上传至路由器并重启。

## 生成 TLS 证书

使用安全 EAP 方法时，客户端设备（请求方）在发送自身凭据之前会验证认证服务器的身份。  
为此，认证服务器需要具备 TLS 证书。

该证书应满足以下要求：

1. 必须有效，并由客户端设备信任的证书颁发机构（CA）签名。
2. 在通用名称（CN）和主题备用名称（SAN）字段中包含完全限定域名（FQDN）。
3. 具有扩展密钥用法（EKU）属性，表明其被授权用于 TLS 服务器认证。
4. 有效期不超过 825 天。

EAP-TLS 方法要求客户端设备具备 TLS 证书（而非密码）。

要被视为 User Manager 认可的有效证书，客户端证书必须满足以下要求：

1. 必须有效，并由运行 User Manager 的设备信任的颁发机构签名。
2. 在主题备用名称（SAN）字段中包含用户名。为向后兼容，也可在 CN 字段中添加。更多信息请参阅：[https://datatracker.ietf.org/doc/html/rfc5216#section-5.2](https://datatracker.ietf.org/doc/html/rfc5216#section-5.2)

最后，WPA3 企业版规范包含一种额外的安全模式，可提供 192 位加密安全性。

该模式要求使用 EAP-TLS，且证书需满足以下条件：

1. 使用 P-384 椭圆曲线密钥或长度至少为 3072 位的 RSA 密钥。
2. 使用 SHA384 作为摘要（哈希）算法。

为简洁起见（并展示 RouterOS 的更多功能），本指南将演示如何在运行 User Manager 的设备上生成所有证书。但在大规模企业环境中，认证服务器和客户端设备应各自在本地生成私钥和证书签名请求（CSR），然后将 CSR 上传至证书颁发机构进行签名。

**在运行 User Manager 的设备上执行的命令：**

```ros
# 生成证书颁发机构（CA）
/certificate
add name=radius-ca common-name="RADIUS CA" key-size=secp384r1 digest-algorithm=sha384 days-valid=1825 key-usage=key-cert-sign,crl-sign
sign radius-ca ca-crl-host=radius.mikrotik.test
# 为 User Manager 生成服务器证书
add name=userman-cert common-name=radius.mikrotik.test subject-alt-name=DNS:radius.mikrotik.test key-size=secp384r1 digest-algorithm=sha384 days-valid=800 key-usage=tls-server
sign userman-cert ca=radius-ca
# 生成客户端证书
add name=maija-client-cert common-name=maija@mikrotik.test subject-alt-name=email:maija@mikrotik.test key-usage=tls-client days-valid=800 key-size=secp384r1 digest-algorithm=sha384
sign maija-client-cert ca=radius-ca
# 导出 CA 的公钥以及生成的客户端私钥和证书，以便分发给客户端设备
export-certificate radius-ca file-name=radius-ca
# 导出时需要口令才能包含私钥
export-certificate maija-client-cert type=pkcs12 export-passphrase="true zebra capacitor ziptie"
```

## 配置 User Manager

**在运行 User Manager 的设备上执行的命令：**

```ros
# 启用 User Manager 并指定使用的证书
/user-manager
set enabled=yes certificate=userman-cert
# 启用 CRL 检查，避免接受已撤销的用户证书
/certificate/settings
set crl-download=yes crl-use=yes
# 添加接入点
/user-manager/router
add name=ap1 address=10.0.0.11 shared-secret="请使用安全密码生成器生成此密码"
add name=ap2 address=10.0.0.12 shared-secret="请同样使用安全密码生成器生成此密码"
# 限制允许的认证方法
/user-manager/user/group
set [find where name=default] outer-auths=eap-tls,eap-peap
add name=certificate-authenticated outer-auths=eap-tls
# 添加用户
/user-manager/user
add name=maija@mikrotik.test group=certificate-authenticated
add name=paija@mikrotik.test group=default password="right mule accumulator nail"
```

:::info
使用 CAPsMAN 控制器配置 AP 时，可以使用下方所示的完全相同配置来配置 CAP。只需为 CAP 配置 SSID 和 wpa2-eap/wpa3-eap 认证类型即可。  
使用 CAPsMAN 时，CAPsMAN 应作为 `/radius` 客户端（而非下方独立设置示例中所示的 AP）。
:::

## 配置接入点

### 运行常规 wireless 包的 AP

**在 ap1 上执行的命令：**

```ros
# 配置 radius 客户端
/radius
add address=10.0.0.10 secret="请使用安全密码生成器生成此密码" service=wireless timeout=1s
/radius/incoming
set accept=yes
# 添加安全配置文件并将其应用于无线接口
/interface/wireless/security-profile
add name=radius mode=dynamic-keys authentication-types=wpa2-eap
/interface/wireless
set [find] security-profile=radius
```

### 运行 wifi-qcom 包的 AP

**在 ap2 上执行的命令：**

```ros
# 配置 radius 客户端
/radius
add address=10.0.0.10 secret="请同样使用安全密码生成器生成此密码" service=wireless timeout=1s
/radius/incoming
set accept=yes
# 配置启用的认证类型。也可以通过安全配置文件完成，但请注意，接口属性（如果指定）会覆盖配置文件属性
/interface/wifi/set [find] security.authentication-types=wpa2-eap,wpa3-eap
```

wifi-qcom AP 也可以配置为使用更安全的 wpa3-eap-192 模式，但请注意，这要求所有客户端设备支持 GCMP-256 密码套件并使用 EAP-TLS 认证。

## 客户端设备配置说明

### Windows

在 Windows 中手动安装 CA 时，请务必将其显式放置在“受信任的根证书颁发机构”证书存储中。系统不会自动将其放置在该位置。

### Android

连接到使用 EAP 认证的网络时，Android 设备会要求用户指定“域名”。这指的是 RADIUS 服务器 TLS 证书中包含的主机名的预期域名（在我们的示例中为“mikrotik.test”）。

默认情况下，Android 设备使用其内置的根 CA 列表来验证 RADIUS 服务器的证书。使用自有 CA 时，需要在相应的下拉菜单中选择该 CA。

### iOS

Apple iOS 似乎不会实际信任手动导入的 CA 来认证 RADIUS 服务器。除非使用 Apple 专有的“Configurator”工具或经批准的第三方 MDM 工具导入 CA，否则服务器证书将被标记为“不受信任”。