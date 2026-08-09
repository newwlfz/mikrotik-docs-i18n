# PCQ 示例

> 每连接队列（PCQ）是 RouterOS 中一种用于在用户间均衡带宽的排队方法，以下示例展示了如何使用队列树和简单队列设置下载/上传限制。

# PCQ 示例

每连接队列（PCQ）是一种排队规则，可用于动态均衡或整形多个用户的流量，且管理开销极小。PCQ 场景可分为三大类：为一定数量的用户提供相等带宽、在用户间平均分配特定带宽，以及在未知带宽条件下在用户间平均分配带宽。

## 为一定数量的用户提供相等带宽

PCQ 类型可通过队列树和简单队列来均衡带宽[并设置最大限制]给一定数量的用户。我们将设置 64kbps 的下载限制和 32kbps 的上传限制。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/queues/img/pcq-example-01.webp)

### 步骤 1：在队列类型中添加 PCQ

添加两个新条目——一个用于下载，一个用于上传。`dst-address` 是用户下载流量的分类器，`src-address` 用于上传流量：

```ros
/queue/type/add name="PCQ_download" kind=pcq pcq-rate=64000 pcq-classifier=dst-address
/queue/type/add name="PCQ_upload" kind=pcq pcq-rate=32000 pcq-classifier=src-address
 
```

### 步骤 2：部署 PCQ

#### 队列树选项

使用 packet-marks 标记所有数据包为上传/下载：（假设 ether1-WAN 是连接到互联网的公共接口，ether2-LAN 是客户端连接的本地接口）：

```ros
/ip/firewall/mangle/add chain=prerouting action=mark-packet \
   in-interface=ether2-LAN new-packet-mark=client_upload
/ip/firewall/mangle/add chain=prerouting action=mark-packet \
   in-interface=ether1-WAN new-packet-mark=client_download
```

然后，需要两条队列规则，一条用于下载，一条用于上传：

```ros
/queue/tree/add parent=global queue=PCQ_download packet-mark=client_download
/queue/tree/add parent=global queue=PCQ_upload packet-mark=client_upload
```

#### 简单队列选项

或者，您也可以通过一条命令完成此操作，如下所示：

```ros
/queue/simple/add target=192.168.0.0/24 queue=PCQ_upload/PCQ_download
```