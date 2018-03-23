#__author__ = 'shuai'
# -*- coding: UTF-8 -*-

import cookielib
import urllib2
import urllib
from requests import Session

'''
url = 'http://127.0.0.1:8000/login_validation/ '
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
values = {'username':'12','password':'12'}
data = urllib.urlencode(values)
request = urllib2.Request(url=url,data=data,headers=headers)
responce = urllib2.urlopen(request)
print responce.read()
'''

#
# url = 'http://127.0.0.1:8000/login_validation/ '
# values = {'username':'12','password':'12'}
# data = urllib.urlencode(values)
# req = urllib2.Request(url=url,data=data)
# res = urllib2.urlopen(req)
# a = res.read()
# b = eval(a)
# if b['res'] == 1:
#     print "loginsuccen"
# else:
#     print "loginerror"


def login(url,username,password):
    session=Session()
    res=session.post(url,data={'username':username,'password':password})
    return {'session':session,'res':res.text}



login("http://127.0.0.1:8000/login_validation/","12","12")


def a(*args,**kwargs):
    def b(req):
        def c(*args,**kwargs):
            session = Session()
            res = session.post(args[0], kwargs)
            req(session)
        return c
    return b


