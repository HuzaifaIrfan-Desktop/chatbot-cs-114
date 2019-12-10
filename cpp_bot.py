from bot import bot

import json
import random

from colorama import Fore

class cpp_bot(bot):

    def printanswer(self):
        print(Fore.YELLOW+"CPP_Bot: "+Fore.GREEN+self.answer+Fore.RESET)



