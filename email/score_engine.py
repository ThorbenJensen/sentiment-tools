# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 21:45:39 2016

@author: Thorben Jensen
"""

import sqlite3 as lite
import pandas as pd

class Engine(): 
    
    # initializes Score engine from dictionary in SQLite database
    def __init__(self):      
        # load dictionary
        db = '../dict/dictionary_german.sqlite'
        con = lite.connect(db)
        self.dict = pd.read_sql("SELECT * FROM dict", con)
        con.close()
        # format dictionary
        self.dict['word'] = self.dict['word'].str.lower()
        self.dict = self.dict.set_index('word').drop('index', 1).sort_index()

    # scores a word from dictionary (which has lower case words)
    def score_word(self, word):
        if word in self.dict.index:
            return self.dict.loc[word].score
        else: 
            return 0
    # scores a list of words
    def score_list(self, text, method='sum'):
        score = 0
        for word in text:
            score += self.score_word(word)
#        if method == 'normalized':
#            score = score / len(text)            
        return score
