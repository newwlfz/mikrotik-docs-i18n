# 降级 RouterOS

> 了解如何将 RouterOS 降级到先前版本，包括降级前检查、架构验证及分步操作指南。

您可以降级 RouterOS，**但仅限于出厂预装版本**，可通过以下命令查看：

```ros
/system/resource/print

          uptime: 1w1d11h11m1s
         version: 7.23.1 (stable)
      build-time: Jan/01/2026 11:11:11
factory-software: 7.20.8
```

:::warning
factory-software 版本是您的硬件引导加载程序所支持的最早版本。尝试安装比此更旧的版本可能导致系统严重不稳定或设备变砖。
:::

## 降级前检查清单

- **备份所有数据。** 主要版本之间的配置语法会有所变化。直接降级可能导致设置损坏。在继续操作前，请务必生成[二进制备份（`.backup`）](../getting-started/configuration-management/backup.md)和[导出文件（`.rsc`）](../getting-started/configuration-management/#configuration-export)。
- **安全性与稳定性。** 请注意，回退到旧版本会使您的路由器暴露于旧版软件缺陷及已修补的安全漏洞之中。

## 分步降级操作流程

1. **验证架构。** 通过 `/system/resource/print` 检查设备的架构类型（查看 `architecture` 字段，例如 `arm64`、`mipsbe`、`mmips`）。
2. **下载软件包。** 从 [MikroTik 下载页面](https://mikrotik.com/download) 下载与目标旧版本及确切架构相匹配的“Extra packages”或主捆绑包 zip 文件。
3. **上传文件。** 通过 WinBox、WebFig 或 FTP 客户端连接到路由器，打开 Files 菜单，上传所有必需的 `.npk` 文件。
4. **执行降级。** 在终端中运行降级命令序列：

   ```ros
   /system/package/downgrade
   ```

5. **重启。** 在提示时确认操作。执行 `/system/reboot` 重启路由器——它将解包旧版本并重新上线，完成降级。

重启后，运行 `/system/resource/print` 并确认 `version` 字段显示预期的降级目标版本，以验证新版本。