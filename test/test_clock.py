# test_clock.py

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
from six502.component import clock
from six502 import CLOCK

class TestClock(unittest.TestCase):

    def test_init(self):
        clk = clock()

        self.assertEqual(clk.counter, 0)
        self.assertEqual(clk.time, 0)
        self.assertEqual(clk.speed, CLOCK)

    def test_reset(self):
        clk = clock()

        clk.tick()
        clk.reset()

        self.assertEqual(clk.counter, 0)
        self.assertEqual(clk.time, 0)
        self.assertEqual(clk.speed, CLOCK)

    def test_tick(self):
        clk = clock()

        clk.tick()

        self.assertEqual(clk.counter, 1)
        self.assertEqual(clk.time, 1/CLOCK)

        with self.assertRaises(Exception):
            clk.tick(-1)


if __name__ == '__main__':
    unittest.main()