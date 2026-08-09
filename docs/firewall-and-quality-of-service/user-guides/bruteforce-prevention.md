# Bruteforce prevention

> This page explains how to configure bruteforce prevention on MikroTik RouterOS by using firewall filters to block SSH login attempts after multiple failed attempts, with varying timeouts for each attempt level and a final allowance for legitimate users.

# Bruteforce prevention

This example demonstrates how to protect against bruteforce attacks on the SSH port. Note that SSH allows 3 login attempts per connection, and the address lists are not cleared upon a successful login. This means you could accidentally blacklist yourself if you trigger the protection.

```
/ip/firewall/filter/add action=add-src-to-address-list address-list=bruteforce_blacklist address-list-timeout=1d chain=input comment="Blacklist" connection-state=new dst-port=22 protocol=tcp src-address-list=connection3

/ip/firewall/filter/add action=add-src-to-address-list address-list=connection3 address-list-timeout=1h chain=input comment="Third attempt" connection-state=new dst-port=22 protocol=tcp src-address-list=connection2

/ip/firewall/filter/add action=add-src-to-address-list address-list=connection2 address-list-timeout=15m chain=input comment="Second attempt" connection-state=new dst-port=22 protocol=tcp src-address-list=connection1

/ip/firewall/filter/add action=add-src-to-address-list address-list=connection1 address-list-timeout=5m chain=input comment="First attempt" connection-state=new dst-port=22 protocol=tcp

/ip/firewall/filter/add action=accept chain=input dst-port=22 protocol=tcp src-address-list=!bruteforce_blacklist
```

If all three connection lists used a 1-minute timeout, an attacker could perform 9 guesses per minute. With the structure above, the maximum is 3 guesses per 5 minutes.

:::warning
The address list naming follows the convention used in the Port knocking article. A similar naming scheme is used where the trusted address list is named as "secured".
:::
