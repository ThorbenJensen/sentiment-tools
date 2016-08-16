# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 14:38:21 2016

@author: Thorben Jensen
"""

import score_engine
import email
import re

def eml_to_str(textfile):
    message = email.message_from_file(open(textfile))
    return message.get_payload()

def str_to_wordlist(string):
    string = re.sub("([^\w])|(\d)", " ",  str(string))
    string = re.sub('\s{2,}', " ",  string)
    wordlist = string.split()
    wordlist = list(map(lambda x: x.lower(), wordlist))
    return wordlist
    
def score_email(textfile, method = 'normalized'):
    string = eml_to_str(textfile)
    wordlist = str_to_wordlist(string)
    engine = score_engine.Engine()
    score = engine.score_list(wordlist, method)
    return score

#print(score_email('../data/test3.eml', 'sum'))

