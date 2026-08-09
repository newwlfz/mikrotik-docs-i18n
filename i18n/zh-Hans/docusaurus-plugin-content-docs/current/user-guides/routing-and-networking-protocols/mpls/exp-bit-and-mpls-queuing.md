# EXP位与MPLS队列

> 本页解释了MPLS数据包中的EXP位以及RouterOS如何处理它以实现QoS，包括优先级标记、队列策略和MPLS mangle规则。详细说明了在数据包交换、倒数第二跳弹出和本地处理过程中EXP位的处理方式，并提供了在RouterOS中配置MPLS mangle规则的示例。

# EXP位与MPLS队列

当MPLS标签附加到数据包时，数据包长度会增加32位（4字节）。这32位分解如下：

- 标签值本身（20位）。
- EXP（“实验”）字段（3位）。
- 生存时间字段（8位）。
- 栈底字段（1位）。

MPLS标准未规定“实验”位的用途，但最常见的用途是携带QoS信息，类似于VLAN标签中的802.1q优先级。EXP字段仅包含3位，这意味着它可以携带0到7的值，允许8个流量类别。

## RouterOS中的EXP字段处理

当RouterOS接收到MPLS数据包时，它会将数据包的“入站优先级”值设置为顶层标签内携带的值。“入站优先级”不是数据包头内的字段——它是RouterOS在处理数据包时分配的一个附加标记。当RouterOS为MPLS数据包打标签时，它会将EXP位设置为分配给数据包的“优先级”（而非“入站优先级”）。当RouterOS交换MPLS数据包时，它会自动将“入站优先级”复制到“优先级”。这样，常规MPLS交换在整个标签交换路径上传递优先级信息。

有关“入站优先级”和“优先级”处理的更多信息，请参阅[WMM和VLAN优先级](../../../bridging-and-switching/user-guides/wmm-and-vlan-priority.md)。

EXP字段的行为取决于对数据包执行的操作：

- 如果RouterOS交换MPLS数据包（通过弹出标签并推送新标签），新标签中的EXP字段与接收到的标签匹配，因为：
  - RouterOS将“入站优先级”设置为接收标签中的EXP位。
  - 交换自动将“优先级”设置为“入站优先级”。
  - RouterOS使用新标签标记数据包，并将其EXP位设置为“优先级”中的值。
- 如果RouterOS通过倒数第二跳弹出交换MPLS数据包（路由器弹出接收到的标签且不推送新标签），EXP字段优先级保留在数据包的“优先级”字段中。其他MAC协议（如WMM或802.1q VLAN）随后可以使用此值：
  - RouterOS将“入站优先级”设置为接收标签中的EXP位。
  - 交换自动将“优先级”设置为“入站优先级”。
  - RouterOS将数据包交换到下一跳而不推送标签，并且这发生在VLAN接口上。
  - VLAN接口将VLAN头中的802.1q优先级设置为数据包的“优先级”值。

倒数第二跳弹出可能会在标签交换路径的最后一跳丢失QoS信息。如果需要保留此信息，请通过为标签交换路径的最后一跳使用显式NULL标签而非隐式NULL标签来禁用倒数第二跳弹出。MPLS TE隧道默认在最后一跳使用显式NULL标签。

- 如果RouterOS通过标签交换路径发送数据包（路由器将第一个标签推送到数据包上），它会将EXP位设置为“优先级”中的值。您可以使用防火墙规则或其他方式（例如，从IP头中的DSCP字段）正确设置此值。
- 如果RouterOS接收到用于本地处理的数据包，它会将“入站优先级”设置为接收数据包的EXP字段。然后，您可以使用此值更新数据包的DSCP字段，或使用防火墙规则从“入站优先级”设置“优先级”。

## MPLS Mangle与队列

RouterOS防火墙仅处理IP流量，这意味着您无法直接在mangle中标记MPLS数据包并通过队列限制它们。您必须在添加MPLS头之前的入站边缘路由器上或移除MPLS标签之后的出站边缘路由器上执行队列操作。

从ROS v7.17开始，RouterOS包含MPLS Mangle。此功能允许您基于EXP位添加数据包标记，或在标签交换（P）路由器上或MPLS封装后的PE输出上更改分配的EXP位。

此配置可从`/mpls/mangle`菜单访问。

### 基本示例

让我们看一个非常基本的示例，在LSP上的标签交换路由器（P）上，我们希望标记EXP位为0的数据包，限制带宽并将EXP位更改为3：

```routeros
/mpls/mangle
add chain=forward exp=0 set-exp=3 set-mark=m0

/queue/tree
add limit-at=10M max-limit=10M name=mpls_queue packet-mark=m0 parent=sfp-sfpplus2
```

MPLS数据包不能使用使用IMQ接口的队列（简单队列、全局队列树）进行排队。您必须使用以“真实”接口为父级的队列树。

MPLS Mangle表显示匹配的数据包计数，这对于调试您的配置很有用：

```ros
[admin@CCR2004_2XS_111] /mpls/mangle> print 
Flags: X - DISABLED
Columns: CHAIN, EXP, SET-EXP, SET-MARK, PACKETS
#   CHAIN    EXP  SET-EXP  SET-MARK  PACKETS
0   forward    0        3  m0        221 654
```

MPLS mangle规则不像常规防火墙mangle规则那样逐行执行。相反，MPLS Mangle会一次性应用所有操作。

例如，查看以下规则集：

```routeros
/mpls/mangle
add chain=forward exp=0 set-mark=m0
add chain=forward exp=0 set-exp=3
add chain=forward exp=3 set-mark=m3
```

在此示例中，如果传入数据包的EXP位值为0，则第三条规则不适用。

在您为特定EXP位设置操作后，其他规则无法修改它：

```ros
[admin@CCR2004_2XS_111] /mpls/mangle> add chain=forward exp=0 set-mark=m4
failure: conflicting forward set-mark rule
```