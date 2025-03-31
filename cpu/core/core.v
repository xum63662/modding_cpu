module core (CLK,command);
    input CLK;

    input [31:0] command; 

    reg[10:0] OP;
    
    decode decoder(.command(ID));

    reg [31:0] IF,ID,EX,WB;

    always @(posedge CLK) begin
        IF <= command;
        ID <= IF;

    end
    
endmodule

module decode (input [31:0] command);
    always @(command) begin
        if(command[31:26] == 6'b000101)begin //B
            
        end
    end
endmodule

module PC (input clk,JUMP,input [31:0] oldPC,shiftPC,output reg [31:0] outPC);
    always @(posedge clk) begin
        if(JUMP == 'b0)begin
            outPC = oldPC + 4;    
        end
        else begin
            outPC = shiftPC;
        end
        
    end
endmodule

module ALU (
    mode,A,B,out,zeroflag
);

    input [3:0] mode;
    input [63:0] A,B;
    output reg [63:0] out;
    output reg zeroflag;
    

    always @(A or B or mode) begin
        case (mode)
            4'b0000: out = A & B;//and
            4'b0001: out = A | B;//or
            4'b0010: out = A + B;//add
            4'b0011: out = A - B;//sub
            4'b0100: out = B;
            4'b0101: out = A ^ B;
            4'b0110: out = A * B;
            4'b0111: out = A / B;
            4'b1000: out = A ** B;
        endcase
    end
endmodule

module ALU_compile (
);

    
    
endmodule