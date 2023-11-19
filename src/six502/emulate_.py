# emulate.py

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

from six502 import clock
from six502 import memory
from six502 import bus
from six502 import cpu
from six502 import monitor
from six502 import keyboard

class emulate:
    def __init__(self):
        self.cpu = cpu
        self.memory = memory
        self.bus = bus
        self.monitor = monitor
        self.clock = clock
        self.keyboard = keyboard

    def reset(self):
        self.cpu.reset()
        self.memory.reset()
        self.monitor.reset()
        self.clock.reset()

    def run():
        pass