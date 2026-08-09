# user-manager

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# user-manager

**Package:** userman-5
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="authentication-port" typ="num"></ArgTableRow>
<ArgTableRow arg="accounting-port" typ="num"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="radsec-certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="use-profiles" typ="bool"></ArgTableRow>
<ArgTableRow arg="require-message-auth" typ="enum (no | yes-access-request)"></ArgTableRow>
</ArgTable>

## user-manager/advanced

**Package:** userman-5
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="web-private-username" typ="string"></ArgTableRow>
<ArgTableRow arg="web-private-password" typ="string"></ArgTableRow>
<ArgTableRow arg="paypal-allow" typ="bool"></ArgTableRow>
<ArgTableRow arg="paypal-use-sandbox" typ="bool"></ArgTableRow>
<ArgTableRow arg="paypal-user" typ="string"></ArgTableRow>
<ArgTableRow arg="paypal-password" typ="string"></ArgTableRow>
<ArgTableRow arg="paypal-signature" typ="string"></ArgTableRow>
<ArgTableRow arg="paypal-currency" typ="string"></ArgTableRow>
</ArgTable>

## user-manager/attribute

**Package:** userman-5
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="vendor-id" typ="enum (standard | Cisco | Microsoft | Mikrotik)"></ArgTableRow>
<ArgTableRow arg="type-id" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="value-type" typ="enum (ip-address | string | uint32 | hex | ip6-prefix | macro)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="packet-types" typ="ubit (access-accept, access-challenge)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="default-name" typ="string"></ArgTableRow>
<ArgTableRow arg="standard-name" typ="string"></ArgTableRow>
</ArgTable>

## user-manager/database

**Package:** userman-5
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="db-path" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="found-legacy-db-path" typ="string"></ArgTableRow>
<ArgTableRow arg="db-size" typ="num"></ArgTableRow>
<ArgTableRow arg="free-disk-space" typ="num"></ArgTableRow>
</ArgTable>

### user-manager/database/load

**Package:** userman-5
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="file {  }"></ArgTableRow>
</ArgTable>

### user-manager/database/migrate-legacy-db

**Package:** userman-5
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="database-path" typ="file"></ArgTableRow>
<ArgTableRow arg="overwrite" typ="bool"></ArgTableRow>
</ArgTable>

### user-manager/database/optimize-db

**Package:** userman-5
**Type:** Command

### user-manager/database/save

**Package:** userman-5
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="file {  }"></ArgTableRow>
<ArgTableRow arg="overwrite" typ="bool"></ArgTableRow>
</ArgTable>

## user-manager/generate-report

**Package:** userman-5
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="columns" typ="ubit (username, session-start, session-end, user-ip, calling-station-id, uptime, download, upload, acct-session-id, nas-ip-address, nas-port-type, nas-port-id, terminate-cause, nas-identifier)"></ArgTableRow>
<ArgTableRow arg="report-template" typ="enum"></ArgTableRow>
</ArgTable>

## user-manager/limitation

**Package:** userman-5
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="download-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="upload-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="transfer-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="uptime-limit" typ="time"></ArgTableRow>
<ArgTableRow arg="reset-counters-start-time" typ="date"></ArgTableRow>
<ArgTableRow arg="reset-counters-interval" typ="alt { enum (disabled | hourly | daily | weekly | monthly) { disabled:radserv::limitation::RC_NEVER, hourly:radserv::limitation::RC_HOURLY, daily:radserv::limitation::RC_DAILY, weekly:radserv::limitation::RC_WEEKLY, monthly:radserv::limitation::RC_MONTHLY }
, time
 }"></ArgTableRow>
<ArgTableRow arg="rate-limit-rx" typ="num"></ArgTableRow>
<ArgTableRow arg="rate-limit-tx" typ="num"></ArgTableRow>
<ArgTableRow arg="rate-limit-burst-rx" typ="num"></ArgTableRow>
<ArgTableRow arg="rate-limit-burst-tx" typ="num"></ArgTableRow>
<ArgTableRow arg="rate-limit-burst-threshold-rx" typ="num"></ArgTableRow>
<ArgTableRow arg="rate-limit-burst-threshold-tx" typ="num"></ArgTableRow>
<ArgTableRow arg="rate-limit-burst-time-rx" typ="time"></ArgTableRow>
<ArgTableRow arg="rate-limit-burst-time-tx" typ="time"></ArgTableRow>
<ArgTableRow arg="rate-limit-min-rx" typ="num"></ArgTableRow>
<ArgTableRow arg="rate-limit-min-tx" typ="num"></ArgTableRow>
<ArgTableRow arg="rate-limit-priority" typ="num"></ArgTableRow>
</ArgTable>

## user-manager/monitor

**Package:** userman-5
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="active-sessions" typ="num"></ArgTableRow>
</ArgTable>

## user-manager/payment

**Package:** userman-5
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="user" typ="enum"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="price" typ="num"></ArgTableRow>
<ArgTableRow arg="currency" typ="string"></ArgTableRow>
<ArgTableRow arg="trans-start" typ="date"></ArgTableRow>
<ArgTableRow arg="trans-end" typ="alt { enum (not-finished) { not-finished:0 }
, date
 }"></ArgTableRow>
<ArgTableRow arg="trans-status" typ="enum (started | pending | approved | declined | error | timeout | aborted | user-approved)"></ArgTableRow>
<ArgTableRow arg="method" typ="enum (paypal | authorize-net)"></ArgTableRow>
<ArgTableRow arg="user-message" typ="string"></ArgTableRow>
</ArgTable>

## user-manager/profile

**Package:** userman-5
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="validity" typ="alt { enum (unlimited) { unlimited:0 }
, time
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="name-for-users" typ="string"></ArgTableRow>
<ArgTableRow arg="starts-when" typ="enum (first-auth | assigned)"></ArgTableRow>
<ArgTableRow arg="price" typ="num"></ArgTableRow>
<ArgTableRow arg="override-shared-users" typ="enum (off | unlimited)"></ArgTableRow>
</ArgTable>

## user-manager/profile-limitation

**Package:** userman-5
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="profile" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="limitation" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="from-time" typ="time"></ArgTableRow>
<ArgTableRow arg="till-time" typ="time"></ArgTableRow>
<ArgTableRow arg="weekdays" typ="ubit (sunday, monday, tuesday, wednesday, thursday, friday, saturday)"></ArgTableRow>
</ArgTable>

## user-manager/router

**Package:** userman-5
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46/)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (udp | radsec)"></ArgTableRow>
<ArgTableRow arg="shared-secret" typ="string"></ArgTableRow>
<ArgTableRow arg="coa-port" typ="num"></ArgTableRow>
</ArgTable>

### user-manager/router/monitor

**Package:** userman-5
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="broken-requests" typ="num"></ArgTableRow>
<ArgTableRow arg="unknown-requests" typ="num"></ArgTableRow>
<ArgTableRow arg="access-requests" typ="num"></ArgTableRow>
<ArgTableRow arg="access-failures" typ="num"></ArgTableRow>
<ArgTableRow arg="accounting-requests" typ="num"></ArgTableRow>
<ArgTableRow arg="accounting-failures" typ="num"></ArgTableRow>
<ArgTableRow arg="disconnect-ack" typ="num"></ArgTableRow>
<ArgTableRow arg="disconnect-nak" typ="num"></ArgTableRow>
<ArgTableRow arg="coa-ack" typ="num"></ArgTableRow>
<ArgTableRow arg="coa-nak" typ="num"></ArgTableRow>
<ArgTableRow arg="sent-from-cache" typ="num"></ArgTableRow>
</ArgTable>

### user-manager/router/reset-counters

**Package:** userman-5
**Type:** Command

## user-manager/session

**Package:** userman-5
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="A" typ="active"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="user" typ="enum"></ArgTableRow>
<ArgTableRow arg="acct-session-id" typ="string"></ArgTableRow>
<ArgTableRow arg="acct-multi-session-id" typ="string"></ArgTableRow>
<ArgTableRow arg="nas-port-type" typ="enum (async | sync | isdn-sync | isdn-sync-v120 | isdn-sync-v110 | virtual | piafs | hdlc | x25 | x75 | g3-fax | sdsl | adsl-cap | adsl-dmt | idsl | ethernet | dsl | cable | wireless | wireless-802.11)"></ArgTableRow>
<ArgTableRow arg="nas-port-id" typ="string"></ArgTableRow>
<ArgTableRow arg="nas-ip-address" typ="alt { ipAddr
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="nas-identifier" typ="string"></ArgTableRow>
<ArgTableRow arg="calling-station-id" typ="string"></ArgTableRow>
<ArgTableRow arg="user-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="status" typ="ubit (start, stop, interim, close-acked, expired)"></ArgTableRow>
<ArgTableRow arg="started" typ="date"></ArgTableRow>
<ArgTableRow arg="ended" typ="date"></ArgTableRow>
<ArgTableRow arg="terminate-cause" typ="enum (user-request | lost-carrier | lost-service | idle-timeout | session-timeout | admin-reset | admin-reboot | port-error | nas-error | nas-request | nas-reboot | port-unneeded | port-preempted | port-suspended | service-unavailable | callback | user-error | host-request | supplicant-restart | reauthentication-failure | port-reinitialized | port-administratively-disabled | um-user-deleted | um-user-disabled | um-admin-request | um-nas-rebooted | um-simultaneous-sessions | um-limits-reached | um-limits-changed | um-unknown)"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="download" typ="num"></ArgTableRow>
<ArgTableRow arg="upload" typ="num"></ArgTableRow>
<ArgTableRow arg="last-accounting-packet" typ="date"></ArgTableRow>
</ArgTable>

### user-manager/session/close-session

**Package:** userman-5
**Type:** Command

## user-manager/user

**Package:** userman-5
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="otp-secret" typ="string"></ArgTableRow>
<ArgTableRow arg="group" typ="enum"></ArgTableRow>
<ArgTableRow arg="shared-users" typ="enum (unlimited)"></ArgTableRow>
<ArgTableRow arg="caller-id" typ="enum (bind)"></ArgTableRow>
<ArgTableRow arg="attributes" typ="object { super { enum
, :string
 } { enum
, :string
 }
 }"></ArgTableRow>
</ArgTable>

## user-manager/user-profile

**Package:** userman-5
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="user" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="state" typ="enum (waiting | running | running-active | used)"></ArgTableRow>
<ArgTableRow arg="end-time" typ="alt { enum (not-yet-running | unlimited) { not-yet-running:radserv::UNKNOWN, unlimited:radserv::UNLIMITED }
, date
 }"></ArgTableRow>
</ArgTable>

### user-manager/user-profile/activate-user-profile

**Package:** userman-5
**Type:** Command

### user-manager/user/add-batch-users

**Package:** userman-5
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="username-length" typ="num"></ArgTableRow>
<ArgTableRow arg="number-of-users" typ="num"></ArgTableRow>
<ArgTableRow arg="username-prefix" typ="string"></ArgTableRow>
<ArgTableRow arg="password-length" typ="enum (empty | same-as-username)"></ArgTableRow>
<ArgTableRow arg="username-characters" typ="ubit (uppercase, lowercase, numbers)"></ArgTableRow>
<ArgTableRow arg="password-characters" typ="ubit (uppercase, lowercase, numbers)"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="group" typ="enum"></ArgTableRow>
<ArgTableRow arg="caller-id" typ="enum (bind)"></ArgTableRow>
<ArgTableRow arg="shared-users" typ="enum (unlimited)"></ArgTableRow>
<ArgTableRow arg="disabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="comment" typ="string"></ArgTableRow>
</ArgTable>

### user-manager/user/generate-voucher

**Package:** userman-5
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="voucher-template" typ="enum"></ArgTableRow>
</ArgTable>

### user-manager/user/group

**Package:** userman-5
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="outer-auths" typ="ubit (pap, chap, mschap1, mschap2, eap-tls, eap-ttls, eap-peap, eap-mschap2)"></ArgTableRow>
<ArgTableRow arg="inner-auths" typ="ubit (ttls-pap, ttls-chap, ttls-mschap1, ttls-mschap2, peap-mschap2)"></ArgTableRow>
<ArgTableRow arg="attributes" typ="object { super { enum
, :string
 } { enum
, :string
 }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="default-name" typ="string"></ArgTableRow>
</ArgTable>

### user-manager/user/monitor

**Package:** userman-5
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="total-uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="total-download" typ="num"></ArgTableRow>
<ArgTableRow arg="total-upload" typ="num"></ArgTableRow>
<ArgTableRow arg="active-sessions" typ="num"></ArgTableRow>
<ArgTableRow arg="active-sub-sessions" typ="num"></ArgTableRow>
<ArgTableRow arg="actual-profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="attributes-details" typ="object { super { enum
, :string
, :enum (ip-address | string | uint32 | hex | ip6-prefix | macro) { ip-address:radserv::attr::ATTR_TYPE_IP_ADDR, string:radserv::attr::ATTR_TYPE_STRING, uint32:radserv::attr::ATTR_TYPE_U32, hex:radserv::attr::ATTR_TYPE_HEX, ip6-prefix:radserv::attr::ATTR_TYPE_IP6_PREFIX, macro:radserv::attr::ATTR_TYPE_MACRO }
, :0xstring
 } { enum
, :string
, :enum (ip-address | string | uint32 | hex | ip6-prefix | macro) { ip-address:radserv::attr::ATTR_TYPE_IP_ADDR, string:radserv::attr::ATTR_TYPE_STRING, uint32:radserv::attr::ATTR_TYPE_U32, hex:radserv::attr::ATTR_TYPE_HEX, ip6-prefix:radserv::attr::ATTR_TYPE_IP6_PREFIX, macro:radserv::attr::ATTR_TYPE_MACRO }
, :0xstring
 }
 }"></ArgTableRow>
</ArgTable>
