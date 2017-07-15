#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: http_port.py
@time: 2017/1/6 8:51
"""

import requests
import datetime

from libs.utils import com_db


URL = 'http://mapi.beta.tbkt.cn'

def get_cookies():
    """
    功能说明：                http手动获取cookies
    -----------------------------------------------
    修改人                    修改时间
    -----------------------------------------------
    张帅男                    2017-1-6
    """
    login_url = URL + '/account/login/t'
    data = {"username": "13592183552", "password": "111111", "login_type": "91"}
    r = requests.post(login_url, params=data)
    cookies = r.cookies
    return cookies

def get_user_info(cookies):
    """
    功能说明：                http获取用户信息
    -----------------------------------------------
    修改人                    修改时间
    -----------------------------------------------
    张帅男                    2017-1-6
    """
    url = URL + '/account/profile'
    r = requests.post(url, cookies=cookies)
    result = r.json()
    data = result['data']
    return data

def get_user_book(cookies):
    """
    功能说明：                http获取用户教材
    -----------------------------------------------
    修改人                    修改时间
    -----------------------------------------------
    张帅男                    2017-1-6
    """
    url = URL + '/account/book'
    data = {"subject_id": 91, "type": 1}
    r = requests.post(url, params=data, cookies=cookies)
    result = r.json()
    data = result['data']
    # return data

def get_addtask_count(cookies):
    """
    功能说明：                http获取本月发作业数
    -----------------------------------------------
    修改人                    修改时间
    -----------------------------------------------
    张帅男                    2017-1-7
    """
    url = URL + '/account/addtask_count'
    r = requests.post(url, cookies=cookies)
    result = r.json()
    data = result['data']
    return data

def get_unopen_count(cookies):
    """
    功能说明：                http获取班级下未开通人数
    -----------------------------------------------
    修改人                    修改时间
    -----------------------------------------------
    张帅男                    2017-1-7
    """
    url = URL + '/account/unopen_count'
    r = requests.post(url, cookies=cookies)
    result = r.json()
    data = result['data']
    return data

def send_one_phone(cookies, data):
    """
    功能说明：                http发送单条短信
    -----------------------------------------------
    修改人                    修改时间
    -----------------------------------------------
    张帅男                    2017-1-7
    """
    url = URL + '/account/sendone'
    r = requests.post(url, params=data, cookies=cookies)
    result = r.json()
    data = result['response']
    return data

def send_many_phone(cookies, data):
    """
    功能说明：                http发送多条短信
    -----------------------------------------------
    修改人                    修改时间
    -----------------------------------------------
    张帅男                    2017-1-7
    """
    url = URL + '/account/sendmany'
    r = requests.post(url, params=data, cookies=cookies)
    result = r.json()
    data = result['response']
    return data


