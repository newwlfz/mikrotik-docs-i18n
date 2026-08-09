# E-mail

> The E-mail tool in RouterOS enables sending emails directly from the device using SMTP with plain authentication or TLS encryption, supporting scheduled backups and customizable email content. It allows configuration of SMTP servers, authentication details, encryption settings, and attachment handling through the `/tool/e-mail` submenu.

# E-mail

The E-mail tool is a built-in RouterOS utility that enables the router to send e-mail messages directly from the device. It can be used to automate delivery of configuration backups and exports to a network administrator on a scheduled basis.

The E-mail tool supports plain authentication and TLS encryption. No other authentication or encryption methods are supported.

## Properties

**Sub-menu:** `/tool/e-mail`

This submenu allows setting an SMTP server that will be used.

| Property | Description |
| :-- | :-- |
| **address** (*IP/IPv6 address*; Default: **0.0.0.0**) | SMTP server's IP address. |
| **certificate-verification**(*yes* \| *yes-without-crl* \| *no*; Default: **no**) | Enables trust chain validation from the local certificate store. *yes-without-crl* validates a certificate, not performing a CRL check (certificate revocation list). |
| **from** (*string*; Default: **\<>**) | Name or email address that will be shown as the sender. |
| **password** (*string*; Default: **""**) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | Password used for authenticating to an SMTP server. |
| **port** (*integer[0..65535]*; Default: **25**) | SMTP server's port. |
| **tls** (*no\|yes\|starttls*; Default: **no**) | Whether to use TLS encryption:yes - sends STARTTLS and drops the session if TLS is not available on the serverno - does not send STARTTLSstarttls - sends STARTTLS and continues without TLS if a server responds that TLS is not available |
| **user** (*string*; Default: **""**) | The username used for authenticating to an SMTP server. |
| **vrf** (*VRF name*; default value: **main**) | Set VRF on which service is creating outgoing connections. |

:::warning
**Note:** All server configurations (if specified) can be overridden by send command.
:::

---

## Sending Email

**Sub-menu:** `/tool/e-mail`

The Send command takes the following parameters:

| Property | Description |
| :-- | :-- |
| **body** (*string*; Default: ) | The actual body of the email message |
| **cc** (*string*; Default: ) | Send a copy to listed recipients. Multiple addresses allowed, use "," to separate entries |
| **certificate-verification**(*yes* \| *yes-without-crl* \| *no*; Default: **no**) | Enables trust chain validation from the local certificate store. *yes-without-crl,* validates a certificate, not performing a CRL check (certificate revocation list). |
| **file** (*File[,File]*; Default: ) | List of the file names that will be attached to the mail separated by a comma. |
| **from** (*string*; Default: ) | Name or email address which will appear as the sender. If not specified, a value from the server's configuration is used. |
| **password** (*string*; Default: ) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | Password used to authenticate to an SMTP server. If not specified, a value from the server's configuration is used. |
| **port** (*integer[0..65535]*; Default: ) | Port of SMTP server. If not specified, a value from the server's configuration is used. |
| **server** (*IP/IPv6 address*; Default: ) | IP or IPv6 address of the SMTP server. If not specified, a value from the server's configuration is used. |
| **tls** (*yes\|no\|starttls*; Default: **no**) | Whether to use TLS encryption:yes - sends STARTTLS and drops the session if TLS is not available on the serverno - do not send STARTTLSstarttls - sends STARTTLS and continues without TLS if a server responds that TLS is not available |
| **subject** (*string*; Default: ) | The subject of the message. |
| **to** (*string*; Default: ) | Destination email address. Single address allowed. |
| **user** (*string*; Default: ) | The username used to authenticate to an SMTP server. If not specified, a value from the server's configuration is used. |

---

## Basic examples

**This example will show how to send an email with configuration export every 24 hours.**

1. Configure SMTP server.

```ros
[admin@MikroTik] /tool/e-mail> set server=10.1.1.1 port=25 from="router@mydomain.com"
```

1. Add a new script named "export-send":

```ros
/export file=export 
/tool/e-mail/send to="config@mydomain.com" subject="$[/system/identity/get name] export" \ 
body="$[/system/clock/get date] configuration file" file=export.rsc
```

1. Add scheduler to run our script.

```ros
/system/scheduler/add on-event="export-send" start-time=00:00:00 interval=24h
```

**Send e-mail to a server using TLS/SSL encryption.**

:::info
Google Mail does not allow third-party devices to authenticate using a standard Gmail password. An App password must be generated and used instead.

To generate an App password, navigate to **Security > How you sign in to Google**, enable 2-Step Verification, then generate an App password. Use the generated value in the `set password=mypassword` setting shown below.
:::

1. Configure the client to connect to the correct server.

```ros
/tool/e-mail 
set address=smtp.gmail.com
set port=587
set tls=yes 
set from=myuser@gmail.com 
set user=myuser 
set password=mypassword
```

1. Send an e-mail using the send command.

```ros
/tool/e-mail/send to=myuser@anotherdomain.com subject="email test" body="email test" 
```
