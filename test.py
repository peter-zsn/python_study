#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: test.py
@time: 2016/10/27 13:45
"""
# a = '390864|390865|390866|390867|390868|390869|390870|390871|390872|'
# a = a.split('|')
# print a
#
# a = [2,1,3,76,2,3,4]
# a.sort()
# print a
#
# a = [1,2,3,4,5,6,7,8]
# b = [1,2,3]
#
# for c in b:
#     a.remove(c)
#
# print a

# a = "10333986", "10333967"
# a = str(a)
# a = a.split(",")
# print a

# mark = "|312160|312162|312166|312168|312172|"
# qids = [int(q) for q in mark.split('|') if q]
# print qids


# import re
# a = '     化学@  '
#
# class_pattern = re.compile(r'\s*化学\s*')
# a = class_pattern.match(a)
#
# print a.group(), '111'

# s = '  数学   '
# s = s.replace(' ', '')
#
# print s
# subject_list = ['英语', '数学', '化学', '物理']
# if s not in subject_list:
# #     print 'nihao'
# phone_list=[[u'13569465550', '10657050500001'], [u'13569737391', '10657050500001'], [u'13569980221', '10657050500001'], [u'13639666844', u'10657050500888'], [u'13673811772', '10657050500001'], [u'13733641938', '10657050500001'], [u'13837481818', '10657050500001'], [u'13937449297', '10657050500001'], [u'13938795276', '10657050500001'], [u'15290958423', u'10657050521802'], [u'15290962425', u'10657050500888'], [u'15290967647', u'10657050521802'], [u'15290987485', u'10657050500888'], [u'15837400547', u'10657050500888'], [u'18224510027', '10657050500001'], [u'18768816852', u'10657050511442']]
# print len(phone_list)

# print ord('w')
# print chr(8), '111'
#
# def fibon(n):
#     a = b = 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
# fibon(10)
# for x in fibon(10):
#     print x

# import datetime
#
# today = datetime.datetime.today()
# ling_time = datetime.datetime(today.year, today.month, today.day, 0, 0, 0)  # 得到现在时间的零点
# ling_time = ling_time.strftime("%Y-%m-%d %H:%M:%S")
#
# sql = "SELECT count(score) FROM score_user_detail WHERE user_id = %s AND item_no = %s AND app_id=24 AND add_date >= '%s';" % (1, 5, ling_time)
# print sql
#
# import time, datetime
# now = datetime.datetime.now()
# now = now.strftime("%Y-%m-%d %H:%M:%S")
# begin_time = '2017-3-31 00:00:00'
# end_time = '2017-4-15 23:59:59'
#
# now = time.strptime(now, "%Y-%m-%d %H:%M:%S")
# begin_time = time.strptime(begin_time, "%Y-%m-%d %H:%M:%S")
# end_time = time.strptime(end_time, "%Y-%m-%d %H:%M:%S")
# if now >= begin_time and now <= end_time:
#     print 'in time'
# else:
#     print 'no time'


# a = {1: 4, 6: 5}
# for i in range(3):
#     status = 0
#     status += a.get(i, 0)
#     print  status


url = 'http://127.0.0.1:8090/account/login/s'
data = {
    "username": 13600000000,
    "password": 11111
}
import requests
r = requests.post(url, params=data)
text_json = r.json()
response = text_json['response']
print text_json, 11111111111