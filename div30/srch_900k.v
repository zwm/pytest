// Author: Wbird
// Time  : 201804051207
module srch_900k (
    input      [ 1:0] scs,
    input      [11:0] re_index,
    output reg [ 7:0] seg_900k,
    output reg [ 7:0] mod_900k
);

// scs30, seg128
reg [6:0] scs30_900k_seg;
reg [4:0] scs30_900k_mod;
always @(*) begin
    case (re_index[11:5])
        7'd0:
            if (re_index[4:0] < 30) begin
                scs30_900k_seg = 0;
                scs30_900k_mod = re_index[4:0] + 0;
            end
            else begin
                scs30_900k_seg = 1;
                scs30_900k_mod = re_index[4:0] - 30;
            end
        7'd1:
            if (re_index[4:0] < 28) begin
                scs30_900k_seg = 1;
                scs30_900k_mod = re_index[4:0] + 2;
            end
            else begin
                scs30_900k_seg = 2;
                scs30_900k_mod = re_index[4:0] - 28;
            end
        7'd2:
            if (re_index[4:0] < 26) begin
                scs30_900k_seg = 2;
                scs30_900k_mod = re_index[4:0] + 4;
            end
            else begin
                scs30_900k_seg = 3;
                scs30_900k_mod = re_index[4:0] - 26;
            end
        7'd3:
            if (re_index[4:0] < 24) begin
                scs30_900k_seg = 3;
                scs30_900k_mod = re_index[4:0] + 6;
            end
            else begin
                scs30_900k_seg = 4;
                scs30_900k_mod = re_index[4:0] - 24;
            end
        7'd4:
            if (re_index[4:0] < 22) begin
                scs30_900k_seg = 4;
                scs30_900k_mod = re_index[4:0] + 8;
            end
            else begin
                scs30_900k_seg = 5;
                scs30_900k_mod = re_index[4:0] - 22;
            end
        7'd5:
            if (re_index[4:0] < 20) begin
                scs30_900k_seg = 5;
                scs30_900k_mod = re_index[4:0] + 10;
            end
            else begin
                scs30_900k_seg = 6;
                scs30_900k_mod = re_index[4:0] - 20;
            end
        7'd6:
            if (re_index[4:0] < 18) begin
                scs30_900k_seg = 6;
                scs30_900k_mod = re_index[4:0] + 12;
            end
            else begin
                scs30_900k_seg = 7;
                scs30_900k_mod = re_index[4:0] - 18;
            end
        7'd7:
            if (re_index[4:0] < 16) begin
                scs30_900k_seg = 7;
                scs30_900k_mod = re_index[4:0] + 14;
            end
            else begin
                scs30_900k_seg = 8;
                scs30_900k_mod = re_index[4:0] - 16;
            end
        7'd8:
            if (re_index[4:0] < 14) begin
                scs30_900k_seg = 8;
                scs30_900k_mod = re_index[4:0] + 16;
            end
            else begin
                scs30_900k_seg = 9;
                scs30_900k_mod = re_index[4:0] - 14;
            end
        7'd9:
            if (re_index[4:0] < 12) begin
                scs30_900k_seg = 9;
                scs30_900k_mod = re_index[4:0] + 18;
            end
            else begin
                scs30_900k_seg = 10;
                scs30_900k_mod = re_index[4:0] - 12;
            end
        7'd10:
            if (re_index[4:0] < 10) begin
                scs30_900k_seg = 10;
                scs30_900k_mod = re_index[4:0] + 20;
            end
            else begin
                scs30_900k_seg = 11;
                scs30_900k_mod = re_index[4:0] - 10;
            end
        7'd11:
            if (re_index[4:0] < 8) begin
                scs30_900k_seg = 11;
                scs30_900k_mod = re_index[4:0] + 22;
            end
            else begin
                scs30_900k_seg = 12;
                scs30_900k_mod = re_index[4:0] - 8;
            end
        7'd12:
            if (re_index[4:0] < 6) begin
                scs30_900k_seg = 12;
                scs30_900k_mod = re_index[4:0] + 24;
            end
            else begin
                scs30_900k_seg = 13;
                scs30_900k_mod = re_index[4:0] - 6;
            end
        7'd13:
            if (re_index[4:0] < 4) begin
                scs30_900k_seg = 13;
                scs30_900k_mod = re_index[4:0] + 26;
            end
            else begin
                scs30_900k_seg = 14;
                scs30_900k_mod = re_index[4:0] - 4;
            end
        7'd14:
            if (re_index[4:0] < 2) begin
                scs30_900k_seg = 14;
                scs30_900k_mod = re_index[4:0] + 28;
            end
            else begin
                scs30_900k_seg = 15;
                scs30_900k_mod = re_index[4:0] - 2;
            end
        7'd15:
            if (re_index[4:0] < 30) begin
                scs30_900k_seg = 16;
                scs30_900k_mod = re_index[4:0] + 0;
            end
            else begin
                scs30_900k_seg = 17;
                scs30_900k_mod = re_index[4:0] - 30;
            end
        7'd16:
            if (re_index[4:0] < 28) begin
                scs30_900k_seg = 17;
                scs30_900k_mod = re_index[4:0] + 2;
            end
            else begin
                scs30_900k_seg = 18;
                scs30_900k_mod = re_index[4:0] - 28;
            end
        7'd17:
            if (re_index[4:0] < 26) begin
                scs30_900k_seg = 18;
                scs30_900k_mod = re_index[4:0] + 4;
            end
            else begin
                scs30_900k_seg = 19;
                scs30_900k_mod = re_index[4:0] - 26;
            end
        7'd18:
            if (re_index[4:0] < 24) begin
                scs30_900k_seg = 19;
                scs30_900k_mod = re_index[4:0] + 6;
            end
            else begin
                scs30_900k_seg = 20;
                scs30_900k_mod = re_index[4:0] - 24;
            end
        7'd19:
            if (re_index[4:0] < 22) begin
                scs30_900k_seg = 20;
                scs30_900k_mod = re_index[4:0] + 8;
            end
            else begin
                scs30_900k_seg = 21;
                scs30_900k_mod = re_index[4:0] - 22;
            end
        7'd20:
            if (re_index[4:0] < 20) begin
                scs30_900k_seg = 21;
                scs30_900k_mod = re_index[4:0] + 10;
            end
            else begin
                scs30_900k_seg = 22;
                scs30_900k_mod = re_index[4:0] - 20;
            end
        7'd21:
            if (re_index[4:0] < 18) begin
                scs30_900k_seg = 22;
                scs30_900k_mod = re_index[4:0] + 12;
            end
            else begin
                scs30_900k_seg = 23;
                scs30_900k_mod = re_index[4:0] - 18;
            end
        7'd22:
            if (re_index[4:0] < 16) begin
                scs30_900k_seg = 23;
                scs30_900k_mod = re_index[4:0] + 14;
            end
            else begin
                scs30_900k_seg = 24;
                scs30_900k_mod = re_index[4:0] - 16;
            end
        7'd23:
            if (re_index[4:0] < 14) begin
                scs30_900k_seg = 24;
                scs30_900k_mod = re_index[4:0] + 16;
            end
            else begin
                scs30_900k_seg = 25;
                scs30_900k_mod = re_index[4:0] - 14;
            end
        7'd24:
            if (re_index[4:0] < 12) begin
                scs30_900k_seg = 25;
                scs30_900k_mod = re_index[4:0] + 18;
            end
            else begin
                scs30_900k_seg = 26;
                scs30_900k_mod = re_index[4:0] - 12;
            end
        7'd25:
            if (re_index[4:0] < 10) begin
                scs30_900k_seg = 26;
                scs30_900k_mod = re_index[4:0] + 20;
            end
            else begin
                scs30_900k_seg = 27;
                scs30_900k_mod = re_index[4:0] - 10;
            end
        7'd26:
            if (re_index[4:0] < 8) begin
                scs30_900k_seg = 27;
                scs30_900k_mod = re_index[4:0] + 22;
            end
            else begin
                scs30_900k_seg = 28;
                scs30_900k_mod = re_index[4:0] - 8;
            end
        7'd27:
            if (re_index[4:0] < 6) begin
                scs30_900k_seg = 28;
                scs30_900k_mod = re_index[4:0] + 24;
            end
            else begin
                scs30_900k_seg = 29;
                scs30_900k_mod = re_index[4:0] - 6;
            end
        7'd28:
            if (re_index[4:0] < 4) begin
                scs30_900k_seg = 29;
                scs30_900k_mod = re_index[4:0] + 26;
            end
            else begin
                scs30_900k_seg = 30;
                scs30_900k_mod = re_index[4:0] - 4;
            end
        7'd29:
            if (re_index[4:0] < 2) begin
                scs30_900k_seg = 30;
                scs30_900k_mod = re_index[4:0] + 28;
            end
            else begin
                scs30_900k_seg = 31;
                scs30_900k_mod = re_index[4:0] - 2;
            end
        7'd30:
            if (re_index[4:0] < 30) begin
                scs30_900k_seg = 32;
                scs30_900k_mod = re_index[4:0] + 0;
            end
            else begin
                scs30_900k_seg = 33;
                scs30_900k_mod = re_index[4:0] - 30;
            end
        7'd31:
            if (re_index[4:0] < 28) begin
                scs30_900k_seg = 33;
                scs30_900k_mod = re_index[4:0] + 2;
            end
            else begin
                scs30_900k_seg = 34;
                scs30_900k_mod = re_index[4:0] - 28;
            end
        7'd32:
            if (re_index[4:0] < 26) begin
                scs30_900k_seg = 34;
                scs30_900k_mod = re_index[4:0] + 4;
            end
            else begin
                scs30_900k_seg = 35;
                scs30_900k_mod = re_index[4:0] - 26;
            end
        7'd33:
            if (re_index[4:0] < 24) begin
                scs30_900k_seg = 35;
                scs30_900k_mod = re_index[4:0] + 6;
            end
            else begin
                scs30_900k_seg = 36;
                scs30_900k_mod = re_index[4:0] - 24;
            end
        7'd34:
            if (re_index[4:0] < 22) begin
                scs30_900k_seg = 36;
                scs30_900k_mod = re_index[4:0] + 8;
            end
            else begin
                scs30_900k_seg = 37;
                scs30_900k_mod = re_index[4:0] - 22;
            end
        7'd35:
            if (re_index[4:0] < 20) begin
                scs30_900k_seg = 37;
                scs30_900k_mod = re_index[4:0] + 10;
            end
            else begin
                scs30_900k_seg = 38;
                scs30_900k_mod = re_index[4:0] - 20;
            end
        7'd36:
            if (re_index[4:0] < 18) begin
                scs30_900k_seg = 38;
                scs30_900k_mod = re_index[4:0] + 12;
            end
            else begin
                scs30_900k_seg = 39;
                scs30_900k_mod = re_index[4:0] - 18;
            end
        7'd37:
            if (re_index[4:0] < 16) begin
                scs30_900k_seg = 39;
                scs30_900k_mod = re_index[4:0] + 14;
            end
            else begin
                scs30_900k_seg = 40;
                scs30_900k_mod = re_index[4:0] - 16;
            end
        7'd38:
            if (re_index[4:0] < 14) begin
                scs30_900k_seg = 40;
                scs30_900k_mod = re_index[4:0] + 16;
            end
            else begin
                scs30_900k_seg = 41;
                scs30_900k_mod = re_index[4:0] - 14;
            end
        7'd39:
            if (re_index[4:0] < 12) begin
                scs30_900k_seg = 41;
                scs30_900k_mod = re_index[4:0] + 18;
            end
            else begin
                scs30_900k_seg = 42;
                scs30_900k_mod = re_index[4:0] - 12;
            end
        7'd40:
            if (re_index[4:0] < 10) begin
                scs30_900k_seg = 42;
                scs30_900k_mod = re_index[4:0] + 20;
            end
            else begin
                scs30_900k_seg = 43;
                scs30_900k_mod = re_index[4:0] - 10;
            end
        7'd41:
            if (re_index[4:0] < 8) begin
                scs30_900k_seg = 43;
                scs30_900k_mod = re_index[4:0] + 22;
            end
            else begin
                scs30_900k_seg = 44;
                scs30_900k_mod = re_index[4:0] - 8;
            end
        7'd42:
            if (re_index[4:0] < 6) begin
                scs30_900k_seg = 44;
                scs30_900k_mod = re_index[4:0] + 24;
            end
            else begin
                scs30_900k_seg = 45;
                scs30_900k_mod = re_index[4:0] - 6;
            end
        7'd43:
            if (re_index[4:0] < 4) begin
                scs30_900k_seg = 45;
                scs30_900k_mod = re_index[4:0] + 26;
            end
            else begin
                scs30_900k_seg = 46;
                scs30_900k_mod = re_index[4:0] - 4;
            end
        7'd44:
            if (re_index[4:0] < 2) begin
                scs30_900k_seg = 46;
                scs30_900k_mod = re_index[4:0] + 28;
            end
            else begin
                scs30_900k_seg = 47;
                scs30_900k_mod = re_index[4:0] - 2;
            end
        7'd45:
            if (re_index[4:0] < 30) begin
                scs30_900k_seg = 48;
                scs30_900k_mod = re_index[4:0] + 0;
            end
            else begin
                scs30_900k_seg = 49;
                scs30_900k_mod = re_index[4:0] - 30;
            end
        7'd46:
            if (re_index[4:0] < 28) begin
                scs30_900k_seg = 49;
                scs30_900k_mod = re_index[4:0] + 2;
            end
            else begin
                scs30_900k_seg = 50;
                scs30_900k_mod = re_index[4:0] - 28;
            end
        7'd47:
            if (re_index[4:0] < 26) begin
                scs30_900k_seg = 50;
                scs30_900k_mod = re_index[4:0] + 4;
            end
            else begin
                scs30_900k_seg = 51;
                scs30_900k_mod = re_index[4:0] - 26;
            end
        7'd48:
            if (re_index[4:0] < 24) begin
                scs30_900k_seg = 51;
                scs30_900k_mod = re_index[4:0] + 6;
            end
            else begin
                scs30_900k_seg = 52;
                scs30_900k_mod = re_index[4:0] - 24;
            end
        7'd49:
            if (re_index[4:0] < 22) begin
                scs30_900k_seg = 52;
                scs30_900k_mod = re_index[4:0] + 8;
            end
            else begin
                scs30_900k_seg = 53;
                scs30_900k_mod = re_index[4:0] - 22;
            end
        7'd50:
            if (re_index[4:0] < 20) begin
                scs30_900k_seg = 53;
                scs30_900k_mod = re_index[4:0] + 10;
            end
            else begin
                scs30_900k_seg = 54;
                scs30_900k_mod = re_index[4:0] - 20;
            end
        7'd51:
            if (re_index[4:0] < 18) begin
                scs30_900k_seg = 54;
                scs30_900k_mod = re_index[4:0] + 12;
            end
            else begin
                scs30_900k_seg = 55;
                scs30_900k_mod = re_index[4:0] - 18;
            end
        7'd52:
            if (re_index[4:0] < 16) begin
                scs30_900k_seg = 55;
                scs30_900k_mod = re_index[4:0] + 14;
            end
            else begin
                scs30_900k_seg = 56;
                scs30_900k_mod = re_index[4:0] - 16;
            end
        7'd53:
            if (re_index[4:0] < 14) begin
                scs30_900k_seg = 56;
                scs30_900k_mod = re_index[4:0] + 16;
            end
            else begin
                scs30_900k_seg = 57;
                scs30_900k_mod = re_index[4:0] - 14;
            end
        7'd54:
            if (re_index[4:0] < 12) begin
                scs30_900k_seg = 57;
                scs30_900k_mod = re_index[4:0] + 18;
            end
            else begin
                scs30_900k_seg = 58;
                scs30_900k_mod = re_index[4:0] - 12;
            end
        7'd55:
            if (re_index[4:0] < 10) begin
                scs30_900k_seg = 58;
                scs30_900k_mod = re_index[4:0] + 20;
            end
            else begin
                scs30_900k_seg = 59;
                scs30_900k_mod = re_index[4:0] - 10;
            end
        7'd56:
            if (re_index[4:0] < 8) begin
                scs30_900k_seg = 59;
                scs30_900k_mod = re_index[4:0] + 22;
            end
            else begin
                scs30_900k_seg = 60;
                scs30_900k_mod = re_index[4:0] - 8;
            end
        7'd57:
            if (re_index[4:0] < 6) begin
                scs30_900k_seg = 60;
                scs30_900k_mod = re_index[4:0] + 24;
            end
            else begin
                scs30_900k_seg = 61;
                scs30_900k_mod = re_index[4:0] - 6;
            end
        7'd58:
            if (re_index[4:0] < 4) begin
                scs30_900k_seg = 61;
                scs30_900k_mod = re_index[4:0] + 26;
            end
            else begin
                scs30_900k_seg = 62;
                scs30_900k_mod = re_index[4:0] - 4;
            end
        7'd59:
            if (re_index[4:0] < 2) begin
                scs30_900k_seg = 62;
                scs30_900k_mod = re_index[4:0] + 28;
            end
            else begin
                scs30_900k_seg = 63;
                scs30_900k_mod = re_index[4:0] - 2;
            end
        7'd60:
            if (re_index[4:0] < 30) begin
                scs30_900k_seg = 64;
                scs30_900k_mod = re_index[4:0] + 0;
            end
            else begin
                scs30_900k_seg = 65;
                scs30_900k_mod = re_index[4:0] - 30;
            end
        7'd61:
            if (re_index[4:0] < 28) begin
                scs30_900k_seg = 65;
                scs30_900k_mod = re_index[4:0] + 2;
            end
            else begin
                scs30_900k_seg = 66;
                scs30_900k_mod = re_index[4:0] - 28;
            end
        7'd62:
            if (re_index[4:0] < 26) begin
                scs30_900k_seg = 66;
                scs30_900k_mod = re_index[4:0] + 4;
            end
            else begin
                scs30_900k_seg = 67;
                scs30_900k_mod = re_index[4:0] - 26;
            end
        7'd63:
            if (re_index[4:0] < 24) begin
                scs30_900k_seg = 67;
                scs30_900k_mod = re_index[4:0] + 6;
            end
            else begin
                scs30_900k_seg = 68;
                scs30_900k_mod = re_index[4:0] - 24;
            end
        7'd64:
            if (re_index[4:0] < 22) begin
                scs30_900k_seg = 68;
                scs30_900k_mod = re_index[4:0] + 8;
            end
            else begin
                scs30_900k_seg = 69;
                scs30_900k_mod = re_index[4:0] - 22;
            end
        7'd65:
            if (re_index[4:0] < 20) begin
                scs30_900k_seg = 69;
                scs30_900k_mod = re_index[4:0] + 10;
            end
            else begin
                scs30_900k_seg = 70;
                scs30_900k_mod = re_index[4:0] - 20;
            end
        7'd66:
            if (re_index[4:0] < 18) begin
                scs30_900k_seg = 70;
                scs30_900k_mod = re_index[4:0] + 12;
            end
            else begin
                scs30_900k_seg = 71;
                scs30_900k_mod = re_index[4:0] - 18;
            end
        7'd67:
            if (re_index[4:0] < 16) begin
                scs30_900k_seg = 71;
                scs30_900k_mod = re_index[4:0] + 14;
            end
            else begin
                scs30_900k_seg = 72;
                scs30_900k_mod = re_index[4:0] - 16;
            end
        7'd68:
            if (re_index[4:0] < 14) begin
                scs30_900k_seg = 72;
                scs30_900k_mod = re_index[4:0] + 16;
            end
            else begin
                scs30_900k_seg = 73;
                scs30_900k_mod = re_index[4:0] - 14;
            end
        7'd69:
            if (re_index[4:0] < 12) begin
                scs30_900k_seg = 73;
                scs30_900k_mod = re_index[4:0] + 18;
            end
            else begin
                scs30_900k_seg = 74;
                scs30_900k_mod = re_index[4:0] - 12;
            end
        7'd70:
            if (re_index[4:0] < 10) begin
                scs30_900k_seg = 74;
                scs30_900k_mod = re_index[4:0] + 20;
            end
            else begin
                scs30_900k_seg = 75;
                scs30_900k_mod = re_index[4:0] - 10;
            end
        7'd71:
            if (re_index[4:0] < 8) begin
                scs30_900k_seg = 75;
                scs30_900k_mod = re_index[4:0] + 22;
            end
            else begin
                scs30_900k_seg = 76;
                scs30_900k_mod = re_index[4:0] - 8;
            end
        7'd72:
            if (re_index[4:0] < 6) begin
                scs30_900k_seg = 76;
                scs30_900k_mod = re_index[4:0] + 24;
            end
            else begin
                scs30_900k_seg = 77;
                scs30_900k_mod = re_index[4:0] - 6;
            end
        7'd73:
            if (re_index[4:0] < 4) begin
                scs30_900k_seg = 77;
                scs30_900k_mod = re_index[4:0] + 26;
            end
            else begin
                scs30_900k_seg = 78;
                scs30_900k_mod = re_index[4:0] - 4;
            end
        7'd74:
            if (re_index[4:0] < 2) begin
                scs30_900k_seg = 78;
                scs30_900k_mod = re_index[4:0] + 28;
            end
            else begin
                scs30_900k_seg = 79;
                scs30_900k_mod = re_index[4:0] - 2;
            end
        7'd75:
            if (re_index[4:0] < 30) begin
                scs30_900k_seg = 80;
                scs30_900k_mod = re_index[4:0] + 0;
            end
            else begin
                scs30_900k_seg = 81;
                scs30_900k_mod = re_index[4:0] - 30;
            end
        7'd76:
            if (re_index[4:0] < 28) begin
                scs30_900k_seg = 81;
                scs30_900k_mod = re_index[4:0] + 2;
            end
            else begin
                scs30_900k_seg = 82;
                scs30_900k_mod = re_index[4:0] - 28;
            end
        7'd77:
            if (re_index[4:0] < 26) begin
                scs30_900k_seg = 82;
                scs30_900k_mod = re_index[4:0] + 4;
            end
            else begin
                scs30_900k_seg = 83;
                scs30_900k_mod = re_index[4:0] - 26;
            end
        7'd78:
            if (re_index[4:0] < 24) begin
                scs30_900k_seg = 83;
                scs30_900k_mod = re_index[4:0] + 6;
            end
            else begin
                scs30_900k_seg = 84;
                scs30_900k_mod = re_index[4:0] - 24;
            end
        7'd79:
            if (re_index[4:0] < 22) begin
                scs30_900k_seg = 84;
                scs30_900k_mod = re_index[4:0] + 8;
            end
            else begin
                scs30_900k_seg = 85;
                scs30_900k_mod = re_index[4:0] - 22;
            end
        7'd80:
            if (re_index[4:0] < 20) begin
                scs30_900k_seg = 85;
                scs30_900k_mod = re_index[4:0] + 10;
            end
            else begin
                scs30_900k_seg = 86;
                scs30_900k_mod = re_index[4:0] - 20;
            end
        7'd81:
            if (re_index[4:0] < 18) begin
                scs30_900k_seg = 86;
                scs30_900k_mod = re_index[4:0] + 12;
            end
            else begin
                scs30_900k_seg = 87;
                scs30_900k_mod = re_index[4:0] - 18;
            end
        7'd82:
            if (re_index[4:0] < 16) begin
                scs30_900k_seg = 87;
                scs30_900k_mod = re_index[4:0] + 14;
            end
            else begin
                scs30_900k_seg = 88;
                scs30_900k_mod = re_index[4:0] - 16;
            end
        7'd83:
            if (re_index[4:0] < 14) begin
                scs30_900k_seg = 88;
                scs30_900k_mod = re_index[4:0] + 16;
            end
            else begin
                scs30_900k_seg = 89;
                scs30_900k_mod = re_index[4:0] - 14;
            end
        7'd84:
            if (re_index[4:0] < 12) begin
                scs30_900k_seg = 89;
                scs30_900k_mod = re_index[4:0] + 18;
            end
            else begin
                scs30_900k_seg = 90;
                scs30_900k_mod = re_index[4:0] - 12;
            end
        7'd85:
            if (re_index[4:0] < 10) begin
                scs30_900k_seg = 90;
                scs30_900k_mod = re_index[4:0] + 20;
            end
            else begin
                scs30_900k_seg = 91;
                scs30_900k_mod = re_index[4:0] - 10;
            end
        7'd86:
            if (re_index[4:0] < 8) begin
                scs30_900k_seg = 91;
                scs30_900k_mod = re_index[4:0] + 22;
            end
            else begin
                scs30_900k_seg = 92;
                scs30_900k_mod = re_index[4:0] - 8;
            end
        7'd87:
            if (re_index[4:0] < 6) begin
                scs30_900k_seg = 92;
                scs30_900k_mod = re_index[4:0] + 24;
            end
            else begin
                scs30_900k_seg = 93;
                scs30_900k_mod = re_index[4:0] - 6;
            end
        7'd88:
            if (re_index[4:0] < 4) begin
                scs30_900k_seg = 93;
                scs30_900k_mod = re_index[4:0] + 26;
            end
            else begin
                scs30_900k_seg = 94;
                scs30_900k_mod = re_index[4:0] - 4;
            end
        7'd89:
            if (re_index[4:0] < 2) begin
                scs30_900k_seg = 94;
                scs30_900k_mod = re_index[4:0] + 28;
            end
            else begin
                scs30_900k_seg = 95;
                scs30_900k_mod = re_index[4:0] - 2;
            end
        7'd90:
            if (re_index[4:0] < 30) begin
                scs30_900k_seg = 96;
                scs30_900k_mod = re_index[4:0] + 0;
            end
            else begin
                scs30_900k_seg = 97;
                scs30_900k_mod = re_index[4:0] - 30;
            end
        7'd91:
            if (re_index[4:0] < 28) begin
                scs30_900k_seg = 97;
                scs30_900k_mod = re_index[4:0] + 2;
            end
            else begin
                scs30_900k_seg = 98;
                scs30_900k_mod = re_index[4:0] - 28;
            end
        7'd92:
            if (re_index[4:0] < 26) begin
                scs30_900k_seg = 98;
                scs30_900k_mod = re_index[4:0] + 4;
            end
            else begin
                scs30_900k_seg = 99;
                scs30_900k_mod = re_index[4:0] - 26;
            end
        7'd93:
            if (re_index[4:0] < 24) begin
                scs30_900k_seg = 99;
                scs30_900k_mod = re_index[4:0] + 6;
            end
            else begin
                scs30_900k_seg = 100;
                scs30_900k_mod = re_index[4:0] - 24;
            end
        7'd94:
            if (re_index[4:0] < 22) begin
                scs30_900k_seg = 100;
                scs30_900k_mod = re_index[4:0] + 8;
            end
            else begin
                scs30_900k_seg = 101;
                scs30_900k_mod = re_index[4:0] - 22;
            end
        7'd95:
            if (re_index[4:0] < 20) begin
                scs30_900k_seg = 101;
                scs30_900k_mod = re_index[4:0] + 10;
            end
            else begin
                scs30_900k_seg = 102;
                scs30_900k_mod = re_index[4:0] - 20;
            end
        7'd96:
            if (re_index[4:0] < 18) begin
                scs30_900k_seg = 102;
                scs30_900k_mod = re_index[4:0] + 12;
            end
            else begin
                scs30_900k_seg = 103;
                scs30_900k_mod = re_index[4:0] - 18;
            end
        7'd97:
            if (re_index[4:0] < 16) begin
                scs30_900k_seg = 103;
                scs30_900k_mod = re_index[4:0] + 14;
            end
            else begin
                scs30_900k_seg = 104;
                scs30_900k_mod = re_index[4:0] - 16;
            end
        7'd98:
            if (re_index[4:0] < 14) begin
                scs30_900k_seg = 104;
                scs30_900k_mod = re_index[4:0] + 16;
            end
            else begin
                scs30_900k_seg = 105;
                scs30_900k_mod = re_index[4:0] - 14;
            end
        7'd99:
            if (re_index[4:0] < 12) begin
                scs30_900k_seg = 105;
                scs30_900k_mod = re_index[4:0] + 18;
            end
            else begin
                scs30_900k_seg = 106;
                scs30_900k_mod = re_index[4:0] - 12;
            end
        7'd100:
            if (re_index[4:0] < 10) begin
                scs30_900k_seg = 106;
                scs30_900k_mod = re_index[4:0] + 20;
            end
            else begin
                scs30_900k_seg = 107;
                scs30_900k_mod = re_index[4:0] - 10;
            end
        7'd101:
            if (re_index[4:0] < 8) begin
                scs30_900k_seg = 107;
                scs30_900k_mod = re_index[4:0] + 22;
            end
            else begin
                scs30_900k_seg = 108;
                scs30_900k_mod = re_index[4:0] - 8;
            end
        7'd102:
            if (re_index[4:0] < 6) begin
                scs30_900k_seg = 108;
                scs30_900k_mod = re_index[4:0] + 24;
            end
            else begin
                scs30_900k_seg = 109;
                scs30_900k_mod = re_index[4:0] - 6;
            end
        7'd103:
            if (re_index[4:0] < 4) begin
                scs30_900k_seg = 109;
                scs30_900k_mod = re_index[4:0] + 26;
            end
            else begin
                scs30_900k_seg = 110;
                scs30_900k_mod = re_index[4:0] - 4;
            end
        7'd104:
            if (re_index[4:0] < 2) begin
                scs30_900k_seg = 110;
                scs30_900k_mod = re_index[4:0] + 28;
            end
            else begin
                scs30_900k_seg = 111;
                scs30_900k_mod = re_index[4:0] - 2;
            end
        7'd105:
            if (re_index[4:0] < 30) begin
                scs30_900k_seg = 112;
                scs30_900k_mod = re_index[4:0] + 0;
            end
            else begin
                scs30_900k_seg = 113;
                scs30_900k_mod = re_index[4:0] - 30;
            end
        7'd106:
            if (re_index[4:0] < 28) begin
                scs30_900k_seg = 113;
                scs30_900k_mod = re_index[4:0] + 2;
            end
            else begin
                scs30_900k_seg = 114;
                scs30_900k_mod = re_index[4:0] - 28;
            end
        7'd107:
            if (re_index[4:0] < 26) begin
                scs30_900k_seg = 114;
                scs30_900k_mod = re_index[4:0] + 4;
            end
            else begin
                scs30_900k_seg = 115;
                scs30_900k_mod = re_index[4:0] - 26;
            end
        7'd108:
            if (re_index[4:0] < 24) begin
                scs30_900k_seg = 115;
                scs30_900k_mod = re_index[4:0] + 6;
            end
            else begin
                scs30_900k_seg = 116;
                scs30_900k_mod = re_index[4:0] - 24;
            end
        7'd109:
            if (re_index[4:0] < 22) begin
                scs30_900k_seg = 116;
                scs30_900k_mod = re_index[4:0] + 8;
            end
            else begin
                scs30_900k_seg = 117;
                scs30_900k_mod = re_index[4:0] - 22;
            end
        7'd110:
            if (re_index[4:0] < 20) begin
                scs30_900k_seg = 117;
                scs30_900k_mod = re_index[4:0] + 10;
            end
            else begin
                scs30_900k_seg = 118;
                scs30_900k_mod = re_index[4:0] - 20;
            end
        7'd111:
            if (re_index[4:0] < 18) begin
                scs30_900k_seg = 118;
                scs30_900k_mod = re_index[4:0] + 12;
            end
            else begin
                scs30_900k_seg = 119;
                scs30_900k_mod = re_index[4:0] - 18;
            end
        7'd112:
            if (re_index[4:0] < 16) begin
                scs30_900k_seg = 119;
                scs30_900k_mod = re_index[4:0] + 14;
            end
            else begin
                scs30_900k_seg = 120;
                scs30_900k_mod = re_index[4:0] - 16;
            end
        7'd113:
            if (re_index[4:0] < 14) begin
                scs30_900k_seg = 120;
                scs30_900k_mod = re_index[4:0] + 16;
            end
            else begin
                scs30_900k_seg = 121;
                scs30_900k_mod = re_index[4:0] - 14;
            end
        7'd114:
            if (re_index[4:0] < 12) begin
                scs30_900k_seg = 121;
                scs30_900k_mod = re_index[4:0] + 18;
            end
            else begin
                scs30_900k_seg = 122;
                scs30_900k_mod = re_index[4:0] - 12;
            end
        7'd115:
            if (re_index[4:0] < 10) begin
                scs30_900k_seg = 122;
                scs30_900k_mod = re_index[4:0] + 20;
            end
            else begin
                scs30_900k_seg = 123;
                scs30_900k_mod = re_index[4:0] - 10;
            end
        7'd116:
            if (re_index[4:0] < 8) begin
                scs30_900k_seg = 123;
                scs30_900k_mod = re_index[4:0] + 22;
            end
            else begin
                scs30_900k_seg = 124;
                scs30_900k_mod = re_index[4:0] - 8;
            end
        7'd117:
            if (re_index[4:0] < 6) begin
                scs30_900k_seg = 124;
                scs30_900k_mod = re_index[4:0] + 24;
            end
            else begin
                scs30_900k_seg = 125;
                scs30_900k_mod = re_index[4:0] - 6;
            end
        7'd118:
            if (re_index[4:0] < 4) begin
                scs30_900k_seg = 125;
                scs30_900k_mod = re_index[4:0] + 26;
            end
            else begin
                scs30_900k_seg = 126;
                scs30_900k_mod = re_index[4:0] - 4;
            end
        7'd119:
            if (re_index[4:0] < 2) begin
                scs30_900k_seg = 126;
                scs30_900k_mod = re_index[4:0] + 28;
            end
            else begin
                scs30_900k_seg = 127;
                scs30_900k_mod = re_index[4:0] - 2;
            end
        7'd120:
            if (re_index[4:0] < 30) begin
                scs30_900k_seg = 128;
                scs30_900k_mod = re_index[4:0] + 0;
            end
            else begin
                scs30_900k_seg = 129;
                scs30_900k_mod = re_index[4:0] - 30;
            end
        7'd121:
            if (re_index[4:0] < 28) begin
                scs30_900k_seg = 129;
                scs30_900k_mod = re_index[4:0] + 2;
            end
            else begin
                scs30_900k_seg = 130;
                scs30_900k_mod = re_index[4:0] - 28;
            end
        7'd122:
            if (re_index[4:0] < 26) begin
                scs30_900k_seg = 130;
                scs30_900k_mod = re_index[4:0] + 4;
            end
            else begin
                scs30_900k_seg = 131;
                scs30_900k_mod = re_index[4:0] - 26;
            end
        7'd123:
            if (re_index[4:0] < 24) begin
                scs30_900k_seg = 131;
                scs30_900k_mod = re_index[4:0] + 6;
            end
            else begin
                scs30_900k_seg = 132;
                scs30_900k_mod = re_index[4:0] - 24;
            end
        7'd124:
            if (re_index[4:0] < 22) begin
                scs30_900k_seg = 132;
                scs30_900k_mod = re_index[4:0] + 8;
            end
            else begin
                scs30_900k_seg = 133;
                scs30_900k_mod = re_index[4:0] - 22;
            end
        7'd125:
            if (re_index[4:0] < 20) begin
                scs30_900k_seg = 133;
                scs30_900k_mod = re_index[4:0] + 10;
            end
            else begin
                scs30_900k_seg = 134;
                scs30_900k_mod = re_index[4:0] - 20;
            end
        7'd126:
            if (re_index[4:0] < 18) begin
                scs30_900k_seg = 134;
                scs30_900k_mod = re_index[4:0] + 12;
            end
            else begin
                scs30_900k_seg = 135;
                scs30_900k_mod = re_index[4:0] - 18;
            end
        7'd127:
            if (re_index[4:0] < 16) begin
                scs30_900k_seg = 135;
                scs30_900k_mod = re_index[4:0] + 14;
            end
            else begin
                scs30_900k_seg = 136;
                scs30_900k_mod = re_index[4:0] - 16;
            end
    endcase
end
// scs15, seg64
reg [5:0] scs15_900k_seg;
reg [5:0] scs15_900k_mod;
always @(*) begin
    case (re_index[11:6])
        6'd0:
            if (re_index[5:0] < 60) begin
                scs15_900k_seg = 0;
                scs15_900k_mod = re_index[5:0] + 0;
            end
            else begin
                scs15_900k_seg = 1;
                scs15_900k_mod = re_index[5:0] - 60;
            end
        6'd1:
            if (re_index[5:0] < 56) begin
                scs15_900k_seg = 1;
                scs15_900k_mod = re_index[5:0] + 4;
            end
            else begin
                scs15_900k_seg = 2;
                scs15_900k_mod = re_index[5:0] - 56;
            end
        6'd2:
            if (re_index[5:0] < 52) begin
                scs15_900k_seg = 2;
                scs15_900k_mod = re_index[5:0] + 8;
            end
            else begin
                scs15_900k_seg = 3;
                scs15_900k_mod = re_index[5:0] - 52;
            end
        6'd3:
            if (re_index[5:0] < 48) begin
                scs15_900k_seg = 3;
                scs15_900k_mod = re_index[5:0] + 12;
            end
            else begin
                scs15_900k_seg = 4;
                scs15_900k_mod = re_index[5:0] - 48;
            end
        6'd4:
            if (re_index[5:0] < 44) begin
                scs15_900k_seg = 4;
                scs15_900k_mod = re_index[5:0] + 16;
            end
            else begin
                scs15_900k_seg = 5;
                scs15_900k_mod = re_index[5:0] - 44;
            end
        6'd5:
            if (re_index[5:0] < 40) begin
                scs15_900k_seg = 5;
                scs15_900k_mod = re_index[5:0] + 20;
            end
            else begin
                scs15_900k_seg = 6;
                scs15_900k_mod = re_index[5:0] - 40;
            end
        6'd6:
            if (re_index[5:0] < 36) begin
                scs15_900k_seg = 6;
                scs15_900k_mod = re_index[5:0] + 24;
            end
            else begin
                scs15_900k_seg = 7;
                scs15_900k_mod = re_index[5:0] - 36;
            end
        6'd7:
            if (re_index[5:0] < 32) begin
                scs15_900k_seg = 7;
                scs15_900k_mod = re_index[5:0] + 28;
            end
            else begin
                scs15_900k_seg = 8;
                scs15_900k_mod = re_index[5:0] - 32;
            end
        6'd8:
            if (re_index[5:0] < 28) begin
                scs15_900k_seg = 8;
                scs15_900k_mod = re_index[5:0] + 32;
            end
            else begin
                scs15_900k_seg = 9;
                scs15_900k_mod = re_index[5:0] - 28;
            end
        6'd9:
            if (re_index[5:0] < 24) begin
                scs15_900k_seg = 9;
                scs15_900k_mod = re_index[5:0] + 36;
            end
            else begin
                scs15_900k_seg = 10;
                scs15_900k_mod = re_index[5:0] - 24;
            end
        6'd10:
            if (re_index[5:0] < 20) begin
                scs15_900k_seg = 10;
                scs15_900k_mod = re_index[5:0] + 40;
            end
            else begin
                scs15_900k_seg = 11;
                scs15_900k_mod = re_index[5:0] - 20;
            end
        6'd11:
            if (re_index[5:0] < 16) begin
                scs15_900k_seg = 11;
                scs15_900k_mod = re_index[5:0] + 44;
            end
            else begin
                scs15_900k_seg = 12;
                scs15_900k_mod = re_index[5:0] - 16;
            end
        6'd12:
            if (re_index[5:0] < 12) begin
                scs15_900k_seg = 12;
                scs15_900k_mod = re_index[5:0] + 48;
            end
            else begin
                scs15_900k_seg = 13;
                scs15_900k_mod = re_index[5:0] - 12;
            end
        6'd13:
            if (re_index[5:0] < 8) begin
                scs15_900k_seg = 13;
                scs15_900k_mod = re_index[5:0] + 52;
            end
            else begin
                scs15_900k_seg = 14;
                scs15_900k_mod = re_index[5:0] - 8;
            end
        6'd14:
            if (re_index[5:0] < 4) begin
                scs15_900k_seg = 14;
                scs15_900k_mod = re_index[5:0] + 56;
            end
            else begin
                scs15_900k_seg = 15;
                scs15_900k_mod = re_index[5:0] - 4;
            end
        6'd15:
            if (re_index[5:0] < 60) begin
                scs15_900k_seg = 16;
                scs15_900k_mod = re_index[5:0] + 0;
            end
            else begin
                scs15_900k_seg = 17;
                scs15_900k_mod = re_index[5:0] - 60;
            end
        6'd16:
            if (re_index[5:0] < 56) begin
                scs15_900k_seg = 17;
                scs15_900k_mod = re_index[5:0] + 4;
            end
            else begin
                scs15_900k_seg = 18;
                scs15_900k_mod = re_index[5:0] - 56;
            end
        6'd17:
            if (re_index[5:0] < 52) begin
                scs15_900k_seg = 18;
                scs15_900k_mod = re_index[5:0] + 8;
            end
            else begin
                scs15_900k_seg = 19;
                scs15_900k_mod = re_index[5:0] - 52;
            end
        6'd18:
            if (re_index[5:0] < 48) begin
                scs15_900k_seg = 19;
                scs15_900k_mod = re_index[5:0] + 12;
            end
            else begin
                scs15_900k_seg = 20;
                scs15_900k_mod = re_index[5:0] - 48;
            end
        6'd19:
            if (re_index[5:0] < 44) begin
                scs15_900k_seg = 20;
                scs15_900k_mod = re_index[5:0] + 16;
            end
            else begin
                scs15_900k_seg = 21;
                scs15_900k_mod = re_index[5:0] - 44;
            end
        6'd20:
            if (re_index[5:0] < 40) begin
                scs15_900k_seg = 21;
                scs15_900k_mod = re_index[5:0] + 20;
            end
            else begin
                scs15_900k_seg = 22;
                scs15_900k_mod = re_index[5:0] - 40;
            end
        6'd21:
            if (re_index[5:0] < 36) begin
                scs15_900k_seg = 22;
                scs15_900k_mod = re_index[5:0] + 24;
            end
            else begin
                scs15_900k_seg = 23;
                scs15_900k_mod = re_index[5:0] - 36;
            end
        6'd22:
            if (re_index[5:0] < 32) begin
                scs15_900k_seg = 23;
                scs15_900k_mod = re_index[5:0] + 28;
            end
            else begin
                scs15_900k_seg = 24;
                scs15_900k_mod = re_index[5:0] - 32;
            end
        6'd23:
            if (re_index[5:0] < 28) begin
                scs15_900k_seg = 24;
                scs15_900k_mod = re_index[5:0] + 32;
            end
            else begin
                scs15_900k_seg = 25;
                scs15_900k_mod = re_index[5:0] - 28;
            end
        6'd24:
            if (re_index[5:0] < 24) begin
                scs15_900k_seg = 25;
                scs15_900k_mod = re_index[5:0] + 36;
            end
            else begin
                scs15_900k_seg = 26;
                scs15_900k_mod = re_index[5:0] - 24;
            end
        6'd25:
            if (re_index[5:0] < 20) begin
                scs15_900k_seg = 26;
                scs15_900k_mod = re_index[5:0] + 40;
            end
            else begin
                scs15_900k_seg = 27;
                scs15_900k_mod = re_index[5:0] - 20;
            end
        6'd26:
            if (re_index[5:0] < 16) begin
                scs15_900k_seg = 27;
                scs15_900k_mod = re_index[5:0] + 44;
            end
            else begin
                scs15_900k_seg = 28;
                scs15_900k_mod = re_index[5:0] - 16;
            end
        6'd27:
            if (re_index[5:0] < 12) begin
                scs15_900k_seg = 28;
                scs15_900k_mod = re_index[5:0] + 48;
            end
            else begin
                scs15_900k_seg = 29;
                scs15_900k_mod = re_index[5:0] - 12;
            end
        6'd28:
            if (re_index[5:0] < 8) begin
                scs15_900k_seg = 29;
                scs15_900k_mod = re_index[5:0] + 52;
            end
            else begin
                scs15_900k_seg = 30;
                scs15_900k_mod = re_index[5:0] - 8;
            end
        6'd29:
            if (re_index[5:0] < 4) begin
                scs15_900k_seg = 30;
                scs15_900k_mod = re_index[5:0] + 56;
            end
            else begin
                scs15_900k_seg = 31;
                scs15_900k_mod = re_index[5:0] - 4;
            end
        6'd30:
            if (re_index[5:0] < 60) begin
                scs15_900k_seg = 32;
                scs15_900k_mod = re_index[5:0] + 0;
            end
            else begin
                scs15_900k_seg = 33;
                scs15_900k_mod = re_index[5:0] - 60;
            end
        6'd31:
            if (re_index[5:0] < 56) begin
                scs15_900k_seg = 33;
                scs15_900k_mod = re_index[5:0] + 4;
            end
            else begin
                scs15_900k_seg = 34;
                scs15_900k_mod = re_index[5:0] - 56;
            end
        6'd32:
            if (re_index[5:0] < 52) begin
                scs15_900k_seg = 34;
                scs15_900k_mod = re_index[5:0] + 8;
            end
            else begin
                scs15_900k_seg = 35;
                scs15_900k_mod = re_index[5:0] - 52;
            end
        6'd33:
            if (re_index[5:0] < 48) begin
                scs15_900k_seg = 35;
                scs15_900k_mod = re_index[5:0] + 12;
            end
            else begin
                scs15_900k_seg = 36;
                scs15_900k_mod = re_index[5:0] - 48;
            end
        6'd34:
            if (re_index[5:0] < 44) begin
                scs15_900k_seg = 36;
                scs15_900k_mod = re_index[5:0] + 16;
            end
            else begin
                scs15_900k_seg = 37;
                scs15_900k_mod = re_index[5:0] - 44;
            end
        6'd35:
            if (re_index[5:0] < 40) begin
                scs15_900k_seg = 37;
                scs15_900k_mod = re_index[5:0] + 20;
            end
            else begin
                scs15_900k_seg = 38;
                scs15_900k_mod = re_index[5:0] - 40;
            end
        6'd36:
            if (re_index[5:0] < 36) begin
                scs15_900k_seg = 38;
                scs15_900k_mod = re_index[5:0] + 24;
            end
            else begin
                scs15_900k_seg = 39;
                scs15_900k_mod = re_index[5:0] - 36;
            end
        6'd37:
            if (re_index[5:0] < 32) begin
                scs15_900k_seg = 39;
                scs15_900k_mod = re_index[5:0] + 28;
            end
            else begin
                scs15_900k_seg = 40;
                scs15_900k_mod = re_index[5:0] - 32;
            end
        6'd38:
            if (re_index[5:0] < 28) begin
                scs15_900k_seg = 40;
                scs15_900k_mod = re_index[5:0] + 32;
            end
            else begin
                scs15_900k_seg = 41;
                scs15_900k_mod = re_index[5:0] - 28;
            end
        6'd39:
            if (re_index[5:0] < 24) begin
                scs15_900k_seg = 41;
                scs15_900k_mod = re_index[5:0] + 36;
            end
            else begin
                scs15_900k_seg = 42;
                scs15_900k_mod = re_index[5:0] - 24;
            end
        6'd40:
            if (re_index[5:0] < 20) begin
                scs15_900k_seg = 42;
                scs15_900k_mod = re_index[5:0] + 40;
            end
            else begin
                scs15_900k_seg = 43;
                scs15_900k_mod = re_index[5:0] - 20;
            end
        6'd41:
            if (re_index[5:0] < 16) begin
                scs15_900k_seg = 43;
                scs15_900k_mod = re_index[5:0] + 44;
            end
            else begin
                scs15_900k_seg = 44;
                scs15_900k_mod = re_index[5:0] - 16;
            end
        6'd42:
            if (re_index[5:0] < 12) begin
                scs15_900k_seg = 44;
                scs15_900k_mod = re_index[5:0] + 48;
            end
            else begin
                scs15_900k_seg = 45;
                scs15_900k_mod = re_index[5:0] - 12;
            end
        6'd43:
            if (re_index[5:0] < 8) begin
                scs15_900k_seg = 45;
                scs15_900k_mod = re_index[5:0] + 52;
            end
            else begin
                scs15_900k_seg = 46;
                scs15_900k_mod = re_index[5:0] - 8;
            end
        6'd44:
            if (re_index[5:0] < 4) begin
                scs15_900k_seg = 46;
                scs15_900k_mod = re_index[5:0] + 56;
            end
            else begin
                scs15_900k_seg = 47;
                scs15_900k_mod = re_index[5:0] - 4;
            end
        6'd45:
            if (re_index[5:0] < 60) begin
                scs15_900k_seg = 48;
                scs15_900k_mod = re_index[5:0] + 0;
            end
            else begin
                scs15_900k_seg = 49;
                scs15_900k_mod = re_index[5:0] - 60;
            end
        6'd46:
            if (re_index[5:0] < 56) begin
                scs15_900k_seg = 49;
                scs15_900k_mod = re_index[5:0] + 4;
            end
            else begin
                scs15_900k_seg = 50;
                scs15_900k_mod = re_index[5:0] - 56;
            end
        6'd47:
            if (re_index[5:0] < 52) begin
                scs15_900k_seg = 50;
                scs15_900k_mod = re_index[5:0] + 8;
            end
            else begin
                scs15_900k_seg = 51;
                scs15_900k_mod = re_index[5:0] - 52;
            end
        6'd48:
            if (re_index[5:0] < 48) begin
                scs15_900k_seg = 51;
                scs15_900k_mod = re_index[5:0] + 12;
            end
            else begin
                scs15_900k_seg = 52;
                scs15_900k_mod = re_index[5:0] - 48;
            end
        6'd49:
            if (re_index[5:0] < 44) begin
                scs15_900k_seg = 52;
                scs15_900k_mod = re_index[5:0] + 16;
            end
            else begin
                scs15_900k_seg = 53;
                scs15_900k_mod = re_index[5:0] - 44;
            end
        6'd50:
            if (re_index[5:0] < 40) begin
                scs15_900k_seg = 53;
                scs15_900k_mod = re_index[5:0] + 20;
            end
            else begin
                scs15_900k_seg = 54;
                scs15_900k_mod = re_index[5:0] - 40;
            end
        6'd51:
            if (re_index[5:0] < 36) begin
                scs15_900k_seg = 54;
                scs15_900k_mod = re_index[5:0] + 24;
            end
            else begin
                scs15_900k_seg = 55;
                scs15_900k_mod = re_index[5:0] - 36;
            end
        6'd52:
            if (re_index[5:0] < 32) begin
                scs15_900k_seg = 55;
                scs15_900k_mod = re_index[5:0] + 28;
            end
            else begin
                scs15_900k_seg = 56;
                scs15_900k_mod = re_index[5:0] - 32;
            end
        6'd53:
            if (re_index[5:0] < 28) begin
                scs15_900k_seg = 56;
                scs15_900k_mod = re_index[5:0] + 32;
            end
            else begin
                scs15_900k_seg = 57;
                scs15_900k_mod = re_index[5:0] - 28;
            end
        6'd54:
            if (re_index[5:0] < 24) begin
                scs15_900k_seg = 57;
                scs15_900k_mod = re_index[5:0] + 36;
            end
            else begin
                scs15_900k_seg = 58;
                scs15_900k_mod = re_index[5:0] - 24;
            end
        6'd55:
            if (re_index[5:0] < 20) begin
                scs15_900k_seg = 58;
                scs15_900k_mod = re_index[5:0] + 40;
            end
            else begin
                scs15_900k_seg = 59;
                scs15_900k_mod = re_index[5:0] - 20;
            end
        6'd56:
            if (re_index[5:0] < 16) begin
                scs15_900k_seg = 59;
                scs15_900k_mod = re_index[5:0] + 44;
            end
            else begin
                scs15_900k_seg = 60;
                scs15_900k_mod = re_index[5:0] - 16;
            end
        6'd57:
            if (re_index[5:0] < 12) begin
                scs15_900k_seg = 60;
                scs15_900k_mod = re_index[5:0] + 48;
            end
            else begin
                scs15_900k_seg = 61;
                scs15_900k_mod = re_index[5:0] - 12;
            end
        6'd58:
            if (re_index[5:0] < 8) begin
                scs15_900k_seg = 61;
                scs15_900k_mod = re_index[5:0] + 52;
            end
            else begin
                scs15_900k_seg = 62;
                scs15_900k_mod = re_index[5:0] - 8;
            end
        6'd59:
            if (re_index[5:0] < 4) begin
                scs15_900k_seg = 62;
                scs15_900k_mod = re_index[5:0] + 56;
            end
            else begin
                scs15_900k_seg = 63;
                scs15_900k_mod = re_index[5:0] - 4;
            end
        6'd60:
            if (re_index[5:0] < 60) begin
                scs15_900k_seg = 64;
                scs15_900k_mod = re_index[5:0] + 0;
            end
            else begin
                scs15_900k_seg = 65;
                scs15_900k_mod = re_index[5:0] - 60;
            end
        6'd61:
            if (re_index[5:0] < 56) begin
                scs15_900k_seg = 65;
                scs15_900k_mod = re_index[5:0] + 4;
            end
            else begin
                scs15_900k_seg = 66;
                scs15_900k_mod = re_index[5:0] - 56;
            end
        6'd62:
            if (re_index[5:0] < 52) begin
                scs15_900k_seg = 66;
                scs15_900k_mod = re_index[5:0] + 8;
            end
            else begin
                scs15_900k_seg = 67;
                scs15_900k_mod = re_index[5:0] - 52;
            end
        6'd63:
            if (re_index[5:0] < 48) begin
                scs15_900k_seg = 67;
                scs15_900k_mod = re_index[5:0] + 12;
            end
            else begin
                scs15_900k_seg = 68;
                scs15_900k_mod = re_index[5:0] - 48;
            end
    endcase
end
// scs5, seg16
reg [3:0] scs5_900k_seg;
reg [7:0] scs5_900k_mod;
always @(*) begin
    case (re_index[11:8])
        4'd0:
            if (re_index[7:0] < 180) begin
                scs5_900k_seg = 0;
                scs5_900k_mod = re_index[7:0] + 0;
            end
            else begin
                scs5_900k_seg = 1;
                scs5_900k_mod = re_index[7:0] - 180;
            end
        4'd1:
            if (re_index[7:0] < 104) begin
                scs5_900k_seg = 1;
                scs5_900k_mod = re_index[7:0] + 76;
            end
            else begin
                scs5_900k_seg = 2;
                scs5_900k_mod = re_index[7:0] - 104;
            end
        4'd2:
            if (re_index[7:0] < 28) begin
                scs5_900k_seg = 2;
                scs5_900k_mod = re_index[7:0] + 152;
            end
            else begin
                scs5_900k_seg = 3;
                scs5_900k_mod = re_index[7:0] - 28;
            end
        4'd3:
            if (re_index[7:0] < 132) begin
                scs5_900k_seg = 4;
                scs5_900k_mod = re_index[7:0] + 48;
            end
            else begin
                scs5_900k_seg = 5;
                scs5_900k_mod = re_index[7:0] - 132;
            end
        4'd4:
            if (re_index[7:0] < 56) begin
                scs5_900k_seg = 5;
                scs5_900k_mod = re_index[7:0] + 124;
            end
            else begin
                scs5_900k_seg = 6;
                scs5_900k_mod = re_index[7:0] - 56;
            end
        4'd5:
            if (re_index[7:0] < 160) begin
                scs5_900k_seg = 7;
                scs5_900k_mod = re_index[7:0] + 20;
            end
            else begin
                scs5_900k_seg = 8;
                scs5_900k_mod = re_index[7:0] - 160;
            end
        4'd6:
            if (re_index[7:0] < 84) begin
                scs5_900k_seg = 8;
                scs5_900k_mod = re_index[7:0] + 96;
            end
            else begin
                scs5_900k_seg = 9;
                scs5_900k_mod = re_index[7:0] - 84;
            end
        4'd7:
            if (re_index[7:0] < 8) begin
                scs5_900k_seg = 9;
                scs5_900k_mod = re_index[7:0] + 172;
            end
            else begin
                scs5_900k_seg = 10;
                scs5_900k_mod = re_index[7:0] - 8;
            end
        4'd8:
            if (re_index[7:0] < 112) begin
                scs5_900k_seg = 11;
                scs5_900k_mod = re_index[7:0] + 68;
            end
            else begin
                scs5_900k_seg = 12;
                scs5_900k_mod = re_index[7:0] - 112;
            end
        4'd9:
            if (re_index[7:0] < 36) begin
                scs5_900k_seg = 12;
                scs5_900k_mod = re_index[7:0] + 144;
            end
            else begin
                scs5_900k_seg = 13;
                scs5_900k_mod = re_index[7:0] - 36;
            end
        4'd10:
            if (re_index[7:0] < 140) begin
                scs5_900k_seg = 14;
                scs5_900k_mod = re_index[7:0] + 40;
            end
            else begin
                scs5_900k_seg = 15;
                scs5_900k_mod = re_index[7:0] - 140;
            end
        4'd11:
            if (re_index[7:0] < 64) begin
                scs5_900k_seg = 15;
                scs5_900k_mod = re_index[7:0] + 116;
            end
            else begin
                scs5_900k_seg = 16;
                scs5_900k_mod = re_index[7:0] - 64;
            end
        4'd12:
            if (re_index[7:0] < 168) begin
                scs5_900k_seg = 17;
                scs5_900k_mod = re_index[7:0] + 12;
            end
            else begin
                scs5_900k_seg = 18;
                scs5_900k_mod = re_index[7:0] - 168;
            end
        4'd13:
            if (re_index[7:0] < 92) begin
                scs5_900k_seg = 18;
                scs5_900k_mod = re_index[7:0] + 88;
            end
            else begin
                scs5_900k_seg = 19;
                scs5_900k_mod = re_index[7:0] - 92;
            end
        4'd14:
            if (re_index[7:0] < 16) begin
                scs5_900k_seg = 19;
                scs5_900k_mod = re_index[7:0] + 164;
            end
            else begin
                scs5_900k_seg = 20;
                scs5_900k_mod = re_index[7:0] - 16;
            end
        4'd15:
            if (re_index[7:0] < 120) begin
                scs5_900k_seg = 21;
                scs5_900k_mod = re_index[7:0] + 60;
            end
            else begin
                scs5_900k_seg = 22;
                scs5_900k_mod = re_index[7:0] - 120;
            end
    endcase
end

// output
always @(*) begin
    case (scs) begin
        2'd0: begin
            seg_900k = 0;
            mod_900k = 0;
        end
        2'd1: begin
            seg_900k = {4'd0, scs5_900k_seg};
            mod_900k = scs5_900k_mod;
        end
        2'd2: begin
            seg_900k = {2'd0, scs15_900k_seg};
            mod_900k = {2'd0, scs15_900k_mod};
        end
        2'd3: begin
            seg_900k = {1'd0, scs30_900k_seg};
            mod_900k = {3'd0, scs30_900k_mod};
        end
    endcase
end

endmodule
