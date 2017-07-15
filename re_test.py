#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: re_test.py
@time: 2017/3/22 16:38
"""

import re

text = "JGood is a handsome boy, he is cool, clever, and so on..."
print re.sub(r'\s+', '-', text)
print re.split(r'\s+', text)
print re.findall(r'\w*oo\w*', text)
regex = re.compile(r'\w*oo\w*')
print regex.findall(text)

m = re.search(r'\shan(ds)ome\s', text)      # re.search匹配整个字符串，直到找到一个匹配
if m:
    print m.group(0), m.group(1)
else:
    print 'no serch'

m = re.match(r"(\w+)\s", text)              # re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败
if m:
    print m.group(0), m.group(1)
else:
    print 'no serch'