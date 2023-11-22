# addressing.py

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

class addressing:
    def __init__(self, bus, registers, clock):
        self.__bus = bus
        self.__registers = registers
        self.__clock = clock
    
    def eval(self, mode):
        if mode == "ACC":
            self.__clock.tick()
            return self.__registers["ACC"].get()
        
        elif mode =="ABS":
            self.__clock.tick(2)
            pc = self.__registers["PC"].get()
            LL = self.__bus.get(pc)
            self.__registers["PC"].set(pc + 1)
            HH = self.__bus.get(pc + 1)
            self.__registers["PC"].set(pc + 2)
            return (HH << 8) + LL
        
        elif mode =="ABX":
            self.__clock.tick(2)
            pc = self.__registers["PC"].get()
            LL = self.__bus.get(pc)
            self.__registers["PC"].set(pc + 1)
            HH = self.__bus.get(pc + 1)
            self.__registers["PC"].set(pc + 2)
            X = self.__registers["X"].get()
            
            
            return (HH << 8) + LL + X
        
        elif mode == "ABY":
            pass
        elif mode == "IMM":
            pass
        elif mode == "IMP":
            pass
        elif mode == "IND":
            pass
        elif mode == "XIN":
            pass
        elif mode == "INY":
            pass
        elif mode == "REL":
            pass
        elif mode == "ZPG":
            pass
        elif mode == "ZPX":
            pass
        elif mode == "ZPY":
            pass