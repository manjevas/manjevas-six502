# test_addressing.py

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
from six502.instruction._addressing import addressing
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
        
m_bus = bus()

class TestAddressing(unittest.TestCase):

    def test_mode_accumulator(self):
        registers["PC"].set(0x0200)
        registers["AC"].set(0x6F)
        mode = "A"
        data, memAddr = addressing(mode, registers, m_bus, dbg)
        
        self.assertEqual(registers["PC"].get(), 0x0200)
        self.assertEqual(data, 0x6F)
        self.assertEqual(memAddr, 'AC')
        
    def test_mode_immediate(self):
        registers["PC"].set(0x0200)
        m_bus.set(0x56, 0x0200)
        mode = "#"
        data, memAddr = addressing(mode, registers, m_bus, dbg)
        
        self.assertEqual(registers["PC"].get(), 0x0201)
        self.assertEqual(data, 0x56)
        self.assertEqual(memAddr, 0x0200)
        
    def test_mode_absolute(self):
        registers["PC"].set(0x0200)
        m_bus.set(0x05, 0x0200)
        m_bus.set(0x02, 0x0201)
        m_bus.set(0x11, 0x0205)
        mode = "abs"
        data, memAddr = addressing(mode, registers, m_bus, dbg)
        
        self.assertEqual(registers["PC"].get(), 0x0202)
        self.assertEqual(data, 0x11)
        self.assertEqual(memAddr, 0x0205)
        
    def test_mode_zeroPage(self):
        registers["PC"].set(0x0200)
        m_bus.set(0x05, 0x0200)
        m_bus.set(0x02, 0x0005)
        mode = "zpg"
        data, memAddr = addressing(mode, registers, m_bus, dbg)
        
        self.assertEqual(registers["PC"].get(), 0x0201)
        self.assertEqual(data, 0x02)
        self.assertEqual(memAddr, 0x0005)
        
    def test_mode_absoluteX(self):
        registers["PC"].set(0x0200)
        registers["X"].set(0x12)
        m_bus.set(0x05, 0x0200)
        m_bus.set(0x02, 0x0201)
        m_bus.set(0x11, 0x0217)
        mode = "abs,X"
        data, memAddr = addressing(mode, registers, m_bus, dbg)
        
        self.assertEqual(registers["PC"].get(), 0x0202)
        self.assertEqual(data, 0x11)
        self.assertEqual(memAddr, 0x0217)
        
    def test_mode_absoluteY(self):
        registers["PC"].set(0x0200)
        registers["Y"].set(0x12)
        m_bus.set(0x05, 0x0200)
        m_bus.set(0x02, 0x0201)
        m_bus.set(0x11, 0x0217)
        mode = "abs,Y"
        data, memAddr = addressing(mode, registers, m_bus, dbg)
        
        self.assertEqual(registers["PC"].get(), 0x0202)
        self.assertEqual(data, 0x11)
        self.assertEqual(memAddr, 0x0217)
        
    def test_mode_zeroPageX(self):
        registers["PC"].set(0x0200)
        registers["X"].set(0x12)
        m_bus.set(0x05, 0x0200)
        m_bus.set(0x02, 0x0017)
        mode = "zpg,X"
        data, memAddr = addressing(mode, registers, m_bus, dbg)
        
        self.assertEqual(registers["PC"].get(), 0x0201)
        self.assertEqual(data, 0x02)
        self.assertEqual(memAddr, 0x0017)
        
    def test_mode_zeroPageY(self):
        registers["PC"].set(0x0200)
        registers["Y"].set(0x12)
        m_bus.set(0x05, 0x0200)
        m_bus.set(0x02, 0x0017)
        mode = "zpg,Y"
        data, memAddr = addressing(mode, registers, m_bus, dbg)
        
        self.assertEqual(registers["PC"].get(), 0x0201)
        self.assertEqual(data, 0x02)
        self.assertEqual(memAddr, 0x0017)
        
    def test_mode_indirect(self):
        registers["PC"].set(0x0200)
        m_bus.set(0x05, 0x0200)
        m_bus.set(0x02, 0x0201)
        m_bus.set(0x10, 0x0205)
        m_bus.set(0x02, 0x0206)
        m_bus.set(0xA2, 0x0210)
        mode = "ind"
        data, memAddr = addressing(mode, registers, m_bus, dbg)
        
        self.assertEqual(registers["PC"].get(), 0x0202)
        self.assertEqual(data, 0xA2)
        self.assertEqual(memAddr, 0x0210)
           
if __name__ == '__main__':
    unittest.main()