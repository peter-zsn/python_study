#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: thread_pool.py
@time: 2017/6/12 18:06
"""

import threading, Queue


POOL_SIZE = 50

q = Queue.Queue()

class Client(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.setDaemon(False)
        self.id = id
    def run(self):
        while 1:
            f, args, kwargs = q.get()
            if f:
                f(*args, **kwargs)

def call(f, *args, **kwargs):
    q.put((f, args, kwargs))

def init():
    Clients = []
    for i in xrange(POOL_SIZE):
        client = Client(i)
        Clients.append(client)

    for client in Clients:
        client.start()
init()
