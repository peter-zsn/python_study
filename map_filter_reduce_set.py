#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: map_filter_reduce_set.py
@time: 2017/3/13 15:27
"""

a = [1, 2, 3, 4]
b = map(lambda x: x + 1, a)
c = filter(lambda x: x > 2, a)
d = reduce(lambda x, y: x * y, a)

print b
print c
print d
