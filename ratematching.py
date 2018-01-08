#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os 

bit_len = 57

# 0: puncture
# 1: repeat
rm_repeat = 1

rm_ei = 1
rm_em = 128
rm_ep = 114


print "RM_INX   BIT_IDX"
j = 0
for i in range(bit_len):
    if rm_repeat == 1 :      # repeat
        print "%4d\t%4d" % (j, i)
        j = j + 1
        rm_ei = rm_ei - rm_em
        while rm_ei <= 0:
            print "%4d\t%4d" % (j, i)
            j = j + 1
            rm_ei = rm_ei + rm_ep
    elif rm_repeat == 0 :   # puncture
        pass
    else:
        print ""
        print "ERROR PARAMETER : rm_repeat"
        break

