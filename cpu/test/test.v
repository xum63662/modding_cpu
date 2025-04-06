`timescale 1ps/1ps
// `include "../core/core.v"
`include "../core/LU.v"

module tb ();
  // reg clk,reset;
  // reg [31:0] code;
  // reg [23:0] PC;
  // Core core(clk,reset,code,PC);

  reg [31:0] A,B;
  reg [3:0] mode;
  wire [31:0] Y;
  FPU_float floatFPU(.A(A), .B(B), .mode(mode), .Y(Y),.ZF(),.NF());


  initial begin
    mode = 4'b0001;
            
    A = 32'b01000111110000110101000000000000;
    B = 32'b01000010110010000000000000000000;
    #50;
  end
  initial begin
    $dumpfile("test.vcd");
    $dumpvars();
  end
endmodule

// 00111111011000010100011110101110
// 01000000011000010100011110101110