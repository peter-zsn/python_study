#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: args.py
@time: 2017/3/13 14:31
"""

"""
*args 和 **kargs 用于函数定于， 传递不定数量的参数到一个函数
args 和 kargs 不是固定这样写的， 只是约定是俗称， 重点是* 和 **
*args 是用来发送一个非键值对的可变数量的参数列表给一个函数.
**kwargs 允许你将不定长度的键值对, 作为参数传递给一个函数
"""

def test_arg(a, *args):
    print 'first arg', a
    for b in args:
        print b
test_arg(1, 2, '3', 4, '5')

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print key, value

greet_me(name=u'传等式这样的')

def test(a1, a2, a3):
    print 'a1', a1
    print 'a2', a2
    print 'a3', a3

tmp_dict = {'a1': 1, 'a2': 2, 'a3': 3}
tmp_list = [1, 2, 3]
test(*tmp_list)
test(**tmp_dict)