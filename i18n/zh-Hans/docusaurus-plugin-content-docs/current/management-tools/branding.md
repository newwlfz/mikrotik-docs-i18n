# 品牌定制

> RouterOS 品牌定制包支持对系统元素进行定制，包括路由器名称、公司URL、ASCII标志和WebFig界面。它支持为登录页面、皮肤和热点标志包含自定义文件，同时提供版本特定的选项，如SNMP名称隐藏。

# 品牌定制

RouterOS允许通过品牌定制包对系统进行轻度定制（修改默认配置、LCD标志、WebFig主页等）。

这是一个特殊的系统包，您可以从您的 [mikrotik.com](https://mikrotik.com) 账户中的“品牌定制器”部分生成。生成的文件将具有 .dpk 扩展名，可以通过与 .npk 包相同的方式安装。

要在路由器上安装该包，需要将其上传到路由器，然后重启路由器。Netinstall 工具也可用于实现相同效果。

生成的包可以安装在任何 RouterOS 版本中。

:::info
请注意，特定品牌定制功能从特定 RouterOS 版本开始可用。

:::

## 选项

可以使用品牌定制包配置的选项：

- **路由器名称** - 品牌定制包名称、设备标识和 RouterOS 中的 [平台名称](../diagnostics-monitoring-and-troubleshooting/resource.md)，只能是一个单词，不要使用空格或特殊字符。
- **公司 URL** - 当您连接到 RouterOS 设备时在控制台中显示的值。
- **手册 URL** - 文档链接，可以在 [WebFig](./webfig.md) 中打开。
- **ASCII 标志** - 登录命令行界面（即 Telnet、SSH、WinBox 终端）时显示的文本标志。可以在 [品牌定制器](https://mikrotik.com/client/branding) 中创建标志，或从任何其他纯文本编辑器中复制。标志高度不能超过 8 行，宽度不受限制，但请注意在窄终端窗口中标志可能会变形。
- **从 SNMP 信息中隐藏“Mikrotik”** - MikroTik 名称将在 SNMP 信息中隐藏。
- **安装时不运行脚本** - 安装品牌定制包时不运行默认配置脚本。
- **隐藏默认配置提示** - 配置重置后隐藏默认配置提示 *(从 RouterOS 7.15 开始可用)*。
- **隐藏默认 CAPs 模式脚本** - 隐藏默认 CAPs 模式脚本 *(从 RouterOS 7.15 开始可用)*。

## 自定义文件

自定义文件，如 WebFig 登录页面、WebFig 标志、热点、皮肤、默认配置、LCD 标志和 CAPs 模式脚本，可以包含在品牌定制包中。

:::warning
任何重置按钮模式都将从品牌定制包恢复默认配置。

:::

#### WebFig 登录页面

WebFig 登录页面是定制的默认 RouterOS 登录界面，在访问路由器的 IP 地址时出现。此页面可以根据品牌或功能需求进行定制。

- **定制文件：**

  - **`/index2.html`**：登录页面的主模板。
  - **`/assets/style.css`**：MikroTik RouterOS 样式表。
  - **`/assets/script.js`** 负责处理登录功能，并包含使按钮具有交互性的代码。
- **`script.js` 的必需元素：**

  1. **登录表单：**  
     `<form id="login">`
  2. **用户名字段：**  
     `<input id="name" data-defaultuser="admin">`
     - `admin` 值可以更改为其他用户名或留空。
  3. **密码字段：**  
     `<input id="password">`
  4. **错误显示区域：**  
      ``
- 以下是一个用户自定义登录页面的示例，带有“显示密码”按钮，通过修改后的 **`[index2.html](pathname:///assets/295239801_index2.html)`** 以及额外的 [toggle_button.css](pathname:///assets/295239803_toggle_button.css) 和 [show_password.js](pathname:///assets/295239802_show_password.js) 文件实现。  
  HTML 文件必须命名为“index2.html”，并应使用正确嵌套的 HTML 以确保与所有浏览器兼容。
- 上传的图像或 JavaScript 文件必须引用与索引文件相同的路径。不能使用自定义文件夹名称。

---

#### WebFig 标志

RouterOS WebFig 页面（配置页面）标志。要覆盖 WebFig 登录页面上的 MikroTik 标志，请上传名为“mikrotik\_logo.png”的自定义标志。

#### 热点

热点登录页面标志。文件必须命名为“logobottom.png”。

#### 皮肤

名为“your\_file\_name.json”的皮肤文件。要将特定皮肤应用于特定用户组，您无需登录路由器。您可以通过上传默认配置文件来进行品牌定制。

#### 默认配置

一个 RouterOS 默认配置文件，将覆盖 RouterOS 默认配置。此配置即使在 RouterOS 重置后也会保留。可以使用只读变量 *$defconfPassword* 和 *$defconfWifiPassword* 重新应用出厂密码（从 RouterOS 7.10 开始可访问出厂密码）。

:::warning
如果默认配置或 CAPs 模式脚本执行时间超过 2 分钟，脚本将失败，LOG 中将包含 *"runtime limit exceeded"* 或极少数情况下出现 *"std failure: timeout"* 错误。

:::

#### LCD 标志

LCD 标志将显示在配备 LCD 屏幕的设备上。标志大小不能超过 160px 宽和 72px 高。CCR1xxx 系列具有白色（0xffffff）背景，2011 系列具有黑色（0x000000）背景。

#### 自定义文件

自定义文件将被复制到名为“branding”的文件夹中，并可从 RouterOS 内部访问。

#### CAPs 模式脚本

一个 RouterOS CAPs 模式脚本，将覆盖 RouterOS 默认 CAPs 模式脚本。可以通过利用只读变量 *$defconfPassword* 和 *$defconfWifiPassword* 重新应用出厂密码（从 RouterOS 7.15 开始可用）。

:::warning
任何重置按钮模式都将从品牌定制包恢复默认配置。CAPs 模式脚本只能在设备完全启动后通过 GUI 或 CLI 执行 [配置重置](../getting-started/configuration-management/index.md#configuration-reset) 来应用。

:::

:::warning
如果默认配置或 CAPs 模式脚本执行时间超过 2 分钟，脚本将失败，LOG 中将包含 *"runtime limit exceeded"* 或极少数情况下出现 *"std failure: timeout"* 错误。

:::