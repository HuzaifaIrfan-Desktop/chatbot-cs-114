import json
import random 

import sys



try:
    import nltk
    from nltk.tokenize import word_tokenize
except:
    print("NLTK library Not Installed Properly")
    input("Press Enter to exit")
    sys.exit()




#Parent Class
class bot:


#Contructor Function
    def __init__(self,filename):
        self.fname=filename
        try:
            with open(self.fname) as dbfile:
                self.db = json.load(dbfile)
        except:
            print("Database File not found at ",self.fname)
            input("Press Enter to exit")
            sys.exit()

        self.synonymslst=self.db["synonyms"]
        self.querieslst=self.db["queries"]
        self.inp=""
        self.tokens=[]
        self.answer=""
        print("           Initializing CHAT BOT")

#to setup nltk puntk
    def setup(self):
        nltk.download('punkt')


#to check if quit token is present
    def checkquit(self):
        for token in self.tokens:
            if(token=="quit"):
                return False
        return True


#to reset the variables
    def reset(self):
        self.inp=""
        self.tokens=[]
        self.answer=""

#to get input from user
    def getinput(self):
        self.inp =input("\nYOU: ").lower()


#to set input from program
    def setinput(self,inp):
        self.inp =inp.lower()


#Use NLTK tokenizer to tokenize
    def tokenize(self):
        self.tokens = word_tokenize(self.inp)


#Use Builtin string split function with whitespace as delimiter after whitelisting invalid characters from input string
    def split(self):
        whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ+')
        self.inp=''.join(filter(whitelist.__contains__, self.inp)) #whitelist invalid characters from input string
        self.tokens = self.inp.split()


#print the seperated Token's list
    def printtokens(self):
        print(self.tokens)


#return the seperated Token
    def returntokens(self):
        return self.tokens



#Replace the similar tokens from the synonym list
    def similartokens(self):
        for word in self.tokens:
            for synonym in self.synonymslst:
                br=0
                for keyword in synonym["keywords"]:
                    if(keyword==word):

                        self.tokens[int(self.tokens.index(keyword))]=synonym["tag"]

                        br=1
                        break
                if(br==1):
                    break


#remove Duplicate Word in tokens list
    def removeduplicate(self):
        self.tokens=list(dict.fromkeys(self.tokens))



#Searching Response from the queries list and save to answer variable
    def searchresponse(self):
        for query in self.querieslst:
            for matchlst in query["match"]:
                matched=0
                for match in matchlst:
                    for token in self.tokens:
                        if(token==match):
                            matched+=1
                if(matched>=len(matchlst)):
                    self.answer=random.choice(query["res"])
                    return


#Print answer to the screen
    def printanswer(self):
        print("BOT:",self.answer)

#Return answer
    def getanswer(self):
        return self.answer