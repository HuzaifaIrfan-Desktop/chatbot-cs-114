from cpp_bot import cpp_bot
from colorama import Fore
import random


titles=["           Initializing C++ CHAT BOT"]

empty=["Plz write anything"]
quits=["Exiting.."]



print(random.choice(titles))


newbot = cpp_bot()
newbot.setup()







checkquit=True
while(checkquit):
    newbot.reset()

    while(len(newbot.tokens)==0):
        newbot.reset()
        newbot.getinput()
        newbot.tokenize()
        if(len(newbot.tokens)==0):
            print(Fore.RED+"BOT: "+Fore.GREEN+random.choice(empty))
    checkquit=newbot.checkquit()
    newbot.similartokens()
    newbot.removeduplicate()
    newbot.searchresponse()
    newbot.printanswer()






print(random.choice(quits))