# -*- coding: utf-8 -*-
# Author : zwm
# Time   : 20160408
import os 

'''
在python2.5及以后，file对象已经写好了__enter__和__exit__函数，我们可以这样测
>>> f = open("x.txt")
>>> f
<open file 'x.txt', mode 'r' at 0x00AE82F0>
>>> f.__enter__()
<open file 'x.txt', mode 'r' at 0x00AE82F0>
>>> f.read(1)
'X'
>>> f.__exit__(None, None, None)
>>> f.read(1)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file
之后，我们如果要打开文件并保证最后关闭他，只需要这么做：
with open("x.txt") as f:
    data = f.read()
    do something with data
如果有多个项，我们可以这么写：
with open("x.txt") as f1, open('xxx.txt') as f2:
    do something with f1,f2
'''

class opened(object):
    def __init__(self, name):
        print 'Init of class opened()'
        self.handle = open(name)
#        try:
#            self.handle = open(name)
#        except:
#            print "Error when opening file."
#            exit(-1)

    def __enter__(self):
        print 'Enter of class opened()'
        return self.handle

    def __exit__(self, type, value, traceback):
        print 'Exit of class opened()'
        print 'type         : ', type
        print 'value        : ', value
        print 'traceback    : ', traceback
        self.handle.close()


with opened('./a.txt') as f:
    for line in f.readlines():
        print(line)
