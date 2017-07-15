#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: group.py
@time: 2017/7/6 17:57
"""

a = [
    {"qid": "6109", "tcid": 15902, "cid": 15902},
    {"qid": "6113", "tcid": 15902, "cid": 15902},
    {"qid": "6109", "tcid": 15903, "cid": 15903},
    {"qid": "6113", "tcid": 15903, "cid": 15903}
]

output_dict = {}
for item in a:
    output_dict.setdefault(item['cid'], []).append(item['qid'])

print output_dict