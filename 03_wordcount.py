#!/usr/bin/python
#PERFORMED BY: alexxa
#DATE: 19.12.2013
#SOURCE: Google Python course 
# https://developers.google.com/edu/python/
#PURPOSE: Basics.

# The original course and exercises are in Python 2.4
# But I performed them in Python 3


# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys, string

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.

def del_punctuation(item):
    '''
        This function deletes punctuation from a word.
    '''
    punctuation = string.punctuation
    for c in item:
        if c in punctuation:
            item = item.replace(c, '')
    return item 

def dictionary(words_list):
    d = dict()
    for c in words_list:
        d[c] = d.get(c, words_list.count(c))
        print(c, d[c])
    d.pop('', None)
    return d

def break_into_words(filename):
    '''
        This function reads file, breaks it into 
        a list of used words in lower case.
    '''
    book = open(filename)
    words_list = []
    for line in book:
        for item in line.split():
            item = del_punctuation(item)
            item = item.lower()
            words_list.append(item)
    return words_list

    
def print_top(filename):
    '''
        This function returns the 20 most
         frequently-used words in the book
    '''
    words_list = break_into_words(filename)
    d = dictionary(words_list)    
    print(d)
    dict_copy = d
    counter = 0
    while counter < 20 :
        popular_word = max(dict_copy, key=dict_copy.get)
        print(popular_word, dict_copy[popular_word])
        dict_copy.pop(popular_word, None)
        counter += 1

print_top('alice.txt')
