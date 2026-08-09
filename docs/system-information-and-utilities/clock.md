# Clock

> The page describes MikroTik RouterOS clock configuration, detailing time zone settings including automatic detection and manual adjustments, GMT offsets, daylight saving rules, and warnings about internal clock reliability.

# Clock

RouterOS uses data from the TZ database. Most of the time zones from this database are included, and have the same names. Because local time on the router is used mostly for timestamping and time-dependent configuration, and not for historical date calculations, time zone information about past years is not included. Currently, only information starting from 2005 is included.

The following settings are available in the `/system/clock` console path and in the "Time" tab of the "System > Clock" WinBox window.

Startup date and time is **1970-01-02 00:00:00** [+|-]gmt-offset.

## Properties

| Property | Description |
| :-- | :-- |
| **time** (*HH:MM:SS);* | where *HH* - hour 00..23, *MM* - minutes 00..59, *SS* - seconds 00..59. |
| **date** (*YYYY-MM-DD);* | where *YYYY* - year, 1970..2037, *MM* - month, 01..12, *DD* - date, 01..31: **date** and **time** show current local time on the router. These values can be adjusted using the **set** command. Local time cannot, however, be exported, and is not stored with the rest of the configuration. |
| **time-zone-name** (*manual*, or name of time zone; default value: *manual*); | Name of the time zone. As with most of the text values in RouterOS, this value is case sensitive. Special value *manual* applies manually configured GMT offset, which by default is *00:00* with no daylight saving time. |
| **time-zone-autodetect** (*yes* or *no*; default: yes); | Feature available from v6.27. If enabled, the time zone will be set automatically. |

:::warning
Time-zone-autodetect by default is enabled on a new RouterOS installation and after configuration reset. The time zone is detected depending on the router's public IP address and our Cloud servers database. Since RouterOS v6.43 your device will use cloud2.mikrotik.com to communicate with MikroTik's Cloud server. Older versions will use cloud.mikrotik.com to communicate with MikroTik's Cloud server.

**Important:** Be aware that the router's internal CPU clock is not a reliable time source for precise timing operations, as its frequency may vary due to power management, thermal conditions, and hardware differences, even between identical models. This variation is expected and does not affect normal router performance. For accurate timekeeping, it is recommended to use network-based time synchronisation, such as NTP (Network Time Protocol).
:::

Configuration

### Active time zone information

- **dst-active** (*yes* or *no*; read-only property): This property has the value *yes* while daylight saving time of the current time zone is active.
- **gmt-offset** ([*+*|*-*]*HH:MM* - offset in hours and minutes; read-only property): This is the current value of GMT offset used by the system, after applying base time zone offset and active daylight saving time offset.

### Manual time zone configuration

These settings are available in the `/system/clock/manual` console path and in the "Manual Time Zone" tab of the "System > Clock" WinBox window. These settings have an effect only when **time-zone-name**=*manual*. It is only possible to manually configure a single daylight saving time period.

- **time-zone**, **dst-delta** ([*+*|*-*]*HH:MM* - time offset in hours and minutes, leading plus sign is optional; default value: *+00:00*) : While DST is not active, use GMT offset **time-zone**. While DST is active, use GMT offset **time-zone** + **dst-delta**.
- **dst-start**, **dst-end** (*YYYY-MM-DD HH:MM:SS* - date and time, either date or time can be omitted in the **set** command; default value: *1970-01-01 00:00:00*): Local time when DST starts and ends.
