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

# Instructions by Name
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

from _addressing import addressing
import json

class instruction:
    def __init__(self, registers, bus):
        with open('opcodes.json') as f:
            self._opCodesDict = json.load(f)

        self._bus = bus
        self._registers = registers
        self._setupOps()

    def _setupOps(self):
        self.op["ADC"] = lambda: self._ADC()
        self.op["AND"] = lambda: self._AND()
        self.op["ASL"] = lambda: self._ASL()
        self.op["BCC"] = lambda: self._BCC()
        self.op["BCS"] = lambda: self._BCS()
        self.op["BEQ"] = lambda: self._BEQ()
        self.op["BIT"] = lambda: self._BIT()
        self.op["BMI"] = lambda: self._BMI()
        self.op["BNE"] = lambda: self._BNE()
        self.op["BPL"] = lambda: self._BPL()
        self.op["BRK"] = lambda: self._BRK()
        self.op["BVC"] = lambda: self._BVC()
        self.op["BVS"] = lambda: self._BVS()
        self.op["CLC"] = lambda: self._CLC()
        self.op["CLD"] = lambda: self._CLD()
        self.op["CLI"] = lambda: self._CLI()
        self.op["CLV"] = lambda: self._CLV()
        self.op["CMP"] = lambda: self._CMP()
        self.op["CPX"] = lambda: self._CPX()
        self.op["CPY"] = lambda: self._CPY()
        self.op["DEC"] = lambda: self._DEC()
        self.op["DEX"] = lambda: self._DEX()
        self.op["DEY"] = lambda: self._DEY()
        self.op["EOR"] = lambda: self._EOR()
        self.op["INC"] = lambda: self._INC()
        self.op["INX"] = lambda: self._INX()
        self.op["INY"] = lambda: self._INY()
        self.op["JMP"] = lambda: self._JMP()
        self.op["JSR"] = lambda: self._JSR()
        self.op["LDA"] = lambda: self._LDA()
        self.op["LDX"] = lambda: self._LDX()
        self.op["LDY"] = lambda: self._LDY()
        self.op["LSR"] = lambda: self._LSR()
        self.op["NOP"] = lambda: self._NOP()
        self.op["ORA"] = lambda: self._ORA()
        self.op["PHA"] = lambda: self._PHA()
        self.op["PHP"] = lambda: self._PHP()
        self.op["PLA"] = lambda: self._PLA()
        self.op["PLP"] = lambda: self._PLP()
        self.op["ROL"] = lambda: self._ROL()
        self.op["ROR"] = lambda: self._ROR()
        self.op["RTI"] = lambda: self._RTI()
        self.op["RTS"] = lambda: self._RTS()
        self.op["SBC"] = lambda: self._SBC()
        self.op["SEC"] = lambda: self._SEC()
        self.op["SED"] = lambda: self._SED()
        self.op["SEI"] = lambda: self._SEI()
        self.op["STA"] = lambda: self._STA()
        self.op["STX"] = lambda: self._STX()
        self.op["STY"] = lambda: self._STY()
        self.op["TAX"] = lambda: self._TAX()
        self.op["TAY"] = lambda: self._TAY()
        self.op["TSX"] = lambda: self._TSX()
        self.op["TXA"] = lambda: self._TXA()
        self.op["TXS"] = lambda: self._TXS()
        self.op["TYA"] = lambda: self._TYA()

    def run(self, opCode):
        try:
            opCodeDict = self.opCodesDict[opCode]
        except:
            raise Exception(f"{hex(opCode)} is an invalid opcode.")
        
        self._data, self._memAddr = addressing(opCodeDict[addressing], self._registers, self._bus)

        self.op[opCodeDict["instruction"]]

    def _ADC(self):
        pass
    def _AND(self):
        pass
    def _ASL(self):
        pass
    def _BCC(self):
        pass
    def _BCS(self):
        pass
    def _BEQ(self):
        pass
    def _BIT(self):
        pass
    def _BMI(self):
        pass
    def _BNE(self):
        pass
    def _BPL(self):
        pass
    def _BRK(self):
        pass
    def _BVC(self):
        pass
    def _BVS(self):
        pass
    def _CLC(self):
        pass
    def _CLD(self):
        pass
    def _CLI(self):
        pass
    def _CLV(self):
        pass
    def _CMP(self):
        pass
    def _CPX(self):
        pass
    def _CPY(self):
        pass
    def _DEC(self):
        pass
    def _DEX(self):
        pass
    def _DEY(self):
        pass
    def _EOR(self):
        pass
    def _INC(self):
        pass
    def _INX(self):
        pass
    def _INY(self):
        pass
    def _JMP(self):
        pass
    def _JSR(self):
        pass
    def _LDA(self):
        pass
    def _LDX(self):
        pass
    def _LDY(self):
        pass
    def _LSR(self):
        pass
    def _NOP(self):
        pass
    def _ORA(self):
        pass
    def _PHA(self):
        pass
    def _PHP(self):
        pass
    def _PLA(self):
        pass
    def _PLP(self):
        pass
    def _ROL(self):
        pass
    def _ROR(self):
        pass
    def _RTI(self):
        pass
    def _RTS(self):
        pass
    def _SBC(self):
        pass
    def _SEC(self):
        pass
    def _SED(self):
        pass
    def _SEI(self):
        pass
    def _STA(self):
        pass
    def _STX(self):
        pass
    def _STY(self):
        pass
    def _TAX(self):
        pass
    def _TAY(self):
        pass
    def _TSX(self):
        pass
    def _TXA(self):
        pass
    def _TXS(self):
        pass
    def _TYA(self):
        pass