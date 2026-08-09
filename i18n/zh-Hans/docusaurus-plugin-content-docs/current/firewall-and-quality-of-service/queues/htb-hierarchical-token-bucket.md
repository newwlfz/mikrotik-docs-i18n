# HTB（分层令牌桶）

> HTB（分层令牌桶）是 RouterOS 中的一种排队规则，用于速率限制和突发处理，采用令牌桶算法管理数据速率，并支持可配置的容量和限制。

# HTB（分层令牌桶）

## 引言

HTB（分层令牌桶）是一种基于类别的排队规则，适用于速率限制和突发处理。本文将专门讨论 RouterOS 中的 HTB 特性，因为我们使用了修改版本来提供 Simple Queue 和 Queue Tree 等功能。

## 令牌桶算法（图中的红色部分）

令牌桶算法基于一个桶的类比，其中以字节表示的令牌以特定速率添加。桶本身具有指定的容量。

如果桶已满，新到达的令牌将被丢弃。

**桶容量 = bucket-size \* max-limit**

- **bucket size**（0..10，默认值：0.1）

在允许任何数据包通过队列之前，会检查队列的桶，看此时是否已有足够的令牌。

如果有，则移除相应数量的令牌（“兑现”），并允许数据包通过队列。

如果没有，数据包将停留在数据包等待队列的起始位置，直到有足够数量的令牌可用。

在多级队列结构的情况下，子队列中使用的令牌也会“计入”其父队列。换句话说——子队列从父队列“借用”令牌。

### 数据包队列（图中的蓝色部分）

此数据包队列的大小、顺序、数据包如何添加到该队列以及何时丢弃数据包由以下因素决定：

- **queue-type** - [Queue](./index.md)
- **queue-size** - [Queue Size](./queue-size.md)

### 令牌速率选择（图中的黑色部分）

任意给定时间的最大令牌速率等于以下值中的最高活动值：

- **limit-at**（*数字/数字*）：保证目标的上传/下载数据速率。
- **max-limit**（*数字/数字*）：允许目标的最大上传/下载数据速率。
- **burst-limit**（*数字/数字*）：在“突发”激活期间允许目标的最大上传/下载数据速率。

**burst-limit** 仅在“突发”处于允许状态时激活——更多信息请参见：[Queue Burst](./queue-burst.md)

当 **limit-at** 为最高值时，需要发放额外的令牌，以补偿所有未从父队列借用的缺失令牌。

### 图示

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/queues/img/htb-hierarchical-token-bucket-01.webp)

### Bucket Size 的实际应用

让我们设置一个简单的场景，其中所有来自和发往一个 IP 地址的流量都通过 packet-mark 进行标记：

```ros
/ip/firewall/mangle
add chain=forward action=mark-connection connection-mark=no-mark src-address=192.168.88.101 new-connection-mark=pc1_conn
add chain=forward action=mark-connection connection-mark=no-mark dst-address=192.168.88.101 new-connection-mark=pc1_conn
add chain=forward action=mark-packet connection-mark=pc1_conn new-packet-mark=pc1_traffic
```

#### 默认队列 Bucket

```ros
/queue/tree
add name=download parent=Local packet-mark=pc1_traffic max-limit=10M
add name=upload parent=Public packet-mark=pc1_traffic max-limit=10M
```

在这种情况下，bucket-size=0.1，因此桶容量 = 0.1 x 10M = 1M。

如果桶已满（即客户端在一段时间内未使用队列的全部容量），则接下来的 1Mb 流量可以以不受限制的速度通过队列。

#### 大型队列 Bucket

```ros
/queue/tree
add name=download parent=Local packet-mark=pc1_traffic max-limit=10M bucket-size=10
add name=upload parent=Public packet-mark=pc1_traffic max-limit=10M bucket-size=10
```

让我们尝试将相同的逻辑应用于 bucket size 处于最大值的情况：

在这种情况下，bucket-size=10，因此桶容量 = 10 x 10M = 100M。

如果桶已满（即客户端在一段时间内未使用队列的全部容量），则接下来的 100Mb 流量可以以不受限制的速度通过队列。

因此，您可以实现：

- 20Mbps 传输速度持续 10 秒。
- 60Mbps 传输突发持续 2 秒。
- 1Gbps 传输突发约 100 毫秒。

因此，您可以看到桶允许通过队列的流量具有某种“突发性”。该行为类似于普通突发功能，但缺少突发的上限。如果我们在队列结构中利用 bucket size，可以避免此缺陷：

#### 大型子队列 Bucket，小型父队列 Bucket

```ros
/queue/tree
add name=download_parent parent=Local max-limit=20M
add name=download parent=download_parent packet-mark=pc1_traffic max-limit=10M bucket-size=10
add name=upload_parent parent=Public max-limit=20M
add name=upload parent=upload_parent packet-mark=pc1_traffic max-limit=10M bucket-size=10
```

在这种情况下：

- 父队列 bucket-size=0.1，桶容量 = 0.1 x 20M = 2M
- 子队列 bucket-size=10，桶容量 = 10 x 10M = 100M

父队列的令牌将比子队列更快耗尽，由于子队列始终从父队列借用令牌，整个系统将受限于父队列的令牌速率——在本例中为 max-limit=20M。此速率将持续到子队列的令牌耗尽，然后将被限制为其 10Mbps 的令牌速率。

通过这种方式，我们可以实现高达 20Mbps 的突发，持续最长 10 秒。

## 配置

我们需要遵循三个基本步骤来创建 HTB：

- **匹配并标记流量** – 对流量进行分类以供后续使用。它包含一个或多个匹配参数，用于为特定类别选择数据包。
- **创建规则（策略）来标记流量** – 将特定流量类别放入特定队列，并定义为每个类别采取的操作。
- **为特定接口附加策略** – 为所有接口（global-in、global-out 或 global-total）、特定接口或特定父队列附加策略。

HTB 允许创建分层队列结构，并确定队列之间的关系，如“父子”或“子-子”。

一旦队列至少有一个子队列，它就成为一个**内部**队列。所有没有子队列的队列都是**叶子**队列。**叶子**队列实际消耗流量，**内部**队列仅负责流量分配。所有**叶子**队列均被平等对待。

在 RouterOS 中，必须指定 **parent** 选项，以将队列分配为另一个队列的子队列。

### 双重限制

HTB 中的每个队列都有两个速率限制：

- **CIR**（承诺信息速率）——（RouterOS 中的 **limit-at**）最坏情况下的速率，无论发生什么情况，流量都将获得此数量的带宽（假设我们实际上可以发送这么多数据）。
- **MIR**（最大信息速率）——（RouterOS 中的 **max-limit**）最佳情况下的速率，如果其队列的父队列有剩余带宽，流量可以达到的速率。

换句话说，首先将满足所有队列的 **limit-at**（**CIR**），然后子队列才会尝试从父队列借用必要的数据速率以达到其 **max-limit**（**MIR**）。

:::warning
**CIR** 将无条件分配给相应的队列（即使超过了父队列的 max-limit）。

:::

因此，为了确保双重限制功能的最佳（按设计）使用，我们建议遵循以下规则：

- 所有子队列的承诺速率之和必须小于或等于父队列可用的流量；

CIR(父)\* ≥ CIR(子1) +...+ CIR(子N)\* 如果父是主父队列，则 CIR(父)=MIR(父)

- 任何子队列的最大速率必须小于或等于父队列的最大速率。

MIR（父）≥ MIR（子1）且 MIR（父）≥ MIR（子2）且 ... 且 MIR（父）≥ MIR（子N）

# Winbox 中的队列颜色

- 已使用可用流量的 0% - 50% - 绿色
- 已使用可用流量的 50% - 75% - 黄色
- 已使用可用流量的 75% - 100% - 红色

#### 优先级

我们已经知道，**limit-at**（**CIR**）将无条件分配给所有队列。

优先级负责将父队列的剩余流量分配给子队列，以便它们能够达到 **max-limit**。

优先级较高的队列将比优先级较低的队列更先达到其 **max-limit**。8 是最低优先级，1 是最高优先级。

请注意，优先级仅在以下情况下有效：

- 对于**叶子**队列——**内部**队列中的优先级没有意义。
- 如果指定了 **max-limit**（非 0）。

### 示例

在本节中，我们将分析 HTB 的实际运行情况。为此，我们将采用一个 HTB 结构，并尝试通过改变 HTB 需要处理的内入流量以及更改某些选项，来覆盖所有可能的情况和功能。

#### 结构

我们的 HTB 结构将由 5 个队列组成：

- **Queue01** 内部队列，有两个子队列——**Queue02** 和 **Queue03**
- **Queue02** 内部队列，有两个子队列——**Queue04** 和 **Queue05**
- **Queue03** 叶子队列
- **Queue04** 叶子队列
- **Queue05** 叶子队列

**Queue03**、**Queue04** 和 **Queue05** 是需要持续 10Mbps 的客户端。出接口能够处理 10Mbps 的流量。

#### 示例 1：常规情况

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/queues/img/htb-hierarchical-token-bucket-02.webp)

- **Queue01** limit-at=0Mbps max-limit=10Mbps
- **Queue02** limit-at=4Mbps max-limit=10Mbps
- **Queue03** limit-at=6Mbps max-limit=10Mbps priority=1
- **Queue04** limit-at=2Mbps max-limit=10Mbps priority=3
- **Queue05** limit-at=2Mbps max-limit=10Mbps priority=5

#### 示例 1 的结果

- **Queue03** 将获得 6Mbps。
- **Queue04** 将获得 2Mbps。
- **Queue05** 将获得 2Mbps。
- **说明：** HTB 的构建方式使得在满足所有 **limit-at** 后，主队列不再有吞吐量可供分配。

#### 示例 2：带 max-limit 的常规情况

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/queues/img/htb-hierarchical-token-bucket-03.webp)

- **Queue01** limit-at=0Mbps max-limit=10Mbps
- **Queue02** limit-at=4Mbps max-limit=10Mbps
- **Queue03** limit-at=2Mbps max-limit=10Mbps priority=3
- **Queue04** limit-at=2Mbps max-limit=10Mbps priority=1
- **Queue05** limit-at=2Mbps max-limit=10Mbps priority=5

#### 示例 2 的结果

- **Queue03** 将获得 2Mbps。
- **Queue04** 将获得 6Mbps。
- **Queue05** 将获得 2Mbps。
- **说明：** 在满足所有 **limit-at** 后，HTB 将吞吐量分配给优先级最高的队列。

#### 示例 3：内部队列 limit-at

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/queues/img/htb-hierarchical-token-bucket-04.webp)

- **Queue01** limit-at=0Mbps max-limit=10Mbps。
- **Queue02** limit-at=8Mbps max-limit=10Mbps。
- **Queue03** limit-at=2Mbps max-limit=10Mbps priority=1。
- **Queue04** limit-at=2Mbps max-limit=10Mbps priority=3。
- **Queue05** limit-at=2Mbps max-limit=10Mbps priority=5。

#### 示例 3 的结果

- **Queue03** 将获得 2Mbps。
- **Queue04** 将获得 6Mbps。
- **Queue05** 将获得 2Mbps。
- **说明：** 在满足所有 **limit-at** 后，HTB 将吞吐量分配给优先级最高的队列。但在本例中，**内部**队列 **Queue02** 指定了 **limit-at**，通过这样做，它为队列 **Queue04** 和 **Queue05** 预留了 8Mbps 的吞吐量。在这两个队列中，**Queue04** 具有最高优先级，这就是它获得额外吞吐量的原因。

#### 示例 4：叶子队列 limit-at

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/queues/img/htb-hierarchical-token-bucket-05.webp)

- **Queue01** limit-at=0Mbps max-limit=10Mbps。
- **Queue02** limit-at=4Mbps max-limit=10Mbps。
- **Queue03** limit-at=6Mbps max-limit=10Mbps priority=1。
- **Queue04** limit-at=2Mbps max-limit=10Mbps priority=3。
- **Queue05** limit-at=12Mbps max-limit=15Mbps priority=5。

#### 示例 4 的结果

- **Queue03** 将获得约 3Mbps。
- **Queue04** 将获得约 1Mbps。
- **Queue05** 将获得约 6Mbps。
- **说明：** 仅为了满足所有 **limit-at**，HTB 就被迫分配 20Mbps——6Mbps 给 **Queue03**，2Mbps 给 **Queue04**，12Mbps 给 **Queue05**，但我们的出接口只能处理 10Mbps。由于出接口队列通常是 FIFO，吞吐量分配将保持 6:2:12 或 3:1:6 的比例。