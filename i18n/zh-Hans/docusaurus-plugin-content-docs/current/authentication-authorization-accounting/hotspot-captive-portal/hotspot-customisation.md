# Hotspot 自定义

> 通过覆盖路由器 FTP 服务器上存储的默认 HTML 文件，并在 HotSpot 配置文件中通过 'html-directory-override' 指定自定义目录，来自定义 HotSpot 认证页面。可以从预定义页面（如 login.html、status.html 和 logout.html）中选择，或使用 $(username) 和 $(password) 等变量创建自定义页面。

# Hotspot 自定义

#### 简介

您可以为每个 HotSpot 服务器创建一套完全不同的 servlet 页面，方法是在 HotSpot 服务器配置文件 `/ip/hotspot/profile` 的 "html-directory-override" 属性中指定目录。默认的 servlet 页面在您创建服务器配置文件后会被复制到 "hotspot" 目录中。您可以通过 FTP 客户端连接到路由器来访问此目录。您可以复制此目录，并使用本手册本节中的信息根据需要修改页面。请注意，建议手动编辑文件，因为自动化的 HTML 编辑工具可能会通过删除变量或其他关键部分来破坏页面。完成内容修改后，您需要将此修改后的内容上传到热点路由器上的某个自定义目录，并将前面提到的 "html-directory-override" 属性值指向这个新的自定义 HTML 目录的路径。

**注意：** 如果 "html-directory-override" 值的路径缺失或为空，则热点服务器将恢复使用默认的 HTML 文件。

#### 可用页面

向用户显示的主要 HTML servlet 页面：

- **redirect.html** - 将用户重定向到另一个 URL（例如，登录页面）。
- **login.html** - 向用户显示的登录页面，用于请求用户名和密码。此页面可能接受以下参数：
  - **username** - 用户名。
  - **password** - 可以是明文密码（使用 PAP 认证时）或 chap-id 变量、密码和 CHAP 挑战值的 MD5 哈希（使用 CHAP 认证时）。此值用作试用用户的电子邮件地址。
  - **dst** - 重定向前请求的原始 URL。成功登录后将打开此 URL。
  - **popup** - 是否在成功登录时弹出状态窗口。
  - **radius\<id>** - 以文本字符串形式将标识为 \<id> 的属性发送到 RADIUS 服务器（使用 RADIUS 认证时；否则丢失）。
  - **radius\<id>u** - 以无符号整数形式将标识为 \<id> 的属性发送到 RADIUS 服务器（使用 RADIUS 认证时；否则丢失）。
  - **radius\<id>-\<vnd-id>** - 以文本字符串形式将标识为 \<id> 且供应商 ID 为 \<vnd-id> 的属性发送到 RADIUS 服务器（使用 RADIUS 认证时；否则丢失）。
  - **radius\<id>-\<vnd-id>u** - 以无符号整数形式将标识为 \<id> 且供应商 ID 为 \<vnd-id> 的属性发送到 RADIUS 服务器（使用 RADIUS 认证时；否则丢失）。
- **md5.js** - 用于 MD5 密码哈希的 JavaScript。与 http-chap 登录方法一起使用。
- **alogin.html** - 客户端登录后显示的页面。它会弹出状态页面并将浏览器重定向到最初请求的页面（在他/她被重定向到 HotSpot 登录页面之前）。
- **status.html** - 状态页面，显示客户端的统计信息。它还能够自动显示广告。
- **logout.html** - 注销页面，在用户注销后显示。显示关于已结束会话的最终统计信息。此页面可能接受以下附加参数：
  - **erase-cookie** - 是否在注销时从 HotSpot 服务器擦除 cookie（使得下次从同一浏览器无法使用 cookie 登录，在多用户环境中可能有用）。
- **error.html** - 错误页面，仅在发生致命错误时显示。

如果需要更多控制，还可以使用其他一些页面：

- **rlogin.html** - 如果客户端需要授权才能访问某个 URL，则将此页面从其他 URL 重定向客户端到登录页面。
- **rstatus.html** - 类似于 rlogin.html，但仅在客户端已登录且原始 URL 未知的情况下使用。
- **radvert.html** - 将客户端重定向到预定的广告链接。
- **flogin.html** - 如果发生错误（例如，用户名或密码无效），则显示此页面而不是 login.html。
- **fstatus.html** - 如果请求了状态页面但客户端未登录，则显示此页面而不是重定向。
- **flogout.html** - 如果请求了注销页面但客户端未登录，则显示此页面而不是重定向。

#### 提供 Servlet 页面

HotSpot servlet 识别 5 种不同的请求类型：

1. **对远程主机的请求**
   - 如果用户已登录且广告需要显示，则显示 radvert.html。此页面重定向到预定的广告页面。
   - 如果用户已登录且未为此用户安排广告，则提供请求的页面。
   - 如果用户未登录，但目标主机被围墙花园允许，则也提供该请求。
   - 如果用户未登录，且目标主机被围墙花园禁止，则显示 rlogin.html；如果未找到 rlogin.html，则使用 redirect.html 重定向到登录页面。
2. **对 HotSpot 主机上 "/" 的请求**
   - 如果用户已登录，则显示 rstatus.html；如果未找到 rstatus.html，则使用 redirect.html 重定向到状态页面。
   - 如果用户未登录，则显示 rlogin.html；如果未找到 rlogin.html，则使用 redirect.html 重定向到登录页面。
3. **对 "/login" 页面的请求**
   - 如果用户已成功登录（或已登录），则显示 alogin.html；如果未找到 alogin.html，则使用 redirect.html 重定向到最初请求的页面或状态页面（如果未提供原始目标页面）。
   - 如果用户未登录（未提供用户名，未出现错误消息），则显示 login.html。
   - 如果登录过程失败（提供了错误消息），则显示 flogin.html；如果未找到 flogin.html，则使用 login.html。
   - 如果发生致命错误，则显示 error.html。
4. **对 "/status" 页面的请求**
   - 如果用户已登录，则显示 status.html。
   - 如果用户未登录，则显示 fstatus.html；如果未找到 fstatus.html，则使用 redirect.html 重定向到登录页面。
5. **对 '/logout' 页面的请求**
   - 如果用户已登录，则显示 logout.html。
   - 如果用户未登录，则显示 flogout.html；如果未找到 flogout.html，则使用 redirect.html 重定向到登录页面。

**注意：** 如果无法使用路由器 FTP 服务器上存储的页面满足请求，则显示错误 404。

有许多方法可以自定义 HotSpot 认证页面的外观：

- 页面易于修改。它们存储在路由器 FTP 服务器上您为相应 HotSpot 服务器配置文件选择的目录中。
- 通过更改客户端发送到 HotSpot servlet 的变量，可以将关键字数量减少到一个（用户名或密码；例如，客户端的 MAC 地址可以用作另一个值）甚至为零（许可协议；一些对所有用户通用的预定义值或客户端的 MAC 地址可以用作用户名和密码）。
- 注册可能发生在不同的服务器上（例如，能够进行信用卡收费的服务器）。客户端的 MAC 地址可以传递给它，这样就不必手动输入此信息。注册后，服务器应更改 RADIUS 数据库，使客户端能够登录一段时间。

要在 HTML 文件的某个位置插入变量，使用 $(var\_name) 语法，其中 "var\_name" 是变量名（不带引号）。此构造可用于任何作为 '/'、'/login'、'/status' 或 '/logout' 访问的 HotSpot HTML 文件，以及存储在 HotSpot 服务器上的任何文本或 HTML（.txt、.htm 或 .html）文件（流量计数器除外，它们仅在状态页面中可用，以及 **error**、**error-orig**、**chap-id**、**chap-challenge** 和 **popup** 变量，它们仅在登录页面中可用）。例如，要显示指向登录页面的链接，可以使用以下构造：

```
login

```

#### 变量

所有 Servlet HTML 页面都使用变量来显示用户特定的值。变量名仅出现在 servlet 页面的 HTML 源代码中 - 它们由 HotSpot Servlet 自动替换为相应的值。对于大多数变量，括号中包含了其可能值的示例。所有描述的变量在所有 servlet 页面中都有效，但其中一些在访问时可能为空（例如，在用户登录之前没有运行时间）。

##### 可用变量列表

**注意：** 某些变量使用硬编码的 http URL，如果您使用 https，可以通过其他方式构造链接，例如对于 $link-status，您可以使用 https://$(hostname)/$(target-dir)status

**通用服务器变量：**

- **hostname** - HotSpot Servlet 的 DNS 名称或 IP 地址（如果未给出 DNS 名称）（"[hotspot.example.net](http://hotspot.example.net)"）。
- **identity** - RouterOS 身份名称（"MikroTik"）。
- **login-by** - 用户使用的认证方法。
- **plain-passwd** - 是否允许 HTTP-PAP 登录方法的 "是/否" 表示（"no"）。
- **server-address** - HotSpot 服务器地址（"10.5.50.1:80"）。
- **ssl-login** - 是否使用 HTTPS 方法访问该 servlet 页面的 "是/否" 表示（"no"）。
- **server-name** - HotSpot 服务器名称（在 `/ip/hotspot` 菜单中设置为 name 属性）。

**链接：**

- **link-login** - 指向登录页面的链接，包括原始请求的 URL（"[http://10.5.50.1/login?dst=http://www.example.com/](http://10.5.50.1/login?dst=http://www.example.com/)"）
- **link-login-only** - 指向登录页面的链接，不包括原始请求的 URL（"[http://10.5.50.1/login](http://10.5.50.1/login)"）
- **link-logout** - 指向注销页面的链接（"[http://10.5.50.1/logout](http://10.5.50.1/logout)"）
- **link-status** - 指向状态页面的链接（"[http://10.5.50.1/status](http://10.5.50.1/status)"）
- **link-orig** - 原始请求的 URL（"[http://www.example.com/](http://www.example.com/)"）

**通用客户端信息：**

- **domain** - 用户的域名（"[example.com](http://example.com)"）。
- **interface-name** - 物理 HotSpot 接口名称（对于桥接接口，这将返回实际的桥接端口名称）。
- **ip** - 客户端的 IP 地址（"10.5.50.2"）。
- **logged-in** - 如果用户已登录则为 "yes"，否则为 "no"（"yes"）。
- **mac** - 用户的 MAC 地址（"01:23:45:67:89:AB"）。
- **trial** - 用户是否有权访问试用时间的 "是/否" 表示。如果用户的试用时间已过期，则值为 "no"。
- **username** - 用户的名称（"John"）。
- **host-ip** - 来自 `/ip/hotspot/host` 表的客户端 IP 地址。
- **vlan-id** - 表示客户端所连接的 VLAN 接口的 ID。

**用户状态信息：**

- **idle-timeout** - 空闲超时（"20m" 或 "" 如果没有）。
- **idle-timeout-secs** - 以秒为单位的空闲超时（"88" 或 "0" 如果没有此类超时）。
- **limit-bytes-in** - 发送的字节限制（"1000000" 或 "---" 如果没有限制）。
- **limit-bytes-out** - 接收的字节限制（"1000000" 或 "---" 如果没有限制）。
- **refresh-timeout** - 状态页面刷新超时（"1m30s" 或 "" 如果没有）。
- **refresh-timeout-secs** - 以秒为单位的状态页面刷新超时（"90s" 或 "0" 如果没有）。
- **session-timeout** - 用户的剩余会话时间（"5h" 或 "" 如果没有）。
- **session-timeout-secs** - 以秒为单位的用户剩余会话时间（"3475" 或 "0" 如果没有此类超时）。
- **session-time-left** - 用户的剩余会话时间（"5h" 或 "" 如果没有）。
- **session-time-left-secs** - 以秒为单位的用户剩余会话时间（"3475" 或 "0" 如果没有此类超时）。
- **uptime** - 当前会话运行时间（"10h2m33s"）。
- **uptime-secs** - 以秒为单位的当前会话运行时间（"125"）。

**流量计数器，仅在状态页面上可用：**

- **bytes-in** - 从用户接收的字节数（"15423"）。
- **bytes-in-nice** - 从用户接收的字节数的用户友好形式（"15423"）。
- **bytes-out** - 发送给用户的字节数（"11352"）。
- **bytes-out-nice** - 发送给用户的字节数的用户友好形式（"11352"）。
- **packets-in** - 从用户接收的数据包数（"251"）。
- **packets-out** - 发送给用户的数据包数（"211"）。
- **remain-bytes-in** - 达到 limit-bytes-in 之前的剩余字节数（"337465" 或 "---" 如果没有限制）。
- **remain-bytes-out** - 达到 limit-bytes-out 之前的剩余字节数（"124455" 或 "---" 如果没有限制）。

**其他变量：**

- **session-id** - 上次请求中 'session-id' 参数的值。
- **var** - 上次请求中 'var' 参数的值。
- **error** - 错误消息，如果出现问题（"invalid username or password"）。
- **error-orig** - 原始错误消息（没有从 errors.txt 获取的翻译），如果出现问题（"invalid username or password"）。
- **chap-id** - chap ID 的值（"\371"）。
- **chap-challenge** - chap 挑战值的值（"\357\015\330\013\021\234\145\245\303\253\142\246\133\175\375\316"）。
- **popup** - 是否弹出复选框（"true" 或 "false"）。
- **advert-pending** - 是否有待显示的广告（"yes" 或 "no"）。
- **http-status** - 允许设置 http 状态代码和消息。
- **http-header** - 允许设置 http 标头。

**与 RADIUS 相关的变量：**

- **radius\<id>** - 以文本字符串形式显示标识为 \<id> 的属性（使用 RADIUS 认证时；否则为 ""）
- **radius\<id>u** - 以无符号整数形式显示标识为 \<id> 的属性（使用 RADIUS 认证时；否则为 "0"）
- **radius\<id>-\<vnd-id>** - 以文本字符串形式显示标识为 \<id> 且供应商 ID 为 \<vnd-id> 的属性（使用 RADIUS 认证时；否则为 ""）
- **radius\<id>-\<vnd-id>u** - 以无符号整数形式显示标识为 \<id> 且供应商 ID 为 \<vnd-id> 的属性（使用 RADIUS 认证时；否则为 "0"）

##### 使用变量

可以在这些页面中使用 $(if \<var\_name>) 语句。如果 \<var\_name> 的值不是空字符串，则将包含以下内容。它等同于 $(if \<var\_name> != "") 也可以进行等价比较：$(if \<var\_name> == \<value>) 这些语句一直有效，直到 $(elif \<var\_name>)、$(else) 或 $(endif)。在一般情况下，它看起来像这样：

```
some content, which will always be displayed
$(if username == john)
Hey, your username is john
$(elif username == dizzy)
Hello, Dizzy! How are you? Your administrator.
$(elif ip == 10.1.2.3)
You are sitting at that old computer, which is so slow...
$(elif mac == 00:01:02:03:04:05)
This is an ethernet card, which was stolen few months ago...
$(else)
I don't know who you are, so lets live in peace.
$(endif)
other content, which will always be displayed

```

只会显示这些表达式中的一个。显示哪一个取决于每个客户端的这些变量的值。

##### 重定向和自定义标头

```
	$(if http-status == 302)Hotspot login required$(endif)
	$(if http-header == "Location")$(link-redirect)$(endif)

```

**注意：** 尽管上述内容看起来使用了条件表达式 'if'，但实际上是在将 'http-status' 设置为 '302'，而不是测试它。变量 'http-header' 也是如此。再次强调，尽管它使用了 'if'，但实际上是在将变量设置为 'Location'，后跟从变量 'link-redirect' 设置的 URL。

例如，在 $(link-redirect) 计算结果为 "[http://192.168.88.1/login](http://192.168.88.1/login)" 的情况下，返回给客户端的 HTTP 响应将更改为：

```
HTTP/1.0 302 Hotspot login required
<regular HTTP headers>
Location: http://192.168.88.1/login

```

**http-status 语法**：

```
	$(if http-status == XYZ)HTTP_STATUS_MESSAGE$(endif)

```

- *XYZ* - 您希望返回的状态代码。应为 3 位十进制数字，第一位不能为 0。
- *HTTP\_STATUS\_MESSAGE* - 您希望返回给客户端的任何文本，它将在 HTTP 回复中跟随上述状态代码。

在任何 HTTP 响应中，它将位于第一行，如下所示：

```
HTTP/1.0 XYZ HTTP_STATUS_MESSAGE

```

**http-header 语法：**

```
$(if http-header == HTTP_HEADER_NAME)HTTP_HEADER_VALUE$(endif)

```

- *HTTP\_HEADER\_NAME* - 要在响应中发送的 HTTP 标头的名称
- *HTTP\_HEADER\_VALUE* - 要在响应中发送的名为 HTTP\_HEADER\_NAME 的 HTTP 标头的值

HTTP 响应将显示为：

```
HTTP_HEADER_NAME: HTTP_HEADER_VALUE

```

HTTP\_HEADER\_VALUE 和 HTTP\_STATUS\_MESSAGE 中的所有变量和条件表达式都照常处理。

如果添加了多个同名的标头，则只使用最后一个（之前的将被丢弃）。它允许系统覆盖常规 HTTP 标头（例如，Content-Type 和 Cache-Control）。

#### 自定义错误消息

所有错误消息都存储在相应 HotSpot servlet 目录中的 errors.txt 文件中。您可以更改并将所有这些消息翻译成您的母语。为此，请编辑 errors.txt 文件。您也可以在消息中使用变量。所有说明都在该文件中给出。

#### 多个版本的 HotSpot 页面

支持同一 HotSpot 服务器的多个 HotSpot 页面集。用户可以选择它们（例如选择语言），或者通过 JavaScript 自动选择（例如选择 PDA/常规版本的 HTML 页面）。

要利用此功能，请在 HotSpot HTML 目录中创建子目录，并将不同的 HTML 文件放在该子目录中。例如，要将所有内容翻译成拉脱维亚语，可以创建子目录 "lv"，其中包含翻译成拉脱维亚语的 login.html、logout.html、status.html、alogin.html、radvert.html 和 errors.txt 文件。如果在请求的子目录中找不到请求的 HTML 页面，则将使用主目录中相应的 HTML 文件。主 login.html 文件将包含指向 "/lv/login?dst=$(link-orig-esc)" 的链接，然后显示拉脱维亚语版本的登录页面：Latviski。而拉脱维亚语版本将包含指向英语版本的链接：English

引用目录的另一种方法是指定 'target' 变量：

```
        Latviski
        English

```

选择首选目录（例如，"lv"）后，指向本地 HotSpot 页面的所有链接都将包含该路径（例如，$(link-status) = "[http://hotspot.mt.lv/lv/status](http://hotspot.mt.lv/lv/status)"）。因此，如果所有 HotSpot 页面都使用 "$(link-xxx)" 变量引用链接，则无需再进行任何更改 - 每个客户端将始终停留在所选目录中。

#### 其他

如果您想使用 HTTP-CHAP 认证方法，则需要在登录表单的 **Submit 操作** 之前包含 **doLogin()** 函数（该函数引用必须已加载的 **md5.js**）。否则，CHAP 登录将失败。

在使用 HTTP-CHAP 方法的情况下，发送到 HotSpot 网关的最终密码是通过对以下内容的连接进行 MD5 哈希形成的：chap-id、用户密码和 chap-challenge（按给定顺序）

如果要在链接中直接使用变量，则必须相应地转义它们。例如，在登录页面中，如果用户名为 "123&456=1 2"，则 **link** 将无法按预期工作。在这种情况下，应使用 $(user) 的转义版本：$(user-esc)：**link**。现在，相同的用户名将被转换为 "123%26456%3D1+2"，这是 "123&456=1 2" 在 URL 中的有效表示。此技巧可用于任何变量，不仅限于 $(username)。

注销页面有一个布尔参数 "erase-cookie"，可以是 "on" 或 "true"，用于在注销时删除用户 cookie（这样用户下次打开浏览器时就不会自动登录）。

#### 示例

凭借基本的 HTML 语言知识和以下示例，应该很容易实现上述想法：

- 要提供预定义值作为用户名，请在 login.html 中更改：

```
<input type="text" name="username" value="$(username)">

```

为此行：

```
<input type="hidden" name="username" value="hsuser">

```

（其中 hsuser 是您提供的用户名）

- 要提供预定义值作为密码，请在 login.html 中更改。

```
<input type="password">

```

为此行：

```
<input type="hidden" name="password" value="hspass">

```

（其中 hspass 是您提供的密码）

- 要将客户端的 MAC 地址以以下形式发送到注册服务器：

[https://www.example.com/register.html?mac=XX:XX:XX:XX:XX:XX](https://www.example.com/register.html?mac=XX:XX:XX:XX:XX:XX)

将 login.html 中的登录按钮链接更改为：

```
https://www.example.com/register.html?mac=$(mac)

```

（您应该更正链接以指向您的服务器）

- 要在用户登录后显示横幅，请在 alogin.html 中。

$(if popup == 'true') 添加以下行：

```
open('http://www.example.com/your-banner-page.html', 'my-banner-name','');

```

（您应该更正链接以指向您想要显示的页面）

- 要选择登录后显示的不同页面，请在 login.html 中更改：

```
<input type="hidden" name="dst" value="$(link-orig)">

```

为此行：

```
<input type="hidden" name="dst" value="http://www.example.com">

```

（您应该更正链接以指向您的服务器）

- 要在注销时擦除 cookie，请在包含注销链接的页面（例如，status.html）中更改。

```
open('$(link-logout)', 'hotspot_logout', ...

```

为此：

```
open('$(link-logout)?erase-cookie=on', 'hotspot_logout', ...

```

或者添加此行：

```
<input type="hidden" name="erase-cookie" value="on">

```

在此行之前：

```
<input type="submit" value="log off">

```

##### 外部认证

另一个示例是让 HotSpot 在远程服务器上进行认证（例如，该服务器可以执行信用卡收费）：

- 允许在围墙花园中直接访问外部服务器（基于 HTTP 或基于 IP）。
- 修改 HotSpot servlet 的登录页面以重定向到外部认证服务器。外部服务器应根据需要修改 RADIUS 数据库。

以下是要放在 HotSpot 路由器上的此类登录页面的示例（它重定向到 [https://auth.example.com/login.php](https://auth.example.com/login.php)，请将其替换为外部认证服务器的实际地址）：

```
<html>
<title>...</title>
<body>
<form name="redirect" action="https://auth.example.com/login.php" method="post">
<input type="hidden" name="mac" value="$(mac)">
<input type="hidden" name="ip" value="$(ip)">
<input type="hidden" name="username" value="$(username)">
<input type="hidden" name="link-login" value="$(link-login)">
<input type="hidden" name="link-orig" value="$(link-orig)">
<input type="hidden" name="error" value="$(error)">
</form>
<script language="JavaScript">
<!--
	document.redirect.submit();
//-->
</script>
</body>
</html>
          

```

- 外部服务器可以通过将客户端重定向回原始 HotSpot servlet 登录页面（指定正确的用户名和密码）来登录 HotSpot 客户端。

以下是此类页面的示例（它重定向到 [https://hotspot.example.com/login](https://hotspot.example.com/login)，请将其替换为 HotSpot 路由器的实际地址；此外，它在成功登录后显示 [www.mikrotik.com](http://www.mikrotik.com)，请将其替换为所需内容）：

```
<html>
<title>Hotspot login page</title>
<body>
<form name="login" action="https://hotspot.example.com/login" method="post">
<input type="text" name="username" value="demo">
<input type="password" name="password" value="none">
<input type="hidden" name="domain" value="">
<input type="hidden" name="dst" value="http://www.mikrotik.com/">
<input type="submit" name="login" value="log in">
</form>
</body>
</html>
          

```

- Hotspot 将询问 RADIUS 服务器是否允许登录。如果允许，将显示 alogin.html 页面（可以修改它来执行任何操作）。如果不允许，将显示 flogin.html（或 login.html）页面，该页面将客户端重定向回外部认证服务器。

**注意：** 如这些示例所示，可以使用 HTTPS 协议和 POST 方法来保护通信安全。

##### HTTP 标头检测

Hotspot 登录页面可以通过使用 **$(http-header-name);** 来访问 HTTP 标头。

例如，存在检查用户代理（或浏览器）的能力，如果需要，它将返回任何其他内容而不是常规登录页面。例如，这可以用于禁用手机中的自动弹出窗口。

例如，要为特定 Firefox 移动版的用户输出 "SUCCESS" 而不是登录页面，您可以在热点目录中的 **rlogin.html** 页面顶部添加以下行：

```
$(if user-agent == "Mozilla/5.0 (Android; Mobile; rv:40.0) Gecko/40.0 Firefox/40.0" ) 
<HTML><HEAD><TITLE>Success</TITLE></HEAD><BODY>Success</BODY></HTML> 
$(else)
---- regular content of rlogin.html page  ----
$(endif)

```

这将为 Android Firefox 40 用户禁用登录弹出窗口。

##### 一键登录

可以为不需要用户名或密码的场景创建一个修改后的强制门户，用于快速一键登录。

您需要做的是：

- 为此目的创建一个用户。例如，用户名为 "notsosecretuser"，密码为 "notsosecretpass"。
- 将此用户分配给允许特定/无限数量并发活动用户的用户配置文件。
- 复制路由器文件菜单中根级别已生成的原始热点目录。
- 修改此副本目录的内容。
  - 只需修改一个文件即可实现此功能，即 "login.html"。

原始：

```

  login
      <input style={{width: '80px'}} name="username" type="text" value="$(username)"/>
  
  password
      <input style={{width: '80px'}} name="password" type="password"/>
  
   
      <input type="submit" value="OK" />
  

```

修改后：

```

  login
    <input style={{width: '80px'}} name="username" type="text" value="notsosecretuser"/>
  
  password
    <input style={{width: '80px'}} name="password" type="password" value="notsosecretpass"/>
  
   
    <input type="submit" value="Proceed to Internet!" />
  

```

更改内容：

- - - 用户和密码 "" 字段被隐藏。
    - 用户和密码字段值都包含预定义值。
    - 将 "OK" 按钮的值（名称）更改为更合适的名称。

- 现在将此新的热点文件夹上传回路由器，最好使用不同的名称。
- 更改热点服务器配置文件中的设置以使用此新的 html 目录。

```
/ip/hotspot/profile/set (profile number or name) html-directory-override=(dir path/name)

```

### 防火墙自定义

#### 摘要

除了 `/ip/hotspot` 子菜单本身中明显的动态条目（如主机和活动用户）之外，在激活 HotSpot 服务时，防火墙表中还会添加一些额外的规则。

#### NAT

从 **`/ip/firewall/nat/print` dynamic** 命令，您可以获得类似以下内容（每条规则后有注释）：

```
 0 D chain=dstnat action=jump jump-target=hotspot hotspot=from-client

```

将所有来自所有 HotSpot 客户端的数据包的所有 HotSpot 相关任务放入一个单独的链中。

```
 1 I chain=hotspot action=jump jump-target=pre-hotspot

```

任何应在 HotSpot 规则应用之前执行的操作，都应放在 pre-hotspot 链中。此链完全由管理员控制，不包含系统设置的任何规则，因此跳转规则无效（因为该链默认没有任何规则）。

```
 2 D chain=hotspot action=redirect to-ports=64872 dst-port=53 protocol=udp 
 3 D chain=hotspot action=redirect to-ports=64872 dst-port=53 protocol=tcp 

```

将所有 DNS 请求重定向到 HotSpot 服务。64872 端口为所有 HotSpot 用户提供 DNS 服务。如果您希望 HotSpot 服务器监听另一个端口，请在此处以相同方式添加规则，更改 dst-port 属性。

```
 4 D chain=hotspot action=redirect to-ports=64873 hotspot=local-dst dst-port=80
     protocol=tcp

```

将所有 HTTP 登录请求重定向到 HTTP 登录 servlet。64873 是 HotSpot HTTP servlet 端口。

```
 5 D chain=hotspot action=redirect to-ports=64875 hotspot=local-dst dst-port=443
     protocol=tcp

```

将所有 HTTPS 登录请求重定向到 HTTPS 登录 servlet。64875 是 HotSpot HTTPS servlet 端口。

```
 6 D chain=hotspot action=jump jump-target=hs-unauth hotspot=!auth protocol=tcp

```

来自未授权客户端的除 DNS 和登录请求之外的所有其他数据包应通过 hs-unauth 链。

```
 7 D chain=hotspot action=jump jump-target=hs-auth hotspot=auth protocol=tcp

```

来自授权客户端的数据包 - 通过 hs-auth 链。

```
 8 D ;;; www.mikrotik.com
     chain=hs-unauth action=return dst-address=66.228.113.26 dst-port=80 protocol=tcp

```

在 **hs-unauth** 链中，首先放置所有影响 `/ip/hotspot/walled-garden/ip` 子菜单中 TCP 协议的内容（即，所有未设置协议或设置为 TCP 的内容）。这里我们将 [www.mikrotik.com](http://www.mikrotik.com) 排除在重定向到登录页面之外。

```
 9 D chain=hs-unauth action=redirect to-ports=64874 dst-port=80 protocol=tcp

```

所有其他 HTTP 请求都被重定向到监听 64874 端口的围墙花园代理服务器。如果 `/ip/hotspot/walled-garden` 菜单中有针对 HTTP 请求的 "allow" 条目，则将其转发到目的地。否则，请求将自动重定向到 HotSpot 登录 servlet（端口 64873）。

```
10 D chain=hs-unauth action=redirect to-ports=64874 dst-port=3128 protocol=tcp 
11 D chain=hs-unauth action=redirect to-ports=64874 dst-port=8080 protocol=tcp 

```

HotSpot 默认假定只有这些端口可用于 HTTP 代理请求。这两个条目用于"捕获"客户端对未知代理的请求（您可以在此处为其他端口添加更多规则），即，使具有未知代理设置的客户端能够与 HotSpot 系统一起工作。此功能称为"通用代理"。如果检测到客户端正在使用某个代理服务器，系统将自动用 HTTP 热点标记标记这些数据包，以解决未知代理问题，我们稍后将看到。请注意，使用的端口（64874）与规则 #9 中 HTTP 请求的端口相同（因此 HTTP 和 HTTP 代理请求都由同一代码处理）。

```
12 D chain=hs-unauth action=redirect to-ports=64875 dst-port=443 protocol=tcp

```

HTTPS 代理监听 64875 端口。

```
13 I chain=hs-unauth action=jump jump-target=hs-smtp dst-port=25 protocol=tcp

```

SMTP 协议的重定向也可以在 HotSpot 配置中定义。如果是这样，将在 hs-smtp 链中放置一条重定向规则。这样做是为了让具有未知 SMTP 配置的用户能够通过服务提供商（您的）SMTP 服务器发送邮件，而不是使用用户在其计算机上配置的 [可能在其原始网络之外不可用的] SMTP 服务器。该链默认为空，因此跳转规则无效。

```
14 D chain=hs-auth action=redirect to-ports=64874 hotspot=http protocol=tcp

```

为授权用户提供 HTTP 代理服务。经过认证的用户请求可能需要进行透明代理（"通用代理"技术和广告功能）。此 HTTP 标记会自动添加到对 HotSpot HTTP 代理（监听 64874 端口的那个）检测为未知代理服务器的 HTTP 代理请求的数据包上。这样做是为了让具有某些代理设置的用户使用 HotSpot 网关，而不是使用用户在其计算机上配置的 [可能在其原始网络之外不可用的] 代理服务器。当需要向用户显示广告时，以及来自其配置文件配置为透明代理其请求的用户的任何 HTTP 请求，也会应用此标记。

```
15 I chain=hs-auth action=jump jump-target=hs-smtp dst-port=25 protocol=tcp

```

为授权用户提供 SMTP 代理（与规则 #13 相同）。

#### 数据包过滤

从 **`/ip/firewall/filter/print` dynamic** 命令，您可以获得类似以下内容（每条规则后有注释）：

```
 0 D chain=forward action=jump jump-target=hs-unauth hotspot=from-client,!auth

```

任何来自未授权客户端穿越路由器的数据包都将被发送到 **hs-unauth** 链。hs-unauth 实现基于 IP 的围墙花园过滤器。

```
 1 D chain=forward action=jump jump-target=hs-unauth-to hotspot=to-client,!auth

```

所有通过路由器到达客户端的内容都会被重定向到另一个名为 **hs-unauth-to** 的链。此链应拒绝未授权请求到达客户端。

```
 2 D chain=input action=jump jump-target=hs-input hotspot=from-client

```

所有从客户端到达路由器本身的内容都会进入另一个名为 **hs-input** 的链。

```
 3 I chain=hs-input action=jump jump-target=pre-hs-input

```

在处理 [预定义的] 动态规则之前，数据包会到达管理员控制的 **pre-hs-input** 链，该链默认为空，因此跳转规则状态无效。

```
 4 D chain=hs-input action=accept dst-port=64872 protocol=udp 
 5 D chain=hs-input action=accept dst-port=64872-64875 protocol=tcp 

```

允许客户端访问本地认证和代理服务（如前所述）。

```
 6 D chain=hs-input action=jump jump-target=hs-unauth hotspot=!auth

```

来自未授权客户端到路由器本身的所有其他流量将以与穿越路由器的流量相同的方式处理。

```
 7 D chain=hs-unauth action=return protocol=icmp
 8 D ;;; www.mikrotik.com
     chain=hs-unauth action=return dst-address=66.228.113.26 dst-port=80 protocol=tcp

```

与 NAT 表中仅添加与 TCP 协议相关的围墙花园条目不同，在数据包过滤器中，**hs-unauth** 链被添加到您在 `/ip/hotspot/walled-garden/ip` 菜单中设置的所有内容。这就是为什么虽然您在 NAT 表中只看到一个条目，但这里有两个规则。

```
 9 D chain=hs-unauth action=reject