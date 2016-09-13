#!/usr/bin/python
#encoding:utf8

import MySQLdb

def queryData(sql):
	conn = MySQLdb.connect(host="localhost",user="root",passwd="test",db="test",charset="utf8")
	cursor = conn.cursor()
	cursor.execute(sql)
	row = cursor.fetchall()
	cursor.close()
	conn.close()
	return row

def executeData(sql):
	conn = MySQLdb.connect(host="localhost",user="root",passwd="test",db="test",charset="gbk")
	cursor = conn.cursor()
	cursor.execute(sql)
	conn.commit()
	cursor.close()
	conn.close()
	return 1
