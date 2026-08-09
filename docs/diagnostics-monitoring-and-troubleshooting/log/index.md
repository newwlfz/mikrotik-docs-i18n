# Log

> This section provides an overview of MikroTik RouterOS logging capabilities, covering how to view and filter log messages in real-time using the `/log` menu, along with detailed configuration options for forwarding logs to external systems via `/system/logging`.

import DocCardList from '@theme/DocCardList';

# Log

This section covers log export and integration examples. Use it to forward RouterOS logs to external systems such as Elasticsearch.

<DocCardList />

RouterOS is capable of logging various system events and status information. Logs can be saved in router memory (RAM), disk, file, sent by email or even sent to a remote syslog server.

[Video: Logging Basics](http://youtube.com/watch?v=E-QAhaWtsnU)

## Log messages

**Sub-menu:** `/log`

All messages stored in router's local memory can be printed from the `/log` menu. Each entry contains time and date when the event occurred, topics that this message belongs to and the message itself.

```ros
[admin@MikroTik] /log> print 
1970-01-02 02:00:09 system,info router rebooted 
sep/15 09:54:33 system,info,account user admin logged in from 10.1.101.212 via winbox 
sep/15 12:33:18 system,info item added by admin 
sep/15 12:34:26 system,info mangle rule added by admin 
sep/15 12:34:29 system,info mangle rule moved by admin 
sep/15 12:35:34 system,info mangle rule changed by admin 
sep/15 12:42:14 system,info,account user admin logged in from 10.1.101.212 via telnet 
sep/15 12:42:55 system,info,account user admin logged out from 10.1.101.212 via telnet 
01:01:58 firewall,info input: in:ether1 out:(none), src-mac 00:21:29:6d:82:07, proto UDP, 
10.1.101.1:520->10.1.101.255:520, len 452
```

If logs are printed on the same date when the log entry was added, then only the time will be shown. In the example above you can see that the second message was added on sep/15 of the current year (year is not added) and the last message was added today so only the time is displayed.

*Print* command accepts several parameters that allow to detect new log entries, print only necessary messages and so on.

For example, the following command will print all log messages where one of the topics is info and will detect new log entries until <kbd>Control</kbd>+<kbd>C</kbd> is pressed.

```ros
[admin@MikroTik] /log > print follow where topics~".info"
12:52:24 script,info hello from script
-- Ctrl-C to quit.
```

In this example it will print only the dhcp info messages:

```ros
[admin@MikroTik] /log/print where topics~"dhcp.info"
11:42:32 dhcp,info defconf deassigned 192.168.88.37 for B0:E4:5C:27:EF:F2 Samsung
11:42:32 dhcp,info defconf assigned 192.168.88.37 for B0:E4:5C:27:EF:F2 Samsung
```

If print is in follow mode you can hit 'space' on the keyboard to insert a separator:

```ros
[admin@MikroTik] /log > print follow where topics~".info"
12:52:24 script,info hello from script

= = = = = = = = = = = = = = = = = = = = = = = = = = =

-- Ctrl-C to quit.
```

## Logging configuration

**Sub-menu:** `/system/logging`

| Property | Description |
| :--- | :--- |
| **action** (*name*; Default: **memory**) | Specifies one of the system default actions or a user-defined action listed in the actions menu. |
| **prefix** (*string*; Default: none) | Prefix added at the beginning of log messages. |
| **regex** (*string*; Default: none) | Regular expression used to match log messages. If the regex does not match, the action is not performed, even if the topic is configured for logging. |
| **topics** (*account, acme-client, amt, async, backup, bfd, bgp, bridge, calc, caps, certificate, clock, container, critical, ddns, debug, dhcp, discover, disk, dns, dot1x, dude, e-mail, error, event, evpn, fetch, firewall, gps, gsm, health, hotspot, igmp-proxy, info, interface, ipsec, iscsi, isdn, isis, kvm, l2tp, lora, ldp, lte, manager, mme, mpls, mqtt, mvrp, natpmp, netwatch, ntp, ospf, ovpn, packet, pim, poe-in, poe-out, ppp, pppoe, pptp, ptp, queue, radvd, radius, raw, read, rip, route, rpki, rproxy, rsvp, script, sertcp, simulator, smb, snmp, socksify, ssh, ssld, sstp, state, store, stp, system, telephony, tftp, timer, tr069, update, upnp, ups, vpls, vrrp, warning, watchdog, web-proxy, wiliot, wireguard, wireless, write, zerotier*; Default: **info**) | Logs all messages that match the specified topic or list of topics.Use the **!** character before a topic to exclude matching messages. For example, to log NTP debug messages without packet details:`/system/logging/add topics=ntp,debug,!packet` |

### Actions

**Sub-menu:** `/system/logging/action`

| Property | Description |
| :--- | :--- |
| **add-topics-string** (*yes\|no*; Default: **no**) |  |
| **cef-event-delimiter** (string; Default: **\r\n**) | option helps remote syslog to distinguish between individual events within a sent batch |
| **check-certificate** (*yes\|no*; Default: no) | Whether to check the server certificate when using TLS type of logging for remote action. |
| **disk-file-count** (*integer [1..65535]*; Default: **2**) | specifies the number of files used to store log messages, applicable only if action=disk |
| **disk-file-name** (*string*; Default: **log**) | name of the file used to store log messages, applicable only if action=disk |
| **disk-lines-per-file** (*integer [1..65535]*; Default: **100**) | specifies the maximum size of the file in lines, applicable only if action=disk |
| **disk-stop-on-full** (*yes\|no*; Default: **no**) | whether to stop saving log messages to disk after the specified disk-lines-per-file and disk-file-count number is reached, applicable only if action=disk |
| **email-cc (*string*; Default: )** | email address where logs are sent as CC, applicable only if action=email |
| **email-start-tls** (*yes \| no*; Default: **no**) | Whether to use tls when sending email, applicable only if action=email |
| **email-to** (*string*; Default: ) | email address where logs are sent, applicable only if action=email |
| **memory-lines** (*integer [1..65535]*; Default: **1000**) | number of records in local memory buffer, applicable only if action=memory |
| **memory-stop-on-full** (*yes\|no*; Default: **no**) | whether to stop saving log messages in local buffer after the specified memory-lines number is reached |
| **name** (*string*; Default: ) | name of an action. When target=memory, this name also serves as the identifier for a specific memory buffer. Multiple actions with target=memory can be created, each storing logs in its own separate buffer. |
| **remember** (*yes\|no*; Default: ) | whether to keep log messages, which have not yet been displayed in console, applicable if action=echo |
| **remote-log-format** (*cef, default, syslog*; Default: **default**) | Format for logs to be sent to remote instance: cef - logs are sent in CEF format;default - logs are sent as it is;syslog - logs are sent in BSD-syslog format |
| **remote-port** (*integer [1..65535]*; Default: **514**) | Remote logging server's UDP port (address is configured via the **remote** property). |
| **remote-protocol** (*tcp / udp / tls*; Default: **udp**) | protocol for remote logging messages, TCP and TLS only work with CEF remote-log-format, for syslog it will always use UDP, even if TCP / TLS is set |
| **script** |  |
| **src-address** (*IP address*; Default: **0.0.0.0**) | source address used when sending packets to remote server |
| **syslog-facility** (*auth, authpriv, cron, daemon, ftp, kern, local0, local1, local2, local3, local4, local5, local6, local7, lpr, mail, news, ntp, syslog, user, uucp*; Default: **daemon**) |  |
| **syslog-severity** (*alert, auto, critical, debug, emergency, error, info, notice, warning*; Default: **auto**) | Severity level indicator defined in RFC 3164:Emergency: system is unusableAlert: action must be taken immediatelyCritical: critical conditionsError: error conditionsWarning: warning conditionsNotice: normal but significant conditionInformational: informational messagesDebug: debug-level messages |
| **syslog-time-format** (*bsd-syslog, iso8601*; Default: **bsd-syslog**) | Time log format for messages |
| **target** (*disk, echo, email, memory, remote, script*; Default: **memory**) | Storage facility or target of log messagesdisk - logs are saved to the hard driveecho - logs are displayed on the console screenemail - logs are sent by emailmemory - logs are stored in local memory buffer or multiple separate buffers (RAM files). remote - logs are sent to remote hostscript -     executes a script from /system/script/ when a log message matches the rule. The script receives two variables: topics (log topic string) and message (log message content). |
| **vrf** (*name*; Default: **main**) | Set VRF on which the remote logging is making outgoing connections, applicable only if target=remote. The setting is available since RouterOS version 7.19. |

### Create separate memory logging buffers

Just like having different text files for different notes, these separate memory buffers allow you to direct specific types of log messages (based on topics) into distinct storage areas in memory.

- **Isolation:** Logs sent to `buffer_A` are completely separate from logs sent to `buffer_B`.
- **Independent Viewing:** You can view the contents of just one buffer at a time using `/log/print where buffer=buffer_name`.
- **Targeted Clearing:** You can clear the contents of one specific buffer using `/system/logging/action/clear action=buffer_name` without affecting the logs stored in any other memory buffer.

This provides much better organization and control over logs stored in memory, especially for debugging or monitoring, without mixing them all into the single default memory log.

**Sub-menu:** `/system/logging/action/clear`

Starting from 7.20\_ab244, memory logs (target=memory) can be cleared with command: **`/system/logging/action/clear` action=\<`logging` action name>**  
  
Topics

 Each log entry has a topic which describes the origin of the log message. There can be more than one topic assigned to the log message. For example, OSPF debug logs have four different topics: route, ospf, debug and raw.

```ros
11:11:43 route,ospf,debug SEND: Hello Packet 10.255.255.1 -> 224.0.0.5 on lo0 
11:11:43 route,ospf,debug,raw PACKET: 
11:11:43 route,ospf,debug,raw 02 01 00 2C 0A FF FF 03 00 00 00 00 E7 9B 00 00 
11:11:43 route,ospf,debug,raw 00 00 00 00 00 00 00 00 FF FF FF FF 00 0A 02 01 
11:11:43 route,ospf,debug,raw 00 00 00 28 0A FF FF 01 00 00 00 00 
```

#### List of Facility independent topics

| Topic | Description |
| :-- | :-- |
| **critical** | Log entries marked as critical; these log entries are printed to the console each time you log in. |
| **debug** | Debug log entries |
| **error** | Error messages |
| **info** | Informative log entry |
| **packet** | Log entry that shows contents from a received/sent packet |
| **raw** | Log entry that shows raw contents of a received/sent packet |
| **warning** | Warning message. |

#### Topics used by various RouterOS facilities

| Topic | Description |
| :-- | :-- |
| **account** | Log messages generated by accounting facility. |
| **async** | Log messages generated by asynchronous devices |
| **backup** | Log messages generated by backup creation facility. |
| **bfd** | Log messages generated by BFD protocol |
| **bgp** | Log messages generated by BGP protocol |
| **calc** | Routing calculation log messages. |
| **caps** | CAPsMAN wireless device management |
| **certificate** | Security certificate |
| **clock** | Log messages generated by Clock, IP Cloud time changes. |
| **dns** | Name server lookup related information |
| **ddns** | Log messages generated by Dynamic DNS tool |
| **dude** | Messages related to the Dude server package and The Dude tool |
| **dhcp** | DHCP client, server and relay log messages |
| **e-mail** | Messages generated by e-mail tool. |
| **event** | Log message generated at a routing event. For example, new route has been installed in the routing table. |
| **firewall** | Firewall log messages generated when **action=log** is set in firewall rule |
| **gsm** | Log messages generated by GSM devices |
| **hotspot** | Hotspot related log entries |
| **igmp-proxy** | IGMP Proxy related log entries |
| **ipsec** | IPSec log entries |
| **iscsi** |  |
| **isdn** |  |
| **interface** |  |
| **kvm** | Messages related to the KVM virtual machine functionality |
| **l2tp** | Log entries generated by L2TP client and server |
| **lte** | Messages related to the LTE/4G modem configuration |
| **ldp** | LDP protocol related messages |
| **manager** | User Manager log messages. |
| **mme** | MME routing protocol messages |
| **mpls** | MPLS messages |
| **ntp** | sNTP client generated log entries |
| **ospf** | OSPF routing protocol messages |
| **ovpn** | OpenVPN tunnel messages |
| **pim** | Multicast PIM-SM related messages |
| **ppp** | ppp facility messages |
| **pppoe** | PPPoE server/client related messages |
| **pptp** | PPTP server/client related messages |
| **radius** | Log entries generated by RADIUS Client |
| **radvd** | IPv6 radv daemon log messages. |
| **read** | SMS tool messages |
| **rip** | RIP routing protocol messages |
| **route** | Routing facility log entries |
| **rsvp** | Resource Reservation Protocol generated messages. |
| **script** | Log entries generated from scripts |
| **sertcp** | Log messages related to the facility responsible for "/port remote-access" |
| **simulator** |  |
| **state** | DHCP Client and routing state messages. |
| **store** | Log entries generated by Store facility |
| **smb** | Messages related to the SMB file sharing system |
| **snmp** | Messages related to Simple network management protocol (SNMP) configuration |
| **system** | Generic system messages |
| **telephony** | *Obsolete! Previously used by the IP telephony package* |
| **tftp** | TFTP server generated messages |
| **timer** | Log messages that are related to timers used in RouterOS. For example bgp keepalive logs`12:41:40 route,bgp,debug,timer KeepaliveTimer expired``12:41:40 route,bgp,debug,timer     RemoteAddress=2001:470:1f09:131::1` |
| **ups** | Messages generated by UPS monitoring tool |
| **vrrp** | Messages generated by VRRP |
| **watchdog** | Watchdog generated log entries |
| **web-proxy** | Log messages generated by web proxy |
| **wireless** | Wireless log entries. |
| **write** | SMS tool messages. |

## Examples

### Create separate memory logging buffers

Create new memory logging buffers, which will store specified logs separately from default memory logs.

```ros
/system/logging/action/add name=dhcpMemoryLog target=memory memory-lines=300
/system/logging/action/add name=wirelessLog target=memory memory-lines=500
```

Assign topics to created buffers. This rule sends all DHCP logs to dhcpMemoryLog, and wireless logs to wirelessLog buffer.

```ros
/system/logging/add topics=dhcp action=dhcpMemoryLog
/system/logging/add topics=wireless action=wirelessLog
```

```ros
# View only DHCP related logs stored in its dedicated buffer
/log/print where buffer=dhcpMemoryLog

# View only non-info Wireless logs stored in its dedicated buffer
/log/print where buffer=wirelessLog
```

```ros
/system/logging/action/clear action=dhcpMemoryLog
```

### Logging to file

To log everything to a file, add a new log action:

```ros
/system/logging/action/add name=file target=disk disk-file-name=log
```

and then make everything log using this new action:

```ros
/system/logging/add action=file
```

You can log only errors there by issuing the command:

```ros
/system/logging/add topics=error action=file 
```

This will log into files **log.0.txt** and **log.1.txt**.

You can specify the maximum size of the file in lines by specifying *disk-lines-per-file*. **\<file>.0.txt** is the active file where new logs are going to be appended and once its size will reach the maximum it will become **\<file>.1.txt**, and new empty **\<file>.0.txt** will be created.

You can log into USB flashes or into *MicroSD/CF* (on Routerboards) by specifying its directory name before file name. For example, if you have accessible usb flash as **usb1** directory under */files*, you should issue the following command:

```ros
/system/logging/action/add name=usb target=disk disk-file-name=usb1/log
```

:::warning
Logging entries from files will be stored back in memory after reboot.
:::
