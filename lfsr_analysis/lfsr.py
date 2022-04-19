#!/bin/python
import os
import re

equal_point = 57336
eq_level = 8

# D^16+D^3+D^2+D^1+1
def lfsr_next (ini):
    nxt = (ini << 1) & 0xffff
    shift_in = ((ini & (1 << 15)) >> 15) ^ \
               ((ini & (1 << 2)) >> 2) ^ \
               ((ini & (1 << 1)) >> 1) ^ \
               ((ini & (1 << 0)) >> 0)
    nxt = nxt + shift_in
    return nxt

# D^16+D^14+D^13+D^11+D^9+D^8+1
def lfsr_next2 (ini):
    nxt = (ini << 1) & 0xffff
    shift_in = ((ini & (1 << 15)) >> 15) ^ \
               ((ini & (1 << 13)) >> 13) ^ \
               ((ini & (1 << 12)) >> 12) ^ \
               ((ini & (1 << 10)) >> 10) ^ \
               ((ini & (1 << 8)) >> 8) ^ \
               ((ini & (1 << 7)) >> 7)
    nxt = nxt + shift_in
    return nxt

#D^16+D^8+D^7+D^5+D^4+D^3+D^2+D^1+1
def lfsr_next3 (ini):
    nxt = (ini << 1) & 0xffff
    shift_in = ((ini & (1 << 15)) >> 15) ^ \
               ((ini & (1 << 7)) >> 7) ^ \
               ((ini & (1 << 6)) >> 6) ^ \
               ((ini & (1 << 4)) >> 4) ^ \
               ((ini & (1 << 3)) >> 3) ^ \
               ((ini & (1 << 2)) >> 2) ^ \
               ((ini & (1 << 1)) >> 1) ^ \
               ((ini & (1 << 0)) >> 0)
    nxt = nxt + shift_in
    return nxt

def lfsr_raw_out(ini):
    ret = (ini & (1<<15)) >> 15
    return ret
def lfsr_out (ini, poly):
    so = 0
    for it in poly:
        so = so ^ ((ini & (1<<it)) >> it)
    return so

li = 0xaaaa
ln = 0xaaaa
li2 = li
ln2 = ln
sl = [[], [], [], []]
for i in range(65536*2):
    if i < 10:
        print(hex(li))
    #s0 = lfsr_out(li, (15, 9, 7, 3))
    s0 = lfsr_raw_out(li)
    s1 = lfsr_out(li, (15,11, 7, 2))
    s2 = lfsr_out(li, (15, 9, 8, 1))
    s3 = lfsr_out(li, (15,12, 6, 0))
    ln = lfsr_next(li)
    li = ln
    ## 2
    #s1 = lfsr_raw_out(li2)
    #ln2 = lfsr_next3(li2)
    #li2 = ln2

    sl[0].append(s0)
    sl[1].append(s1)
    sl[2].append(s2)
    sl[3].append(s3)
    if li == 0xaaaa:
        print("Equal init, index: %d"%i)


print(sl[0][0:50])
print(sl[1][0:50])
print(sl[0][equal_point*1+0:equal_point*1+50])


# '0' and '1'
for i in range(4):
    print('---------------- row: %d info'%i)
    num0_max = 0
    num1_max = 0
    last_val = 9
    last_cnt = 0
    for j in range(equal_point):
        val = sl[i][j]
        if last_val == val:
            last_cnt += 1
        else:
            # update
            if last_val == 0:
                if num0_max < last_cnt:
                    num0_max = last_cnt
            else:
                if num1_max < last_cnt:
                    num1_max = last_cnt
            # init 
            last_val = val
            last_cnt = 1
    print('num0 max: %d'%num0_max)
    print('num1 max: %d'%num1_max)


# most equal len
for i in range(3):
    if i == 0:
        jl = [1,2,3]
    elif i == 1:
        jl = [2,3]
    elif i == 2:
        jl = [3]
    print('-----------list: %d'%i)
    for j in jl:
        print('----------- compare list: %d'%j)
        eqmax = 0
        eqlen = 0
        more_cnt = 0
        for x in range(equal_point*2):
            if sl[i][x] == sl[j][x]:
                eqlen += 1
            else:
                if eqlen >= eq_level:
                    more_cnt = more_cnt + 1
                    #print('eqmax: %d, index: %d'%(eqlen, x))
                # update
                if eqlen > eqmax:
                    eqmax = eqlen
                # reset
                eqlen = 0
        print('Update eqmax: %d, more_cnt: %d'%(eqmax, more_cnt))


