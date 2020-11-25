
module adc_reg {
    // bus
    input bus_rd,
    input bus_wr,
    input [3:0] bus_bsel,
    input [5:0] bus_addr,
    input [31:0] bus_wdata,
    output reg [31:0] bus_rdata,
    // reg
    input [4:0] cte_len,
    output [4:0] cte_len_clr,
    output reg cte_type,
    output reg cte_enable,
    output reg aod_enable,
    output reg [22:0] pkt_len,
    output reg [1:0] agc_win,
    output reg second_agc_enable,
    output reg pintracking_enable,
    output reg agc_timeout_enable,
    output reg agc_disable
);
// reg_offset: 8f47, reg_name: aod_ctrl
always @(posedge clk or negedge rstn)
    if (~rstn) begin
        cte_type <= 1'h0;
        cte_enable <= 1'h0;
        aod_enable <= 1'h0;
    end
    else if (bus_sel && bus_wr && bus_addr == 9169) begin
        if (bus_bsel[0]) begin
            cte_type <= bus_wdata[2];
            cte_enable <= bus_wdata[1];
            aod_enable <= bus_wdata[0];
        end
    end
// clr
assign cte_len_clr[4] = bus_sel && bus_wr && bus_addr == 9169 && bus_bsel[0] && bus_wdata[7];
assign cte_len_clr[3] = bus_sel && bus_wr && bus_addr == 9169 && bus_bsel[0] && bus_wdata[6];
assign cte_len_clr[2] = bus_sel && bus_wr && bus_addr == 9169 && bus_bsel[0] && bus_wdata[5];
assign cte_len_clr[1] = bus_sel && bus_wr && bus_addr == 9169 && bus_bsel[0] && bus_wdata[4];
assign cte_len_clr[0] = bus_sel && bus_wr && bus_addr == 9169 && bus_bsel[0] && bus_wdata[3];
// reg_offset: 8948, reg_name: pkt_len
always @(posedge clk or negedge rstn)
    if (~rstn) begin
        pkt_len <= 23'h0;
    end
    else if (bus_sel && bus_wr && bus_addr == 8786) begin
        if (bus_bsel[3]) begin
            pkt_len[22:21] <= bus_wdata[25:24];
        end
        if (bus_bsel[2]) begin
            pkt_len[20:13] <= bus_wdata[23:16];
        end
        if (bus_bsel[1]) begin
            pkt_len[12:5] <= bus_wdata[15:8];
        end
        if (bus_bsel[0]) begin
            pkt_len[4:0] <= bus_wdata[7:3];
        end
    end
// reg_offset: 8960, reg_name: agc_ctrl
always @(posedge clk or negedge rstn)
    if (~rstn) begin
        agc_win <= 2'h2;
        second_agc_enable <= 1'h0;
        pintracking_enable <= 1'h1;
        agc_timeout_enable <= 1'h1;
        agc_disable <= 1'h0;
    end
    else if (bus_sel && bus_wr && bus_addr == 8792) begin
        if (bus_bsel[0]) begin
            agc_win[1:0] <= bus_wdata[5:4];
            second_agc_enable <= bus_wdata[3];
            pintracking_enable <= bus_wdata[2];
            agc_timeout_enable <= bus_wdata[1];
            agc_disable <= bus_wdata[0];
        end
    end
// bus_rdata
always @(*) begin
    // default
    bus_rdata = 0
    // rdata_mux
    case(bus_addr)
        9169: begin
            bus_rdata[7:3] = cte_len[4:0];
            bus_rdata[2] = cte_type;
            bus_rdata[1] = cte_enable;
            bus_rdata[0] = aod_enable;
        end
        8786: begin
            bus_rdata[25:3] = pkt_len[22:0];
        end
        8792: begin
            bus_rdata[5:4] = agc_win[1:0];
            bus_rdata[3] = second_agc_enable;
            bus_rdata[2] = pintracking_enable;
            bus_rdata[1] = agc_timeout_enable;
            bus_rdata[0] = agc_disable;
        end
        default: bus_rdata = 0;
    endcase
end

endmodule

