from enum import Enum
import os

class Action(Enum):
    RESTART = 1
    SHUTDOWN = 2


class ActionWorker:
    def configure(self, config):
        self.config = config

    def run(self):
        selected_action = self.config.action
        match(selected_action):
            case Action.RESTART: 
                os.system("sudo systemctl restart openvpn@client.service")
            case Action.SHUTDOWN:
                os.system("sudo shutdown now")
