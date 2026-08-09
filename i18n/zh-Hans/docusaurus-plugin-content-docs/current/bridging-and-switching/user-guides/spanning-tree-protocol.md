# 生成树协议

> 本页介绍 MikroTik RouterOS 中的生成树协议（STP），详细说明其如何通过选择根桥和利用桥接协议数据单元（BPDU）优化端口使用来防止网络环路。它强调在较大型网络中需手动配置，并提供了用于检查桥接和端口上 STP 状态的监控命令。

# 生成树协议

---

生成树协议的目的是在拥有冗余链路的同时，提供创建无环二层拓扑的能力。当连接多个桥接器或交叉连接桥接端口时，可能会产生网络环路，严重影响网络的稳定性。生成树协议通过引入根桥的概念来解决此问题。同一二层域中的所有桥接器将交换关于到根桥最短路径的信息。之后，每个桥接器将协商使用哪些端口来达到根桥。此信息交换借助桥接协议数据单元（BPDU）完成。STP 将为每个桥接器禁用某些端口以避免环路，同时确保所有桥接器仍能相互通信。有关协议的深入描述，请参阅 IEEE 802.1D 标准。

作为最佳实践，始终建议手动设置每个桥接器的优先级、端口优先级和端口路径开销，以确保二层功能始终正常。对于由 1 到 2 个启用（R/M）STP 的桥接器组成的网络，将 STP 相关值保留为默认值是可以接受的，但对于较大的网络，强烈建议手动设置这些值。由于 STP 通过检查网络中桥接器的 STP 相关值来选举根桥和根端口，将 STP 设置保留为自动可能会选举出非预期的根桥和根端口，并且在硬件故障的情况下可能导致网络无法访问。

:::info
RouterOS 桥接器不兼容 PVST 及其变体。PVST BPDU（目的 MAC 地址为 01:00:0C:CC:CC:CD）会被 RouterOS 桥接器视为典型的组播数据包。简单来说，它们会经过 RouterOS 桥接/交换转发逻辑，并可能被标记或取消标记。
:::

## 监控

---

您可以使用 `/interface/bridge/monitor` 命令检查桥接器的 STP 状态，例如：

```ros
/interface/bridge/monitor bridge1
                    state: enabled                         
      current-mac-address: 74:4D:28:6F:31:10               
                bridge-id: 0x8000.74:4D:28:6F:31:10        
              root-bridge: no                              
           root-bridge-id: 0.74:4D:28:11:70:6B             
  regional-root-bridge-id: 0.74:4D:28:11:70:6B             
           root-path-cost: 0                               
                root-port: combo1                          
               port-count: 2                               
    designated-port-count: 0                               
        mst-config-digest: 4e22fbb9ede77faa45ec995c4ffa8085
             fast-forward: no                              
         multicast-router: yes                             
             igmp-querier: none                            
              mld-querier: none                            
        declared-vlan-ids: 1                               
      registered-vlan-ids: 1      
```

请注意，根桥没有任何根端口，只有指定端口。

您可以使用 `/interface/bridge/port/monitor` 命令检查桥接端口的 STP 状态，例如：

```ros
/interface/bridge/port/monitor [find interface=combo1]
                  interface: combo1             
                     status: in-bridge          
                    port-id: 0x80.1             
                       role: root-port          
                  edge-port: no                 
        edge-port-discovery: yes                
        point-to-point-port: yes                
               external-fdb: no                 
               sending-rstp: yes                
                   learning: yes                
                 forwarding: yes                
           actual-path-cost: 2000               
    internal-root-path-cost: 2000               
       designated-bridge-id: 0.74:4D:28:11:70:6B
   designated-internal-cost: 0                  
         designated-port-id: 0x80.1             
  designated-remaining-hops: 20                 
                 bpdu-tx-rx: 3/7791             
        discard-transitions: 0                  
        forward-transitions: 1                  
                   tc-tx-rx: 2/2                
           topology-changes: 1                  
       last-topology-change: 4h19m43s           
           multicast-router: no                 
           hw-offload-group: switch1            
          declared-vlan-ids: 1                  
                             100                
        registered-vlan-ids: 1                  
                             100                
                             200-203     
```

请注意，`root-bridge-id` 由桥接器优先级和桥接器的 MAC 地址组成；对于非根桥，根桥将显示为 `designated-bridge`。

:::warning
当使用设置为使用 802.1Q 作为 EtherType 的桥接器时，它们会将 BPDU 发送到 01:80:C2:00:00:00，该地址被 MSTP、RSTP 和 STP 使用。当使用 802.1ad 作为桥接器 VLAN 协议时，BPDU 与 802.1Q 桥接器不兼容，并且它们被发送到 01:80:C2:00:00:08。如果二层网络中存在不同的桥接器 VLAN 协议，（R/M）STP 将无法正常运行。
:::

## STP 与 RSTP

---

STP 和快速生成树协议（RSTP）在许多网络中被广泛使用，但几乎所有网络都已转向仅使用 RSTP，因为它具有优势。STP 是一种非常古老的协议，其收敛时间（完全学习网络拓扑变化并继续正确转发流量所需的时间）长达 50 秒。RSTP 的收敛时间要短得多，只需几秒甚至几毫秒。建议使用 RSTP 而不是 STP，因为它速度更快，并且向后兼容 STP。RSTP 更快的原因之一是减少了可能的端口状态，以下是 STP 可能的端口状态列表：

- **转发（Forwarding）** - 端口参与流量转发，学习 MAC 地址，并接收 BPDU。
- **监听（Listening）** - 端口不参与流量转发，不学习 MAC 地址，但接收 BPDU。
- **学习（Learning）** - 端口不参与流量转发，但学习 MAC 地址。
- **阻塞（Blocking）** - 端口因导致环路而被阻塞，但接收 BPDU。
- **禁用（Disabled）** - 端口被禁用或不活动。

在 RSTP 中，禁用、监听和阻塞端口状态被替换为仅一种称为**丢弃（Discarding）**的状态：

- **转发（Forwarding）** - 端口参与流量转发，学习 MAC 地址并接收 BPDU（forwarding=yes）。
- **学习（Learning）** - 端口不参与流量转发，但学习 MAC 地址（learning=yes）。
- **丢弃（Discarding）** - 端口不参与流量转发，不学习 MAC 地址，但接收 BPDU（forwarding=no）。

在 STP 中，端口主要按状态分类（例如，转发、监听、学习、阻塞、禁用）。端口行为基于生成树算法动态确定，但没有明确分配角色。转发或阻塞流量的逻辑源自根桥、根端口和指定端口的计算，但这些被认为是生成树拓扑的一部分，而非正式化的端口角色。RSTP 明确定义了端口角色，并引入了备份路径的概念，通过备用端口（Alternate Port）和备份端口（Backup Port）角色明确表示。这些角色在 STP 中不存在，因为 STP 对阻塞端口进行通用处理，不区分其作为潜在备份的功能。

以下是 RSTP 协议的端口角色分类：

- **根端口（Root Port）** - 面向根桥且具有到根桥最佳（最低开销）路径的端口。每个桥接器（根桥自身除外）仅选举一个根端口。
- **指定端口（Designated Port）** - 背向根桥的端口，将流量从根桥转发到下游设备。
- **备用端口（Alternate Port）** - 面向根桥但不转发流量的端口。该端口在当前根端口发生故障时提供到根桥的备份路径。
- **备份端口（Backup Port）** - 背向根桥但不转发流量的端口。该端口作为同一网段上指定端口的备份。
- **禁用端口（Disabled Port）** - 禁用或不活动的端口。

在 STP 中，桥接器之间的连通性通过相邻桥接器之间发送和接收 BPDU 来确定。指定端口向根端口发送 BPDU。如果连续 3 次**HelloTime** 内未收到 BPDU，则认为连接不可用，并将开始网络拓扑收敛。在某些情况下，可以通过减少 `forward-delay` 定时器来缩短 STP 收敛时间，该定时器负责端口可以处于学习/监听状态的时间。

在 RouterOS 中，可以指定哪些桥接端口是边缘端口。边缘端口是不应接收任何 BPDU 的端口。这是有益的，因为它允许 STP 跳过学习和监听状态，直接进入转发状态。此功能有时称为 **PortFast**。您可以将此参数保留为默认值 **auto**，也可以手动指定。对于不应在其后面再有桥接器的端口，可以手动将其设置为边缘端口。通常，这些是接入端口。

此外，桥接端口 `point-to-point` 指定桥接端口是否通过点对点链路连接到桥接器，以便在故障时更快收敛。通过将此属性设置为 `yes`，您强制该链路为点对点链路，这将跳过检测机制，该机制会等待来自此单条链路上其他设备的 BPDU。通过将此属性设置为 `no`，您暗示一条链路可以从多个设备接收 BPDU。通过将此属性设置为 `yes`，您可以显著改善（R/M）STP 收敛时间。通常，仅当可能在其他设备连接到链路之间时，才应将此属性设置为 `no`。这主要与无线介质和以太网集线器相关。如果以太网链路是全双工的，`auto` 会启用点对点功能。当 `protocol-mode` 设置为 `none` 时，此属性无效。

### 默认值

创建桥接器或将端口添加到桥接器时，RouterOS 会分配以下默认值：

- 默认桥接器优先级：**32768** / **0x8000**
- 默认桥接端口路径开销：**基于接口速度**
- 默认桥接端口优先级：**0x80**
- BPDU 消息老化时间增量：**1**
- HelloTime：**2**
- 默认最大消息老化时间：**20**

桥接接口设置 `port-cost-mode` 更改桥接端口的 `path-cost` 和 `internal-path-cost` 模式，利用基于接口速度的自动值。此设置不影响手动配置了 `path-cost` 或 `internal-path-cost` 属性的桥接端口。以下示例说明了与特定数据速率对应的路径开销（中间速率按比例计算）：

| 数据速率 | 长模式 | 短模式 |
| :-- | :-- | --: |
| 10 Mbps | 2,000,000 | 100 |
| 100 Mbps | 200,000 | 19 |
| 1 Gbps | 20,000 | 4 |
| 10 Gbps | 2,000 | 2 |
| 25 Gbps | 800 | 1 |
| 40 Gbps | 500 | 1 |
| 50 Gbps | 400 | 1 |
| 100 Gbps | 200 | 1 |

对于绑定接口，应用所有绑定成员端口中最高的 `path-cost` 值，该值不受绑定的总链路速度影响。对于虚拟接口（如 VLAN、EoIP、VXLAN）以及 wifi、wireless 和 60GHz 接口，长模式分配 `path-cost` 为 20,000，短模式为 10。对于动态桥接的接口（例如 wifi、wireless、PPP、VPLS），`path-cost` 默认为长模式 20,000，短模式 10。但是，这可以通过动态添加接口到桥接器的服务手动覆盖，例如，使用 CAPsMAN 的 `datapath.bridge-cost` 设置。RouterOS 7.13 之前的版本不会根据链路速度更改端口路径开销，对于 10M、100M、1000M 和 10000M 链路速度，端口添加到桥接器时的默认路径开销值始终为 **10**。

BPDU 的老化时间由 BPDU 经过的桥接器数量乘以消息老化时间决定。由于 RouterOS 使用 **1** 作为消息老化时间增量，因此 BPDU 数据包可以通过 `max-message-age` 参数中指定的尽可能多的桥接器。默认情况下，此值设置为 **20**。这意味着在第 20 个桥接器之后，BPDU 数据包将被丢弃，下一个桥接器将成为根桥。请注意，如果设置了 `max-message-age=20`，则很难预测第 21 个桥接器上哪些端口将成为指定端口，并可能导致流量无法正确转发。

:::warning
如果使用了桥接过滤规则，请确保允许目的 MAC 地址为 **01:80:C2:00:00:00** 的数据包，因为这些数据包携带对 STP 正常运行至关重要的 BPDU。
:::

### 选举过程

要在网络中正确配置 STP，您需要了解选举过程以及哪些参数按何种顺序参与。在 RouterOS 中，根桥将根据以下顺序选择最小优先级和最小 MAC 地址：

1. 桥接器优先级（最低）。
2. 桥接器 MAC 地址（最低）。

在 RouterOS 中，根端口根据最低根端口路径开销、最低桥接器标识符和最低桥接端口 ID 按以下顺序选举：

1. 根端口路径开销（最低）
2. 桥接器标识符（最低）
3. 桥接端口 ID（最低）

首先，当设备考虑选择其哪个端口作为根端口时，它会检查其端口看到的**根路径开销**。如果两个或多个端口的根路径开销相同，则将检查**上游**设备的**桥接器标识符**，连接到最低桥接器标识符的端口将成为根端口。如果在两个或多个端口上看到相同的桥接器标识符，则将检查**上游**设备的**桥接端口 ID**。

## 属性说明

根路径开销：所有桥接器都有根路径开销。根桥的根路径开销为 0。对于所有其他桥接器，它是到根桥的最低开销路径上的端口路径开销之和。您可以在 `/interface/bridge/port` 下修改本地端口路径开销。
桥接器标识符是“桥接器优先级”和“桥接器 MAC”的组合，可在 `/interface/bridge` 下配置。

桥接端口 ID 是“唯一 ID”和“桥接端口优先级”的组合。唯一 ID 在将桥接端口添加到桥接器时自动分配。它无法编辑。可以在 WinBox 的“Bridge Port”“Port Number”列中查看，或使用 `/interface/bridge/port/monitor` 查看，如 `port-number`。

:::tip 理解 STP 端口选举
确保将路径开销和优先级应用到正确的端口：

- **路径开销**影响面向*根桥*的端口。（在根桥端口上设置路径开销无效）。
- **端口优先级**影响背向*根桥*的端口。
- **桥接器标识符**不影响设备自身的根端口选举；它影响*下游*设备的根端口选举。
:::

:::warning 桥接器优先级兼容性
RouterOS 允许设置 0 到 65535 之间的任何桥接器优先级值。但是，IEEE 802.1W 标准严格要求桥接器优先级必须以 4096 为步长。为避免与其他厂商设备不兼容，请**仅**使用以下优先级值：
`0, 4096, 8192, 12288, 16384, 20480, 24576, 28672, 32768, 36864, 40960, 45056, 49152, 53248, 57344, 61440`
:::

### 示例

#### 根路径开销示例

![根路径](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/spanning-tree-protocol-01.webp)

此示例说明了根路径开销的工作原理。SW1 将作为根桥，因为它具有最低的优先级 0x1000。每个桥接器将计算到根桥的路径开销。在计算根路径开销时，桥接器会考虑其端口上配置的路径开销加上相邻桥接器通告的根路径开销。

**SW1**：由于它是根桥，它向其邻居通告根路径开销为 0，即使它配置了路径开销为 10。

**SW2：****ether1** 的根路径开销为 0 + 25=**25**。在 **ether2** 路径上，开销将为 10+10+10+0=**30**。

**SW3：** **ether2** 的根路径开销为 0 + 10=**10**。在 **ether4** 路径上，路径开销将为 10+5+25+0=**40**。

**SW4：** **ether1** 的根路径开销为 0+25+5=**30**。在 **ether4** 上，路径开销将为 10+10+0=**20**。

具有最低路径开销的端口将被选举为根端口。STP 拓扑中的每个桥接器都需要一条到根桥的路径。找到最佳路径后，冗余路径将被阻塞，在这种情况下，即 SW2 和 SW4 之间的路径。

:::warning
您可以在根桥上配置路径开销，但只有在桥接器失去其根状态时才会被考虑。
:::

#### STP 示例

![STP 示例 1](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/spanning-tree-protocol-02.webp)

在此示例中，我们希望确保从 ServerA 到 ServerB 的连接具有二层冗余。如果端口连接到非桥接器且未运行（R）STP 的设备，则该端口被视为边缘端口。在这种情况下，ServerA 和 ServerB 连接到边缘端口。这可以通过在网络中使用 STP 来实现。以下是每个交换机的配置示例：

- SW1 的配置：

```ros
/interface/bridge
add name=bridge priority=0x1000
/interface/bridge/port
add bridge=bridge interface=ether1 priority=0x60
add bridge=bridge interface=ether2 priority=0x50
add bridge=bridge interface=ether3 priority=0x40
add bridge=bridge interface=ether4 priority=0x30
add bridge=bridge interface=ether5
```

- SW2 的配置：

```ros
/interface/bridge
add name=bridge priority=0x2000
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
add bridge=bridge interface=ether3
```

- SW3 的配置

```ros
/interface/bridge
add name=bridge priority=0x3000
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
add bridge=bridge interface=ether3
```

- SW4 的配置：

```ros
/interface/bridge
add name=bridge priority=0x4000
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2 path-cost=20
add bridge=bridge interface=ether3
```

在此示例中，**SW1** 是根桥，因为它具有最低的桥接器优先级。**SW2** 和 **SW3** 的 ether1、ether2 连接到根桥，ether3 连接到 **SW4**。当所有交换机正常工作时，流量将从 ServerA 通过 SW1\_ether2、SW2、SW4 流向 ServerB。如果 **SW1** 发生故障，**SW2** 将因具有次低优先级而成为根桥，如图中虚线所示。以下是每个交换机的端口及其角色列表：

- **根端口（root-port）** - SW2\_ether2, SW3\_ether2, SW4\_ether1
- **备用端口（alternate-port）** - SW2\_ether1, SW3\_ether1, SW4\_ether2
- **指定端口（designated-port）** - SW1\_ether1, SW1\_ether2, SW1\_ether3, SW1\_ether4, SW1\_ether5, SW2\_ether3, SW3\_ether3, SW4\_ether3

:::note
**注意：** 根据 802.1Q 建议，您应该使用步长为 4096 的桥接器优先级。要设置推荐的优先级，使用十六进制表示法更方便，例如，0 是 0x0000，4096 是 0x1000，8192 是 0x2000，依此类推（0..F）。
:::

## 多生成树协议

---

多生成树协议（MSTP）在桥接接口上使用，以确保跨多个 VLAN 的无环拓扑。MSTP 还可以提供二层冗余，并可用作 VLAN 的负载均衡技术，因为它能够在不同 VLAN 间拥有不同路径。MSTP 的运行方式与（R）STP 非常相似，（R）STP 的许多概念可以应用于 MSTP，强烈建议在使用 MSTP 之前理解（R）STP 背后的原理，但在设计启用 MSTP 的网络时，必须考虑一些差异。

如果使用（R）STP，BPDU 会通过桥接器中的所有物理接口发送，以确定环路并阻止可能导致环路的端口转发流量。如果某个 VLAN 内存在环路，（R）STP 可能无法检测到。一些 STP 变体通过在每个 VLAN 上运行一个 STP 实例（PVST）来解决此问题，但这已被证明效率低下；而另一些 STP 变体通过在所有 VLAN 上运行单个 STP 实例（CST）来解决此问题，但它缺乏为每个 VLAN 或 VLAN 组进行负载均衡的可能性。MSTP 倾向于通过使用可以定义一组 VLAN（VLAN 映射）的 MST 实例来解决这两个问题，这些实例可用于负载均衡和冗余，这意味着每个 VLAN 组可以有不同的根桥和不同的路径。请注意，将多个 VLAN 分组到单个实例中是有益的，以减少每次网络拓扑变化的 CPU 周期数。

:::danger
在启用 MSTP 的 RouterOS 中，桥接器优先级是 CIST 的根桥优先级，如 IEEE 802.1Q 标准所述，桥接器优先级必须以 4096 为步长，最低的 12 位被忽略。有效的桥接器优先级为：0, 4096, 8192, 12288, 16384, 20480, 24576, 28672, 32768, 36864, 40960, 45056, 49152, 53248, 57344, 61440。当设置无效的桥接器优先级时，RouterOS 会警告您并将值截断为有效值，但会将原始值保存在配置中，因为无效的桥接器优先级值仍可在运行 RouterOS 的设备之间的（R）STP 中使用，但建议使用有效的桥接器优先级。
:::

### MSTP 区域

MSTP 在称为区域的组中工作。每个区域将有一个区域根桥，区域之间将选举一个根桥。MSTP 将使用内部生成树（IST）在区域内构建网络拓扑，并使用公共生成树（CST）在区域外构建多个区域之间的网络拓扑。MSTP 将这两种协议组合成公共和内部生成树（CIST），它保存有关区域内和区域间拓扑的信息。从 CST 的角度来看，一个区域看起来就像一个单一的虚拟桥接器，因此 MSTP 被认为对于大型网络具有很高的可扩展性。要使桥接器处于同一区域，它们的配置必须匹配。BPDU 不包含 VLAN 映射，因为它们可能很大，而是传输计算出的哈希值。如果桥接器通过端口接收到 BPDU 且配置不匹配，则 MSTP 将把该端口视为边界端口，并认为它可用于到达其他区域。以下是 MSTP 认为 BPDU 来自同一区域需要匹配的参数列表：

- 区域名称
- 区域修订号
- VLAN 到 MST 实例 ID 的映射（计算出的哈希值）

可以创建没有区域的 MSTP 网络，但要实现按 VLAN 组进行负载均衡，桥接器必须从与其连接的桥接器接收到具有上述相同参数的 BPDU。在 RouterOS 中，默认区域名称为空，区域修订号为 0，这些是有效值，但您必须确保它们匹配才能将多个桥接器置于单个 MSTP 区域中。如果桥接器分散在网络中，则区域无法存在；这些桥接器必须至少以一种方式连接，以便它们可以在不离开区域的情况下发送和接收 BPDU，例如，如果具有不同区域相关参数的桥接器位于两个具有相同区域相关参数的桥接器之间，则将存在至少 3 个不同的 MSTP 区域。

![MSTP 拓扑](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/spanning-tree-protocol-03.webp)

在单个 MSTP 区域中运行每个桥接器的缺点是 CPU 周期过多。相比之下，PVST(+) 为网络上存在的每个 VLAN ID 创建一个生成树实例，由于网络中可能存在的路径非常有限，这种方法会产生大量开销和不必要的 CPU 周期。这也意味着这种方法扩展性不佳，并且可能使 CPU 性能不强的交换机过载。MSTP 通过将网络划分为 MSTP 区域来解决此问题，其中该区域内的每个桥接器将交换和处理有关同一区域内存在的 VLAN 的信息，但会在后台运行单个生成树协议实例以维护区域之间的网络拓扑。这种方法已被证明更加有效和可扩展。这意味着对于较大的网络，应使用区域来减少 CPU 周期。

在区域中，您可以定义 MST 实例，用于配置每个 VLAN 组的负载均衡并选举区域根桥。值得一提的是，每个区域中都存在一个预定义的 MST 实例，在大多数文档中，这被称为 **MSTI0**。此 MST 实例被视为默认 MST 实例。某些参数适用于此特殊 MST 实例。当流量通过启用 MSTP 的桥接器时，MSTP 将查找具有匹配 VLAN 映射的 MST 实例，但如果某个 VLAN ID 不存在 VLAN 映射，则流量将归入 **MSTI0**。

:::warning
由于 MSTP 要求在桥接接口上启用 VLAN 过滤，请确保您已在 `/interface/bridge/vlan` 中允许所有必需的 VLAN ID，否则流量将不会被转发，并且可能看起来像是 MSTP 配置错误，尽管这实际上是 VLAN 过滤配置错误。
:::

### 选举过程

MSTP 中的选举过程可以分为两个部分：区域内和区域间。要使 MSTP 正常工作，始终需要有一个区域根，即区域内的根桥，以及一个 CIST 根，即区域间的根桥。区域根是区域内的根桥，需要区域根桥来正确设置区域内 VLAN 组的负载均衡。CIST 根将用于配置哪些端口将成为备用/备份端口（非活动）以及哪些端口将成为根端口（活动）。

:::warning
区域之间没有按 VLAN 组的负载均衡，没有根端口选举过程，MSTP 区域之间的端口阻塞方式与（R）STP 相同。如果 CIST 阻塞了 MSTP 区域内的端口以防止 MSTP 区域之间的流量环路，则该端口对于 IST 来说仍然可以处于活动状态，以便在 MSTP 区域内按 VLAN 组进行负载均衡。
:::

- 以下参数参与选举 MSTP 区域内的区域根桥或根端口：

| 属性 | 描述 |
| :-- | :-- |
| **priority** (*整数：0..65535 十进制格式或 0x0000-0xffff 十六进制格式*；默认值：**32768 / 0x8000**) | `/interface/bridge/msti`，MST 实例优先级，用于在 MSTP 区域内选举区域根。必须以 4096 (0x1000) 为步长设置；最低的 12 位被忽略。有效值：0x0000, 0x1000, 0x2000, ..., 0xf000（或十进制等效值：0, 4096, 8192, ..., 61440）。 |
| **internal-path-cost** (*整数：1..200000000*；默认值：) | `/interface/bridge/port`，未知 VLAN ID（MSTI0）到区域根的路径开销，用于 MSTP 区域内的根端口。 |
| **priority** (*0x00 \| 0x10 \| 0x20 \| 0x30 \| 0x40 \| 0x50 \| 0x60 \| 0x70 \| 0x80 \| 0x90 \| 0xa0 \| 0xb0 \| 0xc0 \| 0xd0 \| 0xe0 \| 0xf0*；默认值：**0x80**) | `/interface/bridge/port/mst-override`，为定义的 MST 实例设置的 MST 端口优先级，用于区域根桥上的桥接端口。必须以 16 (0x10) 为步长设置。 |
| **internal-path-cost** (*整数：1..200000000*；默认值：) | `/interface/bridge/port/mst-override`，为定义的 MST 实例设置的 MST 端口路径开销，用于 MSTP 区域内的非根桥端口。 |

- 以下参数参与选举 CIST 根桥或 CIST 根端口：

| 属性 | 描述 |
| :-- | :-- |
| **priority** (*整数：0..65535 十进制格式或 0x0000-0xffff 十六进制格式*；默认值：**32768 / 0x8000**) | `/interface/bridge`，CIST 桥接器优先级，用于选举 CIST 根桥。必须以 4096 (0x1000) 为步长设置；最低的 12 位被忽略。 |
| **priority** (*0x00 \| 0x10 \| 0x20 \| 0x30 \| 0x40 \| 0x50 \| 0x60 \| 0x70 \| 0x80 \| 0x90 \| 0xa0 \| 0xb0 \| 0xc0 \| 0xd0 \| 0xe0 \| 0xf0*；默认值：**0x80**) | `/interface/bridge/port`，CIST 端口优先级，用于在 CIST 根桥上选举 CIST 根端口。必须以 16 (0x10) 为步长设置。 |
| **path-cost** (*整数：1..200000000*；默认值：) | `/interface/bridge/port`，CIST 端口路径开销，用于在 CIST 非根桥端口上选举 CIST 根端口。 |

:::warning
MSTP 检查以选举根桥/端口的参数顺序与（R）STP 相同，您可以在（R）STP 选举过程部分阅读更多相关信息。
:::

### MST 实例

**子菜单：** `/interface/bridge/msti`

此部分用于将多个 VLAN ID 分组到单个实例中，以便在 MSTP 区域内为每个 VLAN 组创建不同的根桥。

| 属性 | 描述 |
| :-- | :-- |
| **bridge** (*文本*；默认值：) | MST 实例分配到的桥接器。 |
| **identifier** (*整数：1..31*；默认值：) | MST 实例标识符。 |
| **priority** (*整数：0..65535 十进制格式或 0x0000-0xffff 十六进制格式*；默认值：**32768 / 0x8000**) | MST 实例优先级用于确定 MSTP 区域中一组 VLAN 的根桥。 |
| **vlan-mapping** (*整数：1..4094*；默认值：) | 要分配给 MST 实例的 VLAN ID 列表。此设置接受 VLAN ID 范围以及逗号分隔的值。例如 `vlan-mapping=100-115,120,122,128-130` |

### MST 覆盖

**子菜单：** `/interface/bridge/port/mst-override`

此部分用于在 MSTP 区域内为每个 VLAN 映射选择所需路径。

| 属性 | 描述 |
| :-- | :-- |
| **disabled** (*yes \| no*；默认值：**no**) | 条目是否被禁用。 |
| **internal-path-cost** (*整数：1..200000000*；默认值：) | MST 实例 VLAN 映射的路径开销，用于面向根桥的 VLAN 以操纵路径选择；优先选择较低的路径开销。 |
| **identifier** (*整数：1..31*；默认值：) | MST 实例标识符。 |
| **priority** (*整数：0..240*；默认值：**128**) | MST 实例 VLAN 的优先级，用于背向根桥的 VLAN 以操纵路径选择；优先选择较低的优先级。 |
| **interface** (*名称*；默认值：) | 要使用配置的 MST 实例 VLAN 映射以及定义的路径开销和优先级的端口名称。 |

### 监控

与（R）STP 类似，也可以监控 MSTP 状态。通过监控桥接接口本身，可以查看当前的 CIST 根桥和 MSTI0 的当前区域根桥。还可以查看 MST 实例标识符和 VLAN 映射的计算哈希值。这在确保某些桥接器位于同一 MSTP 区域时非常有用。下面是一个监控 MSTP 桥接器的示例：

```ros
/interface/bridge/monitor bridge
                    state: enabled
      current-mac-address: 6C:3B:6B:7B:F0:AA
                bridge-id: 0x8000.6C:3B:6B:7B:F0:AA 
              root-bridge: no
           root-bridge-id: 0x1000.64:D1:54:24:23:72
  regional-root-bridge-id: 0x4000.6C:3B:6B:7B:F0:AA
           root-path-cost: 10
                root-port: ether4
               port-count: 5
    designated-port-count: 3
        mst-config-digest: 74edbeefdbf82cf63a70cf60e43a56f3
             fast-forward: no                              
         multicast-router: yes                             
             igmp-querier: none                            
              mld-querier: none                            
        declared-vlan-ids: 1                               
      registered-vlan-ids: 1
```

在 MSTP 中，可以监控 MST 实例。这对于确定某个 MST 实例和 VLAN 组的当前区域根桥非常有用。下面是一个监控 MST 实例的示例：

```ros
/interface/bridge/msti/monitor 1
                    state: enabled
               identifier: 2
      current-mac-address: 6C:3B:6B:7B:F0:AA
                bridge-id: 0x8000.6C:3B:6B:7B:F0:AA
              root-bridge: no
           root-bridge-id: 0.00:00:00:00:00:00
  regional-root-bridge-id: 0x1002.6C:3B:6B:7B:F9:08
           root-path-cost: 0
                root-port: ether2
               port-count: 5
    designated-port-count: 1
```

还可以监控某个 MST 覆盖条目。这在配置 MSTP 区域中的根端口和备用/备份端口时，对于确定某个 MST 实例的端口角色非常有用。下面是一个监控 MST 覆盖条目的示例：

```ros
/interface/bridge/port/mst-override/monitor 1
                      port: ether3
                    status: active
                identifier: 2
                   port-id: 0x80.1     
                      role: alternate-port
                  learning: no
                forwarding: no
   internal-root-path-cost: 15
         designated-bridge: 0x1002.6C:3B:6B:7B:F9:08
  designated-internal-cost: 0
        designated-port-id: 0x80.1  
 designated-remaining-hops: 20                      
                tx-rx-bpdu: 3/7991                  
       discard-transitions: 0                       
       forward-transitions: 1                       
                  tx-rx-tc: 2/2                     
          topology-changes: 1                       
```

### MSTP 示例

假设我们需要设计一个拓扑并配置 MSTP，使得 VLAN 10,20 沿一条路径转发，而 VLAN 30,40 沿另一条不同路径转发，同时所有其他 VLAN ID 沿其中一条路径转发。这可以通过设置 MST 实例并分配端口路径