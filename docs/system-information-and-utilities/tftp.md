# TFTP

> The TFTP page describes MikroTik RouterOS's implementation of the Trivial File Transfer Protocol, detailing configuration options for TFTP server access rules including IP address ranges, filename handling, block size limits, and regular expression support for client requests.

# TFTP

Trivial File Transfer Protocol or simply TFTP is a very simple protocol used to transfer files. Each nonterminal packet is acknowledged separately.

**Sub-menu:** `/ip/tftp`

This menu contains all TFTP access rules. If there are no rules in this menu, the TFTP server is not started when RouterOS boots. This menu only shows 1 additional attribute compared to what you can set when creating a rule.

## Parameters

| Property | Description |
| :-- | :-- |
| **ip-addresses** *(required)* | Range of IP addresses accepted as clients. If empty *0.0.0.0/0* will be used |
| **allow-rollover** *(Default: No)* | If set to *yes*, TFTP server will allow the sequence number to roll over when the maximum value is reached. This is used to enable large downloads using the TFTP server. |
| **req-filename** | Requested filename as a *regular expression (regex)*. If a field is left empty, it defaults to *.\** |
| **real-filename** | If **req-filename** and **real-filename** values are set and valid, the requested filename will be replaced with the matched file. This field has to be set. If multiple *regex* are specified in *req-filename*, with this field you can set which ones should match, so this rule is validated. The *real-filename* format for using multiple *regex* is **filename\0\5\6** |
| **allow** (*default: yes*) | To allow a connection if the above fields are set. If *no*, a connection will be interrupted |
| **read-only** (*default: no*) | Sets if a file can be written to, if set to "yes", a write attempt will fail with an error |
| **hits** *(read-only)* | How many times this access rule entry has been used (read-only) |

### Settings

**Sub-menu:** `/ip/tftp/settings`

This menu contains all TFTP settings.

| Property | Description |
| :-- | :-- |
| **max-block-size** (*default:4096*) | Maximum accepted block size value. During the transfer negotiation phase, the RouterOS device will not negotiate a larger value than this. |

## Regexp

Req-filename field allows regexp, the allowed regexp in this field are:

### brackets () - marking subsection

```
    example 1 a(sd|fg) will match asd or afg

```

### asterisk "\*" - match zero or more times preceding symbol

```
    example 1 a* will match any length name consisting purely of symbols a or no symbols at all
    example 2 .* will match any length name, also, empty field
    example 3 as*df will match adf, asdf, assdf, asssdf etc.

```

### plus "+" will match one or more times the preceding symbol

```
    example: as+df will match asdf, assdf etc.

```

### dot "." - matches any symbol

```
    example as.f will match asdf, asbf ashf etc.

```

### square brackets [] - variation between

```
    example as[df] will match asd and asf

```

### question mark "?" will match one or no symbols

```
    example asd?f will match asdf and asf

```

### caret "^" - used at the beginning of the line means that the line starts with

### dollar "$" - means at the end of the line

## Examples

If a file is requested, return the file from the store called sata1:

```ros
/ip/tftp/add req-filename=file.txt real-filename=/sata1/file.txt allow=yes read-only=yes
```

If we want to give out one specific *file* no matter what the user is requesting:

```ros
/ip/tftp/add req-filename=.* real-filename=/sata1/file.txt allow=yes read-only=yes
```

 If the user requests *aaa.bin* or *bbb.bin* then give them *ccc.bin*:

```ros
/ip/tftp/add req-filename="(aaa.bin)|(bbb.bin)" real-filename="/sata1/ccc.bin\\0" allow=yes read-only=yes
```

:::tip

RouterOS receives TFTP requests, but the client gets a transfer timeout?

Some embedded clients request large block sizes and yet do not handle fragmented packets correctly. For these clients, it is recommended to set "max-block-size" on the RouterOS side or "blksize" on the client side to the value of the smallest MTU on your network minus 32 bytes (20 bytes for IP, 8 for UDP, and 4 for TFTP) and more if you use IP options on your network.

:::
