#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: sql.py
@time: 2017/6/28 10:06
"""

import MySQLdb

# 112数据库信息
BIG_HOST = '116.255.220.112'
BIG_NAME = 'renwanxing'
BIG_PWD = '********'
BIG_DB = 'tbkt'

# 130数据库信息
LOCAL_HOST = '192.168.7.250'
LOCAL_NAME = 'dba_user'
LOCAL_PWD = 'tbkt123456'
LOCAL_DB = 'tbkt_yingyu'

def big_fetchall(sql):
    big_conn = MySQLdb.connect(BIG_HOST, BIG_NAME, BIG_PWD, BIG_DB, charset='utf8')  # 连接mysql 112
    big_cur = big_conn.cursor()
    big_cur.execute(sql)
    big_recode = big_cur.fetchall()
    big_cur.close()
    big_conn.close()
    return big_recode

def big_sql_count(sql):
    big_conn = MySQLdb.connect(BIG_HOST, BIG_NAME, BIG_PWD, BIG_DB, charset='utf8')  # 连接mysql 112
    big_cur = big_conn.cursor()
    big_cur.execute(sql)
    big_recode = big_cur.fetchone()
    big_cur.close()
    big_conn.close()
    if big_recode:
        return int(big_recode[0])
    else:
        return 0

def local_insert(table_name, details):
    my_conn = MySQLdb.connect(LOCAL_HOST, LOCAL_NAME, LOCAL_PWD, LOCAL_DB, charset='utf8')  # 连接mysql 130
    my_cur = my_conn.cursor()
    kw = details[0]
    fields = ["`%s`" % k for k in kw.keys()]
    fields = ','.join(fields)
    tokens = ','.join(['%s'] * len(kw))

    insert_sql = "insert into %s (%s) VALUES (%s)" % (table_name, fields, tokens)
    args = [o.values() for o in details]
    my_cur.executemany(insert_sql, args)
    my_conn.commit()
    my_cur.close()
    my_conn.close()

def local_sql_count(sql):
    my_conn = MySQLdb.connect(LOCAL_HOST, LOCAL_NAME, LOCAL_PWD, LOCAL_DB, charset='utf8')  # 连接mysql 130
    my_cur = my_conn.cursor()
    my_cur.execute(sql)
    my_recode = my_cur.fetchone()
    my_cur.close()
    my_conn.close()
    if my_recode:
        return int(my_recode[0])
    else:
        return 0
