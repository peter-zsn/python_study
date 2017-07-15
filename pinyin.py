#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: pinyin.py
@time: 2016/12/9 16:41
"""

import pypinyin

# a = ['赵日天', '叶良辰', '叶九州', '轩辕败天', '帝释天']
#
# for name in a:
#     print name
#
# print 'sort--nochange'
# a.sort()
# for name in a:
#     print name
#
# print '按中文排序'
#
# pinyin_list = []
# for name in a:
#     s = {}
#     name = name.decode('utf-8')
#     name_pinyin = pypinyin.pinyin(name, style=pypinyin.NORMAL)
#     name_pinyin = ''.join(row[0][0] for row in name_pinyin if len(row) > 0) # 'yjz'
#     s['name'] = name
#     s['pinyin'] = name_pinyin
#     pinyin_list.append(s)
#
# pinyin_list.sort(key=lambda x: x['pinyin'])
#
# for name in pinyin_list:
#     print name['name']



name = u''
rows = pypinyin.pinyin(name, style=pypinyin.NORMAL)
a = ''.join(row[0][0] for row in rows if len(row)>0)
print a[0]