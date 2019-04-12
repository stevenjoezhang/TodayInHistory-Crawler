#!/usr/bin/env python3

username = "username"
password = "password"
dbname = "dbname"

import datetime
import pymysql
from flask import Flask
from flask import request

app = Flask(__name__)

conn = pymysql.connect(host = "127.0.0.1", user = username, password = password, db = dbname, charset = "utf8")
print(conn)
cur = conn.cursor()

@app.route("/", methods = ["GET", "POST"])
def query():
	date = datetime.date.today()
	today = str(date.month) + "月" + str(date.day) + "日"
	_date = request.args.get("date") or today
	_type = int(request.args.get("type") or 0)
	_count = int(request.args.get("count") or 1)
	cur.execute("select * from `event` where `date` = %s and `type` = %s order by RAND() limit %s", (_date, _type, _count))
	rows = cur.fetchall()
	result = []
	for row in rows:
		result.append({"year": row[2], "info": row[4]})
	return str(result)

app.run(debug = True, port = 8080, host = "0.0.0.0")
