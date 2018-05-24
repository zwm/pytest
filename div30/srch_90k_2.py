#20180405
module_name="ul_srch_90k"
file_name = module_name+".v"

with open (file_name, "w") as fp:
    fp.write("// Author: Wbird\n")
    fp.write("// Time  : 201804051453\n")
    fp.write("module %s (\n"%module_name)
    fp.write("    input      [ 1:0] scs,\n")
    fp.write("    input      [ 7:0] re_index,\n")
    fp.write("    output reg [ 3:0] seg_90k\n")
    fp.write(");\n")
    fp.write("\n")

#scs30, gap3
scs=30
num=30
num_root=5
gap=3
with open (file_name, "a") as fp:
    fp.write("// scs%0d, gap%0d\n"%(scs, gap))
    fp.write("reg [3:0] scs%0d_90k_seg;\n"%(scs))
    fp.write("always @(*) begin\n")
    fp.write("    case (re_index[%0d:%0d])\n"%((num_root-1), (num_root-1-2)))
    for i in range (8):
        fp.write("        3'd%0d:\n"%(i))
        var_base = i*(2**(num_root-3))
        var_mod = var_base%gap
        var_div = var_base/gap
        var_seg = gap - var_mod
        fp.write("            if (re_index[%0d:0] < %0d)\n"%((num_root-1-2-1), var_seg))
        fp.write("                scs%0d_90k_seg = %0d;\n"%(scs, var_div))
        fp.write("            else\n")
        fp.write("                scs%0d_90k_seg = %0d;\n"%(scs, (var_div+1)))
    fp.write("    endcase\n")
    fp.write("end\n")
#scs15, gap6
scs=15
num=60
num_root=6
gap=6
with open (file_name, "a") as fp:
    fp.write("// scs%0d, gap%0d\n"%(scs, gap))
    fp.write("reg [3:0] scs%0d_90k_seg;\n"%(scs))
    fp.write("always @(*) begin\n")
    fp.write("    case (re_index[%0d:%0d])\n"%((num_root-1), (num_root-1-2)))
    for i in range (8):
        fp.write("        3'd%0d:\n"%(i))
        var_base = i*(2**(num_root-3))
        var_mod = var_base%gap
        var_div = var_base/gap
        var_seg = gap - var_mod
        fp.write("            if (re_index[%0d:0] < %0d)\n"%((num_root-1-2-1), var_seg))
        fp.write("                scs%0d_90k_seg = %0d;\n"%(scs, var_div))
        fp.write("            else\n")
        fp.write("                scs%0d_90k_seg = %0d;\n"%(scs, (var_div+1)))
    fp.write("    endcase\n")
    fp.write("end\n")
#scs5, gap18
scs=5
num=180
num_root=8
gap=18
with open (file_name, "a") as fp:
    fp.write("// scs%0d, gap%0d\n"%(scs, gap))
    fp.write("reg [3:0] scs%0d_90k_seg;\n"%(scs))
    fp.write("always @(*) begin\n")
    fp.write("    case (re_index[%0d:%0d])\n"%((num_root-1), (num_root-1-2)))
    for i in range (8):
        fp.write("        3'd%0d:\n"%(i))
        var_base = i*(2**(num_root-3))
        var_mod = var_base%gap
        var_div = var_base/gap
        var_seg = gap - var_mod
        fp.write("            if (re_index[%0d:0] < %0d)\n"%((num_root-1-2-1), var_seg))
        fp.write("                scs%0d_90k_seg = %0d;\n"%(scs, var_div))
        fp.write("            else\n")
        fp.write("                scs%0d_90k_seg = %0d;\n"%(scs, (var_div+1)))
    fp.write("    endcase\n")
    fp.write("end\n")





with open (file_name, "a") as fp:
    fp.write("\n")
    fp.write("// output\n")
    fp.write("always @(*) begin\n")
    fp.write("    case (scs) begin\n")
    fp.write("        2'd0:\n")
    fp.write("            seg_90k = 0;\n")
    fp.write("        2'd1:\n")
    fp.write("            seg_90k = scs5_90k_seg;\n")
    fp.write("        2'd2:\n")
    fp.write("            seg_90k = scs15_90k_seg;\n")
    fp.write("        2'd3:\n")
    fp.write("            seg_90k = scs30_90k_seg;\n")
    fp.write("    endcase\n")
    fp.write("end\n")

with open (file_name, "a") as fp:
    fp.write("\n")
    fp.write("endmodule\n")
