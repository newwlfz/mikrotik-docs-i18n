# 使用 Elasticsearch 进行 Syslog 日志收集与分析

> 本指南介绍如何配置使用 Elasticsearch、Kibana 和 Fleet Server 收集和分析 MikroTik RouterOS 设备的 Syslog 数据。涵盖 Elastic 和 RouterOS 组件的前置要求、设置步骤，包括代理策略创建和自定义 UDP 日志集成配置。

# 使用 Elasticsearch 进行 Syslog 日志收集与分析

## 引言

Elasticsearch 是一种流行的 NoSQL 数据库，可用于存储各种数据，包括 Syslog 数据。结合 Kibana，您可以创建强大的工具来分析来自 RouterOS 设备的 Syslog 数据。本指南将依赖 Elasticsearch 集成，为此您需要有一个可用的 Elasticsearch 环境。本指南不涵盖 Elasticsearch 和 Kibana 的安装说明，但会涵盖设置 Syslog 数据收集和分析的相关步骤。

Elasticsearch 有许多可能的配置方式，但为了本指南的目的，我们将采用以下原则：

- RouterOS 设备（10.0.0.1）将 Syslog 数据发送到运行 [自定义 UDP 日志](https://www.elastic.co/docs/current/integrations/udp) 的服务器（10.0.0.2）。
- 运行自定义 UDP 日志集成的服务器（10.0.0.2）接收 Syslog 数据，处理数据并将其发送到 [Fleet Server](https://www.elastic.co/guide/en/fleet/current/fleet-server.html)（10.0.0.3）。
- Fleet Server（10.0.0.3）将数据存储在 [Elasticsearch](https://www.elastic.co/elasticsearch)（10.0.0.4）中。
- [Kibana](https://www.elastic.co/kibana)（10.0.0.5）从 Elasticsearch（10.0.0.4）检索数据，进行分析并允许您搜索数据。

:::info
本指南不会使用 [Logstash](https://www.elastic.co/logstash) 作为分析 Syslog 数据的一部分；它已被 Fleet Server 取代。

:::

:::info
可以将 Elasticsearch、Kibana、Fleet Server 和自定义 UDP 日志集成安装在同一台设备上。

:::

## 前置要求

- [设置 Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html)。  
  :::info
  Elasticsearch 在众多平台上得到广泛支持。建议设置 Elasticsearch 节点集群。
  :::
- [设置 Kibana](https://www.elastic.co/guide/en/kibana/current/setup.html)。  
  :::info
  Kibana 可以安装在您安装 Elasticsearch 的同一台设备上，但出于性能考虑，也可以安装在单独的设备上。虽然可以在没有 Kibana 的情况下分析 Syslog 数据，但这需要编写自己的 API 请求，而 Kibana 非常易于使用且功能丰富。
  :::
- [设置 Fleet Server](https://www.elastic.co/guide/en/fleet/current/add-fleet-server-on-prem.html)。  
  :::info
  可以在您安装 Elasticsearch 和/或 Kibana 的同一台设备上设置 Fleet Server。建议将 Fleet Server 安装在不同的设备上。有关硬件和拓扑要求的建议，请参阅 Elasticsearch 手册。
  :::

## 设置

设置说明分为两部分：Elastic（关于 Elasticsearch、Kibana 和 Fleet Server 的配置）和 RouterOS（与您的 RouterOS 设备相关的配置）。

### Elastic

:::warning
某些步骤可能会随时间变化。请参阅 Elastic 手册以获取最新的步骤。

:::

1. [登录您的 Kibana](https://www.elastic.co/guide/en/kibana/current/access.html)。
2. 在主菜单中打开 [Fleet](https://www.elastic.co/guide/en/kibana/current/fleet.html) 部分。
3. 打开“[代理策略](https://www.elastic.co/guide/en/fleet/current/agent-policy.html)”部分。
4. 按“创建代理策略”按钮以[创建新的代理策略](https://www.elastic.co/guide/en/fleet/current/agent-policy.html#create-a-policy)。
5. 为策略命名，例如“Syslog 策略”，根据需要调整高级设置，然后创建策略。或者您可以使用以下 API 请求：  

   ```routeros
   POST kbn:/api/fleet/agent_policies
   {
     "name": "Syslog policy",
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

6. 通过点击策略名称打开您新创建的策略。
7. 按“[添加集成](https://www.elastic.co/guide/en/fleet/current/agent-policy.html#add-integration)”。
8. 搜索“[自定义 UDP 日志](https://www.elastic.co/docs/current/integrations/udp)”并按“添加自定义 UDP 日志”。
9. 调整配置，并确保：  
   - 将“监听地址”设置为将要运行自定义 UDP 日志集成的服务器的 IP 地址，在本示例中地址应为“10.0.0.2”。  
   - 将“监听端口”设置为“5514”。  
   - 将“数据集名称”设置为“routeros”。  
   - 将“摄取管道”设置为“logs-routeros@custom”。  
   - 将“Syslog 解析”设置为“是”。
10. 保存集成。
11. 按“[将 Elastic Agent 添加到您的主机](https://www.elastic.co/guide/en/fleet/current/elastic-agent-installation.html)”按钮。
12. 按照说明将 Elastic Agent 添加到您的主机。  
    :::info
    官方 Elastic 手册建议将 Elastic Agent 安装为 Fleet 管理。建议遵循该建议，因为当代理由 Fleet 管理时更容易管理。
    :::
13. 在主菜单中转到“Stack Management”，然后打开“[摄取管道](https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest.html)”。
14. 按“[创建管道](https://www.elastic.co/guide/en/fleet/current/data-streams-pipeline-tutorial.html#data-streams-pipeline-one)”然后“新建管道”来创建新的摄取管道。
15. 将“名称”设置为“logs-routeros@custom”。
16. 按“导入处理器”并粘贴以下处理器：  

    ```routeros
    {
    	"processors": [
    		{
    			"grok": {
    			"field": "message",
    			"patterns": [
    				"^first L2TP UDP packet received from %{IP:source.ip}$",
    				"^login failure for user %{USERNAME:user.name} from %{IP:source.ip} via %{DATA:service.name}$",
    				"^%{USERNAME:user.name} logged in, %{IP:client.ip} from %{IP:source.ip}$",
    				"^dhcp alert on %{DATA}: discovered unknown dhcp server, mac %{MAC:source.mac}, ip %{IP:source.ip}$",
    				"in:%{DATA} out:%{DATA}, ?(connection-state:%{DATA},|)?(src-mac %{MAC:source.mac},|) proto %{DATA:network.transport} \\(%{DATA}\\), %{IP:source.ip}:?(%{INT:source.port}|)->%{IP:destination.ip}:?(%{INT:destination.port}|), len %{INT:network.bytes}$",
    				"in:%{DATA} out:%{DATA}, ?(connection-state:%{DATA},|)?(src-mac %{MAC:source.mac},|) proto %{DATA:network.transport}, %{IP:source.ip}:?(%{INT:source.port}|)->%{IP:destination.ip}:?(%{INT:destination.port}|), len %{INT:network.bytes}$",
    				"^%{DATA:network.name} (deassigned|assigned) %{IP:client.ip} for %{MAC:client.mac} %{DATA}$",
    				"^%{DATA:user.name} logged out, %{INT:event.duration} %{INT} %{INT} %{INT} %{INT} from %{IP:client.ip}$",
    				"^user %{DATA:user.name} logged out from %{IP:source.ip} via %{DATA:service.name}$",
    				"^user %{DATA:user.name} logged in from %{IP:source.ip} via %{DATA:service.name}$",
    				"^%{DATA:network.name} client %{MAC:client.mac} declines IP address %{IP:client.ip}$",
    				"^%{DATA:network.name} link up \\(speed %{DATA}\\)$",
    				"^%{DATA:network.name} link down$",
    				"^user %{DATA:user.name} authentication failed$",
    				"^%{DATA:network.name} fcs error on link$",
    				"^phase1 negotiation failed due to time up %{IP:source.ip}\\[%{INT:source.port}\\]<=>%{IP:destination.ip}\\[%{INT:destination.port}\\] %{DATA}:%{DATA}$",
    				"^%{DATA:network.name} (learning|forwarding)$",
    				"^user %{DATA:user.name} is already active$",
    				"^%{GREEDYDATA}$"
    			]
    			}
    		},
    		{
    			"lowercase": {
    			"field": "network.transport",
    			"ignore_missing": true
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "event.category",
    			"description": "Enrich logon events",
    			"allow_duplicates": false,
    			"value": [
    				"authentication"
    			],
    			"if": "ctx.message =~ /(login failure for user|logged in from|logged in,)/"
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "event.outcome",
    			"description": "Enrich successful login events",
    			"allow_duplicates": false,
    			"value": [
    				"success"
    			],
    			"if": "ctx.message =~ /(logged in from|logged in,)/"
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "event.outcome",
    			"description": "Enrich failed login events",
    			"allow_duplicates": false,
    			"value": [
    				"failure"
    			],
    			"if": "ctx.message =~ /(login failure for user)/"
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "event.category",
    			"description": "Enrich network events",
    			"allow_duplicates": false,
    			"value": [
    				"network"
    			],
    			"if": "ctx.message =~ /( fcs error on link| link down| link up)/"
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "event.outcome",
    			"description": "Enrich network failures",
    			"allow_duplicates": false,
    			"value": [
    				"failure"
    			],
    			"if": "ctx.message =~ /( fcs error on link)/"
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "event.category",
    			"allow_duplicates": false,
    			"value": [
    				"session"
    			],
    			"if": "ctx.message =~ /(logged out)/"
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "event.category",
    			"allow_duplicates": false,
    			"value": [
    				"threat"
    			],
    			"if": "ctx.message =~ /(from address that has not seen before)/"
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "service.name",
    			"value": [
    				"l2tp"
    			],
    			"if": "ctx.message =~ /(^L2TP\\/IPsec VPN)/"
    			}
    		},
    		{
    			"geoip": {
    			"ignore_failure": true,
    			"ignore_missing": true,
    			"field": "source.ip",
    			"target_field": "source.geo"
    			}
    		},
    		{
    			"geoip": {
    			"ignore_failure": true,
    			"ignore_missing": true,
    			"field": "destination.ip",
    			"target_field": "destination.geo"
    			}
    		},
    		{
    			"geoip": {
    			"ignore_failure": true,
    			"ignore_missing": true,
    			"field": "client.ip",
    			"target_field": "client.geo"
    			}
    		}
    	]
    }
    ```

17. 按“保存管道”。
18. 在主菜单中转到“Stack Management”，然后选择“索引管理”，再选择“组件模板”。
19. 按“创建组件模板”创建新模板。
20. 将“名称”设置为“logs-routeros@custom”。
21. 在“索引设置”部分下，粘贴以下内容：  

    ```routeros
    {
      "index": {
        "lifecycle": {
          "name": "logs"
        },
        "default_pipeline": "logs-routeros@custom"
      }
    }
    ```

    :::info
    将 ILM 策略更改为您需要的策略名称。“logs”策略是可能用于其他日志的默认策略。
    :::
22. 在“映射”部分下，按“加载 JSON”并粘贴以下内容：  

    ```routeros
    {
      "dynamic_templates": [],
      "properties": {
        "service": {
          "type": "object",
          "properties": {
            "name": {
              "type": "keyword"
            }
          }
        },
        "destination": {
          "type": "object",
          "properties": {
            "port": {
              "type": "long"
            },
            "ip": {
              "type": "ip"
            }
          }
        },
        "host": {
          "type": "object",
          "properties": {
            "ip": {
              "type": "ip"
            }
          }
        },
        "client": {
          "type": "object",
          "properties": {
            "ip": {
              "type": "ip"
            },
            "mac": {
              "type": "keyword"
            }
          }
        },
        "source": {
          "type": "object",
          "properties": {
            "geo": {
              "type": "object",
              "properties": {
                "continent_name": {
                  "ignore_above": 1024,
                  "type": "keyword"
                },
                "region_iso_code": {
                  "ignore_above": 1024,
                  "type": "keyword"
                },
                "city_name": {
                  "ignore_above": 1024,
                  "type": "keyword"
                },
                "country_iso_code": {
                  "ignore_above": 1024,
                  "type": "keyword"
                },
                "country_name": {
                  "ignore_above": 1024,
                  "type": "keyword"
                },
                "location": {
                  "type": "geo_point"
                },
                "region_name": {
                  "ignore_above": 1024,
                  "type": "keyword"
                }
              }
            },
            "as": {
              "type": "object",
              "properties": {
                "number": {
                  "type": "long"
                },
                "organization": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "ignore_above": 1024,
                      "type": "keyword",
                      "fields": {
                        "text": {
                          "type": "match_only_text"
                        }
                      }
                    }
                  }
                }
              }
            },
            "address": {
              "ignore_above": 1024,
              "type": "keyword"
            },
            "port": {
              "type": "long"
            },
            "domain": {
              "ignore_above": 1024,
              "type": "keyword"
            },
            "ip": {
              "type": "ip"
            },
            "mac": {
              "type": "keyword"
            }
          }
        },
        "event": {
          "type": "object",
          "properties": {
            "duration": {
              "type": "long"
            },
            "category": {
              "type": "keyword"
            },
            "outcome": {
              "type": "keyword"
            }
          }
        },
        "message": {
          "type": "match_only_text"
        },
        "user": {
          "type": "object",
          "properties": {
            "name": {
              "type": "keyword"
            }
          }
        },
        "network": {
          "type": "object",
          "properties": {
            "bytes": {
              "type": "long"
            },
            "name": {
              "type": "keyword"
            },
            "transport": {
              "type": "keyword"
            }
          }
        },
        "tags": {
          "ignore_above": 1024,
          "type": "keyword"
        }
      }
    }
    ```

23. 按“下一步”，然后按“保存组件模板”。  
    :::warning
    如果存在同名的组件模板，请改为编辑现有模板。
    :::
24. 在主菜单中转到“Stack Management”，然后选择“索引管理”，再选择“索引模板”。
25. 按“创建模板”创建新模板。
26. 将“名称”设置为“logs-routeros”。
27. 将“索引模式”设置为“logs-routeros-\*”。
28. 在“组件模板”部分下，将以下模板添加到您的新索引模板中：  

    ```routeros
    logs@settings
    logs-routeros@custom
    ecs@mappings
    ```

29. 按“下一步”，然后按“保存模板”。
30. 确保您已在主机上以及从 RouterOS 设备（10.0.0.1）到主机的路径中打开了 5514/UDP 端口。
31. 您的 Elastic Agent 现在已准备好接收 Syslog 数据！

### RouterOS

1. 在您的 RouterOS 设备（10.0.0.1）上配置[日志操作](./index.md#actions)设置：  

   ```routeros
   /system/logging/action
   set [find where name="remote"] remote-log-format=syslog remote=10.0.0.2 remote-port=5514 syslog-facility=syslog
   ```

2. 添加您希望从 RouterOS 设备（10.0.0.1）接收的[主题](index.md#topics-used-by-various-routeros-facilities)，例如：  

   ```routeros
   /system/logging
   add action=remote topics=info
   add action=remote topics=error
   add action=remote topics=critical
   add action=remote topics=warning
   add action=remote topics=bridge,stp
   ```

3. 您现在应该开始看到 Syslog 数据被摄取。
4. 继续本指南以开始使用 Kibana。

## 使用 Kibana

Kibana 允许您搜索已摄取的 Syslog 数据。要查看已摄取的日志，请执行以下操作：

1. [登录您的 Kibana](https://www.elastic.co/guide/en/kibana/current/access.html)。
2. 从主菜单中打开“Discover”。
3. [添加过滤器](https://www.elastic.co/guide/en/kibana/current/discover-get-started.html#explore-fields-in-your-data)，并使用以下参数：  

   ```routeros
   选择字段：data_stream.dataset
   选择运算符：IS
   选择值：routeros
   ```

4. 为简单起见，我们建议在 Discover 菜单中[搜索字段](https://www.elastic.co/guide/en/kibana/current/discover-get-started.html#explore-fields-in-your-data)并搜索“message”，然后将该字段添加到视图中。
5. 我们还建议搜索“log.syslog.hostname”字段并将其添加到视图中。
6. 考虑[保存搜索](https://www.elastic.co/guide/en/kibana/current/save-open-search.html#_save_a_search)以便日后更方便地访问。
7. 完成。

:::tip
虽然搜索日志可能很有用，但您更可能希望为某些活动创建[警报](https://www.elastic.co/guide/en/kibana/current/alerting-getting-started.html)并创建[连接器](https://www.elastic.co/guide/en/kibana/current/action-types.html)以将警报发送到电子邮件、Webhook、聊天等选项。考虑启用[登录失败事件激增](https://www.elastic.co/guide/en/security/current/spike-in-failed-logon-events.html)规则以在登录失败次数过多时发出警报。您还可以创建[阈值规则](https://www.elastic.co/guide/en/observability/current/metrics-threshold-alert.html)并设置为在固定次数的登录失败后发出警报。

:::