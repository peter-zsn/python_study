#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: urlport.py
@time: 2017/1/5 17:30
"""

import urllib
import urllib2
import json
import requests

def http_post_port(url, data):
    jdata = json.dumps(data)
    req = urllib2.Request(url, jdata)
    response = urllib2.urlopen(req)
    return eval(response.read())

def http_get_port(url):
    response = urllib2.urlopen(url)
    return eval(response.read())


if __name__ == '__main__':
    url = 'http://mapi.beta.tbkt.cn/account/login/t'
    data = {'username': '13592183552', 'password': '111111', 'login_type': '91'}
    result = http_post_port(url, data)
    # print result['data']['user_id']

    r = requests.post(url, params=data)
    cookies = r.cookies
    print cookies, '1111'
    print cookies['tbkt_token']
    print cookies.keys()
    # print r.headers['content-type']
    tmp = {}
    tmp['tbkt_token'] = 'cnF4cHV2dzxxdHh1dHJyeXJ5PHF0eHd0eXZ5cHI'
    url = 'http://mapi.beta.tbkt.cn/account/profile'
    r = requests.post(url, cookies=tmp)
    result = r.json()
    print result, type(result)
    print result['data']

