#20180405
module_name="srch_900k"
file_name = module_name+".v"

with open (file_name, "w") as fp:
    fp.write("// Author: Wbird\n")
    fp.write("// Time  : 201804051207\n")
    fp.write("module %s (\n"%module_name)
    fp.write("    input      [ 1:0] scs,\n")
    fp.write("    input      [11:0] re_index,\n")
    fp.write("    output reg [ 7:0] seg_900k,\n")
    fp.write("    output reg [ 7:0] mod_900k\n")
    fp.write(");\n")
    fp.write("\n")

#scs30, seg128
scs=30
seg=128
seg_root=7
gap=30
with open (file_name, "a") as fp:
    fp.write("// scs%0d, seg%0d\n"%(scs, seg))
    fp.write("reg [%0d:0] scs%0d_900k_seg;\n"%((seg_root-1), scs))
    fp.write("reg [%0d:0] scs%0d_900k_mod;\n"%((12-seg_root-1), scs))
    fp.write("always @(*) begin\n")
    fp.write("    case (re_index[11:%0d])\n"%(11-seg_root+1))
    for i in range (seg):
        fp.write("        %0d'd%0d:\n"%(seg_root, i))
        var_base = i*4096/seg
        var_mod = var_base%gap
        var_div = var_base/gap
        var_seg = gap - var_mod
        fp.write("            if (re_index[%0d:0] < %0d) begin\n"%((12-seg_root-1), var_seg))
        fp.write("                scs%0d_900k_seg = %0d;\n"%(scs, var_div))
        fp.write("                scs%0d_900k_mod = re_index[%0d:0] + %0d;\n"%(scs, (12-seg_root-1), (gap-var_seg)))
        fp.write("            end\n")
        fp.write("            else begin\n")
        fp.write("                scs%0d_900k_seg = %0d;\n"%(scs, (var_div+1)))
        fp.write("                scs%0d_900k_mod = re_index[%0d:0] - %0d;\n"%(scs, (12-seg_root-1), var_seg))
        fp.write("            end\n")
    fp.write("    endcase\n")
    fp.write("end\n")
#scs15, seg64
scs=15
seg=64
seg_root=6
gap=60
with open (file_name, "a") as fp:
    fp.write("// scs%0d, seg%0d\n"%(scs, seg))
    fp.write("reg [%0d:0] scs%0d_900k_seg;\n"%((seg_root-1), scs))
    fp.write("reg [%0d:0] scs%0d_900k_mod;\n"%((12-seg_root-1), scs))
    fp.write("always @(*) begin\n")
    fp.write("    case (re_index[11:%0d])\n"%(11-seg_root+1))
    for i in range (seg):
        fp.write("        %0d'd%0d:\n"%(seg_root, i))
        var_base = i*4096/seg
        var_mod = var_base%gap
        var_div = var_base/gap
        var_seg = gap - var_mod
        fp.write("            if (re_index[%0d:0] < %0d) begin\n"%((12-seg_root-1), var_seg))
        fp.write("                scs%0d_900k_seg = %0d;\n"%(scs, var_div))
        fp.write("                scs%0d_900k_mod = re_index[%0d:0] + %0d;\n"%(scs, (12-seg_root-1), (gap-var_seg)))
        fp.write("            end\n")
        fp.write("            else begin\n")
        fp.write("                scs%0d_900k_seg = %0d;\n"%(scs, (var_div+1)))
        fp.write("                scs%0d_900k_mod = re_index[%0d:0] - %0d;\n"%(scs, (12-seg_root-1), var_seg))
        fp.write("            end\n")
    fp.write("    endcase\n")
    fp.write("end\n")
#scs5, seg16
scs=5
seg=16
seg_root=4
gap=180
with open (file_name, "a") as fp:
    fp.write("// scs%0d, seg%0d\n"%(scs, seg))
    fp.write("reg [%0d:0] scs%0d_900k_seg;\n"%((seg_root-1), scs))
    fp.write("reg [%0d:0] scs%0d_900k_mod;\n"%((12-seg_root-1), scs))
    fp.write("always @(*) begin\n")
    fp.write("    case (re_index[11:%0d])\n"%(11-seg_root+1))
    for i in range (seg):
        fp.write("        %0d'd%0d:\n"%(seg_root, i))
        var_base = i*4096/seg
        var_mod = var_base%gap
        var_div = var_base/gap
        var_seg = gap - var_mod
        fp.write("            if (re_index[%0d:0] < %0d) begin\n"%((12-seg_root-1), var_seg))
        fp.write("                scs%0d_900k_seg = %0d;\n"%(scs, var_div))
        fp.write("                scs%0d_900k_mod = re_index[%0d:0] + %0d;\n"%(scs, (12-seg_root-1), (gap-var_seg)))
        fp.write("            end\n")
        fp.write("            else begin\n")
        fp.write("                scs%0d_900k_seg = %0d;\n"%(scs, (var_div+1)))
        fp.write("                scs%0d_900k_mod = re_index[%0d:0] - %0d;\n"%(scs, (12-seg_root-1), var_seg))
        fp.write("            end\n")
    fp.write("    endcase\n")
    fp.write("end\n")

with open (file_name, "a") as fp:
    fp.write("\n")
    fp.write("// output\n")
    fp.write("always @(*) begin\n")
    fp.write("    case (scs) begin\n")
    fp.write("        2'd0: begin\n")
    fp.write("            seg_900k = 0;\n")
    fp.write("            mod_900k = 0;\n")
    fp.write("        end\n")
    fp.write("        2'd1: begin\n")
    fp.write("            seg_900k = {4'd0, scs5_900k_seg};\n")
    fp.write("            mod_900k = scs5_900k_mod;\n")
    fp.write("        end\n")
    fp.write("        2'd2: begin\n")
    fp.write("            seg_900k = {2'd0, scs15_900k_seg};\n")
    fp.write("            mod_900k = {2'd0, scs15_900k_mod};\n")
    fp.write("        end\n")
    fp.write("        2'd3: begin\n")
    fp.write("            seg_900k = {1'd0, scs30_900k_seg};\n")
    fp.write("            mod_900k = {3'd0, scs30_900k_mod};\n")
    fp.write("        end\n")
    fp.write("    endcase\n")
    fp.write("end\n")

with open (file_name, "a") as fp:
    fp.write("\n")
    fp.write("endmodule\n")
