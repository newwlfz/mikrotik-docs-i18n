# Fetch

> Fetch is a RouterOS utility for transferring files via HTTP, HTTPS, FTP, TFTP, and SFTP with configurable authentication, compression, redirects, and variable storage options. It supports both download/upload modes and VRF integration for targeted transfers.

# Fetch

Fetch is a RouterOS console utility for copying files and performing HTTP‑based requests. It works with HTTP, HTTPS, FTP, TFTP and SFTP, allowing uploads, downloads, and arbitrary GET or POST operations to remote servers.

## Properties

| Property | Description |
| :-- | :-- |
| **address** (*string*; Default: ) | IP address of the target device. Append `@vrf_name` to run the fetch operation within a specific VRF, or omit the address and supply only the VRF when using the <code>url</code> parameter |
| **as-value** (*set \| not-set*; Default: **not-set**) |When set, stores the fetch result in a variable (requires `output` parameter) |
| **ascii** (*yes \| no*; Default: **no**) | Enables ASCII mode for FTP/TFTP transfers |
| **certificate**(*string*; Default: ) | [Certificate from certificate store](../authentication-authorization-accounting/certificates.md) used for server verification in HTTPS mode, applicable only when <code>check-certificate</code> is enabled |
| **check-certificate** (*yes \| yes-without-crl \| no*; Default: **no**) | Enables trust‑chain validation against the router’s [certificate store](../authentication-authorization-accounting/certificates.md). `yes-without-crl` validates the certificate but skips CRL checks. HTTPS only|
| **dst-path** (*string*; Default: ) | Destination path where the fetched file will be saved|
| **duration** (*time;* Default: ) | Maximum execution time for the fetch operation |
| **host** (*string*; Default: ) | Hostname or virtual hostname of the remote web server. Useful when the same IP serves multiple virtual hosts. For example, `address=manual.mikrotik.com host=forum.mikrotik.com`|
| **http-auth-scheme** (*basic\|digest*; Default: **basic**) | HTTP authentication scheme |
| **http-method** (*delete\|get\|head\|post\|put\|patch*; Default: **get**) | HTTP method |
| **http-data** (*string*; Default: ) | The data to be transmitted. Maximum data limit is 64 Kb|
| **http-header-field** (*string*; Default: **\*empty\***) | List of all header fields and values, in the form of `http-header-field="h1:fff,h2:yyy"` or `http-header-field="h:fff\\,yyy"` (within a single header multiple values need to be "escaped" using two backslashes). |
| **http-content-encoding** (*deflate\|gzip*; Default: \***empty\***) | Encodes the payload using **gzip** or **deflate** compression and adds a corresponding `Content-Encoding` header. Only applicable to POST and PUT methods |
| **http-max-redirect-count** (*integer*; Default: 2) | Maximum number of HTTP redirects the fetch will follow automatically |
| **http-percent-encoding**(*yes \| no*; Default: **no**) | Enables URL percent‑encoding of the request path |
| **http-version** (*http1\_1* \| *http2*; Default: **http1\_1**) | Chooses the HTTP protocol version. HTTP2 is supported only on ARM64 and x86/CHR devices |
| **idle-timeout** (*time;* Default: 10s) | Idle timeout since last read/write action |
| **ip-type** (*any \| ipv4 \| ipv6;* Default: **any**) | Specify which IP family to prefer when working with domain names |
| **keep-result** (*yes \| no*; Default: **yes**) | When enabled, the fetched data is written to a file |
| **mode** (*ftp\|http\|https\|sftp\|tftp*; Default: **http**) | The protocol used for the connection. Prefer specifying the protocol via the `url` parameter (for example, `url=sftp://ip_address/path` |
| **output** (*none\|file\|user\|user-with-headers*; Default: **file**) | Determines where the fetched data is stored: `none` - do not store downloaded data<code>file</code> - store downloaded data in a file`user` - store downloaded data in the data variable (variable limit is 64Kb)`user-with-headers` - store downloaded data and headers in the data variable (variable limit is 64Kb - 20Kb for downloaded data, 44Kb for headers) |
| **password** (*string*; Default: **anonymous**) |Password for authentication on the remote device |
| **port** (*integer*; Default: ) | Port used for the connection |
| **src-address** (ip address; Default: ) | Source IP address for establishing the connection, applicable only to HTTP/S and SFTP modes |
| **src-path** (*string*; Default: ) | Path of the remote file |
| **upload** (*yes \| no*; Default: **no**) | Enables upload mode for FTP/SFTP transfers, requires `src-path` and `dst-path` |
| **url** (*string*; Default: ) | Full URL of the resource; can replace the separate `address` and `src-path` parameters |
| **user** (*string*; Default: **anonymous**) |Username for authentication on the remote device |

## Configuration Examples

The following example shows how to copy the file with filename "conf.rsc" from a device with ip address 192.168.88.2 by FTP protocol and save it as a file with filename "123.rsc". User and password are needed to log in to the device.

```ros
[admin@MikroTik] /tool> fetch address=192.168.88.2 src-path=conf.rsc user=admin mode=ftp password=123 dst-path=123.rsc port=21 host="" keep-result=yes
```

Example to upload a file to another router:

```ros
[admin@MikroTik] /tool> fetch address=192.168.88.2 src-path=conf.rsc user=admin mode=ftp password=123 dst-path=123.rsc upload=yes
```

Another file download example that demonstrates the usage of the url property.

```ros
[admin@MikroTik] /> /tool/fetch url="https://www.mikrotik.com/img/netaddresses2.pdf" mode=http
  status: finished

[admin@test_host] /> /file/print
 # NAME                     TYPE                  SIZE                 CREATION-TIME
 ...
 5 netaddresses2.pdf        .pdf file             11547                2010-06-01 11:59:51
```

You can run /tool fetch through a specific VRF by appending the VRF name after an “@” symbol:

* In the URL – ```url="http://192.168.88.2@vrf1/…"``` (works for HTTP/HTTPS, not for SFTP).
* In the address property – ```address=192.168.88.2@vrf1```
* As a separate address parameter –  ```address=@vrf1``` combined with a URL that supplies the IP.

Address property can be combined with VRF and separated with "@" (`address=192.168.88.2@vrf1`) or simply as address parameter with "@" symbol before the VRF name as in the example (uses the address from the URL and combines it with the VRF name from the address parameter):

```ros
[admin@MikroTik] /> /tool/fetch url="sftp://192.168.88.2" address=@test src-path=test.txt user=admin password="" upload=yes

  status: finished
```

### Sending information to a remote host

It is possible to use an HTTP POST request to send information to a remote server that is prepared to accept it. In the following example, we send geographic coordinates to a PHP page:

```ros
/tool/fetch http-method=post http-header-field="Content-Type:application/json" http-data="{\"lat\":\"56.12\",\"lon\":\"25.12\"}" url="https://testserver.lv/index.php"    
```

In this example, the data is uploaded as a file. Important note, since variable data comes from a file, a file can only be up to 4KB in size. This is a limitation of RouterOS variables.

```ros
/export file=export.rsc

:global data [/file/get [/file/find name=export.rsc] contents];
:global url "https://prod-51.westeurope.logic.azure.com:443/workflows/blabla/triggers/manual/paths/invoke....";

/tool/fetch mode=https http-method=put http-data=$data url=$url
```

### Return value to a variable

It is possible to save the result of the fetch command to a variable.

#### Example 1

It's possible to trigger a certain action based on the result that an HTTP page returns. You can find a very simple example below that disables **ether2** whenever a PHP page returns "0":

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

#### Example 2

In case fetch fails, it is possible to access the error code ("code") and returned HTTP headers ("http-headers").

```ros
:onerror err,attr in={ /tool/fetch http://127.0.0.1/error as-value} do={:put $err;:put ($attr->"code");:put ($attr->"http-headers")}
failure: Status 404, Not Found
404
Cache-Control: no-store;Connection: Keep-Alive;Content-Length: 99;Content-Type: text/html;Date: Tue, 09 Dec 2025 13:27:44 GMT;Expires: 0;Pragma: no-cache;X-Frame-Options: sameorigin 
```
