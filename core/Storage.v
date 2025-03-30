//X0 - X31

module Registers (read1,read2,writeReg,writeData,CONTROL_REGWRITE,data1,data2);

    input [5:0] read1,read2,writeReg;
    input [63:0] writeData;
    input CONTROL_REGWRITE;
    output reg [63:0] data1,data2;

    reg [63:0] data [31:0];

    integer initCount;

    initial begin
        for(initCount=0;initCount<31;initCount = initCount + 1)begin
            data[initCount] = initCount;
        end

        data[31] = 64'h00000000;
    end

    always @(read1,read2,writeData,writeReg,CONTROL_REGWRITE) begin
        data1 = data[read1];
        data2 = data[read2];
    end
    
endmodule

module Data_Memory
(
  input [63:0] inputAddress,
  input [63:0] inputData,
  input CONTROL_MemRead,
  input CONTROL_MemWrite,
  output reg [63:0] outputData
);

  reg [63:0] Data[31:0];

  integer initCount;

  initial begin
    for (initCount = 0; initCount < 32; initCount = initCount + 1) begin
      Data[initCount] = initCount * 100;
    end

   Data[10] = 1540;
   Data[11] = 2117;
  end

    always @(inputAddress, inputData, CONTROL_MemRead, CONTROL_MemWrite) begin
      if (CONTROL_MemWrite == 1) begin
        Data[inputAddress] = inputData;
      end

      if (CONTROL_MemRead == 1) begin
        outputData = Data[inputAddress];
      end
    end
endmodule