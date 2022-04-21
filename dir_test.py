# -*- coding: utf-8 -*-
# Author : zwm
# Time   : 201606071003

'''
dir([object]) process
1. invoke object method named __dir__(), must return a list!!!
2. gather information form __dict__ attribute
3. __getattr__()
'''

class dir_test(object):
    __dict__ = ['__dict__', 'name', 'hello_dict']

    def __init__(self):
        self.name = 'dir_test'
        print 'Init of class dir_test()'

#    def __dir__(self):
#        print '__dir__() method invoked'
#        return ['__dir__()', 'name', 'hello_dir']

    def __getattr__(self):
        print '__getattr__() method invoked'
        return ['__getattr__()', 'name', 'hello_getattr']

