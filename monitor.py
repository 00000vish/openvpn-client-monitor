from action import Action, ActionWorker
import time
import requests


class Monitor:
    def configure(self, config):
        self.config = config
        self.worker = ActionWorker()
        self.worker.configure(config)
        self.request_header = {
            'User-Agent': 'curl/7.81.0',
        }

    def check_ip_leak(self, ip):
        if (self.config.ip == -1):
            return False
        return (str(self.config.ip).strip() == str(ip).strip())

    def check_connection(self):
        try:
            res = requests.get("https://ifconfig.co", headers=self.request_header, timeout=5)
            return True, res.text
        except Exception:
            return False, -1

    def start(self):
        while (True):
            time.sleep(int(self.config.connection_check_seconds))
            connected, ip = self.check_connection()
            if not connected:
                self.worker.run()
                continue
            if self.check_ip_leak(ip):
                self.worker.run()
