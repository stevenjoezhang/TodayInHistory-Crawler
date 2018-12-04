#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import datetime
import re
import mysql

typeList = ["大事记", "出生", "逝世"]

def getDateList():
	list = []
	date = datetime.date(2016, 1, 1)
	for i in range(366):
		date_str = str(date.month) + "月" + str(date.day) + "日"
		list.append(date_str)
		date += datetime.timedelta(days = 1)
	return list

def getInfo(html, type, date):
	flag = re.compile("(<h2><span id=.*<span class=\"mw-headline\" id=.*?" + typeList[type] + "[\s\S]*?</ul>\s*?)<h2>").search(html)
	if flag:
		bsObj = BeautifulSoup(flag.group(1), "html.parser").findAll("li")
		for li in bsObj:
			match = re.compile("((^前|^)\d{1,4}年)：([\s\S]*$)").match(li.get_text())
			if match:
				year = match.group(1)
				info = re.sub("\[\d{1,}\]", "", match.group(3).strip())
				data = (type, year, date, info)
				print(data)
				mysql.savedb(data)

def main():
	list = getDateList()
	for date in list:
		print(date)
		url = "https://zh.wikipedia.org/zh-cn/%s" % date
		#url = "https://api.galaxymimi.com/proxy/?url=https://zh.wikipedia.org/zh-cn/%s" % date
		r = requests.get(url)
		getInfo(r.text, 0, date)  # 大事记
		getInfo(r.text, 1, date)  # 出生
		getInfo(r.text, 2, date)  # 逝世

if __name__ == '__main__':
	main()
