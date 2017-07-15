#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: yy_sql.py
@time: 2017/6/28 10:18
"""
from log import logging
import sql
import json

def to_task():
    logging.info("to_task----start----")
    count_sql = """SELECT count(id) FROM u_task WHERE subject_id = 91;"""
    task_nums = sql.big_sql_count(count_sql)
    if not task_nums:
        return

    # 每次执行500条
    page = task_nums / 500 + 2
    task_count = 0
    for i in range(page):
        start = i * 500
        task_sql = "SELECT id, type, object_id, add_user, title, sms_content, status, UNIX_TIMESTAMP(add_time)," \
              " UNIX_TIMESTAMP(begin_time), UNIX_TIMESTAMP(end_time), is_sendpwd" \
              " FROM u_task WHERE subject_id = 91 ORDER BY id LIMIT %s, 500;" % start
        recode = sql.big_fetchall(task_sql)
        if not recode:
            continue
        details = []
        for (id, type_id, object_id, add_user, title, sms_content,
             status, add_time, begin_time, end_time, is_sendpwd) in recode:
            try:
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
                details.append(d)
            except Exception, e:
                logging.info('id:%s--------limit %s: 500-----%s' % (id, i, e))
        sql.local_insert('yy_task1', details)
        task_count += len(details)
    task_count_sql = """SELECT count(id) FROM yy_task1"""
    task_count_now = sql.local_sql_count(task_count_sql)
    logging.info("procedure-count:%s,  query-count:%s" % (task_count, task_count_now))

def to_task_class():
    logging.info("to_task_class----start----")
    count_sql = """
              SELECT count(tc.id) FROM u_task t INNER JOIN u_task_class tc ON tc.task_id = t.id WHERE t.subject_id = 91;
            """
    nums = sql.big_sql_count(count_sql)
    if not nums:
        return
    # 每次执行500条
    page = nums / 500 + 2
    count = 0
    for i in range(page):
        start = i * 500
        task_class_sql = """
                  SELECT tc.id, tc.task_id, tc.unit_class_id, tc.type, tc.student_id, UNIX_TIMESTAMP(tc.add_time)
                  FROM u_task_class tc INNER JOIN u_task t ON t.id = tc.task_id AND t.subject_id = 91 LIMIT %s, 500;
                  """ % start
        recode = sql.big_fetchall(task_class_sql)
        if not recode:
            continue
        details = []
        for (id, task_id, unit_class_id, type, student_id, add_time) in recode:
            try:
                d = dict(
                    id=id,
                    task_id=task_id,
                    unit_class_id=unit_class_id,
                    type=type,
                    student_id=student_id,
                    add_time=add_time,
                )
                details.append(d)
            except Exception, e:
                logging.info('id:%s---task_id:%s----limit %s: 500-----%s' % (id, task_id, i, e))
        sql.local_insert('yy_task_class1', details)
        count += len(details)
    task_count_sql = """SELECT count(id) FROM yy_task_class1"""
    count_now = sql.local_sql_count(task_count_sql)
    logging.info("procedure-count:%s,  query-count:%s" % (count, count_now))

def to_task_detail():
    logging.info("to_task_detail----start----")
    count_sql ="""
        SELECT COUNT(c.id) FROM (
        SELECT td.id, td.task_id, GROUP_CONCAT(td.catalog_id), GROUP_CONCAT(td.text_catalog_id), GROUP_CONCAT(td.question_id),
        content_type FROM u_task_detail td
        INNER JOIN u_task t ON t.id= td.task_id and t.subject_id = 91 GROUP BY task_id, content_type) c;
                """
    nums = sql.big_sql_count(count_sql)
    if not nums:
        return
    # 每次执行500条
    page = nums / 500 + 2
    count = 0
    for i in range(page):
        start = i * 500
        task_detail_sql = """SELECT td.id, td.task_id, GROUP_CONCAT(td.catalog_id), GROUP_CONCAT(td.text_catalog_id),
        GROUP_CONCAT(td.question_id), content_type FROM u_task_detail td
        INNER JOIN u_task t ON t.id= td.task_id WHERE t.subject_id = 91 GROUP BY task_id, content_type limit %s, 500
                 """ % start
        recode = sql.big_fetchall(task_detail_sql)
        if not recode:
            continue
        details = []
        for (id, task_id, catalog_id, text_catalog_id, question_id,
             content_type) in recode:
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
                details.append(d)
            except Exception, e:
                logging.info('id:%s---task_id:%s--content_type:%s--limit %s: 500-----%s' % (id, task_id, content_type, i, e))
        sql.local_insert('yy_task_detail1', details)
        count += len(details)
    task_count_sql = """SELECT count(id) FROM yy_task_detail1"""
    count_now = sql.local_sql_count(task_count_sql)
    logging.info("procedure-count:%s,  query-count:%s" % (count, count_now))

def to_task_progress():
    logging.info("to_task_progress----start----")
    count_sql = """
                      SELECT count(ytp.id) FROM tbkt_web.u_yy_task_progress ytp
                      INNER JOIN tbkt.u_task t ON t.id = ytp.task_id WHERE t.subject_id = 91;
                """
    nums = sql.big_sql_count(count_sql)
    if not nums:
        return
    # 每次执行500条
    page = nums / 500 + 2
    count = 0
    for i in range(page):
        start = i * 500
        task_pro_sql ="""
                    SELECT ytp.id, ytp.user_id, ytp.task_id, ytp.`status`, ytp.update_time
                    FROM tbkt_web.u_yy_task_progress ytp
                    INNER JOIN tbkt.u_task t ON t.id = ytp.task_id WHERE t.subject_id = 91 limit %s, 500;
                    """ % start
        recode = sql.big_fetchall(task_pro_sql)
        if not recode:
            continue
        details = []
        for (id, user_id, task_id, status, update_time) in recode:
            try:
                d = dict(
                    id=id,
                    user_id=user_id,
                    task_id=task_id,
                    status=status,
                    update_time=update_time,
                )
                details.append(d)
            except Exception, e:
                logging.info('id:%s---task_id:%s---user_id:%s-limit %s: 500-----%s' % (id, task_id, user_id, i, e))
        sql.local_insert('yy_task_progress1', details)
        count += len(details)
    task_count_sql = """SELECT count(id) FROM yy_task_progress1"""
    count_now = sql.local_sql_count(task_count_sql)
    logging.info("procedure-count:%s,  query-count:%s" % (count, count_now))

def to_test():
    logging.info("to_test----start----")
    count_sql = """
              SELECT count(id) FROM tbkt_web.u_yy_test;
            """
    nums = sql.big_sql_count(count_sql)
    if not nums:
        return
    # 每次执行500条
    page = nums / 500 + 2
    count = 0
    for i in range(page):
        start = i * 500
        test_sql ="""
                SELECT id, user_id, catalog_id, nquestion, score, `status`, add_time, test_time, object_id
                 FROM tbkt_web.u_yy_test limit %s, 500;
            """ % start
        recode = sql.big_fetchall(test_sql)
        if not recode:
            continue
        details = []
        for (id, user_id, catalog_id, nquestion, score, status, add_time, test_time, object_id) in recode:
            try:
                d = dict(
                    id=id,
                    user_id=user_id,
                    catalog_id=catalog_id,
                    nquestion=nquestion,
                    score=score,
                    status=status,
                    add_time=add_time,
                    test_time=test_time,
                    object_id=object_id,
                )
                details.append(d)
            except Exception, e:
                logging.info('id:%s---user_id:%s----limit %s: 500-----%s' % (id, user_id, i, e))
        sql.local_insert('yy_test1', details)
        count += len(details)
    task_count_sql = """SELECT count(id) FROM yy_test1"""
    count_now = sql.local_sql_count(task_count_sql)
    logging.info("procedure-count:%s,  query-count:%s" % (count, count_now))

def to_test_detail():
    logging.info("to_test_detail----start----")
    count_sql = """
                 SELECT count(t.id) FROM (SELECT id, GROUP_CONCAT(question_id) FROM tbkt_web.u_yy_test_detail GROUP BY test_id) t;
               """
    nums = sql.big_sql_count(count_sql)
    if not nums:
        return
    # 每次执行500条
    page = nums / 500 + 2
    count = 0
    for i in range(page):
        start = i * 500
        test_detail_sql ="""
            SELECT id, test_id, GROUP_CONCAT(question_id), GROUP_CONCAT(ask_id),
             GROUP_CONCAT(result), GROUP_CONCAT(answer), GROUP_CONCAT(option_id)
             FROM tbkt_web.u_yy_test_detail GROUP BY test_id limit %s, 500;
        """ % start
        recode = sql.big_fetchall(test_detail_sql)
        if not recode:
            continue
        details = []
        for (id, test_id, question_id, ask_id, result, answer, option_id) in recode:
            try:
                qids = question_id.split(',')
                ask_ids = ask_id.split(',')
                answers = answer.split(',')
                results = result.split(',')
                option_ids = option_id.split(',')
                text = []
                for i in range(len(qids)):
                    text.append({"qid": qids[i], "aid": ask_ids[i], "result": results[i], "answer": answers[i],
                                 "oid": option_ids[i]})
                text = json.dumps(text)
                d = dict(
                    id=id,
                    test_id=test_id,
                    text=text
                )
                details.append(d)
            except Exception, e:
                logging.info('id:%s---test_id:%s----limit %s: 500-----%s' % (id, test_id, i, e))
        sql.local_insert('yy_test_detail1', details)
        count += len(details)
    task_count_sql = """SELECT count(id) FROM yy_test_detail1"""
    count_now = sql.local_sql_count(task_count_sql)
    logging.info("procedure-count:%s,  query-count:%s" % (count, count_now))


if __name__ == '__main__':
    # to_task()           # 转换task数据
    # to_task_class()     # 转换task_class数据
    # to_task_detail()    # 转换task_detail数据
    # to_task_progress()  # 转换task_progress数据
    # to_test()           # 转换yy_test数据
    to_test_detail()    # 转换yy_test_detail数据
