`timescale 1ns / 1ps

module DFF(
    output q,
    output qBar,
    input d,
    input clk,
    input resetBar
    );

wire tmp0;
wire tmp1;
wire tmp2;
wire tmp3;
assign tmp3 = ~(resetBar & clk);
assign tmp2 = ~(resetBar & ~(tmp1 & ~(d & tmp0)));
assign tmp1 = ~(~tmp2 & tmp3);
assign tmp0 = ~(tmp2 & tmp3);
assign qBar = ~(tmp0 & q);
assign q = ~(tmp1 & qBar);

endmodule
