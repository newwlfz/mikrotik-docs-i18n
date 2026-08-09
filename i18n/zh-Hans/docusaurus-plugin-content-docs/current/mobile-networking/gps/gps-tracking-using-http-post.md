# 使用 HTTP POST 进行 GPS 追踪

> 本页说明如何利用 MikroTik RouterOS 的 GPS 功能及 HTTP POST 方式，将坐标发送至 Web 服务器，并存储于 SQLite3 数据库中，以便通过 Leaflet.js 进行可视化展示。

# 使用 HTTP POST 进行 GPS 追踪

以下文章将介绍如何利用 RouterOS 的 GPS 功能及脚本，创建一个简易的车辆追踪系统。

## 方法

此方案利用了 RouterOS Fetch 工具的 HTTP POST 功能。它允许您直接从 RouterOS 命令行向 Web 服务器 POST 任意类型的数据。当然，您也可以使用脚本将变量填充至 POST 数据中。POST 的数据将被写入 SQLite3 数据库（若文件不存在则会自动创建），随后从数据库中读取并输入至 Leaflet.js 的 Polyline 数组。此示例仅为概念验证；不包含身份验证、安全性或错误处理机制。

## 需求

- 任意 Web 服务器。
- PHP。
- 适用于 PHP 的 SQLite3 模块。
- 带有可用 GPS 模块的 RouterOS 设备。
- RouterOS。
- 将 RouterOS 中的 GPS 格式设置为 **dd**。

## RouterOS 脚本

您可以在 Scheduler 工具中运行此脚本，设置间隔为 1 秒，以便每秒钟发送一次坐标。

```ros
{
:global lat
:global lon
/system/gps/monitor once do={
:set $lat $("latitude")
:set $lon $("longitude")
}
/tool/fetch mode=http url="http://YOURSERVER.com/index.php" port=80 http-method=post http-data=("{\"lat\":\"" . $lat . "\",\"lon\":\"" . $lon . "\"}") http-header-field="Content-Type: application/json" 
:put ("{\"lat\":\"" . $lat . "\",\"lon\":\"" . $lon . "\"}")
}
```

## index.php 文件

在 index.php 文件旁边创建一个名为 **sqlite\_db** 的空目录。确保该目录及文件对用户组可写，使用 **chmod -R a+w sqlite\_db/** 命令。

```ros
<?php
$loc = dirname(__FILE__).'/sqlite_db/coord.db';
$db = new SQLite3($loc,SQLITE3_OPEN_READWRITE | SQLITE3_OPEN_CREATE);
$raw = file_get_contents('php://input');
$raw = preg_replace('/\\x00/','',$raw);
$data = json_decode($raw);

if (!empty($data) && is_object($data) && property_exists($data,'lat') && property_exists($data,'lon')){
    if(file_exists($loc)) echo 'exists!'.chr(0xa);
    $src = 'SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'coordinates\'';
    $res = $db->querySingle($src);
    if ($res === false){
            $db->exec('CREATE TABLE coordinates (latitude TEXT, longitude TEXT, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, added TIMESTAMP DEFAULT CURRENT_TIMESTAMP ) ');
    }
    
$regex = '/^(|\-)([0-9]{2,3}\.[0-9]{0,8})$/';

if (preg_match($regex,$data->lat) && preg_match($regex,$data->lon) )
	{
		$lat = $data->lat;
		$lon = $data->lon;
	}
	$ins = 'INSERT INTO coordinates (latitude,longitude) VALUES (\''.SQLite3::escapeString($lat).'\',\''.SQLite3::escapeString($lon).'\')';
	$db->exec($ins);
	die();
}
?>

<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.3.1/dist/leaflet.css" integrity="sha512-Rksm5RenBEKSKFjgI3a41vrjkw4EVPlJ3+OiI65vTjIdo9brlAacEuKOiQ5OFh7cOI1bkDwLqdLw3Zg0cRJAAQ==" crossorigin=""/>
  <script src="https://unpkg.com/leaflet@1.3.1/dist/leaflet.js" integrity="sha512-/Nsx9X4HebavoBvEBuyp3I7od5tA0UzAxs+j83KgC8PU0kgB4XiK4Lfe4y4cgBtaRJQEIFCW+oC506aPT2L1zw==" crossorigin=""></script>
</head>
<body>

<script>
var map = L.map('map').setView([0,0], 4);
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {attribution: 'OSM'}).addTo(map);

<?php
    if($result = $db->query('SELECT latitude,longitude FROM coordinates')){
    echo ' var latlngs = [ ';
    while($obj = $result->fetchArray()){
    	if (!is_array($obj) || !isset($obj['latitude']) || !isset($obj['longitude']) || empty($obj['latitude']) || empty($obj['longitude'])) continue;
    	echo '["'. $obj['latitude'].'","'.$obj['longitude'].'"],';
    }
    echo ']; ';
    } else
     echo('//'.$db->lastErrorMsg().chr(0xa));  

?>
var polyline = L.polyline(latlngs, {color: 'red'}).addTo(map);
map.fitBounds(polyline.getBounds());
</script>
</body>
</html>
```

## 结果

![](https://manual.mikrotik.com/docs/mobile-networking/gps/img/gps-tracking-using-http-post-01.webp)