# 接地

> MikroTik RouterOS 设备的接地要求强调正确安装屏蔽电缆、避雷器以及使用 2.5-4 mm² 铜线（配耐腐蚀连接器）的可靠接地基础设施，包括 RouterBOARD 单元上的特定连接点。

# 接地

## 简介

屏蔽电缆安装基础设施（铁塔和桅杆）、天线以及路由器本身必须正确接地。所有外部天线电缆上必须安装避雷器（靠近天线或在天线本身上），以防止设备损坏和人员受伤。请注意，如果避雷器未正确接地，则无法发挥效用。

使用 2.5-4 mm² 铜线（AWG 11–13）并配耐腐蚀连接器进行接地。确保您使用的接地基础设施完全有效（不仅仅是装饰性的，如某些安装中所见）：

1. 对于屏蔽连接器，请使用屏蔽电缆，因为它们提供更好的抗干扰能力。
2. 如果 RouterBOARD 提供了接地线连接点，接地线应连接到该连接点。此线缆随后应连接到铁塔底座，确保连接符合接地标准。天线的接地线应连接到 RouterBOARD 室外机壳附近，并可并入用于 RouterBOARD 的同一接地线。

## 屏蔽 RJ45 端口与非屏蔽 RJ45 端口

### 带屏蔽端口的设备

![shielded.png](https://manual.mikrotik.com/docs/hardware/img/grounding-01.webp)
![](https://manual.mikrotik.com/docs/hardware/img/grounding-diagram.png)

### 带非屏蔽端口的设备

![unshielded.png](https://manual.mikrotik.com/docs/hardware/img/grounding-02.webp)

### 带屏蔽连接器的 PoE 供电器

![poeinjector.png](https://manual.mikrotik.com/docs/hardware/img/grounding-03.webp)

## RouterBOARD 接地线连接点

![](https://manual.mikrotik.com/docs/hardware/img/grounding-04.webp)

![screw1.png](https://manual.mikrotik.com/docs/hardware/img/grounding-05.webp)

![screw2.png](https://manual.mikrotik.com/docs/hardware/img/grounding-06.webp)

:::info
如果供电设备（PSE）的正极端子连接到保护接地（PE），则不应将其用于为 MikroTik 设备供电。这可能导致短路，对您和您的设备造成伤害。
:::