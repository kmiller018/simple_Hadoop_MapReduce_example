#!/usr/bin/env python
import sys
import string
import nltk
from nltk.corpus import stopwords

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    #make lowercase
    line = line.lower()
    
    #remove punctuation
    line = line.translate(None, string.punctuation)

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    stop_words = set(stopwords.words('english'))
    
    for word in words:
        for word not in stop_words:
            print '%s\t%s' % (word, "1")
