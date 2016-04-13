# -*- coding: utf-8 -*-
# Author : zwm
# Time   : 20160408
 


# 当使用from ... import时，前面不加module名。。
# 当只使用import时，必须加module名，使用module.class访问module内功能
#'''
from module1 import A
from module1 import fun1

a1 = A()
# a2 = module1.A() # cause error
f1 = fun1()
#'''


'''
import module1
a1 = module1.A()
# a2 = A()   # cause error
f1 = module1.fun1()
'''

