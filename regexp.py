#coding=utf-8

"""
@事关正则表达式的尊严
@varsion: ??
@author: 张帅男
@file: regexp.py
@time: 2016/11/30 9:58
"""

import re
"""
. :匹配出换行符之外的任意字符 a.b  (a b, avb, a1b)
^ :首部以什么开始。 ^1 以1为开头
$ :匹配字符串末尾 在多行模式下匹配每一行的末尾
[...]: 可以去[]中间的值， 1[abc]2   (可匹配 1a2 1b2 1c2)
\d :数字 [0-9] 必须是数字0-9
{9} : 匹配前一个字符9次
\D :非数字（[^\d]）
\s : 空白字符    a\sc  (a c)
\S :非空白字符[^\s]
\w :单词字符[A-Za-z0-9]
\W :非单词字符[^\w]
* :匹配前一个字符0或无限次
+ :匹配前一个字符1或无限次
? :匹配前一个字符0或1次
{m} :匹配前一个字符m次
{n, m} :匹配前一个字符n-m次， n省略，则从0开始， m省略则无限次
\A :仅匹配字符串开头
\Z :仅匹配字符串末尾
\b :匹配\w和\W之间   （没看懂）“er\b”可以匹配“never”中的“er”，但不能匹配“verb”中的“er”。
\B :[^\b]
| :左右表达式任意匹配一个， 先匹配左边的,再匹配右边的, 仅在()
() : 分组表达式，  作为一个整体。
(?P<name>...) : 分组，另外制定一个额外的别名
(?P=name) :引用别名为name的分组匹配到的字符串
(?=...)    :之后的字符串内容需要匹配到才能匹配成功    a(?=\d) （后面是数字的a）
(?!...)    :之后的字符串内容不需要匹配到才能匹配成功  a(?!\d) （后面不是数字的a）
(?<=...)   :之前的字符串内容需要匹配到才能匹配成功    (?<=\d)a （前面是数字的a）
(?<!...)   :之前的字符串内容不需要匹配到才能匹配成功   (?<!\d)a （前面不是数字的a）
"""

# 手机号码正则匹配
_phone_match = '^1[34578]\d{9}'
phone_number = '18111111111'
if re.match(_phone_match, phone_number):
    m = re.match(_phone_match, phone_number)
    print m.group()
    print '这是手机号'
else:
    print '这不是手机号码'

# 匹配空白字符
_space_match = '\s*英语\s+$'
subjec = ' 英语   '
if re.match(_space_match, subjec):
    m = re.match(_space_match, subjec)
    print m.group()
    print '这是英语'
else:
    print '这不是英语'

# 匹配单词
_word_match = '^\w+'
char = 'a@'
if re.match(_word_match, char):
    print '这不是单词'
else:
    print '这是单词'