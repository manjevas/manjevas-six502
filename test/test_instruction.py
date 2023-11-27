# test_instruction.py

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

import unittest
import sys
sys.path.append('../src')

from _bus import bus
from six502.component import register
from six502.component import clock
from six502.instruction import instruction
from six502.debug import tools

dbg = tools()
registers = {
            "AC": register(),
            "X" : register(),
            "Y" : register(),
            "SP": register(),
            "SR": register(),
            "PC": register(16)
        }
        
registers["SP"].set(0xFF)
registers["SR"].set_bit(5, 1)
registers["PC"].set(0x0200)   # Set PC = 0x0200
        
m_bus = bus()

clk = clock()

class TestInstruction(unittest.TestCase):

    def test_opCodes_init(self):
        inst = instruction(registers, m_bus, clk, dbg)
        
        self.assertEqual(len(inst._opCodesDict), 252)
        
    def test_ADC_immediate_noCarry(self):
        registers["AC"].set(0x05)     # Set A = 5
        m_bus.set(0x69, 0x0200)       # 0x0200: 0x69
        m_bus.set(0xFE, 0x0201)       # 0x0201: 0xFE
        
        inst = instruction(registers, m_bus, clk, dbg)
        opCode = m_bus.get(registers["PC"].get())
        inst.run(opCode)
        
        self.assertEqual(registers["AC"].get(), 0x03)
        self.assertEqual(registers["SR"].get_bit(0), 1)
        
    def test_ADC_immediate_Carry(self): 
        registers["SR"].set_bit(0, 1) # set carry
        
        registers["AC"].set(0x05)     # Set A = 5
        m_bus.set(0x69, 0x0200)       # 0x0200: 0x69
        m_bus.set(0x05, 0x0201)       # 0x0201: 0x05
        
        inst = instruction(registers, m_bus, clk, dbg)
        opCode = m_bus.get(registers["PC"].get())
        inst.run(opCode)
        
        self.assertEqual(registers["AC"].get(), 0x0B)
        self.assertEqual(registers["SR"].get_bit(0), 0)
        
if __name__ == '__main__':
    unittest.main()