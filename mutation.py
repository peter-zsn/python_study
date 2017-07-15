#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: mutation.py
@time: 2017/3/13 16:17
"""

a = [1]

def add(num, target=[]):
    target.append(num)
    return target

add(1)
add(2)
add(3)
print add(4)

from pprint import pprint

a = {'1': 1, '2': 2, '3': 3}
pprint(a)
print a