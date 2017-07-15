#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: 11.py.py
@time: 2017/7/13 17:48
"""
import os

def get_operation():
    print u"请选择你要进行的操作:"
    print u"1, 自动上传push:"
    print u"2， 打标签:"

def push_ope():
    print u"请输入分支"
    branch = raw_input()
    add = "git add ."
    commit = "git commit -m -a 'zsn'"
    pull = "git pull origin " + branch
    push = "git push origin " + branch
    os.system(add)
    os.system(commit)
    os.system(pull)
    os.system(push)


if __name__ == "__main__":
    try:
        get_operation()
        first = input()
        if first == 1:
            push_ope()
    except Exception, e:
        print e