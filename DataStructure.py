#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:49:08 2019

@author: Brettmccausland
"""
alphbet="abcdefghijklmnopqrstuv"
class DFA:
    def __init__(self):
        self.start ={}

        
    def insert(self,dict_o, substr):
        print("inside dictionary",substr)
        if substr == '':
            dict_o['']= 'ACCEPTING'
            return
        else:
            c = substr[0] # get first character
            substr = substr[1:] # remove first character
            if c in dict_o: # get c dictonary and go 1 layer deeper
                dict_edge = dict_o[c]
                self.insert(dict_edge,substr,value)
            else: # need to create a new dictionary and continue
                dict_new = {}   # building sub dictionarys
                dict_o[c]=dict_new
                self.insert(dict_o[c],substr,value)
    
    def insert_dict(self,dict_o, dict_words):
       for all_words in dict_words:
           gg=1
    
    def suggestions(self, dict_o, encodeing, substr,edits):
       # print(substr,edits)
      
        if edits == len(value):
            return
        if substr == '':
          if '' in dict_o:
              return (edits, encodeing)
          else: return
        
        allresults=[]
        # check with c
        edge = substr[0]
        encodeing = encodeing + substr[0] 
        substr = substr[1:] # remove first character
        if edge in dict_o: # get c dictonary and go 1 layer deeper
            allresults.append(self.suggestions(dict_o[c],encodeing+c,substr,value,edits))
                # check without c
        allresults.append(self.suggestions(dict_o,substr,value,edits+1))
        for c in dict_o:
            allresults.append(self.suggestions(dict_o[c],substr,value,edits+1))
            
        return allresults       

g = DFA()
g.insert(g.start, "string")
results=[]
reults=g.suggestions(g.start, "","string",0)
print(results)

## suggestions