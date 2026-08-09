# RouterOS IPsec 中的 QKD 集成（PPK）

> 本页介绍 RouterOS IPsec 的后量子预共享密钥（PPK）功能，详细说明其与量子密钥分发（QKD）的集成、支持的密钥来源（静态、PSK、QKD）、安全建议以及双设备设置示例。

# RouterOS IPsec 中的 QKD 集成（PPK）

### 1. 引言

本手册介绍 RouterOS IPsec 中的后量子预共享密钥（RFC9867）功能及其与量子密钥分发（QKD）的集成。

PPK 通过使用动态分发或静态配置的密钥，针对量子攻击提供前向安全性。所有 PPK 类型（静态、PSK、QKD）均遵循 RFC 8784 建议：密钥应至少具有 256 位熵，以提供约 128 位的后量子安全性。

RouterOS 支持三种 PPK 来源：

- 静态 PPK — 手动配置的每对等体密钥。
- PSK（预共享密钥）— 一次性生成的密钥，可选仅用于初始 IKE SA。
- QKD — 从 QKD 服务器动态分发的密钥。

动态密钥（PSK/QKD）在使用后被消耗并失效。静态密钥在会话间保持有效，但重复使用会降低安全性。

### ![](https://manual.mikrotik.com/docs/virtual-private-networks/ipsec/img/qkd-integration-in-routeros-ipsec-ppk-01.webp)

### 2. 概念

- **PPK（后量子预共享密钥）：** 在 IKE 协商期间共享的附加密钥，用于抵御量子攻击。
- **QKD：** 基于量子的密钥分发，通过密钥管理实体（KME）提供全新的对称密钥。

#### IKE SA 与 ESP SA

- IKE SA：控制隧道协商。
- ESP SA：承载加密的用户数据。

#### 静态密钥与动态密钥

- 动态：临时 PSK 或 QKD 分发的密钥，使用一次后即丢弃。
- 静态：手动为每个对等体设置，在会话间持续有效。

#### 2.1 RouterOS PPK 来源

| PPK 来源 | 描述 |
| :-- | :-- |
| 静态 | 持久存在、手动配置的密钥。 |
| PSK | 一次性动态生成的预共享密钥。可选仅用于初始 IKE SA（`psk-ike-initial`）。 |
| QKD | 从 QKD 服务器动态获取的密钥，使用后即被消耗。 |

### 3. 安全建议

- 所有 PPK 密钥应满足 RFC 8784 建议：熵 ≥256 位。
- 静态 PPK 密钥在足够长的情况下可提升后量子保护，但重复使用会降低安全性。
- 动态密钥（PSK/QKD）因一次性使用而提供更强的安全性。同步失败可能导致密钥失同步。

### 4. 双设备设置概述

本手册重点介绍包含两台设备的最小化设置：

| 角色 | 设备 | 功能 |
| :-- | :-- | :-- |
| 服务器 | RouterOS | 承载 IPsec 隧道；提供 QKD/PPK 密钥 |
| 客户端 | ROS/LibreSwan | 使用 QKD/PPK 连接服务器 |

RouterOS 服务器可作为 KME 的 QKD 客户端，因此无需第三台设备。

```routeros
# 向远端对等体推送配置的示例（IPsec）
/ip ipsec peer
add address=192.168.88.1/32 name=Server exchange-mode=ike2
/ip ipsec proposal
set [ find default=yes ] auth-algorithms=sha256 enc-algorithms=aes-256-gcm
```

### 5. 配置对象

#### 5.1 证书

QKD 需要：

- CA 证书（用于验证服务器）。
- SAE 客户端证书（用于向 QKD 服务器进行身份验证）。

```
/certificate/import file-name=ca.crt.pem
/certificate/import file-name=sae-server.crt.pem
/certificate/import file-name=sae-server.key.pem

```

#### 5.2 PSK 示例

生成用于 PPK 的一次性 PSK：

```
/ip/ipsec/key/psk/generate count=10 key-size=32

```

- **count** → 要生成的 PSK 数量。
- **key-size** → 每个密钥的大小（字节）（32 字节 = 256 位）。

#### 5.3 QKD 密钥管理器

RouterOS 服务器可作为 QKD 客户端：

```
/ip/ipsec/key/qkd/set address=10.2.3.4:8020 \
    cache-size=1 \
    certificate=sae-server \
    key-size=32 \
    kme-id=server-kme-id \
    peer-sae-id=client-sae-id

```

参数说明：

| 参数 | 描述 |
| :-- | :-- |
| cache-size | IPsec 将从 QKD 服务器预取的密钥数量。 |
| cache-state | 当前缓存并可用的密钥数量。 |
| key-size | 请求的每个密钥的大小（字节）（例如，32 字节 = 256 位）。 |
| kme-id | 用于证书验证。如果未指定，则不验证 KME 身份。 |
| peer-sae-id | 对等体 SAE 的标识符。 |

#### 5.4 配置文件和对等体

```
/ip/ipsec/profile/add name=qkd-profile ppk=qkd
/ip/ipsec/peer/add address=10.2.1.2 exchange-mode=ike2 \
    name=peer-client profile=qkd-profile proposal-check=obey
/ip/ipsec/identity/add peer=peer-client profile=qkd-profile

```

配置文件的 PPK 选项：

| 选项 | 描述 |
| :-- | :-- |
| no | 禁用 PPK。 |
| psk | 用于 IKE 和 ESP 重新密钥的一次性 PSK。 |
| psk-ike-initial | 仅用于初始 IKE SA 的 PSK（由 `psk-ike-only` 重命名而来）。 |
| qkd | 从 QKD 服务器获取密钥。 |

#### 5.5 提议 / 策略

```
/ip/ipsec/proposal/add name=qkd-proposal auth-algorithms=sha256 \
    enc-algorithms=aes-256-gcm pfs-group=modp2048
/ip/ipsec/policy/add src-address=10.1.0.0/24 dst-address=10.2.0.0/24 \
    peer=peer-client proposal=qkd-proposal tunnel=yes

```

### 6. 行为特性

- 动态密钥：从 `/ip/ipsec/key/psk/` 或 QKD 服务器获取，使用一次后即被删除。
- 静态密钥：为每个对等体配置，可重复使用。
- 一次性动态密钥提供最强的保护，但需要同步。
- 静态回退可确保隧道建立，但密钥应足够长（熵 ≥256 位）。
- PPK 使用可选限制为仅用于 IKE SA（`psk-ike-initial`），以减少密钥消耗。

### 7. 调试与故障排除

要验证 QKD 集成和密钥获取，请启用 IPsec 调试日志：

```
/system/logging/add topics=ipsec,debug action=memory

```

显示 QKD 密钥获取的示例调试输出：

```
2025-10-11 17:32:38 ipsec,debug,packet POST
2025-10-11 17:32:38 ipsec,debug,packet Host: 10.2.3.4\r\n
2025-10-11 17:32:38 ipsec,debug,packet {"number":1,"size":16}
2025-10-11 17:32:38 ipsec,debug,packet HTTP/1.1 200 OK\r\n
2025-10-11 17:32:38 ipsec,debug,packet {"keys":[{"key_ID":"37f4c842-dd82-4c49-8dfc-52a3793e5331","key":"m/JIEIUCzAE="}]}
2025-10-11 17:32:38 ipsec,debug,packet qkd: add to cache key 37f4c842-dd82-4c49-8dfc-52a3793e5331: 9bf24
```

如果密钥未添加到缓存中，请检查与 KME 的网络连接、证书验证以及 `kme-id` 和 `peer-sae-id` 配置是否正确。

### 8. 配置导出示例（双设备设置）

#### RouterOS 服务器

```
/ip/ipsec/key/qkd
set address=10.2.3.4:8020 cache-size=1 certificate=sae-server key-size=32 \
    kme-id=server-kme-id peer-sae-id=client-sae-id
/ip/ipsec/profile/add name=qkd-profile ppk=qkd
/ip/ipsec/proposal/add name=qkd-proposal auth-algorithms=sha256 enc-algorithms=aes-256-gcm pfs-group=modp2048
/ip/ipsec/peer/add address=10.2.1.2 exchange-mode=ike2 name=peer-client profile=qkd-profile proposal-check=obey
/ip/ipsec/identity/add peer=peer-client profile=qkd-profile
/ip/ipsec/policy/add src-address=10.1.0.0/24 dst-address=10.2.0.0/24 peer=peer-client proposal=qkd-proposal tunnel=yes

```

#### 客户端设备

```
/ip/ipsec/key/qkd
set address=10.2.3.4:8020 cache-size=1 certificate=sae-client key-size=32 \
    kme-id=client-kme-id peer-sae-id=server-sae-id
/ip/ipsec/profile/add name=qkd-profile ppk=qkd
/ip/ipsec/proposal/add name=qkd-proposal auth-algorithms=sha256 enc-algorithms=aes-256-gcm pfs-group=modp2048
/ip/ipsec/peer/add address=10.2.1.1 exchange-mode=ike2 name=peer-server profile=qkd-profile proposal-check=obey
/ip/ipsec/identity/add peer=peer-server profile=qkd-profile
/ip/ipsec/policy/add src-address=10.2.0.0/24 dst-address=10.1.0.0/24 peer=peer-server proposal=qkd-proposal tunnel=yes

```

### 9. 参考资料

- IETF 草案：IKEv2 后量子 PPK：[https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-qr-alt/](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-qr-alt/)
- [https://datatracker.ietf.org/doc/html/rfc9867](https://datatracker.ietf.org/doc/html/rfc9867)

### 备注

#### QKD 作为分发机制

- RouterOS 中的 QKD 本身并非新的加密方法，而是一种**密钥分发机制**。
- 它通过**密钥管理实体（KME）** 提供动态生成的密钥，双方对等体均可安全获取。

#### 动态来源与静态来源

- *动态来源*：QKD 分发的密钥、来自 `/ip/ipsec/key/psk/` 的一次性 PSK。
- *静态来源*：为每个对等体配置的静态 PPK 密钥。
- 建议：长期安全优先使用**动态密钥**；保留**静态回退**以防止动态密钥耗尽时隧道中断。

#### 安全指南（RFC 8784）

- 后量子预共享密钥应包含**至少 256 位熵**，以提供 128 位后量子安全性。
- 仅使用单个静态密钥保护 IKE SA 是可行的，但重复使用存在风险。

#### 运维注意事项

- **密钥耗尽**：在激进的重新密钥（IKE + ESP）过程中，一次性 PSK 消耗较快。QKD 通过持续提供新密钥来避免此问题。
- **中心辐射型拓扑**：动态 PSK 需要对等体关联，以避免各分支之间的失同步。
- **回退行为**：确保系统在动态密钥不可用时能够平滑切换到静态 PPK。

#### 兼容性说明

- **RouterOS - RouterOS**：支持 PSK 和 QKD PPK。
- **RouterOS - LibreSwan**：支持静态 PPK；动态 PSK 可能需要自定义构建。
- **RouterOS - StrongSwan**：需要适配，因为不同草案版本中的标识符存在差异。