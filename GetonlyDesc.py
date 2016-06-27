#!/usr/bin/env python
# -*- coding: utf-8 -*-
# test get only descriptor

'''

'''

class GetonlyDesc(object):
    "Another descriptor"
    def __init__(self):
        self.data = "Init"

    def __get__(self, obj, cls=None):
        print "self : ", self
        print "obj  : ", obj
        print "cls  : ", cls
        return self.data

    def funny(self):
        print 'You invoked function: funny() of class Desc() ::: ', self, self.data

# attach it to a class and put it to work
class C(object):
    "A class with a single descriptor"
    d = GetonlyDesc()

cobj = C()

