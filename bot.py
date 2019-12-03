import nltk
from nltk.tokenize import word_tokenize
from colorama import Fore

import json
import random




class bot:


    def __init__(self):
        self.fname=""
        with open(self.fname) as dbfile:
            self.db = json.load(dbfile)
        self.synonymslst=self.db["synonyms"]
        self.querieslst=self.db["queries"]
        self.inp=""
        self.tokens=[]
        self.answer=""

    def setup(self):
        print(Fore.YELLOW)
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
        print(Fore.RESET,end="")

    def getinput(self):
        self.inp =input("\nYOU: ").lower()

    def setinput(self,inp):
        self.inp =inp.lower()

    def tokenize(self):
        self.tokens = word_tokenize(self.inp)

    def printtokens(self):
        print(self.tokens)


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

        return 404


    def printanswer(self):
        print("BOT:",self.answer)

    def getanswer(self):
        return self.answer