# _six502.py

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

from component import clock, register
from instruction import instruction

class six502:
    def __init__(self, bus):
        self._clk = clock()
        self._registers = {
            "PC": register(16),
            "AC": register(),
            "X": register(),
            "SR": register(),
            "SP": register()
        }
        self._bus = bus
        
    def step(self):
        pass