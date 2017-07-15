#coding=utf-8


a = True
print a

#数据结构list(列表[])
temp = "nihao"			#列表下表（索引），列表内的元素可以改变
print temp, temp[2], temp[-1]
print 'nihao'[-1]

a = 'hello world'		#列表切片
print a[:2], a[:-1], a[0:-1:2], 'hehe', a[0:-1:1]

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b			#相同类型的列表才能相加，进行连接
print c

print 'a' * 5


empty = [None] * 10		#有10个元素的空列表
print empty

if 1 in a:
    print True
else:
    print False
	
if 2 in a : print True

print len(a),min(a),max(a)		#求列表长度，最大值。最小值
b = ['nihao','nene','world']
print len(b),min(b),max(b)

print  list('nihao')		#把字符串转换成列表

#改变列表中元素的值
tmp = [1,2,3,4,5,6,7,8,9]
tmp[0] = 10
print tmp,len(tmp)
del tmp[0]					#删除列表中的元素
print tmp,len(tmp)
tmp[0:2] = [32,12]			#分片赋值
print tmp

#列表中的方法		append 追加   count 统计元素出现的次数
					#extend  扩展元素		
					#insert 将对象插入到列表中
					#pop 移出列表中的元素,默认为最后一个元素
					#remove 移出列表中某个值的第一个匹配项
					#reverse  将列表中的元素反向存放
					#sort  对列表进行排序
print a						
a.append(5)
print a,a.count(1)
a.extend([6,7,8])
print a

number = [1,2,3,4,5]
number.insert(3,'insert')
print number
number[3:3] = ['hello']
print number
print len(number),number.pop(1),number,len(number)

number.remove('insert')
print len(number),number

number.reverse()
b = list(reversed(number))
print number,b

a = [1,2,1,5,6,7,1,34,9]
b = sorted(a)
a.sort()
print a,b

c = ['aaa','bb','c']
c.sort()
print c
c.sort(key = len)
print c
c.sort(reverse = True)
print c