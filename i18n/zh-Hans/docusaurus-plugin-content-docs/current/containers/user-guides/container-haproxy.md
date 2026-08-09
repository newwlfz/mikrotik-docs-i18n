# Container - HAProxy

> 本文档介绍了如何在 MikroTik RouterOS 中将 HAProxy 配置为容器，提供使用 Certbot 设置带 HTTPS 支持的反向代理和负载均衡的分步指南。

# Container - HAProxy

HAProxy 是一个高性能的反向代理和负载均衡器，可作为容器运行。

为了获得最佳安全性，强烈建议使用像 HAProxy 这样的反向 HTTP/HTTPS 代理作为外部用户与内部服务之间的中介，而不是将容器直接暴露在网络中。

## 配置

要在 RouterOS 设备上设置 HAProxy 容器，请按照以下步骤操作。

:::info

在继续之前，请确保您已创建了 [Container 网络](../#networking-examples)。

:::

1. 创建 HAProxy 容器挂载点。

   ```routeros
   /container/mounts/add list=haproxy_etc src=disk1/haproxy-etc dst=/usr/local/etc/haproxy
   ```

2. 创建 HAProxy 容器。

   ```routeros
   /container/add remote-image=haproxy:latest interface=veth1 root-dir=disk1/haproxy mountlists=haproxy_etc user=0:0 name=haproxy
   ```

3. 使用 SFTP 客户端（例如，在 Microsoft Windows 上使用 WinSCP）连接到您的 RouterOS 设备，并创建一个新文件 `disk1/haproxy-etc/haproxy.cfg`，您可以使用以下配置作为示例。

```cfg
defaults
  mode http
  timeout client 10s
  timeout connect 10s
  timeout server 10s
  timeout http-request 10s

frontend http_synapse
  bind *:80
  use_backend synapse

backend synapse
  server server1 172.17.0.2:8008 maxconn 32
```

1. 启动 HAProxy 容器。

   ```routeros
   /container/start [find where name=haproxy]
   ```

## 高级：HAProxy 与 Certbot

此示例演示了如何配置 HAProxy 以提供 HTTPS 流量，并通过使用 Certbot 和 RFC2136 自动续期证书。

1. 创建 HAProxy 容器：

   ```routeros
   /container/mounts/add list=MOUNT_HAPROXY src=disk1/volumes/haproxy/config dst=/usr/local/etc/haproxy
   /container/add remote-image=haproxy:latest interface=veth1 root-dir=disk1/images/haproxy mountlists=MOUNT_HAPROXY name=haproxy start-on-boot=yes user=0:0 logging=yes
   ```

2. 在您的 PC 上创建一个名为 `haproxy.cfg` 的新文件，并将其上传到 `disk1/volumes/haproxy/config/`，根据您的需求调整配置：

```cfg
global
  log stdout format raw local0 info
  stats socket :9999 level admin expose-fd listeners
  ssl-default-bind-ciphers EECDH+AESGCM:EDH+AESGCM
  ssl-default-server-ciphers EECDH+AESGCM:EDH+AESGCM
  ssl-default-bind-options ssl-min-ver TLSv1.2
  ssl-default-server-options ssl-min-ver TLSv1.2
  tune.ssl.default-dh-param 2048
  tune.bufsize 43768
  tune.ssl.cachesize 1000000
  nbthread 8

defaults
  log global
  timeout client 10s
  timeout connect 10s
  timeout server 10s
  timeout http-request 10s

frontend frontend_webapp
  mode http
  option httplog
  option http-server-close
  option forwardfor except 127.0.0.0/8
  stick-table type ipv6 size 100k expire 30s store http_req_rate(10s)
  http-request track-sc0 src
  http-request deny deny_status 429 if { sc_http_req_rate(0) gt 10000 }
  bind *:80
  bind *:443 ssl crt /usr/local/etc/haproxy/certs/
  http-request redirect scheme https unless { ssl_fc }
  http-request set-header X-Forwarded-Host %[req.hdr(host)]
  http-request set-header X-Forwarded-For %[src]
  use_backend backend_webapp

backend backend_webapp
  mode http
  balance roundrobin
  option http-server-close
  option forwardfor
  server server1 172.17.0.2:8080

```

1. 创建 Certbot 容器：

   ```routeros
   /container/mounts/add list=MOUNT_CERTBOT_CONFIG src=disk1/volumes/certbot/config dst=/etc/letsencrypt
   /container/mounts/add list=MOUNT_CERTBOT_DATA src=disk1/volumes/certbot/data dst=/var/lib/letsencrypt
   /container/mounts/add list=MOUNT_CERTBOT_LOG src=disk1/volumes/certbot/log dst=/var/log/letsencrypt
   /container/mounts/add list=MOUNT_CERTBOT_HAPROXY src=disk1/volumes/haproxy/config dst=/etc/haproxy
   /container/add remote-image=certbot/dns-rfc2136 cmd="certonly -n --agree-tos --dns-rfc2136 --dns-rfc2136-credentials /etc/letsencrypt/rfc2136.ini -m admin@<FQDN> --deploy-hook 'cat /etc/letsencrypt/li\
       ve/<FQDN>/fullchain.pem /etc/letsencrypt/live/<FQDN>/privkey.pem | tee /etc/haproxy/certs/<FQDN>.pem > /dev/null; echo -e \"set ssl cert /usr/local/e\
       tc/haproxy/certs/<FQDN>.pem <<\
       \n\$(cat /etc/haproxy/certs/<FQDN>.pem)\
       \n\" | nc 127.0.0.1:9999; echo \"commit ssl cert /usr/local/etc/haproxy/certs/<FQDN>.pem\" | nc 127.0.0.1:9999' -d <FQDN> --cert-name <FQDN>" \
       interface=veth1 logging=yes mountlists=MOUNT_CERTBOT_CONFIG,MOUNT_CERTBOT_DATA,MOUNT_CERTBOT_LOG,MOUNT_CERTBOT_HAPROXY name=certbot root-dir=\
       disk1/images/certbot start-on-boot=yes workdir=/opt/certbot

   ```

:::warning

请确保将上述示例中的所有 `<FQDN>` 占位符替换为您实际的完全限定域名！

:::

1. 等待容器镜像下载完成，然后启动 Certbot 容器：

   ```routeros
   /container/start [find where name=certbot]
   ```

2. 检查日志以确保您成功获取了新证书：

   ```routeros
   /log/print follow
   ```

3. 启动 HAProxy 容器：

   ```routeros
   /container/start [find where name=haproxy]
   ```

4. 设置一个计划任务，例如，每天 06:30 检查新证书：

   ```routeros
   /system/scheduler
   add interval=1d name=SCHEDULE_RenewCertbot on-event=SCRIPT_RenewCertbot policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon start-date=\
       2025-03-10 start-time=06:30:00
   /system/script
   add dont-require-permissions=no name=SCRIPT_RenewCertbot owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source=\
       "/container/start [find where name=\"certbot\"]"
   ```

5. 完成

证书将自动续期并替换 HAProxy 中的旧证书，无需重启容器。