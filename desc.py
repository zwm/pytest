#!/usr/bin/env python
# -*- coding: utf-8 -*-
# test descriptor

'''
Creating Descriptors
Any object with a __get__() method, and optionally __set__() and __delete__() methods,
accepting specific parameters is said to follow the DESCRIPTOR PROTOCOL.
Such an object qualifies as a descriptor and can be placed inside a class's __dict__
to do something special when an attribute is retrived, set or deleted.

Descriptors are invoked by the __getattribute__() method

Overriding __getattribute__() prevents automatic descriptor calls

'''

class Desc(object):
    "A descriptor example that just demonstrates the protocol"
    def __init__(self):
        self.data = "Init"

    def __get__(self, obj, cls=None):
        print "self : ", self
        print "obj  : ", obj
        print "cls  : ", cls
        return self.data

    def __set__(self, obj, val):
        print "self : ", self
        print "obj  : ", obj
        print "val  : ", val
        self.data = val
  
    def __delete__(self, obj):
        print "self : ", self
        print "obj  : ", obj
        del self.data

    def funny(self):
        print 'You invoked function: funny() of class Desc() ::: ', self, self.data

# attach it to a class and put it to work
class C(object):
    "A class with a single descriptor"
    d = Desc()
    d.funny()
    def fun(self):
        pass

'''
  C.__dict__['fun'] : the most direct way to get item, it's just a function
  C.fun             : actually there will be C.__dict__['fun'].__get__(None, class), the access of this way is internally wrappered
  cobj.fun          : actually there will be C.__dict__['fun'].__get__(cobj, class), the access of this way is internally wrappered
'''
cobj = C()
e = Desc()

