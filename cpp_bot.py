from bot import bot
import sys

try:
    from colorama import Fore
except:
    print("Colarama library Not Installed Properly")
    input("Press Enter to exit")
    sys.exit()


#Class Inheritence From Parent to Child
class cpp_bot(bot):


#Polymorphic Function
    def printanswer(self):
        print(Fore.YELLOW+"CPP_Bot: "+Fore.GREEN+self.answer+Fore.RESET)



