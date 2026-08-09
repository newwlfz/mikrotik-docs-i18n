# CHR：AWS 安装指南

> 本页面指导用户通过将原始磁盘镜像导入为 AMI 并在 Amazon Web Services (AWS) 上启动 EC2 实例，来部署 MikroTik CHR。

# CHR：AWS 安装指南

Amazon Web Services (AWS) 的 Marketplace 中不直接提供 MikroTik CHR。要在 AWS 上部署 CHR，您需要将原始磁盘镜像导入为 Amazon Machine Image (AMI)，然后从中启动 EC2 实例。

## 前提条件

- 一个具有使用 EC2、S3 和 VM Import/Export 服务权限的 AWS 账户。
- 在本地机器上安装并配置了 [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)。
- 一个用于上传 CHR 磁盘镜像的 S3 存储桶。

:::info
IAM 用户或角色必须配置 `vmimport` 服务角色。有关所需权限和信任策略，请参阅 [AWS VM Import/Export 文档](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html)。
:::

## 步骤 1：下载 CHR 原始磁盘镜像

1. 访问 [MikroTik 下载页面](https://mikrotik.com/download)。
2. 找到适用于您目标架构的最新稳定版 **CHR 原始磁盘镜像**（`.img` 文件）。
3. 下载并解压归档文件。

## 步骤 2：将镜像上传到 S3

将原始 `.img` 文件上传到您的 S3 存储桶：

```bash
aws s3 cp chr-x.x.x.img s3://YOUR-BUCKET-NAME/chr-x.x.x.img
```

将 `YOUR-BUCKET-NAME` 替换为您实际的 S3 存储桶名称，将 `x.x.x` 替换为 RouterOS 版本号。

## 步骤 3：创建导入清单

创建一个描述导入过程磁盘镜像的 JSON 文件（例如 `containers.json`）：

```json
{
  "Description": "MikroTik RouterOS CHR",
  "Format": "raw",
  "UserBucket": {
    "S3Bucket": "YOUR-BUCKET-NAME",
    "S3Key": "chr-x.x.x.img"
  }
}
```

## 步骤 4：导入快照

启动快照导入并捕获任务 ID：

```bash
aws ec2 import-snapshot \
  --description "MikroTik RouterOS CHR" \
  --disk-container file://containers.json
```

输出中包含一个 `ImportTaskId`。使用它来监控进度：

```bash
aws ec2 describe-import-snapshot-tasks \
  --import-task-ids import-snap-xxxxxxxxxxxxxxxxx
```

等待状态显示为 `completed`。输出中将包含 `SnapshotId`。

## 步骤 5：注册 AMI

将导入的快照注册为 AMI：

```bash
aws ec2 register-image \
  --name "MikroTik RouterOS CHR" \
  --description "MikroTik RouterOS CHR" \
  --architecture x86_64 \
  --virtualization-type hvm \
  --ena-support \
  --root-device-name "/dev/sda1" \
  --block-device-mappings "[{\"DeviceName\": \"/dev/sda1\", \"Ebs\": { \"SnapshotId\": \"snap-xxxxxxxxxxxxxxxxx\"}}]"
```

将 `SnapshotId` 替换为上一步骤中的值。输出中包含一个 `ImageId` — 这就是您的新 AMI。

## 步骤 6：启动 EC2 实例

1. 打开 [EC2 控制台](https://console.aws.amazon.com/ec2/)。
2. 导航到 **镜像 > AMI**，找到您新的 CHR AMI。
3. 选择它并点击 **启动**。
4. 选择实例类型（例如，用于测试的 `t3.micro`）。
5. 根据需要配置网络、安全组和密钥对。
6. 启动实例。

:::warning
确保您的安全组仅允许从您的管理 IP 访问 SSH（端口 22）和 WinBox（端口 8291）。首次登录后请立即保护路由器安全 — 请参阅 [保护您的路由器](../../../securing-your-router.md)。
:::

## 步骤 7：连接到 CHR

1. 使用实例的公有 IP 通过 SSH 连接：

   ```ros
   ssh admin@INSTANCE_PUBLIC_IP
   ```

2. 首次登录时，请查看软件许可协议并设置强密码。
3. 继续进行配置。有关生产环境设置指南，请参阅 [首次配置](../../../first-time-configuration.md)。

:::tip
AWS 默认不分配公有 IP。请确保您的实例具有公有 IP 或关联了弹性 IP，并且安全组允许入站 SSH 访问。
:::