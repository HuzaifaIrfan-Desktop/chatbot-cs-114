from cpp_bot import cpp_bot
from colorama import Fore
import random



titles=["           Initializing C++ CHAT BOT"]

empty=["Plz write anything"]

quits=["Exiting.."]



print(random.choice(titles))


#create new cpp_bot Object
newbot = cpp_bot("db/cpp.json")


#Setting up or initializing Nltk library
newbot.setup()







notcheckquit=True

while(notcheckquit):



    newbot.reset()

    while(len(newbot.tokens)==0):
        newbot.reset()
        newbot.getinput() #asking for input from the user

        newbot.tokenize() #spliting the input into tokens 

        if(len(newbot.tokens)==0):
            print(Fore.RED+"BOT: "+Fore.GREEN+random.choice(empty))


    newbot.similartokens() #Replacing similar tokens with synonyms from the synonyms list

    notcheckquit=newbot.checkquit()

    newbot.removeduplicate() #Removing duplicate word from the tokens

    newbot.searchresponse() #search for words match and response from the queries list

    newbot.printanswer() #print the answer out






print(random.choice(quits))