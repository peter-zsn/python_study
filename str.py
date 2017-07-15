#coding=utf-8

#字符串的介绍
#字符串可以看成特殊的列表，不过字符串是不可改变的

format = "my name is %s"
name = 'peter'
print format %  name
print "my name is {0}".format(name)

from string import Template
s = Template('$s is good $x!')
#b = s.substitute(s = 'peter')
#print b
d = {}
d['s'] = 'peter'
d['x'] = 'man'
c = s.substitute(d)
print c

print "%s is a %s %s" % ('peter','good','man')
print 'one year is %d month' % 12
print 'one year is %.2f month' % 12


#字符串中的方法
#find 在原字符串中发现字串，并返回index,未找到则返回-1
a = 'it is a good apple'
b = 'is'
print a.find(b)

#join 可以在字符串中添加字符串,列表中没有join
a = '+'
b = ['1','2','3','4','5']
print a.join(b)

#lower 返回字符串的小写字母版 对应的是upper

#replace 替换	a.replace(sub,tar)
print 'it is a woman'.replace('woman','man')

#split 将字符串分割成序列,可以说是join的逆方法
print '1+2+3+4+5'.split('+')
tm = ['1','2','3','4','5']
b = '+'
print b.join(tm)

#strip 删除开头结尾要删除的字符,lstrip(开头),rstrip(结尾)
a = ' ihao woqu enn '
print a.strip()



