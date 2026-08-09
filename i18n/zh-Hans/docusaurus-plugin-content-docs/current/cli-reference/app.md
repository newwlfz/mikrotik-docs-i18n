# app

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# app

**Syscap:** app
**Package:** container
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">应用已禁用（未下载/未安装，或已下载但被禁用）</ArgTableRow>
<ArgTableRow arg="R" typ="running">应用正在活跃运行且可访问</ArgTableRow>
<ArgTableRow arg="c" typ="custom">用户创建的自定义应用</ArgTableRow>
<ArgTableRow arg="s" typ="from-app-store">从自定义应用商店安装的应用</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="container-command-lines" typ="object { composite { ,  } { ,  }
 }">指定启动容器时传递给应用的命令行参数</ArgTableRow>
<ArgTableRow arg="auto-update" typ="bool">启用或禁用在新容器镜像版本可用时的自动更新</ArgTableRow>
<ArgTableRow arg="use-https" typ="bool">为应用 URL 使用 HTTPS。此选项在不支持云服务的设备上无效</ArgTableRow>
<ArgTableRow arg="network" typ="enum (default)">指定容器使用的网络：internal（NAT 后）、lan（LAN 网络）或 default（因应用而异）</ArgTableRow>
<ArgTableRow arg="network-pvid" typ="num">设置容器虚拟以太网接口在 bridge 中的 Port VLAN ID (PVID)</ArgTableRow>
<ArgTableRow arg="network-outgoing-access" typ="bool">允许特定容器应用的网络出站访问。设置为 no 时，将创建 mangle drop 规则</ArgTableRow>
<ArgTableRow arg="firewall-redirects" typ="object { composite { ,  } { ,  }
 }">配置从主机设备到容器的端口重定向</ArgTableRow>
<ArgTableRow arg="yaml" typ="string">提供应用的 YAML 配置。配置示例请参阅文档</ArgTableRow>
<ArgTableRow arg="required-mounts" typ="object { composite { ,  } { ,  }
 }">挂载容器启动所需的目录。格式：[host-dir]:[app-dir]</ArgTableRow>
<ArgTableRow arg="extra-mounts" typ="object { composite { ,  } { ,  }
 }">指定附加到容器的额外挂载点</ArgTableRow>
<ArgTableRow arg="environment" typ="object { super { !
, composite { ,  } { ,  }
  } { !
, composite { ,  } { ,  }
  }
 }">定义运行应用可用的环境变量。以键值对列表形式指定</ArgTableRow>
<ArgTableRow arg="secrets" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="required-hw-devices" typ="object { composite { ,  } { ,  }
 }">容器启动时主机上必须存在的硬件设备。格式：[host-hw-device]:[app-device]</ArgTableRow>
<ArgTableRow arg="devices" typ="object { composite { ,  } { ,  }
 }">指定传递给容器应用的额外硬件设备</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="app-store-url" typ="string">安装应用的应用商店 URL</ArgTableRow>
<ArgTableRow arg="name" typ="string">YAML 配置中定义的应用名称</ArgTableRow>
<ArgTableRow arg="description" typ="string">YAML 配置中定义的应用描述</ArgTableRow>
<ArgTableRow arg="project-page" typ="string">YAML 配置中定义的应用项目页面 URL</ArgTableRow>
<ArgTableRow arg="category" typ="string">应用功能分类</ArgTableRow>
<ArgTableRow arg="ui-url" typ="string">应用 Web 界面的生成 URL（如可用）</ArgTableRow>
<ArgTableRow arg="default-credentials" typ="string">应用所需的默认凭据</ArgTableRow>
<ArgTableRow arg="status" typ="string">应用的当前状态（获取 veth、配置容器、下载/解压、启动）</ArgTableRow>
<ArgTableRow arg="default-network" typ="enum">应用使用的默认网络（lan 或 internal）</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum { none:nv::BADID }">应用使用的 VETH 接口</ArgTableRow>
<ArgTableRow arg="ip-address" typ="ipAddr">分配给 VETH 接口的 IP 地址</ArgTableRow>
<ArgTableRow arg="cmds" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="cpu-usage" typ="num">应用当前使用的 CPU 百分比</ArgTableRow>
<ArgTableRow arg="memory-current" typ="num">应用当前使用的内存量</ArgTableRow>
<ArgTableRow arg="app-size" typ="num">应用的总大小</ArgTableRow>
<ArgTableRow arg="data-size" typ="num">应用存储的数据大小</ArgTableRow>
<ArgTableRow arg="configs" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="variables-to-use-in-environment" typ="object { composite { ,  } { ,  }
 }">应用环境中存在的所有变量列表</ArgTableRow>
</ArgTable>

## app/cleanup

**Package:** container
**Type:** Command

删除所有应用数据、配置文件和容器镜像。此操作具有破坏性且不可逆。

## app/network

**Package:** container
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="e" typ="external"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="allow-outgoing-access" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="network" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="ip" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="used-ips" typ="multi { array-id, array-id, composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="bridge-interface" typ="iface_enum { none:nv::BADID }"></ArgTableRow>
<ArgTableRow arg="cmds" typ="multi { string
 }"></ArgTableRow>
</ArgTable>

## app/remove

**Package:** container
**Type:** Command

从系统中移除指定的应用。

## app/restart

**Package:** container
**Type:** Command

重启指定的运行中应用。

## app/settings

**Package:** container
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="disk" typ="enum (none)">全局设置，指定用于存储操作的磁盘</ArgTableRow>
<ArgTableRow arg="router-ip" typ="ipAddr">手动指定当前 RouterOS 设备可访问的 IP 地址</ArgTableRow>
<ArgTableRow arg="lan-bridge" typ="iface_enum { none:nv::BADID }">手动指定代表局域网的 bridge 接口</ArgTableRow>
<ArgTableRow arg="media-path" typ="file">手动指定所有媒体文件的存储目录路径</ArgTableRow>
<ArgTableRow arg="download-path" typ="file">手动指定所有下载内容的存储目录路径</ArgTableRow>
<ArgTableRow arg="show-in-webfig" typ="bool">控制是否在 WebFig 登录页面显示已启用应用的链接</ArgTableRow>
<ArgTableRow arg="auto-update" typ="bool">全局设置，为所有已安装的应用包启用自动更新</ArgTableRow>
<ArgTableRow arg="registry-mirrors" typ="multi { array-id, array-id, composite { ,  } { ,  }
 }">指定一个或多个用于容器镜像获取的 registry 镜像 URL</ArgTableRow>
<ArgTableRow arg="app-store-urls" typ="multi { array-id, string
 }">自定义应用商店的 URL。必须指向一个 YAML 数组，其中每个应用为一个元素</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="assumed-router-ip" typ="ipAddr">自动检测到的 RouterOS 设备网络 IP 地址</ArgTableRow>
<ArgTableRow arg="assumed-lan-bridge" typ="iface_enum { none:nv::BADID }">自动检测到的用于 LAN 连接的 bridge 接口</ArgTableRow>
<ArgTableRow arg="assumed-media-path" typ="file">默认媒体存储路径，通常位于系统磁盘上</ArgTableRow>
<ArgTableRow arg="assumed-download-path" typ="file">默认下载目录路径，通常位于媒体存储区域内</ArgTableRow>
<ArgTableRow arg="certificate-status" typ="string"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)"></ArgTableRow>
</ArgTable>

## app/setup

**Package:** container
**Type:** Command

启动设置向导，自动配置 App 系统的网络、存储和 registry。

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="disk" typ="enum (none)">为应用安装选择的存储磁盘</ArgTableRow>
<ArgTableRow arg="lan-bridge" typ="iface_enum { none:nv::BADID }">为容器网络选择的 LAN bridge 接口</ArgTableRow>
<ArgTableRow arg="router-ip-alt" typ="alt { enum
, ipAddr
 }">RouterOS 设备的手动 IP 地址覆盖</ArgTableRow>
</ArgTable>

## app/update

**Package:** container
**Type:** Command

将指定应用更新到最新的可用容器镜像。