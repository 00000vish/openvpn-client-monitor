import os
import sys
from config import Action, Config
from monitor import Monitor


def print_banner():
    print("\n  ___   ____   ___  ____   __ __  ____  ____          __  _      ____    ___  ____   ______      ___ ___   ___   ____   ____  ______   ___   ____  "
          + "\n /   \ |    \ /  _]|    \ |  |  ||    \|    \        /  ]| |    |    |  /  _]|    \ |      |    |   |   | /   \ |    \ |    ||      | /   \ |    \ "
            + "\n|     ||  o  )  [_ |  _  ||  |  ||  o  )  _  |      /  / | |     |  |  /  [_ |  _  ||      |    | _   _ ||     ||  _  | |  | |      ||     ||  D  )"
            + "\n|  O  ||   _/    _]|  |  ||  |  ||   _/|  |  |     /  /  | |___  |  | |    _]|  |  ||_|  |_|    |  \_/  ||  O  ||  |  | |  | |_|  |_||  O  ||    / "
            + "\n|     ||  | |   [_ |  |  ||  :  ||  |  |  |  |    /   \_ |     | |  | |   [_ |  |  |  |  |      |   |   ||     ||  |  | |  |   |  |  |     ||    \ "
            + "\n|     ||  | |     ||  |  | \   / |  |  |  |  |    \     ||     | |  | |     ||  |  |  |  |      |   |   ||     ||  |  | |  |   |  |  |     ||  .  \\"
            + "\n \___/ |__| |_____||__|__|  \_/  |__|  |__|__|     \____||_____||____||_____||__|__|  |__|      |___|___| \___/ |__|__||____|  |__|   \___/ |__|\_|"
          )


def print_command_line_help():
    print_banner()
    print("\n\nUsage: python3 [[OPTIONS] [VALUE] ...]")
    print("\nOption         Meaning")
    print("-t             Time in seconds to check for connection status (defualt=5)")
    print("-a             Action to perform when connection is down (defualt=1(restart))")
    print("\nActions Values           Meaning")
    print("1                        Restart OpenVPN Client service")
    print("2                        Shutdown computer")
    print("\n")


def parse_args(config, switchInput, valueInput):
    match(str(switchInput)):
        case "-t":
            config.configure(check_seconds=int(valueInput))
        case "-a":
            config.configure(enum_Action=Action(int(valueInput)))
        case "-i":
            config.configure(ip=str(valueInput))
        case _:
            config = None
    return config


def generate_config():
    arg_counts = len(sys.argv)
    if (arg_counts % 2 == 0):
        return None
    if (arg_counts < 3):
        return Config()
    config = Config()
    for switchIndex in range(1, arg_counts-1, 2):
        swithInput = sys.argv[switchIndex]
        valueInput = sys.argv[switchIndex+1]
        config = parse_args(config, swithInput, valueInput)
    return config


def is_root():
    try:
        testFolder = "/etc/openvpn-client-montior"
        if (os.path.exists(testFolder)):
            os.rmdir(testFolder)
        os.mkdir(testFolder)
        if (os.path.exists(testFolder)):
            return True
        return False
    except Exception:
        return False


def main():
    if not is_root():
        print("Please run the sciprt with sudo.")
        sys.exit()
    config = generate_config()
    if (config == None):
        print_command_line_help()
        exit()
    monitor = Monitor()
    monitor.configure(config)
    monitor.start()


if __name__ == '__main__':
    main()
