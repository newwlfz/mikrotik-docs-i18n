# 入门指南

> 入门指南提供了RouterOS初始设置的基本说明，包括连接方法、管理界面访问以及将MikroTik路由器投入服务所需的基本安全任务。

# 入门指南

import DocCardList from '@theme/DocCardList';

入门指南涵盖了RouterOS的初始设置、配置管理、安装、许可、升级、备份以及首次安全任务。使用本部分内容将路由器投入服务并维护基础系统。

## 快速入门：连接您的路由器

如果您刚拆开MikroTik设备的包装，并希望访问其管理界面：

1. 将以太网电缆从您的计算机连接到路由器上除`ether1`之外的**任意**端口。
2. 接通电源。等待大约一分钟，让设备完成启动。
3. 使用以下任一方式访问管理界面：
   - 浏览器访问 **`http://192.168.88.1`**（WebFig）
   - **[WinBox](https://mikrotik.com/download)** — 适用于Windows、macOS和Linux的桌面图形界面
   - **MikroTik移动应用**（iOS / Android）
4. 以用户 **`admin`** 身份登录，密码为**路由器标签上**打印的设备专属密码（包装盒上也有）。

您已成功进入。当您准备好实际配置互联网访问、Wi-Fi、防火墙规则等时，请遵循完整的[首次配置](./first-time-configuration.md)指南。

<DocCardList />