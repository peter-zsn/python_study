#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: structpack.py
@time: 2017/3/13 14:23
"""
import struct

def add(x):
    return x + 1

a = struct.pack('ihb', 1,2,3)
print repr(a)