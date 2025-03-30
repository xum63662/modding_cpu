module core (CLK,command);
    input CLK;

    input [63:0] command; 

    reg[10:0] OP;
    
    

    reg [63:0] IF,ID,EX,WB;

    always @(posedge CLK) begin
        IF <= command;
        ID <= IF;
    end
    
endmodule