# 本地更新

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### system/package/local-update

**类型：** 目录

您可以将软件包文件上传到本地 RouterOS 设备之一，并将其用作本地软件包服务器，而不是直接连接到 MikroTik 服务器。

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="download" typ="bool">是否从本地软件包服务器下载可用软件包。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="source" typ="alt { ip6Addr
, ipAddr
 }">本地软件包服务器的 IP 地址。</ArgTableRow>
<ArgTableRow arg="name" typ="string">软件包的名称。</ArgTableRow>
<ArgTableRow arg="version" typ="string">软件包的版本。</ArgTableRow>
<ArgTableRow arg="status" typ="enum (installed | downloaded | downloading | scheduled | available)">软件包的当前状态。</ArgTableRow>
<ArgTableRow arg="completed" typ="num">下载完成百分比。</ArgTableRow>
</ArgTable>

#### system/package/local-update/download

**类型：** 命令

下载本地软件包服务器上可用的特定兼容（匹配设备架构）软件包。下载的软件包保存在根目录中。

#### system/package/local-update/download-all

**类型：** 命令

下载本地软件包服务器上可用的所有兼容（匹配设备架构）软件包。下载的软件包保存在根目录中。

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="download-beta" typ="bool">下载所有兼容软件包时是否包含 beta 软件包。</ArgTableRow>
<ArgTableRow arg="reboot-after-download" typ="bool">所有软件包下载完成后是否自动重启设备。</ArgTableRow>
</ArgTable>

#### system/package/local-update/mirror

**类型：** 设置目录

您可以通过此菜单从主本地软件包服务器镜像（适用于所有架构）软件包。下载的软件包保存在根目录下的 `packs` 文件夹中。

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="enabled" typ="bool">是否启用定期检查并从本地软件包服务器下载软件包。</ArgTableRow>
<ArgTableRow arg="primary-server" typ="alt { ip6Addr
, ipAddr
 }">主本地软件包服务器的 IP 地址。</ArgTableRow>
<ArgTableRow arg="secondary-server" typ="alt { ip6Addr
, ipAddr
 }">备用本地软件包服务器的 IP 地址。</ArgTableRow>
<ArgTableRow arg="check-interval" typ="time">设备检查本地软件包服务器是否有新软件包的时间间隔。如果发现新软件包，则开始下载。仅下载设备上尚不存在的软件包。</ArgTableRow>
<ArgTableRow arg="user" typ="string">访问本地软件包服务器的用户名。</ArgTableRow>
<ArgTableRow arg="password" typ="string">访问本地软件包服务器的密码。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="software-id" typ="string">设备的软件 ID。</ArgTableRow>
</ArgTable>

##### system/package/local-update/mirror/force-check

**类型：** 命令

#### system/package/local-update/refresh

**类型：** 命令

刷新并检查本地软件包服务器上可用的兼容（匹配设备架构）软件包列表。

#### system/package/local-update/update-package-source

**类型：** 目录

获取软件包的服务器在此列表中定义。

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="address" typ="alt { ip6Addr
, ipAddr
 }" mandatory="1">本地软件包服务器的 IP 地址。</ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1">访问本地软件包服务器的用户名。</ArgTableRow>
<ArgTableRow arg="password" typ="string" mandatory="1">访问本地软件包服务器的密码。</ArgTableRow>
</ArgTable>