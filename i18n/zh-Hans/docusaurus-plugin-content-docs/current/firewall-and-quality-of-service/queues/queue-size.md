# 队列大小

> 本页说明如何在 MikroTik RouterOS 中配置队列大小限制，详细阐述设置最大数据包数量对流量整形和调度的影响。文中通过比较 100% 整形器、调度器和默认队列类型的示例，展示数据包丢弃率和延迟情况。

# 队列大小

最大允许的队列大小可以指定为最大内存限制，但许多算法将其简化为最大数据包数量，因此实际使用的内存会因数据包大小不同而变化。

本页其余部分将演示此机制如何应用于处理数据包计数的队列类型，如 PFIFO、BFIFO、PCQ 和 RED。

## 示例

此示例旨在突出队列大小对特定队列中排队流量的影响。

为简化可视化，我们假设按步骤处理数据，并确切知道每一步将接收/传输多少数据包，且不会发生丢弃数据包的重传。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/queues/img/queue-size-01.webp)

如上图所示，共有 **25 个步骤**，在此时间范围内总计有 **1610 个传入数据包**。

### 100% 整形器

当队列为 100% 整形器时，任何超过允许限制的数据包将被立即丢弃。这样，所有未被丢弃的数据包将无延迟地发送出去。

让我们对示例应用 **max-limit=100 数据包/步骤** 的限制：

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/queues/img/queue-size-02.webp)

采用此类限制时，1610 个数据包中仅有 1250 个能够通过队列（**22.4% 数据包丢弃率**），但所有到达的数据包均无延迟。

### 100% 调度器

当队列为 100% 调度器时，完全不发生数据包丢弃，所有数据包均被排队，并在最早可能时刻发送出去。

在每一步中，队列必须首先发送上一步排队的数据包，然后才发送本步骤的数据包；这样可确保数据包的正确顺序。

我们再次使用相同的限制（**100 数据包/步骤**）。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/queues/img/queue-size-03.webp)

没有发生数据包丢失，但 630 个（**39.1%**）数据包经历了 1 步延迟，其余 170 个（**10.6%**）数据包经历了 2 步延迟。（延迟 = 时延）

### 默认小型队列类型

也可以选择折中方案，即队列同时使用整形和调度这两种排队机制。默认情况下，RouterOS 中大多数队列的队列大小为 10。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/queues/img/queue-size-04.webp)

共有 320 个（**19.9%**）数据包被丢弃，80 个（**5.0%**）数据包经历了 1 步延迟。

### 默认队列类型

RouterOS 中另一个常用的队列大小为 50。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/queues/img/queue-size-05.webp)

共有 190 个（**11.8%**）数据包被丢弃，400 个（**24.8%**）数据包经历了 1 步延迟。