#!/usr/bin/env python
"""mapper.py"""

from operator import itemgetter
import sys
import math

current_word = None
current_file = None
current_count = 0
word = None
current_sum = 0
current_num_docs = 0
current_dft = 0

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    word,file,count,num_docs,dft = line.split('\t',4)
    
    try:
        count = int(count)
        num_docs = int(num_docs)
        dft = int(dft)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    current_count = count
    current_word = word
    current_file = file
    current_num_docs = num_docs
    current_dft = dft
    #print('idf = ',current_num_docs,'/', current_dft)
    current_idf = math.log(current_num_docs / current_dft,10)
    
        
    
    print(current_file, '\t', current_word, '\t', current_count,'\t', current_idf)
