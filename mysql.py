#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: mysql.py
@time: 2017/3/13 11:28
"""

import MySQLdb
import time

HOST = '116.255.220.112'
PORT = 3306
USER = '******'
PASSWD = '*******'

conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db='tbkt')

cur = conn.cursor()

sql = "SELECT GROUP_CONCAT(content_type)  FROM u_task_detail td " \
      "WHERE td.task_id in (SELECT task_id FROM tbkt_web.u_yy_task_progress WHERE user_id = 2731972 " \
      "AND update_time >= unix_timestamp('2017-4-4 12:00:00') AND  update_time <= unix_timestamp('2017-4-7 12:00:00')) GROUP BY td.task_id;"

result = cur.execute(sql)
b = cur.fetchall()
a = 0
for o in b:
    # print o[0], type(o[0]), len(o[0])
    c = o[0]
    d = c.split(',')
    e = set([s for s in d if s])
    # print d, len(d)
    a += len(e)

print a
