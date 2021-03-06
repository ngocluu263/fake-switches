# Copyright 2015 Internap.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from fake_switches.dell.command_processor.default import DellDefaultCommandProcessor

from fake_switches.dell10g.command_processor.enabled import \
    Dell10GEnabledCommandProcessor


class Dell10GDefaultCommandProcessor(DellDefaultCommandProcessor):
    enabled_command_processor = Dell10GEnabledCommandProcessor
