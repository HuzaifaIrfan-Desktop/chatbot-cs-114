from cpp_bot import cpp_bot

newbot = cpp_bot();
newbot.setup()







checkquit=True
while(checkquit):
    while(len(newbot.tokens)==0):
        newbot.getinput()
        newbot.tokenize()
        if(len(newbot.tokens)==0):
            print("Plz write something")
    checkquit=newbot.checkquit()
    newbot.similartokens()
    newbot.searchresponse()
    newbot.printanswer()
    newbot.reset()
