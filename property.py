#coding=utf-8

import time
"""
@varsion: ??
@author: 张帅男
@file: property.py
@time: 2017/1/10 16:43
"""


class Test(object):
    def __init__(self, r):
        self.r = r

    @property
    def get_tmp(self):
        print 'evalute1111111'
        return 3.14 * self.r ** 2

c = Test(2)
print c.r
print c.get_tmp
print c.get_tmp
print c.get_tmp


class lazy(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        val = self.func(instance)
        setattr(instance, self.func.__name__, val)
        return val

class Circle(object):
    def __init__(self, r):
        self.r = r

    @lazy
    def get_tmp(self):
        print 'evalute222222'
        return 3.14 * self.r ** 2

c = Circle(2)
print c.r
print c.get_tmp
print c.get_tmp
print c.get_tmp


class LazyProperty(object):
  def __init__(self, func):
    self.func = func
  def __get__(self, instance, owner):
    if instance is None:
      return self
    else:
      value = self.func(instance)
      setattr(instance, self.func.__name__, value)
      return value
import math
class Circle(object):
  def __init__(self, r):
    self.r = r
  @LazyProperty
  def get_tmp(self):
    print 'Computing area'
    return 3.14 * self.r ** 2

c = Circle(2)
print c.r
print c.get_tmp
c.r = 5
print c.r
print c.get_tmp
print c.get_tmp
