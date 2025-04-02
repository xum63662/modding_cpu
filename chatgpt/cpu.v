module cpu (
    input clk,
    input reset
);
    // ---------------------------- 流水线寄存器 ---------------------------- //
    reg [31:0] PC, IF_ID_PC, ID_EX_PC, EX_MEM_PC, MEM_WB_PC;
    reg [31:0] IF_ID_IR, ID_EX_IR, EX_MEM_IR, MEM_WB_IR;  // 指令寄存器

    // ---------------------------- 寄存器文件 ---------------------------- //
    reg [31:0] register_file [31:0];  // 32 个寄存器
    wire [31:0] read_data1, read_data2;
    wire [4:0] rs, rt, rd;
    assign rs = ID_EX_IR[25:21];
    assign rt = ID_EX_IR[20:16];
    assign rd = ID_EX_IR[15:11];

    // ---------------------------- 指令提取 ---------------------------- //
    // IF 阶段：指令从内存中获取
    always @(posedge clk or posedge reset) begin
        if (reset) begin
            PC <= 0;
            IF_ID_PC <= 0;
            IF_ID_IR <= 32'b0;
        end else begin
            IF_ID_PC <= PC;
            // IF_ID_IR <= instruction_memory[PC];  // 假设 instruction_memory 已定义
            PC <= PC + 4;
        end
    end

    // ---------------------------- 指令解码 ---------------------------- //
    // ID 阶段：解码并准备寄存器读取
    always @(posedge clk or posedge reset) begin
        if (reset) begin
            ID_EX_PC <= 0;
            ID_EX_IR <= 32'b0;
        end else begin
            ID_EX_PC <= IF_ID_PC;
            ID_EX_IR <= IF_ID_IR;
            // 读取寄存器数据
            // read_data1 <= register_file[rs];
            // read_data2 <= register_file[rt];
        end
    end

    // ---------------------------- 执行阶段 ---------------------------- //
    // EX 阶段：执行操作，例如算术运算或计算跳转地址
    always @(posedge clk or posedge reset) begin
        if (reset) begin
            EX_MEM_PC <= 0;
            EX_MEM_IR <= 32'b0;
        end else begin
            EX_MEM_PC <= ID_EX_PC;
            EX_MEM_IR <= ID_EX_IR;

            // 操作执行，这里以加法操作为例
            if (ID_EX_IR[31:26] == 6'b000000) begin
                // R型指令，执行加法
                // ALU_result <= read_data1 + read_data2; // ALU执行的结果
            end
        end
    end

    // ---------------------------- 内存访问 ---------------------------- //
    // MEM 阶段：访问内存，例如加载或存储
    always @(posedge clk or posedge reset) begin
        if (reset) begin
            MEM_WB_PC <= 0;
            MEM_WB_IR <= 32'b0;
        end else begin
            MEM_WB_PC <= EX_MEM_PC;
            MEM_WB_IR <= EX_MEM_IR;
            // 这里假设 MEM 操作是存储到内存
            if (EX_MEM_IR[31:26] == 6'b101011) begin
                // Store 指令，将数据写入内存
                // memory[EX_MEM_IR[15:0]] <= ALU_result;
            end
        end
    end

    // ---------------------------- 写回阶段 ---------------------------- //
    // WB 阶段：将数据写回到寄存器
    always @(posedge clk or posedge reset) begin
        if (reset) begin
            // Reset 写回寄存器
        end else begin
            // 只有当该指令需要写回数据时才进行
            if (MEM_WB_IR[31:26] == 6'b100011) begin
                // Load 指令，将数据从内存加载到寄存器
                // register_file[rd] <= memory[MEM_WB_IR[15:0]];
            end
        end
    end

    // ---------------------------- 数据转发与冒险检测 ---------------------------- //
    // 检测数据冒险并实现数据转发
    always @(posedge clk) begin
        if (ID_EX_IR[25:21] == EX_MEM_IR[15:11] && EX_MEM_IR[31:26] == 6'b000000) begin
            // 数据冒险检测，如果有 RAW hazard，则从 EXMEM 转发数据
            // read_data1 <= ALU_result;
        end
        if (ID_EX_IR[20:16] == EX_MEM_IR[15:11] && EX_MEM_IR[31:26] == 6'b000000) begin
            // 数据冒险检测，如果有 RAW hazard，则从 EXMEM 转发数据
            // read_data2 <= ALU_result;
        end
    end

endmodule