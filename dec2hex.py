import os, re

fsrc = "E:/btfddata/nok2.txt"
fdst = "E:/btfddata/nok2_hex.txt"

with open(fsrc, 'r') as f:
    din = f.readlines()

with open(fdst, 'w') as f:
    for line in din:
        print line.strip()
        h = int(line.strip())
        if h < 0:
            h = 2**32 + h
        h = hex(int(h))
        if len(h) < 10:
            h = "0"*(10-len(h)) + h[2:]
        else:
            h = h[2:]
        h = h[0:4] + '_' + h[4:8]
       
        f.write(h)
        f.write('\n')
