<?php
	$mysqli = new mysqli("localhost", "username", "password", "dbname");

	/* 检查连接 */
	if (mysqli_connect_errno()) {
		printf("Connect failed: %s\n", mysqli_connect_error());
		exit();
	}

	$date = $_GET['date'] ? $mysqli->real_escape_string($_GET['date']) : date("m月d日");
	$type = $_GET['type'] ? (int)$mysqli->real_escape_string($_GET['type']) : 0;
	$count = $_GET['count'] ? (int)$mysqli->real_escape_string($_GET['count']) : 1;
	$result = array();

	/* 创建一个预编译 SQL 语句 */
	if ($stmt = $mysqli->prepare("select * from `event` where `date` = ? and `type` = ? order by RAND() limit ?")) {

		/* 对于参数占位符进行参数值绑定 */
		$stmt->bind_param("dii", $date, $type, $count);

		/* 执行查询 */
		$stmt->execute();

		/* 将查询结果绑定到变量 */
		$stmt->bind_result($id, $type, $year, $date, $info);

		/* 获取查询结果值 */
		while ($stmt->fetch()) {
			$arr = array('year' => $year, 'info' => $info);
			$result[] = $arr;
		};

		echo json_encode($result, JSON_UNESCAPED_UNICODE);

		/* 关闭语句句柄 */
		$stmt->close();
	}

	/* 关闭连接 */
	$mysqli->close();
?>
