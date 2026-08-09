# 脚本编写技巧与窍门

> 本页提供 MikroTik RouterOS 的脚本编写技巧，强调使用内部 ID 而非字面值的重要性，以避免对象重新编号时出错。文中解释了如何通过 `find` 命令和类型转换正确引用接口路由、IP 地址及其他网络元素。

# 脚本编写技巧与窍门

让我们从基础开始。当你在终端中工作时，习惯使用以下语法来访问参数：

```
[admin@r1] /interface> print
Flags: D - dynamic, X - disabled, R - running, S - slave
 #     NAME                                TYPE       ACTUAL-MTU L2MTU  MAX-L2MTU
 0  R  ether1                              ether            1500  1580      1022
[admin@r1] /interface> set 0 name=LAN

```

`print` 命令会临时保存带有 ID 编号的缓冲区，这些编号引用内部 ID 号。因此，如果你尝试使用不存在的值，脚本将会失败，例如以下脚本：

```ros
/system script add name=script1 source={
  /ip route set 1 gateway=3.3.3.3
}

```

该脚本不知道“1”指的是什么，因此会抛出错误。正确的方法是使用内部 ID 号，这些编号可以通过 `print as-value` 查看，或由 `find` 命令返回，例如：

```ros
[admin@r1] /ip route> :put [find where dst-address="10.0.0.0/8"]
*1

```

因此在这种情况下，正确的脚本应为：

```ros
/system script add name=script1 source={
  /ip route set *1 gateway=3.3.3.3
}

```

请注意，不建议直接使用内部编号，因为项目可能被删除并重新添加，此时内部 ID 会改变，脚本将失败。请在代码中使用 `find` 命令：

```ros
/system script add name=script1 source={
  /ip route set [find dst-address="0.0.0.0/0"] gateway=3.3.3.3
}

```

## 为什么指定了正确的值，find 却不起作用？

假设我们想要打印一个特定的地址：

```
[admin@r1] /ip address> print where address=111.111.1.1/24
Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE

```

我们知道这样的地址存在，那为什么没有输出呢？

因为脚本引擎会尽可能积极地尝试转换变量类型，但并不总能成功。让我们仔细分析这个例子失败的原因。首先，检查 `address` 的变量类型：

```
[admin@r1] /ip address> :put [:typeof ([print as-value]->0->"address")]
str

```

显然，我们是在将字符串与 ip-prefix 类型进行比较，而 ip-prefix 不会自动转换为字符串。要解决此问题，我们需要将变量转换为正确的格式：

```
[admin@r1] /ip address> print where address=[:tostr 111.111.1.1/24]

Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE
 0   111.111.1.1/24     111.111.1.0     ether2

```

或者直接用双引号将查询值括起来作为字符串使用：

```
[admin@r1] /ip address> print where address="111.111.1.1/24"

Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE
 0   111.111.1.1/24     111.111.1.0     ether2

```

显然，如果你从变量中获取 IP 前缀，第二种方法并不适用；在这种情况下，请按照第一个示例进行转换，或者使用 `"$myVar"` 将变量写入字符串。

## 如何定义空数组

RouterOS 不允许以你预期的方式定义空数组：

```ros
[admin@1p_DUT_wAP ac] /interface> :global array {}
syntax error (line 1 column 17)

```

解决方法是将空字符串转换为数组：

```ros
[admin@r1] > :global array [:toarray ""]
[admin@r1] > :environment print
array={}
```

从这里开始，我们可以使用这个数组来设置元素：

```ros
[admin@r1] > :set ($array->"el0") "el0_val"
[admin@r1] > :environment print
array={el0="el0_val"}
```

## 如何删除变量

你可以使用 `/system script environment remove` 来删除未使用的变量；不过，更推荐的方法是取消设置变量。

为现有参数设置空值即可取消设置；例如：

```ros
[admin@MikroTik] /system script environment> :global myVar 1
[admin@MikroTik] /system script environment> print
 # NAME               VALUE
 0 myVar              1
[admin@MikroTik] /system script environment> :set myVar
[admin@MikroTik] /system script environment> print
 # NAME               VALUE
[admin@MikroTik] /system script environment>

```

## 当 'get' 命令不可用时获取属性值

例如，要从 `/interface wireless info hw-info` 命令获取可用于脚本的输出，请使用 `as-value` 参数：

```ros
[admin@1p_DUT_wAP ac] /interface wireless info> :put [hw-info wlan1 as-value ]
ranges=2312-2732/5/b;g;gn20;gn40;2484-2484/5/b;g;gn20;gn40;rx-chains=0;1;tx-chains=0;1

```

输出是一维数组，因此你可以轻松获取感兴趣的属性值。

```ros
[admin@1p_DUT_wAP ac] /interface wireless info> :put ([hw-info wlan1 as-value ]->"tx-chains")
0;1

```

## 始终检查命令返回的值和类型

假设我们尝试使用 `as-value` 获取特定路由的网关，但脚本返回为空：

```ros
[admin@r1] /ip address> :put ([/ip route print as-value where gateway="ether1"]->"gateway")

```

首先检查 `print` 是否真的找到了内容：

```ros
[admin@r1] /ip address> :put ([/ip route print as-value where gateway="ether1"])

.id=*400ae12f;distance=255;dst-address=111.111.111.1/32;gateway=ether1;pref-src=111.111.111.1

```

该命令假设输出是一维数组，我们可以从中提取名为 `gateway` 的元素。显然，变量或其类型有问题。让我们更仔细地检查：

```ros
[admin@r1] /ip address> :global aa ([/ip route print as-value where gateway="ether1"])
[admin@r1] /ip address> :environment print

aa={{.id=*400ae12f; distance=255; dst-address=111.111.111.1/32; gateway={"ether1"}; pref-src=111.11
1.111.1}}

```

现在很清楚了，返回值是包含一个元素的二维数组。因此，提取网关的正确顺序应为：

- 获取二维数组
- 获取第一个元素
- 从选取的元素中获取 `gateway`

```ros
[admin@r1] /ip address> :put ([:pick [/ip route print as-value where gateway="ether1"] 0]->"gateway")

ether1

```

## 将数组添加到字符串时要小心

如果你打印数组或将其追加到现有字符串，请务必小心，因为结果可能出乎意料。例如，对于一个包含两个元素的数组：

```ros
[admin@1p_DUT_wAP ac] /> :global array {"cccc", "ddddd"}
[admin@1p_DUT_wAP ac] /> :put ("array value is: " . $array )

array value is: cccc;array value is: ddddd

```

连接运算符（`.`）会将字符串添加到每个数组元素，然后打印输出。要解决此问题，需要先转换为字符串：

```ros
[admin@1p_DUT_wAP ac] /> :put ("array value is: " . [:tostr  $array] )

array value is: cccc;ddddd

```

## 获取/设置数组中的未命名元素

假设我们有一个包含三个元素的数组 `{ "el1"; "el2"; "el3" }`。你可以使用 `pick` 命令选取元素，但更好的方法是直接通过索引访问元素：

```ros
[admin@1p_DUT_wAP ac] /> :global test { "el1"; "el2"; "el3" }
[admin@1p_DUT_wAP ac] /> :put ($test->1)

el2

```

同样的语法可用于设置值：

```ros
[admin@1p_DUT_wAP ac] /> :set ($test->2) "el3_changed"
[admin@1p_DUT_wAP ac] /> :environment print

test={"el1"; "el2"; "el3_changed"}

```

## 在二维数组中设置元素值

你也可以直接在二维数组中按索引设置值：

```ros
[admin@1p_DUT_wAP ac] /> :global test {{"11";"12";"13"};{"21";"22";"23"}}
[admin@1p_DUT_wAP ac] > :set ($test->1->1) "22_changed"
[admin@1p_DUT_wAP ac] > :put [($test->1->1)]
22_changed
[admin@1p_DUT_wAP ac] > :environment print
test={{"11"; "12"; "13"}; {"21"; "22_changed"; "23"}}

```

## 读取在另一个脚本中定义的全局变量的值

假设我们有一个脚本声明了一个变量并设置了它的值：

```ros
/system script add name=script1 source={
  :global myVar "hello!"
}

```

如果我们想在另一个脚本中将该变量的值写入日志，添加 `/log info $myVar` 将无法返回正确的值，因为第二个脚本不知道在其他脚本中定义的变量。要使其正常工作，需要定义该变量：

```ros
/system script add name=script2 source={
  :global myVar;
  :log info "value is: $myVar"
}

```

## 从函数中访问全局变量

从逻辑上讲，你可能会认为全局定义的变量应该在函数中可访问，但事实并非如此。让我们看一个例子：

```ros
:global myVar "test"
:global myFunc do={
  :put "global var=$myVar"
}
[$myFunc]

```

输出为：

```
global var=

```

输出为空，因为全局变量不能直接访问。要使其工作，我们需要在函数内部声明全局变量：

```ros
:global myVar "test"
:global myFunc do={
  :global myVar;
  :put "global var=$myVar"
}
[$myFunc]

```

输出：

```
global var=test

```

## 从另一个函数运行函数

如果你想从另一个函数运行一个函数，则需要先声明它。

```ros
:global test do={
  :return ($1 + 1)
}

:global testtest do={
  :local x 5
  :local y [$test $x]
  :put "typeof = $[:typeof $y]"
  :put "testets_res=$y"
}

```

上述代码将无法按预期工作，输出将是：

```
typeof = nil
testets_res=

```

要解决此问题，我们需要在“testtest”函数中声明全局变量“test”：

```ros
:global testtest do={
  :global test
  :local x 5
  :local y [$test $x]
  :put "typeof = $[:typeof $y]"
  :put "testets_res=$y"
}

```

## 始终使用唯一的变量名

最常见的错误之一是使用不唯一的变量名。例如，函数中定义的变量可能与全局变量同名，导致意外结果：

```ros
:global my2 "123"

:global myFunc do={ :global my2; :put $my2; :set my2 "lala"; :put $my2 }
$myFunc my2=1234
:put "global value $my2"

```

输出将是：

```
1234
lala
global value 123

```

另一个常见问题是用户定义的变量与 RouterOS 内置属性同名。例如，要打印带有变量中定义的 `dst-address` 的路由：

```ros
[admin@1p_DUT_wAP ac] /ip route> :global "dst-address" "0.0.0.0/0"
[admin@1p_DUT_wAP ac] /ip route> print where dst-address=$"dst-address"
Flags: X - disabled, A - active, D - dynamic, C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme,
B - blackhole, U - unreachable, P - prohibit
 #      DST-ADDRESS        PREF-SRC        GATEWAY            DISTANCE
 0 ADS  0.0.0.0/0                          10.155.136.1              1
 1 ADC  10.155.136.0/24    10.155.136.41   ether1                    0

```

显然结果不符合预期，简单的解决方案是使用唯一的变量名：

```ros
[admin@1p_DUT_wAP ac] /ip route> :global myDst "0.0.0.0/0"
[admin@1p_DUT_wAP ac] /ip route> print where dst-address=$myDst
Flags: X - disabled, A - active, D - dynamic, C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme,
B - blackhole, U - unreachable, P - prohibit
 #      DST-ADDRESS        PREF-SRC        GATEWAY            DISTANCE
 0 ADS  0.0.0.0/0                          10.155.136.1              1

```

## 从循环交互式命令（如“monitor”）中获取值

一个常见的问题是如何在脚本中获取 `monitor` 等交互式命令返回的值。第一个问题是这些命令会无限期运行，直到用户干预，而脚本无法做到这一点。相反，可以使用 `once` 参数运行它们，该参数只执行一次命令然后停止。另一个问题是检索返回的变量：没有 `as-value` 也没有 `get`，但有 `do`。它允许你访问命令返回的变量。例如：

```ros
[admin@1p_DUT_wAP ac] /interface> monitor-traffic ether1 once do={:global myBps $"rx-bits-per-second" }
...
[admin@1p_DUT_wAP ac] /interface> :environment print

myBps=71464

```

## 获取 fetch 工具接收的文件内容

fetch 工具可以轻松地将文件内容下载到内存中，并从脚本中访问。为此，请使用 `as-value` 参数配合 `output=user`：

```ros
[admin@rack1_b34_CCR1036] > :put ([/tool fetch ftp://admin:@10.155.136.41/test.txt
 output=user as-value ]->"data")

my file content

```

## 检查脚本权限

假设我们有一个创建文件并向文件写入内容的脚本：

```ros
/system script add name=script1 policy=ftp,read,write source={
        /file print file=test;
        /file set test.txt contents="my content"
}

```

现在让我们添加一个调度器，尝试执行此脚本：

```ros
/system scheduler
add interval=10s name=test on-event=script1 policy=read,write

```

等待 10 秒后，我们可以看到文件没有被创建。如果仔细查看，脚本需要“ftp”策略来创建文件，但调度器只有“read”和“write”策略。要解决此问题，请将调度器设置为使用正确的策略“read,write,ftp”。

这也适用于从 netwatch、ppp `on-event` 等类似钩子运行脚本的情况，这些钩子仅限于 `read,write,test,reboot` 策略。在这种情况下，你无法执行创建备份或文件的高级脚本。

你可以通过使用 `dont-require-permissions` 来解决此限制，但授予脚本不受限制的权限时要非常小心。

## 使用 dont-require-permissions 时要小心

可以为脚本设置 `dont-require-permissions` 参数。基本上，它允许任何没有足够权限的人执行该脚本。例如，如果脚本具有“read,write,test,sensitive”策略，但执行脚本的用户或应用程序权限较少（例如，只有“read,write”），那么通过设置 `dont-require-permissions=yes`，我们将允许脚本无论如何都能运行。

这可能会导致即使执行脚本的用户没有足够的权限，也能通过脚本更改敏感信息。