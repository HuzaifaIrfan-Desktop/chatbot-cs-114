from bot import bot

import json
import random

from colorama import Fore



class cpp_bot(bot):
    
    def __init__(self,filename):
        self.fname=filename
        with open(self.fname) as dbfile:
            self.db = json.load(dbfile)

        self.synonymslst=self.db["synonyms"]
        self.querieslst=self.db["queries"]
        self.inp=""
        self.tokens=[]
        self.answer=""


    def printanswer(self):
        print(Fore.YELLOW+"CPP_Bot: "+Fore.GREEN+self.answer+Fore.RESET)



