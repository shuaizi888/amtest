#__author__ = 'shuai'
# -*- coding: UTF-8 -*-

import urllib
import urllib2
import time

username = "45678912"
password = "45678912"
email = "45612@163.com"
url = "http://127.0.0.1:8000/user_register/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
values = {'username':username,'password':password,'email':email}
data = urllib.urlencode(values)
req = urllib2.Request(url=url,headers=headers,data=data)
print req
time.sleep(4)
res = urllib2.urlopen(req)
print res