# CHR：VMware ESXi 安装

> 本文档记录了在 VMware ESXi 上安装和配置 MikroTik CHR 的过程，涵盖支持的网络接口（vmxnet3、E1000）和磁盘控制器（IDE、VMware Paravirtual SCSI），以及通过调整 MTU 设置和重新配置接口来启用巨型帧的说明。

# CHR：VMware ESXi 安装

## 支持的网络和磁盘接口

### VMware ESXi

**网络适配器：**

- vmxnet3
- E1000

**磁盘控制器：**

- IDE
- VMware Paravirtual SCSI
- LSI Logic SAS
- LSI Logic Parallel

#### ESXi

在用于虚拟机的端口组或虚拟交换机上启用混杂模式。

**ESXi 文档：**

- https://kb.vmware.com/kb/1004099

### 在 VMware ESXi 上运行

#### 更改 MTU

VMware ESXi 支持最高 9000 字节的 MTU 值。要利用巨型帧，请调整 ESXi 安装以允许更高的 MTU。

**重要提示：** 在 MTU 更改**之后**添加的虚拟以太网接口将正确支持巨型帧。但是，在 MTU 更改**之前**添加的接口将受限于原始 MTU 值。如果您在更改 MTU 之前已配置了接口，则必须将其从虚拟客户机中移除并重新添加。

**示例：** 添加到 ESXi 客户机的两个接口根据添加时间显示不同的 MTU 值：

```
[admin@chr-vm] > interface ethernet print 
Flags: X - disabled, R - running, S - slave 
 #    NAME           MTU MAC-ADDRESS       ARP       
 0 R  ether1        9000 00:0C:29:35:37:5C enabled   
 1 R  ether2        1500 00:0C:29:35:37:66 enabled
```