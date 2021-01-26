# python_study----主要是16，17年的记录， python版本2.7，python3 会有少许变化
## 涉及python常用的一些语法 如下：

### 1 dict_to_attr
    主要涉及__getattr__, __setattr__, __delattr__
    封装一个类，可以把dict 转换成class， 例如dict_a= {'a': 1}, 为转换之前获取key或者设置value 只能用常规的写法，转换之后，dict_a.a = 2（赋值）， b = dict_a.a （获取value)
### 2:yy_to_sql
    主要是基础的mysqldb 初始化连接，进行基础的查询，插入，更新，删除操作----原生sql
### 3: 11.py
    主要是git提交脚本，输入对应的指令进行git操作， 暂时只是获取和提交，后期可拓展更多
### 4: args.py
    主要是讲解 参数传递的区别， 主要为*args 和 **kwargs 等的用法
### 5：asd.py
    主要是split 和 join的用法
### 6: callback.py
    简单的递归 回调用法
### 7: chuli.py 
    主要是处理excel文件，使用xlrd读取excel文件的内容。 
### 8:decorator.py
    主要涉及装饰器的使用，对多个函数进行统一处理或者限制
### 9:dict.py ----python3 一些迭代就不再区分了， 直接简单的用法返回的就是迭代器
    涉及字典的基础用法：init，clear，copy，deepcopy，fromkeys，get haskey，items，iteritems，keys，iterkeys， pop，setdefault，update， values等
### 10:first_word.py
    获取字符串的首字母
### 11: http_port.py
    request   post的使用
### 12: list.py
    主要是list的用法 index，split，append， +，-， *，len， max， min，del， 切片赋值，count,extend,insert,pop,remove,reverse,sort等
### 13: log.py
    主要是做了一些日志输出
### 14:long_str.py
    对一些注释，换行符，转义符做了一些说明
### 15:map_filter_reduce.py
    主要针对map，filter,reduce函数作了说明
### 16:pinyin.py
    引用第三方pinyin库，对汉字作了一些处理
### 17:propery,py
    对propery的使用，以及源码的分析
### 18:re_test.py
    re模块的简单实用，主要涉及sub,split,findall,compile,search,match
### 19:regexp.py
    正则表达式的尊严。。。。。。各种匹配规则
### 20: str.py
    字符串操作，涉及format,Tamplate,find,join,lower,upper,replace,split,strip,lstrip,rstrip
### 21: structpack.py
    涉及c语言结构的转换
### 22:tbkt_uwsgi_pro.ini
    简单的uwsgi配置，以及注释
### 23:thread_pool.py
    线程池的封装，主要是thread和queue配合使用
### 24:thread_pool2.py
    线程池的封装，主要是thread和queue配合使用
### 25:time_block.py
    计算函数运行时间
### 26:time_detail.py
    涉及time,datetime模块的使用
### 27: tuple.py
    涉及元祖的使用
### 28: xlrd_detail.pu
    对xlsl文件处理，读写操作
### 29:yield.py
    生成器的使用理解
