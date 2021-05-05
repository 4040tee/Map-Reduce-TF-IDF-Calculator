#!/usr/bin/env python
  
path = 'C:\\Users\\tabis\\Documents\\CS4417\\Assignment2\\testfiles'

#The glob finds all the pathnames matching a specified pattern according to the rules used by the Unix shell

import glob


file_list= list()

#The glob function  returns a list of files in a directory matching a pattern

directory_name = glob.glob(path+"/*")
for file in directory_name:
   file_list.append(file)
num_docs = len(file_list)
   
#for each file, the lines are printed out

for file in file_list:
  fp = open(file)
  doc_size = 0
  for line in fp: 
    words = line.split()
    doc_size += len(words)
    for word in words:
       print (word,"\t",file.split('\\')[-1],"\t", 1, '\t', num_docs)
