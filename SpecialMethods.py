#!/usr/bin/env python
# -*- coding: utf-8 -*-
# test special methods

'''
* Special methods work on type only!!!
'''
class C(object):
    def __len__(self):
        return 0

cobj = C()

def mylen():
    return 1

cobj.__len__ = mylen
print len(cobj)


'''
* A simple technique to allow defining such methods for each instance separately is shown below.
'''

class D(object):
    def __len__(self):
        return self._instlen()
    def _instlen(self):
        return 0

dobj = D()

def instlen():
    return 1

dobj._instlen = instlen
print len(dobj)
    
i = 1
assert i == 1       # no message reported
assert i != 1       # assertion_exception reported

