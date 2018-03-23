#__author__ = 'shuai'
# -*- coding: UTF-8 -*-
import urllib
import urllib2
import time
import requests
from requests import Session
from logintest import login
from  logintest import a

#
# session =Session()
# values = {'username':'12','password':'12'}
# #headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
# url = 'http://127.0.0.1:8000/login_validation/'
# req = session.post(url,values)
# print req
# print(req.content.decode('utf-8'))
#
# url = 'http://127.0.0.1:8000/iface/'
# resp = session.get(url)
# #print(resp.content.decode('utf-8'))

# url = 'http://127.0.0.1:8000/case_add_data/'
# values = {'idesc':'143','iurl':'243','idata':'112','iresult':'112','imethod':1}
# #headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
# reqs = session.post(url,values)
# time.sleep(5)
# print reqs

#ses=login("http://127.0.0.1:8000/login_validation/","12","12")
# def zengjiacase(url,data,ses):
#     res = ses['session'].post(url,data=data)
#     time.sleep(5)
#     return res
#
# values = {'idesc':'14311','iurl':'243','idata':'112','iresult':'112','imethod':1}
# b = zengjiacase('http://127.0.0.1:8000/case_add_data/',values,ses)
# print b

@a(('http://127.0.0.1:8000/login_validation/',),{'username':12,'password':12})

def zengjiacase(url,data,ses):
    res = ses['session'].post(url,data=data)
    time.sleep(5)
    return res

values = {'idesc':'14311','iurl':'243','idata':'112','iresult':'112','imethod':1}
b = zengjiacase('http://127.0.0.1:8000/case_add_data/',values,ses)
print b
