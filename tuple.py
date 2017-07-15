#coding=utf-8

#数据结构，元组是不可变的数据结构(tuple())
#元组可以作为字典的key值，而列表不可以

a = (1,2,3)
print a
b = ()						#空元组
print b

c = (1,)					#一个元素的元组, 必须加逗号
print c
print 3 * (42), 3 * c

#元组函数	
a = [1,2,3]
print a,tuple(a)			#强转

							#元组的分片和列表一样
