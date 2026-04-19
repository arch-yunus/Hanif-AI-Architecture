import logging
from colorama import Fore, Style, init

init(autoreset=True)

class HanifLogger:
    def __init__(self):
        self.logger = logging.getLogger("Hanif-AI")
        self.logger.setLevel(logging.INFO)
        
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def ai_info(self, msg):
        print(f"{Fore.CYAN}[AI (Analytical)]{Style.RESET_ALL} {msg}")

    def ac_info(self, msg):
        print(f"{Fore.MAGENTA}[AC (Conscience)]{Style.RESET_ALL} {msg}")

    def am_info(self, msg):
        print(f"{Fore.GREEN}[AM (Mind)]{Style.RESET_ALL} {msg}")

    def error(self, msg):
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} {msg}")

logger = HanifLogger()
