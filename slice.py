#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: slice.py
@time: 2017/7/13 16:25
"""

import copy

class Fib(object):
    def __init__(self, *item):
        self.item = []
        self._result = None
        for i in item:
            self.item.append(i)

    def fush(self):
        if self._result:
            return 2
        else:
            return 3

    def show(self, args):
        self._result = args
        return self

    def __iter__(self):
        tmp = self.fush()
        return tmp

    def __getitem__(self, n):
        if isinstance(n, int):
            if self._result:
                return self.fush()
        if isinstance(n, slice):
            if self._result:
                return self.fush()
            start = n.start if n.start else 0
            stop = n.stop if n.stop else len(self.item)
            list_tmp = []
            for x in range(start, stop):
                list_tmp.append(self.item[x])
            return list_tmp

a = Fib()
b = a.show(2)[0]
print b
