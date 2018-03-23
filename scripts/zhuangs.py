#__author__ = 'shuai'
# -*- coding: UTF-8 -*-
# def myfunc():
#     print("myfunc() called.")
#
# def deco(func):
#     print("before myfunc() called.")
#     func()
#     print("  after myfunc() called.")
#     return func
# @deco
# def myfunc():
#     print(" myfunc() called.")
#
# myfunc = deco(myfunc)
# myfunc()
# myfunc()


# def deco(func):
#     def _deco():
#         print("before myfunc() called.")
#         func()
#         print("  after myfunc() called.")
#         # 不需要返回func，实际上应返回原函数的返回值
#     return _deco
# @deco
# def myfunc():
#     print(" myfunc() called.")
#     return 'ok'
#
#
# myfunc()
# myfunc()


# def a():
#     print "111"
# a()

# def b(c):
#     def d (*args,**kwargs):
#         print "222"
#         g = c(*args,**kwargs)
#         print "2221"
#         return g
#     return d
# @b
# def a(e,f):
#     print e + f
#
# @b
# def a1(e,f,h):
#     print e + f +h
#
# a(1,2)
# a(2,6)
# a1(1,2,4)
# a1(2,4,3)

#

# class a:
#     def __int__(self):
#         print "111"
#     @staticmethod
#     def b():
#         print "bbb"
#     @staticmethod
#     def c():
#         print "ccc"
#
# def d(cls):
#     def g(i):
#         def k():
#             print "kkk"
#             cls.b()
#             try:
#                 return i()
#             finally:
#                 cls.c()
#         return k
#     return g
# @d(a)
# def m():
#     print "mmm"
#
# m()
# m()

class a:
    def __int__(self):
        print "111"
    @staticmethod
    def b():
        print "222"
    @staticmethod
    def c():
        print "333"

class d(a):
    @staticmethod
    def b():
        print "333"
    @staticmethod
    def c():
        print "444"

def k(l):
    def h(p):
        def j(*args,**kwargs):
            print "jjj"
            l.b()
            try:
                return p(*args,**kwargs)
            finally:
                l.c()
        return j
    return h



