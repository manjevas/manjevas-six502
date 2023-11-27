# _status.py

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

def set_status(register, bits, result, *argv):
    def set_N():
        if result & 0x80:
            register.set_bit(7, 1)
        else:
            register.set_bit(7, 0)
            
    def set_V():
        if len(argv) < 3:
            return
        a = argv[0]
        b = argv[1]
        
        if not((a >> 7) ^ (b >> 7)):
            result = result & 0xFF
            if result & 0x80:
                register.set_bit(6, 1)
            else:
                register.set_bit(6, 0)                
    
    def set_B():
        if result:
                register.set_bit(4, 1)
        else:
            register.set_bit(4, 0)  
    
    def set_D():
        if result:
                register.set_bit(3, 1)
        else:
            register.set_bit(3, 0)   
    
    def set_I():
        register.set_bit(2, 0)
    
    def set_Z():
        if result == 0:
            register.set_bit(1, 1)
        else:
            register.set_bit(1, 0)
            
    def set_C():
        if result & 0x100:
            register.set_bit(0, 1)
        else:            
            register.set_bit(0, 0)
            
    bit_rubrick = {
        "N": lambda: set_N(), 
        "V": lambda: set_V(), 
        "B": lambda: set_B(),
        "D": lambda: set_D(), 
        "I": lambda: set_I(),
        "Z": lambda: set_Z(),
        "C": lambda: set_C()
    }
    
    if bits == "":
        pass
    else:
        for bit in bits:
            bit_rubrick[bit]()
                