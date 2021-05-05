#!/usr/bin/env python
"""mapper.py"""

from operator import itemgetter
import sys
import math

current_word = None
current_file = None
current_count = 0
word = None
current_doc_size = 0
current_tf = 0
current_tf_idf = 0


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    word,file,count,idf,doc_size = line.split('\t',4)
    
    try:
        count = int(count)
        idf = float(idf)
        doc_size = int(doc_size)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    current_word = word
    current_file = file
    
    current_count = count
    current_doc_size = doc_size
    
    current_tf = current_count / current_doc_size
    
    current_idf = idf
    
    current_tf_idf = current_tf * current_idf
    
    
    print('((' + current_word.strip() + ', ' + current_file.strip() + '), ' + str(current_tf) + ', ' + str(current_idf) + ', ' + str(current_tf_idf) + ')')
