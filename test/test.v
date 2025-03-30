`timescale 1ns / 1ps

module pipeline_add_tb;

    // 测试输入信号
    reg clk;
    reg [31:0] operand1;
    reg [31:0] operand2;

    // 输出信号
    wire [31:0] result;

    // 实例化 pipeline_add 模块
    pipeline_add uut (
        .clk(clk),
        .operand1(operand1),
        .operand2(operand2),
        .result(result)
    );

    // 初始化时钟信号
    always begin
        #5 clk = ~clk; // 时钟周期为 10ns，周期反转
    end

    // 初始化输入信号
    initial begin
        // 初始化时钟信号
        clk = 0;

        // 初始化操作数
        operand1 = 32'd15;  // operand1 = 15
        operand2 = 32'd10;  // operand2 = 10

        // 等待几时钟周期后查看结果
        #50;
        
        // 更改输入操作数，测试不同值
        operand1 = 32'd50;  // operand1 = 50
        operand2 = 32'd30;  // operand2 = 30

        // 等待一些时钟周期后查看结果
        #50;

        // 结束仿真
        $finish;
    end

    // 监控输出信号
    initial begin
        $monitor("At time %t, operand1 = %d, operand2 = %d, result = %d", $time, operand1, operand2, result);
        $dumpfile("test.vcd");
        $dumpvars();
    end

endmodule

module pipeline_add (
    input clk,
    input [31:0] operand1,   // 第一个操作数
    input [31:0] operand2,   // 第二个操作数
    output reg [31:0] result // 加法结果
);
    reg [31:0] IF_ID, ID_EX, EX_MEM, MEM_WB;  // 五个流水线寄存器

    always @(posedge clk) begin
        IF_ID <= operand1 + operand2;  // IF 阶段获取指令
        ID_EX <= IF_ID;                // ID 阶段解码
        EX_MEM <= ID_EX;               // EX 阶段执行
        MEM_WB <= EX_MEM;              // WB 阶段写回结果
    end

    always @(posedge clk) begin
        result <= MEM_WB; // 最终结果来自 WB 阶段
    end
endmodule