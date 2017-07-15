#coding=utf-8

import pypinyin

"""
@varsion: ??
@author: 张帅男
@file: first_word.py
@time: 2016/12/22 19:55
"""


def get_first(unicode1):
    if unicode1 == '':
        return '#'
    str1 = unicode1.encode('gbk')
    try:
        return chr(ord(str1))
    except:
        pass
    asc = ord(str1[0]) * 256 + ord(str1[1]) - 65536
    if asc >= -20319 and asc <= -20284:
        return 'a'
    if asc >= -20283 and asc <= -19776:
        return  'b'
    if asc >= -19775 and asc <= -19219:
        return  'c'
    if asc >= -19218 and asc <= -18711:
        return  'd'
    if asc >= -18710 and asc <= -18527:
        return  'e'
    if asc >= -18526 and asc <= -18240:
        return  'f'
    if asc >= -18239 and asc <= -17923:
        return  'g'
    if asc >= -17922 and asc <= -17418:
        return  'h'
    if asc >= -17417 and asc <= -16475:
        return  'j'
    if asc >= -16474 and asc <= -16213:
        return  'k'
    if asc >= -16212 and asc <= -15641:
        return  'l'
    if asc >= -15640 and asc <= -15166:
        return  'm'
    if asc >= -15165 and asc <= -14923:
        return  'n'
    if asc >= -14922 and asc <= -14915:
        return  'o'
    if asc >= -14914 and asc <= -14631:
        return  'p'
    if asc >= -14630 and asc <= -14150:
        return  'q'
    if asc >= -14149 and asc <= -14091:
        return  'r'
    if asc >= -14090 and asc <= -13119:
        return  's'
    if asc >= -13118 and asc <= -12839:
        return  't'
    if asc >= -12838 and asc <= -12557:
        return  'w'
    if asc >= -12556 and asc <= -11848:
        return  'x'
    if asc >= -11847 and asc <= -11056:
        return  'y'
    if asc >= -11055 and asc <= -10247:
        return  'z'
    else:
        return str1[0]

def get_first_letter(char):
    char = char.encode('GBK')
    if char < b"\xb0\xa1" or char > b"\xd7\xf9":
        return char[0]
    if char < b"\xb0\xc4":
        return "a"
    if char < b"\xb2\xc0":
        return "b"
    if char < b"\xb4\xed":
        return "c"
    if char < b"\xb6\xe9":
        return "d"
    if char < b"\xb7\xa1":
        return "e"
    if char < b"\xb8\xc0":
        return "f"
    if char < b"\xb9\xfd":
        return "g"
    if char < b"\xbb\xf6":
        return "h"
    if char < b"\xbf\xa5":
        return "j"
    if char < b"\xc0\xab":
        return "k"
    if char < b"\xc2\xe7":
        return "l"
    if char < b"\xc4\xc2":
        return "m"
    if char < b"\xc5\xb5":
        return "n"
    if char < b"\xc5\xbd":
        return "o"
    if char < b"\xc6\xd9":
        return "p"
    if char < b"\xc8\xba":
        return "q"
    if char < b"\xc8\xf5":
        return "r"
    if char < b"\xcb\xf9":
        return "s"
    if char < b"\xcd\xd9":
        return "t"
    if char < b"\xce\xf3":
        return "w"
    if char < b"\xd1\x88":
        return "x"
    if char < b"\xd4\xd0":
        return "y"
    if char < b"\xd7\xf9":
        return "z"

name = u'安心'            # 前两种方法ao拼音的汉子不能识别
print get_first(name)
print get_first_letter(name)

rows = pypinyin.pinyin(name, style=pypinyin.NORMAL)
a = ''.join(row[0][0] for row in rows if len(row)>0)
print a[0]


