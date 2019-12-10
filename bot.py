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





class bot:


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

    def setup(self):
        nltk.download('punkt')

    def checkquit(self):
        for token in self.tokens:
            if(token=="quit"):
                return False
        return True

    def reset(self):
        self.inp=""
        self.tokens=[]
        self.answer=""

    def getinput(self):
        self.inp =input("\nYOU: ").lower()

    def setinput(self,inp):
        self.inp =inp.lower()

    def tokenize(self):
        self.tokens = word_tokenize(self.inp)

    def split(self):
        whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ+')
        self.inp=''.join(filter(whitelist.__contains__, self.inp))
        self.tokens = self.inp.split()

    def printtokens(self):
        print(self.tokens)

    def returntokens(self):
        return self.tokens


    def similartokens(self):
        temptokens=self.tokens
        for word in self.tokens:
            for synonym in self.synonymslst:
                br=0
                for keyword in synonym["keywords"]:
                    if(keyword==word):

                        temptokens[int(temptokens.index(keyword))]=synonym["tag"]

                        br=1
                        break
                if(br==1):
                    break
        self.tokens=temptokens


    def removeduplicate(self):
        self.tokens=list(dict.fromkeys(self.tokens))


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
                    return 0
        return 0


    def printanswer(self):
        print("BOT:",self.answer)

    def getanswer(self):
        return self.answer