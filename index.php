<?php
	$link = mysqli_connect("127.0.0.1", "username", "password", "dbname");

	/* 检查连接 */
	if (mysqli_connect_errno()) {
		printf("Connect failed: %s\n", mysqli_connect_error());
		exit();
	}

	$date = $_GET['date'] ? mysqli_real_escape_string($link, $_GET['date']) : date("m月d日");
	$type = $_GET['type'] ? (int)mysqli_real_escape_string($link, $_GET['type']) : 0;
	$count = $_GET['count'] ? (int)mysqli_real_escape_string($link, $_GET['count']) : 1;
	$result = array();

	/* 创建一个预编译 SQL 语句 */
	if ($stmt = mysqli_prepare($link, "select * from `event` where `date` = ? and `type` = ? order by RAND() limit ?")) {

		/* 对于参数占位符进行参数值绑定 */
		mysqli_stmt_bind_param($stmt, "ssd", $date, $type, $count);

		/* 执行查询 */
		mysqli_stmt_execute($stmt);

		/* 将查询结果绑定到变量 */
		mysqli_stmt_bind_result($stmt, $id, $type, $year, $date, $info);

		/* 获取查询结果值 */
		while (mysqli_stmt_fetch($stmt)) {
			$arr = array('year' => $year, 'info' => $info);
			$result[] = $arr;
		};

		echo json_encode($result, JSON_UNESCAPED_UNICODE);

		/* 关闭语句句柄 */
		mysqli_stmt_close($stmt);
	}

	/* 关闭连接 */
	mysqli_close($link);
?>
