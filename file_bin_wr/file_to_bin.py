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


# input
lc = []
fs = 0
fs = os.path.getsize(fi)
print('INFO file size: %0d bytes' % (fs))
with open(fi, 'rb') as f:
    for i in range(fs):
        one_byte = f.read(1)
        lc.append(one_byte)

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

# out test
if out_test_en:
    # rename
    res = re.search('\.', fi)
    if res:
        sp = res.start()
        fo = fi[:sp-1] + '_testout' + fi[sp:]
    else:
        fo = fi + '_testout'
    # write
    with open(fo, 'wb') as f:
        for i in range(fs):
            one_byte = lc[i]
            f.write(one_byte)
    print('INFO test file: %s write finish.' % fo)

# write file
if write_file_en:
    # rename
    res = re.search('\.', fi)
    if res:
        sp = res.start()
        fo = fi[:sp-1] + '_hex' + fi[sp:]
    else:
        fo = fi + '_hex'
    # write
    with open(fo, 'w') as f:
        for i in range(fs):
            one_byte = lc[i]
            hx = my_bytes2char(one_byte)
            f.write(hx)
    print('INFO write file: %s write finish.' % fo)



