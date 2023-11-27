# bus.py

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

import warnings

class bus:    
    def __init__(self, ram_size=8192, addrBits=16, valBits=8, rom_size=256, rom_tape='./wozmon'):
        from _memory import memory
        from six502.component import register

        try: 
            from six502 import RAM_SIZE      
            ram_size = RAM_SIZE
        except:
            pass

        self.__addrBits = addrBits
        self.__valBits = valBits
        self.__ram = memory(ram_size)
        self.__dsp = register()
        self.__dspcr = register()
        self.__kbd = register()
        self.__kbdcr = register()
        self.__rom = memory(rom_size)
        self.__dat = [
            self.__ram,     # RAM
            self.__kbd,     # KBD
            self.__kbdcr,   # KDBCR
            self.__dsp,     # DSP
            self.__dspcr,   # DSPCR
            self.__ram,     # RAM
            self.__rom      # ROM
        ]

        # Define various memory address range and what that corresponds to
        self.__addressRanges = [
                    (0x0000, 0x0FFF), # RAM, system & user space
                    (0xD010, 0xD010), # KBD
                    (0xD011, 0xD011), # KBDCR
                    (0xD012, 0xD012), # DSP
                    (0xD013, 0xD013), # DSPCR
                    (0xE000, 0xEFFF), # Extended RAM, Integer Apple Basic, PIA
                    (0xFF00, 0xFFFF)  # ROM
                ]
        
        self.__rom.load(rom_tape)

    def reset(self, trueZero=False):
        self.__ram.reset(trueZero=trueZero)
        self.__rom.reset()
        self.__dsp.reset()
        self.__dspcr.reset()
        self.__kbd.reset()
        self.__kbdcr.reset()
    
    def set(self, val, addr):
        if val < 2 ** self.__valBits:
            if addr < 2 ** self.__addrBits:
                for i, addressRange in enumerate(self.__addressRanges):
                    warnFlag = True
                    if (addr >= addressRange[0]) and (addr <= addressRange[1]):
                        if i == 5:
                            addr -= 0xD000
                        elif i == 6:
                            addr -= 0xFF00
                        self.__dat[i].set(val, addr)
                        warnFlag = False
                        break

                if warnFlag:
                    warnings.warn(f"Unused address {hex(addr)}", UserWarning)
            else:
                raise Exception(f"{str(addr)} is beyond address range")
        else:
            raise Exception(f"{str(val)} is beyond value range")
        
    def get(self, addr):
        if addr < 2 ** self.__addrBits:
            for i, addressRange in enumerate(self.__addressRanges):
                warnFlag = True
                if (addr >= addressRange[0]) and (addr <= addressRange[1]):
                    if i == 5:
                        addr -= 0xD000
                    elif i == 6:
                        addr -= 0xFF00
                    warnFlag = False
                    return self.__dat[i].get(addr)

            if warnFlag:
                warnings.warn(f"Unused address {hex(addr)}", UserWarning)
        else:
            raise Exception(f"{str(addr)} is beyond address range")
        
    def tapeIn(self, name):
        self.__ram.load(name)

    def tapeOut(self, name):
        self.__ram.save(name)