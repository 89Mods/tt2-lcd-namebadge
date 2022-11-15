`default_nettype none
`timescale 1ns/1ps

module tb (
	input CLK,
	input RST,
	output RS,
	output E,
	output [3:0] dout,
	output LED
	);
	
	initial begin
		$dumpfile ("tb.vcd");
		$dumpvars (0, tb);
		#1;
	end
	
	wire [7:0] inputs = {RST, CLK};
	wire [7:0] outputs;
	assign RS = outputs[0];
	assign E = outputs[1];
	assign dout = outputs[5:2];
	assign LED = outputs[6];
	
	tt2_tholin_namebadge tt2_tholin_namebadge (
		`ifdef GL_TEST
			.vccd1( 1'b1),
			.vssd1( 1'b0),
		`endif
		.io_in (inputs),
		.io_out (outputs)
	);
endmodule
