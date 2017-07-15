#coding=utf-8

import datetime
import time
# import time_deal
# import MySQLdb
# from urllib import urlopen
#
# now = datetime.datetime.now()
# print now, type(now),
# a = datetime.datetime.strftime(now,'%Y%m%d%H%M%S')
#
# time1 = time_deal.mktime(now.timetuple())
#
# print time_deal.localtime(time1)


# tmp_url = "http://file.tbkt.cn/upload_media/tbkt_cms_batch/2016/09/09/20160909092829250148.txt"
#
# doc = urlopen(tmp_url).readlines()
#
# for obj in doc:
#     print obj.split('\n')[0]

# a = [1, 2]
# b = 1
# if b in a:
#     print 'nihao'
#
# a = lambda x: x
# print a(1)
#
# import datetime
# import time
#
# now = time.time()
# #把当前时间戳转换成时间元组
# now = time.localtime(now)
# #把时间元组转换成时间字符串
# now = time.strftime("%Y-%m-%d %H:%M:%S", now)
# print now, type(now)
# #
#
# year = now.year
# month = now.month
# FORMAT = "%d-%d-%d 0:0:0"
# be_str = FORMAT % (year, month, 1)
# la_str = FORMAT % (year, month, 31)
#
# print be_str
# print la_str
#
# be_str = time.strptime(be_str, "%Y-%m-%d %H:%M:%S")
# la_str = time.strptime(la_str, "%Y-%m-%d %H:%M:%S")
# print be_str, type(be_str)
# print la_str, type(la_str)

PRESS = {51: '人教版一起点', 79: '人教版三起点', 63:'科普版', 75: '外研版'}

# 版本对应的试卷 按照上面的版本顺序，和班级，卷的顺序， 一次向下递加
#press: test_id
PRESS_PAPER = {
    51: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    79: [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    63: [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
    75: [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54],
}

keys = [a for a in PRESS_PAPER.keys()]
result = None
data = None
for key in keys:
    data = PRESS_PAPER[key]
    result = str(data)
    result = result[1:-1]
    result = result.replace(',', '|')
    result = result.replace(' ', '')
    break
print data
print result

a = 'nihjao enen'
b = a.replace('nihjao', 'ene')
print a, b
