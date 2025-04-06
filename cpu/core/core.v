`include "./LU.v"


module PC (input clk,input [23:0] jump,input[23:0] old_PC,output reg [23:0] next_PC);
  initial
  begin
    next_PC[23:0] = 24'h0;
  end
  always @(posedge clk)
  begin
    next_PC = old_PC;
  end
endmodule



module Core (input clk,reset,input [31:0] code,input [23:0] PC);

  //ALU,FLU
  reg [63:0] A;
  reg [3:0] ALU_mode,FLU_mode;
  wire [63:0] ALU_out;
  reg [63:0] B;
  reg [63:0] float_A;
  reg [63:0] float_B;
  reg [63:0] FLU_out;
  wire ZF,NF;

  ALU alu(.A(A),.B(B),.mode(ALU_mode),.out(ALU_out),.ZeroFlag(ZF),.NF(NF));


  reg [31:0] IF,ID,EX,MEM,WB;
  initial
  begin
    IF = 32'h0;
    ID = 32'h0;
    EX = 32'h0;
    MEM =32'h0;
    WB = 32'h0;
  end
  //IF
  always @(posedge clk or posedge reset)
  begin
    if(reset)
    begin
      IF = 32'h0;
    end
    else
    begin
      IF <= code;
    end

  end
  //ID
  always @(posedge clk or posedge reset)
  begin
    if(reset)
    begin
      ID = 32'h0;
    end
    else
    begin
      ID <= IF;

    end
  end
  //EX
  always @(posedge clk or posedge reset)
  begin
    if(reset)
    begin
      EX = 32'h0;
    end
    else
    begin
      EX <= ID;
    end
  end
  //MEM
  always @(posedge clk or posedge reset)
  begin
    if(reset)
    begin
      MEM = 32'h0;
    end
    else
    begin
      MEM <= EX;
    end
  end

  //WB
  always @(posedge clk or posedge reset)
  begin
    if(reset)
    begin
      WB = 32'h0;
    end
    else
    begin
      WB<= MEM;
    end
  end
endmodule
