
module adc_reg {
    // bus
    input bus_rd,
    input bus_wr,
    input [3:0] bus_bsel,
    input [5:0] bus_addr,
    input [31:0] bus_wdata,
    output reg [31:0] bus_rdata,
    // reg
    output reg [1:0] adc_clk_sel,
    output reg [2:0] adc_ch_sel,
    output reg [2:0] adc_mode,
    output reg adc_en,
    output reg [8:0] tmr_ovfl_en,
    output reg cont_mode,
    output reg sw_start,
    output reg awd_en,
    output reg fifo_ovfl_en,
    output reg fifo_hi_en,
    output reg eoc_en,
    input awd_state,
    input fifo_ovfl_state,
    input fifo_hi_state,
    input eoc_state,
    output reg fifo_reset,
    input [3:0] fifo_items,
    output reg [3:0] fifo_waterlevel,
    input [31:0] fifo data port,
    output reg [11:0] awd_hi,
    output reg [11:0] awd_lo,
    output reg [31:0] ana_ctrl
);
// reg_offset: 0, reg_name: ADC_CR1
always @(posedge clk or negedge rstn)
    if (~rstn) begin
        adc_clk_sel <= 2'h0;
        adc_ch_sel <= 3'h0;
        adc_mode <= 3'h0;
        adc_en <= 1'h0;
    end
    else if (bus_sel && bus_wr && bus_addr == 0) begin
        if (bus_bsel[3]) begin
            adc_clk_sel[1:0] <= bus_wdata[25:24];
        end
        if (bus_bsel[2]) begin
            adc_ch_sel[2:0] <= bus_wdata[18:16];
        end
        if (bus_bsel[1]) begin
            adc_mode[2:0] <= bus_wdata[10:8];
        end
        if (bus_bsel[0]) begin
            adc_en <= bus_wdata[0];
        end
    end
// reg_offset: 4, reg_name: ADC_CR2
always @(posedge clk or negedge rstn)
    if (~rstn) begin
        tmr_ovfl_en <= 9'h0;
        cont_mode <= 1'h0;
        sw_start <= 1'h0;
    end
    else if (bus_sel && bus_wr && bus_addr == 1) begin
        if (bus_bsel[2]) begin
            tmr_ovfl_en[7:0] <= bus_wdata[23:16];
        end
        if (bus_bsel[1]) begin
            cont_mode <= bus_wdata[8];
        end
        if (bus_bsel[0]) begin
            sw_start <= bus_wdata[0];
        end
    end
// reg_offset: 10, reg_name: ADC_IE
always @(posedge clk or negedge rstn)
    if (~rstn) begin
        awd_en <= 1'h0;
        fifo_ovfl_en <= 1'h0;
        fifo_hi_en <= 1'h0;
        eoc_en <= 1'h0;
    end
    else if (bus_sel && bus_wr && bus_addr == 4) begin
        if (bus_bsel[0]) begin
            awd_en <= bus_wdata[3];
            fifo_ovfl_en <= bus_wdata[2];
            fifo_hi_en <= bus_wdata[1];
            eoc_en <= bus_wdata[0];
        end
    end
// reg_offset: 14, reg_name: ADC_STATE
// reg_offset: 20, reg_name: ADC_FIFO
always @(posedge clk or negedge rstn)
    if (~rstn) begin
        fifo_reset <= 1'h0;
        fifo_waterlevel <= 4'h0;
    end
    else if (bus_sel && bus_wr && bus_addr == 8) begin
        if (bus_bsel[2]) begin
            fifo_reset <= bus_wdata[16];
        end
        if (bus_bsel[0]) begin
            fifo_waterlevel[3:0] <= bus_wdata[3:0];
        end
    end
// reg_offset: 24, reg_name: ADC_DATA
// reg_offset: 30, reg_name: ADC_AWD
always @(posedge clk or negedge rstn)
    if (~rstn) begin
        awd_hi <= 12'h0;
        awd_lo <= 12'h0;
    end
    else if (bus_sel && bus_wr && bus_addr == 12) begin
        if (bus_bsel[3]) begin
            awd_hi[11:8] <= bus_wdata[27:24];
        end
        if (bus_bsel[2]) begin
            awd_hi[7:0] <= bus_wdata[23:16];
        end
        if (bus_bsel[1]) begin
            awd_lo[11:8] <= bus_wdata[11:8];
        end
        if (bus_bsel[0]) begin
            awd_lo[7:0] <= bus_wdata[7:0];
        end
    end
// reg_offset: 40, reg_name: ADC_ANA
always @(posedge clk or negedge rstn)
    if (~rstn) begin
        ana_ctrl <= 32'h0;
    end
    else if (bus_sel && bus_wr && bus_addr == 16) begin
        if (bus_bsel[3]) begin
            ana_ctrl[31:24] <= bus_wdata[31:24];
        end
        if (bus_bsel[2]) begin
            ana_ctrl[23:16] <= bus_wdata[23:16];
        end
        if (bus_bsel[1]) begin
            ana_ctrl[15:8] <= bus_wdata[15:8];
        end
        if (bus_bsel[0]) begin
            ana_ctrl[7:0] <= bus_wdata[7:0];
        end
    end
// bus_rdata
always @(*) begin
    // default
    bus_rdata = 0
    // rdata_mux
    case(bus_addr)
        0: begin
            bus_rdata[25:24] = adc_clk_sel[1:0];
            bus_rdata[18:16] = adc_ch_sel[2:0];
            bus_rdata[10:8] = adc_mode[2:0];
            bus_rdata[0] = adc_en;
        end
        1: begin
            bus_rdata[24:16] = tmr_ovfl_en[8:0];
            bus_rdata[8] = cont_mode;
            bus_rdata[0] = sw_start;
        end
        4: begin
            bus_rdata[3] = awd_en;
            bus_rdata[2] = fifo_ovfl_en;
            bus_rdata[1] = fifo_hi_en;
            bus_rdata[0] = eoc_en;
        end
        5: begin
            bus_rdata[3] = awd_state;
            bus_rdata[2] = fifo_ovfl_state;
            bus_rdata[1] = fifo_hi_state;
            bus_rdata[0] = eoc_state;
        end
        8: begin
            bus_rdata[16] = fifo_reset;
            bus_rdata[11:8] = fifo_items[3:0];
            bus_rdata[3:0] = fifo_waterlevel[3:0];
        end
        9: begin
            bus_rdata[31:0] = fifo data port[31:0];
        end
        12: begin
            bus_rdata[27:16] = awd_hi[11:0];
            bus_rdata[11:0] = awd_lo[11:0];
        end
        16: begin
            bus_rdata[31:0] = ana_ctrl[31:0];
        end
        default: bus_rdata = 0;
    endcase
end

endmodule

