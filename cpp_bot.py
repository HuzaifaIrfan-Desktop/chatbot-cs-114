from bot import bot
import sys

try:
    from colorama import Fore
except:
    print("Colarama library Not Installed Properly")
    input("Press Enter to exit")
    sys.exit()

class cpp_bot(bot):

    def printanswer(self):
        print(Fore.YELLOW+"CPP_Bot: "+Fore.GREEN+self.answer+Fore.RESET)



