#!/bin/python
import os
import shutil

#----------------------------------------------------------------------------
# Macros
#----------------------------------------------------------------------------
log_path = r'E:\Code\case'
data_path = r'E:\Code\data_src'
path_delimiter = '\\'                   # for windows
#path_delimiter = '/'                    # for unix
dname_tx = 'tx_'                        # dir of transmit cases
dname_rx = 'rx_'                        # dir of receive cases
dname_txrx = 'txrx_'                    # dir of transceive cases
fname_case_cfg = 'case_cfg.dat'
fname_reg_cfg = 'reg_cfg.dat'
fname_tx_evlp = 'tx_evlp.dat'
fname_tx_fifo = 'tx_fifo.dat'
fname_reg_info = 'reg_info.dat'
fname_tx_crc = 'tx_crc.dat'
CASE_TYPE_RECEIVE           = 1
CASE_TYPE_TRANSMIT          = 2
CASE_TYPE_TRANSCEIVE        = 3

# Tx
tx_cfg = [
#   Common                   Type_A                  Type_B
#   [0] [1]   [2]    [3]     [4]    [5]     [6]      [7]    [8]    [9]    [10]   [11]   [12]
#   A/B cc_en cc_inv crc_pre prt_en prt_odd last_bit no_sof no_eof sof_lo sof_hi eof_lo egt
   [ 0,   0,    0,      0,      0,     0,       0,     0,     0,     0,     0,     0,    0 ], # 0
   [ 0,   0,    0,      0,      0,     0,       1,     0,     0,     0,     0,     0,    0 ], # 1
   [ 0,   0,    0,      0,      0,     0,       2,     0,     0,     0,     0,     0,    0 ], # 2
   [ 0,   0,    0,      0,      0,     0,       3,     0,     0,     0,     0,     0,    0 ], # 3
   [ 0,   0,    0,      0,      0,     0,       4,     0,     0,     0,     0,     0,    0 ], # 4
   [ 0,   0,    0,      0,      0,     0,       5,     0,     0,     0,     0,     0,    0 ], # 5
   [ 0,   0,    0,      0,      0,     0,       6,     0,     0,     0,     0,     0,    0 ], # 6
   [ 0,   0,    0,      0,      0,     0,       7,     0,     0,     0,     0,     0,    0 ], # 7
   [ 0,   0,    0,      0,      1,     0,       0,     0,     0,     0,     0,     0,    0 ], # 8
   [ 0,   0,    0,      0,      1,     1,       0,     0,     0,     0,     0,     0,    0 ], # 9
   [ 0,   1,    0,      0,      1,     1,       0,     0,     0,     0,     0,     0,    0 ], # 10
   [ 0,   1,    0,      1,      1,     1,       0,     0,     0,     0,     0,     0,    0 ], # 11
   [ 0,   1,    0,      2,      1,     1,       0,     0,     0,     0,     0,     0,    0 ], # 12
   [ 0,   1,    0,      4,      1,     1,       0,     0,     0,     0,     0,     0,    0 ], # 13
   [ 0,   1,    1,      0,      1,     1,       0,     0,     0,     0,     0,     0,    0 ], # 14
   [ 0,   1,    1,      1,      1,     1,       0,     0,     0,     0,     0,     0,    0 ], # 15
   [ 0,   1,    1,      2,      1,     1,       0,     0,     0,     0,     0,     0,    0 ], # 16
   [ 0,   1,    1,      4,      1,     1,       0,     0,     0,     0,     0,     0,    0 ], # 17
   [ 1,   0,    0,      0,      0,     0,       0,     0,     0,     0,     0,     0,    0 ], # 18
   [ 1,   0,    0,      0,      0,     0,       0,     0,     0,     0,     0,     0,    1 ], # 19
   [ 1,   0,    0,      0,      0,     0,       0,     0,     0,     0,     0,     0,    2 ], # 20
   [ 1,   0,    0,      0,      0,     0,       0,     0,     0,     0,     0,     0,    3 ], # 21
   [ 1,   0,    0,      0,      0,     0,       0,     0,     0,     0,     0,     0,    4 ], # 22
   [ 1,   0,    0,      0,      0,     0,       0,     0,     0,     0,     0,     0,    5 ], # 23
   [ 1,   0,    0,      0,      0,     0,       0,     0,     0,     0,     0,     0,    6 ], # 24
   [ 1,   0,    0,      0,      0,     0,       0,     0,     0,     0,     0,     0,    7 ], # 25
   [ 1,   0,    0,      0,      0,     0,       0,     1,     0,     0,     0,     0,    0 ], # 26
   [ 1,   0,    0,      0,      0,     0,       0,     1,     1,     1,     1,     1,    0 ], # 27
   [ 1,   1,    0,      0,      0,     0,       0,     0,     0,     0,     0,     0,    0 ], # 28
   [ 1,   1,    0,      1,      0,     0,       0,     0,     0,     0,     0,     0,    0 ], # 29
   [ 1,   1,    0,      2,      0,     0,       0,     0,     0,     0,     0,     0,    0 ], # 30
   [ 1,   1,    0,      3,      0,     0,       0,     0,     0,     0,     0,     0,    0 ], # 31
   [ 1,   1,    1,      0,      0,     0,       0,     0,     0,     0,     0,     0,    0 ], # 32
   [ 1,   1,    1,      1,      0,     0,       0,     0,     0,     0,     0,     0,    0 ], # 33
   [ 1,   1,    1,      2,      0,     0,       0,     0,     0,     0,     0,     0,    0 ], # 34
   [ 1,   1,    1,      3,      0,     0,       0,     0,     0,     0,     0,     0,    0 ]  # 35
]

# Rx
rx_cfg = [
#               rx_crc_en rx_crc_inv rx_crc_val rx_pty_en rx_pty_odd rx_alian
                [  0     ,    0     ,    0     ,    0    ,    0     ,     0     ],
                [  0     ,    0     ,    0     ,    0    ,    0     ,     1     ],
                [  0     ,    0     ,    0     ,    0    ,    0     ,     2     ],
                [  0     ,    0     ,    0     ,    0    ,    0     ,     3     ],
                [  0     ,    0     ,    0     ,    0    ,    0     ,     4     ],
                [  0     ,    0     ,    0     ,    0    ,    0     ,     5     ],
                [  0     ,    0     ,    0     ,    0    ,    0     ,     6     ],
                [  0     ,    0     ,    0     ,    0    ,    0     ,     7     ],
                [  0     ,    0     ,    0     ,    1    ,    0     ,     0     ],
                [  0     ,    0     ,    0     ,    1    ,    1     ,     0     ],
                [  1     ,    0     ,    0     ,    1    ,    1     ,     0     ],
                [  1     ,    0     ,    1     ,    1    ,    1     ,     0     ],
                [  1     ,    0     ,    2     ,    1    ,    1     ,     0     ],
                [  1     ,    0     ,    3     ,    1    ,    1     ,     0     ],
                [  1     ,    1     ,    0     ,    1    ,    1     ,     0     ],
                [  1     ,    1     ,    1     ,    1    ,    1     ,     0     ],
                [  1     ,    1     ,    2     ,    1    ,    1     ,     0     ],
                [  1     ,    1     ,    3     ,    1    ,    1     ,     0     ]
]
#!!! for debug
rx_cfg = tx_cfg

#----------------------------------------------------------------------------
# Class log_base
#----------------------------------------------------------------------------
class log_base (object):
    def __init__(self, baud_rate=0, tc=[], rc=[], log_path='', data_path='', case_index=0):
        #self.crc_poly           = 0x11021
        self.baud_rate           = baud_rate
        self.tc                  = tc
        self.rc                  = rc
        self.log_path            = log_path
        self.data_path           = data_path
        self.case_index          = case_index

    def reg_parse(self):
        self.crc_poly            = 0x8408
        self.tx_coding           = self.tc[0]
        self.tx_crc_en           = self.tc[1]
        self.tx_crc_invert       = self.tc[2]
        self.tx_crc_preset_val   = self.tc[3]
        self.tx_parity_en        = self.tc[4]
        self.tx_parity_odd       = self.tc[5]
        self.tx_last_bits        = self.tc[6]
        self.tx_no_sof           = self.tc[7]
        self.tx_no_eof           = self.tc[8]
        self.sof_lo_width        = self.tc[9]
        self.sof_hi_width        = self.tc[10]
        self.eof_width           = self.tc[11]
        self.charspacing         = self.tc[12]
        self.rx_parity_en        = self.rc[4]
        self.rx_parity_odd       = self.rc[5]
        if (self.baud_rate == 0):   self.tx_mod_width = 31 # 28~40.5
        elif (self.baud_rate == 1): self.tx_mod_width = 17 # 16.5~20
        elif (self.baud_rate == 2): self.tx_mod_width = 8  # 8~10
        elif (self.baud_rate == 3): self.tx_mod_width = 4  # 4~5

    def reg_asm (self):
        self.reg_parse()
        reg_asm = []
        # 0x00, nfc_en=1, enable block
        reg_addr = 0x00
        reg_val = 0x10
        reg_asm.append([reg_addr, reg_val])
        # 0x02, flush_fifo=1, flush_fifo
        reg_addr = 0x02
        reg_val = 0x01
        reg_asm.append([reg_addr, reg_val])
        # 0x02, flush_fifo=0, flush_fifo
        reg_addr = 0x02
        reg_val = 0x00
        reg_asm.append([reg_addr, reg_val])
        #***************
        # Tx Related
        #***************
        # 24, tx_coder_ctrl
        reg_addr = 24
        reg_val = self.baud_rate + self.tx_coding*4 + self.tx_last_bits*8;
        reg_asm.append([reg_addr, reg_val])
        # 25, tx_crc_ctrl
        reg_addr = 25
        reg_val = self.tx_crc_en + self.tx_crc_invert*2 + self.tx_crc_preset_val*4 + self.charspacing*32;
        reg_asm.append([reg_addr, reg_val])
        # 26, mod_width
        reg_addr = 26
        reg_asm.append([reg_addr, self.tx_mod_width])
        # 27, tx_type_b_framing
        reg_addr = 27
        reg_val = self.sof_lo_width + self.sof_hi_width*4 + self.eof_width*16 + self.tx_no_eof*64 + self.tx_no_sof*128
        reg_asm.append([reg_addr, reg_val])
        # 28, fram_con
        reg_addr = 28
        reg_val = self.tx_parity_en + self.rx_parity_en*2 + self.tx_parity_odd*4 + self.rx_parity_odd*8;
        reg_asm.append([reg_addr, reg_val])
        #***************
        # Rx Related
        #***************
        # return
        return reg_asm

    def reg_info_gen (self, case_dir):
        with open(case_dir + path_delimiter + fname_reg_info, 'w') as f:
            f.write('baud_rate          0x%02x\n'%self.baud_rate)
            f.write('tx_coding          0x%02x\n'%self.tx_coding)
            f.write('tx_crc_en          0x%02x\n'%self.tx_crc_en)
            f.write('tx_crc_invert      0x%02x\n'%self.tx_crc_invert)
            f.write('tx_crc_preset_val  0x%02x\n'%self.tx_crc_preset_val)
            f.write('tx_parity_en       0x%02x\n'%self.tx_parity_en)
            f.write('tx_parity_odd      0x%02x\n'%self.tx_parity_odd)
            f.write('tx_last_bits       0x%02x\n'%self.tx_last_bits)
            f.write('tx_no_sof          0x%02x\n'%self.tx_no_sof)
            f.write('tx_no_eof          0x%02x\n'%self.tx_no_eof)
            f.write('sof_lo_width       0x%02x\n'%self.sof_lo_width)
            f.write('sof_hi_width       0x%02x\n'%self.sof_hi_width)
            f.write('eof_width          0x%02x\n'%self.eof_width)
            f.write('charspacing        0x%02x\n'%self.charspacing)
            f.write('rx_parity_en       0x%02x\n'%self.rx_parity_en)
            f.write('rx_parity_odd      0x%02x\n'%self.rx_parity_odd)
            f.write('tx_mod_width       0x%02x\n'%self.tx_mod_width)

    def reg_cfg_gen (self, case_dir):
        reg_asm = self.reg_asm()
        with open(case_dir + path_delimiter + fname_reg_cfg, 'w') as f:
            for i in range(len(reg_asm)):
                reg_addr = reg_asm[i][0]
                reg_val = reg_asm[i][1]
                reg_val = hex(reg_val)
                if len(reg_val)<4: # <16
                    reg_val = '0' + reg_val[2]
                else:
                    reg_val = reg_val[2:4]
                f.write("%d %s\n" % (reg_addr, reg_val))

    def case_cfg_gen (self, case_dir, case_type):
        with open(case_dir + path_delimiter + fname_case_cfg, 'w') as f:
            f.write("%02x\n"%case_type)

    def seq_x_gen (self, baud_rate, mod_width):
        t = ''
        etu_len = int(128/(2**baud_rate))
        for etu_cnt in range(int(etu_len/2)):
            t=t+'1\n'
        for etu_cnt in range(mod_width+1):
            t=t+'0\n'
        for etu_cnt in range(int(etu_len/2 - (mod_width+1))):
            t=t+'1\n'
        return t

    def seq_y_gen (self, baud_rate, mod_width):
        t = ''
        etu_len = int(128/(2**baud_rate))
        for etu_cnt in range(etu_len):
            t=t+'1\n'
        return t

    def seq_z_gen (self, baud_rate, mod_width):
        t = ''
        etu_len = int(128/(2**baud_rate))
        for etu_cnt in range(mod_width+1):
            t=t+'0\n'
        for etu_cnt in range(etu_len - (mod_width+1)):
            t=t+'1\n'
        return t

    def etu_lo_gen (self, baud_rate):
        t = ''
        etu_len = int(128/(2**baud_rate))
        for etu_cnt in range(etu_len):
            t=t+'0\n'
        return t

    def etu_hi_gen (self, baud_rate):
        t = ''
        etu_len = int(128/(2**baud_rate))
        for etu_cnt in range(etu_len):
            t=t+'1\n'
        return t

    def tx_evlp_gen (self, case_dir, data_file):
        data_byte = []
        with open (data_file, 'r') as f:
            for i in f:
                data_byte.append(i.strip())
        data_byte = self.crc_proc(data_byte, self.tx_crc_en, self.tx_crc_invert, self.tx_crc_preset_val)
        # print debug info: tx_crc
        with open (case_dir + path_delimiter + fname_tx_crc, 'w') as f:
            if self.tx_crc_en == 1:
                f.write(data_byte[-2]+'\n')
                f.write(data_byte[-1]+'\n')
            else:
                f.write('\n')
        etu_len = int(128/(2**self.baud_rate))
        evlp = ''
        # Type A
        if self.tx_coding == 0: 
            # SOF: Sequence Z
            evlp = evlp + self.seq_z_gen(self.baud_rate, self.tx_mod_width)
            etu_bak = 0
            # DataByte
            for byt_idx in range(len(data_byte)):
                byt = int(data_byte[byt_idx], 16)
                prt = 0 # parity
                # data_byte
                for bit_idx in range(8):
                    if (self.tx_last_bits != 0) and (byt_idx == (len(data_byte)-1)) and (bit_idx >= self.tx_last_bits):
                        break
                    else:
                        etu = byt & 1
                        byt = byt >> 1
                        prt = prt ^ etu
                        #Sequence Z
                        if (etu == 0) and (etu_bak == 0):
                            evlp = evlp + self.seq_z_gen(self.baud_rate, self.tx_mod_width)
                        #Sequence Y
                        elif (etu == 0) and (etu_bak == 1):
                            evlp = evlp + self.seq_y_gen(self.baud_rate, self.tx_mod_width)
                        #Sequence X
                        elif (etu == 1):
                            evlp = evlp + self.seq_x_gen(self.baud_rate, self.tx_mod_width)
                        etu_bak = etu
                # parity
                if (self.tx_last_bits != 0) and (byt_idx == (len(data_byte)-1)) and (bit_idx >= self.tx_last_bits):
                    break
                else:
                    if self.tx_parity_en:
                        prt = prt ^ self.tx_parity_odd
                        etu = prt
                        #Sequence Z
                        if (etu == 0) and (etu_bak == 0):
                            evlp = evlp + self.seq_z_gen(self.baud_rate, self.tx_mod_width)
                        #Sequence Y
                        elif (etu == 0) and (etu_bak == 1):
                            evlp = evlp + self.seq_y_gen(self.baud_rate, self.tx_mod_width)
                        #Sequence X
                        elif (etu == 1):
                            evlp = evlp + self.seq_x_gen(self.baud_rate, self.tx_mod_width)
                        etu_bak = etu
            # EOF, logic '0' followed by sequence Y
            if etu_bak == 0:
                evlp = evlp + self.seq_z_gen(self.baud_rate, self.tx_mod_width)
                evlp = evlp + self.seq_y_gen(self.baud_rate, self.tx_mod_width)
            else:
                evlp = evlp + self.seq_y_gen(self.baud_rate, self.tx_mod_width)
                evlp = evlp + self.seq_y_gen(self.baud_rate, self.tx_mod_width)
            # Additional 10 etu seuqence Y
            for i in range(10):
                evlp = evlp + self.seq_y_gen(self.baud_rate, self.tx_mod_width)
        # Type B
        else:
            etu_len = int(128/(2**self.baud_rate))
            # SOF_LO
            if self.tx_no_sof == 0:
                if self.sof_lo_width == 0:
                    tmp = 10*etu_len
                elif self.sof_lo_width == 1:
                    tmp = 10*etu_len + int(etu_len/2)
                else:
                    tmp = 11*etu_len
                for i in range(tmp):
                    evlp = evlp + '0\n'
            # SOF_HI
            if self.tx_no_sof == 0:
                if self.sof_hi_width == 0:
                    tmp = 2*etu_len
                elif self.sof_hi_width == 1:
                    tmp = 2*etu_len + int(etu_len/2)
                else:
                    tmp = 3*etu_len
                for i in range(tmp):
                    evlp = evlp + '1\n'
            # DataByte
            for byt_idx in range(len(data_byte)):
                byt = int(data_byte[byt_idx], 16)
                # Start, logic '0'
                evlp = evlp + self.etu_lo_gen(self.baud_rate)
                # Data
                for bit_idx in range(8):
                    etu = byt & 1
                    byt = byt >> 1
                    if etu == 0:
                        evlp = evlp + self.etu_lo_gen(self.baud_rate)
                    else:
                        evlp = evlp + self.etu_hi_gen(self.baud_rate)
                # Stop, logic '1'
                evlp = evlp + self.etu_hi_gen(self.baud_rate)
                # EGT
                for i in range(self.charspacing):
                    evlp = evlp + self.etu_hi_gen(self.baud_rate)
            # EOF_LO
            if self.tx_no_eof == 0:
                if self.eof_width == 0:
                    tmp = 10*etu_len
                elif self.eof_width == 1:
                    tmp = 10*etu_len + int(etu_len/2)
                else:
                    tmp = 11*etu_len
                for i in range(tmp):
                    evlp = evlp + '0\n'
            # Additional 10 etu logic '1'
            for i in range(10*etu_len):
                evlp = evlp + '1\n'
        # Write File
        with open(case_dir + path_delimiter + fname_tx_evlp, 'w') as f:
            f.write(evlp)

    def crc_proc (self, data_byte, crc_en, crc_inv, crc_init):
        if crc_en == 0:
            return data_byte
        if crc_init == 0:
            crc = 0
        elif crc_init == 1:
            crc = 0x6363
        elif crc_init == 2:
            crc = 0xA671
        elif crc_init == 3:
            crc = 0xFFFE
        else:
            crc = 0xFFFF
        for i in data_byte:
            tmp = int(i, 16)
            for j in range(8):
                # 14443-3 B.1 data shift in from msb, shift out from lsb
                pre = (crc^tmp)&1
                #tmp = (int(i, 16)>>(7-j)) & 0x1
                #tmp = (int(i, 16)>>j) & 1
                tmp = tmp>>1
                if pre == 1:
                    crc = (crc>>1) ^ self.crc_poly
                else:
                    crc = (pre<<15) + (crc>>1)
        if crc_inv == 1:
            crc = ~crc
        tmp = data_byte
        crc_lsb = crc&0xFF
        crc_msb = (crc>>8)&0xFF
        crc_lsb = hex(crc_lsb)
        crc_msb = hex(crc_msb)
        if len(crc_lsb) < 4:
            crc_lsb = '0' + crc_lsb[2]
        else:
            crc_lsb = crc_lsb[2:4]
        if len(crc_msb) < 4:
            crc_msb = '0' + crc_msb[2]
        else:
            crc_msb = crc_msb[2:4]
        tmp.append(crc_lsb)
        tmp.append(crc_msb)
        return tmp

    def log_dir_clear (self):
        if os.path.exists(self.log_path):
            shutil.rmtree(self.log_path)
        os.mkdir(self.log_path)

    def tx_log_gen (self):
        self.reg_parse()
        for (maindir, subdir, dl) in os.walk(self.data_path):
            pass
        for i in dl:
            case_dir = log_path + path_delimiter + dname_tx + '%03d%02d'%(self.case_idx, int(i))
            data_file = data_path + path_delimiter + i
            if os.path.exists(case_dir):
                shutil.rmtree(case_dir)
            os.mkdir(case_dir)
            self.case_cfg_gen(case_dir, CASE_TYPE_TRANSMIT)
            self.reg_cfg_gen(case_dir)
            self.reg_info_gen(case_dir)
            self.tx_evlp_gen(case_dir, data_file)
            shutil.copyfile(data_file, case_dir + path_delimiter + fname_tx_fifo)

def main():
    # Log Instance
    log_inst = log_base()
    log_inst.log_path  = log_path
    log_inst.data_path = data_path
    log_inst.log_dir_clear()
    case_idx = 0;
    for baud_rate in range(1):
        case_idx = baud_rate*100
        #for i in range(len(tx_cfg)):
        for i in range(1):
            log_inst.baud_rate = baud_rate
            log_inst.tc        = tx_cfg[i]
            log_inst.rc        = rx_cfg[i]
            log_inst.case_idx  = case_idx
            log_inst.tx_log_gen()
            case_idx = case_idx + 1

## reg_gen
#def reg_info_gen (baud_rate, tc, rc):
#    tx_coding           = tc[0]
#    tx_crc_en           = tc[1]
#    tx_crc_invert       = tc[2]
#    tx_crc_preset_val   = tc[3]
#    tx_parity_en        = tc[4]
#    tx_parity_odd       = tc[5]
#    tx_last_bits        = tc[6]
#    tx_no_sof           = tc[7]
#    tx_no_eof           = tc[8]
#    sof_lo_width        = tc[9]
#    sof_hi_width        = tc[10]
#    eof_width           = tc[11]
#    charspacing         = tc[12]
#    rx_parity_en        = rc[4]
#    rx_parity_odd       = rc[5]
#    reg_info = []
#    # 0x00, nfc_en=1, enable block
#    reg_addr = 0x00
#    reg_val = 0x10
#    reg_info.append([reg_addr, reg_val])
#    # 0x02, flush_fifo=1, flush_fifo
#    reg_addr = 0x02
#    reg_val = 0x01
#    reg_info.append([reg_addr, reg_val])
#    # 0x02, flush_fifo=0, flush_fifo
#    reg_addr = 0x02
#    reg_val = 0x00
#    reg_info.append([reg_addr, reg_val])
#    #***************
#    # Tx Related
#    #***************
#    # 24, tx_coder_ctrl
#    reg_addr = 24
#    reg_val = baud_rate + tx_coding*4 + tx_last_bits*8;
#    reg_info.append([reg_addr, reg_val])
#    # 25, tx_crc_ctrl
#    reg_addr = 25
#    reg_val = tx_crc_en + tx_crc_invert*2 + tx_crc_preset_val*4 + charspacing*32;
#    reg_info.append([reg_addr, reg_val])
#    # 26, mod_width
#    reg_addr = 26
#    if (baud_rate == 0):   reg_val = 31 # 28~40.5
#    elif (baud_rate == 1): reg_val = 17 # 16.5~20
#    elif (baud_rate == 2): reg_val = 8  # 8~10
#    elif (baud_rate == 3): reg_val = 4  # 4~5
#    reg_info.append([reg_addr, reg_val])
#    # 27, tx_type_b_framing
#    reg_addr = 27
#    reg_val = sof_lo_width + sof_hi_width*4 + eof_width*16 + tx_no_eof*64 + tx_no_sof*128
#    reg_info.append([reg_addr, reg_val])
#    # 28, fram_con
#    reg_addr = 28
#    reg_val = tx_parity_en + rx_parity_en*2 + tx_parity_odd*4 + rx_parity_odd*8;
#    reg_info.append([reg_addr, reg_val])
#    #***************
#    # Rx Related
#    #***************
#
#    # return
#    return reg_info
#
#def write_reg_cfg (casedir, reginfo):
#    print("reginfo: ")
#    print(reginfo)
#    with open(casedir+'\\reg_cfg.dat', 'w') as f:
#        for i in range(len(reginfo)):
#            reg_addr = reginfo[i][0]
#            reg_val = reginfo[i][1]
#            reg_val = hex(reg_val)
#            if len(reg_val)<4: # <16
#                reg_val = '0' + reg_val[2]
#            else:
#                reg_val = reg_val[2:4]
#            f.write("%d %s\n" % (reg_addr, reg_val))

# main
if __name__ == '__main__':
    main()

