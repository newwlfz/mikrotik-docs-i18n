# DLNA Media Server

> The page introduces DLNA media server functionality in MikroTik RouterOS, explaining how it enables networked devices to share digital media using UPnP protocols. It details server settings such as allowed hosts, IP restrictions, and friendly names, with examples for configuring multiple instances with access limitations.

# DLNA Media Server

DLNA (Digital Living Network Alliance) is a set of network protocols that enables devices to share digital media such as videos, photos, and music. DLNA is built on the UPnP (Universal Plug and Play) architecture, which provides device discovery and control capabilities.

UPnP allows devices to discover each other on the network and exchange control messages. It uses SSDP (Simple Service Discovery Protocol) for discovery, SOAP (Simple Object Access Protocol) for control messages, and XML for device and service descriptions. This enables devices such as TVs, computers, and mobile devices to connect and share media content seamlessly.

In RouterOS, you can enable the media server to share movies or music with home devices such as TVs or player applications like VLC on your computer.

:::danger
Media sharing (DLNA) is not supported on SMIPS devices.
:::

## Server settings

| Property | Description |
| :-- | :-- |
| **allowed-hostname** | To restrict access to specific hostnames. |
| **allowed-ip** | To limit access to specified IP addresses |
| **friendly-name** | The name that will be displayed for the DLNA server on the network. |
| **interface** | Specifies the network interface that the DLNA server will use |
| **path** | The file path where the media content is stored and will be served from. |
| **disabled** | Specifies if entry is disabled |

### Creating a DLNA Server

To enable DLNA media streaming on your MikroTik router, use the `/ip media add` command. This command configures a media server that allows DLNA-compatible devices on your network to discover and access media files stored on connected USB storage. Replace `Mikrotik` with a descriptive name for your media server, `bridge1` with the bridge interface you want to use for media discovery, and `usb1` with the USB storage path where your media files are located.

```ros
/ip/media/add friendly-name=Mikrotik interface=bridge1 path=usb1
```

### Creating Multiple DLNA Server Instances with Access Limitations

This example demonstrates how to configure separate DLNA server instances with specific access restrictions. Use case: restrict a children's TV to access only child-friendly media stored in the "usb1/kids" folder.

```ros
/ip/media/add friendly-name=adults interface=bridge1 path=usb1/adults allowed-hostname=ADULTS_TV
/ip/media/add friendly-name=kids interface=bridge1 path=usb1/kids allowed-hostname=KIDS_TV
```
