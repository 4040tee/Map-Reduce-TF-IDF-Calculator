#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_file = None
current_count = 0
current_size = 0
file_count_dict = {}
sizes = {}
current_num_docs = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, file, count, num_docs = line.split('\t', 3)
    #print('iteration: ',word,'\t',file,'\t',count,'\t',num_docs)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
            file_count_dict[file] = count
        
    else:
        if current_word and current_file:
            # write result to STDOUT
            #print(current_word, '\t',file_count_dict,'\t',num_docs,'\t',len(file_count_dict))
            for key in file_count_dict:    
                print(current_word, '\t',key,'\t',file_count_dict[key],'\t',num_docs,'\t',len(file_count_dict))
        current_count = count
        current_word = word
        current_file = file
        current_num_docs = num_docs
        file_count_dict = {}
        file_count_dict[current_file] = current_count
        

# do not forget to output the last word if needed!
if current_word == word and current_file == file:
    file_count_dict = {}
    file_count_dict[file] = count
    for key in file_count_dict:    
                print(current_word, '\t',key,'\t',file_count_dict[key],'\t',num_docs,'\t',len(file_count_dict))
    #print(current_word, '\t',file_count_dict,'\t',num_docs,'\t',len(file_count_dict))