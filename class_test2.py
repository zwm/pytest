#!/usr/bin/env python
# -*- coding: utf-8 -*-
# blog.ithomer.net
 
class MyClass(object):
    def __init__(self):
        print '__init__'
        self._name = 'blog.ithomer.net'
 
    @staticmethod
    def static_method():
        print 'This is a static method!'
 
    def test(self):
        print 'call test'
 
    @classmethod
    def class_method(cls):
        print 'cls: ',cls
        print 'cls.name: ',cls.name
        print 'cls.static_method(): ',cls.static_method()
        instance = cls()
        print 'instance.test(): ',instance.test()
 
    @property
    def name(self):
        return self._name
     
    @name.setter
    def name(self, value):
        self._name = value
 
if __name__ == '__main__':
    MyClass.static_method()
    MyClass.class_method()
     
    mc = MyClass()
    print mc.name
    mc.name = 'forum.ithomer.net' 
    print mc.name
