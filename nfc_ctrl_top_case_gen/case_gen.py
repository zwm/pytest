#!/bin/python
import os
import shutil
#----------------------------------------------------------------------------
# Macros
#----------------------------------------------------------------------------
# ctrl
const_rx_baudrate_num = 4
# log
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
fname_rx_etu = 'rx_etu.dat'
fname_rx_fifo = 'rx_fifo.dat'
fname_reg_info = 'reg_info.dat'
fname_tx_crc = 'tx_crc.dat'
fname_rx_crc = 'rx_crc.dat'
fname_etu_cfg = 'etu_cfg.dat'
CASE_TYPE_RECEIVE           = 1
CASE_TYPE_TRANSMIT          = 2
CASE_TYPE_TRANSCEIVE        = 3
# rx demod reg_cfg
const_minlevel = 394
const_dpll_dither = 2
const_data_gain = 0
const_combine_mod = 0
const_coll_level = 6
const_det_gen = 2
const_force_rssi_calc = 0
const_win_size = 1
const_new_peak_en = 0
const_peak_num = 4
const_peak_shift = 2
const_adc_format = 1

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
   [ 0,   1,    0,      1,      1,     1,       0,     0,     0,     0,     0,     0,    0 ], # 11 * 14443 Type A
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
   [ 1,   1,    1,      3,      0,     0,       0,     0,     0,     0,     0,     0,    0 ]  # 35 # 14443 Type B?
]

# Rx
rx_cfg = [
#   Common                   Type_A                                      Type_B
#   [0] [1]   [2]    [3]     [4]    [5]     [6]      [7]    [8]    [9]   [10]   [11]   [12]   [13]   [14]   [15]   [16]  [17]  [18]
#   A/B cc_en cc_inv crc_pre prt_en prt_odd rx_alian collen nocoll vaftc rx_sof rx_eof rx_tlr ralltb inscdt emdsup emdhi emdlo rxmtpl
   [ 0,   0,    0,      0,      0,     0,     0,      0,     0,     0,     0,     0,     3,     0,     0,     0,     0,    0,    0    ], # 0
   [ 0,   0,    0,      0,      0,     0,     1,      0,     0,     0,     0,     0,     3,     0,     0,     0,     0,    0,    0    ], # 1
   [ 0,   0,    0,      0,      0,     0,     2,      0,     0,     0,     0,     0,     3,     0,     0,     0,     0,    0,    0    ], # 2
   [ 0,   0,    0,      0,      0,     0,     3,      0,     0,     0,     0,     0,     3,     0,     0,     0,     0,    0,    0    ], # 3
   [ 0,   0,    0,      0,      0,     0,     4,      0,     0,     0,     0,     0,     3,     0,     0,     0,     0,    0,    0    ], # 4
   [ 0,   0,    0,      0,      0,     0,     5,      0,     0,     0,     0,     0,     3,     0,     0,     0,     0,    0,    0    ], # 5
   [ 0,   0,    0,      0,      0,     0,     6,      0,     0,     0,     0,     0,     3,     0,     0,     0,     0,    0,    0    ], # 6
   [ 0,   0,    0,      0,      0,     0,     7,      0,     0,     0,     0,     0,     3,     0,     0,     0,     0,    0,    0    ], # 7
   [ 0,   0,    0,      0,      1,     0,     0,      0,     0,     0,     0,     0,     3,     0,     0,     0,     0,    0,    0    ], # 8
   [ 0,   0,    0,      0,      1,     1,     0,      0,     0,     0,     0,     0,     3,     0,     0,     0,     0,    0,    0    ], # 9
   [ 0,   1,    0,      0,      1,     1,     0,      0,     0,     0,     0,     0,     3,     0,     0,     0,     0,    0,    0    ], # 10
   [ 0,   1,    0,      1,      1,     1,     0,      0,     0,     0,     0,     0,     3,     0,     0,     0,     0,    0,    0    ], # 11 * 14443 Type A
   [ 0,   1,    0,      2,      1,     1,     0,      0,     0,     0,     0,     0,     3,     0,     0,     0,     0,    0,    0    ], # 12
   [ 0,   1,    0,      3,      1,     1,     0,      0,     0,     0,     0,     0,     3,     0,     0,     0,     0,    0,    0    ], # 13
   [ 0,   1,    1,      0,      1,     1,     0,      0,     0,     0,     0,     0,     3,     0,     0,     0,     0,    0,    0    ], # 14
   [ 0,   1,    1,      1,      1,     1,     0,      0,     0,     0,     0,     0,     3,     0,     0,     0,     0,    0,    0    ], # 15
   [ 0,   1,    1,      2,      1,     1,     0,      0,     0,     0,     0,     0,     3,     0,     0,     0,     0,    0,    0    ], # 16
   [ 0,   1,    1,      3,      1,     1,     0,      0,     0,     0,     0,     0,     3,     0,     0,     0,     0,    0,    0    ], # 17
   [ 1,   0,    0,      0,      0,     0,     0,      0,     0,     0,     0,     0,     1,     0,     0,     0,     0,    0,    0    ], # 18, rx_tolerance modified from 0 to 1! 20181030
   [ 1,   0,    0,      0,      0,     0,     0,      0,     0,     0,     1,     1,     1,     0,     0,     0,     0,    0,    0    ], # 19, rx_tolerance modified from 0 to 1! 20181030
   [ 1,   0,    0,      0,      0,     0,     0,      0,     0,     0,     1,     1,     1,     0,     0,     0,     0,    0,    0    ], # 20
   [ 1,   0,    0,      0,      0,     0,     0,      0,     0,     0,     1,     1,     2,     0,     0,     0,     0,    0,    0    ], # 21
   [ 1,   0,    0,      0,      0,     0,     0,      0,     0,     0,     1,     1,     3,     0,     0,     0,     0,    0,    0    ], # 22
   [ 1,   1,    0,      0,      1,     1,     0,      0,     0,     0,     1,     1,     3,     0,     0,     0,     0,    0,    0    ], # 23
   [ 1,   1,    0,      1,      1,     1,     0,      0,     0,     0,     1,     1,     3,     0,     0,     0,     0,    0,    0    ], # 24
   [ 1,   1,    0,      2,      1,     1,     0,      0,     0,     0,     1,     1,     3,     0,     0,     0,     0,    0,    0    ], # 25
   [ 1,   1,    0,      3,      1,     1,     0,      0,     0,     0,     1,     1,     3,     0,     0,     0,     0,    0,    0    ], # 26
   [ 1,   1,    1,      0,      1,     1,     0,      0,     0,     0,     0,     0,     3,     0,     0,     0,     0,    0,    0    ], # 27
   [ 1,   1,    1,      1,      1,     1,     0,      0,     0,     0,     0,     0,     3,     0,     0,     0,     0,    0,    0    ], # 28
   [ 1,   1,    1,      2,      1,     1,     0,      0,     0,     0,     0,     0,     3,     0,     0,     0,     0,    0,    0    ], # 29
   [ 1,   1,    1,      3,      1,     1,     0,      0,     0,     0,     0,     0,     3,     0,     0,     0,     0,    0,    0    ]  # 30 * 14443 Type B
]    

#----------------------------------------------------------------------------
# Class log_base
#----------------------------------------------------------------------------
class log_base (object):
    def __init__(self, tcfg=[], rcfg=[], log_path='', data_path=''):
        #self.crc_poly              = 0x11021
        self.tcfg                   = tcfg
        self.rcfg                   = rcfg
        self.log_path               = log_path
        self.data_path              = data_path
        self.tc                     = []
        self.rc                     = []
        self.baud_rate              = 0
        self.data_len               = 0
        self.minlevel               = const_minlevel
        self.dpll_dither            = const_dpll_dither
        self.data_gain              = const_data_gain
        self.combine_mod            = const_combine_mod
        self.coll_level             = const_coll_level
        self.det_gen                = const_det_gen
        self.force_rssi_calc        = const_force_rssi_calc
        self.win_size               = const_win_size
        self.new_peak_en            = const_new_peak_en
        self.peak_num               = const_peak_num
        self.peak_shift             = const_peak_shift
        self.adc_format             = const_adc_format
        # other control
        self.sof_sup                = 0 # SOF Supression
        self.eof_sup                = 0 # EOF Supression

    def reg_parse(self):
        # common
        self.crc_poly               = 0x8408
        # Tx
        self.tx_coding              = self.tc[0]
        self.tx_crc_en              = self.tc[1]
        self.tx_crc_invert          = self.tc[2]
        self.tx_crc_preset_val      = self.tc[3]
        self.tx_parity_en           = self.tc[4]
        self.tx_parity_odd          = self.tc[5]
        self.tx_last_bits           = self.tc[6]
        self.tx_no_sof              = self.tc[7]
        self.tx_no_eof              = self.tc[8]
        self.sof_lo_width           = self.tc[9]
        self.sof_hi_width           = self.tc[10]
        self.eof_width              = self.tc[11]
        self.charspacing            = self.tc[12]
        # baud_rate related
        if (self.baud_rate == 0):   self.tx_mod_width = 31 # 28~40.5
        elif (self.baud_rate == 1): self.tx_mod_width = 17 # 16.5~20
        elif (self.baud_rate == 2): self.tx_mod_width = 8  # 8~10
        elif (self.baud_rate == 3): self.tx_mod_width = 4  # 4~5
        # Rx
        self.rx_framing             = self.rc[0]
        self.rx_crc_en              = self.rc[1]
        self.rx_crc_invert          = self.rc[2]
        self.rx_crc_preset_val      = self.rc[3]
        self.rx_parity_en           = self.rc[4]
        self.rx_parity_odd          = self.rc[5]
        self.rx_alian               = self.rc[6]
        self.coll_en                = self.rc[7]
        self.no_coll                = self.rc[8]
        self.value_after_coll       = self.rc[9]
        self.rx_sof_req             = self.rc[10]
        self.rx_eof_req             = self.rc[11]
        self.rx_tolerance           = self.rc[12]
        self.rx_all_data_type_b     = self.rc[13]
        self.ignore_no_sc_det       = self.rc[14]
        self.emd_sup                = self.rc[15]
        self.emd_condition_mask_hi  = self.rc[16]
        self.emd_condition_mask_lo  = self.rc[17]
        self.rx_multiple            = self.rc[18]
        # baud_rate related
        if (self.rx_framing == 0) and (self.baud_rate == 0): # only type a 106kbps, using Manchester, else NRZ-L BPSK
            self.rx_coding = 0
        else:
            self.rx_coding = 1

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
        # 31, rx_coder_ctrl
        reg_addr = 31
        reg_val = self.baud_rate + self.rx_framing*4 + self.rx_coding*8 + self.rx_multiple*16 + self.emd_sup*32
        reg_asm.append([reg_addr, reg_val])
        # 32, rx_crc_ctrl
        reg_addr = 32
        reg_val = self.rx_crc_en + self.rx_crc_invert*2 + self.rx_crc_preset_val*4
        reg_asm.append([reg_addr, reg_val])
        # 33, rx_bit_ctrl
        reg_addr = 33
        reg_val = self.rx_alian + self.no_coll*8 + self.coll_en*16 + self.value_after_coll*32
        reg_asm.append([reg_addr, reg_val])
        # 34, RO, rx_coll
        # 35, rx_type_b_framing
        reg_addr = 35
        reg_val = self.rx_tolerance + self.rx_eof_req*4 + self.rx_sof_req*8 + self.ignore_no_sc_det*16 + self.rx_all_data_type_b*32
        reg_asm.append([reg_addr, reg_val])
        # 36, RO, rx_last_bits
        # 37, emd_condition_mask0
        reg_addr = 37
        reg_val = self.emd_condition_mask_hi
        reg_asm.append([reg_addr, reg_val])
        # 38, emd_condition_mask1
        reg_addr = 38
        reg_val = self.emd_condition_mask_lo
        reg_asm.append([reg_addr, reg_val])
        # 39, RO, emd_status0
        # 40, RO, emd_status1
        # 41, RO, emd_frame_length_hi
        # 42, RO, emd_frame_length_lo
        #***************
        # Demod Related
        #***************
        # 60, demod_ctrl
        reg_addr = 60
        reg_val = self.combine_mod + self.dpll_dither*4 + self.data_gain*16 + self.det_gen*64
        reg_asm.append([reg_addr, reg_val])
        # 61, demod_typea_ctrl
        reg_addr = 61
        reg_val = self.peak_shift + self.peak_num*4 + self.new_peak_en*16
        reg_asm.append([reg_addr, reg_val])
        # 62, min_level_low
        reg_addr = 62
        reg_val = int(self.minlevel%256)
        reg_asm.append([reg_addr, reg_val])
        # 63, min_level_high
        reg_addr = 63
        reg_val = int(self.minlevel/256)
        reg_asm.append([reg_addr, reg_val])
        # 64, coll_level
        reg_addr = 64
        reg_val = self.coll_level
        reg_asm.append([reg_addr, reg_val])
        # 65, rssi_calc_config
        reg_addr = 65
        reg_val = self.win_size
        reg_asm.append([reg_addr, reg_val])
        # 66, rssi_calc_ctrl
        reg_addr = 66
        reg_val = self.force_rssi_calc
        reg_asm.append([reg_addr, reg_val])
        #***************
        # ADC Related
        #***************
        # 83, adc_ctrl
        reg_addr = 83
        reg_val = self.adc_format
        reg_asm.append([reg_addr, reg_val])
        #***************
        # Return
        #***************
        return reg_asm

    def reg_info_gen (self, case_dir):
        with open(case_dir + path_delimiter + fname_reg_info, 'w') as f:
            # Tx
            f.write('---------------Tx\n')
            f.write('baud_rate              0x%02x\n'%self.baud_rate)
            f.write('tx_coding              0x%02x\n'%self.tx_coding)
            f.write('tx_crc_en              0x%02x\n'%self.tx_crc_en)
            f.write('tx_crc_invert          0x%02x\n'%self.tx_crc_invert)
            f.write('tx_crc_preset_val      0x%02x\n'%self.tx_crc_preset_val)
            f.write('tx_parity_en           0x%02x\n'%self.tx_parity_en)
            f.write('tx_parity_odd          0x%02x\n'%self.tx_parity_odd)
            f.write('tx_last_bits           0x%02x\n'%self.tx_last_bits)
            f.write('tx_no_sof              0x%02x\n'%self.tx_no_sof)
            f.write('tx_no_eof              0x%02x\n'%self.tx_no_eof)
            f.write('sof_lo_width           0x%02x\n'%self.sof_lo_width)
            f.write('sof_hi_width           0x%02x\n'%self.sof_hi_width)
            f.write('eof_width              0x%02x\n'%self.eof_width)
            f.write('charspacing            0x%02x\n'%self.charspacing)
            f.write('rx_parity_en           0x%02x\n'%self.rx_parity_en)
            f.write('rx_parity_odd          0x%02x\n'%self.rx_parity_odd)
            f.write('tx_mod_width           0x%02x\n'%self.tx_mod_width)
            # Rx
            f.write('---------------Rx\n')
            f.write('rx_framing             0x%02x\n'%self.rx_framing)
            f.write('rx_coding              0x%02x\n'%self.rx_coding)
            f.write('rx_crc_en              0x%02x\n'%self.rx_crc_en)
            f.write('rx_crc_invert          0x%02x\n'%self.rx_crc_invert)
            f.write('rx_crc_preset_val      0x%02x\n'%self.rx_crc_preset_val)
            f.write('rx_parity_en           0x%02x\n'%self.rx_parity_en)
            f.write('rx_parity_odd          0x%02x\n'%self.rx_parity_odd)
            f.write('rx_alian               0x%02x\n'%self.rx_alian)
            f.write('coll_en                0x%02x\n'%self.coll_en)
            f.write('no_coll                0x%02x\n'%self.no_coll)
            f.write('value_after_coll       0x%02x\n'%self.value_after_coll)
            f.write('rx_sof_req             0x%02x\n'%self.rx_sof_req)
            f.write('rx_eof_req             0x%02x\n'%self.rx_eof_req)
            f.write('rx_tolerance           0x%02x\n'%self.rx_tolerance)
            f.write('rx_all_data_type_b     0x%02x\n'%self.rx_all_data_type_b)
            f.write('ignore_no_sc_det       0x%02x\n'%self.ignore_no_sc_det)
            f.write('emd_sup                0x%02x\n'%self.emd_sup)
            f.write('emd_condition_mask_hi  0x%02x\n'%self.emd_condition_mask_hi)
            f.write('emd_condition_mask_lo  0x%02x\n'%self.emd_condition_mask_lo)
            f.write('rx_multiple            0x%02x\n'%self.rx_multiple)
            # Demod
            f.write('---------------Demod\n')
            f.write('minlevel               0x%02x\n'%self.minlevel)
            f.write('dpll_dither            0x%02x\n'%self.dpll_dither)
            f.write('data_gain              0x%02x\n'%self.data_gain)
            f.write('combine_mod            0x%02x\n'%self.combine_mod)
            f.write('coll_level             0x%02x\n'%self.coll_level)
            f.write('det_gen                0x%02x\n'%self.det_gen)
            f.write('force_rssi_calc        0x%02x\n'%self.force_rssi_calc)
            f.write('win_size               0x%02x\n'%self.win_size)
            f.write('new_peak_en            0x%02x\n'%self.new_peak_en)
            f.write('peak_num               0x%02x\n'%self.peak_num)
            f.write('peak_shift             0x%02x\n'%self.peak_shift)
            # ADC
            f.write('---------------ADC\n')
            f.write('adc_format             0x%02x\n'%self.adc_format)

    def reg_cfg_gen (self, case_dir):
        reg_asm_ret = self.reg_asm()
        with open(case_dir + path_delimiter + fname_reg_cfg, 'w') as f:
            for i in range(len(reg_asm_ret)):
                reg_addr = reg_asm_ret[i][0]
                reg_val = reg_asm_ret[i][1]
                reg_val = hex(reg_val)
                if len(reg_val)<4: # <16
                    reg_val = '0' + reg_val[2]
                else:
                    reg_val = reg_val[2:4]
                f.write("%d %s\n" % (reg_addr, reg_val))

    def case_cfg_gen (self, case_dir, case_type):
        with open(case_dir + path_delimiter + fname_case_cfg, 'w') as f:
            f.write("%02x\n"%case_type)
            f.write("01")   # SPI

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
        #for br in range(4):
        for br in range(1):
            self.baud_rate = br
            case_base = self.baud_rate*100
            for case_idx in range(len(self.tcfg)):
                if case_idx != 27:
                    continue
                self.tc = self.tcfg[case_idx]
                self.rc = self.rcfg[0]
                self.reg_parse()
                for (maindir, subdir, dl) in os.walk(self.data_path):
                    pass
                for i in dl:
                    if i != '4':
                        continue
                    case_dir = log_path + path_delimiter + dname_tx + '%03d%02d'%((case_base + case_idx), int(i))
                    data_file = self.data_path + path_delimiter + i
                    if os.path.exists(case_dir):
                        shutil.rmtree(case_dir)
                    os.mkdir(case_dir)
                    self.case_cfg_gen(case_dir, CASE_TYPE_TRANSMIT)
                    self.reg_cfg_gen(case_dir)
                    self.reg_info_gen(case_dir)
                    self.tx_evlp_gen(case_dir, data_file)
                    shutil.copyfile(data_file, case_dir + path_delimiter + fname_tx_fifo)

    def rx_etu_gen (self, case_dir, data_file):
        data_byte = []
        with open (data_file, 'r') as f:
            for i in f:
                data_byte.append(i.strip())
        data_byte = self.crc_proc(data_byte, self.rx_crc_en, self.rx_crc_invert, self.rx_crc_preset_val)
        # print debug info: tx_crc
        with open (case_dir + path_delimiter + fname_rx_crc, 'w') as f:
            if self.rx_crc_en == 1:
                f.write(data_byte[-2]+'\n')
                f.write(data_byte[-1]+'\n')
            else:
                f.write('\n')
        etus = ''
        self.data_len = 0 # for BER
        #print('case_dir: %s'%case_dir)
        #print('data_byte: ')
        #print(data_byte)
        #print('rx_coding=%d'%self.rx_coding)
        #print('rx_framing=%d'%self.rx_framing)
        # Type A
        if self.rx_framing == 0: 
            # no_subcarrier
            for i in range(10):
                etus = etus + '2\n'
            # sof
            if self.baud_rate == 0: # 106kbps, sequence D
                etus = etus + '1\n'
            else: # higher rate, burst of 32 subcarrier cycles logic '1' followed by logic '0'
                for i in range(32):
                    etus = etus + '1\n'
                etus = etus + '0\n'
            # data_byte
            for byt_idx in range(len(data_byte)):
                # data
                byt = int(data_byte[byt_idx], 16)
                prt = 0
                if byt_idx == 0: # first byte
                    for bit_idx in range(8-self.rx_alian):
                        etu = (byt>>(self.rx_alian+bit_idx))&1
                        etus = etus + '%0d\n'%(etu)
                        self.data_len = self.data_len + 1
                        prt = prt ^ etu
                else:
                    for bit_idx in range(8):
                        etu = (byt>>bit_idx)&1
                        etus = etus + '%0d\n'%(etu)
                        self.data_len = self.data_len + 1
                        prt = prt ^ etu
                # parity
                if self.rx_parity_en == 1:
                    prt = prt ^ self.rx_parity_odd
                    etu = prt
                    etus = etus + '%0d\n'%(etu)
                    self.data_len = self.data_len + 1
            # eof, no subscarrier for 1 etus
            for i in range(10):
                etus = etus + '2\n'
        # Type B
        else:
            # TR0, no subscarrier for 1280
            for i in range(10*(2**self.baud_rate)):
                etus = etus + '2\n'
            # TR1, logic '1' for 2560
            for i in range(20*(2**self.baud_rate)):
                etus = etus + '1\n'
            # SOF_LO, 10*eut, only 106kbps can apply sof supression
            if self.sof_sup == 1 and self.rx_sof_req == 0 and self.baud_rate == 0:
                pass
            else:
                for i in range(10):
                    etus = etus + '0\n'
            # SOF_HI, 2*etu
            if self.sof_sup == 1 and self.rx_sof_req == 0 and self.baud_rate == 0:
                pass
            else:
                for i in range(2):
                    etus = etus + '1\n'
            # Databyte
            for byt_idx in range(len(data_byte)):
                byt = int(data_byte[byt_idx], 16)
                # Start, logic '0'
                etus = etus + '0\n'
                self.data_len = self.data_len + 1
                # Data
                for bit_idx in range(8):
                    etu = byt & 1
                    byt = byt >> 1
                    etus = etus + '%0d\n'%(etu)
                    self.data_len = self.data_len + 1
                # Stop
                etus = etus + '1\n'
                self.data_len = self.data_len + 1
                # EGT
            # EOF_LO, 10*etu
            if self.eof_sup == 1 and self.rx_sof_req == 0 and self.baud_rate == 0:
                pass
            else:
                for i in range(10):
                    etus = etus + '0\n'
            etus = etus + '1\n'
            # no subscarrier
            for i in range(10):
                etus = etus + '2\n'
        # Finally, writefile
        with open (case_dir + path_delimiter + fname_rx_etu, 'w') as f:
            f.write(etus)
        # print etu_cfg
        with open(case_dir + path_delimiter + fname_etu_cfg,  'w') as f:
            f.write('0.003\n')                      # line  1: sensitivity
            f.write('%0d\n'%self.baud_rate)         # line  2: rate_sel
            f.write('%0d\n'%self.rx_coding)         # line  3: bpsk_en
            f.write('%0d\n'%self.rx_framing)        # line  4: type_b
            f.write('%0d\n'%self.coll_en)           # line  5: anticoll_en
            f.write('%0d\n'%self.minlevel)          # line  6: minlevel
            f.write('%0d\n'%self.dpll_dither)       # line  7: dpll_dither
            f.write('%0d\n'%self.data_gain)         # line  8: data_gain
            f.write('%0d\n'%self.combine_mod)       # line  9: combine_mod
            f.write('%0d\n'%self.coll_level)        # line 10: coll_level
            f.write('%0d\n'%self.det_gen)           # line 11: det_gen
            f.write('%0d\n'%self.force_rssi_calc)   # line 12: force_rssi_calc
            f.write('%0d\n'%self.win_size)          # line 13: win_size
            f.write('%0d\n'%self.new_peak_en)       # line 14: new_peak_en
            f.write('%0d\n'%self.peak_num)          # line 15: peak_num
            f.write('%0d\n'%self.peak_shift)        # line 16: peak_shift
            f.write('%0d\n'%self.data_len)          # line 17: data_len

    def rx_log_gen (self):        
        for br in range(4):
        #for br in range(1):
            self.baud_rate = br
            case_base = self.baud_rate*100
            for case_idx in range(len(self.rcfg)):
            #for case_idx in range(1):
            #for j in range(2):
            #    if j == 0:
            #        case_idx = 0
            #    else:
            #        case_idx = 18
                self.tc = self.tcfg[0]
                self.rc = self.rcfg[case_idx]
                self.reg_parse()
                for (maindir, subdir, dl) in os.walk(self.data_path):
                    pass
                for df in dl:
                    # long frame generate a little!
                    if df == '9':
                        if case_idx >= 0 and case_idx <= 15:
                            continue
                        elif case_idx >= 18 and case_idx <= 28:
                            continue
                    data_file = self.data_path + path_delimiter + df
                    case_dir = self.log_path + path_delimiter + dname_rx + '%03d%02d'%((case_base + case_idx), int(df))
                    if os.path.exists(case_dir):
                        shutil.rmtree(case_dir)
                    os.mkdir(case_dir)
                    self.case_cfg_gen(case_dir, CASE_TYPE_RECEIVE)
                    self.reg_cfg_gen(case_dir)
                    self.reg_info_gen(case_dir)
                    self.rx_etu_gen(case_dir, data_file)
                    shutil.copyfile(data_file, case_dir + path_delimiter + fname_rx_fifo)

def main():
    # Log Instance
    log_inst = log_base()
    log_inst.log_path  = log_path
    log_inst.data_path = data_path
    log_inst.tcfg = tx_cfg
    log_inst.rcfg = rx_cfg

    # rx_test
    log_inst.log_dir_clear()
    #log_inst.tx_log_gen()
    log_inst.rx_log_gen()

# main
if __name__ == '__main__':
    main()

