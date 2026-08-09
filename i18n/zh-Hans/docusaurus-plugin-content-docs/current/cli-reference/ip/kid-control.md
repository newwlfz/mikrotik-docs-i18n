# 儿童控制

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/kid-control

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="P" typ="paused">已暂停</ArgTableRow>
<ArgTableRow arg="B" typ="blocked">已阻止</ArgTableRow>
<ArgTableRow arg="L" typ="rate-limited">限速中</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="sun" typ="multi { , , composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="mon" typ="multi { , , composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="tue" typ="multi { , , composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="wed" typ="multi { , , composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="thu" typ="multi { , , composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="fri" typ="multi { , , composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="sat" typ="multi { , , composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string"></ArgTableRow>
<ArgTableRow arg="tur-sun" typ="multi { , , composite { ,  } { ,  }
 }">星期日不限速的时间段</ArgTableRow>
<ArgTableRow arg="tur-mon" typ="multi { , , composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="tur-tue" typ="multi { , , composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="tur-wed" typ="multi { , , composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="tur-thu" typ="multi { , , composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="tur-fri" typ="multi { , , composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="tur-sat" typ="multi { , , composite { ,  } { ,  }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="pause-left" typ="time"></ArgTableRow>
<ArgTableRow arg="pause-till" typ="date"></ArgTableRow>
</ArgTable>

### ip/kid-control/device

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="B" typ="blocked">已阻止</ArgTableRow>
<ArgTableRow arg="L" typ="limited">受限</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="all" typ="switch"></ArgTableRow>
<ArgTableRow arg="static" typ="switch"></ArgTableRow>
<ArgTableRow arg="dynamic" typ="switch"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr" mandatory="1"></ArgTableRow>
<ArgTableRow arg="user" typ="enum ()" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="ip-address" typ="object { alt { ipAddr
, ip6Addr
 } { ipAddr
, ip6Addr
 }
 }"></ArgTableRow>
<ArgTableRow arg="activity" typ="string"></ArgTableRow>
<ArgTableRow arg="rate-down" typ="num"></ArgTableRow>
<ArgTableRow arg="rate-up" typ="num"></ArgTableRow>
<ArgTableRow arg="bytes-down" typ="num"></ArgTableRow>
<ArgTableRow arg="bytes-up" typ="num"></ArgTableRow>
<ArgTableRow arg="idle-time" typ="time"></ArgTableRow>
</ArgTable>

#### ip/kid-control/device/reset-counters

**类型：** 命令

### ip/kid-control/pause

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="duration" typ="time"></ArgTableRow>
<ArgTableRow arg="till" typ="date"></ArgTableRow>
</ArgTable>

### ip/kid-control/resume

**类型：** 命令