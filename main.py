#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 14:20:46 2019

@author: Brettmccausland
"""
import numpy as np
import pandas as pd
import urllib.request
import urllib
import pandas as pd
from collections import namedtuple
import pandas as pd
import glob
import nltk

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords 
from nltk.corpus import words



stop_words = set(stopwords.words('english')) 
from PyDictionary import PyDictionary
dictionary = PyDictionary()
ps = PorterStemmer()


def driver_tokenize():
 path = "mobydick"
 tokens = tokenize(path)
 print(tokens)


def driver_spellchecker():
 dict_tokens={}
 path = "mobydick"
 tokens = tokenize(path)
 dict_tokens = loadintodictionary(tokens)
 spell_checker(dict_tokens)

# precondition: 
    #python Dictionary has been loaded 
    #text is a tokenized list of words
#postconition: Returns list of misspelled words
def spell_checker(dict_tokens):
    misspelled = []
    dict_words = {}
    dict_words=loadintodictionary(words.words())
    
    for word in dict_tokens:
        if word not in dict_words:
            misspelled.append(word)
    print(misspelled)
    return misspelled

def tokenize(path):
  tokens=[]
  spath = path + ".txt"
  files = glob.glob(spath)
  for fname in files:
    with open(fname) as f: #file
      for line in f:
         tokens= tokens + nltk.word_tokenize(line)
  
  return tokens

def loadintodictionary(text):
    dict_words = {}
    for word in text:
        w = word.lower()
        if w not in stop_words:
            dict_words[w]= w
    return dict_words
    

def main():
    
 driver_spellchecker()

 
 
 
if __name__ == "__main__":
    main()      
        