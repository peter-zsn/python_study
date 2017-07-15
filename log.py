#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: log.py
@time: 2017/6/28 10:13
"""

import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(funcName)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='yy_sql.log',
                filemode='w')

logging.info('This is info message')