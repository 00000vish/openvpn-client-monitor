from action import Action

class Config:

    def __init__(self):
        self.connection_check_seconds = 300
        self.action = Action(1)
        self.ip = -1

    def configure(self, check_seconds=300, enum_Action=Action(1), ip=-1):
        if not isinstance(check_seconds, int):
            raise TypeError('check_seconds should be in seconds (int)')
        if not isinstance(enum_Action, Action):
            raise TypeError('enum_Action should be enum Action')
        if (check_seconds != 300):
            self.connection_check_seconds = check_seconds
        if (enum_Action != Action(1)):
            self.action = enum_Action
        if (ip != -1):
            self.ip = ip

    def __str__(self):
        checking_str = "Network Checking Interval = {}(s)".format(self.connection_check_seconds)
        action_str = "\nOn Fail = {}\n".format(self.action)
        ip_str = "Ip Monitoring = {}".format("Off" if (self.ip == -1) else self.ip)
        return checking_str + action_str + ip_str
