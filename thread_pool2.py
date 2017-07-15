#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: thread_pool2.py
@time: 2017/6/12 18:47
"""
#coding: utf-8
import time
import threading
import Queue
import traceback
import logging

POOL_SIZE = 50

q = Queue.Queue()

def loop(id):
    while 1:
        f, args, kwargs = q.get()
        try:
            f(*args, **kwargs)
        except:
            logging.error(traceback.format_exc())


def call(f, *args, **kwargs):
    q.put((f, args, kwargs))


def init():
    print 'thread_pool init.'
    for i in xrange(POOL_SIZE):
        t = threading.Thread(target=loop, args=(i, ))
        t.start()

init()

if __name__ == '__main__':
    def foo(x):
        for i in range(10):
            print 3
    def too(x):
        for i in range(5):
            print 4

    call(foo, 1)
    call(too, 2)

    time.sleep(1)