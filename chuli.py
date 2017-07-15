#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: chuli.py
@time: 2016/10/19 16:46
"""




import xlrd
import sys
import string
from functools import wraps

fp = xlrd.open_workbook(r'1.1.xlsx')
table = fp.sheets()[3]

print table.ncols
for i in range(0, table.ncols):
    row = []
    for j in range(len(table.col_values(i))):
        if j < 2:
            continue
        else:
            data = table.col_values(i)[j].encode('utf-8')
            data = data[3:]
            if data == '' or data == '试':
                continue
            row.append(int(data))
    print row