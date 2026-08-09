# CHR：VirtualBox 安装指南

> 本页提供在 VirtualBox 中安装 MikroTik RouterOS 云托管路由器（CHR）的分步指南，涵盖虚拟机创建、配置及初始设置，并包含登录说明。

# CHR：VirtualBox 安装指南

## CHR VirtualBox 安装视频

**[![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/install/chr-installation/img/chr_video.png)](https://www.youtube.com/watch?v=oHXkaHkSVVo)**

1. **下载 VirtualBox**  
   从官方网站安装最新版本的 VirtualBox。

2. **下载 CHR 磁盘镜像**  
   从 [MikroTik 下载页面](https://mikrotik.com/download) 下载并解压最新长期版、稳定版或测试版的云托管路由器（CHR）VDI 镜像。

![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/install/chr-installation/img/chr_install_virtualbox_01.png)

## 步骤 1：创建新的虚拟机

- 启动 VirtualBox。
- 点击 **新建** 以创建新的虚拟机。

![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/install/chr-installation/img/chr_install_virtualbox_02.png)

### 名称和操作系统

- **名称**：输入虚拟机名称（例如，MikroTik_CHR）
- **类型**：Linux
- **版本**：其他 Linux（64 位）

![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/install/chr-installation/img/chr_install_virtualbox_03.png)

## 步骤 2：配置内存大小

- 分配至少 **512 MB 内存**（RouterOS 7 最低要求）
- 分配所需的 CPU 核心数

![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/install/chr-installation/img/chr_install_virtualbox_04.png)

## 步骤 3：添加虚拟硬盘

- 选择 **使用现有的虚拟硬盘文件**
- 选择下载的 `.vdi` 镜像

![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/install/chr-installation/img/chr_install_virtualbox_05.png)

点击 **完成** 以创建虚拟机。

## 步骤 4：配置虚拟机设置

选择虚拟机 → 点击 **设置**

![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/install/chr-installation/img/chr_install_virtualbox_06.png)

### 系统

- 在启动顺序中禁用 **软盘** 和 **光驱**

![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/install/chr-installation/img/chr_install_virtualbox_06_1.png)

### 处理器

- 设置所需的 CPU 核心数

### 网络

- 适配器 1：
  - 启用网络适配器
  - 连接到 **桥接适配器** 或 **NAT**（取决于您的网络环境）

![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/install/chr-installation/img/chr_install_virtualbox_07.png)

## 步骤 5：启动虚拟机

- 点击 **启动** 以启动虚拟机

![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/install/chr-installation/img/chr_install_virtualbox_08.png)

- 登录凭据：
  - 用户名：`admin`
  - 密码：*（留空，首次登录后立即设置）*

![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/install/chr-installation/img/chr_install_virtualbox_09.png)

## 恭喜

您已成功在 VirtualBox 上安装 MikroTik CHR。

现在，您可以使用控制台、WinBox 或 WebFig 进行 RouterOS 的初始配置。

## 支持的网络和磁盘接口

### 网络适配器

- E1000
- RTL8139
- Virtio（半虚拟化）

### 磁盘控制器

- IDE

> **警告：** 除非没有更好的合成或半虚拟化选项，否则请避免使用 E1000 网络适配器。Virtio 在 VirtualBox 上提供更好的性能。