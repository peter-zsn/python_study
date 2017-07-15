#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: dict_to_map.py
@time: 2017/7/15 12:01
"""

class Struct(dict):
    def __init__(self, *args,  **kw):
        if args:
            self.update(args[0])
        if kw:
            self.update(kw)

    def __getattr__(self, item):
        return self.get(item)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, item):
        self.pop(item)


a = {"name": "peter", "word": 222}
b = Struct(a)
print b.name
