
module wokwi(input CLK, input RST, input EF0, input EF1, input EF2, output RS, output reg E, output D4, output D5, output D6, output D7);
    wire [6:0] rom_addr;
    reg[6:0] s_ROM;
        always @(*)
        begin
            case (rom_addr)
            0 : s_ROM = 7'h72;
            1 : s_ROM = 7'h65;
            2 : s_ROM = 7'h6b;
            3 : s_ROM = 7'h61;
            4 : s_ROM = 7'h4d;
            5 : s_ROM = 7'h20;
            6 : s_ROM = 7'h64;
            7 : s_ROM = 7'h6c;
            8 : s_ROM = 7'h72;
            9 : s_ROM = 7'h6f;
            10 : s_ROM = 7'h57;
            11 : s_ROM = 7'h20;
            12 : s_ROM = 7'h43;
            13 : s_ROM = 7'h52;
            14 : s_ROM = 7'h56;
            15 : s_ROM = 7'h76;
            16 : s_ROM = 7'h65;
            17 : s_ROM = 7'h44;
            18 : s_ROM = 7'h20;
            19 : s_ROM = 7'h65;
            20 : s_ROM = 7'h72;
            21 : s_ROM = 7'h61;
            22 : s_ROM = 7'h77;
            23 : s_ROM = 7'h64;
            24 : s_ROM = 7'h72;
            25 : s_ROM = 7'h61;
            26 : s_ROM = 7'h48;
            27 : s_ROM = 7'h76;
            28 : s_ROM = 7'h65;
            29 : s_ROM = 7'h44;
            30 : s_ROM = 7'h20;
            31 : s_ROM = 7'h65;
            32 : s_ROM = 7'h72;
            33 : s_ROM = 7'h61;
            34 : s_ROM = 7'h77;
            35 : s_ROM = 7'h74;
            36 : s_ROM = 7'h66;
            37 : s_ROM = 7'h6f;
            38 : s_ROM = 7'h53;
            39 : s_ROM = 7'h69;
            40 : s_ROM = 7'h6c;
            41 : s_ROM = 7'h61;
            42 : s_ROM = 7'h76;
            43 : s_ROM = 7'h41;
            44 : s_ROM = 7'h76;
            45 : s_ROM = 7'h65;
            46 : s_ROM = 7'h64;
            47 : s_ROM = 7'h2e;
            48 : s_ROM = 7'h6e;
            49 : s_ROM = 7'h69;
            50 : s_ROM = 7'h6c;
            51 : s_ROM = 7'h6f;
            52 : s_ROM = 7'h68;
            53 : s_ROM = 7'h74;
            54 : s_ROM = 7'h2e;
            55 : s_ROM = 7'h77;
            56 : s_ROM = 7'h77;
            57 : s_ROM = 7'h77;
            58 : s_ROM = 7'h33;
            59 : s_ROM = 7'h3a;
            60 : s_ROM = 7'h20;
            61 : s_ROM = 7'h6e;
            62 : s_ROM = 7'h69;
            63 : s_ROM = 7'h6c;
            64 : s_ROM = 7'h6f;
            65 : s_ROM = 7'h68;
            66 : s_ROM = 7'h54;
            67 : s_ROM = 7'h20;
            68 : s_ROM = 7'h6d;
            69 : s_ROM = 7'h27;
            70 : s_ROM = 7'h49;
            71 : s_ROM = 7'h20;
            72 : s_ROM = 7'h2c;
            73 : s_ROM = 7'h69;
            74 : s_ROM = 7'h48;
            75 : s_ROM = 7'h20;
            default : s_ROM = 0;
        endcase
    end
    assign rom_addr = str_seq;

    reg toggle = 1'b0;
    reg [7:0] seq = 8'h0;
    reg [6:0] str_seq = 75;
    reg [4:0] data;
    reg round = 0;
    wire [1:0] res;
    assign res = EF0 + EF1 + EF2;

    assign {RS, D7, D6, D5, D4} = data;
    
    always @(posedge CLK) begin
        if(RST) begin
            toggle <= 1'b0;
            seq = 0;
            str_seq <= 75;
        end
        toggle <= !toggle;
        if (toggle) begin
            seq <= seq + 1'b1;
            E <= 1'b0;
            if (seq > 5) begin
                if (round) begin
                    if (seq <= 15) begin
                        data <= (1 << 4) | ((seq & 1) ? s_ROM[3:0] : s_ROM[6:4]);
                        str_seq <= str_seq - (seq & 1);
                    end else if(seq <= 47) begin
                        data <= (seq & 1) ? 5'b00100 : 5'b01001;
                    end else if(seq <= 71) begin
                        data <= (1 << 4) | ((seq & 1) ? s_ROM[3:0] : s_ROM[6:4]);
                        str_seq <= str_seq - (seq & 1);
                    end else if(seq <= 103) begin
                        data <= (seq & 1) ? 5'b00000 : 5'b01100;
                    end else if(seq <= 127) begin
                        data <= (1 << 4) | ((seq & 1) ? s_ROM[3:0] : s_ROM[6:4]);
                        str_seq <= str_seq - (seq & 1);
                    end else if(seq <= 159) begin
                        data <= (seq & 1) ? 5'b00100 : 5'b01001;
                    end else if(seq <= 189) begin
                        data <= (1 << 4) | ((seq & 1) ? s_ROM[3:0] : s_ROM[6:4]);
                        str_seq <= str_seq - (seq & 1);
                    end else begin
                        data <= 5'b00011;
                        str_seq <= 75;
                    end
                end else begin
                    if (seq <= 41) begin
                        data <= (1 << 4) | ((seq & 1) ? s_ROM[3:0] : s_ROM[6:4]);
                        str_seq <= str_seq - (seq & 1);
                    end else if (seq <= 63) begin
                        data <= (seq & 1) ? 5'b00100 : 5'b01101;
                    end else if (seq <= 91) begin
                        data <= (1 << 4) | ((seq & 1) ? s_ROM[3:0] : s_ROM[6:4]);
                        str_seq <= str_seq - (seq & 1);
                    end else if(seq <= 97) begin
                        data <= (1 << 4) | ((seq & 1) ? 0 : 2);
                    end else if(seq <= 101) begin
                        data <= (1 << 4) | ((seq & 1) ? res[seq[1]] : 3);
                    end else begin
                        data <= 5'b00011;
                    end
                end
                if (seq == 255) begin
                    round <= !round;
                end
            end else
                if (round) begin
                    case(seq)
                        // Switch to 4 bit mode
                        0 : data <= 5'b00011;
                        1 : data <= 5'b00010;

                        // Display on
                        2 : data <= 5'b00000;
                        3 : data <= 5'b01111;

                        // Put cursor on line 2
                        4 : data <= 5'b01100;
                        5 : data <= 5'b00000;
                    endcase
                end else begin
                    case(seq)
                        // Switch to 4 bit mode
                        0 : data <= 5'b00011;
                        1 : data <= 5'b00010;

                        // Display on
                        2 : data <= 5'b00000;
                        3 : data <= 5'b01111;

                        // Clear display
                        4 : data <= 5'b00000;
                        5 : data <= 5'b00001;
                    endcase
                end
            end
        else begin
            E <= 1'b1;
        end
    end
endmodule
