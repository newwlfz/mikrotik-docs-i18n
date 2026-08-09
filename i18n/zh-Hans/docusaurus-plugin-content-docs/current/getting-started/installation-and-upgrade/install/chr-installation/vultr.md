# CHR：Vultr 安装指南

> 本页面指导用户在 Vultr 上部署 MikroTik CHR，首先设置 SystemRescue 服务器，然后使用 wget 和 dd 命令将 CHR 镜像写入磁盘，最后通过 SSH 连接并配置路由器。

# CHR：Vultr 安装指南

Vultr 拥有超过[二十四个数据中心位置](https://www.vultr.com/features/datacenter-locations/)，您可以选择在这些位置部署 MikroTik CHR，以获得最佳的[吞吐量和延迟](https://nj-us-ping.vultr.com/)表现。  
请按照以下步骤在 Vultr 上安装 MikroTik CHR。

## 步骤 1：以救援模式部署服务器

在此步骤中，您将在 Vultr 上部署一台新服务器，并使用 SystemRescue（一个可引导的 Linux ISO）。

1. [部署](https://my.vultr.com/deploy/)一台新的 [Cloud Compute](https://www.vultr.com/products/cloud-compute/) 实例。
2. 根据您的需求选择性能最佳的位置。您可以使用 Vultr 的[网络透视镜](https://nj-us-ping.vultr.com/)来测试任意位置的吞吐量和延迟。
3. 在 **服务器镜像** 部分选择 **ISO 库** 选项卡。
4. 选择 **SystemRescue x64**。
5. 选择具有[足够带宽配额](https://www.vultr.com/resources/faq/?query=bandwidth#bandwidthcalculation)的服务器规格，以满足您的需求。
6. 为服务器设置主机名和标签，然后点击 **立即部署**。

服务器部署完成后，请继续下一步。

## 步骤 2：将 CHR 镜像写入磁盘

1. 在您的网页浏览器中，访问 [MikroTik 下载页面](https://mikrotik.com/download)。
2. 找到最新的 Stable RAW CHR 磁盘镜像。Vultr 要求版本 **7.2.3 Stable** 或更高版本。
3. 右键点击软盘图标以复制 URL。现在不要下载镜像；您将在后续步骤中将其下载到服务器。  
   ![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/install/chr-installation/img/vultr-01.webp)
4. 在 [Vultr 客户门户](https://my.vultr.com/)中导航到服务器的信息页面。
5. 连接到 [Web 控制台](https://www.vultr.com/docs/vultr-web-console-faq/)。  
   ![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/install/chr-installation/img/vultr-02.webp)
6. 在 Web 控制台中，使用 "wget" 将 CHR 镜像下载到服务器。如果您已将下载 URL 复制到剪贴板，可以通过 Web 控制台[将其发送到服务器](https://www.vultr.com/docs/vultr-web-console-faq/)。

   在以下示例中，请将 x.x.x 替换为您所使用的版本。

    ```bash
    # wget https://download.mikrotik.com/routeros/x.x.x/chr-x.x.x.img.zip
    ```

7. 解压下载的文件。

    ```bash
    # unzip chr-x.x.x.img.zip
    ```

8. 使用 dd 命令将 MikroTik CHR 镜像写入服务器磁盘。

    ```bash
    # dd if=chr-x.x.x.img of=/dev/vda
    ```

- - **if** 是您在上一步中解压的镜像文件。
  - **of** 是服务器的磁盘：`/dev/vda`。

此过程需要几分钟时间；完成后请继续下一步。

## 步骤 3：连接到 MikroTik CHR

1. 导航到服务器的[设置页面](https://my.vultr.com/)。
2. 选择 **自定义 ISO** 菜单，然后点击 **移除 ISO**。服务器将重新启动。
3. 连接到 [Web 控制台](https://www.vultr.com/docs/vultr-web-console-faq/)。
4. 以 admin 身份登录。由于未设置密码，请在提示符处按 <kbd>Enter</kbd> 键。
5. 查看软件许可证，然后设置一个新的强密码。
6. 关闭 Web 控制台，然后在本地计算机上打开终端。
7. 使用 SSH 以 admin 身份连接到服务器的 IP 地址。

   ```ros
   ssh admin@192.0.2.2
   ```

8. 输入您在上一步中设置的强密码。

至此，基本安装已完成。请[保护您的 MikroTik CHR 路由器](../../../securing-your-router.md)，并查阅[文档](../../../first-time-configuration.md)以配置服务器用于生产环境。请访问 Vultr 网站了解其 [VPC](https://docs.vultr.com/products/network/vpc) 和[防火墙](https://docs.vultr.com/vultr-firewall)功能。