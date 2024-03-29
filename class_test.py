#!/usr/bin/env python
# -*- coding: utf-8 -*-
# blog.ithomer.net
 
class Test(object):
    x = 11
    def __init__(self, _x):
        print("__init__ has been invoked")
        self._x = _x
        print("Test.__init__")
  
    @classmethod
    def class_method(cls):
        print("class_method")
  
    @staticmethod
    def static_method():
        print("static_method")
  
    @classmethod
    def getPt(cls):
        cls.class_method()
#        class_method(cls)      # Error!
        cls.static_method()
  
if "__main__" == __name__:
    Test.class_method()         # class_method
    Test.static_method()        # static_method
    Test.getPt()                # class_method  static_method
 
    t = Test(22)                # Test.__init__
    t.class_method()            # class_method
    t.static_method()           # static_method

#    print("Test.__dict__: " + Test.__dict__)
    print("Test.__dict__: ")
    print(Test.__dict__)
    print("Test.__name__: ")
    print(Test.__name__)
    print("Test.__doc__: ")
    print(Test.__doc__)
    print("Test.__bases__: ")
    print(Test.__bases__)
     
    print(Test.x)               # 11
#     print Test._x
     
    print(t.x)                  # 11
    print(t._x)                 # 22
     
#     t.getPr()   # 'Test' object has no attribute 'getPr'
