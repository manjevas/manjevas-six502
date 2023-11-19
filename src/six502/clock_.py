# clock.py

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
import ctypes

class clock:
    def __init__(self):
        self.counter = 0x0
        self.time = 0.0
        self.speed = six502.CLOCK

    def __get__(self, instance, owner):
        return self.value

    def reset(self):
        self.counter = 0x0
        self.time = 0.0

    def tick(self, count=1):
        def delay_execution(nanoseconds):
            # Load the ntdll DLL
            ntdll = ctypes.windll.ntdll

            # Define the argument types and return type
            ntdll.NtDelayExecution.argtypes = [ctypes.c_byte, ctypes.POINTER(ctypes.c_longlong)]
            ntdll.NtDelayExecution.restype = ctypes.c_long

            # The delay must be negative to represent a relative delay.
            delay = -int(nanoseconds / 100)  # Convert to 100-nanosecond intervals
            ntdll.NtDelayExecution(False, ctypes.byref(ctypes.c_longlong(delay)))

        if count < 0:
            raise Exception(f"{str(count)} is non-negative")
        
        self.counter += count
        self.time += count * 1 / self.speed
        delay_execution(self.time * 10 ** 9)
        