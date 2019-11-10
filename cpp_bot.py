from bot import bot

import json
import random

from colorama import Fore


answerfile="db/cpp.json"
e404file="db/404.json"

with open(answerfile) as cppdbs:
    cppdb = json.load(cppdbs)

class cpp_bot(bot):
    def __init__(self):
        self.synonymslst=cppdb["synonyms"]
        self.querieslst=cppdb["queries"]
        self.inp=""
        self.tokens=[]
        self.answer=""

        with open(e404file) as nfdb:
            self.e404 = json.load(nfdb)
        

    def printanswer(self):
        print(Fore.RED+"BOT (CPP_Bot): "+Fore.GREEN+self.answer)
