# 包

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/package

**类型：** 目录

在此菜单中执行的命令仅在路由器重启后生效。在此之前，您可以自由安排或撤销已设置的操作。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="A" typ="available"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string">软件包名称。</ArgTableRow>
<ArgTableRow arg="version" typ="string">软件包版本。</ArgTableRow>
<ArgTableRow arg="build-time" typ="date">软件包构建的日期和时间。</ArgTableRow>
<ArgTableRow arg="scheduled" typ="enum ( | scheduled for uninstall | scheduled for disable | scheduled for enable | 使用 `apply-changes` 继续安装)">下次重启后软件包的预定操作。</ArgTableRow>
<ArgTableRow arg="bundle" typ="enum">此软件包所属的捆绑包。</ArgTableRow>
<ArgTableRow arg="size" typ="num">软件包大小（字节）。</ArgTableRow>
</ArgTable>

### system/package/apply-changes

**类型：** 命令

应用已安排的更改并重启设备。

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="ignore-missing" typ="bool" unset="1">仅升级 RouterOS 主软件包，忽略缺失或未上传的软件包。</ArgTableRow>
</ArgTable>

### system/package/disable

**类型：** 命令

安排软件包在下次重启后被禁用。该软件包提供的所有功能将不可访问。

### system/package/downgrade

**类型：** 命令

提示重启。在重启过程中，路由器将尝试通过检查已上传到路由器的软件包，将 RouterOS 降级到尽可能旧的版本。

### system/package/enable

**类型：** 命令

### system/package/uninstall

**类型：** 命令

安排软件包从路由器中移除。该操作将在重启时执行。

### system/package/unschedule

**类型：** 命令

### system/package/update

**类型：** 设置目录

管理 `check-for-updates` 频道并执行 RouterOS 升级。

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="channel" typ="enum ()">检查新版本时使用的升级 [频道](#channel)。</ArgTableRow>
<ArgTableRow arg="mode" typ="enum ()">连接到 MikroTik 下载服务器的协议。仅在您的网络阻止 HTTPS 时使用 `http`。推荐使用 HTTPS。</ArgTableRow>
<ArgTableRow arg="check-certificate" typ="enum ()">是否以及如何验证服务器 SSL 证书。始终使用 `yes` 以确保安全连接。</ArgTableRow>
<ArgTableRow arg="ip-version" typ="enum ()">连接到 MikroTik 下载服务器的 IP 版本偏好。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="installed-version" typ="string">当前安装的 RouterOS 版本。</ArgTableRow>
<ArgTableRow arg="latest-version" typ="string">所选 [频道](#channel) 中可用的最新 RouterOS 版本。</ArgTableRow>
<ArgTableRow arg="status" typ="string">更新过程的当前状态（例如，`New version is available`）。</ArgTableRow>
</ArgTable>

#### system/package/update/cancel

**类型：** 命令

#### system/package/update/check-for-updates

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="fetch-changelog" typ="switch">是否在检查更新时同时获取变更日志。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="changelog" typ="string">最新可用版本的变更日志文本。</ArgTableRow>
</ArgTable>

#### system/package/update/download

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="ignore-missing" typ="bool" unset="1">仅下载 RouterOS 主软件包，忽略缺失或未上传的软件包。</ArgTableRow>
</ArgTable>

#### system/package/update/install

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="ignore-missing" typ="bool" unset="1">仅安装 RouterOS 主软件包，忽略缺失或未上传的软件包。</ArgTableRow>
</ArgTable>