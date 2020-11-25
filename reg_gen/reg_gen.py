import os
import re
import xlrd

f_excel         = 'E:\svn\prj_share_sec\YC3122\Architecture\YC3122_Reg.xls'
f_vlog          = 'adc_reg.v'

module_name     = 'adc_reg'

row_start       = 1223
row_stop        = 1258
column_num      = 7

reg_addr        = 1
reg_name        = 2
field_width     = 3
field_name      = 4
field_access    = 5         # support RW/RO/WO/RW1C
field_default   = 6

reg_addr_base   = 0xfbb00

fp_exl = xlrd.open_workbook(f_excel)

sheet_num = len(fp_exl.sheets())
sheets = fp_exl.sheets()
print(sheets)
for i in range(sheet_num):
    sheet_name = sheets[i].name
    print('Index: %d, Name: %s' % (i, sheet_name))

table = fp_exl.sheet_by_index(0)

def reg_addr_proc (raw):
    if raw != "":
        if isinstance(raw, int):
            print('addr, int, %d'%raw)
            raw_int = int(raw)
            raw_str = str(raw_int)
            raw_hex = int(raw_str, 16)
        elif isinstance(raw, float):
            print('addr, float, %f'%raw)
            raw_int = int(raw)
            raw_str = str(raw_int)
            raw_hex = int(raw_str, 16)
        elif isinstance(raw, str):
            print('addr, string, %s'%raw)
            raw_str = raw
            raw_hex = int(raw_str, 16)
        else:
            print("Error type of reg_addr")
            print("    reg_addr")
            print(raw)
        # remove base
        raw_hex = raw_hex - reg_addr_base
        #raw_hex = hex(raw_hex)
    else:
        raw_hex = ""
    return raw_hex

def reg_field_width_proc (raw):
    if raw != "":
        if isinstance(raw, float):
            print('field, float, %f'%raw)
            raw = (int(raw),)
        elif isinstance(raw, str):
            print('field, string, %s'%raw)
            if raw[0] == '[':
                raw = raw[1:]
            if raw[-1] == ']':
                raw = raw[0:-1]
            if ':' in raw:
                raw = raw.split(':')
                raw = (int(raw[0]), int(raw[1]))
            else:
                raw = (int(raw),)
        else:
            print("Error type of reg_field_width")
            print("    reg_field_width")
            print(raw)
    else:
        raw = ""
    return raw

def reg_field_default_proc (raw):
    if raw != "":
        if isinstance(raw, float):
            raw = int(raw)
            raw = str(raw)
            raw = int(raw, 16)
        elif isinstance(raw, str):
            if raw != '-':
                raw = int(raw, 16)
            else:
                pass
        else:
            print("Error type of reg_field_default")
            print("    reg_field_default")
            print(raw)
    else:
        raw = ""
    return raw

#############################################################################
# get sheet
#############################################################################
sheet = table

# re
#############################################################################
# generate reg array database
#############################################################################
# data struct
# [[addr, reg_name,
#                   [[field1, field1_name, field1_access],
#                    [field2, field2_name, field2_access],
#                    ... ...
#                    [field9, field9_name, field9_access]]], 
# 
nrows = sheet.nrows

# init
rdb = []
reg_flag = 0
reg_item = []
reg_field = []
# proc
for i in range(nrows):
    if i < (row_start-1):
        continue
    elif i >= row_stop:
        # store
        if reg_flag:
            reg_item.append(reg_field)
            rdb.append(reg_item)
            reg_flag = 0
        # exit
        break
    else:
        # get row
        row_list = []
        for j in range(column_num): # need update, using function!!!
            row_list.append(sheet.cell_value(i, j)) # add more, remove begin/end space!!!
        row_list[reg_addr] = reg_addr_proc(row_list[reg_addr])
        row_list[field_width] = reg_field_width_proc(row_list[field_width])
        row_list[field_default] = reg_field_default_proc(row_list[field_default])
        # analysis row
        if reg_flag:
            # field process
            if row_list[reg_addr] == "": # 
                if row_list[field_name] == "" and row_list[field_width] == "" and row_list[field_access] == "": # blank line
                    reg_item.append(reg_field)
                    rdb.append(reg_item)
                    reg_flag = 0
                    reg_item = []
                    reg_field = []
                    print('Escape blank line: %d'%(i+1))
                elif (row_list[field_name] == "-") or (row_list[field_name] == "reserved") or (row_list[field_name] == ""):
                    pass
                    #reg_item.append(reg_field)
                    #rdb.append(reg_item)
                    #reg_flag = 0
                    #reg_item = []
                    #reg_field = []
                else:
                    reg_field.append((row_list[field_width], row_list[field_name], row_list[field_access], row_list[field_default])) 
            # reg process
            else:
                # store last reg
                reg_item.append(reg_field)
                rdb.append(reg_item)
                # load new reg
                reg_item = []
                reg_field = []
                reg_item.append(row_list[reg_addr])
                reg_item.append(row_list[reg_name])
                if (row_list[field_name] == "-") or (row_list[field_name] == "reserved") or (row_list[field_name] == ""):
                    pass
                else:
                    reg_field.append((row_list[field_width], row_list[field_name], row_list[field_access], row_list[field_default])) 
                reg_flag = 1
        else:
            if row_list[reg_addr] != "": # 
                reg_item.append(row_list[reg_addr])
                reg_item.append(row_list[reg_name])
                if (row_list[field_name] == "-") or (row_list[field_name] == "reserved") or (row_list[field_name] == ""):
                    pass
                else:
                    reg_field.append((row_list[field_width], row_list[field_name], row_list[field_access], row_list[field_default])) 
                reg_flag = 1

print('----------------------------------------------')
for i in rdb:
    print(i)
    print('\n')
print('----------------------------------------------')


#############################################################################
# generate header
#############################################################################
fl = ''
fl = fl + '\n'
fl = fl + 'module ' + module_name + ' {\n'
fl = fl + '    // bus\n'
fl = fl + '    input bus_rd,\n'
fl = fl + '    input bus_wr,\n'
fl = fl + '    input [3:0] bus_bsel,\n'
fl = fl + '    input [5:0] bus_addr,\n'
fl = fl + '    input [31:0] bus_wdata,\n'
fl = fl + '    output reg [31:0] bus_rdata,\n'
fl = fl + '    // reg\n'
#############################################################################
# generate port
#############################################################################
for r in rdb:
    for f in r[2]:
        port_name = f[1]
        if len(f[0]) == 1:
            port_width = 1
        else:
            port_width = f[0][0] - f[0][1] + 1
        port_dir = f[2]
        # gen port
        if (port_dir == 'RW') or (port_dir == 'WO'):
            if port_width == 1:
                fl = fl + '    output reg %s'%port_name
            else:
                fl = fl + '    output reg [%0d:0] %s'%(port_width-1, port_name)
        elif port_dir == 'RO':
            if port_width == 1:
                fl = fl + '    input %s'%port_name
            else:
                fl = fl + '    input [%0d:0] %s'%(port_width-1, port_name)
        elif port_dir == 'RW1C':
            if port_width == 1:
                fl = fl + '    input %s,\n'%port_name
                fl = fl + '    output %s_clr'%port_name
            else:
                fl = fl + '    input [%0d:0] %s,\n'%(port_width-1, port_name)
                fl = fl + '    output [%0d:0] %s_clr'%(port_width-1, port_name)
        # last check
        if f == r[2][-1] and r == rdb[-1]:
            fl = fl + '\n'
        else:
            fl = fl + ',\n'
# port end
fl = fl + ');\n'
#############################################################################
# generate reg write
#############################################################################
for r in rdb:
    # init
    w_flag = 0
    w1c_flag = 0
    reg_addr = r[0]
    reg_name = r[1]
    fl = fl + '// reg_offset: %x, reg_name: %s\n'%(reg_addr, reg_name)
    for f in r[2]:
        field_name = f[1]
        field_dir = f[2]
        if field_dir == 'RW' or field_dir == 'WO':
            w_flag = 1
        elif field_dir == 'RW1C':
            w1c_flag = 1
    # generate write
    if w_flag:
        # head
        fl = fl + 'always @(posedge clk or negedge rstn)\n'
        # rstn
        fl = fl + '    if (~rstn) begin\n'
        for f in r[2]:
            if len(f[0]) == 1:
                field_width = 1
            else:
                field_width = f[0][0] - f[0][1] + 1
            field_name = f[1]
            field_dir = f[2]
            field_default = f[3]
            if field_dir == 'RW' or field_dir == 'WO':
                fl = fl + '        %s <= %d\'h%s;\n'%(field_name, field_width, hex(field_default)[2:])
        fl = fl + '    end\n'
        # write
        fl = fl + '    else if (bus_sel && bus_wr && bus_addr == %d) begin\n'%(int(reg_addr/4))
        for b in range(4):
            seg_vld = 0
            index_max = (4-b)*8-1
            index_min = (3-b)*8
            # RW/WO seg process
            for f in r[2]:
                if len(f[0]) == 1:
                    field_single = 1
                    field_start = f[0][0]
                else:
                    field_single = 0
                    field_start = f[0][0]
                    field_stop  = f[0][1]
                field_name = f[1]
                field_dir = f[2]
                if field_dir == 'RW' or field_dir == 'WO':
                    # single
                    if field_single:
                        if (field_start >= index_min) and (field_start <= index_max):
                            if seg_vld:
                                fl = fl + '            %s <= bus_wdata[%d];\n'%(field_name, field_start)
                            else:
                                seg_vld = 1
                                fl = fl + '        if (bus_bsel[%d]) begin\n'%(3-b)
                                fl = fl + '            %s <= bus_wdata[%d];\n'%(field_name, field_start)
                    # non-single
                    else:
                        # involved in seg
                        if (field_start <= index_max) and (field_stop >= index_min):
                            if seg_vld:
                                fl = fl + '            %s[%d:0] <= bus_wdata[%d:%d];\n'%(field_name, field_start-field_stop, field_start, field_stop)
                            else:
                                seg_vld = 1
                                fl = fl + '        if (bus_bsel[%d]) begin\n'%(3-b)
                                fl = fl + '            %s[%d:0] <= bus_wdata[%d:%d];\n'%(field_name, field_start-field_stop, field_start, field_stop)
                        # involved outer seg
                        elif (field_start > index_max) and (field_stop < index_min):
                            if seg_vld:
                                fl = fl + '            %s[%d:%d] <= bus_wdata[%d:%d];\n'%(field_name, index_max-field_stop, index_min-field_stop, index_max, index_min)
                            else:
                                seg_vld = 1
                                fl = fl + '        if (bus_bsel[%d]) begin\n'%(3-b)
                                fl = fl + '            %s[%d:%d] <= bus_wdata[%d:%d];\n'%(field_name, index_max-field_stop, index_min-field_stop, index_max, index_min)
                        # high cross seg
                        elif (field_start <= index_max) and (field_start > index_min) and (field_stop < index_min):
                            if seg_vld:
                                fl = fl + '            %s[%d:%d] <= bus_wdata[%d:%d];\n'%(field_name, field_start-field_stop, index_min-field_stop, field_start, index_min)
                            else:
                                seg_vld = 1
                                fl = fl + '        if (bus_bsel[%d]) begin\n'%(3-b)
                                fl = fl + '            %s[%d:%d] <= bus_wdata[%d:%d];\n'%(field_name, field_start-field_stop, index_min-field_stop, field_start, index_min)
                        # low cross seg
                        elif (field_start > index_max) and (field_stop >= index_min) and (field_stop < index_max):
                            if seg_vld:
                                fl = fl + '            %s[%d:0] <= bus_wdata[%d:%d];\n'%(field_name, index_max-field_stop, index_max, field_stop)
                            else:
                                seg_vld = 1
                                fl = fl + '        if (bus_bsel[%d]) begin\n'%(3-b)
                                fl = fl + '            %s[%d:0] <= bus_wdata[%d:%d];\n'%(field_name, index_max-field_stop, index_max, field_stop)
                # write finish
            # RW/WO seg end
            if seg_vld:
                fl = fl + '        end\n'
        # end
        fl = fl + '    end\n'
        # RW1C seg process
        for b in range(1):
            clr_flag = 0
            for f in r[2]:
                if len(f[0]) == 1:
                    field_single = 1
                    field_start = f[0][0]
                else:
                    field_single = 0
                    field_start = f[0][0]
                    field_stop  = f[0][1]
                field_name = f[1]
                field_dir = f[2]
                if field_dir == 'RW1C':
                    if field_single:
                        if clr_flag == 0:
                            fl = fl + '// clr\n'
                            clr_flag = 1
                        fl = fl + 'assign %s_clr = bus_sel && bus_wr && bus_addr == %d && bus_bsel[%d] && bus_wdata[%d];\n'%(field_name, int(reg_addr/4), int(field_start/8), field_start)
                    else:
                        if clr_flag == 0:
                            fl = fl + '// clr\n'
                            clr_flag = 1
                        w = field_start-field_stop + 1
                        for i1 in range(w):
                            tmp = field_start - i1
                            fl = fl + 'assign %s_clr[%d] = bus_sel && bus_wr && bus_addr == %d && bus_bsel[%d] && bus_wdata[%d];\n'%(field_name, w-1-i1, int(reg_addr/4), int(tmp/8), tmp)
            # RW1C seg end
#############################################################################
# generate reg read
#############################################################################
fl = fl + '// bus_rdata\n'
fl = fl + 'always @(*) begin\n'
fl = fl + '    // default\n'
fl = fl + '    bus_rdata = 0\n'
fl = fl + '    // rdata_mux\n'
fl = fl + '    case(bus_addr)\n'
# bus_rdata mux
for r in rdb:
    reg_addr = r[0]
    fl = fl + '        %d: begin\n'%(int(reg_addr/4))
    for f in r[2]:
        field_name = f[1]
        field_dir = f[2]
        if len(f[0]) == 1:
            field_single = 1
            field_start = f[0][0]
        else:
            field_single = 0
            field_start = f[0][0]
            field_stop  = f[0][1]
        if field_dir == 'RW' or field_dir == 'RO' or field_dir == 'RW1C':
            if field_single:
                fl = fl + '            bus_rdata[%d] = %s;\n'%(field_start, field_name)
            else:
                fl = fl + '            bus_rdata[%d:%d] = %s[%d:0];\n'%(field_start, field_stop, field_name, (field_start-field_stop))
        elif field_dir == 'WO':
            pass
    fl = fl + '        end\n'
# endcase
fl = fl + '        default: bus_rdata = 0;\n'
fl = fl + '    endcase\n'
fl = fl + 'end\n'

#############################################################################
# generate tail
#############################################################################
fl = fl + '\n'
fl = fl + 'endmodule\n'
fl = fl + '\n'

# debug
print(fl)

#############################################################################
# generate verilog module
#############################################################################
with open(f_vlog, 'w') as f:
    for line in fl:
        f.write(line)

