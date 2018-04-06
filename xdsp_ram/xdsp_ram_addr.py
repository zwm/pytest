#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os 

# const
XDSP_TOP_BASE   = 0x01C00000        # bit[31:22] = ??, bit[21] = 0
XDSP0_BASE      = 0x00000000        # bit[20:19] = "00"
XDSP1_BASE      = 0x00080000        # bit[21:19] = "01"
XDSP2_BASE      = 0x00100000        # bit[21:19] = "10"
XDSP_SHARE_BASE = 0x00180000        # bit[21:19] = "11"

XDSP_RAM_OFFSET = (('IRAM           ',  '12288*32b',    0x00000000),
                   ('D0RAM_LONG_SAT ',  ' 5120*40b',    0x00010000),
                   ('D0RAM_LONG_CHOP',  ' 5120*40b',    0x00018000),
                   ('D0RAM_CPLX_SAT ',  ' 5120*40b',    0x00020000),
                   ('D0RAM_CPLX_CHOP',  ' 5120*40b',    0x00028000),
                   ('D0RAM_OVFL     ',  ' 5120*40b',    0x00030000),
                   ('D1RAM          ',  ' 2048*20b',    0x00040000),
                   ('D2RAM          ',  ' 2048*20b',    0x00048000),)
                    
SHARE_RAM_OFFSET = (('XDSP_SHARE_RAM ',  '  512*40b',    0x00000000),)


#print result
with open ('xdsp_ram_addr.dat', 'w') as fp:
    # xdsp 0~2
    for i in range(3):
        if i == 0:
            base = XDSP0_BASE
        elif i == 1:
            base = XDSP1_BASE
        elif i == 2:
            base = XDSP2_BASE
        for i in range(len(XDSP_RAM_OFFSET)):
            line = XDSP_RAM_OFFSET[i][0] + ' '*4 + XDSP_RAM_OFFSET[i][1] 
            offset = hex(XDSP_TOP_BASE + base + XDSP_RAM_OFFSET[i][2])
            offset = offset.upper()
            if len(offset) < 10:
                offset = '0x' + '0'*(10-len(offset)) + offset[2:]
            else:
                offset = '0x' + offset[2:]
            line = line + ' '*8 + offset + '\n'
            fp.write(line)
        fp.write('\n')
    # share ram
    for i in range(len(SHARE_RAM_OFFSET)):
        line = SHARE_RAM_OFFSET[i][0] + ' '*4 + SHARE_RAM_OFFSET[i][1] 
        offset = hex(XDSP_TOP_BASE + XDSP_SHARE_BASE + SHARE_RAM_OFFSET[i][2])
        offset = offset.upper()
        if len(offset) < 10:
            offset = '0x' + '0'*(10-len(offset)) + offset[2:]
        else:
            offset = '0x' + offset[2:]
        line = line + ' '*8 + offset + '\n'
        fp.write(line)
