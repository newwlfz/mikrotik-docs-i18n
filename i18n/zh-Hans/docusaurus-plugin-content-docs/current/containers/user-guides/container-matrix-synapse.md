# 容器 - Matrix (Synapse)

> 本文档介绍如何在 MikroTik RouterOS 上以容器方式搭建 Synapse Matrix 服务器，涵盖容器网络配置和 PostgreSQL 环境设置等前置要求，以实现跨平台的安全联邦通信。

# 容器 - Matrix (Synapse)

Matrix 是一种去中心化的通信协议。每个 Matrix 服务器独立运行，维护自己的用户集合并定义自己的规则与策略。

### 托管您自己的 Matrix 服务器

您可以使用容器直接在 RouterOS 设备上托管自己的 Matrix 服务器。这样您可以完全掌控自己的通信基础设施。

### 联邦（Federation）

Matrix 服务器可以通过联邦连接，形成一个统一的通信网络。这使得不同 Matrix 服务器上的用户无需中央权威机构即可安全地相互通信。

### 桥接至其他平台

Matrix 支持桥接，以中继来自其他聊天平台的消息，包括：

- WhatsApp
- Discord
- Signal
- Telegram
- 以及许多其他平台

通过使用 Matrix 桥接，您可以将来自多个平台的通信整合到一个应用程序中，例如 [Element](https://element.io/)。这样您就可以通过一个统一界面与不同平台上的用户进行通信。

# 在 RouterOS 上设置 Synapse Matrix 服务器

本指南介绍如何使用容器在您的 MikroTik RouterOS 设备上设置 Synapse（可用的多种 Matrix 服务器之一）。

:::info

在继续操作之前，请确保您已创建容器网络。相关说明请参阅 [容器网络文档](../#networking-examples)。

:::

---

## 前置要求

- 支持容器的 RouterOS 设备
- 已配置好的容器网络
- 足够的存储空间用于数据库和 Synapse 数据

---

## 步骤 1：创建 PostgreSQL 容器环境变量

为 PostgreSQL 容器配置环境变量列表：

```routeros
/container/envs/add list=postgres_synapse_envs key=POSTGRES_DB value="synapse"
/container/envs/add list=postgres_synapse_envs key=POSTGRES_PASSWORD value="<POSTGRES_PASSWORD_HERE>"
/container/envs/add list=postgres_synapse_envs key=POSTGRES_USER value="synapse_user"
/container/envs/add list=postgres_synapse_envs key=PGDATA value="/var/lib/postgresql/data/pgdata"
/container/envs/add list=postgres_synapse_envs key=POSTGRES_INITDB_ARGS value="--encoding='UTF8' --lc-collate='C' --lc-ctype='C'"
/container/envs/add list=postgres_synapse_envs key=PGPORT value=5433
```

:::note

请将 `<POSTGRES_PASSWORD_HERE>` 替换为您想要的 PostgreSQL 密码。

:::

---

## 步骤 2：创建 PostgreSQL 容器挂载点

创建一个挂载点，用于在 RouterOS 设备上持久化 PostgreSQL 数据：

```routeros
/container/mounts/add list=synapse_postgres_data src=disk1/synapse-postgres-data dst=/var/lib/postgresql/data
```

---

## 步骤 3：创建 PostgreSQL 容器

使用前面步骤中的配置启动 PostgreSQL 容器：

```routeros
/container/add remote-image=postgres:17.2-alpine interface=veth1 root-dir=disk1/postgres-17.2-synapse mountlists=synapse_postgres_data envlists=postgres_synapse_envs name=postgresql_synapse
```

---

## 步骤 4：创建 Synapse 容器环境变量

为 Synapse 容器配置环境变量：

```routeros
/container/envs/add list=synapse_envs key=SYNAPSE_CONFIG_DIR value="/data"
/container/envs/add list=synapse_envs key=SYNAPSE_CONFIG_PATH value="/data/homeserver.yaml"
/container/envs/add list=synapse_envs key=SYNAPSE_SERVER_NAME value="test.mt.lv"
/container/envs/add list=synapse_envs key=SYNAPSE_REPORT_STATS value="yes"
```

:::note

请将 `test.mt.lv` 替换为您实际的服务器域名。

:::

---

## 步骤 5：创建 Synapse 容器挂载点

创建一个挂载点，用于在 RouterOS 设备上持久化 Synapse 数据：

```routeros
/container/mounts/add list=synapse_data src=disk1/synapse-data dst=/data
```

---

## 步骤 6：生成初始 Synapse 配置

创建并运行一个 Synapse 容器以生成所需的配置文件。容器使用 `generate` 命令运行以创建初始配置：

```routeros
/container/add remote-image=matrixdotorg/synapse:latest interface=veth1 cmd="generate" root-dir=disk1/synapse mountlists=synapse_data envlists=synapse_envs name=synapse
```

---

## 步骤 7：初始化配置文件

启动然后停止 Synapse 容器，使其生成必要的配置文件：

```routeros
/container/start [find where name=synapse]
/container/stop [find where name=synapse]
```

---

## 步骤 8：移除 generate 命令

清除 Synapse 容器的命令参数，使其以正常模式运行：

```routeros
/container/set [find where name=synapse] cmd=""
```

---

## 步骤 9：配置数据库连接

使用 SFTP 客户端（例如 Windows 下的 WinSCP）连接到您的 RouterOS 设备，并编辑位于 `disk1/synapse-data/homeserver.yaml` 的生成配置文件。使用以下设置更新数据库部分：

```yaml
database:
  name: psycopg2
  args:
    user: synapse_user
    password: <POSTGRES_PASSWORD_HERE>
    dbname: synapse
    host: 172.17.0.2
    port: 5433
    cp_min: 5
    cp_max: 10
    keepalives_idle: 10  # 可选
    keepalives_interval: 10  # 可选
    keepalives_count: 3     # 可选
```

:::info

请将 `<POSTGRES_PASSWORD_HERE>` 替换为步骤 1 中设置的密码。

:::

---

## 步骤 10：启动 PostgreSQL 容器

启动 PostgreSQL 容器以准备数据库：

```routeros
/container/start [find where name=postgresql_synapse]
```

---

## 步骤 11：启动 Synapse 容器

启动 Synapse 容器以运行您的 Matrix 服务器：

```routeros
/container/start [find where name=synapse]
```

---

## 步骤 12：注册 Matrix 用户

进入 Synapse 容器的 shell 并注册新用户：

```routeros
/container/shell [find where name=synapse]
```

进入容器后，运行：

```
register_new_matrix_user -c /data/homeserver.yaml
```

按照提示创建您的管理员用户账户。

---

## 步骤 13：访问您的 Matrix 服务器

您的 Synapse Matrix 服务器现已运行。使用您的 RouterOS 设备的 IP 地址或域名进行访问。

---

:::warning

请始终查阅官方 Synapse 文档以获取最新的配置选项和最佳实践，因为配置流程可能会随新版本而变化。

:::

### Discord 桥接

:::tip

以下示例用于配置 Discord 桥接，但其他类型的[桥接](https://matrix.org/ecosystem/bridges/)的配置流程非常相似。请查阅您所需[桥接](https://matrix.org/ecosystem/bridges/)的官方文档以获取更多信息。

:::

1. 创建 PostgreSQL Discord 桥接容器环境变量：

   ```routeros
   /container/envs/add list=postgres_discord_envs key=POSTGRES_DB value="synapse-discord"
   /container/envs/add list=postgres_discord_envs key=POSTGRES_PASSWORD value="<POSTGRE_BRIDGE_PASSWORD_HERE>"
   /container/envs/add list=postgres_discord_envs key=POSTGRES_USER value="synapse_discord"
   /container/envs/add list=postgres_discord_envs key=PGDATA value="/var/lib/postgresql/data/pgdata"
   /container/envs/add list=postgres_discord_envs key=POSTGRES_INITDB_ARGS value="--encoding='UTF8' --lc-collate='C' --lc-ctype='C'"
    /container/envs/add list=postgres_discord_envs key=PGPORT value=5434
   ```

2. 创建 PostgreSQL Discord 桥接容器挂载点：

   ```routeros
   /container/mounts/add list=discord_postgres_data src=disk1/discord-postgres-data dst=/var/lib/postgresql/data
   ```

3. 为 Discord 桥接创建 PostgreSQL 容器：

   ```routeros
   /container/add remote-image=postgres:17.2-alpine interface=veth1 root-dir=disk1/postgres-17.2-discord mountlists=discord_postgres_data envlists=postgres_discord_envs name=postgresql_discord
   ```

4. 按照 [HAProxy](./container-haproxy.md) 容器指南，为端口 `8080` 设置反向代理
5. 创建 Discord 桥接容器挂载点：

   ```routeros
   /container/mounts/add list=synapse_discord_data src=disk1/synapse-discord-data dst=/data
   ```

6. 创建 Discord 桥接容器：

   ```routeros
   /container/add remote-image=litetex/mau.mautrix.discord:latest interface=veth1 root-dir=disk1/synapse-discord mountlists=synapse_discord_data name=synapse_discord
   ```

7. 启动然后停止 Discord 桥接容器以生成文件：

   ```routeros
   /container/start [find where name=synapse_discord]
   /container/stop [find where name=synapse_discord]
   ```

8. 使用 SFTP 客户端（例如 Microsoft Windows 下的 WinSCP）连接到您的 RouterOS 设备，并调整文件 `disk1/synapse-discord/config.yaml`：

   ```yaml
    homeserver
        address: http://172.17.0.2:8008
        domain: test.mt.lv
       software: standard
       async_media: true
       
   appservice
       address: 保持默认
       hostname: 保持默认
       port: 保持默认
       database:
           type: postgres
           uri: postgres://synapse_discord:<POSTGRE_DISCORD_PASSWORD_HERE>@172.17.0.2:5434/synapse-discord?sslmode=disable
   bridge:
       encryption:
           allow: true
       permissions:
           "*": relay
           "@your_admin_user1:test.mt.lv": admin
           "@your_admin_user2:test.mt.lv": admin
   ```

9. 再次启动然后停止 Discord 桥接容器：

   ```routeros
   /container/start [find where name=synapse_discord]
   /container/stop [find where name=synapse_discord]
   ```

10. 下载文件 `disk1/synapse-discord/registration.yaml` 并将其上传为文件 `disk1/synapse-data/mautrix-discord-registration.yaml`
11. 使用 SFTP 客户端（例如 Microsoft Windows 下的 WinSCP）连接到您的 RouterOS 设备，并将以下行添加到 `disk1/synapse-data/homeserver.yaml`：

     ```yaml
     ...
     app_service_config_files:
     - /data/mautrix-discord-registration.yaml
     ```

12. 启动 Synapse 和 Discord 桥接容器：

     ```routeros
    /container/start [find where name=postgresql_discord]
    /container/start [find where name=synapse_discord]
    /container/start [find where name=postgresql_synapse]
    /container/start [find where name=synapse]
    ```

13. 您的 Matrix 服务器现在应该有一个名为“Discord bridge bot”的新用户。请按照官方文档创建桥接房间。