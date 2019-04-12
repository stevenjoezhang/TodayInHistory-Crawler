#!/usr/bin/env python3

username = "username"
password = "password"
dbname = "dbname"

import requests
from bs4 import BeautifulSoup
import re
import datetime
import pymysql

conn = pymysql.connect(host = "127.0.0.1", user = username, password = password, db = dbname, charset = "utf8")
print(conn)
cur = conn.cursor()

def savedb(data):
	print(data)
	try:
		cur.execute("insert into event values(null,%s,%s,%s,%s)", data)
	except pymysql.err.InternalError:
		print("\033[31mERROR: Incorrect string value.\033[0m", data)
		with open("failed.txt", "a") as myfile:
			myfile.write(str(data) + "\n")
	except pymysql.err.DataError:
		print("\033[31mERROR: Data too long.\033[0m", data)
		with open("failed.txt", "a") as myfile:
			myfile.write(str(data) + "\n")

def getDateList():
	list = []
	date = datetime.date(2016, 1, 1)
	for i in range(366):
		date_str = str(date.month) + "月" + str(date.day) + "日"
		list.append(date_str)
		date += datetime.timedelta(days = 1)
	return list

def getInfo(html, type, date):
	typeList = ["大事记", "出生", "逝世"]
	flag = re.compile("(<h2><span id=.*<span class=\"mw-headline\" id=.*?" + typeList[type] + "[\s\S]*?</ul>\s*?)<h2>").search(html)
	if flag:
		bsObj = BeautifulSoup(flag.group(1), "html.parser").findAll("li")
		for li in bsObj:
			match = re.compile("((^前|^)\d{1,4}年)：([\s\S]*$)").match(li.get_text())
			if match:
				year = match.group(1)
				info = re.sub("\[\d{1,}\]", "", match.group(3).strip())
				data = (type, year, date, info)
				savedb(data)

list = getDateList()
for date in list:
	print(date)
	url = "https://zh.wikipedia.org/zh-cn/%s" % date
	r = requests.get(url)
	getInfo(r.text, 0, date) # 大事记
	getInfo(r.text, 1, date) # 出生
	getInfo(r.text, 2, date) # 逝世

cur.connection.commit()
cur.close()
conn.close()
