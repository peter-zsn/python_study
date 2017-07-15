#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: tosql.py
@time: 2017/6/27 9:32
"""
import MySQLdb
import time
import json
import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='sql.log',
                filemode='w')

logging.info('This is info message')


big_host = '116.255.220.112'
big_name = 'renwanxing'
big_pwd = 'ohStjN6DKXqdfBAfhGzdz'
big_db = 'tbkt'

# 共205044条数据     SELECT count(*) FROM u_task_detail td INNER JOIN u_task t ON t.id = td.task_id AND t.subject_id = 91;
# 先查询u_task表，发现有27378， 每次先查询100条作业，再把作业详细表导入  27300  剩余78条作业
# 目前到 793458这条数据id
"""
SELECT td.id, td.task_id, GROUP_CONCAT(td.catalog_id),
GROUP_CONCAT(td.text_catalog_id), GROUP_CONCAT(td.question_id), td.content_type
                FROM u_task_detail td
                 INNER JOIN u_task t ON t.id = td.task_id AND t.subject_id=91 GROUP BY td.task_id, td.content_type ORDER BY id;
                 共36392条 最后一条的id是5422899
"""

big_conn = MySQLdb.connect(big_host, big_name, big_pwd, big_db, charset='utf8')     # 连接mysql 112
big_cur = big_conn.cursor()
task_nums_sql = """
SELECT COUNT(c.id) FROM (
SELECT td.id, td.task_id, GROUP_CONCAT(td.catalog_id), GROUP_CONCAT(td.text_catalog_id), GROUP_CONCAT(td.question_id),
content_type FROM u_task_detail td
INNER JOIN u_task t ON t.id= td.task_id and t.subject_id = 91 GROUP BY task_id, content_type) c;
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
    sql = """SELECT td.id, td.task_id, GROUP_CONCAT(td.catalog_id), GROUP_CONCAT(td.text_catalog_id),
 GROUP_CONCAT(td.question_id), content_type FROM u_task_detail td
 INNER JOIN u_task t ON t.id= td.task_id and t.subject_id = 91 GROUP BY task_id, content_type limit %s, 500
          """ % start
    big_cur.execute(sql)
    big_recode = big_cur.fetchall()
    task_ids = ','.join(str(i[0]) for i in big_recode)      # 每次100条作业的id
    big_cur.close()
    big_conn.close()

    my_detail = []
    for (id, task_id, catalog_id, text_catalog_id, question_id,
         content_type) in big_recode:
        try:
            cids = catalog_id.split(',')
            tcids = text_catalog_id.split(',')
            qids = question_id.split(',')
            text = []
            for i in range(len(cids)):
                cid = cids[i]
                qid = qids[i]
                tcid = tcids[i]
                text.append({"cid": cid, "tcid": qid, "qid": qid})
            text = json.dumps(text)
            d = dict(
                id=id,
                task_id=task_id,
                text=text,
                content_type=content_type
            )
            my_detail.append(d)
        except:
            logging.info(sql)
            logging.info("id: %s----task_id:%s---content_type:%s" % (id, task_id, content_type))

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

    insert_sql = "insert into yy_task_detail1 (%s) VALUES (%s)" % (fields, tokens)
    args = [o.values() for o in my_detail]
    my_cur.executemany(insert_sql, args)
    my_conn.commit()
    my_cur.close()
    my_conn.close()
