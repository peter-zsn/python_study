#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: urllib.py
@time: 2016/11/14 15:24
"""

import xlrd
import urllib

url = "http://file.tbkt.cn/upload_media/school/2016/11/14/20161114152342199250.xlsx"

fp = urllib.urlopen(url)
file_content = fp.read()
data = xlrd.open_workbook(file_contents=file_content)
table = data.sheets()[0]

for i in range(1, table.nrows):
        for j in range(len(table.row_values(i))):
            if j == 2:
                print table.row_values(i)[j]
            else:
                print table.row_values(i)[j].encode('utf-8')