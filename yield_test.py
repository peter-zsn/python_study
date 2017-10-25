#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: yield_test.py
@time: 2017/10/25 16:23
"""

def simple_generator_func():
    yield 1
    yield 2
    yield 3

for i in simple_generator_func():
    print i

out = simple_generator_func()
a = next(out)
print a
b = next(out)
print b
c = next(out)
print c