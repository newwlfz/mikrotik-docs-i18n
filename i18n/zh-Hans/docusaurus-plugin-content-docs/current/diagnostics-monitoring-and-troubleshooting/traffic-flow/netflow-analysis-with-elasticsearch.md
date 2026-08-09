# 使用 Elasticsearch 进行 NetFlow 分析

> 本指南介绍如何在 MikroTik RouterOS 上通过配置从 RouterOS 设备向 Elasticsearch 服务器收集数据，实现基于 Elasticsearch 的 NetFlow 分析，包括 Kibana 集成和 Fleet Server 部署，以实现高效的 NetFlow 数据处理与可视化。

# 使用 Elasticsearch 进行 NetFlow 分析

Elasticsearch 是一种流行的 NoSQL 数据库，可用于存储各种数据，包括 NetFlow 日志。结合 Kibana，您可以创建一个强大的工具来分析来自 RouterOS 设备的 NetFlow 数据。本指南将依赖 Elasticsearch 集成，并且需要您拥有一个可正常工作的 Elasticsearch 环境才能运行。本指南不涵盖 Elasticsearch 和 Kibana 的安装说明，但会涵盖设置 NetFlow 日志收集和分析的相关步骤。

Elasticsearch 支持多种配置方式，但为了本指南的目的，我们将采用以下架构：

- RouterOS（10.0.0.1）设备将 NetFlow 数据发送到运行 [NetFlow 集成](https://www.elastic.co/docs/current/integrations/netflow) 的服务器（10.0.0.2）。
- 运行 NetFlow 集成的服务器（10.0.0.2）接收 NetFlow 数据，处理数据并将其发送到 [Fleet Server](https://www.elastic.co/guide/en/fleet/current/fleet-server.html)（10.0.0.3）。
- Fleet Server（10.0.0.3）将数据存储在 [Elasticsearch](https://www.elastic.co/elasticsearch)（10.0.0.4）中。
- [Kibana](https://www.elastic.co/kibana)（10.0.0.5）从 Elasticsearch（10.0.0.4）检索数据，进行分析并允许您搜索数据。

![](https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/traffic-flow/img/netflow-analysis-with-elasticsearch-01.webp)

:::info
本指南不会使用 [Logstash](https://www.elastic.co/logstash) 作为 NetFlow 数据分析的一部分；它已被 Fleet Server 取代。

**重要提示：** 可以将 Elasticsearch、Kibana、Fleet Server 和 NetFlow Records 集成安装在同一台设备上。
:::

## 前提条件

- [设置 Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html)  
  :::info
  Elasticsearch 广泛支持多种平台。建议搭建 Elasticsearch 节点集群。
  :::
- [设置 Kibana](https://www.elastic.co/guide/en/kibana/current/setup.html)  
  :::info
  Kibana 可以安装在您安装 Elasticsearch 的同一台设备上，但出于性能考虑，也可以安装在单独的设备上。虽然可以在没有 Kibana 的情况下分析 NetFlow 数据，但这需要您自行编写 API 请求。Kibana 非常易于使用，并且功能丰富。
  :::
- [设置 Fleet Server](https://www.elastic.co/guide/en/fleet/current/add-fleet-server-on-prem.html)  
  :::info
  可以将 Fleet Server 设置在您安装 Elasticsearch 和/或 Kibana 的同一台设备上。建议将 Fleet Server 安装在单独的设备上。有关硬件和拓扑要求的建议，请参阅 Elasticsearch 手册。
  :::

## 设置

设置说明分为两部分：Elastic（与 Elasticsearch、Kibana 和 Fleet Server 相关的配置）和 RouterOS（与您的 RouterOS 设备相关的配置）。

### Elastic

:::warning
某些步骤可能会随时间变化，请参阅 Elastic 手册以获取最新的步骤。
:::

1. [登录您的 Kibana](https://www.elastic.co/guide/en/kibana/current/access.html)
2. 打开主菜单下的 [Fleet](https://www.elastic.co/guide/en/kibana/current/fleet.html) 部分
3. 打开 "[Agent policies](https://www.elastic.co/guide/en/fleet/current/agent-policy.html)" 部分
4. 按下 "Create agent policy" 按钮以[创建新的 Agent Policy](https://www.elastic.co/guide/en/fleet/current/agent-policy.html#create-a-policy)
5. 为策略命名，例如 "NetFlow policy"，根据需要调整高级设置，然后创建策略
6. 点击您新建的策略名称以打开它
7. 按下 "[Add integration](https://www.elastic.co/guide/en/fleet/current/agent-policy.html#add-integration)"
8. 搜索 "[NetFlow Records](https://www.elastic.co/docs/current/integrations/netflow)" 并按下 "Add NetFlow Records"
9. 调整配置，确保：  
   - 将 "UDP host to listen on" 设置为将要运行 NetFlow Records 集成的服务器 IP 地址，在本示例中应为 "10.0.0.2"
10. 保存集成
11. 按下 "[Add Elastic Agent to your host](https://www.elastic.co/guide/en/fleet/current/elastic-agent-installation.html)" 按钮
12. 按照说明将 Elastic Agent 添加到您的主机  
    :::info
    Elastic 官方手册建议将 Elastic Agent 安装为 Fleet 托管。建议遵循该建议，因为当代理由 Fleet 托管时，管理起来更容易。
    :::
13. 确保您已在主机上以及从 RouterOS 设备（10.0.0.1）到主机的路径中开放 NetFlow 端口。默认目标端口为 2055/UDP。
14. 您的 Elastic Agent 现已准备好接收 NetFlow 数据！

### RouterOS

1. （可选）创建 [Interface list](../../system-information-and-utilities/interface-lists.md)（例如 "NetFlow\_interfaces"）并添加需要进行 NetFlow 数据分析的接口。  

   ```routeros
   /interface/list
   add name=NetFlow_interfaces
   /interface/list/member
   add interface=VLAN3000 list=NetFlow_interfaces
   ```

2. 配置 [Traffic-flow](./index.md) 以将 NetFlow 数据发送到您的 Elastic Agent（10.0.0.2）。  

   ```routeros
   /ip/traffic-flow
   set enabled=yes interfaces=NetFlow_interfaces
   /ip/traffic-flow/target
   add dst-address=10.0.0.2
   ```

3. 您现在应该开始看到 NetFlow 数据被接收！
4. 继续本指南以开始使用 Kibana。

## 使用 Kibana

:::warning
某些步骤可能会随时间变化，请参阅 Elastic 手册以获取最新的步骤。
:::

NetFlow Records 集成提供了一些有用的资源，可用于分析 NetFlow 数据。在继续之前，请确保您已[安装这些资源](https://www.elastic.co/guide/en/fleet/7.17/install-uninstall-integration-assets.html)。以下部分将为您提供一些查看 NetFlow 数据的基本方法。

1. [登录您的 Kibana](https://www.elastic.co/guide/en/kibana/current/access.html)
2. 打开主菜单中的 "[Dashboards](https://www.elastic.co/kibana/kibana-dashboard)" 菜单
3. 搜索 Dashboards 并找到 "NetFlow"

您现在应该会看到多个 NetFlow Dashboard。例如，尝试打开 "[Logs Netflow] Overview"。如果您的 NetFlow 数据被正确接收，您现在应该会看到汇总您流量的图表。

另一个有用的 Dashboard 是 "[Logs Netflow] Flow records"，它显示精确的 NetFlow 记录。一个非常有用的功能是过滤选项（顶部的 + 按钮），它允许您向 NetFlow 数据添加过滤器，例如，您可以过滤记录以仅显示单个 IP 地址：

![](https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/traffic-flow/img/netflow-analysis-with-elasticsearch-02.webp)

还有其他选项，例如搜索特定时间范围。您应该进一步阅读 [Discover](https://www.elastic.co/guide/en/kibana/current/discover-get-started.html#find-the-data-you-want-to-use) 以更好地了解其功能。

作为快速参考，以下是您最可能用于搜索 NetFlow 数据的字段：

- source.ip
- source.port
- destination.ip
- destination.port
- network.transport

如果您想检查单条记录，建议使用 [Discover](https://www.elastic.co/guide/en/kibana/current/discover-get-started.html#find-the-data-you-want-to-use) 视图。NetFlow 数据可以在 "data\_stream.dataset: netflow.log" 中找到。

## 日志保留

根据当地法律，您可能需要将 NetFlow 数据存储指定的一段时间。请注意，繁忙的网络可能会产生大量 NetFlow 数据，甚至每天达到 TB 级别。您很可能需要调整 [Lifecycle Policy](https://www.elastic.co/guide/en/elasticsearch/reference/current/set-up-lifecycle-policy.html)。默认情况下，NetFlow 数据应归入 "logs" 策略。如果您有多个 Elasticsearch 节点，可以利用 "[phases](https://www.elastic.co/guide/en/elasticsearch/reference/current/ilm-index-lifecycle.html)"，这允许您将数据存储在不同类型的存储介质上，但如果您只有一个 Elasticsearch 节点，您的选择将受到限制，您很可能需要[删除](https://www.elastic.co/guide/en/elasticsearch/reference/current/ilm-delete.html)旧数据。例如，如果您想在 6 个月后删除数据，您可以简单地将 ILM 策略更改为在 6 个月后删除数据，或使用此 API 请求：

```json
PUT _ilm/policy/logs
{
  "policy": {
    "phases": {
      "hot": {
        "min_age": "0ms",
        "actions": {
          "rollover": {
            "max_age": "30d",
            "max_primary_shard_size": "50gb"
          },
          "set_priority": {
            "priority": 101
          }
        }
      },
      "delete": {
        "min_age": "180d",
        "actions": {
          "delete": {
            "delete_searchable_snapshot": true
          }
        }
      }
    }
  }
}
```

:::danger
如果您更改 "logs" 策略，这将应用于您**所有**的日志，而不仅仅是 NetFlow 数据。如果您需要为其他日志设置不同的保留期，那么最好创建一个新的 ILM 策略，并指定 NetFlow 集成使用新创建的 ILM 策略。
:::

### 使用不同的 ILM 策略

如果您希望 NetFlow 数据具有不同的保留期，则需要执行以下步骤：

1. 创建一个新的 ILM 策略，为其命名并设置所需的删除阶段周期，或使用此 API 请求：  

   ```json
   PUT _ilm/policy/netflow-logs
   {
     "policy": {
       "phases": {
         "hot": {
           "min_age": "0ms",
           "actions": {
             "rollover": {
               "max_age": "30d",
               "max_primary_shard_size": "50gb"
             },
             "set_priority": {
               "priority": 101
             }
           }
         },
         "delete": {
           "min_age": "1000d",
           "actions": {
             "delete": {
               "delete_searchable_snapshot": true
             }
           }
         }
       }
     }
   }
   ```

2. 转到 Kibana，打开 "Stack Management"，然后进入 "Index Management"，再进入 "Component Templates"。
3. 搜索 "logs-netflow.log@custom"，打开并编辑它。
4. 转到 "Index settings" 部分。
5. 粘贴以下内容：  

   ```json
   {
     "index": {
       "lifecycle": {
         "name": "netflow-logs"
       }
     }
   }
   ```

6. 按下 "Next"，然后按下 "Save component template"。