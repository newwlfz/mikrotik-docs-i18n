# x86 安装指南

> 本页提供在 x86 硬件上通过 USB 或 Netinstall 安装 RouterOS 的分步指南，涵盖 Windows/Linux/macOS 方法、BIOS 设置调整及启动优先级配置，以确保安装成功。

# x86 安装指南

## USB 安装

### 分步指南

1. 从下载页面下载 x86 CD 镜像文件：https://mikrotik.com/download

    - 在 Windows 系统上：

        - 下载 Rufus：https://github.com/pbatard/rufus/releases （请使用最新版本）
        - 连接 USB 驱动器并打开 Rufus
        - 选择下载的 ISO 镜像并点击 **START**

    - 在 Linux、FreeBSD 或 macOS 系统上：

        :::danger
        警告！请仔细确认正确的设备地址——`dd` 命令可能不可逆地破坏数据。
        :::

        - 连接 USB 驱动器并识别其设备地址

            macOS：

            ```text
            diskutil list
            ```

            Linux / FreeBSD：

            ```text
            fdisk -l
            ```

        - 使用 `dd` 命令前，请确保 USB 驱动器已格式化且所有旧数据已清除

    使用 `dd` 将镜像写入磁盘：

    ```bash
    dd if=<your_downloaded_routeros_ISO> of=<disk_address> bs=1M status=progress
    ```

    macOS：

    ```bash
    dd if=<your_downloaded_routeros_ISO> of=<disk_address> bs=1m status=progress
    ```

    操作完成后，将 USB 驱动器连接到 x86 系统并从其启动。

    在键盘上按 **"i"** 键继续安装。

    重启后，RouterOS 将安装完成。

启动优先级应在 BIOS 设置中调整。如果 RouterOS 安装在 NVMe 驱动器上，则 USB 必须以 UEFI 模式启动。

请确保 BIOS 启动设置中已禁用 CSM（兼容性支持模块）。

## 使用 Netinstall 安装 x86 系统

1. 下载适用于您系统的 Netinstall 工具并在 PC 上运行
2. 从下载页面下载 x86 CD 镜像文件：https://mikrotik.com/download
3. 将 PC 的 BIOS 启动选项设置为 PXE
4. 保存更改并重启
5. 按照 Netinstall 工具的步骤继续操作