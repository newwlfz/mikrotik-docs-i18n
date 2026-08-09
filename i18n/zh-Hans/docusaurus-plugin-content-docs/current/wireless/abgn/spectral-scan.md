# 频谱扫描

> MikroTik RouterOS 中的频谱扫描功能允许对无线频谱活动进行持续监控和可视化，包括在2.4GHz和5GHz频段上以10MHz步进进行干扰检测，同时提供控制台命令以进行详细分析，并可与The Dude网络监控工具集成。

# 频谱扫描

频谱扫描可以扫描无线网卡支持的所有频率，并直接在控制台中绘制结果。具体频率范围取决于网卡。r52n上允许的范围为：[4790; 6085]，[2182; 2549]。

无线网卡可以为任何20MHz宽的信道生成4微秒长的频谱快照。这被视为单个频谱样本。

为了提高数据质量，频谱以10MHz的频率步进进行扫描，这意味着在每个特定频率上样本覆盖加倍（考虑到20MHz宽的样本）。

:::warning
目前，不支持Atheros 802.11ac芯片（例如QCA98xx、IPQ-4018）。请参阅 [https://mikrotik.com/products](https://mikrotik.com/products) 以确定您设备上的无线芯片。
:::

## 控制台

### 频谱历史

![](https://manual.mikrotik.com/docs/wireless/abgn/img/spectral-scan-01.webp)

```ros
/interface/wireless/spectral-history <无线接口名称> 
```

绘制频谱图。图例和频率标尺每24行打印一次。标尺中的数字对应其最左侧字符位置的值。落在不同范围内的功率值以相同前景色和背景色的不同颜色字符打印，因此可以复制并粘贴此命令的终端输出。

- *value* -- 选择输出中绘制的值。'interference' 是特殊的，因为它显示检测到的干扰源（受'classify-samples'参数影响）而非功率读数，并且不能设置为可听。
- *interval* -- 频谱图行打印的间隔。
- *duration* -- 在指定时间后终止命令。默认为无限期。
- *buckets* -- 频谱图每行显示多少个值。此值受终端列数限制。如果使用'audible'，减少此值很有用。
- *average-samples* -- 在每个频率上获取的4微秒频谱快照数量，并计算它们的平均和最大能量。（默认10）。
- *classify-samples* -- 在每个频率上获取并由干扰分类算法处理的频谱快照数量。通常，更多样本提供更多机会发现某些类型的干扰（默认50）。
- *range* --
  - 2.4ghz - 扫描整个2.4ghz频段；
  - 5ghz - 扫描整个5ghz频段；
  - current-channel - 仅扫描当前信道（20或40 MHz宽）；
  - range - 扫描特定范围。

- *audible=yes* -- 每行打印时播放声音。行与行之间有短暂的静音。每行从左到右播放，较高频率对应频谱图中较高的值。

### 频谱扫描

![](https://manual.mikrotik.com/docs/wireless/abgn/img/spectral-scan-02.webp)

```ros
 /interface/wireless/spectral-scan <无线接口名称> 
```

持续监控频谱数据。此命令使用与'spectral-history'相同的数据源，因此共享许多参数。

每行显示一个频谱图桶 -- 频率、平均功率的数值以及字符图形条。条形图以':'字符显示平均功率值，以'.'字符显示平均峰值保持。最大值显示为单个浮动的':'字符。

- *show-interference* -- 添加一列显示检测到的干扰源；

可能分类的干扰类型：

- Bluetooth-headset
- Bluetooth-stereo
- cordless-phone
- microwave-oven
- CWA
- video-bridge
- wifi

## The Dude

The Dude 是 MikroTik 提供的免费网络监控和管理程序。您可以 [在此处下载](http://www.mikrotik.com/thedude.php)。

The Dude 具有内置功能，可以从任何带有受支持无线网卡的 RouterOS 设备运行图形化频谱扫描。只需在 Dude 地图中选择该设备，右键单击并选择 工具 -> 频谱扫描。

![](https://manual.mikrotik.com/docs/wireless/abgn/img/spectral-scan-03.webp)

这将打开频谱扫描 GUI，其中包含各种选项和不同的视图模式：

![](https://manual.mikrotik.com/docs/wireless/abgn/img/spectral-scan-04.webp)