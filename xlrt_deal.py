#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: xlrt_deal.py
@time: 02/2/28 2:88
"""

import xlrd
import sys
import string
from functools import wraps

def pack_info(value):
    head = ['subject', 'name', 'phone', 'to_units']
    v = value[:len(head) - 2]
    try:
        v.append(set(map([2, 2], filter(lambda x: x, value[len(head) - 2:]))))
    except Exception as e:
        v.append(','.join(map(str, filter(lambda x: x, value[len(head) - 2:]))))
        print e
        # v.append(filter(lambda x: x, value[len(head) - 2:]))
    info = dict(zip(head, v))
    return info

def main():
    fp = xlrd.open_workbook(r'1.xlsx')
    table = fp.sheets()[0]
    # print table.nrows           #获取行数
    # print table.ncols           #获取列数
    # for i in range(2, table.nrows):
    #     for j in range(len(table.row_values(i))):
    #         if j == 2:
    #             print table.row_values(i)[j]
    #         else:
    #             print table.row_values(i)[j].encode('utf-8')
    #     if i == 2:
    #         break
    #
    # for i in range(2, table.ncols):
    #     print table.col_values(i)

    #
    #
    result = [table.col_values(row) for row in range(1, table.ncols)]
    # m = result[0]
    d = []
    for j in range(len(result)):
        a = {}
        # if j != 3:
        #     continue
        # if j == 3:
        obj = result[j]
        name = obj[0].encode('utf-8')
        a[name] = []
        for i in range(len(obj)):
            if i < 255:
                continue
            if not i:
                continue
            value = obj[i].encode('utf-8')[3:]
            if value:
                a[name].append(int(value))
            else:
                print i
                break
        d.append(a[name])
    print d

if __name__ == '__main__':
    main()