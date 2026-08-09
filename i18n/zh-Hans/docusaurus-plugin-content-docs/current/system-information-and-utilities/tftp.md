# TFTP

> 本页面介绍 MikroTik RouterOS 对简单文件传输协议（TFTP）的实现，详细说明 TFTP 服务器访问规则的配置选项，包括 IP 地址范围、文件名处理、块大小限制以及针对客户端请求的正则表达式支持。

# TFTP

简单文件传输协议（Trivial File Transfer Protocol，简称 TFTP）是一种用于传输文件的非常简单的协议。每个非终止数据包都会被单独确认。

**子菜单：** `/ip/tftp`

此菜单包含所有 TFTP 访问规则。如果此菜单中没有规则，则 RouterOS 启动时不会启动 TFTP 服务器。与创建规则时可设置的属性相比，此菜单仅额外显示一个属性。

## 参数

| 属性 | 说明 |
| :-- | :-- |
| **ip-addresses** *(必填)* | 接受为客户端的 IP 地址范围。如果留空，将使用 *0.0.0.0/0* |
| **allow-rollover** *(默认值：No)* | 如果设置为 *yes*，TFTP 服务器将允许序列号在达到最大值时回绕。此选项用于通过 TFTP 服务器支持大文件下载。 |
| **req-filename** | 请求的文件名，以 *正则表达式（regex）* 形式表示。如果字段留空，则默认为 *.\** |
| **real-filename** | 如果 **req-filename** 和 **real-filename** 的值均已设置且有效，则请求的文件名将被替换为匹配的文件。此字段必须设置。如果在 *req-filename* 中指定了多个 *正则表达式*，则可以通过此字段设置哪些表达式应匹配，从而验证此规则。使用多个 *正则表达式* 时的 *real-filename* 格式为 **filename\0\5\6** |
| **allow** (*默认值：yes*) | 如果上述字段已设置，则允许连接。如果为 *no*，连接将被中断 |
| **read-only** (*默认值：no*) | 设置文件是否可写入，如果设置为 "yes"，写入尝试将失败并返回错误 |
| **hits** *(只读)* | 此访问规则条目被使用的次数（只读） |

### 设置

**子菜单：** `/ip/tftp/settings`

此菜单包含所有 TFTP 设置。

| 属性 | 说明 |
| :-- | :-- |
| **max-block-size** (*默认值：4096*) | 最大可接受的块大小值。在传输协商阶段，RouterOS 设备不会协商大于此值的块大小。 |

## 正则表达式

req-filename 字段支持正则表达式，该字段中允许的正则表达式如下：

### 括号 () - 标记子表达式

```
    示例 1 a(sd|fg) 将匹配 asd 或 afg

```

### 星号 "\*" - 匹配前一个符号零次或多次

```
    示例 1 a* 将匹配完全由符号 a 组成的任意长度名称，或空字符串
    示例 2 .* 将匹配任意长度的名称，也匹配空字段
    示例 3 as*df 将匹配 adf、asdf、assdf、asssdf 等

```

### 加号 "+" - 匹配前一个符号一次或多次

```
    示例：as+df 将匹配 asdf、assdf 等

```

### 点号 "." - 匹配任意符号

```
    示例 as.f 将匹配 asdf、asbf、ashf 等

```

### 方括号 [] - 匹配其中任意一个字符

```
    示例 as[df] 将匹配 asd 和 asf

```

### 问号 "?" - 匹配一个符号或零个符号

```
    示例 asd?f 将匹配 asdf 和 asf

```

### 脱字符 "^" - 用于行首，表示行以此开头

### 美元符号 "$" - 表示位于行尾

## 示例

如果请求某个文件，则从名为 sata1 的存储中返回该文件：

```ros
/ip/tftp/add req-filename=file.txt real-filename=/sata1/file.txt allow=yes read-only=yes
```

如果我们希望无论用户请求什么文件，都只提供某个特定 *文件*：

```ros
/ip/tftp/add req-filename=.* real-filename=/sata1/file.txt allow=yes read-only=yes
```

如果用户请求 *aaa.bin* 或 *bbb.bin*，则向其提供 *ccc.bin*：

```ros
/ip/tftp/add req-filename="(aaa.bin)|(bbb.bin)" real-filename="/sata1/ccc.bin\\0" allow=yes read-only=yes
```

:::tip

RouterOS 已收到 TFTP 请求，但客户端却出现传输超时？

某些嵌入式客户端会请求较大的块大小，但无法正确处理分片数据包。对于此类客户端，建议在 RouterOS 端设置 "max-block-size"，或在客户端设置 "blksize"，其值应为网络中最小 MTU 减去 32 字节（IP 头 20 字节、UDP 头 8 字节、TFTP 头 4 字节），如果网络中使用 IP 选项，则还需减去更多字节。

:::