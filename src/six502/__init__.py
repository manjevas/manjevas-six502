# __init__.py

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

from importlib import resources

from six502.bus_ import bus

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

# Version of the manjevas-six502 package
__version__ = "0.1.0"

# Read default CPU configuration from config file
_cfg = tomllib.loads(resources.read_text("six502", "config.toml"))

# cpu config
RAM_SIZE = _cfg["configuration"]["ram_size"]
CLOCK    = _cfg["configuration"]["clock"]
RUN_MODE = _cfg["configuration"]["run_mode"]
LOGGING  = _cfg["configuration"]["logging"]

# initialization config
STATUS_REG_INIT = _cfg["initialization"]["status_reg"]
STACK_PTR_INIT  = _cfg["initialization"]["stack_pointer"]
CYCLE_CNT_INIT  = _cfg["initialization"]["cycle_counter"]