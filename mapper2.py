#!/usr/bin/env python
"""mapper.py"""

from operator import itemgetter
import sys

current_word = None
current_file = None
current_count = 0
word = None
current_sum = 0
current_num_docs = 0
current_idf = 0
doc_size_dict = {}
output_dict = {}

# input comes from STDIN (standard input)
for line in sys.stdin:
    
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    file,word,count,idf = line.split('\t',3)
    #print('iteration: ',file,word,count,idf)
    
    try:
        count = int(count)
        idf = float(idf)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
        
    if current_file == file:
        #print(current_file)
        doc_size_dict[current_file] += count
        
    else:
        doc_size_dict[file] = count
        
    current_count = count
    current_word = word
    current_file = file
    current_idf = idf
    
    output_dict[current_word,current_file] = current_word +'\t' + current_file + '\t' + str(current_count) + '\t' + str(current_idf)
    
    
    #print(current_file, '\t', current_word,'\t',current_count,'\t', current_idf)
for word,file in output_dict:
    print(output_dict[word,file] + '\t' + str(doc_size_dict[file]))
