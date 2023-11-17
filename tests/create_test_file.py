# create_test_file.py

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

import os

# Generate 10 random 8-bit numbers
numbers = os.urandom(0xF) + bytes(1)

# Write the numbers to a binary file
with open('test_load.bin', 'wb') as f:
    f.write(numbers)