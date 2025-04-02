module PC (input clk,input [23:0] jump,input[23:0] old_PC,output reg [23:0] next_PC);
    initial begin
        next_PC[23:0] = 24'h0;
    end
    always @(posedge clk) begin
        next_PC = old_PC;
    end
endmodule

module Core (input clk,input write_enable);
    reg IF,ID,EX,MEM,WB;
    initial begin
        IF = 1;
        ID = 0;
        EX = 0;
        MEM =0;
        WB = 0;
    end
    always @(posedge clk) begin
        if(write_enable)begin
            ID = IF;
            EX = ID;
            MEM = EX;
            WB = MEM; 
        end

    end
endmodule