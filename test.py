from cpp_bot import cpp_bot
import datetime

inps=["What do you mean by operator overloading in classes in cpp???","Define Object Oriented Programming.....","What are loops in functions???"]


def returntime():
    now = datetime.datetime.now()
    timestamp = datetime.datetime.timestamp(now)
    return timestamp*1000

start=returntime()

def printtimedifference():
    print(f"{returntime()-start} miliseconds taken")


newbot = cpp_bot("db/cpp.json")#create new cpp_bot Object
# newbot.setup()#Setting up or initializing Nltk library




for inp in inps:
    start=returntime()

    print("\nSetting Input")
    newbot.setinput(inp)#Setting an input..
    printtimedifference()
    print(newbot.inp)

    print("\nTokenizing Input ")
   # newbot.split() #spliting the input into tokens by builtin python function
    newbot.tokenize() #spliting the input into tokens by nltk tokenizer function
    printtimedifference()
    newbot.printtokens()

    print("\nReplacing Similar Tokens with synonym's tag ")
    newbot.similartokens() #Replacing similar tokens with synonyms from the synonyms list
    printtimedifference()
    newbot.printtokens()

    print("\nRemoved Duplicate Tokens ")
    newbot.removeduplicate() #Removing duplicate word from the tokens
    printtimedifference()
    newbot.printtokens()

    print("\nSearching For Response")
    newbot.searchresponse() #search for words match and response from the queries list
    printtimedifference()

    newbot.printanswer() #print the answer out

    print("------------------------------------------END-----------------------------------------------")




