# _instruction.py

# Copyright [2023] Manjunath Srinivasa

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Legal Instructions by Name
#     ADC  add with carry
#     AND  and (with accumulator)
#     ASL  arithmetic shift left
#     BCC  branch on carry clear
#     BCS  branch on carry set
#     BEQ  branch on equal (zero set)
#     BIT  bit test
#     BMI  branch on minus (negative set)
#     BNE  branch on not equal (zero clear)
#     BPL  branch on plus (negative clear)
#     BRK  break / interrupt
#     BVC  branch on overflow clear
#     BVS  branch on overflow set
#     CLC  clear carry
#     CLD  clear decimal
#     CLI  clear interrupt disable
#     CLV  clear overflow
#     CMP  compare (with accumulator)
#     CPX  compare with X
#     CPY  compare with Y
#     DEC  decrement
#     DEX  decrement X
#     DEY  decrement Y
#     EOR  exclusive or (with accumulator)
#     INC  increment
#     INX  increment X
#     INY  increment Y
#     JMP  jump
#     JSR  jump subroutine
#     LDA  load accumulator
#     LDX  load X
#     LDY  load Y
#     LSR  logical shift right
#     NOP  no operation
#     ORA  or with accumulator
#     PHA  push accumulator
#     PHP  push processor status (SR)
#     PLA  pull accumulator
#     PLP  pull processor status (SR)
#     ROL  rotate left
#     ROR  rotate right
#     RTI  return from interrupt
#     RTS  return from subroutine
#     SBC  subtract with carry
#     SEC  set carry
#     SED  set decimal
#     SEI  set interrupt disable
#     STA  store accumulator
#     STX  store X
#     STY  store Y
#     TAX  transfer accumulator to X
#     TAY  transfer accumulator to Y
#     TSX  transfer stack pointer to X
#     TXA  transfer X to accumulator
#     TXS  transfer X to stack pointer
#     TYA  transfer Y to accumulator

# Illegal Instruction by Name
#     ALR
#     ANC
#     ANE
#     XAA
#     ARR
#     DCP
#     ISC
#     LAS
#     LAX
#     RLA
#     RRA
#     SAX
#     AXS
#     AAX
#     SBX
#     SHA
#     SHX
#     SHY
#     SLO
#     SRE
#     TAS
#     SBC
#     NOP
#     JAM

import json
from _status import set_status
from _addressing import addressing

class instruction:
    def __init__(self, registers, bus, clock):
        with open('opcodes.json') as f:
            self._opCodesDict = json.load(f)

        self._bus = bus
        self._registers = registers
        self._clock = clock
        self._setupOps()

    def run(self, opCode): 
        pc = self._registers["PC"].get()
        pc += 1
        self._registers["PC"].set(pc)
            
        try:
            self._opCodeDict = self._opCodesDict[opCode]
        except:
            raise Exception(f"{hex(opCode)} is an invalid opcode.")
        
        # Addressing mode
        self._data, self._memAddr = addressing(self._opCodeDict[addressing], self._registers, self._bus)

        # Run operation
        self._op[self._opCodeDict["instruction"]]
        
        # Update clock
        self._clock.tick(self._opCodeDict["cycles"])

    def _setupOps(self):
        # Legal instructions
        self._op["ADC"] = lambda: self._ADC()
        self._op["AND"] = lambda: self._AND()
        self._op["ASL"] = lambda: self._ASL()
        self._op["BCC"] = lambda: self._BCC()
        self._op["BCS"] = lambda: self._BCS()
        self._op["BEQ"] = lambda: self._BEQ()
        self._op["BIT"] = lambda: self._BIT()
        self._op["BMI"] = lambda: self._BMI()
        self._op["BNE"] = lambda: self._BNE()
        self._op["BPL"] = lambda: self._BPL()
        self._op["BRK"] = lambda: self._BRK()
        self._op["BVC"] = lambda: self._BVC()
        self._op["BVS"] = lambda: self._BVS()
        self._op["CLC"] = lambda: self._CLC()
        self._op["CLD"] = lambda: self._CLD()
        self._op["CLI"] = lambda: self._CLI()
        self._op["CLV"] = lambda: self._CLV()
        self._op["CMP"] = lambda: self._CMP()
        self._op["CPX"] = lambda: self._CPX()
        self._op["CPY"] = lambda: self._CPY()
        self._op["DEC"] = lambda: self._DEC()
        self._op["DEX"] = lambda: self._DEX()
        self._op["DEY"] = lambda: self._DEY()
        self._op["EOR"] = lambda: self._EOR()
        self._op["INC"] = lambda: self._INC()
        self._op["INX"] = lambda: self._INX()
        self._op["INY"] = lambda: self._INY()
        self._op["JMP"] = lambda: self._JMP()
        self._op["JSR"] = lambda: self._JSR()
        self._op["LDA"] = lambda: self._LDA()
        self._op["LDX"] = lambda: self._LDX()
        self._op["LDY"] = lambda: self._LDY()
        self._op["LSR"] = lambda: self._LSR()
        self._op["NOP"] = lambda: self._NOP()
        self._op["ORA"] = lambda: self._ORA()
        self._op["PHA"] = lambda: self._PHA()
        self._op["PHP"] = lambda: self._PHP()
        self._op["PLA"] = lambda: self._PLA()
        self._op["PLP"] = lambda: self._PLP()
        self._op["ROL"] = lambda: self._ROL()
        self._op["ROR"] = lambda: self._ROR()
        self._op["RTI"] = lambda: self._RTI()
        self._op["RTS"] = lambda: self._RTS()
        self._op["SBC"] = lambda: self._SBC()
        self._op["SEC"] = lambda: self._SEC()
        self._op["SED"] = lambda: self._SED()
        self._op["SEI"] = lambda: self._SEI()
        self._op["STA"] = lambda: self._STA()
        self._op["STX"] = lambda: self._STX()
        self._op["STY"] = lambda: self._STY()
        self._op["TAX"] = lambda: self._TAX()
        self._op["TAY"] = lambda: self._TAY()
        self._op["TSX"] = lambda: self._TSX()
        self._op["TXA"] = lambda: self._TXA()
        self._op["TXS"] = lambda: self._TXS()
        self._op["TYA"] = lambda: self._TYA()
        
        # Illegal instructions
        self._op["ALR"] = lambda: self._ALR()
        self._op["ANC"] = lambda: self._ANC()
        self._op["ANE"] = lambda: self._ANE() 
        self._op["XAA"] = lambda: self._XAA()
        self._op["ARR"] = lambda: self._ARR()
        self._op["DCP"] = lambda: self._DCP()
        self._op["ISC"] = lambda: self._ISC()
        self._op["LAS"] = lambda: self._LAS()
        self._op["LAX"] = lambda: self._LAX()
        self._op["RLA"] = lambda: self._RLA()
        self._op["RRA"] = lambda: self._RRA()
        self._op["SAX"] = lambda: self._SAX() 
        self._op["AXS"] = lambda: self._AXS()
        self._op["AAX"] = lambda: self._AAX()
        self._op["SBX"] = lambda: self._SBX()
        self._op["SHA"] = lambda: self._SHA()
        self._op["SHX"] = lambda: self._SHX() 
        self._op["SHY"] = lambda: self._SHY()
        self._op["SLO"] = lambda: self._SLO() 
        self._op["SRE"] = lambda: self._SRE()
        self._op["TAS"] = lambda: self._TAS()
        self._op["SBC"] = lambda: self._SBC()
        self._op["NOP"] = lambda: self._NOP()
        self._op["JAM"] = lambda: self._JAM()

    def _ADC(self):
        A = self._registers["AC"].get()
        C = self._registers["SR"].get_bit(0)
        result = A + self._data + C
        set_status(self._registers["SR"], self._opCodeDict["flags"], result)
        self._registers["AC"].set(result & 0xFF)
    
    def _AND(self):
        A = self._registers["AC"].get()
        result = A & self._data 
        set_status(self._registers["SR"], self._opCodeDict["flags"], result)
        self._registers["AC"].set(result & 0xFF)
    
    def _ASL(self):
        A = self._registers["AC"].get()
        result = A << 1
        set_status(self._registers["SR"], self._opCodeDict["flags"], result)
        if self._memAddr == "AC":
            self._registers["AC"].set(result & 0xFF)
        else:
            self._bus.set(result & 0xFF, self._memAddr)
    
    def _BCC(self):
        if not(self._registers["SR"].get_bit(0)):
            pc = self._registers["PC"].get()
            pc = (pc + self._data) & 0xFF
            self._registers["PC"].set(pc)
    
    def _BCS(self):
        if self._registers["SR"].get_bit(0):
            pc = self._registers["PC"].get()
            pc = (pc + self._data) & 0xFF
            self._registers["PC"].set(pc)
    
    def _BEQ(self):
        if self._registers["SR"].get_bit(1):
            pc = self._registers["PC"].get()
            pc = (pc + self._data) & 0xFF
            self._registers["PC"].set(pc)
    
    def _BIT(self):
        self._registers["SR"].set_bit(7, self._data >> 7)
        self._registers["SR"].set_bit(6, (self._data & 0x40) >> 6)
        
        if not(self._data & self._registers["AC"]):
            self._registers["SR"].set_bit(1, 1)
        else:
            self._registers["SR"].set_bit(1, 0)
    
    def _BMI(self):
        if self._registers["SR"].get_bit(7):
            pc = self._registers["PC"].get()
            pc = (pc + self._data) & 0xFF
            self._registers["PC"].set(pc)
    
    def _BNE(self):
        if not(self._registers["SR"].get_bit(1)):
            pc = self._registers["PC"].get()
            pc = (pc + self._data) & 0xFF
            self._registers["PC"].set(pc)
    
    def _BPL(self):
        if not(self._registers["SR"].get_bit(7)):
            pc = self._registers["PC"].get()
            pc = (pc + self._data) & 0xFF
            self._registers["PC"].set(pc)
    
    def _BRK(self):
        pc = self._registers["PC"].get()
        sp = self._register["SP"].get()
        self._bus.set((pc + 2) & 0x00FF, 0x0100 + sp)
        sp -= 1
        self._bus.set(((pc + 2) & 0xFF00) >> 8, 0x0100 + sp)
        sp -= 1
        set_status(self._registers["SR"], self._opCodeDict["flags"], 1)
        
        sr = self._registers["SR"].get()
        self._bus.set(sr, 0x0100 + sp)
        sp -= 1
        self._register["SP"].set(sp)
    
    def _BVC(self):
        if not(self._registers["SR"].get_bit(6)):
            pc = self._registers["PC"].get()
            pc = (pc + self._data) & 0xFF
            self._registers["PC"].set(pc)
    
    def _BVS(self):
        if self._registers["SR"].get_bit(6):
            pc = self._registers["PC"].get()
            pc = (pc + self._data) & 0xFF
            self._registers["PC"].set(pc)
    
    def _CLC(self):
        self._registers["SR"].set_bit(0, 0)
    
    def _CLD(self):
        self._registers["SR"].set_bit(3, 0)
    
    def _CLI(self):
        self._registers["SR"].set_bit(2, 0)
    
    def _CLV(self):
        self._registers["SR"].set_bit(6, 0)
    
    def _CMP(self):
        A = self._registers["AC"].get()
        result = A - self._data
        set_status(self._registers["SR"], self._opCodeDict["flags"], result)
    
    def _CPX(self):
        X = self._registers["X"].get()
        result = X - self._data
        set_status(self._registers["SR"], self._opCodeDict["flags"], result)
    
    def _CPY(self):
        Y = self._registers["Y"].get()
        result = Y - self._data
        set_status(self._registers["SR"], self._opCodeDict["flags"], result)
    
    def _DEC(self):
        result = self._data - 1
        set_status(self._registers["SR"], self._opCodeDict["flags"], result)
        self._bus.set(result & 0xFF, self._memAddr)        
    
    def _DEX(self):
        X = self._registers["X"].get()
        result = X - 1
        self._registers["X"].set(result & 0xFF)
        set_status(self._registers["SR"], self._opCodeDict["flags"], result)
    
    def _DEY(self):
        Y = self._registers["Y"].get()
        result = Y - 1
        self._registers["Y"].set(result & 0xFF)
        set_status(self._registers["SR"], self._opCodeDict["flags"], result)
    
    def _EOR(self):
        A = self._registers["AC"].get()
        result = A ^ self._data
        set_status(self._registers["SR"], self._opCodeDict["flags"], result)
        self._registers["AC"].set(result & 0xFF)
    
    def _INC(self):
        result = self._data + 1
        set_status(self._registers["SR"], self._opCodeDict["flags"], result)
        self._bus.set(result & 0xFF, self._memAddr) 
    
    def _INX(self):
        X = self._registers["X"].get()
        result = X + 1
        self._registers["X"].set(result & 0xFF)
        set_status(self._registers["SR"], self._opCodeDict["flags"], result)
    
    def _INY(self):
        Y = self._registers["Y"].get()
        result = Y + 1
        self._registers["Y"].set(result & 0xFF)
        set_status(self._registers["SR"], self._opCodeDict["flags"], result)
    
    def _JMP(self):
        self._registers["PC"] = self._memAddr
    
    def _JSR(self):
        # Push return address to stack
        pc = self._registers["PC"].get()
        sp = self._register["SP"].get()
        self._bus.set((pc + 2) & 0x00FF, 0x0100 + sp)
        sp -= 1
        self._bus.set(((pc + 2) & 0xFF00) >> 8, 0x0100 + sp)
        sp -= 1
        self._registers["SP"].set(sp)
        set_status(self._registers["SR"], self._opCodeDict["flags"], 1)
        
        # Jump to subroutine
        self._registers["PC"] = self._memAddr
    
    def _LDA(self):
        result = self._data
        set_status(self._registers["SR"], self._opCodeDict["flags"], result)
        self._registers["AC"].set(result & 0xFF)
    
    def _LDX(self):
        result = self._registers["X"]
        set_status(self._registers["SR"], self._opCodeDict["flags"], result)
        self._registers["AC"].set(result & 0xFF)
    
    def _LDY(self):
        result = self._registers["Y"]
        set_status(self._registers["SR"], self._opCodeDict["flags"], result)
        self._registers["AC"].set(result & 0xFF)
    
    def _LSR(self):
        C = self._data & 0x01
        result = self._data >> 1
        set_status(self._registers["SR"], self._opCodeDict["flags"], result)        
        self._registers["SR"].set_bit(0, C)
        if self._memAddr == "AC":
            self._registers["AC"].set(result & 0xFF)
        else:
            self._bus.set(result & 0xFF, self._memAddr)
    
    def _NOP(self):
        pass
    
    def _ORA(self):
        A = self._registers["AC"].get()
        result = A | self._data
        set_status(self._registers["SR"], self._opCodeDict["flags"], result)
        self._registers["AC"].set(result & 0xFF)
    
    def _PHA(self):
        sp = self._register["SP"].get()
        A = self._registers["AC"].get()
        self._bus.set(A, 0x0100 + sp)
        sp -= 1
        self._registers["SP"].set(sp)
    
    def _PHP(self):
        self._register["SP"].set_bit(4, 1)
        self._register["SP"].set_bit(5, 1)
        sr = self._register["SP"].get()
        sp = self._register["SP"].get()
        self._bus.set(sr, 0x0100 + sp)
        sp -= 1
        self._registers["SP"].set(sp)        
    
    def _PLA(self):
        sp = self._register["SP"].get()
        A = self._bus.get(0x0100 + sp)
        set_status(self._registers["SR"], self._opCodeDict["flags"], A)
        sp += 1
        self._registers["AC"].set(A)
        self._registers["SP"].set(sp)
    
    def _PLP(self):
        sp = self._register["SP"].get()
        sr = self._bus.get(0x0100 + sp) & 0b11001111
        sp += 1
        self._registers["SR"].set(sr)
        self._registers["SP"].set(sp)
    
    def _ROL(self):
        C = self._registers["SR"].get_bit(0)
        result = (self._data << 1) + C & 0x01
        set_status(self._registers["SR"], self._opCodeDict["flags"], result)
        self._registers["SR"].set_bit(self._data >> 7, 0)        
        if self._memAddr == "AC":
            self._registers["AC"].set(result & 0xFF)
        else:
            self._bus.set(result & 0xFF, self._memAddr)
    
    def _ROR(self):
        C = self._registers["SR"].get_bit(0)
        result = (self._data >> 1) + C & 0x80
        set_status(self._registers["SR"], self._opCodeDict["flags"], result)
        self._registers["SR"].set_bit(self._data & 0x01, 0)        
        if self._memAddr == "AC":
            self._registers["AC"].set(result & 0xFF)
        else:
            self._bus.set(result & 0xFF, self._memAddr)
    
    def _RTI(self):
        sp = self._register["SP"].get()
        sr = self._bus.get(0x0100 + sp) & 0b11001111
        sp += 1
        HH = self._bus.get(0x0100 + sp) << 8
        sp += 1
        LL = self._bus.get(0x0100 + sp) 
        sp += 1        
        self._registers["PC"].set(HH + LL)
        self._registers["SR"].set(sr)
        self._registers["SP"].set(sp)
    
    def _RTS(self):
        sp = self._register["SP"].get()
        HH = self._bus.get(0x0100 + sp) << 8
        sp += 1
        LL = self._bus.get(0x0100 + sp) 
        sp += 1          
        self._registers["PC"].set(HH + LL) 
        self._registers["SP"].set(sp)  
    
    def _SBC(self):
        A = self._registers["AC"].get()
        C = self._registers["SR"].get_bit(0)
        result = A - self._data - (1 - C)
        set_status(self._registers["SR"], self._opCodeDict["flags"], result)
        self._registers["AC"].set(result & 0xFF)
    
    def _SEC(self):
        self._registers["SR"].set_bit(1, 0)
    
    def _SED(self):
        self._registers["SR"].set_bit(1, 3)
    
    def _SEI(self):
        self._registers["SR"].set_bit(1, 2)
    
    def _STA(self):
        A = self._registers["AC"]
        self._bus(A, self._memAddr)
    
    def _STX(self):
        X = self._registers["X"]
        self._bus(X, self._memAddr)
    
    def _STY(self):
        Y = self._registers["AC"]
        self._bus(Y, self._memAddr)
    
    def _TAX(self):
        A = self._registers["AC"]
        self._registers["X"].set(A)
        set_status(self._registers["SR"], self._opCodeDict["flags"], A)
    
    def _TAY(self):
        A = self._registers["AC"]
        self._registers["Y"].set(A)
        set_status(self._registers["SR"], self._opCodeDict["flags"], A)
    
    def _TSX(self):
        sp = self._registers["SP"]
        self._registers["X"].set(A)
        set_status(self._registers["SR"], self._opCodeDict["flags"], sp)
    
    def _TXA(self):
        X = self._registers["X"]
        self._registers["AC"].set(X)
        set_status(self._registers["SR"], self._opCodeDict["flags"], X)
    
    def _TXS(self):
        X = self._registers["X"]
        self._registers["SP"].set(X)
        set_status(self._registers["SR"], self._opCodeDict["flags"], X)
    
    def _TYA(self):
        Y = self._registers["Y"]
        self._registers["AC"].set(Y)
        set_status(self._registers["SR"], self._opCodeDict["flags"], Y)
    
    # Illegal operations
    def _ALR(self):
        pass

    def _ANC(self):
        pass

    def _ANE(self):
        pass

    def _XAA(self):
        pass

    def _ARR(self):
        pass

    def _DCP(self):
        pass

    def _ISC(self):
        pass

    def _LAS(self):
        pass

    def _LAX(self):
        pass

    def _RLA(self):
        pass

    def _RRA(self):
        pass

    def _SAX(self):
        pass

    def _AXS(self):
        pass

    def _AAX(self):
        pass

    def _SBX(self):
        pass

    def _SHA(self):
        pass

    def _SHX(self):
        pass

    def _SHY(self):
        pass

    def _SLO(self):
        pass

    def _SRE(self):
        pass

    def _TAS(self):
        pass

    def _SBC(self):
        pass

    def _NOP(self):
        pass

    def _JAM(self):
        pass
