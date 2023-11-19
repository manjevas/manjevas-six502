# test_bus.py

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
from six502 import bus

class TestClock(unittest.TestCase):

    def test_set_get_val(self):
        mainBus = bus(rom_tape='../tapes/wozmon')

        mainBus.set(0xFA, 0x0001)
        self.assertEqual(mainBus.get(0x0001), 0xFA)

    def test_set_get_warn(self):
        mainBus = bus(rom_tape='../tapes/wozmon')

        with self.assertWarns(UserWarning):
            mainBus.set(0x01, 0x1000)

    def test_set_get_valException(self):
        mainBus = bus(rom_tape='../tapes/wozmon')

        with self.assertRaises(Exception):
            mainBus.set(0xF01, 0x1000)

    def test_set_get_addrException(self):
        mainBus = bus(rom_tape='../tapes/wozmon')

        with self.assertRaises(Exception):
            mainBus.set(0x01, 0xF0000)

    def test_reset_withoutTapeOut(self):
        mainBus = bus(rom_tape='../tapes/wozmon')

        mainBus.set(0xFA, 0x0001)
        mainBus.reset()
        self.assertEqual(mainBus.get(0x0001), 0x00)

    def test_tapeOut(self):
        mainBus = bus(rom_tape='../tapes/wozmon')

        mainBus.set(0xFA, 0x0001)
        mainBus.set(0xA0, 0xD010)

        mainBus.tapeOut('test_tapeOut')

        mainBus.reset()
        self.assertEqual(mainBus.get(0x0001), 0xFA)
        self.assertEqual(mainBus.get(0xD010), 0x00)

    def test_tapeIn(self):
        mainBus = bus(rom_tape='../tapes/wozmon')

        mainBus.tapeIn('test_tapeOut')
        self.assertEqual(mainBus.get(0x0001), 0xFA)
        self.assertEqual(mainBus.get(0xD010), 0x00)

if __name__ == '__main__':
    unittest.main()