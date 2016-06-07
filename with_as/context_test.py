# -*- coding: utf-8 -*-
# Author : zwm
# Time   : 201606071003

'''
   __exit__() 返回值控制 exception 的处理。返回True时，异常会被抑制，程序正常向下执行。返回False时，异常会被传播出去。
'''

class context_test(object):
    def __init__(self, val='hello'):
        print 'Init of class context_test()'
        self.val = val

    def __enter__(self):
        print 'Enter of class context_test()'
        return self.val

    def __exit__(self, type, value, traceback):
        print 'Exit of class context_test()'
        print 'type         : ', type
        print 'value        : ', value
        print 'traceback    : ', traceback
        return True     # suppress exception
#        return False    # propagate exception


with context_test('123') as t:
    abc = aaa   # exception generate
    print t

print "Code following the with statement."
