#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: kill_wrongsql.py.py
@time: 2017/6/28 9:23
"""

import MySQLdb
import time
import json
import logging

big_host = '116.255.220.112'
big_name = 'renwanxing'
big_pwd = 'ohStjN6DKXqdfBAfhGzdz'
big_db = 'tbkt'

big_conn = MySQLdb.connect(big_host, big_name, big_pwd, big_db, charset='utf8')     # 连接mysql 112
big_cur = big_conn.cursor()
sql = """
        SELECT td.id, td.task_id, td.catalog_id, td.text_catalog_id, td.question_id,  td.content_type FROM u_task_detail td
 INNER JOIN u_task t ON t.id= td.task_id and t.subject_id = 91 AND t.id=628620 and td.content_type = 1 ORDER BY id
     """
big_cur.execute(sql)
big_recode = big_cur.fetchall()
big_cur.close()
big_conn.close()

id_new = big_recode[0][0]
task_id_new = big_recode[0][1]
text = []
for (id, task_id, catalog_id, text_catalog_id, question_id, content_type) in big_recode:
    d = dict(
        cid=catalog_id,
        tcid=text_catalog_id,
        qid=question_id
    )
    text.append(d)
text = json.dumps(text)

d = dict(
    id=id_new,
    task_id=task_id_new,
    text=text,
    content_type=content_type
)
my_detail = []
my_detail.append(d)

my_host = '192.168.7.250'
my_name = 'dba_user'
my_pwd = 'tbkt123456'
my_db = 'tbkt_yingyu'

my_conn = MySQLdb.connect(my_host, my_name, my_pwd, my_db, charset='utf8')     # 连接mysql 130
my_cur = my_conn.cursor()
kw = my_detail[0]
fields = ["`%s`" % k for k in kw.keys()]
fields = ','.join(fields)
tokens = ','.join(['%s'] * len(kw))

insert_sql = "insert into yy_task_detail1 (%s) VALUES (%s)" % (fields, tokens)
args = [o.values() for o in my_detail]
my_cur.executemany(insert_sql, args)
my_conn.commit()
my_cur.close()
my_conn.close()
