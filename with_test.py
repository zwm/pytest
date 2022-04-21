#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os 



#try:
#    f = open("a.txt")
#    print "Open file a.txt"
#except:
#    print "Error when open a.txt"
#finally:
#    print "Close file"
#    f.close()

try:
    f = open("a.txt")
except:
    print "Error open a.txt"
    exit(-1)

try:
    print "Open file a.txt"
except:
    print "Error!!!"
finally:
    f.close()
