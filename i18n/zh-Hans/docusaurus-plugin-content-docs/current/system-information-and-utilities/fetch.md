# Fetch

> Fetch 是 RouterOS 中用于通过 HTTP、HTTPS、FTP、TFTP 和 SFTP 传输文件的实用工具，支持可配置的身份验证、压缩、重定向及变量存储选项。它同时支持下载/上传模式，并集成 VRF 以实现定向传输。

# Fetch

Fetch 是 RouterOS 控制台实用程序，用于复制文件和执行基于 HTTP 的请求。它支持 HTTP、HTTPS、FTP、TFTP 和 SFTP 协议，允许向远程服务器进行上传、下载以及任意 GET 或 POST 操作。

## 属性

| 属性 | 说明 |
| :-- | :-- |
| **address** (*字符串*; 默认值: ) | 目标设备的 IP 地址。追加 `@vrf_name` 可在特定 VRF 内执行 fetch 操作，或在使用 <code>url</code> 参数时省略地址而仅提供 VRF |
| **as-value** (*集合 \| 未设置*; 默认值: **未设置**) | 设置后，将 fetch 结果存储到变量中（需要 `output` 参数） |
| **ascii** (*yes \| no*; 默认值: **no**) | 为 FTP/TFTP 传输启用 ASCII 模式 |
| **certificate** (*字符串*; 默认值: ) | 来自[证书库](../authentication-authorization-accounting/certificates.md)的[证书]，用于 HTTPS 模式下的服务器验证，仅在启用 <code>check-certificate</code> 时适用 |
| **check-certificate** (*yes \| yes-without-crl \| no*; 默认值: **no**) | 启用针对路由器[证书库](../authentication-authorization-accounting/certificates.md)的信任链验证。`yes-without-crl` 验证证书但跳过 CRL 检查。仅适用于 HTTPS |
| **dst-path** (*字符串*; 默认值: ) | 获取文件将保存到的目标路径 |
| **duration** (*时间*; 默认值: ) | fetch 操作的最大执行时间 |
| **host** (*字符串*; 默认值: ) | 远程 Web 服务器的主机名或虚拟主机名。当同一 IP 服务多个虚拟主机时非常有用。例如，`address=manual.mikrotik.com host=forum.mikrotik.com` |
| **http-auth-scheme** (*basic\|digest*; 默认值: **basic**) | HTTP 身份验证方案 |
| **http-method** (*delete\|get\|head\|post\|put\|patch*; 默认值: **get**) | HTTP 方法 |
| **http-data** (*字符串*; 默认值: ) | 要传输的数据。最大数据限制为 64 Kb |
| **http-header-field** (*字符串*; 默认值: **\*空\***) | 所有头部字段和值的列表，格式为 `http-header-field="h1:fff,h2:yyy"` 或 `http-header-field="h:fff\\,yyy"`（单个头部内的多个值需要使用两个反斜杠进行"转义"）。 |
| **http-content-encoding** (*deflate\|gzip*; 默认值: **\*空\***) | 使用 **gzip** 或 **deflate** 压缩对负载进行编码，并添加相应的 `Content-Encoding` 头部。仅适用于 POST 和 PUT 方法 |
| **http-max-redirect-count** (*整数*; 默认值: 2) | fetch 自动跟随的 HTTP 重定向最大次数 |
| **http-percent-encoding** (*yes \| no*; 默认值: **no**) | 启用请求路径的 URL 百分号编码 |
| **http-version** (*http1\_1* \| *http2*; 默认值: **http1\_1**) | 选择 HTTP 协议版本。HTTP2 仅在 ARM64 和 x86/CHR 设备上受支持 |
| **idle-timeout** (*时间*; 默认值: 10s) | 自上次读/写操作以来的空闲超时时间 |
| **ip-type** (*any \| ipv4 \| ipv6*; 默认值: **any**) | 指定处理域名时优先使用的 IP 族 |
| **keep-result** (*yes \| no*; 默认值: **yes**) | 启用后，获取的数据将写入文件 |
| **mode** (*ftp\|http\|https\|sftp\|tftp*; 默认值: **http**) | 连接所使用的协议。建议通过 `url` 参数指定协议（例如，`url=sftp://ip_address/path`） |
| **output** (*none\|file\|user\|user-with-headers*; 默认值: **file**) | 确定获取数据的存储位置：`none` - 不存储下载的数据；`file` - 将下载的数据存储在文件中；`user` - 将下载的数据存储在数据变量中（变量限制为 64Kb）；`user-with-headers` - 将下载的数据和头部存储在数据变量中（变量限制为 64Kb - 下载数据 20Kb，头部 44Kb） |
| **password** (*字符串*; 默认值: **anonymous**) | 远程设备上的身份验证密码 |
| **port** (*整数*; 默认值: ) | 连接所使用的端口 |
| **src-address** (*IP 地址*; 默认值: ) | 建立连接所使用的源 IP 地址，仅适用于 HTTP/S 和 SFTP 模式 |
| **src-path** (*字符串*; 默认值: ) | 远程文件的路径 |
| **upload** (*yes \| no*; 默认值: **no**) | 为 FTP/SFTP 传输启用上传模式，需要 `src-path` 和 `dst-path` |
| **url** (*字符串*; 默认值: ) | 资源的完整 URL；可替代单独的 `address` 和 `src-path` 参数 |
| **user** (*字符串*; 默认值: **anonymous**) | 远程设备上的身份验证用户名 |

## 配置示例

以下示例演示如何通过 FTP 协议从 IP 地址为 192.168.88.2 的设备复制文件名为 "conf.rsc" 的文件，并将其保存为文件名为 "123.rsc" 的文件。登录设备需要用户名和密码。

```ros
[admin@MikroTik] /tool> fetch address=192.168.88.2 src-path=conf.rsc user=admin mode=ftp password=123 dst-path=123.rsc port=21 host="" keep-result=yes
```

将文件上传到另一台路由器的示例：

```ros
[admin@MikroTik] /tool> fetch address=192.168.88.2 src-path=conf.rsc user=admin mode=ftp password=123 dst-path=123.rsc upload=yes
```

另一个演示 url 属性用法的文件下载示例。

```ros
[admin@MikroTik] /> /tool/fetch url="https://www.mikrotik.com/img/netaddresses2.pdf" mode=http
  status: finished

[admin@test_host] /> /file/print
 # NAME                     TYPE                  SIZE                 CREATION-TIME
 ...
 5 netaddresses2.pdf        .pdf file             11547                2010-06-01 11:59:51
```

您可以通过在“@”符号后附加 VRF 名称，在特定 VRF 中运行 /tool fetch：

* 在 URL 中 – ```url="http://192.168.88.2@vrf1/…"```（适用于 HTTP/HTTPS，不适用于 SFTP）。
* 在 address 属性中 – ```address=192.168.88.2@vrf1```
* 作为单独的 address 参数 – ```address=@vrf1``` 与提供 IP 的 URL 结合使用。

address 属性可以与 VRF 结合，并用“@”分隔（`address=192.168.88.2@vrf1`），或者如示例中所示，仅作为 address 参数，在 VRF 名称前使用“@”符号（使用 URL 中的地址并将其与 address 参数中的 VRF 名称结合）：

```ros
[admin@MikroTik] /> /tool/fetch url="sftp://192.168.88.2" address=@test src-path=test.txt user=admin password="" upload=yes

  status: finished
```

### 向远程主机发送信息

可以使用 HTTP POST 请求向准备接收信息的远程服务器发送信息。在以下示例中，我们将地理坐标发送到一个 PHP 页面：

```ros
/tool/fetch http-method=post http-header-field="Content-Type:application/json" http-data="{\"lat\":\"56.12\",\"lon\":\"25.12\"}" url="https://testserver.lv/index.php"    
```

在此示例中，数据作为文件上传。重要提示：由于变量数据来自文件，文件大小最大只能为 4KB。这是 RouterOS 变量的限制。

```ros
/export file=export.rsc

:global data [/file/get [/file/find name=export.rsc] contents];
:global url "https://prod-51.westeurope.logic.azure.com:443/workflows/blabla/triggers/manual/paths/invoke....";

/tool/fetch mode=https http-method=put http-data=$data url=$url
```

### 将返回值赋给变量

可以将 fetch 命令的结果保存到变量中。

#### 示例 1

可以根据 HTTP 页面返回的结果触发特定操作。以下是一个非常简单的示例，当 PHP 页面返回“0”时禁用 **ether2**：

```ros
{
    :local result [/tool/fetch url=https://10.0.0.1/disable_ether2.php as-value output=user];
    :if ($result->"status" = "finished") do={
        :if ($result->"data" = "0") do={
            /interface/ethernet/set ether2 disabled=yes;
        } else={
            /interface/ethernet/set ether2 disabled=no;
        }
    }
}
```

#### 示例 2

如果 fetch 失败，可以访问错误代码（“code”）和返回的 HTTP 头部（“http-headers”）。

```ros
:onerror err,attr in={ /tool/fetch http://127.0.0.1/error as-value} do={:put $err;:put ($attr->"code");:put ($attr->"http-headers")}
failure: Status 404, Not Found
404
Cache-Control: no-store;Connection: Keep-Alive;Content-Length: 99;Content-Type: text/html;Date: Tue, 09 Dec 2025 13:27:44 GMT;Expires: 0;Pragma: no-cache;X-Frame-Options: sameorigin 
```