# coding=utf-8
"""
    Time    :   2016/8/22 9:19
    Function:
    Auth    :   Shuainan Zhang
    File    :   nihao.py
"""


import time

# # #得到当前时间的时间戳
# now = time.time()
# print now, type(now)

# now = 1498549129
# #把当前时间戳转换成时间元组
# now = time.localtime(now)
# print now, type(now)
#
# #把时间元组转换成时间字符串
# now = time.strftime("%Y-%m-%d %H:%M:%S", now)
# print now, type(now)
#
now = '2017-07-23 23:59:59'
#把时间字符串转换成时间元组
now = time.strptime(now, "%Y-%m-%d %H:%M:%S")
print now, type(now)

#把时间元组转换成时间戳
now1 = time.mktime(now)
print now1, type(now1)

#
# nowt = time.time()
#
# nowt = int(nowt)
# day = nowt - nowt % (24 * 3600) - 8 * 3600
# print day


import datetime
# """
# •datetime.date：表示日期的类。常用的属性有year, month, day；
# •datetime.time：表示时间的类。常用的属性有hour, minute, second, microsecond；
# •datetime.datetime：表示日期时间。
# •datetime.timedelta：表示时间间隔，即两个时间点之间的长度。
# •datetime.tzinfo：与时区有关的相关信息。（这里不详细充分讨论该类，感兴趣的童鞋可以参考python手册）
# """
# #得到当前时间的时间对象
# now = datetime.datetime.now()
# print now, type(now), 11111111111

#把时间对象转换成字符串
# now = now.strftime("%Y-%m-%d %H:%M:%S"), 333333
# print now, type(now)
#
# #把时间戳转换成事件对象
# date = datetime.datetime.utcfromtimestamp(now1)
# print date, type(date)
#
# today = datetime.datetime.today()
# ling_time = datetime.datetime(today.year, today.month, today.day, 0, 0, 0)
# print ling_time, 222222222
#
# now = datetime.datetime.now()
# now = now.strftime("%Y年%m月%d %H:%M:%S")
# print now
# begin_time = '2017-3-17 00:00:00'
# end_time = '2017-3-19 23:59:59'
#
# now = time.strptime(now, "%Y-%m-%d %H:%M:%S")
# begin_time = time.strptime(begin_time, "%Y-%m-%d %H:%M:%S")
# end_time = time.strptime(end_time, "%Y-%m-%d %H:%M:%S")
#
# if now >= begin_time and now <= end_time:
#     print '你在啊'
# else:
#     print 'haha'
#
