# ===============================================================================
# Copyright 2023 ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================
from pyface.tasks.task import Task
from pyface.tasks.task_layout import TaskLayout, PaneItem
from traits.api import Instance, List, Any

from automation import Automation
from dashboard import Dashboard
from hardware.device import Device
from loggable import Loggable
from pane import HardwareCentralPane, DevicesPane, DashboardsPane, AutomationsPane


class BaseTask(Task):
    pass


class HardwareTask(BaseTask):
    selection = Instance(Loggable)
    devices = List(Device)
    dashboards = List(Dashboard)
    automations = List(Automation)

    def create_dock_panes(self):
        return [DevicesPane(model=self),
                DashboardsPane(model=self),
                AutomationsPane(model=self)]

    def create_central_pane(self):
        return HardwareCentralPane(model=self)

    def _default_layout_default(self):
        return TaskLayout(left=PaneItem("plv.devices"))
# ============= EOF =============================================
