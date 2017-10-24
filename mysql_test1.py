#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: mysql_test1.py
@time: 2017/7/28 9:25
"""


import MySQLdb

con = MySQLdb.connect('192.168.8.37', 'root', '123456', 'tmp')
cur = con.cursor()

data = cur.execute('SELECT VERSION()')
print data
cur.close()
con.close()