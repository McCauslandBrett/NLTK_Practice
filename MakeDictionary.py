#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:43:48 2019

@author: Brettmccausland
"""

def make_dictionary(inpath,outpath):
  dict_mega={}
  
  ## add words corpus  
  for w in words.words():
      dict_mega[w]=w

  ## add additional corpus
  #path = inpath + "/*.txt"
  #files = glob.glob(path)
  for files in inpath:
   path = "ExtraCorpus/" + files 
   print(path)
   files = glob.glob(path)
   for fname in files:
    with open(fname) as f: #file
      for line in f:
          print(line)
          dict_mega[line]=line

 ## save
  out = open(outpath + ".txt", "w")
  for w in dict_mega:
    out.write(w)
    out.write("\n")
  out.close()
  # for loading filesnames
def getfilenames():
  names = []
  spath = "files/filenames.txt"
  files = glob.glob(spath)
  for fname in files:
    with open(fname) as f: #file
      for line in f:
          
          names.append(line.strip())
  return names