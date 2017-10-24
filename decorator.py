#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: decorator.py         # 装饰器
@time: 2017/3/13 15:44
"""
from functools import wraps

can_fun = False

def need_fun(f):
    @wraps(f)
    def limitb():
        if not can_fun:
            return u'登陆失败'
        return f()
    return limitb

@need_fun
def index():
    return u'登陆成功'

print index()
can_fun = True
print index()

print index.__name__        # 引入wraps， 才能打印函数名
