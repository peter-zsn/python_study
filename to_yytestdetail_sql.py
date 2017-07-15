#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: tosql.py
@time: 2017/6/27 9:32
112中的u_yy_test_detail中的小学英语作业， 转移到130中yy_test_detail1中，数据量300378
"""
import MySQLdb
import time
import json

big_host = '116.255.220.112'
big_name = 'renwanxing'
big_pwd = 'ohStjN6DKXqdfBAfhGzdz'
big_db = 'tbkt_web'

big_conn = MySQLdb.connect(big_host, big_name, big_pwd, big_db, charset='utf8')     # 连接mysql 112
big_cur = big_conn.cursor()
task_nums_sql = """
SELECT count(t.id) FROM (SELECT id, GROUP_CONCAT(question_id) FROM u_yy_test_detail GROUP BY test_id) t;
                """
big_cur.execute(task_nums_sql)
big_recode = big_cur.fetchone()
big_cur.close()
big_conn.close()
task_nums = int(big_recode[0])          # 计算出总数据量
# 每次执行500条
page = task_nums / 500 + 1
print task_nums, page
for i in range(page):
    big_conn = MySQLdb.connect(big_host, big_name, big_pwd, big_db, charset='utf8')     # 连接mysql 112
    big_cur = big_conn.cursor()
    start = i * 500
    sql = """
    SELECT id, test_id, GROUP_CONCAT(question_id), GROUP_CONCAT(ask_id),
     GROUP_CONCAT(result), GROUP_CONCAT(answer), GROUP_CONCAT(option_id)
     FROM u_yy_test_detail GROUP BY test_id limit %s, 500;
        """ % start
    print sql
    big_cur.execute(sql)
    big_recode = big_cur.fetchall()
    my_detail = []
    for (id, test_id, question_id, ask_id, result, answer, option_id) in big_recode:
        qids = question_id.split(',')
        ask_ids = ask_id.split(',')
        answers = answer.split(',')
        results = result.split(',')
        option_ids = option_id.split(',')
        text = []
        for i in range(len(qids)):
            text.append({"qid": qids[i], "aid": ask_ids[i], "result": results[i], "answer": answers[i], "oid": option_ids[i]})
        text = json.dumps(text)
        d = dict(
            id=id,
            test_id=test_id,
            text=text
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

    insert_sql = "insert into yy_test_detail1 (%s) VALUES (%s)" % (fields, tokens)

    args = [o.values() for o in my_detail]
    my_cur.executemany(insert_sql, args)
    my_conn.commit()
    my_cur.close()
    my_conn.close()

