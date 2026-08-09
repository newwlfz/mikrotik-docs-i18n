# SNMP 获取

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/snmp-get

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="oid" typ="对象 { 字符串
 }"></ArgTableRow>
<ArgTableRow arg="next" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="address" typ="IP地址"></ArgTableRow>
<ArgTableRow arg="port" typ="数字"></ArgTableRow>
<ArgTableRow arg="tries" typ="数字"></ArgTableRow>
<ArgTableRow arg="try-timeout" typ="时间"></ArgTableRow>
<ArgTableRow arg="version" typ="枚举 (1 | 2c | 3)"></ArgTableRow>
<ArgTableRow arg="community" typ="字符串"></ArgTableRow>
<ArgTableRow arg="security" typ="枚举 (无 | 授权 | 私有)"></ArgTableRow>
<ArgTableRow arg="authentication-password" typ="字符串"></ArgTableRow>
<ArgTableRow arg="authentication-protocol" typ="枚举 (MD5 | SHA1)"></ArgTableRow>
<ArgTableRow arg="encryption-password" typ="字符串"></ArgTableRow>
<ArgTableRow arg="encryption-protocol" typ="枚举 (DES | AES)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="oid" typ="字符串"></ArgTableRow>
<ArgTableRow arg="type" typ="枚举 (空 | 整数 | 计数器 | 计量器 | 时间刻度 | 无符号整数 | 八位字节字符串 | 不透明 | 对象标识符 | IP地址 | 64位计数器 | 无此对象 | 无此实例 | 视图末尾)"></ArgTableRow>
<ArgTableRow arg="value" typ="字符串"></ArgTableRow>
</ArgTable>