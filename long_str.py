#coding=utf-8


#长字符串  5-16
#三引号里面可以使用双引号和单引号，依次递推，
print '''this is a very long string. It continues here. And it's not over yet "hello world!" still here. '''
print "it's a string"		

#单引号里面使用单引号需要使用转义
print 'it\'s a hard string'			

#如果一行中最后的是\   则为换行连接符
print "hello \
world"


#原始字符串  17-28
#\n 换行
print "nihao \nworld"

path = "c:\nowhere"
print path				#会发现打印的是两行，于是需要转义
path = "C:\\nowhere"
print path

#如果有很多的路径，会很麻烦，这是可以使用原始字符串，字符串前面加r,原始字符串使用转义符，转义符会被打印出来（解决办法使用三引号）
print r'C:\nowhere'
print r"C:\nowhere"

#Unicode 字符串 使用前缀u
print u'hello world'