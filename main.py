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
import time
from threading import Thread

import zmq

from application import Application

def demo():
    def func():
        time.sleep(5)
        context = zmq.Context()
        #  Socket to talk to server
        print("Connecting to hello world server…")
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:5555")
        socket.send_json({"device": "switch_controller",
                          "function": "open_switch",
                          "kwargs": {"name": "Af",
                                     "block": True,
                                     "slow": True}})
        print(socket.recv_json())

    t = Thread(target=func)
    t.start()

def main():
    app = Application()
    app.run()


if __name__ == '__main__':
    # demo()
    main()
# ============= EOF =============================================
