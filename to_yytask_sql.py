#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: tosql.py
@time: 2017/6/27 9:32
112中的u_task中的小学英语作业， 转移到130中yy_task中，数据量27382
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
SELECT count(id) FROM u_task WHERE subject_id = 91;
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
    sql = "SELECT id, type, object_id, add_user, title, sms_content, status, UNIX_TIMESTAMP(add_time)," \
          " UNIX_TIMESTAMP(begin_time), UNIX_TIMESTAMP(end_time), is_sendpwd" \
          " FROM u_task WHERE subject_id = 91 ORDER BY id LIMIT %s, 500;" % start
    print sql
    big_cur.execute(sql)
    big_recode = big_cur.fetchall()
    my_detail = []
    for (id, type_id, object_id, add_user, title, sms_content,
         status, add_time, begin_time, end_time, is_sendpwd) in big_recode:
        d = dict(
            id=id,
            type=type_id,
            object_id=object_id,
            add_user=add_user,
            title=title,
            sms_content=sms_content,
            status=status,
            add_time=add_time,
            begin_time=begin_time,
            end_time=end_time,
            is_sendpwd=is_sendpwd
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

    insert_sql = "insert into yy_task1 (%s) VALUES (%s)" % (fields, tokens)

    args = [o.values() for o in my_detail]
    my_cur.executemany(insert_sql, args)
    my_conn.commit()
    my_cur.close()
    my_conn.close()

