# 使用 Elasticsearch 进行 CEF 日志分析

> 本指南介绍如何使用 Elasticsearch、Kibana 和 Fleet Server 配置 MikroTik RouterOS 设备的 CEF 日志收集与分析。内容涵盖 Elastic 和 RouterOS 组件的先决条件、设置步骤，包括代理策略创建和 CEF 集成配置。

# 使用 Elasticsearch 进行 CEF 日志分析

## 简介

Elasticsearch 是一种流行的 NoSQL 数据库，可用于存储包括 CEF 日志在内的各种数据。结合 Kibana，您可以创建一个强大的工具来分析来自 RouterOS 设备的 CEF 日志。本指南将依赖 Elasticsearch 集成，并且要使其正常工作，您需要有一个可用的 Elasticsearch 环境。本指南不涵盖 Elasticsearch 和 Kibana 的设置说明，但会涵盖设置 CEF 日志收集和分析的相关步骤。

Elasticsearch 可以配置多种方案，但为了本指南的目的，我们将采用以下原则：

- RouterOS（10.0.0.1）设备将 CEF 日志发送到运行 [CEF 集成](https://www.elastic.co/docs/reference/integrations/cef) 的服务器（10.0.0.2）。
- 运行 CEF 集成的服务器（10.0.0.2）接收 CEF 日志，处理数据并将其发送到 [Fleet Server](https://www.elastic.co/guide/en/fleet/current/fleet-server.html)（10.0.0.3）。
- Fleet Server（10.0.0.3）将数据存储在 [Elasticsearch](https://www.elastic.co/elasticsearch)（10.0.0.4）中。
- [Kibana](https://www.elastic.co/kibana)（10.0.0.5）从 Elasticsearch（10.0.0.4）检索数据，进行分析并允许您搜索数据。

:::info
本指南不会使用 [Logstash](https://www.elastic.co/logstash) 作为分析 CEF 日志的一部分；它已被 Fleet Server 取代。

:::

:::info
可以在同一设备上安装 Elasticsearch、Kibana、Fleet Server 和 CEF 日志集成。

:::

## 先决条件

- [设置 Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html)。  
  :::info
  Elasticsearch 在许多平台上都得到广泛支持。建议设置一个 Elasticsearch 节点集群。
  :::
- [设置 Kibana](https://www.elastic.co/guide/en/kibana/current/setup.html)。  
  :::info
  Kibana 可以安装在您安装 Elasticsearch 的同一设备上，但出于性能考虑，也可以安装在单独的设备上。虽然可以在没有 Kibana 的情况下分析 CEF 日志，但这需要编写自己的 API 请求。Kibana 非常易于使用，并且具有广泛的功能。
  :::
- [设置 Fleet Server](https://www.elastic.co/guide/en/fleet/current/add-fleet-server-on-prem.html)。  
  :::info
  可以在您安装 Elasticsearch 和/或 Kibana 的同一设备上设置 Fleet Server。建议将 Fleet Server 安装在单独的设备上。有关硬件和拓扑要求的建议，请参阅 Elasticsearch 手册。
  :::

## 设置

设置说明分为两部分：Elastic（关于 Elasticsearch、Kibana 和 Fleet Server 的配置）和 RouterOS（与您的 RouterOS 设备相关的配置）。

### Elastic

:::warning
某些步骤可能会随时间变化，请参阅 Elastic 手册以获取最新的步骤。

:::

- [登录您的 Kibana](https://www.elastic.co/guide/en/kibana/current/access.html)。
- 打开主菜单下的 [Fleet](https://www.elastic.co/guide/en/kibana/current/fleet.html) 部分。
- 打开 "[Agent policies](https://www.elastic.co/guide/en/fleet/current/agent-policy.html)" 部分。
- 按下 "Create agent policy" 按钮以 [创建新的 Agent Policy](https://www.elastic.co/guide/en/fleet/current/agent-policy.html#create-a-policy)。
- 为策略命名，例如 "CEF policy"，根据需要调整高级设置，然后创建策略。或者您可以使用以下 API 请求：  

  ```routeros
  POST kbn:/api/fleet/agent_policies
  {
    "name": "CEF policy",
    "description": "",
    "namespace": "default",
    "monitoring_enabled": [
      "logs",
      "metrics"
    ],
    "inactivity_timeout": 1209600,
    "is_protected": false
  }
  ```

- 点击策略名称打开您新创建的策略。
- 按下 "[Add integration](https://www.elastic.co/guide/en/fleet/current/agent-policy.html#add-integration)" 按钮。
- 搜索 "[Common Event Format (CEF)](https://www.elastic.co/docs/reference/integrations/cef)" 并按下 "Add Common Event Format (CEF)"。
- 调整配置，确保：  
  - 在 "Collect CEF application logs (input: udp)" 部分下，将 "Syslog Host" 设置为 "0.0.0.0"。  
  - 在 "Collect CEF application logs (input: tcp)" 部分下，将 "Syslog Host" 设置为 "0.0.0.0"。
- 保存集成。
- 按下 "[Add Elastic Agent to your host](https://www.elastic.co/guide/en/fleet/current/elastic-agent-installation.html)" 按钮。
- 按照说明将 Elastic Agent 添加到您的主机。  
  :::info
  Elastic 官方手册建议将 Elastic Agent 安装为 Fleet 管理。建议遵循该建议，因为当代理由 Fleet 管理时，管理起来更容易。
  :::
- 转到主菜单上的 "Stack Management"，然后打开 "[Ingest Pipelines](https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest.html)"。
- 通过按下 "[Create pipeline](https://www.elastic.co/guide/en/fleet/current/data-streams-pipeline-tutorial.html#data-streams-pipeline-one)" 然后选择 "New pipeline" 来创建新的 Ingest Pipeline。
- 将 "Name" 设置为 "logs-cef.log@custom"。
- 按下 "Import processors" 并粘贴以下处理器：  

  ```routeros
  {
  	"processors": [
  		{
  			"set": {
  			"ignore_empty_value": true,
  			"field": "host.name",
  			"copy_from": "cef.extensions.deviceHostName"
  			}
  		},
  		{
  			"set": {
  			"ignore_empty_value": true,
  			"field": "host.ip",
  			"copy_from": "cef.extensions.deviceAddress"
  			}
  		}
  	]
  }
  ```

  :::info
  "logs-cef.log@custom" 管道不是必需的，但当您将 Elasticsearch 用于其他类型的日志时，它使搜索日志更容易。
  :::
- 按下 "Save pipeline"。
- 确保您已在主机上以及从 RouterOS 设备（10.0.0.1）到主机的路径中打开 9003/UDP 端口。
- 您的 Elastic Agent 现在已准备好接收 CEF 日志。

### RouterOS

1. 在您的 RouterOS 设备（10.0.0.1）上配置 [Logging action](./index.md#actions) 设置：  

   ```routeros
   /system/logging/action
   add cef-event-delimiter="\n" name=syslog remote=10.0.0.2 remote-log-format=cef remote-port=9003 syslog-facility=syslog syslog-time-format=iso8601 target=remote
   /system/logging
   add action=syslog topics=info
   add action=syslog topics=error
   add action=syslog topics=warning
   add action=syslog topics=critical
   ```

2. 添加您希望从 RouterOS 设备（10.0.0.1）接收的 [Topics](index.md#topics-used-by-various-routeros-facilities)，例如：  

   ```routeros
   /system/logging
   add action=syslog topics=info
   add action=syslog topics=error
   add action=syslog topics=critical
   add action=syslog topics=warning
   add action=syslog topics=bridge,stp
   ```

3. 您现在应该开始看到 CEF 日志被接收。
4. 继续本指南以开始使用 Kibana。

### 使用 Kibana

Kibana 允许您搜索接收到的 CEF 日志。要查看接收到的日志，请执行以下操作：

1. [登录您的 Kibana](https://www.elastic.co/guide/en/kibana/current/access.html)。
2. 从主菜单打开 "Discover"。
3. [添加过滤器](https://www.elastic.co/guide/en/kibana/current/discover-get-started.html#explore-fields-in-your-data)，并使用以下参数：  

   ```routeros
   Select a field: data_stream.dataset
   Select operator: IS
   Select a value: cef.log
   ```

4. 为简单起见，我们建议在 Discover 菜单中 [搜索字段](https://www.elastic.co/guide/en/kibana/current/discover-get-started.html#explore-fields-in-your-data) 并搜索 "message"，然后将该字段添加到视图中。
5. 我们还建议搜索 "host.name" 字段并将其添加到视图中。
6. 考虑 [保存搜索](https://www.elastic.co/guide/en/kibana/current/save-open-search.html#_save_a_search) 以便日后更方便地访问。
7. 完成！