#!/usr/bin/env python3
import pymysql

def savedb(data):
	conn = pymysql.connect(host = "127.0.0.1", user = "username", password = "password", db = "dbname", charset = "utf8")
	print(conn)
	cur = conn.cursor()
	try:
		cur.execute("insert into event values(%s,%s,%s,%s)", data)
	except pymysql.err.InternalError:
		print("\033[31mERROR: Incorrect string value.\033[0m", data)
		with open("errors.txt", "a") as myfile:
			myfile.write(str(data) + "\n")
	except pymysql.err.DataError:
		print("\033[31mERROR: Data too long.\033[0m", data)
		with open("errors.txt", "a") as myfile:
			myfile.write(str(data) + "\n")
	cur.connection.commit()
	cur.close()
	conn.close()
