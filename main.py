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
from nltk.corpus import wordnet

import re



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
    #dict_words=loadintodictionary(words.words())
    
    for word in dict_tokens:
        if word not in allwords:
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
          line=re.sub('[^A-Za-z]+',' ', line)
          line_tokens = nltk.word_tokenize(line)
          #for eachtoken in line_tokens:
              #tokens = tokens + eachtoken.strip().split("-")
          tokens= tokens + line_tokens
  
  return tokens



# for loading mobydick tokens into python dictionary  
def loadintodictionary(text):
    dict_words = {}
    for word in text:
        w = word.lower()
        if w not in stop_words:
            dict_words[w]= w
    return dict_words
    
def line_proc(line):
    return nltk.word_tokenize(line)
  
def driver_stripsplit(txt):
    re.sub('[^A-Za-z0-9]+',' ', txt)
    print(txt)

def getDictionary(fname):
    dict_words = {}
    text= open(fname,"r")
    for word in text:
        dict_words[word]=word
    return dict_words
  
def main():
    
 #driver_spellchecker()
 #inpath= "ExtraCorpus"
 #outpath = "f"
 #names=[]
 #names = getfilenames()
 #print(names)
 #make_dictionary(names,outpath)
 #txt = "sand-hills"
 #driver_stripsplit(txt)
 dict_words = {}
 fname = "dictionary.txt"
 dict_words = getDictionary(fname)
 
 
 
if __name__ == "__main__":
    main()      
        