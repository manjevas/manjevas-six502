# _debug.py

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

class tools:
    def __init__(self, setDebug = True, setLog = True, logFile = '.\debug.log'):
        self._setDebug = setDebug
        self._setLog = setLog
        self._logFile = logFile
        
    def print(self, msgStr, level=0):
        if self._setDebug:
            print(f"    DEBUG: Level {level}, {msgStr}")
            if self._setLog:
                with open(self._logFile, "a") as f:
                    f.write(f"    DEBUG: Level {level}, {msgStr}\n")