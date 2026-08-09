# 脚本编写

> RouterOS 脚本功能通过用户自定义脚本实现自动化，这些脚本可由系统调度或流量监控等事件触发。脚本采用命令行语法，支持可选前缀、命名参数和物理行格式，既可单行执行也可多行执行。

# 脚本编写

RouterOS 包含一种强大的脚本语言，用于自动化维护任务。您可以创建用户自定义脚本并将其绑定到事件上。

您可以将脚本存储在脚本库中，或直接在 CLI 中编写。常见的触发方式包括系统调度器、流量监控工具和 Netwatch 工具事件。

如果您已经熟悉 RouterOS 中的脚本编写，您可能想查看我们的[技巧与窍门](./scripting-tips-and-tricks.md)。

## 行结构

RouterOS 脚本由多个命令行组成。命令行按顺序逐一执行，直到脚本结束或发生运行时错误。

### 命令行

RouterOS CLI 使用以下命令语法：

`[前缀] [路径] 命令 [未命名参数] [参数=[值]] .. [参数=[值]]`

- [前缀] - `:` 或 `/` 字符表示后面的词是[全局命令](#global-commands)或路径。从根菜单或相对于所调用路径/命令的菜单调用时，前缀不是必需的。
- [路径] - 到所需菜单级别的相对路径。可能不是必需的。
- 命令 - 在指定菜单级别可用的[命令](#commands)之一。
- [未命名参数] - 未命名参数，如果命令需要则必须指定。
- [参数] - 一系列命名参数后跟值（如果参数需要值）。

命令行的结束由标记 `;` 或 *换行符* 表示。
包含在 `()`、`[]` 或 `{}` 中的命令不需要任何命令结束字符。命令的结束由整个脚本的内容决定

```ros
:if ( true ) do={ :put "lala" }
```

另一个命令行内部的每个命令行以方括号 `[]` 开始和结束 [（命令连接运算符）](#other-operators)。

```ros
:put [/ip route get [find gateway=1.1.1.1]];
```

请注意，上述代码包含三个命令行：

- `:put`
- `/ip route get`
- `find gateway=1.1.1.1`

请注意，菜单特定的 `find` 命令不需要完整路径，因为路径是从父命令的路径派生的。

一个命令行可以通过遵循[行连接规则](#line-joining)由多个物理行构成。

### 物理行

物理行是由行结束（**EOL**）序列终止的字符序列。可以使用任何标准的平台行终止序列：

- **Unix** – ASCII LF；
- **Windows** – ASCII CR LF；
- **mac** – ASCII CR；

可以使用标准 C 换行符约定（`\n`、`\r\n` 字符）。

### 注释

以下规则适用于注释：

- 注释以井号字符 `#` 开始，并在物理行末尾结束。
- RouterOS 不支持多行注释。
- 如果 `#` 字符出现在字符串内部，则不视为注释。

```ros
# 这是一个注释
# 下一行继续注释
:global a; # 描述变量的注释

:global myStr "字符串的一部分 # 不是注释"
```

### 行连接

使用**反斜杠**字符（`\`）可以将两个或多个物理行连接成逻辑行。
使用反斜杠作为行连接工具时，适用以下规则：

- 以反斜杠结尾的行不能带有注释。
- 反斜杠不能延续注释。
- 反斜杠不能延续标记，字符串字面量除外。
- 在字符串字面量之外，反斜杠在其他位置是非法的。

```ros
:if ($a = true \
	and $b=false) do={ :put "$a $b"; }
:if ($a = true \ # 错误的注释（语法错误）
	and $b=false) do={ :put "$a $b"; }
# 注释 \
	延续无效（语法错误）
```

### 标记之间的空白

空白可用于分隔标记。仅当两个标记的连接可能被解释为不同的标记时，才需要在它们之间使用空白。示例：

```ros
{  
	:local a true; :local b false;
# 不需要空白
	:put (a&&b);
# 需要空白  
	:put (a and b);
}

```

不允许使用空白字符的位置：

- 在 `<参数>=` 之间。
- 在 `from=`、`to=`、`step=`、`in=`、`do=`、`else=` 之间。

示例：

```ros
#错误：
:for i from = 1 to = 2 do = { :put $i }

#正确语法：
:for i from=1 to=2 do={ :put $i }
:for i from= 1 to= 2 do={ :put $i }

#错误
/ip route add gateway = 3.3.3.3

#正确
/ip route add gateway=3.3.3.3
```

### 作用域

变量只能在脚本中称为作用域的特定区域使用。这些区域决定了变量的可见性。在块内声明的变量只能在该块及其嵌套块内访问，并且只能在声明点之后访问。

有两种类型的作用域 — **全局**和**局部**。

#### 全局作用域

全局作用域或根作用域是脚本的默认作用域。它是自动创建的，无法关闭。

可以通过声明而不赋值来访问由另一个脚本设置的全局变量。

例如，第一个脚本将 myVar 值设置为 3：

```ros
:global myVar 3
```

要从另一个脚本访问此变量：

```ros
:global myVar
:put "myVar=$myVar"
```

输出：

```
myVar=3
```

#### 局部作用域

您可以定义组来限制变量访问；这些称为局部作用域。每个局部作用域都用花括号（`{}`）括起来。

```ros
{  
    :local a 3;
    {  
	:local b 4;  
	:put ($a+$b);
    } # 下面的行将变量 b 显示为浅红色，因为它未在此作用域中定义  
    :put ($a+$b);
}

```

变量 `b` 在局部作用域中声明，在右花括号之后不可访问。

在 CLI 中编写的每一行都被视为一个局部作用域。
例如，定义的局部变量在下一个命令行中不可见，并会产生语法错误

```ros
[admin@MikroTik] > :local myVar a;
[admin@MikroTik] > :put $myVar
语法错误（第 1 行第 7 列）

```

:::danger
不要在**局部**作用域内定义**全局**变量。
:::

即使变量可以定义为全局变量，它也只能在其作用域内可用，除非它被引用以在作用域外可见。

```ros
{  
    :local a 3;
    {  
        :global b 4;
    }  
    :put ($a+$b);
}
```

代码输出 3，因为 `b` 在作用域外不可见。

以下代码解决了该问题并按预期输出 7：

```ros
{  
    :local a 3;
    {  
        :global b 4;
    }
    :global b;  
    :put ($a+$b);
}
```

## 关键字

以下词语是关键字，不能用作变量和函数名：

```
and       or       in

```

## 分隔符

以下标记在语法中用作分隔符：

```
()  []  {}  :   ;   $   /

```

## 数据类型

RouterOS 脚本语言具有以下数据类型：

| 类型                 | 描述                                           |
|:--|:--|
| **num（数字）**     | 64 位有符号整数，支持十六进制输入；     |
| **bool（布尔）**   | 值可以是 `true` 或 `false`。                     |
| **str（字符串）**     | 字符序列。                                   |
| **ip**               | IP 地址。                                           |
| **ip-prefix**        | IP 前缀。                                            |
| **ip6**              | IPv6 地址。                                         |
| **ip6-prefix**       | IPv6 前缀。                                          |
| **id（内部 ID）** | 以 `*` 字符为前缀的十六进制值。每个菜单项都有一个分配的唯一编号 - 内部 ID。 |
| **time**             | 日期和时间值。                                  |
| **array**            | 组织在数组中的值序列。             |
| **nil**              | 如果未分配值，则为默认变量类型。        |

## 常量转义序列

以下转义序列可用于在字符串中定义某些特殊字符：

|         |                                                                    |
|:--|:--|
| **\"**  | 插入双引号。                                               |
| **\\**  | 插入反斜杠。                                                  |
| **\n**  | 插入换行符。                                                    |
| **\r**  | 插入回车符。                                            |
| **\t**  | 插入水平制表符。                                             |
| **\$**  | 输出 $ 字符。否则，$ 用于链接变量。     |
| **\\_** | 空格。                                                             |
| **\a**  | 响铃（BEL，0x07）。                                                        |
| **\b**  | 退格（0x08）。                                                  |
| **\f**  | 换页（0x0C）。                                                  |
| **\v**  | 插入垂直制表符。                                               |
| **\xx** | 十六进制值的可打印字符。十六进制数字应使用大写字母。 |

例如：

```ros
:put "\48\45\4C\4C\4F\r\nThis\r\nis\r\na\r\ntest";

```

将输出：

```
HELLO
This
is
a
test
```

## 运算符

### 算术运算符

RouterOS 脚本语言支持常见的算术运算符：

| 运算符   | 描述           | 示例                        |
|:--|:--|:--|
| **`+`**    | 二进制加法       | `:put (3+4);`                  |
| **`-`**    | 二进制减法    | `:put (1-6);`                  |
| **`*`**    | 二进制乘法 | `:put (4*5);`                  |
| **`/`**    | 二进制除法       | `:put (10 / 2); :put ((10)/2)` |
| **`%`**    | 取模运算      | `:put (5 % 3);`                |
| **`-`**    | 一元取反        | `{ :local a 1; :put (-a); }`   |

请注意，要使除法正常工作，您必须在被除数周围使用花括号或空格，以免被误认为是 IP 地址。

### 关系运算符

| 运算符   | 描述      | 示例       |
|:--|:--|:--|
| **`<`**    | 小于             | `:put (3<4);` |
| **`>`**    | 大于          | `:put (3>4);` |
| **`=`**    | 等于            | `:put (2=2);` |
| **`<=`**   | 小于或等于               |               |
| **`>=`**   | 大于或等于 |               |
| **`!=`**   | 不等于        |               |

要否定表达式，可以使用 `<表达式>=false`。例如，要打印所有不是 "ethernet" 的接口，可以像这样使用表达式否定：

```ros
/interface/print where (name~"ether")=false
```

或者做相反的操作，可以使用 `<表达式>=true`：

```ros
/interface/print where (name~"ether")=true
```

### 逻辑运算符

| 运算符         | 描述   | 示例                           |
|:--|:--|:--|
| **`!`**          | 逻辑非   | `:put (!true);`                   |
| **`&&`， `and`**  | 逻辑与   | `:put (true&&true)`               |
| **`\|\|`， `or`** | 逻辑或    | `:put (true\|\|false);`           |
| **`in`**         |               | `:put (1.1.1.1/32 in 1.0.0.0/8);` |

### 位运算符

位运算符仅适用于 IP 和 IPv6 地址[数据类型](#data-types)。

| 运算符   | 描述      | 示例                                      |
|:--|:--|:--|
| **`~`**    | 位取反。   | `:put (~0.0.0.0)` `:put (~::ffff)`           |
| **`\|`**   | 按位或对每对对应位执行逻辑或运算。在每对中，如果其中一个位或两个位均为“1”，则结果为“1”，否则结果为“0”。 | `:put (192.168.88.0\|0.0.0.255)` `:put (2001::1\|::ffff)` |
| **`^`**    | 按位异或与或相同，但每个位置的结果为“1”（如果两个位不相等），“0”（如果位相等）。 | `:put (1.1.1.1^255.255.0.0)` `:put (2001::ffff:1^::ffff:0)` |
| **`&`**    | 按位与的结果为“1”（如果第一位和第二位均为“1”）。否则，结果为“0”。 | `:put (192.168.88.77&255.255.255.0)` `:put (2001::1111&ffff::)` |
| **`<<`**   | 按给定位数左移，不支持 IPv6 地址数据类型。 | `:put (192.168.88.77<<8)` |
| **`>>`**   | 按给定位数右移，不支持 IPv6 地址数据类型。 | `:put (192.168.88.77>>24)` |

例如，使用 `&` 运算符从给定的 IP 和 CIDR 子网掩码计算子网地址：

```ros
{
:local IP 192.168.88.77;
:local CIDRnetmask 255.255.255.0;
:put ($IP&$CIDRnetmask);
}
```

从给定的 IP 地址获取最后 8 位：

```ros
 :put (192.168.88.77&0.0.0.255);
```

使用 `|` 运算符和反转的 CIDR 掩码计算广播地址：

```ros
{
:local IP 192.168.88.77;
:local Network 192.168.88.0;
:local CIDRnetmask 255.255.255.0;
:local InvertedCIDR (~$CIDRnetmask);
:put ($Network|$InvertedCIDR)
}
```

### 连接运算符

| 运算符   | 描述          | 示例                                  |
|:--|:--|:--|
| **`.`**    | 连接两个字符串。| `:put ("concatenate" . " " . "string");` |
| **`,`**    | 连接两个数组或将一个元素添加到数组。 | `:put ({1;2;3} , 5 );` |

可以直接将变量值添加到字符串中，而无需连接运算符：

```ros
:global myVar "world";

# 值可以通过连接运算符添加
:put ("Hello " . $myVar);
# 或无需运算符
:put "Hello $myVar";
```

使用 `$[]` 和 `$()` 可以执行表达式并将结果值插入字符串中：

```ros
:local a 5;
:local b 6;
:put " 5x6 = $($a * $b)";

:put " We have $[ :len [/ip route find] ] routes";
```

### 其他运算符

| 运算符   | 描述       | 示例                                     |
|:--|:--|:--|
| **`[]`**   | 命令替换只能包含单个命令行` | `:put [ :len "my test string"; ];` |
| **`()`**   | 子表达式或分组运算符。 | `:put ( "value is " . (4+5));` |
| **`$`**    | 替换运算符。 | `:global a 5; :put $a;` |
| **`~`**    | 将值与 POSIX 扩展正则表达式匹配的二元运算符。 | 打印所有网关以 202 结尾的路由： `/ip/route/print where gateway~"^[0-9 \\.]*202\$"` |
| **`->`**   | 按键获取数组元素。 | `[admin@x86] >:global aaa {a=1;b=2}``[admin@x86] > :put ($aaa->"a")``1``[admin@x86] > :put ($aaa->"b")``2` |

## 变量

脚本语言有两种类型的变量：

- **全局** - 可从当前用户创建的所有脚本访问，由 [`global`](#global-scope) 关键字定义。
- **局部** - 仅可在当前[作用域](#local-scope)内访问，由 `local` 关键字定义。

变量可能未定义。发生这种情况时，解析器会查找应用程序提供的内置变量。例如，DHCP `lease-script` 提供几个内置变量：

```ros
/system script
add name=myLeaseScript policy=\
	ftp,reboot,read,write,policy,test,winbox,password,sniff,sensitive,api \
	source=":log info \$leaseActIP\r\
	\n:log info \$leaseActMAC\r\
	\n:log info \$leaseServerName\r\
	\n:log info \$leaseBound"

/ip dhcp-server set myServer lease-script=myLeaseScript
```

除了 RouterOS 内置变量外，每个变量在使用前都必须使用 `local` 或 `global` 关键字声明。使用未声明的变量会导致编译错误。例如：

```ros
# 以下代码将导致编译错误，因为 myVar 在未声明的情况下使用
:set myVar "my value";
:put $myVar
```

正确的代码：

```ros
:local myVar;
:set myVar "my value";
:put $myVar;
```

变量名中的有效字符是字母和数字。如果变量名包含字母或数字以外的任何字符（包括运算符），请用双引号（`""`）将其括起来。示例：

```ros
#有效的变量名
:local myVar;
#无效的变量名
:local my-var;
#有效，因为使用了双引号
:global "my-var";
```

如果变量最初定义时没有值，则[变量数据类型](#data-types)设置为 ***nil***；否则，脚本引擎会自动确定数据类型。有时需要从一种数据类型转换为另一种数据类型。这可以通过[数据转换命令](#global-commands)实现。示例：

```ros
#将字符串转换为数组
:local myStr "1,2,3,4,5";
:put [:typeof $myStr];
:local myArr [:toarray $myStr];
:put [:typeof $myArr]
```

变量名区分大小写。

```ros
:local myVar "hello"
# 以下行将生成错误，因为变量 myVAr 未定义
:put $myVAr
# 正确的代码
:put $myVar
```

不带值的 `set` 命令会取消定义变量：

```ros
#从环境中移除变量
:global myVar "myValue"
:set myVar;
```

### 保留变量名

所有内置的 RouterOS 属性都是保留变量。使用与 RouterOS 内置属性同名的变量可能会导致错误。为避免这种情况，请选择不同的名称。

例如，以下脚本将无法工作：

```ros
{
:local type "ether1";
/interface print where name=$type;
}
```

但使用不同的已定义变量则可以工作：

```ros
 {
:local customname "ether1";
/interface print where name=$customname;
}
```

## 命令

### 全局命令

每个全局命令应以 **`:`** 标记开头；否则它将被视为变量。

| 命令         | 语法     | 描述          | 示例                |
|:--|:--|:--|:--|
| **/**           |            | 转到根菜单。 |                        |
| **..**          |            | 返回上一级菜单。 |                  |
| **?**           |            | 列出所有可用的菜单命令和简要描述。 |  |
| **global**      | `:global <变量> [<值>]` | 定义全局变量。 | `:global myVar "something"; :put $myVar;` |
| **local**       | `:local <变量> [<值>]` | 定义局部变量。 | `{ :local myLocalVar "I am local"; :put $myLocalVar; }` |
| **beep**        | `:beep frequency=[数字] length=[数字]` | 使内置扬声器发出蜂鸣声。 |  |
| **convert**     | `:convert from=[参数] to=[参数] transform=[参数]` | 将指定值从一种格式转换为另一种格式。默认情况下，如果未指定 `from` 格式，则使用自动解析的值（例如，"001" 变为 "1"，"10.1" 变为 "10.0.0.1" 等）。  **`from`** - 指定值的格式： *base32, base64, bit-array-lsb, bit-array-msb, byte-array, hex, num, raw, url*。  **`to`** - 指定输出值的格式： *base32, base64, bit-array-lsb, bit-array-msb, byte-array, hex, num, raw, url*。   **`transform`** - 指定如何转换值： *lc（将值转换为小写）、uc（大写）、lcfirst（首字母小写）、ucfirst（首字母大写）、crlf、ed25519-private-to-x25519-private、none、rot 13、x25519-private-to-x25519-public、ed25519-private-to-ed25519-public、ed25519-public-to-x25519-public、md5、reverse（反转文本）、sha512*。 | `:put [:convert 001 to=hex ]`  `31`  `:put [:convert [/ip dhcp-client/option/get hostname raw-value] from=hex to=raw ]`  `MikroTik`  `:put [:convert transform=lc "AAA"]`  `aaa` |
| **delay**       | `:delay <时间>` | 在给定时间段内不执行任何操作。 |  |
| **environment** | `:environment print <开始>` | 打印已初始化的变量信息。 | `:global myVar true; :environment print;` |
| **error**       | `:error <输出>` | 生成控制台错误并停止执行脚本。 |  |
| **execute**     | `:execute <表达式>` | 在后台执行脚本。可以通过设置 `file` 参数将结果写入文件，或通过设置 `as-string` 参数将结果打印到 CLI。 使用 `as-string` 参数时，执行的脚本会被阻塞（不在后台执行）。 执行的脚本不能大于 64 kB。 | `{ :local j [:execute {/interface print follow where [:log info ~Sname~]}]; :delay 10s; :onerror e {/system script job remove $j}}` |
| **find**        | `:find <参数> <参数> <开始>` | 返回子字符串或数组元素的位置。 | `:put [:find "abc" "a" -1];` |
| **grep**        | `:grep script=[字符串] pattern=[表达式] after=[数字] before=[数字] filename=[字符串]` | 在终端中执行提供的 `script`，并打印与给定 `pattern` 匹配的行。参数 `after` 和 `before` 设置匹配行之前和之后额外打印的行数。结果可以通过 `filename` 参数直接保存到文件中。 | `:grep script="/interface print" pattern="ether" after=1 before=1 filename=results.txt` |
| **jobname**     | :jobname   | 返回当前脚本名称。 | **将脚本执行限制为单个实例**  ` :if ([/system script job print count-only as-value where script=[:jobname] ] > 1) do={  :error "script instance already running"  }`|
| **len**         | `:len <表达式>` | 返回字符串长度或数组元素数量。 | `:put [:len "length=8"];` |
| **log**         | `:log <主题> <消息>` | 将消息写入[系统日志](../../diagnostics-monitoring-and-troubleshooting/log/index.md)。可用主题为 `debug`、`error`、`info` 和 `warning`。 | `:log info "Hello from script";` |
| **onerror**     | `:onerror <变量名> in={<命令>} do={<表达式>}` | 捕获错误并获取错误详细信息。当 **`in={...}`** 块出现错误时，执行 **`do={...}`** 块，并将错误详细信息写入 `<变量名>` 变量。   参数顺序很重要。`error` 参数必须在 `do` 块之前设置，否则 `do` 块将看不到局部变量。  `:onerror` 将返回 `false`（如果没有错误）和 `true`（如果有错误），除非另有指定（使用诸如 `:return` 或 `:error` 等命令），因此它可以在 **`:if`** 条件语句脚本中使用。 | `:onerror errorName in={ :error "failure" } do={ :put "Critical $errorName" }` |
| **parse**       | `:parse <表达式>` | 解析字符串并返回解析后的控制台命令。可以用作函数。 | `:global myFunc [:parse ":put hello!"]; $myFunc;` |
| **pick**        | `:pick <变量> <开始> [<结束>]`                                                     | 返回元素范围或子字符串。如果未指定数量，则仅从数组中返回一个元素。 `变量` - 要从中选取元素的值。`开始` - 开始选取的元素（第一个元素索引为 0）。`结束` - 终止索引（不包含此索引处的元素）。 | `[admin@MikroTik] > :put [:pick "abcde" 1 3]``bc` |
| **put**         | `:put <表达式>` | 将提供的参数打印到终端。 | `:put "Hello world"` |
| **range**       | `:range <变量> <变量>` | 从指定范围创建数组。 | `:put [:range 2 8] 2;3;4;5;6;7;8` |
| **resolve**     | `:resolve <参数> [<域名>][<服务器>][<服务器端口>][<类型>]` | 返回给定 DNS 名称的 IP 地址 `域名` - 需要解析的 DNS 名称。`服务器` - 用于解析 DNS 名称的特定服务器（返回的结果不会被缓存）。`服务器端口` - 要连接的服务器端口。`类型` - any/any6/ipv4/ipv6：`any` - 尝试解析 ipv4，失败时尝试 ipv6。`any6` - 尝试解析 ipv6，失败时尝试 ipv4。`ipv4` - 仅尝试解析 ipv4。`ipv6` - 仅尝试解析 ipv6。 | `:put [:resolve "www.mikrotik.com"];`  `:put [:resolve domain-name="www.mikrotik.com"];`  `:put [:resolve domain-name="www.mikrotik.com" server=192.168.88.1 server-port=53];`  `:put [:resolve domain-name="www.mikrotik.com" type=ipv6];` |
| **retry**       | `:onerror e {:retry command=<表达式> delay=[数字] max=[数字]} do={<表达式>}` | 尝试执行给定命令 `max` 次，每次尝试之间间隔 `delay` 秒。失败时，执行 `do={}` 块中的命令。 | `:onerror e {:retry command={abc} delay=1 max=2} do={:put "got error"}` |
| **typeof**      | `:typeof <变量>` | 返回给定变量的数据类型。 | `:put [:typeof 4];` |
| **rndnum**      | `:rndnum from=[数字] to=[数字]` | 随机数生成器。 | `:put [:rndnum from=1 to=99];` |
| **rndstr**      | `:rndstr from=[字符串] length=[数字]` | 随机字符串生成器。  **`from`** 指定用于构造字符串的字符，默认为所有 ASCII 字母和数字。  **`length`** 指定要创建的字符串长度，默认为 16。 | `:put [:rndstr from="abcdef%^&``" length=33];` |
| **set**         | `:set <变量> [<值>]` | 为已声明的变量赋值。 | `:global a; :set a true;` |
| **serialize**   | `:serialize [<值>] to=[参数]` | 将指定的值/数组序列化为 JSON 或 dsv（分隔符分隔值）格式。  **`value`** 指定要处理的值。  **`to`** 指定格式 - *json, dsv*  **`delimiter`** 设置“分隔符”。  **`order`** 指定变量的顺序。  **`options`** 指定附加选项*：* json.pretty  - 使 JSON 输出更具视觉吸引力；json.no-string-conversion - 防止从控制台字符串类型到 json 数字类型的隐式转换；dsv.wrap-strings - 将字符串值用引号括起来；dsv.ignore-size - 如果数组值具有不同大小，例如 <code>a=(1,2);b=(3,4);c=(5,6,7)</code>，此选项将解决 <code>array size mismatch</code> 错误并在这些槽中设置“空”值。dsv.remap - 将字典数组合并为单个字典（在处理“<code>print as-value</code>”时很有用） **file-name** 启用将命令输出生成到文件中的选项（可在“/files”部分下载）。 | `:put [:serialize value=a,b,c to=json]``["a","b","c"]``:local test {a=(1,2,3);b=(4,5,6);c=(7,"text",9)}; :put [ :serialize to=dsv delimiter=";" value=$test order=("c","a","b") ]``c;a;b``7;1;4``text;2;5``9;3;6``:global var ({ "string"="1234"; "number"=1234 });:put [ :serialize to=json value=$var ]``{"number":1234,"string":1234.000000}``:put [ :serialize to=json value=$var options=json.no-string-conversion  ]``{"number":1234,"string":"1234"}``:put [:serialize to=dsv options=dsv.remap delimiter="#" [/ip/address/print as-value]]``.id#address#comment#interface#network``*1#192.168.88.1/24#defconf#bridge#192.168.88.0``*2#192.168.69.190/24##ether1#192.168.69.0`|
| **deserialize** | `:deserialize [<值>] from=[参数]` | 从 JSON 或 dsv（分隔符分隔值）格式反序列化指定的值/数组。  **`from`** 指定格式 - *json, dsv*  **`delimiter`** 设置“分隔符”。  **`options`** 指定附加选项*：* dsv.plain - 将每一行反序列化为一个数组（输入没有标题或列名）；dsv.array - 期望有标题（列名），并将返回一个字典数组，其中值映射到标题中提供的列名。json.no-string-conversion - 防止从 json 字符串类型到控制台值（数字、ip 等）的隐式转换。 | `:put [:deserialize from=json value="[\"a\",\"b\",\"c\"]"]``a;b;c``:put ([ :deserialize from=dsv delimiter=";" value="a;b;c\n1;findme;3" options=dsv.plain ]->1->1)` `findme``:put ([ :deserialize from=dsv delimiter=";" value="a;b;c\n1;findme;3" options=dsv.plain ]->0->1)   ``b``:put ([:deserialize from=dsv "a;b;c\n1;2;3\n4;5;6" delimiter=";" options=dsv.array]->1->"b") ``5``:put ([:deserialize from=dsv "a;b;c\n1;2;3\n4;5;6" delimiter=";" options=dsv.array]->0->"c")    ``3``:put [typeof ([:deserialize "{ \"str\": \"123\" }" from=json options=json.no-string-conversion]->"str")]``str``:deserialize [/file/get file.json contents] from=json` |
| **time**        | `:time <表达式>` | 返回执行提供的表达式所需的时间间隔。 | `:put [:time {:for i from=1 to=10 do={ :delay 100ms }}];` |
| **timestamp**   | `:timestamp` | 返回自 `epoch` 以来的时间，其中 `epoch` 是 1970 年 1 月 1 日（星期四），不计算闰秒。 | `[admin@MikroTik] > :put [:timestamp]``2735w21:41:43.481891543`或`[admin@MikroTik] > :put [:timestamp]``2735w1d21:41:43.481891543`带有天偏移量。 |
| **toarray**     | `:toarray <变量>` | 将变量转换为数组。 |       |
| **tobool**      | `:tobool <变量>` | 将变量转换为布尔值。 |       |
| **toid**        | `:toid <变量>` | 将变量转换为内部 ID。 |       |
| **toip**        | `:toip <变量>` | 将变量转换为 IP 地址。 |     |
| **toip6**       | `:toip6 <变量>` | 将变量转换为 IPv6 地址。 |  |
| **tonum**       | `:tonum <变量>` | 将变量转换为整数。 |       |
| **tostr**       | `:tostr <变量>` | 将变量转换为字符串。 |         |
| **totime**      | `:totime <变量>` | 将变量转换为时间。 |            |
| **tonsec**      | `:tonsec <变量>` | 将时间转换为纳秒。 | `:put [:tonsec value=10:00]               36000000000000` |
| **tocrlf**      | `:tocrlf <变量>` | 将行尾转换为 CRLF。 | `:put [:tocrlf  "AAA\r\nBBB\r\nCCC" ]``AAA``BBB``CCC`|
| **tolf**        | `:tolf <变量>` | 将行尾转换为 LF。 | `:put [:tolf  "AAA\nBBB\nCCC" ]``AAA``   BBB``      CCC`|
| **nothing**     | `:nothing`  | 返回一个空值。 | `:if ([:nothing] = 0) do={:put true} else={:put false} false :if ([:nothing] > 0) do={:put true} else={:put false}  false :if ([:nothing] < 0) do={:put true} else={:put false}` |

如果变量类型转换函数无法将新格式应用于提供的数据，则输出将为空。

例如，如果您对具有非整数值（如 "23.8" 或 "cow&chicken"）的变量运行 `