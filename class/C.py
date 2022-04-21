# -*- coding: utf-8 -*-
# Author : zwm
# Time   : 20160612

class C(object):
    classattr = "attr on class"

    def f(self):
        return 'function f'

cobj = C()
cobj.instattr = "attr on instance"

print "cobj.classattr"
print cobj.classattr
print "cobj.instattr"
print cobj.instattr
print "C.__dict__['classattr']"
print C.__dict__['classattr']
print "cobj.__dict__['instattr']"
print cobj.__dict__['instattr']
print "cobj.__dict__"
print cobj.__dict__
print "C.__dict__"
print C.__dict__
print "f.__dir__"
print C.f.__dir__
