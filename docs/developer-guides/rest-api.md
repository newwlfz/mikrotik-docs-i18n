# REST API

> REST API with examples for developers.

# REST API

The term **REST API** generally refers to an **API** accessed via HTTP protocol at a predefined set of resource-oriented URLs.
**REST API** is implemented as a JSON wrapper interface of the [**API**](./api/index.md). It allows you to create, read, update and delete resources and call arbitrary console commands.

To start using REST API, enable either the `www-ssl` or `www` service in the [`IP Service`](../system-information-and-utilities/services.md) menu.

When the `www-ssl` service is running (HTTPS access), you can connect to:

- `https://<router_IP>/rest`.

When the `www` service is running (HTTP access), you can connect to:

- `http://<router_IP>/rest`.

The main risk of using HTTP access (`www` service) is that authentication credentials can be read by passive eavesdropping. Use it only for tests on networks where an attacker does not have access or when you are certain the data cannot be decrypted, for example when HTTP is carried over an encrypted tunnel.

The easiest way to begin is with cURL, wget, the fetch tool, or any other simple HTTP client.

```sh
$ curl -k -u admin: https://10.155.101.214/rest/system/resource

[{"architecture-name":"tile","board-name":"CCR1016-12S-1S+",
"build-time":"2020-12-04 14:19:51","cpu":"tilegx","cpu-count":"16",
"cpu-frequency":"1200","cpu-load":"1","free-hdd-space":"83439616",
"free-memory":"1503133696","platform":"MikroTik",
"total-hdd-space":"134217728","total-memory":"2046820352",
"uptime":"2d20h12m20s","version":"7.1beta4 (development)"}]
```

## Authentication

Authentication to the REST API uses [HTTP Basic Auth](http://en.wikipedia.org/wiki/Basic_access_authentication). Your username and password are the same as those of a console user (by default, **admin** with no password).

To use a secure connection (HTTPS), set up certificates in the [Certificate menu](../authentication-authorization-accounting/certificates.md) and configure `www-ssl` to use the newly created or imported certificate. If you use a self‑signed certificate, import its CA into the client's trusted root. For tests you can connect insecurely (`-k` with cURL or `--no-check-certificate` with wget).

### JSON format

The server broadly follows the ECMA‑404 standard, with the following notes:

- In JSON replies all object values are encoded as strings, even if the underlying data is a number or a boolean.
- The server also accepts numbers in octal format (begins with 0) and hexadecimal format (begins with 0x). If the numbers are sent in a string format, they are assumed to be in decimal format.
- Numbers with exponents are not supported.

## HTTP Methods

The following table summarizes the supported HTTP methods

| HTTP Verb   | CRUD          | ROS    | Description                                             |
|:--|:--|:--|:--|
| GET         | Read          | print  | To get the records.                                     |
| PATCH       | Update/Modify | set    | To update a single record.                              |
| PUT         | Create        | add    | To create a new record.                                 |
| DELETE      | Delete        | remove | To delete a single record.                              |
| POST        |               |        | Universal method to get access to all console commands. |

### GET

This method allows getting the list of all records or a single record from the specified menu encoded in the URL.
For example, get all IP addresses (equivalent to the `ip/address/print` CLI command):

```sh
$ curl -k -u admin: https://10.155.101.214/rest/ip/address

[{".id":"*1","actual-interface":"ether2","address":"10.0.0.111/24","disabled":"false",
"dynamic":"false","interface":"ether2","invalid":"false","network":"10.0.0.0"},
{".id":"*2","actual-interface":"ether3","address":"10.0.0.109/24","disabled":"true",
"dynamic":"false","interface":"ether3","invalid":"false","network":"10.0.0.0"}]
```

Append an ID at the end of the URL to return a single record:

```sh
$ curl -k -u admin: https://10.155.101.214/rest/ip/address/*1

{".id":"*1","actual-interface":"ether2","address":"10.0.0.111/24","disabled":"false",
"dynamic":"false","interface":"ether2","invalid":"false","network":"10.0.0.0"}
```

If the table contains named parameters, you can use the name instead of the ID; for example, to get **ether1**:

```sh
curl -k -u admin: https://10.155.101.214/rest/interface/ether1
```

You can also filter the output; for example, return only dynamic addresses that belong to the 10.155.101.0 network:

```sh
$ curl -k -u admin: "https://10.155.101.214/rest/ip/address?network=10.155.101.0&dynamic=true"

[{".id":"*8","actual-interface":"sfp12","address":"10.155.101.214/24","disabled":"false",
"dynamic":"true","interface":"sfp12","invalid":"false","network":"10.155.101.0"}]
```

Another example returns only addresses on the "dummy" interface and with the comment "test":

```sh
$ curl -k -u admin: 'https://10.155.101.214/rest/ip/address?comment=test&interface=dummy'

[{".id":"*3","actual-interface":"dummy","address":"192.168.99.2/24","comment":"test",
"disabled":"false","dynamic":"false","interface":"dummy","invalid":"false","network":"192.168.99.0"}]
```

If you want to return only specific properties, you can use the `.proplist`, followed by the `=` character and a list of comma-separated properties. For example, to show only the address and if it's disabled:

```sh
$ curl -k -u admin: https://10.155.101.214/rest/ip/address?.proplist=address,disabled

[{"address":"10.0.0.111/24","disabled":"false"},{"address":"10.0.0.109/24","disabled":"true"}]
```

### PATCH

Use this method to update a single record. Set the body of the PATCH request to a JSON object containing the fields and their new values. For example, add a comment:

```sh
$ curl -k -u admin: -X PATCH https://10.155.101.214/rest/ip/address/*3 \
  --data '{"comment": "test"}' -H "content-type: application/json"

{".id":"*3","actual-interface":"dummy","address":"192.168.99.2/24","comment":"test",
"disabled":"false","dynamic":"false","interface":"dummy","invalid":"false","network":"192.168.99.0"}
```

In case of a successful update, the server returns the updated object with all its parameters.

### PUT

This method creates a new record. Set the request body to a JSON object containing the parameters for the record. Only one record can be created per request.

In case of success, the server returns the created object with all its parameters.
For example, add an IP address to a dummy interface:

```sh
$ curl -k -u admin: -X PUT https://10.155.101.214/rest/ip/address \
  --data '{"address": "192.168.111.111", "interface": "dummy"}' -H "content-type: application/json"

{".id":"*A","actual-interface":"dummy","address":"192.168.111.111/32","disabled":"false",
"dynamic":"false","interface":"dummy","invalid":"false","network":"192.168.111.111"}
```

### DELETE

Use this method to delete a record with a specified ID. If the deletion succeeds, the server responds with an empty body. For example, calling the same delete twice causes the router to return a `404` error on the second attempt:

```sh
$ curl -k -u admin: -X DELETE https://10.155.101.214/rest/ip/address/*9
$ curl -k -u admin: -X DELETE https://10.155.101.214/rest/ip/address/*9
{"error":404,"message":"Not Found"}
```

### POST

All [**API**](./api/index.md) features are available via `POST`. Encode the command word in the URL and pass optional parameters as fields in a JSON object. For example, to change the password of the active user, send:

```
POST https://router/rest/password
{"old-password":"old","new-password":"N3w", "confirm-new-password":"N3w"}
```

A REST response has the same structure as an API response:

- If the response contains `!re` sentences (records), the JSON reply will contain a list of objects.
- If the `!done` sentence contains data, the JSON reply will contain an object with the data.
- If there are no records or data in the `!done` sentence, the response will hold an empty list.

There are two special keys: `.proplist` and `.query`, which are used with the `print` command word. Read more about APIs responses, prop lists, and queries in the [API](./api/index.md) documentation.

#### Proplist

Use the `.proplist` key to specify which properties to return. The value can be a single comma-separated string:

```
POST https://router/rest/interface/print
{".proplist":"name,type"}
```

or a list of strings:

```
POST https://router/rest/interface/print
{".proplist":["name","type"]}
```

For example, return address and interface properties from the `ip/address` menu:

```sh
$ curl -k -u admin: -X POST https://10.155.101.214/rest/ip/address/print\
  --data '{".proplist": ["address","interface"]}' -H "content-type: application/json"

[{"address":"192.168.99.2/24","interface":"dummy"},
{"address":"172.16.5.1/24","interface":"sfpplus1"},
{"address":"172.16.6.1/24","interface":"sfp2"},
{"address":"172.16.7.1/24","interface":"sfp3"},
{"address":"10.155.101.214/24","interface":"sfp12"},
{"address":"192.168.111.111/32","interface":"dummy"}]
```

#### Query

The `.query` key is used to create a query stack. The value is a list of query words. For example:

```
POST https://router/rest/interface/print
{".query":["type=ether","type=vlan","#|!"]}
```

is equivalent to the **API** sentence:

```
/interface/print
?type=ether
?type=vlan
?#|!
```

Example to combine `query` and `proplist`, to return `.id`, `address`, and `interface` properties for all dynamic records and records with the network 192.168.111.111

```sh
$ curl -k -u admin: -X POST https://10.155.101.214/rest/ip/address/print \
  --data '{".proplist": [".id","address","interface"], ".query": ["network=192.168.111.111","dynamic=true","#|"]}'\
  -H "content-type: application/json"

[{".id":"*8","address":"10.155.101.214/24","interface":"sfp12"},
{".id":"*A","address":"192.168.111.111/32","interface":"dummy"}]
```

#### Timeout

If a command runs indefinitely, it will eventually time out and connection will be closed with an error. The current timeout interval is 60 seconds. To avoid timeout errors, add a parameter that would sufficiently limit the command execution time.

For example, the ping command will exceed the timeout unless you add a count parameter to limit its execution:

```sh
$ curl -k -u admin: -X POST https://10.155.101.214/rest/ping \
  --data '{"address":"10.155.101.1"}' \
  -H "content-type: application/json"

{"detail":"Session closed","error":400,"message":"Bad Request"}

$ curl -k -u admin: -X POST https://10.155.101.214/rest/ping \
  --data '{"address":"10.155.101.1","count":"4"}' \
  -H "content-type: application/json"

[{"avg-rtt":"453us","host":"10.155.101.1","max-rtt":"453us","min-rtt":"453us","packet-loss":"0","received":"1","sent":"1","seq":"0","size":"56","time":"453us","ttl":"64"},
{"avg-rtt":"417us","host":"10.155.101.1","max-rtt":"453us","min-rtt":"382us","packet-loss":"0","received":"2","sent":"2","seq":"1","size":"56","time":"382us","ttl":"64"},
{"avg-rtt":"495us","host":"10.155.101.1","max-rtt":"650us","min-rtt":"382us","packet-loss":"0","received":"3","sent":"3","seq":"2","size":"56","time":"650us","ttl":"64"},
{"avg-rtt":"461us","host":"10.155.101.1","max-rtt":"650us","min-rtt":"359us","packet-loss":"0","received":"4","sent":"4","seq":"3","size":"56","time":"359us","ttl":"64"}]
```

For commands that accept a duration parameter, the REST timeout still applies. Even if a command is asked to run for an hour, it will terminate early and return an error.

For example, a bandwidth test tool can be limited by providing run duration less than a timeout value:

```sh
$ curl -k -u admin: -X POST 'https://10.155.101.214/rest/tool/bandwidth-test' \
  --data '{"address":"10.155.101.1","duration":"3s"}' \
  -H "content-type: application/json"

[{".section":"0","connection-count":"20","direction":"receive","lost-packets":"0",
"random-data":"false","rx-10-second-average":"0","rx-current":"0","rx-size":"1500",
"rx-total-average":"0",
"status":"connecting"},
{".section":"1","connection-count":"20","direction":"receive","duration":"1s",
"lost-packets":"0","random-data":"false","rx-10-second-average":"0","rx-current":"0",
"rx-size":"1500","rx-total-average":"0",
"status":"running"},
{".section":"2","connection-count":"20","direction":"receive","duration":"2s",
"lost-packets":"581175","random-data":"false","rx-10-second-average":"854372352",
"rx-current":"854372352","rx-size":"1500","rx-total-average":"854372352",
"status":"running"},
{".section":"3","connection-count":"20","direction":"receive","duration":"3s",
"lost-packets":"9014","random-data":"false","rx-10-second-average":"891979008",
"rx-current":"929585664","rx-size":"1500","rx-total-average":"891979008",
"status":"done testing"}]
```

## Errors

An API call’s success or failure is indicated by the HTTP status code. On failure (400 or higher), the response body contains a JSON object with an error code, description, and optional details. For example, attempting to delete an interface returns

```text
{"error":406,"message":"Not Acceptable","detail":"no such command or directory (remove)"}
```

## Monitor

The REST API does not support continuous commands such as `monitor`. Use the `monitor once` parameter to print a single result.

## Examples

Below we have added a short collection of REST API calls you can make to your devices:

Make a log entry:

```bash
curl -k -u <username>:<password> -X POST https://<ip-address>/rest/execute --data '{"script":"/log/info test"}' -H "content-type: application/json"
```

Run a script:

```bash
curl -k -u <username>:<password> https://<ip-address>/rest/system/script/run --data '{".id":"*1"}' -H "content-type: application/json"
```

LTE monitor once:

```bash
curl -k -u <username>:<password> https://<ip-address>/rest/interface/lte/monitor -d '{"numbers":"0", "once":""}' -H "content-type: application/json"
```

Export device configuration:

```bash
curl -k -u <username>:<password> https://<ip-address>/rest/export --data '{"compact":"","file":"test.rsc"}' -H "content-type: application/json"
```

Move a firewall entry (switch positions):

```bash
curl -k -u <username>:<password> -X POST https://<ip-address>/rest/ip/firewall/nat/move --data '{".id":"*9","destination":"*C"}' -H "content-type: application/json"
```

LTE firmware update:

```bash
curl -k -u <username>:<password> -X POST 'https://<ip-address>/rest/interface/lte/firmware-upgrade'   --data '{"numbers":"lte2"}' -H "content-type: application/json"
```

Get OIDs from `/system/resource` menu:

```bash
curl -k -u <username>:<password> -X POST https://<ip-address>/rest/system/resource/print --data '{"oid":""}' -H "content-type: application/json"
```

Use `/tool/fetch` to run a REST API POST from one RouterOS device to another RouterOS device:

```ros
/tool fetch http-method=post url="https://<ip-address>/rest/execute" \
http-data="{\"script\":\"/log info fetchtest\"}" \
http-header-field="Content-Type:application/json" \
output=user user=<username> password=<password>
```
