# coding=utf-8
"""
    Time    :   2016/8/19 9:44
    Function:   Introduce the method of a dictionary
    Auth    :   Shuainan Zhang
    File    :   dict.py
"""
#字典是python中的唯一映射方法

#创建字典, 字典中的key值必须是不可变的，因此不能用列表
count = {'kuer': '123', 'bige': '456', 'afa': '789'}
print count

#字典方法
#clear()  清除字典中的所有项,返回一个None
d = {}
d['name'] = "jeck"
d['age'] = 21
c = d.clear()
print d, c

#copy 返回具有相同键值对的新字典，是浅拷贝，值的本身相同, 当在副本中替换值时，原字典不受影响， 但是若是修改了（删除等）某值，则原子典也会改变
x = {'name': 'dock', 'age': 22, 'text': ['aaa','bbb','ccc']}
y = x.copy()
print 'x-->', x
print 'y-->', y
y['text'].remove('ccc')     #修改，原字典会跟着改变
print 'x-->', x
print 'y-->', y
y['age'] = 26               #替换 原字典的值不会改变
print 'x-->', x
print 'y-->', y

#deepcopy 深复制, 复制其包含所有的值,深拷贝后得到的值，与原字典没有关联了

from copy import deepcopy
d = {'name': 'rose', 'age': 25, 'text': ['aaa', 'bbb', 'ccc']}
e = d.copy()
dc = deepcopy(d)
d['text'].append('ggg')
d['age'] = 66
dc['text'].append('vvv')
print d
print e
print dc

#fromkeys 使用给定的键，建立新字典, 第一个参数是key值，第二个参数对应键值，无则默认为None
a = {}.fromkeys('woq', 'haha')
print a
tmp = {}.fromkeys(['name', 'sex'])
print tmp

#get 访问字典项的方法
a = {}
#print a['nihap']        #会出现error
print a.get('nihao')     #得到None

#has_key 判断字典中是否有给出的键
if a.has_key('nihao'):
    print True
else:
    print False

#items 和iteritems
#item 将所有的字典以列表的方式返回，列表中的每一项是（key, values）, 无序
print d
print d.items()

#iteritems 和 item的作用相似，但是返回的是一个迭代器对象而不是列表
for i in d.iteritems():
    print i

#keys 和 iterkeys
#keys 字典中的键以列表的形式返回， 而iterkeys 则是以针对键的迭代器返回的
print d.keys()
for i in d.iterkeys():
    print i

#pop 将对应的键值从字典中删除, 并返回对应键的值
#popitem 返回一个键值对
a = {'name': 'jeck', 'age': 22, 'sex': 'man'}
print a, '   ', a.pop('age'), a
print a.popitem()

#setdefault 可以在字典不含有给定键的情况下，设定相应的键值
a = {}
a.setdefault('name', 'None')
print a
a['name'] = 'peter'
a.setdefault('name', 'None')
print a

#update 利用一个字典更新另一个字典(有相同的键则更改，没有则添加)
a = {'name': 'peter', 'age': 22, 'sex': 'man'}
b = {'dock': 'toal'}
a.update(b)
print a

#values 和itervalues
#values 把字典中的值以字典的形式返回
#itervalues 返回值的迭代器
d = {1: 1, 2: 2, 3: 3, 4: 1}
print d.values()
for i in d.itervalues():
    print i