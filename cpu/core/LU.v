module ALU (input [63:0] A,B, input [3:0] mode,output reg [63:0] out,output reg ZeroFlag,NF);
  initial
  begin
    out = 64'h0;
    ZeroFlag = 0;
    NF = 0;
  end
  always @(A or B or mode)
  begin
    if(mode == 4'b0000)
    begin // and
      out = A & B;
    end
    else if(mode == 4'b0001)
    begin//or
      out = A | B;
    end
    else if(mode == 4'b0010)
    begin//xor
      out = A ^ B;
    end
    else if(mode == 4'b0011)
    begin//add
      out = A + B;
    end
    else if(mode == 4'b0100)
    begin//sub
      out = A - B;
      if(out == 0)
      begin
        ZeroFlag = 'b1;
        NF = 'b0;
      end
      else if(out < 0)
      begin
        NF = 'b1;
        ZeroFlag = 'b0;
      end
      else
      begin
        NF = 0;
        ZeroFlag = 0;
      end
    end
    else if(mode == 4'b0101)
    begin//mul
      out = A * B;
    end
    else if(mode == 4'b0110)
    begin//div
      out = A / B;
    end
  end

endmodule


module FPU_float (input [31:0] A, B, input [3:0] mode, output reg [31:0] Y, output ZF,NF);
  reg A_S,B_S;//符號位
  reg out_S;
  reg signed [7:0] A_E,B_E;//指數位(x-127)
  reg signed [7:0] out_E;
  reg unsigned [23:0] A_F,B_F,out_F;//底數位
  integer offset,i;//數字
  reg [3:0] PB,temp_DIV;//保護位(Protection bit,PB)
  //乘法
  integer signed A_point,B_point,total_point,check,offset_point;

  //ALU
  reg [63:0] ALU_A,ALU_B;
  reg [63:0] ALU_out;
  //除法
  integer A_top,B_top,A_lower,B_lower,ALU_top,ALU_lower;

  /*command mode
        4'b0000:加法
        4'b0001:減法
        4'b0010:乘法
        4'b0011:除法
        4'b0100:比較
  */

  initial
  begin
    PB = 4'h0;
  end
  always @(A or B or mode)
  begin
    PB =4'h0;
    if(mode == 4'b0000 || mode == 4'b0001)
    begin//加、減法
      A_E = A[30:23] - 127;
      B_E = B[30:23] - 127;
      A_F = {1'b1,A[22:0]};
      B_F = {1'b1,B[22:0]};
      A_S = A[31];
      B_S = B[31];
      //對齊
      if(A_E > B_E)
      begin
        offset = A_E - B_E;
        out_E = A_E;
        for(i = 0;i < offset; i = i + 1)
        begin
          PB = PB >>> 1;
          PB[3] = B_F[0];
          B_F = B_F >>> 1;
        end
      end
      else if(B_E > A_E)
      begin
        offset = B_E - A_E;
        out_E = B_E;
        for (i = 0;i < offset;i = i + 1)
        begin
          PB = PB >>> 1;
          PB[3] = A_F[0];
          A_F = A_F >>> 1;
        end
      end
      else
      begin
        offset = 0;
      end
      //加法
      if(mode == 4'b0000)
      begin
        ALU_out = A_F+B_F;
      end
      else if(mode == 4'b0001)
      begin
        ALU_out = A_F-B_F;
      end
      #1;
      out_F = ALU_out[24:0];
      //規格化
      while(out_F[23] != 1'b1 || out_F[24] == 1'b1)
      begin
        if(out_F[24] == 1'b1)
        begin
          PB = PB >>> 1;
          PB[3] = out_F[0];
          out_F = out_F >>> 1;
          out_E = out_E + 1;
        end
        else if(out_F[23] == 1'b0)
        begin
          out_F = out_F <<< 1;
          out_E = out_E - 1;
        end
      end
      //捨入(就近捨入)
      if(PB == 4'b1000 || PB > 4'b1000)
      begin
        if(out_F[0] ==1'b1 || PB > 4'b1000)
        begin
          out_F = out_F + 1;
        end
      end
      out_E = out_E + 127;
      Y = {A_S | B_S,out_E,out_F[22:0]};
      $display("A_S = %b | B_S = %b\n Y = %b\n",A_S,B_S,Y);
    end



    else if(mode == 4'b0010 )
    begin//乘法
      A_E = A[30:23] - 127;
      B_E = B[30:23] - 127;
      A_F = {1'b1,A[22:0]};
      B_F = {1'b1,B[22:0]};
      A_S = A[31];
      B_S = B[31];

      
      out_E = A_E + B_E;


      $display("A_E = %b | B_E = %b | out_E = %b\n out_E+127= %b \n",A_E,B_E,out_E,out_E+127);
      A_point = 23;
      B_point = 23;
      while(A_F[A_point] == 1'b0)
      begin
        A_point = A_point - 1;
      end
      while(B_F[B_point] == 1'b0)
      begin
        B_point = B_point - 1;
      end
      total_point = (A_point + B_point);
      ALU_out = A_F * B_F;
      $display("raw_out = %b\n",ALU_out);
      check = 63;
      while(ALU_out[check] == 1'b0)
      begin
        check = check - 1;
      end
      if(check > total_point)
      begin
        offset = check - total_point;
        if(offset > 0)
        begin
          for(i = 0;i < offset;i = i + 1)
          begin
            PB = PB >>> 1;
            PB[3] = ALU_out[0];
            ALU_out = ALU_out >>> 1;
            out_E = out_E + 1;
          end
        end
      end

      if(check < total_point)
      begin
        offset = total_point - check;
        if(offset >0)
        begin
          for(i = 0;i < offset;i = i + 1)
          begin
            ALU_out = ALU_out <<< 1;
            out_E = out_E - 1;
          end
        end
      end
      $display("offset = %d\n ALU_out = %b",offset,ALU_out);
      for(i = total_point;i>23;i = i - 1)
      begin
        PB = PB >>> 1;
        PB[3] = ALU_out[0];
        ALU_out = ALU_out >>> 1;
      end
      out_F = ALU_out[23:0];
      $display("PB = %d\n out_F = %b\n",PB,out_F);
      if(PB >= 4'b1000 )
      begin
        if(out_F[0] == 1'b1 || PB > 4'b1000)
        begin
          out_F = out_F + 1;
        end
      end
      out_E = out_E + 127;
      out_S = A_S ^ B_S;
      Y = {out_S,out_E,out_F[22:0]};

      $display("A_S = %b | B_S = %b\n Y = %b\n",A_S,B_S,Y);
      $display("A = %b | B = %b \n out = %b \n point = %d | check = %d\n A_point = %d | B_point = %d\n E = %b",A_F,B_F,out_F,total_point,check,A_point,B_point,out_E);
    end
    else if(mode == 4'b0011)begin
      A_E = A[30:23] - 127;
      B_E = B[30:23] - 127;
      A_F = {1'b1,A[22:0]};
      B_F = {1'b1,B[22:0]};
      A_S = A[31];
      B_S = B[31];

      
      out_E = A_E - B_E;
      // //對齊
      // while(B_F[0] == 1'b0)begin
      //   B_F = B_F >>> 1;
      // end
      B_top = 63;
      ALU_A = A_F;
      ALU_B = B_F;
      while(ALU_B[B_top] == 1'b0)begin
        B_top = B_top - 1;
      end
      B_top = B_top + 1;
      $display("B_top = %d\n",B_top); 
      temp_DIV = A_F / B_F;
      for(i = 0;i<B_top;i = i + 1)begin  
        ALU_A = ALU_A <<< 1;             
      end
      ALU_out = ALU_A / ALU_B;
      $display("A_F = %b \n B_F = %b\n ALU_A = %b \n ALU_B = %b \n ALU_out = %b \n temp_DIV = %b",A_F,B_F,ALU_A,ALU_B,ALU_out,temp_DIV);
      ALU_top = 63;
      while(ALU_out[ALU_top] == 1'b0)begin
        ALU_top = ALU_top - 1;
      end
      // ALU_top = ALU_top + 1;
      ALU_out = ALU_out >>> 1;

      if(ALU_top > 24)begin
        offset = ALU_top - 24;
        for(i = offset;i > 0;i = i - 1)begin
          PB = PB >>> 1;
          PB[3] = ALU_out[0];
          ALU_out = ALU_out >>> 1;
          out_E = out_E - 1;
        end
      end
      else if(ALU_top < 24)begin
        offset = 24 - ALU_top;
        for(i = offset;i > 0;i = i - 1)begin
          ALU_out = ALU_out <<< 1;
          out_E = out_E - 1;
        end
      end
      if(PB >= 4'b1000)begin
        if(ALU_out[0] == 1'b1 || PB > 4'b1000)begin
          ALU_out = ALU_out + 1;
        end
      end
      PB = 4'b0000;
      out_F[23:0] = ALU_out[23:0];
      
      $display("ALU_top = %d | A_E = %d | B_E = %d | out_E = %d\n out_E+127= %d \n",ALU_top,A_E,B_E,out_E,out_E+127);
      out_E = out_E + 127;
      Y = {A_S ^ B_S,out_E,out_F[22:0]};
      $display("Y = %b\n",Y); 
    
    end
  end
endmodule
