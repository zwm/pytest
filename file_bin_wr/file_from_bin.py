import os
import re
import sys
import struct

# parameter
out_test_en = 1
write_file_en = 1

# argument
arg_num = len(sys.argv)
if arg_num == 2:
    fi = sys.argv[1]
    print('INFO file name: %s' % (fi))
else:
    fi = ''
    print('ERROR: no input file!!!')
    sys.exit(0)

# function
def my_int2hex(i_int):
    if i_int < 10: # 0~9
        i_int = i_int + 48
    else: # A~F
        i_int = i_int + 65 - 10
    i_chr = chr(i_int)
    return i_chr

def my_bytes2char(bt):
    i_int = int.from_bytes(bt, byteorder='big')
    bl = i_int & 15
    bh = (i_int >> 4) & 15
    bl_chr = my_int2hex(bl)
    bh_chr = my_int2hex(bh)
    o_chr = bh_chr + bl_chr
    return o_chr

def my_charproc(ch):
    if ch == 'O' or ch == 'o':
        ch = '0'
    elif ch == 'L' or ch == 'l':
        ch = '1'
    return ch

# size
fs = 0
fs = os.path.getsize(fi)
print('INFO file size: %0d bytes' % (fs))

# read
line_str = ''
with open(fi, 'r') as f:
    for l in f:
        l = l.strip()
        line_str = line_str + l

# out test
if out_test_en:
    # rename
    res = re.search('\.', fi)
    if res:
        sp = res.start()
        fo = fi[:sp-1] + '_hexout' + fi[sp:]
    else:
        fo = fi + '_hexout'
    # write
    with open(fo, 'w') as f:
        f.write(line_str)
    print('INFO test file: %s write finish.' % fo)

# write file
if write_file_en:
    # rename
    res = re.search('\.', fi)
    if res:
        sp = res.start()
        fo = fi[:sp-1] + '_bin' + fi[sp:]
    else:
        fo = fi + '_bin'
    # write
    with open(fo, 'wb') as f:
        for i in range(len(line_str)):
            if i&1 == 0:
                bh = line_str[i]
                bh = my_charproc(bh)
            else:
                bl = line_str[i]
                bl = my_charproc(bl)
                # to int
                bh = int(bh, 16)
                bl = int(bl, 16)
                bt = bh*16 + bl
                bt = bt.to_bytes(1, byteorder='big', signed=False)
                f.write(bt)
    print('INFO write bin file: %s write finish.' % fo)



