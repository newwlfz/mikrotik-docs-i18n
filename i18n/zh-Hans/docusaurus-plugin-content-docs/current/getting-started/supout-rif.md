# Supout.rif

> supout.rif 文件是 MikroTik 的二进制诊断工具，包含路由器配置、日志及详细信息，旨在帮助支持团队高效解决问题。可通过 WinBox、Webfig 或控制台生成，并可使用 Supout.rif 查看器查看，且不包含敏感数据。

# Supout.rif

## 什么是 supout.rif 文件？

supout.rif 文件是 MikroTik 的支持输出文件，用于调试 RouterOS 并加速问题解决。此二进制文件包含路由器的完整配置、日志及其他详细信息，帮助 MikroTik 支持团队更高效地诊断和解决问题。

该文件存储在路由器上，可通过 FTP 或 WinBox 下载。在具有 FLASH 类型存储或外部存储的设备上，您可以通过指定完整路径（例如，name=flash/supout.rif）在 /flash 文件夹中生成该文件。

要查看文件内容，请登录您的 MikroTik 账户，并使用左侧导航栏中的“Supout.rif 查看器”工具上传并分析文件。

**注意：** supout.rif 文件不包含路由器密码等敏感信息。

## 创建支持输出文件

### Winbox

要在 Winbox 中生成此文件，请点击“Make Supout.rif”。

要将文件保存到您的计算机，请右键点击文件并选择“Download”以获取支持输出文件，或直接将文件拖拽至桌面。

### ![](https://manual.mikrotik.com/docs/getting-started/img/supout-rif-01.webp)Webfig

要在 Webfig 中生成此文件，请点击“Make Supout.rif”，然后点击“Download”将其下载到您的计算机。

![](https://manual.mikrotik.com/docs/getting-started/img/supout-rif-02.webp)

![](https://manual.mikrotik.com/docs/getting-started/img/supout-rif-03.webp)

### 控制台

要生成此文件，请在命令行中输入：

```ros
/system/sup-output name=supout.rif
```

如果您在 supout 查看器中打开文件时输出过窄，您可以重新生成 supout 文件，并使用 output-width 选项手动指定输出宽度：

```ros
/system/sup-output name=supout.rif output-width=300
```