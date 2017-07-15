# coding=utf-8
"""
    Time    :   2016/8/29 18:18
    Function:   测试logging模块
    Auth    :   Shuainan Zhang
    File    :   logging.py
"""

import os
import logging
import datetime
#不能自己创建文件夹

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGDIR = os.path.join(BASE_DIR, "study/log")
LOGFILE = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
LOG_NAN = os.path.join(LOGDIR, LOGFILE)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    pathname=LOGDIR,
                    filename= LOG_NAN,
                    filemode='w',)

logging.info("woqunidaye")