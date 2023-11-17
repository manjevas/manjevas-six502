# test_memory.py

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
from six502 import memory

class TestMemory(unittest.TestCase):

    def test_size(self):
        mem = memory()
        self.assertEqual(mem.size, 8192)

    def test_read_write(self):
        mem = memory()
        mem.write(0x00F1, 0xFA)
        self.assertEqual(mem.read(0x00F1), 0xFA)

    def test_load(self):
        mem = memory()
        mem.load("test_load")

        count = 0
        for i in range(0, mem.size):
            if mem.read(i) != 0:
                count += 1

        self.assertEqual(count, 0xF)

    def test_save(self):
        mem = memory()        
        mem.write(0x00F1, 0xFA)
        mem.save("test_save")
        mem.reset()

        self.assertEqual(mem.read(0x00F1), 0xFA)

if __name__ == '__main__':
    unittest.main()