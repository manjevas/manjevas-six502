# _addressing.py

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

def addressing(mode, registers, bus):
    memAddr = -0x01
    data    = -0x01
    pc      = registers["PC"]

    if mode == "A":
        data = registers["AC"].get()
        memAddr = "AC"
        pc += 1
    elif mode == "abs":
        LL = bus.get(pc)
        pc += 1
        HH = bus.get(pc)
        pc += 1
        memAddr = (HH << 8) + LL
        data = bus.get(memAddr)        
    elif mode == "abs,X":
        LL = bus.get(pc)
        pc += 1
        HH = bus.get(pc)
        pc += 1
        X = registers["X"].get()
        memAddr = (HH << 8) + LL + X
        data = bus.get(memAddr)
    elif mode == "abs,Y":
        LL = bus.get(pc)
        pc += 1
        HH = bus.get(pc)
        pc += 1
        Y = registers["Y"].get()
        memAddr = (HH << 8) + LL + Y
        data = bus.get(memAddr)
    elif mode == "#":
        memAddr = pc
        pc += 1
        data = bus.get(memAddr)
    elif mode == "impl":
        pass
    elif mode == "ind":
        tempLL = bus.get(pc)
        pc += 1
        tempHH = bus.get(pc)
        pc += 1
        tempMemAddr = (tempHH << 8) + tempLL
        LL = bus.get(tempMemAddr)
        HH = bus.get(tempMemAddr + 1)
        memAddr = (HH << 8) + LL
        data = bus.get(memAddr)
    elif mode == "X,ind":
        X = registers["X"].get()
        tempLL = bus.get(pc) + X
        pc += 1
        tempHH = tempLL + 1
        tempMemAddr = (tempHH << 8) + tempLL
        LL = bus.get(tempMemAddr)
        HH = bus.get(tempMemAddr + 1)
        memAddr = (HH << 8) + LL
        data = bus.get(memAddr)
    elif mode == "ind,Y":
        tempLL = bus.get(pc)
        pc += 1
        tempHH = tempLL + 1
        tempMemAddr = (tempHH << 8) + tempLL
        Y = registers["Y"].get()
        LL = bus.get(tempMemAddr)
        HH = bus.get(tempMemAddr + Y)
        memAddr = (HH << 8) + LL
        data = bus.get(memAddr)
    elif mode == "rel":
        offset = bus.get(pc)
        pc += 1
        offset = (1 - 2 * ((offset & 0x80) >> 7)) * (offset & 0x7F)
        memAddr = pc + offset
        data = bus.get(memAddr)
    elif mode == "zpg":
        LL = bus.get(pc)
        pc += 1
        memAddr = LL
        data = bus.get(memAddr)
    elif mode == "zpg,X":
        LL = bus.get(pc)
        pc += 1
        X = registers["X"].get()
        memAddr = LL + X
        data = bus.get(memAddr)
    elif mode == "zpg,Y":
        LL = bus.get(pc)
        pc += 1
        Y = registers["Y"].get()
        memAddr = LL + Y
        data = bus.get(memAddr)
    else:
        warnings.warn(f"Invalid address mode acronym: {mode}", UserWarning)

    return data, memAddr