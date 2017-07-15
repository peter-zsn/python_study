#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: 11.py
@time: 2016/12/9 17:48
"""


def fun(a):
    if a == 5:
        return 1
    else:
        return a + fun(a + 1)


a = fun(3)
print a