# test_register.py

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
from six502.component import register

class TestRegister(unittest.TestCase):

    def test_init(self):
        acc = register()
        pc = register(16)

        self.assertEqual(acc.size, 8)
        self.assertEqual(pc.size, 16)

    def test_get_bit(self):
        acc = register()

        self.assertEqual(acc.get_bit(3), 0)
        acc.set_bit(4, 1)
        self.assertEqual(acc.get_bit(4), 1)

        with self.assertRaises(Exception):
            acc.get_bit(10)

    def test_set_bit(self):
        acc = register()

        acc.set_bit(3, 1)
        self.assertEqual(acc.get_bit(3), 1)

        with self.assertRaises(Exception):
            acc.set_bit(8, 1)

        with self.assertRaises(Exception):
            acc.set_bit(3, 2)

    def test_get(self):
        acc = register()

        acc.set(10)
        self.assertEqual(acc.get(), 10)

    def test_set(self):
        acc = register()

        acc.set(255)
        self.assertEqual(acc.get(), 255)

        with self.assertRaises(Exception):
            acc.set(256)


if __name__ == '__main__':
    unittest.main()