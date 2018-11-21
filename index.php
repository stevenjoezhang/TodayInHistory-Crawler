<?php
	//生成一个连接
	$db_connect = mysqli_connect("127.0.0.1", "username", "password");

	$date = $_GET['date'] ? mysqli_real_escape_string($db_connect, $_GET['date']) : date("m月d日");
	$type = $_GET['type'] ? mysqli_real_escape_string($db_connect, $_GET['type']) : 0;

	//选择一个需要操作的数据库
	mysqli_select_db($db_connect, "dbname");

	// 获取查询结果
	$strsql = "select * from `event` where `date` = '$date' and `type` = '$type' order by RAND() limit 1";
	$result = mysqli_query($db_connect, $strsql);

	// 循环取出记录
	while ($row = mysqli_fetch_array($result)) {
		$year = $row['year'];
		$info = $row['info'];
	}

	// 释放资源
	mysqli_free_result($result);
	// 关闭连接
	mysqli_close($db_connect);
	$arr = array('year' => $year, 'info' => $info);
	echo json_encode($arr, JSON_UNESCAPED_UNICODE);
?>
