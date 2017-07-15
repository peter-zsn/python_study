#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: list_json.py
@time: 2017/6/6 9:57
"""
import json

list_t = [
    {'catalog_id': 408, 'text_catalog_id': 408, 'question_id': "21", 'content_type': 9},
    {'catalog_id': 408,'text_catalog_id': 408, 'question_id': "74", 'content_type': 9},
    {'catalog_id': 408,'text_catalog_id': 408, 'question_id': "75", 'content_type': 9},
    {'catalog_id': 408,'text_catalog_id': 408, 'question_id': "58", 'content_type': 9},
    {'catalog_id': 15959, 'text_catalog_id': 15959, 'question_id': 11837, 'content_type': 1},
    {'catalog_id': 15959, 'text_catalog_id': 15959, 'question_id': 11855, 'content_type': 8},
    {'catalog_id': 15959, 'text_catalog_id': 15959, 'question_id': 11839, 'content_type': 2},
    {'catalog_id': 15959, 'text_catalog_id': 15959, 'question_id': 11843, 'content_type': 2},
    {'catalog_id': 15959, 'text_catalog_id': 15959, 'question_id': 11847, 'content_type': 2},
    {'catalog_id': 15959, 'text_catalog_id': 15959, 'question_id': 11847, 'content_type': 8},
    {'catalog_id': 15959, 'text_catalog_id': 15959, 'question_id': 11845, 'content_type': 7},
    {'catalog_id': 15959, 'text_catalog_id': 15959, 'question_id': 11849, 'content_type': 7},
    {'catalog_id': 15959, 'text_catalog_id': 15959, 'question_id': 11851, 'content_type': 8},
    {'catalog_id': 15959, 'text_catalog_id': 15959, 'question_id': 11853, 'content_type': 7},
    {'catalog_id': 15959, 'text_catalog_id': 15959, 'question_id': 11841, 'content_type': 1},
    {'catalog_id': 15959, 'text_catalog_id': 15959, 'question_id': 11845, 'content_type': 1},
    {'catalog_id': 20079, 'text_catalog_id': 20079, 'question_id': 0, 'content_type': 4},
    {'catalog_id': 31134, 'text_catalog_id': 31134, 'question_id': 0, 'content_type': 6},
    {'catalog_id': 31134, 'text_catalog_id': 31134, 'question_id': 0, 'content_type': 3}
]

list_json = json.dumps(list_t)

print list_json