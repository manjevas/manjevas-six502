# register.py

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

class register:
    def __get_nth_bit(self, num, n):
        # Convert the number to binary
        binary = bin(num)[2:]
        
        # Check if n is within the length of the binary string
        if n < len(binary):
            # Return the nth bit, counting from the right (0-indexed)
            return int(binary[-(n+1)])
        else:
            # If n is larger than the length of the binary string, return 0
            return 0
        
    def __set_nth_bit(self, num, n, value):
        if value not in [0, 1]:
            return "Error: Value must be 0 or 1"
        
        # Create a mask with the nth bit set to 1
        mask = 1 << n
        
        if value == 1:
            # Use bitwise OR to set the nth bit of num
            return num | mask
        else:
            # Use bitwise AND with the inverse of the mask to clear the nth bit of num
            return num & ~mask

    def __init__(self, size=8):
        self.__dat = 0
        self.size = size

    def get_bit(self, bit):
        if bit < self.size:
            return self.__get_nth_bit(self.__dat, bit)
        else:
            raise Exception(f"{str(bit)} bit is greater than size of register")

    def set_bit(self, bit, val):
        if (val == 1) or (val == 0):
            if bit < self.size:
                self.__dat = self.__set_nth_bit(self.__dat, bit, val)
            else:
                raise Exception(f"{str(bit)} bit is greater than size of register")
        else:
            raise Exception(f"{str(val)} is not an acceptable bit")

    def get(self, *argv):
        return self.__dat
    
    def set(self, val, *argv):
        if(val >= 2**self.size):
            raise Exception(f"{str(val)} is greater than max value of register")
        else:
            self.__dat = val