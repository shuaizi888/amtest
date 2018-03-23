#__author__ = 'shuai'
# -*- coding: UTF-8 -*-
import urllib
import urllib2
from requests import session


session=session()
url = 'http://127.0.0.1:8000/login_validation/'
data = {'username':'12','password':'12'}
req = session.post(url,data)
print req

url = 'http://127.0.0.1:8000/case_delete_data/'
data = {'caseid':20}
req = session.post(url,data)
print req
