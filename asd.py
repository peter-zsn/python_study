#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: asd.py
@time: 2017/4/27 10:09
"""


a = "15424-0|15425-2|15426-1"
rows = [r.split('-') for r in a.split('|')]
print rows

user_options = {int(r[0] or 0): int(r[1] or -1) for r in rows if len(r) > 1}
print user_options


options = [
    {"id": 1, "link_id": 2},
    {"id": 3, "link_id": 4},
    {"id": 5, "link_id": 6}
]

answer = []
for obj in options:
    a = str(obj['id']) + '-' + str(obj['link_id'])
    answer.append(a)

answer = '|'.join(answer)
print answer