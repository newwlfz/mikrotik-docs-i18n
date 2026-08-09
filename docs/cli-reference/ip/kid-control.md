# Kid Control

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/kid-control

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="P" typ="paused">paused</ArgTableRow>
<ArgTableRow arg="B" typ="blocked">blocked</ArgTableRow>
<ArgTableRow arg="L" typ="rate-limited">rate-limited</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
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
 }">time with unlimited rate on Sunday</ArgTableRow>
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

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="pause-left" typ="time"></ArgTableRow>
<ArgTableRow arg="pause-till" typ="date"></ArgTableRow>
</ArgTable>

### ip/kid-control/device

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="B" typ="blocked">blocked</ArgTableRow>
<ArgTableRow arg="L" typ="limited">limited</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="all" typ="switch"></ArgTableRow>
<ArgTableRow arg="static" typ="switch"></ArgTableRow>
<ArgTableRow arg="dynamic" typ="switch"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr" mandatory="1"></ArgTableRow>
<ArgTableRow arg="user" typ="enum ()" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
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

**Type:** Command

### ip/kid-control/pause

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="duration" typ="time"></ArgTableRow>
<ArgTableRow arg="till" typ="date"></ArgTableRow>
</ArgTable>

### ip/kid-control/resume

**Type:** Command
