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
        endcase
    end
endmodule

module ALU_compile (
);

    
    
endmodule