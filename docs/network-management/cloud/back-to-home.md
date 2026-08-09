# Back To Home

> Back To Home enables secure VPN access from anywhere to your router, even if it lacks a public IP or is behind NAT. It uses MikroTik relay servers for indirect connections, ensuring end-to-end encryption without exposing keys. The feature supports both smartphone apps and manual RouterOS configuration, including sharing tunnels with guests or via WireGuard for computers.

# Back To Home

**Sub-menu:** `/ip/cloud` **Packages required:** `routeros`  
**RouterOS version required:** v7.12 and newer  
**Hardware requirements:** ARM/ARM64/TILE architecture devices

Back To Home is a convenience feature that configures your device for secure VPN access from anywhere in the world to your router and your network, even if your router does not have a public IP address, is behind NAT or Firewall.

Configuration is done with the MikroTik Back to Home app ([Android](https://play.google.com/store/apps/details?id=com.mikrotik.android.freevpn), [iPhone](https://apps.apple.com/lv/app/mikrotik-back-to-home/id6450679198)).

If the VPN server (your home router) has a public IP address, the VPN app will create a direct VPN connection between the phone and the router. However, if the router is not directly reachable from the internet, the connection will be made through the MikroTik relay servers. The connection is always end-to-end encrypted. The relay server or any other device does not have access to the encryption keys. In essence, the relay only helps your device to reach the router. The connection will appear as going out from your router, not from the relay. *In case of going through the relay, speed could be limited.*

This feature is a convenient option to access your home network or view content available in your home country, from locations where some content is not available. It is not meant for anonymity; it is for simple one click access to your home network. For more granular security controls, we recommend you manually configure and secure a VPN connection using the advanced RouterOS options.

#### Enabling BTH using the app

To set up Back to Home, you should have a smartphone with the BTH app and should be inside your home, connected to your router's WiFi network.

- Connect to the router's Wi-Fi using your phone.
- Open the Back to Home application ([Android](https://play.google.com/store/apps/details?id=com.mikrotik.android.freevpn), [iPhone](https://apps.apple.com/lv/app/mikrotik-back-to-home/id6450679198)).
- Tap "Create new".
- Enter your local router IP address (most likely `192.168.88.1`), username, and password of your router, and tap "Connect".
- Give the tunnel a name, then tap "Create tunnel".
- Your phone will ask for permission to add new VPN settings. Approve it with your phone pin.
- Setup is done. You can now disconnect from the router's Wi-Fi and connect to any other network, like LTE/5G or simply leave your house now.
- Tap the Connect button to toggle the connection of the selected tunnel.

| ![](/docs/network-management/cloud/img/back-to-home_01.png) | ![](/docs/network-management/cloud/img/back-to-home_02.png) | ![](/docs/network-management/cloud/img/back-to-home_03.png) | ![](/docs/network-management/cloud/img/back-to-home_04.png) | ![](/docs/network-management/cloud/img/back-to-home_05.png) |
| :-- | :-- | :-- | :-- | :-- |
| Tap "Create new" | Provide your router credentials | Connection established | Allow VPN to be added | If the device is not supported, an error is shown |

#### Sharing the BTH connection with another phone user

It is possible to create Guest tunnels for your friends and family. You can even specify if you want these people to access your local network as well, or if they should be restricted to only use the internet via your router. Once you create shared tunnels, you can send Invitation links via any chat application on your phone, or show a QR code to your friend in person (in both these cases, the friend will have to also install the BTH app). If you want to connect to your router via the WireGuard(TM) app from another phone or from a computer, it is possible as well. Just select to share the WireGuard(TM) config file, and open this file in the WireGuard(TM) app.

| ![](/docs/network-management/cloud/img/back-to-home_06.png) | ![](/docs/network-management/cloud/img/back-to-home_07.png) | ![](/docs/network-management/cloud/img/back-to-home_08.png) | ![](/docs/network-management/cloud/img/back-to-home_17.png) | ![](/docs/network-management/cloud/img/back-to-home_09.jpg) | ![](/docs/network-management/cloud/img/back-to-home_10.jpg) |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Manage shares | Connect to your tunnel first | Once connected, create shares | Provide a name and access level | Share sheet opens | Send the invite link via WhatsApp, Signal etc. |

To share your tunnel with somebody:

- As the owner, connect to your BTH tunnel.
- Click the "..." icon next to your tunnel and click "Manage shares".
- Enter the administration password for the router, since you will be modifying the router config.
- Tap "Create" in the Shares manager.
- Enter your friend's name in the "Tunnel name", since a new tunnel will be made for them.
- Specify the expiry date of this new Guest tunnel.
- Specify if the user will need to access your internal network of your home. Do not check this if they only want to use this tunnel for internet access.
- Once "Create tunnel" has been pressed, the phone Share Sheet opens. Select a method how to send the invite link.
- Once the other person clicks on this link, they will either be directed to install the BTH app, or the BTH app will open and will allow them to set up this new Guest tunnel in their phone.

#### Sharing the BTH tunnel with a computer via the WireGuard(TM) app

Since there is no BTH app for PCs, you can use the [WireGuard(TM) app](https://www.wireguard.com/install/) to connect to the shared tunnel. You can even share your connection with yourself, by "inviting" your computer to connect.

Let's make a new share, this time for yourself, for using from the PC.

| ![](/docs/network-management/cloud/img/back-to-home_13.png) | ![](/docs/network-management/cloud/img/back-to-home_14.png) | ![](/docs/network-management/cloud/img/back-to-home_15.png) | ![](/docs/network-management/cloud/img/back-to-home_16.png) | ![](/docs/network-management/cloud/img/back-to-home_16.png) | ![](/docs/network-management/cloud/img/back-to-home_18.png) |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Create | Specify name and access level | You have two shares now | Click "..." to send an invite | Pick "Share WireGuard config  file" | AirDrop to your macOS or e-mail the file |

Install the WireGuard app on your computer and click "Import Tunnel from file"

![](/docs/network-management/cloud/img/back-to-home_19.jpg)

---

#### Configuring BTH manually in RouterOS (optional, if no smartphone is available to you)

:::info
Important notice

It is important to note, **NOTHING has to be configured in RouterOS to use Back to Home**. Simply use the BTH app (see above section) to enable it. The whole point of Back to Home is to avoid using Winbox or command line. The below instructions are only for debugging or seasoned administrators.
:::

1. Connect to the router
2. Enable DDNS Cloud service: ``/ip/cloud/set ddns-enabled=yes``
3. Enable Back To Home: ``/ip/cloud/set back-to-home-vpn=enabled``
4. Print tunnel configuration: ``/ip/cloud/print``
5. Scan the QR Code (``vpn-wireguard-client-config-qrcode``) or Copy the config (``vpn-wireguard-client-config``) and enter in the preferred WireGuard速 client. Only one client at a time will be available to use this config.  

   :::warning
   After configuring Back To Home - an additional peer entry is automatically made, which can be seen by running the command *`/ip/cloud/print`*. This is intended for the VPN to work in the case that the device does not have access to a public IP address and opts to establish the connection by using MikroTik's relay server.  
   In the case that your device has access to a public IP address, the generated peer entry is ignored:

   ```
   [Peer]
   PublicKey = //////////////////////////////////////////8=
   AllowedIPs = 0.0.0.0/32
   Endpoint = example.com:12345
   PersistentKeepalive = 15 
   ```

   :::

#### Removing and disabling connections

In the smartphone app, the VPN configuration is added to the System VPN settings. In this regard, the Back to Home app only acts as a wizard. It supplies the needed config to the operating system (this is why iPhone will warn you about altering system configuration).

To remove the created connection, go into the smartphone settings app and remove the VPN connection from there.

On the MikroTik router side, you should manually delete the added Peers in the Wireguard menu. Note that the "revoke-and-disable" button can't be used to "Pause" the use of the Back to Home feature. Once you revoke-and-disable in RouterOS, all Peers will be disassociated from the Cloud / Relay servers, and you will have to re-create the connection from the Smartphone app. Therefore, once you have used the option "revoke-and-disable" in the RouterOS IP Cloud menu, you need to also delete the Peers from the Wireguard menu, as they can't be re-used.

## Property reference

### IP Cloud

**Sub-menu:** `/ip/cloud`

Back to Home shares the menu with IP Cloud. Back to Home parameters:

| Property | Description |
| :-- | :-- |
| **back-to-home-vpn** (*enabled \| revoked-and-disabled*; Default: **revoked-and-disabled**) | Enables or revokes and disables the Back to Home service. ddns-enabled must not be set to no, for BTH to function. |
| **vpn-dns-name** (*read-only: string*) | Shows the DNS name assigned to the device. The name consists of the product serial number appended with *.vpn.mynetname.net*. This field is visible only after at least one ddns-request is successfully completed. |
| **vpn-port** (*read-only: integer*) | Port used by BTH VPN. |
| **vpn-status** (*read-only: string*) | Contains text string that describes the current BTH state. |
| **vpn-relay-rtts** (*read-only;* "region (ip4: time(**ms**), ip6: time (**ms)**") | Round trip time in milliseconds for each available relay, values are shown both for IPv4 and IPv6. |
| **vpn-relay-ipv4-status** (*read-only: string*) | Status of the connection to the relay and detailed information about the relay |
| **vpn-relay-ipv6-status**(*read-only: string*) | Status of the connection to the relay and detailed information about the relay |
| **vpn-relay-regions** (*read-only: string*) | Available VPN relay regions, which can be referenced in vpn-prefer-relay-code. All available relays will be shown here. |
| **vpn-relay-addressess**(*read-only: string*) | IPv4 address of the relay |
| **vpn-relay-addressess-ipv6** (*read-only: string*) | IPv6 address of the relay |
| **vpn-private-key** (*read-only: string*) *[sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | Private key for BTH |
| **vpn-public-key** (*read-only: string*) | Public key for BTH |
| **vpn-peer-private-key**(*read-only: string*) *[sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | Peer private key |
| **vpn-peer-public-key** (*read-only: string*) | Peer public key |
| **vpn-prefer-relay-code** (*string;*) | You can enter a relay code that will be preferred for the BTH connection, if not set, the relay with the smallest RTT will be chosen. |
| **vpn-interface** (*read-only: string*) | Name of the created interface for Back to Home WireGuard速 tunnel. |
| **vpn-wireguard-client-config** (*read-only: string*) | Configuration that can be entered in your preferred WireGuard速 client. Only one client at a time will be available to use this config. |
| **vpn-wireguard-client-config-qrcode** (*read-only*) | Scannable QR Code for your preferred WireGuard速 client. Only one client at a time will be available to use this config. |

:::info
When using vpn-wireguard-client-config or vpn-wireguard-client-config-qrcode, both options are equal; you only need to import one of these into your WireGuard client device.
:::

### Back to Home users

**Sub-menu:** `/ip/cloud/back-to-home-user`

Since RouterOS 7.14 there is a new back to home specific user manager available in the menu `/ip/cloud/back-to-home-user` where you can see all the users that are added by the Back to Home mobile app, change their firewall preference and also add new ones.

```
[boss@mikrotik-ax] /ip/cloud/back-to-home-user> print detail   
Flags: X - disabled; A - active   
  
 0  A name="user1" slot=3 expires=never client-address=192.168.216.3/32,fc00:0:0:216::3/128 allow-lan=no   
      private-key="OHqR2BZXJp0N6//3JzzoJhBJVb0rrSxV0dxQL/2UdXY=" public-key="Na7oEq9XLdeK8ouCUX+tC4FIM51vEnZ7mLiFqG9xiUQ="   
  
[boss@mikrotik-ax] /ip/cloud/back-to-home-user>
```

When adding users in this menu, you can view their Wireguard config and QR code with this command `/interface/wireguard/peers/show-client-config user1`

`Allow-lan=no` will add the users into a firewall address list that only allows internet access, but blocks the users from accessing your internal network. Note that expiry date can't be changed, once a user has been added.

| Property | Description |
| :-- | :-- |
| **name** (*string*) | Informative name of BTH user |
| **expires**(string; never \| date: *"YYYY-MM-DD HH:MM:SS";*  Default: **never***)* | Expiration time and date for user. Cannot be changed once user is created |
| **client-address**(string: IPv4 \| IPv6) | Client address. If not specified, one will be made automatically |
| **allow-lan**(string: yes \| no; Default: **no**) | Will add the user into a firewall address list that only allows internet access, but blocks the user from accessing your internal network |
| **private-key**(string;) *[sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | Private key for user, if not set manually, it will be generated by the system |
| **public-key**(string;) | Public key for user, if not set manually, it will be generated by the system |
