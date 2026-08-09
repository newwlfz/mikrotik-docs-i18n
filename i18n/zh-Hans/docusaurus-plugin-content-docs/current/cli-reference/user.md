# user

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="E" typ="expired">已过期</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="group" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="password" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="inactivity-timeout" typ="time">不活动策略生效前等待的时间段</ArgTableRow>
<ArgTableRow arg="inactivity-policy" typ="enum (none | logout | lockscreen)">指定不活动超时后采取的操作</ArgTableRow>
<ArgTableRow arg="address" typ="object { alt { ipPrefix
, ip6Prefix
 } { ipPrefix
, ip6Prefix
 }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="last-logged-in" typ="date"></ArgTableRow>
</ArgTable>

## user/aaa

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="use-radius" typ="bool"></ArgTableRow>
<ArgTableRow arg="accounting" typ="bool"></ArgTableRow>
<ArgTableRow arg="interim-update" typ="time"></ArgTableRow>
<ArgTableRow arg="default-group" typ="enum"></ArgTableRow>
<ArgTableRow arg="exclude-groups" typ="multi { , enum
 }"></ArgTableRow>
</ArgTable>

## user/active

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="R" typ="radius">radius</ArgTableRow>
<ArgTableRow arg="M" typ="by-romon">by-romon</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="when" typ="date"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="address" typ="alt { ipAddr
, ip6Addr
, macAddr
 }"></ArgTableRow>
<ArgTableRow arg="by-romon" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="via" typ="enum (unknown | winbox | console | telnet | ftp | web | ssh | mac-telnet | bandwidth-test | api | romon | rest-api)"></ArgTableRow>
<ArgTableRow arg="group" typ="enum"></ArgTableRow>
</ArgTable>

## user/expire-password

**类型：** 命令

## user/group

**类型：** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="policy" typ="multi { array-id, array-id, super { !
, enum
 } { !
, enum
 }
 }"></ArgTableRow>
<ArgTableRow arg="skin" typ="enum"></ArgTableRow>
</ArgTable>

## user/settings

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="minimum-password-length" typ="num"></ArgTableRow>
<ArgTableRow arg="minimum-categories" typ="num"></ArgTableRow>
</ArgTable>

## user/ssh-keys

**软件包：** security
**类型：** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="user" typ="enum"></ArgTableRow>
<ArgTableRow arg="key" typ="string">仅用于添加新密钥</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="key-type" typ="enum (rsa | ed25519 | ed25519-sk)"></ArgTableRow>
<ArgTableRow arg="bits" typ="num"></ArgTableRow>
<ArgTableRow arg="info" typ="string"></ArgTableRow>
<ArgTableRow arg="fingerprint" typ="string"></ArgTableRow>
</ArgTable>

### user/ssh-keys/import

**软件包：** security
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="public-key-file" typ="file"></ArgTableRow>
<ArgTableRow arg="user" typ="enum"></ArgTableRow>
<ArgTableRow arg="info" typ="string"></ArgTableRow>
</ArgTable>

### user/ssh-keys/private

**软件包：** security
**类型：** 目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="user" typ="enum"></ArgTableRow>
<ArgTableRow arg="key-type" typ="enum (rsa | ed25519)"></ArgTableRow>
<ArgTableRow arg="bits" typ="num"></ArgTableRow>
<ArgTableRow arg="info" typ="string"></ArgTableRow>
</ArgTable>

#### user/ssh-keys/private/import

**软件包：** security
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="private-key-file" typ="file"></ArgTableRow>
<ArgTableRow arg="user" typ="enum"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string"></ArgTableRow>
<ArgTableRow arg="info" typ="string"></ArgTableRow>
</ArgTable>