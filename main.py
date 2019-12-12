from cpp_bot import cpp_bot

import random



titles=["           Initializing C++ CHAT BOT"]
empty=["Plz write anything"]
quits=["Exiting.."]



print(random.choice(titles))


#create new cpp_bot Object
newbot = cpp_bot("db/cpp.json")


#Setting up or initializing Nltk library
newbot.setup()








while(newbot.checkquit()):



    newbot.reset()

    newbot.getinput() #asking for input from the user

    newbot.tokenize() #spliting the input into tokens 

    if(len(newbot.tokens)==0):
        print(random.choice(empty))
        continue
    

    newbot.similartokens() #Replacing similar tokens with synonyms from the synonyms list



    newbot.removeduplicate() #Removing duplicate word from the tokens

    newbot.searchresponse() #search for words match and response from the queries list

    newbot.printanswer() #print the answer out






print(random.choice(quits))