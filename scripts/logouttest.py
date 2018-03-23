#__author__ = 'shuai'
# -*- coding: UTF-8 -*-
import urllib2
import urllib
from requests import session
from logintest import a
from logintest import login

# session = session()
# url = 'http://127.0.0.1:8000/login_validation/'
# data = {'username':'12','password':'12'}
# req = session.post(url,data)
# print req
#
# url = 'http://127.0.0.1:8000/logout/'
# req = session.get(url)
# print req

ses = login("http://127.0.0.1:8000/login_validation/","12","12")
def logout(ses):
    ses.get("http://127.0.0.1:8000/logout/")



