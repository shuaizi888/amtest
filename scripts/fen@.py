#__author__ = 'shuai'
# -*- coding: UTF-8 -*-
from zhuangs import *

class t:
    @k(a)
    def y(self):
        print "123"
    @k(a)
    @k(d)
    def y1(self,i,o):
        print "456"
        return i+o
if __name__=='__main__':
    i = t()
    i.y()
    print (i.y())
    print (i.y1(1,2))
    print (i.y1(3,4))
