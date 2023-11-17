# memory.py

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

import six502
import warnings        

class memory:
    
    def __init__(self):
        self.__dat = [0] * six502.MEM_SIZE
        self.size = len(self.__dat)

    def load(self, file):
        self.__tape = file
        index = 0
        with open(self.__tape + ".bin", "rb") as f:
            byte = f.read(1)
            while byte:
                self.__dat[index] = int.from_bytes(byte, byteorder="big")
                byte = f.read(1)
                index += 1

    def save(self, file):
        self.__tape = file
        with open(self.__tape + ".bin", "wb") as f:
            for hex_num in self.__dat:
                f.write(hex_num.to_bytes(1, "big"))

    def reset(self):
        self.__dat = [0] * six502.MEM_SIZE
        try:
            self.load(self.__tape)
        except:
            warnings.warn("No tape found, loading zeros.", Warning)

    def read(self, addr):
        try:
            return self.__dat[addr]
        except:
            Exception("Memory address outside bounds.")

    def write(self, addr, val):
        if addr <= 0xFFFF:
            self.__dat[addr] = val
        else:
            Exception("Memory address outside bounds.")