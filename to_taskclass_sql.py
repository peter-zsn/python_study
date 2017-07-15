#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: tosql.py
@time: 2017/6/27 9:32
112中的u_task_class中的小学英语作业， 转移到130中yy_task_class中，数据量55333
"""
import MySQLdb
import time
import json

big_host = '116.255.220.112'
big_name = 'renwanxing'
big_pwd = 'ohStjN6DKXqdfBAfhGzdz'
big_db = 'tbkt'

big_conn = MySQLdb.connect(big_host, big_name, big_pwd, big_db, charset='utf8')     # 连接mysql 112
big_cur = big_conn.cursor()
task_nums_sql = """
              SELECT count(tc.id) FROM u_task t INNER JOIN u_task_class tc ON tc.task_id = t.id WHERE t.subject_id = 91;
            """
big_cur.execute(task_nums_sql)
big_recode = big_cur.fetchone()
big_cur.close()
big_conn.close()
task_nums = int(big_recode[0])          # 计算出总数据量
# 每次执行500条
page = task_nums / 500 + 1


for i in range(page):
    big_conn = MySQLdb.connect(big_host, big_name, big_pwd, big_db, charset='utf8')     # 连接mysql 112
    big_cur = big_conn.cursor()
    start = i * 500
    sql = """SELECT tc.id, tc.task_id, tc.unit_class_id, tc.type, tc.student_id, UNIX_TIMESTAMP(tc.add_time)
              FROM u_task_class tc INNER JOIN u_task t ON t.id = tc.task_id AND t.subject_id = 91 LIMIT %s, 500;
          """ % start
    print sql
    big_cur.execute(sql)
    big_recode = big_cur.fetchall()
    my_detail = []
    for (id, task_id, unit_class_id, type, student_id,
         add_time) in big_recode:
        d = dict(
            id=id,
            task_id=task_id,
            unit_class_id=unit_class_id,
            type=type,
            student_id=student_id,
            add_time=add_time,
        )
        my_detail.append(d)

    big_cur.close()
    big_conn.close()

    my_host = '192.168.7.250'
    my_name = 'dba_user'
    my_pwd = 'tbkt123456'
    my_db = 'tbkt_yingyu'

    my_conn = MySQLdb.connect(my_host, my_name, my_pwd, my_db, charset='utf8')     # 连接mysql 130
    my_cur = my_conn.cursor()

    kw = my_detail[0]
    fields = ["`%s`"%k for k in kw.keys()]
    fields = ','.join(fields)
    tokens = ','.join(['%s']*len(kw))

    insert_sql = "insert into yy_task_class1 (%s) VALUES (%s)" % (fields, tokens)

    args = [o.values() for o in my_detail]
    my_cur.executemany(insert_sql, args)
    my_conn.commit()
    my_cur.close()
    my_conn.close()
