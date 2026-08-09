# API

> 本页介绍 RouterOS 的应用程序编程接口（API），用于与路由器进行安全通信，详细说明语法规则、句子结构、编码方法以及支持的命令（如 login 和 cancel）以进行配置管理。

# API

**应用程序编程接口（API）** 允许用户创建自定义软件解决方案，与 RouterOS 通信，用于信息收集、配置调整和路由器管理。API 严格遵循**命令行界面（CLI）** 的语法。您可以使用它来创建翻译版或自定义配置工具，从而更轻松地运行和管理 RouterOS 路由器。

在尝试建立连接之前，必须启用 API 服务。默认情况下，API 使用 TCP 端口 **8728** 和 **8729**（安全）。

**API-SSL** 服务可以在两种模式下运行：带证书或不带证书。如果在 `/ip service` 设置中未提供证书，客户端必须使用匿名 Diffie-Hellman 密码套件来建立连接。如果服务使用证书，客户端可以建立 TLS 会话。

## 协议

您通过发送句子并接收一个或多个返回句子来与路由器通信。句子是由零长度字终止的单词序列。单词是句子的一部分，以特定方式编码：编码长度后跟数据。当路由器收到完整的句子（命令字、一个或多个属性字以及一个零长度字）时，它会评估并执行该句子，然后形成并返回回复。

### API 句子

句子是与 API 通信的主要对象。

- 空句子将被忽略。
- 句子在收到零长度字后进行处理。
- 在客户端登录之前，可以发送的句子数量和大小有限制。
- 不要依赖属性字的顺序，因为顺序和数量可能会被 `.proplist` 属性更改。

句子结构如下：

- 第一个字必须包含一个*命令字*。
- 句子必须包含一个*零长度字*来终止它。
- 句子可以包含零个或多个*属性字*。属性字的顺序无关紧要。
- 句子可以包含零个或多个*查询字*。查询字的顺序很重要。

:::danger
如果未提供零长度字，路由器将不会开始评估发送的字，并将所有后续输入视为同一句子的一部分。
:::

### API 单词

- 单词被分组为句子。零长度字终止一个句子。
- 每个单词编码为长度后跟相应字节数的内容。
- 该方案允许编码长度最大为 **0xFFFFFFFF**；仅支持四字节长度。
- **len** 字节以最高有效字节优先（网络字节序）发送。
- 如果单词的第一个字节 **>= 0xF8**，则它是保留的控制字节。收到未知控制字节后，API 客户端无法继续，因为它不知道如何解释后续字节。
- 目前，不使用控制字节。

单词的长度编码如下：

| 长度值                        |   # 字节数 | 编码                              |
|:--|--:|:--|
| `0 <= len <= 0x7F`             |            1 | len，最低字节                  |
| `0x80 <= len <= 0x3FFF`        |            2 | len \| 0x8000，两个低字节     |
| `0x4000 <= len <= 0x1FFFFF`    |            3 | len \| 0xC00000，三个低字节 |
| `0x200000 <= len <= 0xFFFFFFF` |            4 | len \| 0xE0000000                  |
| `len >= 0x10000000`            |            5 | 0xF0 和 len 作为四个字节        |

一般来说，*单词* 可以这样描述 `<编码单词长度><单词内容>`。
单词内容可以分为五个部分：*[命令字](#命令字)*、*[属性字](#属性字)*、*[API 属性字](#api-属性字)*、*[查询字](#查询字)* 和 *[回复字](#回复字)*

#### 命令字

句子中的第一个字必须是命令，后跟属性字和零长度或终止字。命令字的名称必须以斜杠（`/`）开头。命令的名称严格遵循 CLI。路径对象之间的空格不受支持；必须用斜杠（`/`）替换。

一些特定于 API 的命令：

- `login` - 用于登录过程以提供登录凭据。
- `cancel` - 用于取消当前正在运行的命令。

命令字结构的严格顺序：

- 编码长度
- 内容前缀 */*
- CLI 转换后的命令

命令字内容的一些示例：

```ros
/login

```

```ros
/user/active/listen

```

```ros
/interface/vlan/remove

```

```ros
/system/reboot

```

#### 属性字

每个 *命令字* 根据其内容有其对应的 *属性字* 列表。

*属性字* 结构按顺序由五个部分组成：

- 编码长度
- 内容以等号（`=`）字符为前缀
- 属性名称
- 等号（`=`）字符作为名称和值的分隔符
- 属性值（如果有）。

一些属性示例（不包括编码长度前缀）：

```ros
=address=10.0.0.1

```

```ros
=disable-running-check=yes

```

值可以包含*等号*（`=`）符号：

```
=name=iu=c3Eeg

```

值可以为空：

```ros
=comment=
```

请记住，属性字和 **API** 参数的顺序不重要，不应依赖。

#### API 属性字

API 属性字结构的严格顺序：

- 编码长度
- 内容以点（`.`）字符为前缀
- 属性名称
- 等号（`=`）字符作为名称和值的分隔符
- 属性值

目前，唯一的此类 API 属性是 [`tag`](#标签)。

#### 查询字

句子可以有额外的查询参数来限制其范围。有关详细信息，请参阅 [查询部分](#查询)。

- 查询字以 `?` 开头。
- 目前，只有 `print` 命令处理查询字。

使用查询字属性的句子示例：

```ros
/interface/print
?type=ether
?type=vlan
?#|!

```

:::info
查询字的顺序很重要
:::

#### 回复字

它仅由路由器发送，以响应从客户端收到的完整句子。

- 回复的第一个字以 `!` 开头。
- 每个发送的句子至少生成一个回复（如果连接没有被终止）。
- 每个句子的最后一个回复是第一个字为 `!done` 的回复。
- 错误和异常情况以 `!trap` 开头。
- 数据回复以 `!re` 开头。
- 没有数据可回复的命令的回复以 `!empty` 开头。
- 如果 **API** 连接必须关闭，RouterOS 会发送 `!fatal`，并在描述中说明原因，然后关闭连接。

## 初始登录

- 客户端在第一条消息中发送用户名和密码。在我们的示例中，我们使用 `admin` 和空密码：

  ```ros
  /login
  =name=admin
  =password=
  ```

  如果身份验证成功，路由器回复 `!done`。

- 密码以明文形式发送。
- 如果发生错误，回复包含 `=message=<错误消息>`。
- 成功登录后，客户端可以开始发出命令。

## 标签

**API** 允许同时运行多个命令，而无需等待前一个命令完成。如果 API 客户端这样做并且需要区分命令响应，则可以在命令句子中使用 `tag` 参数。

如果句子包含 `tag`，则该句子的每个回复都将携带相同的标签值。

如果您省略 `tag` 参数或将其留空，则命令的响应将不包含标签参数。

## 命令描述

- `/cancel`
  - 可选参数：`=tag=<要取消的命令的标签>`；如果没有，则取消所有正在运行的命令。
  - 不会取消自身。
  - 所有被取消的命令都会被中断，并且通常会产生 `!trap` 和 `!done` 响应。
  - 请注意，`/cancel` 是一个单独的命令，可以有自己的唯一 `.tag` 参数，该参数与命令的 `=tag` 参数无关。

- `listen`
  - `listen` 命令在 CLI `print` 命令可用的任何地方都可用，但它可能并非在所有地方都有效。
  - 当特定项目列表中的某些内容发生变化时，会生成 `!re` 句子。
  - 当项目被删除或消失时，`!re` 句子包含值 `=.dead=yes`。
  - 此命令不会自行终止；使用 `/cancel` 命令来停止它。

- `getall`
  - `getall` 命令在 CLI `print` 命令可用的任何地方都可用（`getall` 是 `print` 的别名）。
  - 回复包含 `=.id=<项目内部编号>` 属性。

- `print`
  - API `print` 命令与 CLI 对应命令在以下方面有所不同：
    - 不支持 `where` 参数；可以使用 [查询字](#查询) 过滤项目。
    - `.proplist` 参数是要包含在返回项目中的属性名称的逗号分隔列表。
      - 返回的项目可能具有额外的属性。
      - 返回属性的顺序不重要，不能依赖。
      - 如果列表包含重复条目，则对这些重复条目的处理是未定义的。
      - 如果属性出现在 `.proplist` 中但项目中没有该属性，则该项目不具有该属性值（对于该项目，`?name` 评估为 false）。
      - 如果 `.proplist` 不存在，则按照 `print` 命令的请求包含所有属性，即使是访问时间较慢的属性（例如文件内容和性能计数器）。因此，鼓励使用 `.proplist`。如果设置了 `=detail=` 参数，省略 `.proplist` 可能会产生较高的性能损失。

### 查询

`print` 和 `getall` 命令接受限制返回句子集的查询字。

- 查询字以 `?` 开头。
- 查询字的顺序很重要。查询从第一个字开始评估。
- 对列表中的每个项目评估查询。如果查询成功，则处理该项目；如果查询失败，则忽略该项目。
- 使用布尔值堆栈评估查询。最初，堆栈包含无限数量的 `true` 值。在评估结束时，如果堆栈包含至少一个 `false` 值，则查询失败。
- 查询字根据以下规则操作：

| 查询                            | 描述                                |
|:--|:--|
| `?name`                        | 如果项目具有属性 `name` 的值，则压入 `true`，否则压入 `false`。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `?-name`                       | 如果项目不具有属性 `name` 的值，则压入 `true`，否则压入 `false`。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `?name=x` | 如果属性 `name` 的值等于 *x*，则压入 `true`，否则压入 `false`。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `?<name=x`                   | 如果属性 `name` 的值小于 *x*，则压入 `true`，否则压入 `false`。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `?>name=x`                   | 如果属性 `name` 的值大于 *x*，则压入 `true`，否则压入 `false`。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `?#operations`               | 对堆栈中的值应用操作。操作字符串从左到右评估。后跟任何其他字符或单词结尾的十进制数字序列被解释为堆栈索引。顶部值的索引为 0。后跟字符的索引会压入该索引处值的副本。后跟单词结尾的索引将所有值替换为该索引处的值。`!` 字符将顶部值替换为相反值。<code>&amp;</code> 弹出两个值并压入逻辑 `and` 操作的结果。`\|` 弹出两个值并压入逻辑 `or` 操作的结果。索引后的 `.` 不执行任何操作。另一个字符后的 `.` 压入顶部值的副本。 |

:::info
API 中不支持正则表达式，因此不要尝试发送带有 **`~`** 符号的查询
:::

示例：

- 获取所有以太网和 VLAN 接口（等同于 CLI 命令 `/interface/print where type=ether || type=vlan`）：

```ros
/interface/print
?type=ether
?type=vlan
?#|

```

- 获取所有具有非空注释的路由（等同于 CLI 命令 `/ip/route/print where comment`）：

```ros
/ip/route/print
?>comment=

```

- 获取所有距离不大于 1 且网关等于 172.16.1.1 的路由（等同于 CLI 命令 `/ip/route/print where !(distance>1 && gateway=172.16.1.1)`）：

```ros
/ip/route/print
?>distance=1
?gateway=172.16.1.1
?#&!

```

### OID

`print` 命令可以为 SNMP 中可用的属性返回 OID 值。

在 CLI 中，可以通过运行 `print oid` 命令查看 OID 值。在 API 中，这些属性的名称以 `.oid` 结尾，可以通过将其名称添加到 `.proplist` 的值中来检索。示例：

```ros
/system/resource/print
=.proplist=uptime,cpu-load,uptime.oid,cpu-load.oid
```

路由器发送回复：

```ros
!re
=uptime=01:22:53
=cpu-load=0
=uptime.oid=.1.3.6.1.2.1.1.3.0
=cpu-load.oid=.1.3.6.1.2.1.25.3.3.1.2.1

!done
```

### !trap

当 API 句子因任何原因失败时，路由器返回一个 trap，并附带：

- 一个 `message` 属性，提供有关失败的更多详细信息。
- 一个 `category` 属性。如果错误是通用的，路由器返回错误类别。此属性的可能值为：
  - 0 - 缺少项目或命令
  - 1 - 参数值失败
  - 2 - 命令执行被中断
  - 3 - 与脚本相关的失败
  - 4 - 一般性失败
  - 5 - 与 API 相关的失败
  - 6 - 与 TTY 相关的失败
  - 7 - 使用 `:return` 命令生成的值

```ros
/ip/address/add
=address=192.168.88.1
=interface=asdf
```

路由器回复：

```bash
!trap
=category=1
=message=input does not match any value of interface
```

## 修改现有项目

与其 CLI 对应命令一样，API 有一个 `set` 命令，它接受项目的 ID 和要设置的参数。
唯一的例外是 API 不允许直接使用 `set` 命令进行查询。例如，在所有以太网接口上设置 MTU 值的 CLI 命令：

```ros
/interface set [find where type=ether] mtu=1500
```

要使用 API 实现相同目的，您首先需要运行 `print` 查询来获取 ID，然后才能执行 `set` 命令。

```ros
/interface/print
=.proplist=.id
?type=ether
```

路由器回复：

```bash
!re
=.id=*1

!re
=.id=*2
```

现在您需要遍历返回的 ID，并为每个 ID 发送 `set` 命令：

```ros
/interface/set
=.id=*1
=mtu=1500

/interface/set
=.id=*2
=mtu=1500
```

## 命令示例

### `/user/active/listen`

```ros
/user/active/listen

!re
=.id=*68
=radius=no
=when=2006-10-24 08:40:42
=name=admin
=address=0.0.0.0
=via=console

!re
=.id=*68
=.dead=yes

... 更多 !re 句子 ...
```

### /cancel，同时执行命令

开始监听接口更改（标签为 2）：

```ros
/interface/listen
.tag=2
```

发送命令禁用接口（标签为 3）：

```ros
/interface/set
=disabled=yes
=.id=ether1
.tag=3
```

路由器为 `disable` 命令回复 `!done`（使用标签 3 执行）：

```ros
!done
.tag=3
```

启用接口（标签为 4）：

```ros
/interface/set
=disabled=no
=.id=ether1
.tag=4
```

客户端从路由器收到由第一个 `set` 命令（使用标签 3 执行）所做的更改生成的 `listen` 命令的更新：

```ros
!re
=.id=*1
=disabled=yes
=dynamic=no
=running=no
=name=ether1
=mtu=1500
=type=ether
.tag=2
```

随后是 `enable` 命令的 `done`（使用标签 4 执行）：

```ros
!done
.tag=4
```

发送命令获取接口列表（标签为 5）：

```ros
/interface/getall
.tag=5
```

客户端收到由第二个 `set` 命令（使用标签 4 执行）所做的更改生成的更新：

```ros
!re
=.id=*1
=disabled=no
=dynamic=no
=running=yes
=name=ether1
=mtu=1500
=type=ether
.tag=2
```

客户端收到 `getall` 命令的回复（使用标签 5 执行）：

```ros
!re
=.id=*1
=disabled=no
=dynamic=no
=running=yes
=name=ether1
=mtu=1500
=type=ether
.tag=5

!re
=.id=*2
=disabled=no
=dynamic=no
=running=yes
=name=ether2
=mtu=1500
=type=ether
.tag=5

!done
.tag=5
```

停止监听 - 请求取消标签为 2 的命令，`cancel` 本身使用标签 7：

```ros
/cancel
=tag=2
.tag=7
```

`listen` 命令被中断（标签为 2）：

```ros
!trap
=category=2
=message=interrupted
.tag=2
```

`cancel` 命令完成（标签为 7）：

```ros
!done
.tag=7
```

`listen` 命令完成（标签为 2）：

```ros
!done
.tag=2
```

## 示例客户端

一个简单的 [Python3 API 客户端](./python3-example.md)

使用旧登录方法的示例输出：

```bash
debian@localhost:~/api-test$ ./api.py 10.0.0.1 admin ''
<<< /login
<<<
>>> !done
>>> =ret=93b438ec9b80057c06dd9fe67d56aa9a
>>>
<<< /login
<<< =name=admin
<<< =response=00e134102a9d330dd7b1849fedfea3cb57
<<<
>>> !done
>>>
/user/getall

<<< /user/getall
<<<
>>> !re
>>> =.id=*1
>>> =disabled=no
>>> =name=admin
>>> =group=full
>>> =address=0.0.0.0/0
>>> =netmask=0.0.0.0
>>>
>>> !done
>>>
```